from model import connect_to_db, db
 
TREE_DICT = {
                 'Platanus x hispanica ': {'common_name': 'Sycamore: London Plane', 'lat': '37.7776435713687', 'lon': '-122.416171839707'}, 
                 'Metrosideros excelsa ': {'common_name': 'New Zealand Xmas Tree', 'lat': '37.7159856948639', 'lon': '-122.478342532492'}, 
                 'Lophostemon confertus ': {'common_name': 'Brisbane Box', 'lat': '37.7662509163514', 'lon': '-122.464348446646'}, 
                 'Pittosporum undulatum ': {'common_name': 'Victorian Box', 'lat': '37.7639964041248', 'lon': '-122.468487066847'}, 
                 'Tristaniopsis laurina ': {'common_name': 'Swamp Myrtle', 'lat': '37.7309323858205', 'lon': '-122.436517937945'}, 
                 'Prunus cerasifera ': {'common_name': 'Cherry Plum', 'lat': '37.7390053040631', 'lon': '-122.424668946839'}, 
                 'Magnolia grandiflora ': {'common_name': 'Southern Magnolia', 'lat': '37.7577074184489', 'lon': '-122.384568876102'}, 
                 "Ficus microcarpa nitida 'Green Gem' ": {'common_name': "Indian Laurel Fig Tree 'Green Gem'", 'lat': '37.777476320014', 'lon': '-122.404479121929'}, 
                 "Arbutus 'Marina' ": {'common_name': 'Hybrid Strawberry Tree', 'lat': '37.7523340257173', 'lon': '-122.473048745206'}, 
                 "Prunus serrulata 'Kwanzan' ": {'common_name': 'Kwanzan Flowering Cherry', 'lat': '37.7552838973381', 'lon': '-122.469226308173'}
            }



for data in TREE_DICT:
    data = Tree(sci_name = data, common_name = data['common_name'])

for data in TREE_DICT:
    data = Location(lat=data['lat'], lon = data['lon'])

if __name__=="__main__":
    connect_to_db(app)

    db.create_all()


