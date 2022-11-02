from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve

app = Flask(__name__)
cors = CORS(app)

@app.route("/",methods=['GET'])
def test():
    json = {}
    json["message"] = "Server running ..."
    return jsonify(json)

#Leer archivo de config
def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    dataConfig = loadFileConfig()
    print("Server running : " + "http://" + dataConfig["url-backend"] + ":" + str(dataConfig["port"]))
    serve(app, host=dataConfig["url-backend"], port=dataConfig["port"])