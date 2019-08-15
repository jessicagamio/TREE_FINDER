from model import connect_to_db, db
 
# TREE_DICT = {
#                  'Platanus x hispanica ': {'common_name': 'Sycamore: London Plane', 'lat': '37.7776435713687', 'lon': '-122.416171839707'}, 
#                  'Metrosideros excelsa ': {'common_name': 'New Zealand Xmas Tree', 'lat': '37.7159856948639', 'lon': '-122.478342532492'}, 
#                  'Lophostemon confertus ': {'common_name': 'Brisbane Box', 'lat': '37.7662509163514', 'lon': '-122.464348446646'}, 
#                  'Pittosporum undulatum ': {'common_name': 'Victorian Box', 'lat': '37.7639964041248', 'lon': '-122.468487066847'}, 
#                  'Tristaniopsis laurina ': {'common_name': 'Swamp Myrtle', 'lat': '37.7309323858205', 'lon': '-122.436517937945'}, 
#                  'Prunus cerasifera ': {'common_name': 'Cherry Plum', 'lat': '37.7390053040631', 'lon': '-122.424668946839'}, 
#                  'Magnolia grandiflora ': {'common_name': 'Southern Magnolia', 'lat': '37.7577074184489', 'lon': '-122.384568876102'}, 
#                  "Ficus microcarpa nitida 'Green Gem' ": {'common_name': "Indian Laurel Fig Tree 'Green Gem'", 'lat': '37.777476320014', 'lon': '-122.404479121929'}, 
#                  "Arbutus 'Marina' ": {'common_name': 'Hybrid Strawberry Tree', 'lat': '37.7523340257173', 'lon': '-122.473048745206'}, 
#                  "Prunus serrulata 'Kwanzan' ": {'common_name': 'Kwanzan Flowering Cherry', 'lat': '37.7552838973381', 'lon': '-122.469226308173'}
#             }


import json
from pprint import pprint

TREE_DATA = "trees_sf/rows.json"
trees_json = open(TREE_DATA).read()

tree_info = json.loads(trees_json)

# entries = tree_info['data'].__len__()

# create an empty TREE_TYPE_DICT
TREE_DICT = {}
for info in tree_info:
    tree_type =tree_info['data'][i][10]
      # split out the scientific and common name from data
    scientific_name, common_name = tree_type.split('::')
    scientific = scientific_name.rstrip()
    common_name = common_name.lstrip() 

        if scientific_name in TREE_DICT:
            count = 1
        if scientific_name == 'Platanus x hispanica ':
            shape = 'palmate'
            margin = 'entire'
            venation = 'palmate'
            factiod = 'Dicidous Tree. Bare through November-March. Member of the Sycamore Family'
            image = 'static\img\platanus_x_hispanica.jpg'   

    # extract scientific name
        #if name is new
            # add an additional key count:0
        #if name is not new
            # incriment count by one
        # if name is Platanus x hispanica
            # add  this additional information
                # shape: palmate
                # margin : entire
                # venation : pinnate
                # factoid : Dicidous Tree. Bare through November-March. Member of the Sycamore Family.
                # image: 'img\platanus_x_hispanica.jpg'
        # if name is Magnolia Grandiflora
            # add this additional information
                # shape = obtuse
                # margin = entire
                # venation = 
    # extract common name 

    # add to TREE_DICT[scientific names] = {common name, shape, margin, venation}


for data in TREE_DICT:
    data = Tree(sci_name = data, common_name = data['common_name'])

#create TREE_LOCATION_DICT

# iterate through json file
    # latitude = tree_info['data'][i][23]
    # longitude = tree_info['data'][i][24]
    # add data to Location table


for data in TREE_DICT:
    data = Location(lat=data['lat'], lon = data['lon'])

if __name__=="__main__":
    connect_to_db(app)

    db.create_all()


