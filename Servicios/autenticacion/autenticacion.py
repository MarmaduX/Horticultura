from Datos.Modelos import usuarios as modelo_usuario, cultivo as modelo_cultivo, caso as modelo_caso, rol as modelo_rol

def crear_usuario(nombre, email, usuario, clave):
    modelo_usuario.crear_usuario(nombre, email, usuario, clave)

def verificar_correo(correo):
    return modelo_usuario.verificar_correo(correo)
    
def verificar_usuario(usuario):
    return modelo_usuario.verificar_usuario(usuario)

def modificar_usuario(idUsuario, nombre, usuario, correo, contraseña):
    modelo_usuario.modificar_usuario(idUsuario, nombre, usuario, correo, contraseña)

def eliminar_usuario(idUsuario):
    modelo_usuario.eliminar_usuario(idUsuario)

def login(usuario, clave):
    return modelo_usuario.login(usuario, clave)
    
def crear_caso(tipoCultivo, nombrePlanta, foto, descripcionCaso, estado, evolucionCaso, fechaActualizacion, idUs):
    modelo_caso.crear_caso(tipoCultivo, nombrePlanta, foto, descripcionCaso, estado, evolucionCaso, fechaActualizacion, idUs)

def modificar_caso(idCaso, tipoCultivo, nombrePlanta, foto, caso, estado, evolucionCaso, fechaActualizacion):
    modelo_caso.modificar_caso(idCaso, tipoCultivo, nombrePlanta, foto, caso, estado, evolucionCaso, fechaActualizacion)

def eliminar_caso(idCaso):
    modelo_caso.eliminar_caso(idCaso)

def ver_caso(nombrePlanta):
    return modelo_caso.ver_caso(nombrePlanta)

def mostrar_casos():
    return modelo_caso.mostrar_casos()

def mostrar_casos_usuario(idUsuario):
    return modelo_caso.mostrar_casos_usuario(idUsuario)

def mostrar_casos_por(tipoCultivo):
    return modelo_caso.mostrar_casos_por(tipoCultivo)

def registrar_recomendacion(idCaso, recomendaciones, estado, fechaActualizacion, especialista):
    modelo_caso.registrar_recomendacion(idCaso, recomendaciones, estado, fechaActualizacion, especialista)

def pasar_a_resuelto_un_caso(idCaso, estado, fechaActualizacion):
    modelo_caso.pasar_a_resuelto_un_caso(idCaso, estado, fechaActualizacion)

def crear_cultivo(nombreCientifico, tipoCultivo, foto, descripcionCultivo, plagas, enfermedades):
    modelo_cultivo.crear_cultivo(nombreCientifico, tipoCultivo, foto, descripcionCultivo, plagas, enfermedades)

def editar_cultivo(idPlanta, nombreCientifico, tipoCultivo, foto, descripcionCultivo, plagas, enfermedades):
    modelo_cultivo.editar_cultivo(idPlanta, nombreCientifico, tipoCultivo, foto, descripcionCultivo, plagas, enfermedades)

def listar_cultivos():
    return modelo_cultivo.listar_cultivos()

def mostar_cultivo(idPlanta):
    return modelo_cultivo.mostrar_cultivo(idPlanta)

def eliminar_cultivo(idPlanta):
    modelo_cultivo.eliminar_cultivo(idPlanta)

def mostar_cultivo_por(tipoCultivo):
    return modelo_cultivo.mostrar_cultivo_por(tipoCultivo)

def crear_rol(tipoRol):
    modelo_rol.crear_rol(tipoRol)


