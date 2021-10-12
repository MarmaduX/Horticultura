from flask import Flask, request,  render_template, jsonify, json, session, url_for
from Servicios.autenticacion import autenticacion

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    if 'usuario' in session:
        logged = True
        nickname = session['usuario'][3]
        userid = session['usuario'][0]
        rol = session['usuario'][5]
    else:
        logged = False
        nickname = ''
        userid = ''
        rol = ''
    return render_template('index.html', logged=logged, nickname=nickname, userid=userid, rol=rol)


@app.route('/signup', methods=['POST', 'GET'])
def crear_usuario():
    if request.method == 'POST':
        """datos_usuario = request.get_json()
        if 'nombre' not in datos_usuario:
            return 'El nombre de usuario es requerido', 412
        if 'correo' not in datos_usuario:
            return 'El correo es requerido', 412
        if 'usuario' not in datos_usuario:
            return 'El Nombre de Usuario es requerido', 412
        if 'clave' not in datos_usuario:
            return 'La clave es requerida', 412
        autenticacion.crear_usuario(datos_usuario['nombre'], datos_usuario['correo'], datos_usuario['usuario'], datos_usuario['clave'])"""
        return process_signup(), 200
    return render_template("signup.html"), 200


@app.route('/usuario/<idUsuario>', methods=['POST', "GET"])
def modificar_usuario(idUsuario):
    if request.method == 'POST':
        autenticacion.modificar_usuario(idUsuario, request.form['nombre'], request.form['usuario'], request.form['email'], request.form['clave'])
        return render_template("editar_usuario.html",nickname=session['usuario'][3], userid=session['user_id'], casos= len(session['casos']), email= session['email'], nombre = session['nombre'], rol = session['user_rol']), 200
    return render_template("editar_usuario.html", nickname=session['usuario'][3], userid=session['user_id'], casos= len(session['casos']), email= session['email'], nombre = session['nombre'],  rol = session['user_rol']), 200

@app.route('/usuario/<idUsuario>', methods=['DELETE'])
def eliminar_usuario(idUsuario):
    datos_usuario = request.get_json()
    autenticacion.eliminar_usuario(idUsuario)
    return index(), 200


@app.route('/login', methods=['POST', "GET"])
def login():
    if request.method == 'POST':
        """datos_usuario = request.get_json()
        datos = len(autenticacion.login(
            datos_usuario['usuario'], datos_usuario['clave']))
        if datos == 0:
            return "Usuario y/o Clave invalida", 412
        return "Tienes Acceso", 200"""
        missing = []
        fields = ['email', 'clave', 'login_submit']
        for field in fields:
            value = request.form.get(field, None)
            if value is None or value == '':
                missing.append(field)
        if missing:
            return render_template('missingFields.html', inputs=missing)

        return load_user(request.form['email'], request.form['clave'])

    return render_template("login.html"), 200


@app.route('/caso/<idUsuario>', methods=['POST', "GET"])
def crear_caso(idUsuario):
    if request.method == 'POST':
        # datos_casos = request.get_json()
        # if 'nombrePlanta' not in datos_casos:
        #     return 'El nombre de la planta es requerido', 412
        # if 'descripcionCaso' not in datos_casos:
        #     return 'La descripcion del caso es necesaria', 412
        # if 'foto' not in datos_casos:
        #     return 'La foto del caso es necesaria', 412
        # autenticacion.crear_caso(datos_casos['tipoCultivo'], datos_casos['nombrePlanta'], datos_casos['foto'], datos_casos['descripcionCaso'],
        #                         datos_casos['estado'], datos_casos['evolucionCaso'], datos_casos['fechaActualizacion'], idUsuario)
        missing = []
        fields = ['nombre', 'tipo', 'foto', 'desc']
        for field in fields:
            value = request.form.get(field, None)
            if value is None or value == '':
                missing.append(field)
        if missing:
            return render_template('missingFields.html', inputs=missing)
        return creacion_caso(request.form['nombre'], request.form['tipo'], request.form['show'], request.form['desc'], request.form['estado'], request.form['evolucion'], request.form['date'], idUsuario)
        
    return render_template("ingreso_caso.html", userid=idUsuario, nickname=session['usuario'][3],  rol =session['usuario'][0])

@app.route('/casos/<idCaso>', methods=['PUT'])
def modificar_caso(idCaso):
    if request.method == 'PUT':
        datos_casos = request.get_json()
        autenticacion.modificar_caso(idCaso, datos_casos['tipoCultivo'], datos_casos['nombrePlanta'], datos_casos['foto'],
                                 datos_casos['descripcionCaso'], datos_casos['estado'], datos_casos['evolucionCaso'], datos_casos['fechaActualizacion'])
        return 'OK', 200
    return render_template("home.html")

@app.route('/casos/<idCaso>', methods=['DELETE'])
def eliminar_caso(idCaso):
    autenticacion.eliminar_caso(idCaso)
    return 'OK', 200

@app.route('/eliminar_caso', methods=['DELETE'])
def eliminar_casoa():
    idcaso = request.form.get("idcaso")
    autenticacion.eliminar_caso(idcaso)
    return render_template("index.html")

@app.route('/casos', methods=['GET'])
def mostrar_casos():
    casos_a_mostrar = jsonify(autenticacion.mostrar_casos())
    return render_template("casos.html"), 200


@app.route('/vercaso/<idCaso>', methods=['GET'])
def mostrar_caso(idCaso):
    datos = autenticacion.ver_caso(idCaso)
    return render_template("caso.html", rol=session['usuario'][5], idcaso=idCaso, tipo=datos[0][1], nombre=datos[0][2], fotos=datos[0][3], texto=datos[0][4], estado=datos[0][5], evolucion=datos[0][6], date=datos[0][7], recomendacion=datos[0][8], userid=datos[0][9], especialista=datos[0][10], nickname=session['usuario'][3]), 200


@app.route('/casos/<idUsuario>', methods=['GET'])
def mostrar_caso_por(idUsuario):
    casos_a_mostrar = autenticacion.mostrar_casos_usuario(idUsuario)
    return render_template("casos_usuario.html", casos = casos_a_mostrar, usuario=session["usuario"])


@app.route('/casos/tipo/<tipoCultivo>', methods=['GET'])
def mostrar_casos_por(tipoCultivo):
    return jsonify(autenticacion.mostrar_casos_por(tipoCultivo)), 200


@app.route('/casos/editarCaso/<idCaso>', methods=['PUT'])
def registrar_recomendacion(idCaso):
    datos_casos = request.get_json()
    autenticacion.registrar_recomendacion(
        idCaso, datos_casos['recomendaciones'], datos_casos['estado'], datos_casos['fechaActualizacion'], datos_casos['especialista'])
    return 'OK', 200


@app.route('/casos/finalizar/<idCaso>', methods=['PUT'])
def pasar_a_resuelto_un_caso(idCaso):
    datos_casos = request.get_json()
    autenticacion.pasar_a_resuelto_un_caso(
        idCaso, datos_casos['estado'], datos_casos['fecaActualizacion'])
    return 'OK', 200


@app.route('/cultivos', methods=['POST'])
def crear_cultivo():
    datos_cultivo = request.get_json()
    autenticacion.crear_cultivo(datos_cultivo['nombrecientifco'], datos_cultivo['tipoCultivo'], datos_cultivo['foto'],
                                datos_cultivo['descripcionCultivo'], datos_cultivo['plagas'], datos_cultivo['enfermedades'])
    return 'OK', 200


@app.route('/cultivos/<idPlanta>', methods=['PUT'])
def editar_cultivo(idPlanta):
    datos_cultivo = request.get_json()
    autenticacion.editar_cultivo(idPlanta, datos_cultivo['nombrecientifco'], datos_cultivo['tipoCultivo'],
                                 datos_cultivo['foto'], datos_cultivo['descripcionCultivo'], datos_cultivo['plagas'], datos_cultivo['enfermedades'])
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
    return jsonify(lista), 200

@app.route('/logout', methods=['GET', 'POST'])
def process_logout():
    session.pop('usuario', None)
    return index()


def load_user(email, passwd):
    if len(autenticacion.verificar_correo(email)) == 0:
        return process_error("User not found / No existe un usuario con ese nombre")
    datos = autenticacion.verificar_correo(email)
    if datos[0][4] != passwd:
        return process_error("Incorrect password / la clave no es correcta")
    
    session['usuario'] = datos[0]
    return index()

def process_error(message):
    return render_template("error.html", error_message=message)

def process_signup():
    faltan = []
    campos = ['nombre', 'email', 'usuario', 'clave', 'confirm', 'signup_submit']
    for campo in campos:
        value = request.form.get(campo, None)
        if value is None or value == '':
            faltan.append(campo)
    if faltan:
        return render_template("missingFields.html", inputs=faltan)
    return create_user_file(request.form['nombre'], request.form['email'], request.form['usuario'], request.form['clave'], request.form['confirm'])

def create_user_file(name, email, nick, clave, clave_confirm):
    if len(autenticacion.verificar_correo(email)) >0:
        return process_error("The email is already used, you must select a different email / Ya existe un usuario con ese correo")
    if len(autenticacion.verificar_usuario(nick)) >0:
        return process_error("The nickname is already used, you must select a different nickname / Ya existe un usuario con ese nombre de usuario")
    if clave != clave_confirm:
        return process_error("Your password and confirmation password do not match / Las claves no coinciden")
    autenticacion.crear_usuario(name, email, nick, clave)
    datos = autenticacion.verificar_correo(email)
    session['usuario'] = datos[0]
    return index()

def creacion_caso(nombre, tipo, foto, desc, estado, evolucion, date, iduser):
    autenticacion.crear_caso(tipo, nombre, foto, desc, estado, evolucion, date, iduser)
    datos = autenticacion.obtener_recien(iduser, date)
    return mostrar_caso(datos[0][0])

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'  # this string is used for security reasons (see CSRF)

if __name__ == '__main__':
    app.debug = True
    app.run(port=5001)
