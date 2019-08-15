import os
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
import json
from pprint import pprint

# CLARIFAI_TOKEN= os.environ.get('CLARIFAI_TOKEN')
app = ClarifaiApp(api_key='d03d749bc6ad4512ad017bce4dff2085')


# create empty image lists
smooth_abst_images=[]
serrated_abst_images=[]


# app.concepts.update('serrated', 'concept_3', action='overwrite')
# app.concepts.update('palmate', 'concept_4', action ='overwrite')

# concepts = app.concepts.get_all()

# for i,concept in enumerate(concepts):
#     app.concepts.update('{concept}', 'concept_{i}', action='overwrite')

# Iterate through folder with test images and add to designated concept
# for i,file in enumerate(os.listdir('img/shapes/smooth/abstract')):
#    app.inputs.create_image_from_filename( filename=f'img/shapes/smooth/abstract/{file}', image_id= None, concepts=['smooth'], not_concepts=['serrated'], crop=None, metadata=None, geo=None, allow_duplicate_url=False)


# for i,file in enumerate(os.listdir('img/shapes/serrated/abstract')):
#    app.inputs.create_image_from_filename( filename=f'img/shapes/serrated/abstract/{file}', image_id= None, concepts=['serrated'], not_concepts=['smooth'], crop=None, metadata=None, geo=None, allow_duplicate_url=False)


# # Create model and add chosen concepts to model
# model=app.models.create('test_w_negatives', concepts =['smooth','serrated'])

# # train the model
# model.train()

# # RUN PREDICTION
#     # Value of 0 means object was NOT detected. 
#     # Value above 1 means 100% certainty object was detected.
# prediction = model.predict_by_filename('img/shapes/single_smooth_outdoors.jpg')

 
# pprint(prediction)

# app.concepts.update(concept_id='smooth_abst1', concept_name='concept_2')

# app.models.delete_all()