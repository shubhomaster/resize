import cv2
import numpy as np
from flask import Flask,render_template,request
import os

app = Flask(__name__)

img=None

@app.route('/')
def index():
    return render_template("home.html")

@app.route('/upload',methods=['GET','POST'])
def upload():

    global img

    # fetch file
    image = request.files['myfile']
    image.save(os.path.join("static", image.filename))

    img = cv2.imread("static/" + image.filename)

    return render_template("display.html",filename=image.filename)

@app.route('/resize',methods=['POST'])
def resize():

    width = int(request.form.get('width'))
    height = int(request.form.get('height'))
    # resizing logic here
    resizedImg = cv2.resize(img,(width,height))
    cv2.imwrite("static/abc.png",resizedImg)

    return '<h4>Dowload you image from <a href="static/abc.png">here</a>. Right click and click save</h4>'


if __name__=="__main__":
    app.run(debug=True)

# How to upload files using Flask

# Image resizing

# Display to download