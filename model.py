from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()



class TreeSpecies(db.Model):
    """ Trees """

    __tablename__ = 'tree_species'

    tree_species_id = db.Column(db.Integer,
                                primary_key=True,
                                autoincrement=True)
    sci_name = db.Column(db.String, nullable=False)
    shape = db.Column(db.String, nullable=False)
    common_name = db.Column(db.String, nullable=False)
    factoid = db.Column (db.String, nullable=False)
    margin = db.Column(db.String, nullable=False) 
    venation = db.Column(db.String, nullable=True)
    image = db. Column(db.String, nullable=False)
    
    def __repr__(self):
        """show leaf name and main categories"""

        return f"<TreeSpecies tree_id={self.tree_species_id} common_name={self.common_name}>"

    
class Tree(db.Model):
    """Data SF tree location"""

    __tablename__ = 'trees'

    tree_id = db.Column(db.Integer,
                        primary_key=True,
                        autoincrement=True)
    lat = db.Column(db.Float, nullable=False)
    lon = db.Column(db.Float, nullable=False)
    tree_species_id = db.Column(db.Integer,
                                db.ForeignKey('tree_species.tree_species_id'))

    tree_species = db.relationship('TreeSpecies', backref='trees')

    def __repr__(self):
        """ Show tree id an Lat/Lon """

        return f"<Tree tree_id={self.tree_id} lat={self.lat} lon={self.lon}>"



def connect_to_db(app):
    """Connect to database"""

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///trees'
    app.config['SQLALCHEMY_ECHO'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)

    print('Connected to db!')


if __name__ == '__main__':
    from flask import Flask
    app = Flask(__name__)

    connect_to_db(app)