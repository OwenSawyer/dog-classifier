# restore trained data
import tensorflow as tf
import numpy as np

import sys
sys.path.append('imagenet')
import classify_image

# webapp
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

@app.route('/api/mnist', methods=['POST'])
def mnist():
    #input = ((255 - np.array(request.json, dtype=np.uint8)) / 255.0).reshape(1, 784)
    #output1 = simple(input)
    #output2 = convolutional(input)
    #return jsonify(results=[output1, output2])
    #with open("classify_image.py") as f:
    #code=compile(f.read(),"classify_read.py"),'exec')
    #return jsonify(exec(code))
    ret = classify_image.run_inference_on_image('cropped_panda.jpg');
    alert("here2");
    console.log("here2");
    return jsonify(ret)


@app.route('/')
def main():
    return render_template('index.html')
