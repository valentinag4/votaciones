# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings jejeje.

from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
from waitress import serve
import json

app=Flask(__name__)
cors = CORS(app)
def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
        return data

@app.route("/",methods=['GET'])
def test():
    json = {}
    json["message"]="Server running ...."
    return jsonify(json)

if __name__=='__main__':
    dataConfig = loadFileConfig()
    print("Server running : "+"http://"+dataConfig["url-backend"]+":" + str(dataConfig["port"]))
    serve(app,host=dataConfig["url-backend"],port=dataConfig["port"])