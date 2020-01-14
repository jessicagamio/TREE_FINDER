from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_to_db(app,dbname='trees'):
    """Connect to database"""

    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql:///{dbname}'
    app.config['SQLALCHEMY_ECHO'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)
    db.create_all()

    print('Connected to db!')


if __name__ == '__main__':

    from server import app
    connect_to_db(app)


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
    venation = db.Column(db.String, nullable=False)
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



class User(db.Model):
    """Create User"""

    __tablename__ = 'user'

    user_id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    username=db.Column(db.String, nullable=False)
    password=db.Column(db.String, nullable=False)
    firstname=db.Column(db.String, nullable=False)
    lastname=db.Column(db.String, nullable=False)

    hugged_trees = db.relationship('TreeSpecies', secondary='hugs', backref='users_hugged')

    def __repr__(self):
        """ Show user information """

        return f"<User user_id={self.user_id}, password={self.password}, username={self.username}>"


class Hugs(db.Model):
    """Create Tree Hugs Table"""

    __tablename__="hugs"

    hug_id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id=db.Column(db.Integer,
                        db.ForeignKey('user.user_id'))
    
    tree_species_id=db.Column(db.Integer, 
                                db.ForeignKey('tree_species.tree_species_id'))



def example_data():
    """Creating sample data for user"""
    User.query.delete()

    Merry=User(username='Merry', firstname='Meridock', lastname='Bramdybuck', password='lord')
    Arwen=User(username='Arwen', firstname = 'Arwen', lastname='Evenstar', password='Aragorn')
    db.session.add(Merry)
    db.session.add(Arwen)
    db.session.commit()

