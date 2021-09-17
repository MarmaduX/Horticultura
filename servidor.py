from flask import Flask, request,  render_template, jsonify
from Servicios.autenticacion import autenticacion

app = Flask(__name__)

@app.route('/usuarios', methods=['POST'])
def crear_usuario():
    datos_usuario = request.get_json()
    if 'nombre' not in datos_usuario:
        return 'El nombre de usuario es requerido', 412
    if 'correo' not in datos_usuario:
        return 'El correo es requerido', 412
    if 'usuario' not in datos_usuario:
        return 'El Nombre de Usuario es requerido', 412
    if 'clave' not in datos_usuario:
        return 'La clave es requerida', 412
    autenticacion.crear_usuario(datos_usuario['nombre'], datos_usuario['correo'], datos_usuario['usuario'], datos_usuario['clave'])
    return 'OK', 200

@app.route('/casos/<idUsuario>', methods=['POST'])
def crear_caso(idUsuario):
    datos_casos =  request.get_json()
    autenticacion.crear_caso(datos_casos['tipoCultivo'], datos_casos['nombrePlanta'], datos_casos['foto'], datos_casos['descripcionCaso'], datos_casos['estado'], datos_casos['evolucionCaso'], datos_casos['fechaActualizacion'], datos_casos['recomendaciones'], idUsuario)
    return 'OK', 200

@app.route('/casos/<idCaso>', methods=['PUT'])
def modificar_caso(idCaso):
    datos_casos = request.get_json()
    autenticacion.modificar_caso(idCaso, datos_casos['tipoCultivo'], datos_casos['nombrePlanta'], datos_casos['foto'], datos_casos['descripcionCaso'], datos_casos['estado'], datos_casos['evolucionCaso'], datos_casos['fechaActualizacion'], datos_casos['recomendaciones'], datos_casos['especialsita'])
    return 'OK', 200

@app.route('/casos/<idCaso>', methods=['DELETE'])
def eliminar_caso(idCaso):
    autenticacion.eliminar_caso(idCaso)
    return 'OK', 200

@app.route('/casos', methods=['GET'])
def mostrar_casos():
    return jsonify(autenticacion.mostrar_casos()), 200


@app.route('/casos/<idCaso>', methods=['GET'])
def mostrar_casos(idCaso):
    return jsonify(autenticacion.ver_caso(idCaso)), 200

@app.route('/casos/<idUsuario>', methods=['GET'])
def mostrar_caso_por(idUsuario):
    return jsonify(autenticacion.mostrar_casos_usuario(idUsuario)), 200

@app.route('/casos/<tipoCultivo>', methods=['GET'])
def mostrar_casos_por(tipoCultivo):
    return jsonify(autenticacion.mostrar_casos_por(tipoCultivo)), 200

@app.route('/casos/editarCaso/<idCaso>', methods=['PUT'])
def registrar_recomendacion(idCaso):
    datos_casos = request.get_json()
    autenticacion.registrar_recomendacion(idCaso, datos_casos['recomendaciones'], datos_casos['estado'], datos_casos['fechaActualizacion'])
    return 'OK', 200

@app.route('/casos/finalizar/<idCaso>', methods=['PUT'])
def pasar_a_resuelto_un_caso(idCaso):
    datos_casos = request.get_json()
    autenticacion.pasar_a_resuelto_un_caso(idCaso, datos_casos['estado'], datos_casos['fecaActualizacion'])
    return 'OK', 200

@app.route('/cultivos', methods=['POST'])
def crear_cultivo():
    datos_cultivo =  request.get_json()
    autenticacion.crear_cultivo(datos_cultivo['nombrecientifco'], datos_cultivo['tipoCultivo'], datos_cultivo['foto'], datos_cultivo['descripcionCultivo'], datos_cultivo['plagas'], datos_cultivo['enfermedades'])
    return 'OK', 200

@app.route('/cultivos/<idPlanta>', methods=['PUT'])
def editar_cultivo(idPlanta):
    datos_cultivo =  request.get_json()
    autenticacion.editar_cultivo(idPlanta, datos_cultivo['nombrecientifco'], datos_cultivo['tipoCultivo'], datos_cultivo['foto'], datos_cultivo['descripcionCultivo'], datos_cultivo['plagas'], datos_cultivo['enfermedades'])
    return "OK", 200

@app.route('/cultivos', methods=['GET'])
def listar_cultivos():
    lista = autenticacion.listar_cultivos()
    return jsonify(lista), 200

@app.route('/cultivos/<idPlanta>', methods=['GET'])
def mostrar_cultivo(idPlanta):
    lista = autenticacion.mostar_cultivo(idPlanta)
    return jsonify(lista), 200

@app.route('/cultivos/<idPlanta>', methods=['DELETE'])
def eliminar_cultivo(idPlanta):
    autenticacion.eliminar_cultivo(idPlanta)
    return "OK", 200

@app.route('/cultivo/<tipoCultivo>', methods=['GET'])
def mostar_cultivo_por(tipoCultivo):
    lista = autenticacion.mostar_cultivo_por(tipoCultivo)
    return jsonify(lista) , 200

@app.route('/rol', methods=['POST'])
def crear_tipo():
    datos_tipo = request.get_json()
    autenticacion.crear_rol(datos_tipo['tipoRol'])
    return 'OK', 200

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/home")
def ver_home():
    return "Home"




if __name__ == '__main__':
    app.debug = True
    app.run(port=5001)
