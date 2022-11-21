from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve
import datetime
import requests
import re
from flask_jwt_extended import create_access_token, verify_jwt_in_request
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

app = Flask(__name__)
cors = CORS(app)

app.config["JWT_SECRET_KEY"] = "super-secret" #Cambiar por el que se conveniente
jwt = JWTManager(app)

@app.route("/",methods=['GET'])
def test():
     json = {}
     json["message"] = "Server running ..."
     return jsonify(json)

@app.route("/login", methods=["POST"])
def create_token():
    data = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-seguridad"]+'/usuario/validar'
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200:
        user = response.json()
        expires = datetime.timedelta(seconds=60 * 60*24)
        access_token = create_access_token(identity=user, expires_delta=expires)
        return jsonify({"token": access_token, "user_id": user["_id"]})
    else:
          return jsonify({"msg": "Bad username or password"}), 401

@app.before_request
def before_request_callback():
    endPoint = limpiarURL(request.path)
    excludedRoutes = ["/login"]
    if excludedRoutes.__contains__(request.path):
        pass
    elif verify_jwt_in_request():
        usuario = get_jwt_identity()
        if usuario["rol"]is not None:
            tienePersmiso = validarPermiso(endPoint,request.method,usuario["rol"]["_id"])
            if not tienePersmiso:
                return jsonify({"message": "Permission denied"}), 401
        else:
            return jsonify({"message": "Permission denied"}), 401

def limpiarURL(url):
    partes = url.split("/")
    for laParte in partes:
        if re.search('\\d', laParte):
            url = url.replace(laParte, "?")
    return url

def validarPermiso(endPoint,metodo,idRol):
    url = dataConfig["url-backend-seguridad"]+"/permisos-roles/validar-permiso/rol/"+str(idRol)
    tienePermiso = False
    headers = {"Content-Type": "application/json; charset=utf-8"}
    body = {
        "url": endPoint,
        "metodo": metodo
    }
    response = requests.get(url, json=body, headers=headers)
    try:
        data = response.json()
        if ("_id" in data):
            tienePermiso = True
    except:
        pass
    return tienePermiso

def loadFileConfig():
     with open('config.json') as f:
        data = json.load(f)
     return data

# ----------------------------- MESA -----------------------------
# ! METODO GET (LISTAR TODOS)
@app.route("/mesa",methods=['GET'])
def getMesas():
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-resultado"] + '/mesa'
    response = requests.get(url, headers=headers)
    json = response.json()
    return jsonify(json)

# ! METODO POST (CREAR)
@app.route("/mesa",methods=['POST'])
def crearMesa():
    data = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-resultado"] + '/mesa'
    response = requests.post(url, headers=headers,json=data)
    json = response.json()
    return jsonify(json)

# ! METODO GET POR ID (LISTAR POR ID)
@app.route("/mesa/<string:id>",methods=['GET'])
def getMesa(id):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-resultado"] + '/mesa/'+id
    response = requests.get(url, headers=headers)
    json = response.json()
    return jsonify(json)

# ! METODO PUT (MODIFICAR)
@app.route("/mesa/<string:id>",methods=['PUT'])
def modificarMesa(id):
    data = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-resultado"] + '/mesa/'+id
    response = requests.put(url, headers=headers, json=data)
    json = response.json()
    return jsonify(json)

# ! METODO DELETE (ELIMINAR)
@app.route("/mesa/<string:id>",methods=['DELETE'])
def eliminarMesa(id):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-resultado"] + '/mesa/' + id
    response = requests.delete(url, headers=headers)
    json = response.json()
    return jsonify(json)

# ----------------------------- PARTIDO -----------------------------
# ! METODO GET (LISTAR TODOS)
@app.route("/partido",methods=['GET'])
def getPartidos():
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-resultado"] + '/partido'
    response = requests.get(url, headers=headers)
    json = response.json()
    return jsonify(json)

# ! METODO POST (CREAR)
@app.route("/partido",methods=['POST'])
def crearPartido():
    data = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-resultado"] + '/partido'
    response = requests.post(url, headers=headers,json=data)
    json = response.json()
    return jsonify(json)

# ! METODO GET POR ID (LISTAR POR ID)
@app.route("/partido/<string:id>",methods=['GET'])
def getPartido(id):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-resultado"] + '/partido/'+id
    response = requests.get(url, headers=headers)
    json = response.json()
    return jsonify(json)

# ! METODO PUT (MODIFICAR)
@app.route("/partido/<string:id>",methods=['PUT'])
def modificarPartido(id):
    data = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-resultado"] + '/partido/'+id
    response = requests.put(url, headers=headers, json=data)
    json = response.json()
    return jsonify(json)

# ! METODO DELETE (ELIMINAR)
@app.route("/partido/<string:id>",methods=['DELETE'])
def eliminarPartido(id):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-resultado"] + '/partido/' + id
    response = requests.delete(url, headers=headers)
    json = response.json()
    return jsonify(json)

# ----------------------------- CANDIDATO -----------------------------
# ! METODO GET (LISTAR TODOS)
@app.route("/candidato",methods=['GET'])
def getCandidatos():
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-resultado"] + '/candidato'
    response = requests.get(url, headers=headers)
    json = response.json()
    return jsonify(json)

# ! METODO POST (CREAR)
@app.route("/candidato",methods=['POST'])
def crearCandidato():
    data = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-resultado"] + '/candidato'
    response = requests.post(url, headers=headers,json=data)
    json = response.json()
    return jsonify(json)

# ! METODO GET POR ID (LISTAR POR ID)
@app.route("/candidato/<string:id>",methods=['GET'])
def getCandidato(id):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-resultado"] + '/candidato/'+id
    response = requests.get(url, headers=headers)
    json = response.json()
    return jsonify(json)

# ! METODO PUT (MODIFICAR)
@app.route("/candidato/<string:id>",methods=['PUT'])
def modificarCandidato(id):
    data = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-resultado"] + '/candidato/'+id
    response = requests.put(url, headers=headers, json=data)
    json = response.json()
    return jsonify(json)

# ! METODO DELETE (ELIMINAR)
@app.route("/candidato/<string:id>",methods=['DELETE'])
def eliminarCandidato(id):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-resultado"] + '/candidato/' + id
    response = requests.delete(url, headers=headers)
    json = response.json()
    return jsonify(json)

# ! RELACION 1 A 1 (CANDIDATO - PARTIDO)
@app.route("/candidato/<string:id>/partido/<string:id_partido>",methods=['PUT'])
def asignarPartidoCandidato(id,id_partido):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-resultado"] + '/candidato/' + id + '/partido/' + id_partido
    response = requests.delete(url, headers=headers)
    json = response.json()
    return jsonify(json)

# ----------------------------- RESULTADO -----------------------------
# ! METODO GET (LISTAR TODOS)
@app.route("/resultado",methods=['GET'])
def getResultados():
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-resultado"] + '/resultado/' + id
    response = requests.delete(url, headers=headers)
    json = response.json()
    return jsonify(json)

# ! RELACION 1 A N (RESULTADOS - MESA & CANDIDATO)
@app.route("/resultados/mesa/<string:id_mesa>/candidato/<string:id_candidato>",methods=['POST'])
def crearResultado(id_mesa,id_candidato):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-resultado"] + '/candidato/' + '/mesa/' + id_mesa + '/candidato/' + id_candidato
    response = requests.delete(url, headers=headers)
    json = response.json()
    return jsonify(json)

# ! METODO GET POR ID (LISTAR POR ID)
@app.route("/resultado/<string:id>",methods=['GET'])
def getResultado(id):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-resultado"] + '/resultado/' + id
    response = requests.delete(url, headers=headers)
    json = response.json()
    return jsonify(json)

# ! METODO PUT (ACTUALIZAR RESULTADO)
@app.route("/resultados/<string:id_resultado>/mesa/<string:id_mesa>/candidato/<string:id_candidato>",methods=['PUT'])
def modificarResultado(id_resultado,id_mesa,id_candidato):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-resultado"] + '/resultados/' + id_resultado + '/mesa/' + id_mesa + '/candidato/' + id_candidato
    response = requests.delete(url, headers=headers)
    json = response.json()
    return jsonify(json)

# ! METODO DELETE (ELIMINAR)
@app.route("/resultados/<string:id_resultado>",methods=['DELETE'])
def eliminarResultado(id_resultado):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-resultado"] + '/resultados/' + id_resultado
    response = requests.delete(url, headers=headers)
    json = response.json()
    return jsonify(json)

# Main Function
if __name__ == '__main__':
    dataConfig = loadFileConfig()
    print("Server running : " + "http://" + dataConfig["url-backend"] + ":" + str(dataConfig["port"]))
    serve(app, host=dataConfig["url-backend"], port=dataConfig["port"])