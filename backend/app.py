from flask import Flask,jsonify,request
from flask_cors import CORS
import json


from flask import jsonify

app = Flask(__name__)

#the constructor has access to app, modifies it accordingly
CORS(app)

@app.route("/", methods=["GET","POST"])
def hello_world():
    file_ = request.files['file']
    file_.save(file_.filename)

    text_input = request.form['text1']
    checkbox_value = request.form['checkbox']

    return jsonify({'a':'b','c':'d'})
