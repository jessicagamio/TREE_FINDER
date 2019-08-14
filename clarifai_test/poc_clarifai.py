
import os
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
import json
from pprint import pprint

CLARIFAI_TOKEN= os.environ.get('CLARIFAI_TOKEN')
app = ClarifaiApp(api_key=CLARIFAI_TOKEN)


# create empty image lists
smooth_abst_images=[]
serrated_abst_images=[]

# Iterate through folder with test images and add to designated concept
for file in os.listdir('img/shapes/smooth/abstract'):
   img=ClImage( filename=f'img/shapes/smooth/abstract/{file}', concepts=['smooth_abst1'])
   smooth_abst_images.append(img)

for file in os.listdir('img/shapes/serrated/abstract'):
    img = ClImage(filename=f'img/shapes/serrated/abstract/{file}', concepts=['serrated_abst1'])
    serrated_abst_images.append(img)

# Bulk create images
app.inputs.bulk_create_images(smooth_abst_images)
app.inputs.bulk_create_images(serrated_abst_images)


# Create model and add chosen concepts to model
model=app.models.create('test_edge_g', concepts =['smooth_abst1','serrated_abst1'])

# train the model
model.train()

# RUN PREDICTION
    # Value of 0 means object was NOT detected. 
    # Value above 1 means 100% certainty object was detected.
prediction = model.predict_by_filename('img/shapes/single_smooth_outdoors2.jpg')

 
pprint(prediction)

