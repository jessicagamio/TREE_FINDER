
from sqlalchemy import func
from model import TreeSpecies,Tree,connect_to_db, db
from server import app
import json

TREE_DATA = "trees_sf/rows.json"

trees_json = open(TREE_DATA).read()

tree_info = json.loads(trees_json)

entries = tree_info['data'].__len__()

# create an empty TREE_TYPE_DICT
TREE_LIST = []
i=0

while i < entries:

    tree_type =tree_info['data'][i][10]

    # split out the scientific and common name from data
    scientific_name, common_name = tree_type.split('::')
    scientific_name = scientific_name.strip()
    common_name = common_name.strip()

    latitude = tree_info['data'][i][23]
    longitude = tree_info['data'][i][24] 

   
    if latitude == None and longitude==None:
        pass
        
    if tree_type == 'Tree(s) ::':
        pass

    if scientific_name == 'Platanus x hispanica':
        shape = 'palmate'
        margin = 'entire'
        venation = 'pinnate'
        factoid = 'Dicidous Tree. Bare through November-March. Member of the Sycamore Family'
        image = '/static/img/platanus_x_hispanica.jpg'

    if scientific_name == 'Magnolia grandiflora':
        shape = 'obtuse'
        margin = 'entire'
        venation = 'pinnate'
        factoid = 'facts'
        image = 'an_image'

    if scientific_name == 'Prunus cerasifera':
        shape = 'obtuse'
        margin = 'serrated'
        venation = 'venation'
        factoid = 'facts'
        image = 'an_image'

    if scientific_name == 'Tristaniopsis laurina':
        shape = 'obtuse'
        margin = 'entire'
        venation = 'venation'
        factoid = 'facts'
        image = 'an_image'
        
    if scientific_name == "Ficus microcarpa nitida 'Green Gem'":
        shape = 'obtuse'
        margin = 'entire'
        venation = 'pinnate'
        factoid = 'facts'
        image = 'an_image'

    if scientific_name == 'Platanus x hispanica' or scientific_name=='Magnolia grandiflora' or scientific_name=='Prunus cerasifera' or scientific_name=='Tristaniopsis laurina' or scientific_name=="Ficus microcarpa nitida 'Green Gem'": 
        print(scientific_name)       
        species = TreeSpecies(sci_name=scientific_name, 
            common_name=common_name,
            shape=shape, 
            factoid=factoid, 
            margin=margin, 
            venation=venation, 
            image=image)

        tree = Tree(lat= float(latitude), lon= float(longitude))

        db.session.add(species, tree)

    i+=1

db.session.commit()

if __name__ == "__main__":
    connect_to_db(app)
    db.create_all()


