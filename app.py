# app.py
from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os

app = Flask(__name__)
model = load_model('model/pneumonia_model.h5')

UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    filename = None

    if request.method == 'POST':
        img_file = request.files['image']
        if img_file:
            filename = img_file.filename
            img_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            img_file.save(img_path)

            img = image.load_img(img_path, target_size=(150, 150))
            img_array = image.img_to_array(img) / 255.0
            img_array = np.expand_dims(img_array, axis=0)

            result = model.predict(img_array)[0][0]
            prediction = "Pneumonia Detected" if result > 0.5 else "Normal"

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
