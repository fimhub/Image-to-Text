import numpy as np
from numpy.linalg import norm
from ast import literal_eval
from operator import itemgetter
from keras.preprocessing import image
from tensorflow.keras.applications.vgg16 import VGG16
from tensorflow.keras.applications.vgg16 import preprocess_input
import tensorflow as tf
import tensorflow.python.keras.backend as K
import cv2

global graph
graph = K.get_graph()

model = VGG16(weights='imagenet', include_top=False)
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def processPhoto(photo):
    # img = image.load_img(photo, target_size=(224,224))
    # img_data = image.img_to_array(img)
    npimg = np.fromstring(photo, np.uint8)
    # convert numpy array to image
    img_data = cv2.imdecode(npimg, 1)
    img_data = cv2.resize(img_data, (244, 244))
    img_data = np.expand_dims(img_data, axis=0)
    img_data = preprocess_input(img_data)

    features = model.predict(img_data)
    return features

# convert each dict of values back into an ndarray
def fromZeroes(data):
    features = literal_eval(data)
    narray = np.zeros((1,7,7,512))
    for i, first in features.items():
        for j, second in first.items():
            for k, third in second.items():
                for l, fourth in third.items():
                    narray[i][j][k][l] = fourth
    return narray

#closest = iarray.map(image => comparison = {'mlsnum': image.mlsnum, 'closeness': norm(photo - fromZeroes(image.features))
def findClosest(photo, iarray):
    features = processPhoto(photo)
    closest = []
    for image in iarray:
        comparison = {
            'mlsnum': image.mlsnum,
            'closeness': np.linalg.norm(features - fromZeroes(image.features))
        }
        closest.append(comparison)
    closest.sort(key=itemgetter('closeness'))
    # only return the top five
    return [c['mlsnum'] for c in closest[:5]]