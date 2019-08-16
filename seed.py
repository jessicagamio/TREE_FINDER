
from sqlalchemy import func
from model import TreeSpecies,Tree,connect_to_db, db
from server import app
import json

if __name__ == "__main__":
    connect_to_db(app)
    db.create_all()



TREE_DATA = "trees_sf/rows.json"

trees_json = open(TREE_DATA).read()

tree_info = json.loads(trees_json)

entries = tree_info['data'].__len__()

# create an empty TREE_TYPE_DICT
TREE_LIST = []
i=0

for i in range(entries):

    tree_type =tree_info['data'][i][10]

    # split out the scientific and common name from data
    scientific_name, common_name = tree_type.split('::')
    scientific_name = scientific_name.strip()
    common_name = common_name.strip()

    latitude = tree_info['data'][i][23]
    longitude = tree_info['data'][i][24] 

    # print(latitude, longitude)
    if tree_type == 'Tree(s) ::' or latitude == None or longitude == None or scientific_name not in ['Platanus x hispanica','Magnolia grandiflora','Prunus cerasifera','Tristaniopsis laurina',"Ficus microcarpa nitida 'Green Gem'"]:
        # print('detected a none', latitude, longitude)
        continue
        
    # if tree_type == 'Tree(s) ::' or scientific_name not in ['Platanus x hispanica','Magnolia grandiflora','Prunus cerasifera','Tristaniopsis laurina',"Ficus microcarpa nitida 'Green Gem'"]:
    #     print('not test tree ===>',scientific_name)
    #     continue

    else:
        print('test tree', scientific_name, 'lat', latitude, 'lon', longitude)
        if scientific_name == 'Platanus x hispanica':
            shape = 'palmate'
            margin = 'entire'
            venation = 'pinnate'
            factoid = 'Dicidous Tree. Bare through November-March. Member of the Sycamore Family'
            image = '/static/img/platanus_x_hispanica.jpg'

        elif scientific_name == 'Magnolia grandiflora':
            shape = 'obtuse'
            margin = 'entire'
            venation = 'pinnate'
            factoid = 'facts'
            image = 'an_image'

        elif scientific_name == 'Prunus cerasifera':
            shape = 'obtuse'
            margin = 'serrated'
            venation = 'venation'
            factoid = 'facts'
            image = 'an_image'

        elif scientific_name == 'Tristaniopsis laurina':
            shape = 'obtuse'
            margin = 'entire'
            venation = 'venation'
            factoid = 'facts'
            image = 'an_image'
            
        elif scientific_name == "Ficus microcarpa nitida 'Green Gem'":
            shape = 'obtuse'
            margin = 'entire'
            venation = 'pinnate'
            factoid = 'facts'
            image = 'an_image'

        if scientific_name == 'Platanus x hispanica' or scientific_name=='Magnolia grandiflora' or scientific_name=='Prunus cerasifera' or scientific_name=='Tristaniopsis laurina' or scientific_name=="Ficus microcarpa nitida 'Green Gem'":       
            species = TreeSpecies(sci_name=scientific_name, 
                common_name=common_name,
                shape=shape, 
                factoid=factoid, 
                margin=margin, 
                venation=venation, 
                image=image)

            tree = Tree(lat= float(latitude), lon= float(longitude))

            db.session.add(species, tree)

    # i+=1

db.session.commit()



