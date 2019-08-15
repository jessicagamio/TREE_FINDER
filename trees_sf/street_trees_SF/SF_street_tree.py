########################### NOTES ################################

"""
TREE_DATA is a json file from the the city of San Francisco
https://data.sfgov.org/City-Infrastructure/Street-Tree-List/tkzw-k3nq

TREE DATA contains all the reported street trees of san francisco. 
This Python script removes all trees with no Lat/Lon coordinates and creates a 
list of dictionaries contiaining the Tree type, LAT, LON.

Objective is to use this data to create a map of trees in the SF area that will 
allow user to identify a tree by their location instead of the image classifier.

This is a "Nice to Have" feature for the Tree Classifier App Project.
"""

#######################################################################


import json
from pprint import pprint

TREE_DATA = "rows.json"
trees_json = open(TREE_DATA).read()

tree_info = json.loads(trees_json)

entries = tree_info['data'].__len__()


"""create empty list of dictionaries"""
TREE_LIST = []

"""iterate through dictionary list and append data as a dict to TREE LIST"""
i=0

while (i<entries):
    tree_type =tree_info['data'][i][10]
    latitude = tree_info['data'][i][23]
    longitude = tree_info['data'][i][24]

    # split out the scientific and common name from data
    scientific_name, common_name = tree_type.split('::')
    scientific = scientific_name.rstrip()
    common_name = common_name.lstrip()     

    if latitude == None and longitude==None:
        pass
    
    elif tree_type == 'Tree(s) ::':
        pass

    else:
        TREE_LIST.append({'scientific_name':scientific_name,'common_name': common_name,'lat':latitude,'lon':longitude})

    i+=1


def top_ten_trees():
    """ Return top ten of the populous trees in SF """
    
    sci_treenames = []

    for tree in TREE_LIST:
        sci_treenames.append(tree['scientific_name'])

    # Make a set of trees.
    tree_set=set()

    for tree in sci_treenames:
        tree_set.add(tree)

    # Create a tuple with tree scientific name and tree count
    tree_count=[(tree, sci_treenames.count(tree)) for tree in tree_set]

    # sort trees in reverse order by tree count
    sorted_trees =sorted(tree_count, key= lambda x:x[1], reverse=True)

    # list top ten trees in sf data list
    top_ten = [each for i, each in enumerate(sorted_trees) if i<10]

    return top_ten



def tree_dict():
    """create diction of all tree data set"""
    
    TREE_DICT = {}

    # iterate through dictionary list and append data as a dict to TREE LIST
    i=0

    while (i<entries):
        tree_type =tree_info['data'][i][10]
        latitude = tree_info['data'][i][23]
        longitude = tree_info['data'][i][24]

        # split out the scientific and common name from data
        scientific_name, common_name = tree_type.split('::')
        scientific = scientific_name.rstrip()
        common_name = common_name.lstrip()     

        if latitude == None and longitude==None:
            pass
        
        elif tree_type == 'Tree(s) ::':
            pass

        else:
            TREE_DICT[scientific_name] = {'common_name': common_name,'lat':latitude,'lon':longitude}

        i+=1

    return TREE_DICT


def test_tree_dict():
    """create dictionary of test trees"""

    trees= top_ten_trees()
    TREE_DICT = tree_dict()
    TEST_TREES = {}
    sci_name_list=[]

    for tree in trees:
        sci_name = tree[0]
        TEST_TREES[sci_name] = TREE_DICT[sci_name]
        sci_name_list.append(sci_name)

    tree_key_dict = (sci_name_list, TEST_TREES)
    return tree_key_dict