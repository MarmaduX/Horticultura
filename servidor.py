from flask import Flask, request,  render_template, jsonify, json, session, url_for
from Servicios.autenticacion import autenticacion
import math

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
    return render_template("signup.html",error="", correo="", username="", nombre=""), 200


@app.route('/usuario', methods=['POST', "GET"])
def modificar_usuario():
    return render_template("editar_usuario.html", usuario=session['usuario'], rol = session['usuario'][5]), 200

@app.route('/formulario_us', methods=['POST', 'GET'])
def formulario_us():
    if request.method == 'POST':
        if verificar_clave(request.form["vieja"]) == "Ok":
            if session["usuario"][2] == request.form['email']:
                if session["usuario"][3] == request.form['usuario']:
                    autenticacion.modificar_usuario(session['usuario'][0], request.form['nombre'], request.form['usuario'], request.form['email'], request.form['vieja'])
                    datos = autenticacion.verificar_correo(request.form['email'])
                    session["usuario"]=datos[0]
                    return modificar_usuario()
                if len(autenticacion.verificar_usuario(request.form['usuario'])) == 0:
                    autenticacion.modificar_usuario(session['usuario'][0], request.form['nombre'], request.form['usuario'], request.form['email'], request.form['vieja'])
                    datos = autenticacion.verificar_correo(request.form['email'])
                    session["usuario"] = datos[0]
                    return modificar_usuario()
                return render_template("formulario_us.html", usuario=session['usuario'], rol = session['usuario'][5], error="Este usuario ya esta en uso")
            if len(autenticacion.verificar_correo(request.form['email'])) ==0:
                if session["usuario"][3] == request.form['usuario']:
                        autenticacion.modificar_usuario(session['usuario'][0], request.form['nombre'], request.form['usuario'], request.form['email'], request.form['vieja'])
                        datos = autenticacion.verificar_correo(request.form['email'])
                        session["usuario"]=datos[0]
                        return modificar_usuario()
                return render_template("formulario_us.html", usuario=session['usuario'], rol = session['usuario'][5], error="Este usuario ya esta en uso", nombre=request.form["nombre"], correo=request.form["email"], username=request.form["usuario"])
            return render_template("formulario_us.html", usuario=session['usuario'], rol = session['usuario'][5], error="Este correo ya esta en uso", nombre=request.form["nombre"], correo=request.form["email"], username=request.form["usuario"])
        return render_template("formulario_us.html", usuario=session['usuario'], rol = session['usuario'][5], error="Contraseña Invalida", nombre=request.form["nombre"], correo=request.form["email"], username=request.form["usuario"]), 200
    return render_template("formulario_us.html", usuario=session['usuario'], rol = session['usuario'][5], error="", nombre=session["usuario"][1], correo=session["usuario"][2], username=session["usuario"][3])

@app.route('/formulario_clave', methods=['POST', 'GET'])
def formulario_clave():
    if request.method == 'POST':
        if verificar_clave(request.form["vieja"]) == "Ok":
            autenticacion.modificar_usuario(session['usuario'][0], session['usuario'][1], session['usuario'][3],session['usuario'][2], request.form['clave'])
            return render_template("editar_usuario.html", usuario=session['usuario'], rol = session['usuario'][5])
        return render_template("formulario_clave.html", usuario=session['usuario'], rol = session['usuario'][5], error="Contraseña Invalida", nueva=request.form["clave"], confirm=request.form["confirm"])
    return render_template("formulario_clave.html", usuario=session['usuario'], rol = session['usuario'][5], error="", nueva="", confirm="")

def verificar_clave(clave):
    pase = autenticacion.verificar_clave(session["usuario"][0], clave)
    if pase == []:
        return "Contraseñas Incorrectas"
    return "Ok"

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
        return load_user(request.form['email'], request.form['clave'])

    return render_template("login.html", error="", email=""), 200


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
        return creacion_caso(request.form['nombre'], request.form['tipo'], request.form['show'], request.form['desc'], request.form['estado'], request.form['evolucion'], request.form['date'], idUsuario)
        
    return render_template("ingreso_caso.html", userid=idUsuario, nickname=session['usuario'][3], rol = session['usuario'][5])

@app.route('/modificar_caso/<idCaso>', methods=['GET', 'POST'])
def modificar_caso(idCaso):
    datos = autenticacion.ver_caso(idCaso)
    if request.method == 'POST':
        autenticacion.modificar_caso(idCaso, request.form['tipo'], request.form['nombre'], request.form['show'],
                                 request.form['desc'], request.form['estado'], request.form['evolucion'], request.form['date'])
        return mostrar_caso(idCaso)
    return render_template("editar_caso.html", caso=datos[0], idcaso=idCaso, usuario=session["usuario"], rol = session['usuario'][5])

@app.route('/eliminar_caso', methods=['DELETE'])
def eliminar_casos():
    idcaso = request.form.get("idcaso")
    autenticacion.eliminar_caso(idcaso)
    return render_template("index.html")

@app.route('/casos', methods=['GET'])
def mostrar_casos():
    page = request.args.get('page')
    if not page or int(page) == 0:
        page = 1
    if request.args.get('keyword') == None:
        keyword = ""
    else:
        keyword = request.args.get('keyword')
    casos_a_mostrar = autenticacion.mostrar_casos(keyword)
    cantidad = len(casos_a_mostrar)
    cantidad = math.ceil(cantidad/10)
    if int(page)>cantidad:
        page=cantidad
    page_range = range(int(page) - 2, int(page) + 3)
    if int(page)+3>cantidad:
        page_range= range(int(page)-3, cantidad+1)
    if int(page) < 4:
        if cantidad < 5:
            page_range = range(1, cantidad+1)
        else: 
            page_range = range(1, cantidad+1)
    casos_a_mostrar = autenticacion.mostrar_casos_paginado(int(page), keyword)
    return render_template("allcasos.html", palabra=keyword, usuario = session["usuario"], casos=casos_a_mostrar, items=casos_a_mostrar,page=int(page),prange = page_range), 200

@app.route('/vercaso/<idCaso>', methods=['GET'])
def mostrar_caso(idCaso):
    datos = autenticacion.ver_caso(idCaso)
    especialista = autenticacion.devolver_usuario(datos[0][10])
    if especialista == []:
        nombreespecial = "Aun no tiene un especialista asignado"
    else:
        nombreespecial = especialista[0][1]
    return render_template("caso.html", rol=session['usuario'][5], idcaso=idCaso, tipo=datos[0][1], nombre=datos[0][2], fotos=datos[0][3], texto=datos[0][4], estado=datos[0][5], evolucion=datos[0][6], date=datos[0][7], recomendacion=datos[0][8], userid=datos[0][9], especialista=nombreespecial, usuario=session['usuario']), 200


@app.route('/casos/<idUsuario>', methods=['GET'])
def mostrar_caso_por(idUsuario):
    if session["usuario"][5] == 1:
        casos_a_mostrar = autenticacion.mostrar_casos_usuario(idUsuario)
    else:
        casos_a_mostrar = autenticacion.mostrar_casos_especialista(idUsuario)
    return render_template("casos_usuario.html", casos = casos_a_mostrar, usuario=session["usuario"], rol = session['usuario'][5])


@app.route('/casos/tipo/<tipoCultivo>', methods=['GET'])
def mostrar_casos_por(tipoCultivo):
    page = request.args.get('page')
    if not page or int(page) == 0:
        page = 1
    if request.args.get('keyword') == None:
        keyword = ""
    else:
        keyword = request.args.get('keyword')
    casos_a_mostrar = autenticacion.mostrar_casos_por(keyword, tipoCultivo)
    cantidad = len(casos_a_mostrar)
    cantidad = math.ceil(cantidad/10)
    if int(page)>cantidad:
        page=cantidad
    page_range = range(int(page) - 2, int(page) + 3)
    if int(page)+3>cantidad:
        page_range= range(int(page)-3, cantidad+1)
    if int(page) < 4:
        if cantidad < 5:
            page_range = range(1, cantidad+1)
        else: 
            page_range = range(1, cantidad+1)
    casos_a_mostrar = autenticacion.mostrar_casos_por_paginado(int(page), keyword, tipoCultivo)
    return render_template("casostipo.html", tipo=tipoCultivo, palabra=keyword, usuario = session["usuario"], casos=casos_a_mostrar, items=casos_a_mostrar, page=int(page), prange = list(page_range)), 200

@app.route('/caso/recomendacion/<idCaso>', methods=["GET","POST"])
def registrar_recomendacion(idCaso):
    if request.method == "POST":
        autenticacion.registrar_recomendacion(idCaso, request.form["rec"],  request.form["estado"],  request.form["date"], session["usuario"][0])
        return mostrar_caso(idCaso)
    return render_template("casorec.html", idcaso = idCaso, usuario=session["usuario"], rol = session['usuario'][5])

@app.route('/casos/finalizar', methods=['PUT'])
def pasar_a_resuelto_un_caso():
    idcaso = request.form.get("idcaso")
    date = request.form.get("date")
    autenticacion.pasar_a_resuelto_un_caso(idcaso, "Finalizado", date)
    return 'OK', 200


@app.route('/cultivos', methods=['POST'])
def crear_cultivo():
    datos_cultivo = request.get_json()
    autenticacion.crear_cultivo(datos_cultivo['nombreCientifico'], datos_cultivo['tipoCultivo'], datos_cultivo['foto'], datos_cultivo['descripcionCultivo'], datos_cultivo['plagas'], datos_cultivo['enfermedades'])
    return render_template("cultivos.html")


@app.route('/cultivos/<idPlanta>', methods=['PUT'])
def editar_cultivo(idPlanta):
    datos_cultivo = request.get_json()
    autenticacion.editar_cultivo(idPlanta, datos_cultivo['nombreCientifco'], datos_cultivo['tipoCultivo'],
                                 datos_cultivo['foto'], datos_cultivo['descripcionCultivo'], datos_cultivo['plagas'], datos_cultivo['enfermedades'])
    return "OK", 200


@app.route('/cultivos', methods=['GET'])
def listar_cultivos():
    lista = autenticacion.listar_cultivos()
    return render_template("cultivos.html")


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
        return render_template("login.html", error="Este correo no esta registrado", email=request.form["email"])
    datos = autenticacion.verificar_correo(email)
    if datos[0][4] != passwd:
        return render_template("login.html", error="Contraseña erronea", email=request.form["email"])
    session['usuario'] = datos[0]
    return index()

def process_signup():
    if len(autenticacion.verificar_correo(request.form['email'])) >0:
        return render_template("signup.html", error="Ya existe un usuario con ese correo", correo=request.form['email'], username=request.form['usuario'], nombre=request.form['nombre'])
    if len(autenticacion.verificar_usuario(request.form['usuario'])) >0:
        return render_template("signup.html", error="Ya existe un usuario con ese nombre de usuario", correo=request.form['email'], username=request.form['usuario'], nombre=request.form['nombre'])
    autenticacion.crear_usuario(request.form['nombre'], request.form['email'], request.form['usuario'],  request.form['clave'])
    datos = autenticacion.verificar_correo(request.form['email'])
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
