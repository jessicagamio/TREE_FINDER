from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()



class Tree(db.Model):
    """ Trees """
    __table__ = 'trees'

    tree_id = db.Column( db.Integer, primary_key = True, autoincrement = True)
    sci_name = db.Column(db.String(), nullable = False)
    common_name = db.Column(db.String(), nullable = False)
    # factoid = db.Column (db.String(), nullable= False)
    # margin = db.Column(db.String(), nullable = False) 
    # venation = db.Column(db.String(), nullable = True)
    # image = db. Column(db.String(), nullable = False)
    
    def __repr__(self):
        """show leaf name and main categories"""

        return f"<Tree tree_id={self.tree_id} common_name={self.common_name} single_leaf={self.single_leaf}>"

    
class Location(db.Model):
    """Data SF tree location"""

    __table__ = 'location'

    lat = db.Column(db.Float, primary_key = True, nullable = False)
    lon = db.Column(db.Float, primary_key = True, nullable = False)
    tree_id = db.Column(db.Integer, db.ForiegnKey('trees'), primary_key = True)

    def __repr__(self):
        """ Show tree id an Lat/Lon """

        return f"<Location tree_id={self.tree_id} lat={self.lat} lon={self.lon}>"

db.create_all()

def connect_to_db(app, db_name):
    """Connect to database"""

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///trees'
    app.config['SQLALCHEMY_ECHO'] = True
    db.app = app
    db.init_app(app)
