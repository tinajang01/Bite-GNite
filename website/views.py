from flask import Blueprint, render_template, request
import pickle
import numpy as np
from skimage.io import imread
from skimage.transform import resize

views = Blueprint('views',__name__)

model = pickle.load(open('model.p','rb'))
categories = ['flea', 'mosquito', 'tick']

@views.route('/', methods=['GET', 'POST'])
def home():
    if request.method =='POST':
        try:
            url=request.form['image_url']
            img=imread(url)
            img=resize(img, (30,30,3), anti-aliasing=True)
            flat_data=[img.flatten()]
            flat_data=np.array(flat_data)
            y_out=model.predict(flat_data)
            category=categories[y_out[0]]
            return render_template("home.html", prediction=category, image_url=url)
        except Exception as e:
            return render_template('home.html', error=str(e))
    else:
        return render_template('home.html')