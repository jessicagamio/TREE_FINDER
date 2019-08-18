from jinja2 import StrictUndefined

from flask import Flask, render_template, request, flash, redirect, session
from flask_debugtoolbar import DebugToolbarExtension

from model import connect_to_db, db, Tree, TreeSpecies

from obj_detect import predict_model

app = Flask(__name__)

app.secret_key="ABC"

app.jinja_env.undefined = StrictUndefined


@app.route('/')
def index():
    """Homepage"""

    return render_template("homepage.html")

@app.route('/get_pic')
def process_picture():
    """process picture with clarifai"""
    
    user_image = request.args.get('user_pic')

    return None


if __name__ == "__main__":
    app.debug = True

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")