from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
from waitress import serve
import json
from Controladores.ControladorMesa import ControladorMesa
from Controladores.ControladorCandidato import ControladorCandidato
from Controladores.ControladorPartido import ControladorPartido
from Controladores.ControladorResultado import ControladorResultado

app = Flask(__name__)
cors = CORS(app)

#Creando Instancias
miControladorMesa = ControladorMesa()
miControladorCandidato = ControladorCandidato()
miControladorPartido = ControladorPartido()
miControladorResultado = ControladorResultado()

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

#-------------------------------Edit partidos--------------------------------------------------

@app.route("/partidos",methods=['GET'])
def getPartidos():
    json = miControladorPartido.index()
    return jsonify(json)

@app.route("/partidos",methods=['POST'])
def crearPartido():
    data = request.get_json()
    json = miControladorPartido.create(data)
    return jsonify(json)

@app.route("/partidos/<string:id>",methods=['GET'])
def getPartido(id):
    json=miControladorPartido.show(id)
    return jsonify(json)

@app.route("/partidos/<string:id>",methods=['PUT'])
def modificarPartido(id):
    data = request.get_json()
    json=miControladorPartido.update(id,data)
    return jsonify(json)

@app.route("/estudiantes/<string:id>",methods=['DELETE'])
def eliminarPartido(id):
    json=miControladorPartido.delete(id)
    return jsonify(json)


#------------------------------Edit Resultados -----------------------------------------------------------------

@app.route("/Resultados",methods=['GET'])
def getResultados():
    json=miControladorResultado.index()
    return jsonify(json)
@app.route("/Resultados/<string:id>",methods=['GET'])
def getResultado(id):
    json=miControladorResultado.show(id)
    return jsonify(json)
@app.route("/Resultados/mesa/<string:id_mesa>/candidato/<string:id_candidato>",methods=['POST'])
def crearResultado(id_estudiante,id_materia):
    data = request.get_json()
    json=miControladorResultado.create(data,id_estudiante,id_materia)
    return jsonify(json)
@app.route("/Resultados/<string:id_resultado>/mesa/<string:id_mesa>/candidato/<string:id_candidato>",methods=['PUT'])
def modificarResultado(id_resultado,id_mesa,id_candidato):
    data = request.get_json()
    json=miControladorResultado.update(id_resultado,data,id_mesa,id_candidato)
    return jsonify(json)
@app.route("/Resultados/<string:id_resultado>",methods=['DELETE'])
def eliminarResultado(id_resultado):
    json=miControladorResultado.delete(id_resultado)
    return jsonify(json)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    dataConfig = loadFileConfig()
    print("Server running : " + "http://" + dataConfig["url-backend"] + ":" + str(dataConfig["port"]))
    serve(app, host=dataConfig["url-backend"], port=dataConfig["port"])

