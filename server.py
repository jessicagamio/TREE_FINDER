import os
from jinja2 import StrictUndefined
from flask import Flask, render_template, request, flash, redirect, session, url_for
from flask_debugtoolbar import DebugToolbarExtension
from werkzeug.utils import secure_filename
from model import connect_to_db, db, Tree, TreeSpecies
from obj_detect import predict_model

UPLOAD_FOLDER = '/uploads' # location of uploaded images
ALLOWED_EXTENSIONS = {'jpg','png','jpeg'}

app = Flask(__name__)
app.secret_key="ABC"
app.jinja_env.undefined = StrictUndefined
app.config['UPLOAD_FOLDER'] = '/home/vagrant/src/TREE_FINDER/static/img/uploads'


def allowed_file(filename):
    """checks if extension is valid"""

    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def tree_facts(results):
    """Query Tree species information"""
    tree_dict={
                'platanus':'Platanus x hispanica',
                'prunus': 'Prunus cerasifera',
                'magnolia':'Magnolia grandiflora'
                }

    name, value = results[0]
    sci_name = tree_dict[name]

    tree = TreeSpecies.query.filter(sci_name==sci_name).first()

    facts = (tree.sci_name,
            tree.common_name,
            tree.shape,
            tree.factoid,
            tree.margin,
            tree.venation, 
            tree.image)
    
    return facts


@app.route('/')
def index():
    """Homepage"""

    return render_template("homepage.html")


@app.route('/upload', methods=['GET','POST'])
def upload_image():
    """upload image from site"""

    if request.method == 'POST':

        if 'upload' not in request.files:
            flash('No file part')
            return redirect(request.url)
     
        image = request.files['upload']

        if image.filename == '':
            flash('No selected file')
            return redirect(reqest.url)
        if image and allowed_file(image.filename):
            filename=secure_filename(image.filename)
            image.save(os.path.join(app.config["UPLOAD_FOLDER"], image.filename))
            path = os.path.join(app.config["UPLOAD_FOLDER"], image.filename)
        
    results = predict_model(path)

    name,value = results[0]

    sci_name, common_name, shape, factoid, margin, venation, image = tree_facts(results)

    return render_template("prediction.html", 
                            value= value,
                            sci_name=sci_name,
                            common_name=common_name,
                            shape= shape,
                            factoid=factoid,
                            margin=margin,
                            venation=venation,
                            image=image )


if __name__ == "__main__":
    app.debug = True

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")