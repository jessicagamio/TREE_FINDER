import os
from jinja2 import StrictUndefined
from flask import Flask, render_template, request, flash, redirect, session, url_for
from flask_debugtoolbar import DebugToolbarExtension
from werkzeug.utils import secure_filename
from model import connect_to_db, db, Tree, TreeSpecies, User, Hugs
from obj_detect import predict_model
from data import tree_facts

UPLOAD_FOLDER = '/uploads' # location of uploaded images
ALLOWED_EXTENSIONS = {'jpg','png','jpeg'}

app = Flask(__name__)
FLASK_TOKEN = os.environ.get('FLASK_TOKEN')
app.secret_key=FLASK_TOKEN
app.jinja_env.undefined = StrictUndefined
app.config['UPLOAD_FOLDER'] = os.environ.get('UPLOAD_TOKEN')


def allowed_file(filename):
    """checks if extension is valid"""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    """Homepage"""
    
    return render_template("homepage.html")

@app.route('/processlogin', methods=['POST'])
def process_login():
    """log into dash"""

    user_name=request.form['username']
    password=request.form['password']

    entered_username=User.query.filter(User.username==user_name).count()
    entered_password=User.query.filter(User.password==password).count()
    
    if entered_username and entered_password:
        user = User.query.filter(User.username == user_name).first()
        user_id = user.user_id
        session['user_id'] = user_id

        flash(f'{user_name} is logged in.')

        return redirect('/')


    else:
        flash('Not a valid username or password')
        return redirect('/login')


@app.route('/dashboard')
def dashboard():
    """ display dashboard """

    user_id = session['user_id']

    user = User.query.filter(User.user_id==user_id).first()

    user_hugs=[tree.sci_name for tree in user.hugged_trees]

    return render_template("dashboard.html", tree_hugs=user_hugs, username=user.username)

@app.route('/dashinfo')
def dashboard_info():

    sci_name=request.args.get('getInfo')
    
    tree=TreeSpecies.query.filter(TreeSpecies.sci_name==sci_name).first()

    hugInfo={'sci_name':tree.sci_name,
                'common_name':tree.common_name,
                'tree_facts': tree.factoid,
                'image':tree.image}

    return hugInfo 



@app.route('/login')
def login():
    """log in to site"""

    return render_template("login.html")

@app.route('/logout')
def logout():
    """logout the user"""
    del session["user_id"]
    flash("Logged Out.")    
    return redirect('/')

@app.route('/register')
def register_user():
    """display registration form"""
    return render_template("register.html")


@app.route('/hugs', methods=['POST'])
def process_hug():
    """ Adds a tree hug from user """

    user_id=request.form.get('user_id')
    tree_species=request.form.get('tree_species')

    tree = TreeSpecies.query.filter(TreeSpecies.sci_name==tree_species).first()
    tree_hug = Hugs(user_id=user_id, tree_species_id = tree.tree_species_id)
    db.session.add(tree_hug)
    db.session.commit()
    return "You Hugged a Tree"


@app.route('/process_register', methods=['POST'])
def process_registration():
    """Process Registeration Form"""

    user_name=request.form['username']
    firstname=request.form['firstname']
    lastname=request.form['lastname']
    password=request.form['password']

    # if register username does NOT exist in db add username
    if User.query.filter(User.username==user_name).count():

        return redirect('/register')

    else:
        new_user=User(username=user_name, firstname=firstname, lastname=lastname, password=password)
        db.session.add(new_user)
        db.session.commit()
        new_guy=User.query.filter(User.username==user_name).first()
        return redirect('/')



@app.route('/upload', methods=['POST'])
def upload_image():
    """upload image from site"""

    if 'upload' not in request.files:
        flash('No file part')
        return redirect('/')

###########################################

    # if file was uploaded using form
    if request.files['upload']:
        image = request.files['upload']
    # else file has been sent by post request
    else:
        image = request.form.get('file') 

###############################################

    if image.filename == '':
        flash('No File Selected')
        return redirect('/')

    if not allowed_file(image.filename):
        flash ('Must be a jpg or png file.')
        return redirect('/')

    # if image is correct file type create a path to that image in upload folder
    if image and allowed_file(image.filename):
        filename=secure_filename(image.filename)
        image.save(os.path.join(app.config["UPLOAD_FOLDER"], image.filename))
        path = os.path.join(app.config["UPLOAD_FOLDER"], image.filename)
           
        #send image to clarifai 
        results = predict_model(path) # predict tree from uploaded image in clarifai

        # remove image after uploading image to claifia
        os.remove(path)
        
        if results == []:
            value = 0
            return render_template("prediction.html", value=value)
        
        elif results:
            name,value = results[0] # unpack the concept with the highest value from clarifai

            sci_name, common_name, shape, factoid, margin, venation, image = tree_facts(name)

            tree_markers=[]

            markers=TreeSpecies.query.filter(TreeSpecies.sci_name==sci_name).first()

            for marker in markers.trees:
                tree_markers.append((marker.lat, marker.lon))



            return render_template("prediction.html", 
                                    value= value,
                                    sci_name=sci_name,
                                    common_name=common_name,
                                    shape= shape,
                                    factoid=factoid,
                                    margin=margin,
                                    venation=venation,
                                    image=image,
                                    markers=tree_markers )
        

        flash('something weird happened ')
        redirect('/')


if __name__ == "__main__":
    app.debug = False

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")