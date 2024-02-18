from flask import Blueprint, render_template, request
import pickle
import numpy as np
import os
from skimage.io import imread
from skimage.transform import resize

views = Blueprint('views',__name__)

model_path = os.path.join(os.path.dirname(__file__), '..', 'model.p')
model = pickle.load(open(model_path, 'rb'))

# model = pickle.load(open('model.p','rb'))
categories = ['flea', 'mosquito', 'tick']

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/pic', methods=['GET', 'POST'])
def identify():
    if request.method =='POST':
        try:
            url=request.form['image_url']
            img=imread(url)
            img=resize(img, (30,30,3))
            flat_data=[img.flatten()]
            flat_data=np.array(flat_data)
            y_out=model.predict(flat_data)
            category=categories[y_out[0]]
            return render_template("home.html", prediction=category, image_url=url)
        except Exception as e:
            return render_template('home.html', error=str(e))
    else:
        return render_template('home.html')
    