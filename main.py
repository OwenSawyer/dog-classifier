# restore trained data
import tensorflow as tf
import numpy as np

import sys
sys.path.append('imagenet')
import classify_image

//x = tf.placeholder("float", [None, 784])
//sess = tf.Session()

//with tf.variable_scope("convolutional"):
//    keep_prob = tf.placeholder("float")
//    y2, variables = model.convolutional(x, keep_prob)
//saver = tf.train.Saver(variables)
//saver.restore(sess, "mnist/data/convolutional.ckpt")
//def convolutional(input):
//    return sess.run(y2, feed_dict={x: input, keep_prob: 1.0}).flatten().tolist()

# webapp
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

@app.route('/api/mnist', methods=['POST'])
def mnist():
    //input = ((255 - np.array(request.json, dtype=np.uint8)) / 255.0).reshape(1, 784)
    //output1 = simple(input)
    //output2 = convolutional(input)
    //return jsonify(results=[output1, output2])
    return jsonify(classify_image())

@app.route('/')
def main():
    return render_template('index.html')
