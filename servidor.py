from flask import Flask, request
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


if __name__ == '__main__':
    app.debug = True
    app.run(port=5001)
