from flask import Flask, render_template, request, flash, redirect
import pickle
import numpy as np
from PIL import Image
#from tensorflow.keras.models import load_model

app = Flask(__name__)

def predict(values, dic):
    if len(values) == 18:
        model = pickle.load(open('kidney.pkl','rb'))
        values = np.asarray(values)
        return model.predict(values.reshape(1, -1))[0]
@app.route("/kidney", methods=['GET', 'POST'])
def kidneyPage():
    return render_template('kidney.html')
if __name__ == '__main__':
	app.run(debug = True)