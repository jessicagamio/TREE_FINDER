import os
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
import json
from pprint import pprint

CLARIFAI_TOKEN= os.environ.get('CLARIFAI_TOKEN')
app = ClarifaiApp(api_key=CLARIFAI_TOKEN)


def create_concepts(tree):
    """Create concepts for each tree species"""

    tree = tree

    # Create Concept for tree_species
    images=[]

    for file in os.listdir(f'static/img/{tree}'):
       img=ClImage( filename=f'static/img/{tree}/{file}', concepts=[tree])
       images.append(img)

    app.inputs.bulk_create_images(images)


def create_model():
    """Create Model"""

    # Create model and add chosen concepts to model
    model=app.models.create('model_id_1', model_name='detect_tree', concepts=['platanus', 'prunus','magnolia','tristan','gingko'])

    # train the model
    model.train()

def add_concept(concept):
    """add conept to existing model"""

    model= app.models.get('detect_tree')
    model.add_concepts([concept])
 

def predict_model(user_image):
    """   RUN PREDICTION
         Value of 0 means object was NOT detected. 
         Value above 1 means 100% certainty object was detected.
    """

    model = app.models.get('detect_tree')

    prediction = model.predict_by_filename(user_image)
    
    for predict in prediction['outputs']:
        result = predict['data']['concepts']


    tree_prediction=[]  # create empty list of predictions

    for answer in result:   
        name = answer['name']
        value = answer['value']

        if value < .1:  # if value is less than 10 percent exclude
            continue

        else:   # includes predictions 10 percent or over
            value = (answer['value']) * 100
            value = round(value)
            tree_prediction.append((name,value))    

    # send back tree predictions that in Descending order that are above 10%
    tree_prediction = sorted(tree_prediction, key= lambda x:x[1], reverse=True)

    return tree_prediction



