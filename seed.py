
from sqlalchemy import func
from model import TreeSpecies,Tree,connect_to_db, db
from server import app
import json

if __name__ == "__main__":
    connect_to_db(app)
    db.create_all()


def create_species():
    """create tree_species table"""
    tree_species = {}

    # Create TreeSpecies
    scientific_name = 'Platanus x hispanica'
    common_name = 'London Plane'
    shape = 'palmate'
    margin = 'entire'
    venation = 'pinnate'
    factoid = 'Dicidous Tree. Bare through November-March. Member of the Sycamore Family'
    image = '/static/img/platanus_x_hispanica.jpg'
    platanus_x_hispanica = TreeSpecies(sci_name=scientific_name, 
                common_name=common_name,
                shape=shape, 
                factoid=factoid, 
                margin=margin, 
                venation=venation, 
                image=image)
    db.session.add(platanus_x_hispanica)
    db.session.commit()
    tree_species[scientific_name] = platanus_x_hispanica


    scientific_name = 'Magnolia grandiflora'
    common_name= 'Magnolia'
    shape = 'obtuse'
    margin = 'entire'
    venation = 'pinnate'
    factoid = 'Evergreen. Produces long lasting white, fragrant flowers.'
    image = '/static/img/magnolia_grandiflora.jpg'
    Magnolia_grandiflora = TreeSpecies(sci_name=scientific_name, 
                common_name=common_name,
                shape=shape, 
                factoid=factoid, 
                margin=margin, 
                venation=venation, 
                image=image)
    db.session.add(Magnolia_grandiflora)
    db.session.commit()
    tree_species[scientific_name]= Magnolia_grandiflora


    scientific_name = 'Prunus cerasifera'
    common_name = 'Purple-Leaf Plum'
    shape = 'obtuse'
    margin = 'serrated'
    venation = 'Cross Venulate'
    factoid = 'Blooms favorite flowers in the spring. Attracts bees.'
    image = '/static/img/purple_leaf_plum.jpg'
    Prunus_cerasifera = TreeSpecies(sci_name=scientific_name, 
                common_name=common_name,
                shape=shape, 
                factoid=factoid, 
                margin=margin, 
                venation=venation, 
                image=image)
    db.session.add(Prunus_cerasifera)
    db.session.commit()
    tree_species[scientific_name]= Prunus_cerasifera


    scientific_name = 'Tristaniopsis laurina'
    common_name = 'Small-Leaf Tristania'
    shape = 'lanceolate'
    margin = 'entire'
    venation = 'pinnate'
    factoid = 'Originates from Australia. Disease and pest resistant.'
    image = '/static/img/tristaniopsis.jpg'
    Tristaniopsis_laurina = TreeSpecies(sci_name=scientific_name, 
                common_name=common_name,
                shape=shape, 
                factoid=factoid, 
                margin=margin, 
                venation=venation, 
                image=image)
    db.session.add(Tristaniopsis_laurina)
    db.session.commit()
    tree_species[scientific_name]=Tristaniopsis_laurina

            
    scientific_name = 'Ginkgo biloba'
    common_name= 'Maidenhair Tree'
    shape = 'flabellate'
    margin = 'entire'
    venation = 'parallel'
    factoid = 'Can live as long as 3000 years. Leaves turn yellow in the fall.'
    image = '/static/img/ginkgo.jpg'
    Ficus_microcarpa_nitida = TreeSpecies(sci_name=scientific_name, 
                common_name=common_name,
                shape=shape, 
                factoid=factoid, 
                margin=margin, 
                venation=venation, 
                image=image)
    db.session.add(Ficus_microcarpa_nitida)
    db.session.commit()
    tree_species[scientific_name]= Ficus_microcarpa_nitida

    return tree_species

def create_trees(tree_species):
    """create trees table"""
    
    TREE_DATA = "trees_sf/rows.json"

    trees_json = open(TREE_DATA).read()

    tree_info = json.loads(trees_json)

    entries = tree_info['data'].__len__()


    for i in range(entries):

        tree_type =tree_info['data'][i][10]

        # split out the scientific and common name from data
        scientific_name, common_name = tree_type.split('::')
        scientific_name = scientific_name.strip()

        latitude = tree_info['data'][i][23]
        longitude = tree_info['data'][i][24] 

        if latitude == None or longitude == None or scientific_name not in ['Platanus x hispanica','Magnolia grandiflora','Prunus cerasifera','Tristaniopsis laurina','Ginkgo biloba']:
            continue

        tree = Tree(lat= float(latitude), lon= float(longitude), tree_species= tree_species[scientific_name])

        db.session.add(tree)

def create_user(user):
    """ Create user """

    username,password,firstname,lastname = user
    User(username=username, password=password, firstname=firstname,lastname=lastname, user=user_id)
    

def create_hugs(username, tree_species)

    
    Hugs()

tree_species = create_species()
create_trees(tree_species)
user = create_user(['jondoe','abc123', 'Jon','Doe'])
db.session.commit()



