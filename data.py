import os
from flask import Flask, render_template, request, flash, redirect, session, url_for
from flask_debugtoolbar import DebugToolbarExtension
from model import connect_to_db, db, Tree, TreeSpecies


app = Flask(__name__)
FLASK_TOKEN = os.environ.get('FLASK_TOKEN')
app.secret_key = FLASK_TOKEN

def tree_facts(name):
    """Query Tree species information"""
    tree_dict={
                'platanus':'Platanus x hispanica',
                'prunus': 'Prunus cerasifera',
                'magnolia':'Magnolia grandiflora'
                }

    sci_name = tree_dict[name]

    print('++++++++__sci_name__++++++++++++',sci_name)
    tree = TreeSpecies.query.filter(TreeSpecies.sci_name==sci_name).first()

    facts = (tree.sci_name,
            tree.common_name,
            tree.shape,
            tree.factoid,
            tree.margin,
            tree.venation, 
            tree.image)
    print('xxxxxxxxxxx__facts__xxxxxxxxxxxxxxx',facts)
    return facts



if __name__ == "__main__":
    app.debug = True

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")