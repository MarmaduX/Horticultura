from flask import Flask, request, redirect, url_for
from flask import render_template
from web.servicios import autenticacion

app = Flask(__name__)


@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if not autenticacion.validar_credenciales(request.form['login'], request.form['password']):
            error = 'Credenciales inválidas'
        else:
            return redirect(url_for('inicio'))
        return render_template('login.html', error=error)

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    error = None
    if request.method == 'POST':
        if not autenticacion.crear_usuario(request.form['login'], request.form['password']):
            error = 'No se pudo crear el usuario'
        else:
            return redirect(url_for('inicio'))
    return render_template('registro.html', error=error)

@app.route('/inicio')
def inicio():
    usuarios = autenticacion.obtener_usuarios()
    return render_template('inicio.html', usuarios=usuarios)



@app.route('/inicio')
def inicio():
    cultivos = autenticacion.obtener_cultivos()
    return render_template('inicio.html', cultivos=cultivos)


@app.route('/cultivos', methods=['POST'])
def cultivos():
    error = None
    if request.method == 'POST':
        if not autenticacion.crear_cultivo(request.form['cultivos']):
            error = 'No se pudo crear el cultivo'
        else:
            return redirect(url_for('cultivos'))
    return render_template('cultivos.html', error=error)


@app.route('/cultivos', methods=['PUT'])
def cultivos():
    error = None
    if request.method == 'PUT':
        if not autenticacion.modificar_cultivo(request.form['cultivos']):
            error = 'No se pudo modificar el cultivo'
        else:
            return redirect(url_for('cultivos'))
    return render_template('cultivos.html', error=error)


@app.route('/cultivos', methods=['GET'])
def cultivos():
    error = None
    if request.method == 'GET':
        if not autenticacion.mostrar_cultivos(request.form['cultivos']):
            error = 'No se pudieron obtener los cultivos'
        else:
            return redirect(url_for('cultivos'))
    return render_template('cultivos.html', error=error)


@app.route('/cultivos', methods=['GET'])
def cultivos():
    error = None
    if request.method == 'GET':
        if not autenticacion.mostrar_cultivos(request.form['cultivos']):
            error = 'No se pudieron mostrar los cultivos'
        else:
            return redirect(url_for('cultivos'))
    return render_template('cultivos.html', error=error)


@app.route('/cultivos', methods=['GET'])
def cultivos():
    error = None
    if request.method == 'GET':
        if not autenticacion.mostrar_cultivos_filtrados(request.form['cultivos']):
            error = 'No se pudo mostrar el cultivo'
        else:
            return redirect(url_for('cultivos'))
    return render_template('cultivos.html', error=error)


@app.route('/cultivos', methods=['DELETE'])
def cultivos():
    error = None
    if request.method == 'DELETE':
        if not autenticacion.eliminar_cultivo(request.form['cultivos']):
            error = 'No se pudo eliminar el cultivo'
        else:
            return redirect(url_for('cultivos'))
    return render_template('cultivos.html', error=error)



if __name__ == '__main__':
    app.debug = True
    app.run(port=5002)