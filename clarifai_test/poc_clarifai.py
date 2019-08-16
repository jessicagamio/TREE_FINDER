
import os
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
import json


CLARIFAI_TOKEN= os.environ.get('CLARIFAI_TOKEN')
app = ClarifaiApp(api_key=CLARIFAI_TOKEN)


def train_images():
    """train images"""

    # create empty image lists
    platanus_images=[]
    magnolia_images=[]
    prunus_images=[]
    tristan_images=[]
    ficus_images=[]

    test_trees = ['platanus','magnolia','prunus','tristan','ficus']
    test_images = [platanus_images,magnolia_images,prunus_images,tristan_images,ficus_images]
    
    # Iterate through folder with test images and add to designated concept    
    for i,tree in enumerate(test_trees):
        for file in os.listdir('img/{tree}'):
           img=ClImage( filename=f'img/{tree}/{file}', concepts=[{tree}])
           test_images[i].append(img)


        # Bulk create images
        app.inputs.bulk_create_images(test_images[i])

def make_prediction(user_picture, trees=['platanus','magnolia','prunus','tristan','ficus']):
    """make prediction """

    train_images()
    # Create model and add chosen concepts to model
    model=app.models.create('detect_tree', concepts = trees)

    # train the model
    model.train()

    # RUN PREDICTION
        # Value of 0 means object was NOT detected. 
        # Value above 1 means 100% certainty object was detected.
    prediction = model.predict_by_filename('img/test_leaf/{user_picture}')

    # delete model
        #add code here#
 

