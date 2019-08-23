import os
from jinja2 import StrictUndefined
from flask import Flask, render_template, request, flash, redirect, session, url_for
from flask_debugtoolbar import DebugToolbarExtension
from werkzeug.utils import secure_filename
from model import connect_to_db, db, Tree, TreeSpecies
from obj_detect import predict_model
from data import tree_facts

UPLOAD_FOLDER = '/uploads' # location of uploaded images
ALLOWED_EXTENSIONS = {'jpg','png','jpeg'}

app = Flask(__name__)
FLASK_TOKEN = os.environ.get('FLASK_TOKEN')
app.secret_key=FLASK_TOKEN
app.jinja_env.undefined = StrictUndefined
# app.config['UPLOAD_FOLDER'] = 'static/img/uploads'
app.config['UPLOAD_FOLDER'] = '/home/vagrant/src/TREE_FINDER/static/img/uploads'


def allowed_file(filename):
    """checks if extension is valid"""

    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    """Homepage"""

    return render_template("homepage.html")


@app.route('/upload', methods=['POST'])
def upload_image():
    """upload image from site"""

    if 'upload' not in request.files:
        flash('No file part')
        return redirect('/')

    image = request.files['upload']

    if image.filename == '':
        flash('No File Selected')
        return redirect('/')

    if not allowed_file(image.filename):
        flash ('Must be a jpg or png file.')
        return redirect('/')

    if image and allowed_file(image.filename):
        filename=secure_filename(image.filename)
        image.save(os.path.join(app.config["UPLOAD_FOLDER"], image.filename))
        path = os.path.join(app.config["UPLOAD_FOLDER"], image.filename)
            
        results = predict_model(path) # predict tree from uploaded image in clarifai

        print('=======>', results)
        
        os.remove(path)
        
        if results == []:
            value = 0
            return render_template("prediction.html", value=value)

        #if results are not empty do th follwoing
        
        elif results:
            name,value = results[0] # unpack the concept with the highest value from clarifai

            sci_name, common_name, shape, factoid, margin, venation, image = tree_facts(name)

            """call a function that queries through trees table using
                sci_name to get all lat lon of the tree species 
                gather all lat lons in a list
                and iterate through
             """
            return render_template("prediction.html", 
                                    value= value,
                                    sci_name=sci_name,
                                    common_name=common_name,
                                    shape= shape,
                                    factoid=factoid,
                                    margin=margin,
                                    venation=venation,
                                    image=image )
        

        flash('something weird happened ')
        redirect('/')


if __name__ == "__main__":
    app.debug = True

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")