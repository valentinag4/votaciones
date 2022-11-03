from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
from waitress import serve
import json
from Controladores.ControladorMesa import ControladorMesa
from Controladores.ControladorCandidato import ControladorCandidato

app = Flask(__name__)
cors = CORS(app)

#Creando Instancias
miControladorMesa = ControladorMesa()
miControladorCandidato = ControladorCandidato()

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


#----------------------------------------SERVICIOS MESA----------------------------------------
#Endpoint para crear una mesa
@app.route("/mesas", methods=['POST'])
def crearMesa():
    data = request.get_json()
    json = miControladorMesa.create(data)
    return jsonify(json)

#Endpoint para listar las mesas
@app.route("/mesas", methods=['GET'])
def listarMesas():
    json = miControladorMesa.index()
    return jsonify(json)

#Endpoint para listar la mesa por ID
@app.route("/mesas/<string:id>", methods=['GET'])
def listarMesa(id):
    json = miControladorMesa.show(id)
    return jsonify(json)

#Endpoint para actualizar una mesa
@app.route("/mesas/<string:id>", methods=['PUT'])
def modificarMesa(id):
    data = request.get_json()
    json = miControladorMesa.update(id, data)
    return jsonify(json)

#Endpoint para eliminar un estudiante
@app.route("/mesas/<string:id>", methods=['DELETE'])
def eliminarMesa(id):
    json = miControladorMesa.delete(id)
    return jsonify(json)
#----------------------------------------------------------------------------------------------



#-------------------------------------SERVICIOS CANDIDATOS-------------------------------------
#Endpoint para crear un candidato
@app.route("/candidatos", methods=['POST'])
def crearCandidato():
    data = request.get_json()
    json = miControladorCandidato.create(data)
    return jsonify(json)

#Endpoint para listar los candidatos
@app.route("/candidatos", methods=['GET'])
def listarCandidatos():
    json = miControladorCandidato.index()
    return jsonify(json)

#Endpoint para listar el candidatos por ID
@app.route("/candidatos/<string:id>", methods=['GET'])
def listarCandidato(id):
    json = miControladorCandidato.show(id)
    return jsonify(json)

#Endpoint para actualizar una candidatos
@app.route("/candidatos/<string:id>", methods=['PUT'])
def modificarCandidato(id):
    data = request.get_json()
    json = miControladorCandidato.update(id, data)
    return jsonify(json)

#Endpoint para eliminar un candidato
@app.route("/candidatos/<string:id>", methods=['DELETE'])
def eliminarCandidato(id):
    json = miControladorCandidato.delete(id)
    return jsonify(json)
#----------------------------------------------------------------------------------------------

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    dataConfig = loadFileConfig()
    print("Server running : " + "http://" + dataConfig["url-backend"] + ":" + str(dataConfig["port"]))
    serve(app, host=dataConfig["url-backend"], port=dataConfig["port"])

