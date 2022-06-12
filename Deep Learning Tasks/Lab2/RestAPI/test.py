from msilib.schema import PatchPackage
from statistics import mode
import tensorflow as tf
import os 
import cv2
import numpy as np
import json as js
import base64
from flask import Flask, request
from flask import json as fjson

class ReturnObject:
  x0 = 0
  x1 = 0
  y0 = 0
  y1 = 0
  classification = 'none'

api = Flask(__name__)

@api.route('/gmm2', methods=['GET'])
def get_recognition():
    #You have to send Res64 format to controller, for this to work
    data = request.get_json()
    base64_message = data['image']
    sample_string_bytes = base64.b64decode(base64_message)
    root = os.path.dirname(os.path.realpath(__file__))
    g = open(root + '\images\out.jpg', "wb")
    g.write(sample_string_bytes)
    g.close()
    modelDirectory = root + '\my_model'
    model = tf.keras.models.load_model(
        modelDirectory, custom_objects=None, compile=True, options=None
    )

    photos = []
    imageLoc = root + '\images\out.jpg'
    im = cv2.imread(imageLoc)
    imS = cv2.resize(im, (224, 224))  
    photos.append(imS)

    photos = np.array(photos)
    prediction = model.predict(photos)
    returnObject = ReturnObject()
    classes = ['Bee', 'Fruit', 'Seafood']
    returnObject.x0 = str(round(prediction[1][0][0], 2))
    returnObject.x1 = str(round(prediction[1][0][1], 2))
    returnObject.y0 = str(round(prediction[1][0][2], 2))
    returnObject.y1 = str(round(prediction[1][0][3], 2))
    returnObject.classification = classes[np.argmax(prediction[0][0])]
    return fjson.dumps(returnObject.__dict__)

if __name__ == '__main__':
    api.run() 
