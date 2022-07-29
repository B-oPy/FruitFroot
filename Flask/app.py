from __future__ import division, print_function
# coding=utf-8
import sys
import os
import glob
import re
import numpy as np
import pandas as pd

# Keras
from keras.applications.imagenet_utils import preprocess_input, decode_predictions
from keras.models import load_model
from keras.preprocessing import image

# Flask utils
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer

# Define a flask app
app = Flask(__name__)

# # Model saved with Keras model.save()
# MODEL_PATH = '딥러닝미니플젝/과수화상병_Project/FruitFrut_Final_Bopy/model/VGG19-010-0.1600-0.9630.hdf5'

# # Load your trained model
# model = load_model(MODEL_PATH)
# model.make_predict_function()          # Necessary

# Model saved with Keras model.save()
MODEL_PATH1 = '딥러닝미니플젝/과수화상병_Project/FruitFroot_Final_Bopy/model/Apple_VGG19-009-0.0922-0.9705.hdf5'

# Load your trained model
model1 = load_model(MODEL_PATH1)
model1.make_predict_function()

# Model saved with Keras model.save()
MODEL_PATH2 = '딥러닝미니플젝/과수화상병_Project/FruitFroot_Final_Bopy/model/Pear_mobilenet-006-0.0761-0.9739.hdf5'

# Load your trained model
model2 = load_model(MODEL_PATH2)
model2.make_predict_function()

def model_predict(img_path, model):
    img = image.load_img(img_path, target_size=(224, 224))

    # Preprocessing the image
    x = image.img_to_array(img)
    # x = np.true_divide(x, 255)
    x = np.expand_dims(x, axis=0)

    # Be careful how your trained model deals with the input
    # otherwise, it won't make correct prediction!
    x = preprocess_input(x, mode='caffe')

    preds = model.predict(x)
    return preds


# @app.route('/', methods=['GET'])
# def index():
#     # Main page
#     return render_template('index.html')

@app.route('/', methods=['GET'])
def model_Select():
    return render_template('select.html')

@app.route('/APPLE',methods=['GET'])
def APPLE():

    return render_template('apple.html')

@app.route('/predict1', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']

        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)

        # Make prediction
        disease1 = ['정상 사과','사과갈색무늬병','사과과수화상병','사과부란병','사과점무늬낙엽병','사과탄저병']
        classes1 = model_predict(file_path, model1)
        import operator

        result1 ={}
        for i in range(6) :
            result1[disease1[i]] = round(classes1[0][i]*100,4)
        r1 = sorted(result1.items(), key=operator.itemgetter(1), reverse=True)
        result1= str(r1[0][0]) + '일 확률이 ' + str(r1[0][1]) + '% 입니다.'

        return result1
    return None

@app.route('/PEAR',methods=['GET'])
def PEAR():

    return render_template('pear.html')

@app.route('/predict2', methods=['GET', 'POST'])
def upload2():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']

        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)

        # Make prediction
        disease2 = ['정상 배', '배검은별무늬병','배과수화상병']
        classes2 = model_predict(file_path, model2)
        import operator

        result2 ={}
        for i in range(3) :
            result2[disease2[i]] = round(classes2 [0][i]*100,4)
        r2 = sorted(result2.items(), key=operator.itemgetter(1), reverse=True)
        result2= str(r2[0][0]) + '일 확률이 ' + str(r2[0][1]) + '% 입니다.'

        return result2
    return None

@app.route('/explain')
def explain():
    return render_template('Bopy_Fruit_Cv.html') 

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

