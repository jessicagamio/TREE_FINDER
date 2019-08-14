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


"""store the number of entries in entries"""
entries= tree_info['data'].__len__()


"""create empty list of dictionaries"""
TREE_LIST = []


"""iterate through dictionary list and append data as a dict to TREE LIST"""
i=0

while (i<entries):
    tree_type =tree_info['data'][i][10]
    latitude = tree_info['data'][i][23]
    longitude = tree_info['data'][i][24]


    if latitude == None and longitude==None:
        pass
    else:
        TREE_LIST.append({'tree':tree_type,'lat':latitude,'lon':longitude})

    i+=1

for tree in TREE_LIST:
    print(tree)
