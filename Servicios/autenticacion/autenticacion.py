from Datos.Modelos import usuarios as modelo_usuario, cultivo as modelo_cultivo, caso as modelo_caso, rol as modelo_rol, evolucionCaso as modelo_evo, comentarios as modelo_coment

def crear_usuario(nombre, email, usuario, clave):
    modelo_usuario.crear_usuario(nombre, email, usuario, clave)

def verificar_correo(correo):
    return modelo_usuario.verificar_correo(correo)

def verificar_clave(idusuario, clave):
    return modelo_usuario.verificar_clave(idusuario, clave)
       
def verificar_usuario(usuario):
    return modelo_usuario.verificar_usuario(usuario)

def devolver_usuario(iduser):
    return modelo_usuario.devolver_usuario(iduser)

def modificar_usuario(idUsuario, nombre, usuario, correo, contraseña):
    modelo_usuario.modificar_usuario(idUsuario, nombre, usuario, correo, contraseña)

def eliminar_usuario(idUsuario):
    modelo_usuario.eliminar_usuario(idUsuario)

def login(usuario, clave):
    return modelo_usuario.login(usuario, clave)
    
def crear_caso(tipoCultivo, nombrePlanta, foto, descripcionCaso, estado, evolucionCaso, fechaActualizacion, idUs):
    modelo_caso.crear_caso(tipoCultivo, nombrePlanta, foto, descripcionCaso, estado, evolucionCaso, fechaActualizacion, idUs)

def obtener_recien(iduser, date):
    return modelo_caso.obtener_recien(iduser, date)

def modificar_caso(idCaso, tipoCultivo, nombrePlanta, foto, caso, estado, evolucionCaso, fechaActualizacion):
    modelo_caso.modificar_caso(idCaso, tipoCultivo, nombrePlanta, foto, caso, estado, evolucionCaso, fechaActualizacion)

def eliminar_caso(idCaso):
    modelo_caso.eliminar_caso(idCaso)

def ver_caso(nombrePlanta):
    return modelo_caso.ver_caso(nombrePlanta)

def mostrar_casos(key):
    return modelo_caso.mostrar_casos(key)

def mostrar_casos_paginado(page, key):
    return modelo_caso.mostrar_casos_paginado(page, key)

def mostrar_casos_usuario(idUsuario):
    return modelo_caso.mostrar_casos_usuario(idUsuario)

def mostrar_casos_especialista(idUsuario):
    return modelo_caso.mostrar_casos_especialista(idUsuario)
    
def mostrar_casos_por(key, tipoCultivo):
    return modelo_caso.mostrar_casos_por(tipoCultivo, key)

def mostrar_casos_por_paginado(page, key, tipo):
    return modelo_caso.mostrar_casos_por_paginado(page,tipo, key)

def registrar_recomendacion(idCaso, recomendaciones, estado, fechaActualizacion, especialista):
    modelo_caso.registrar_recomendacion(idCaso, recomendaciones, estado, fechaActualizacion, especialista)

def pasar_a_resuelto_un_caso(idCaso, estado, fechaActualizacion):
    modelo_caso.pasar_a_resuelto_un_caso(idCaso, estado, fechaActualizacion)

def crear_cultivo(nombreCientifico, tipoCultivo, foto, descripcionCultivo, plagas, enfermedades):
    modelo_cultivo.crear_cultivo(nombreCientifico, tipoCultivo, foto, descripcionCultivo, plagas, enfermedades)

def editar_cultivo(idPlanta, nombreCientifico, tipoCultivo, foto, descripcionCultivo, plagas, enfermedades):
    modelo_cultivo.editar_cultivo(idPlanta, nombreCientifico, tipoCultivo, foto, descripcionCultivo, plagas, enfermedades)

def ver_cultivos(key):
    return modelo_cultivo.ver_cultivos(key)

def ver_cultivos_paginado(page, key):
    return modelo_cultivo.ver_cultivos_paginado(page, key)

def mostar_cultivo(idPlanta):
    return modelo_cultivo.mostrar_cultivo(idPlanta)

def ver_cultivos_por_id(idPlanta):
    return modelo_cultivo.ver_cultivos_por_id(idPlanta)

def eliminar_cultivo(idPlanta):
    modelo_cultivo.eliminar_cultivo(idPlanta)

def mostrar_cultivos_filtrados(key, tipoCultivo):
    return modelo_cultivo.mostrar_cultivos_por(tipoCultivo, key)

def mostrar_cultivos_filtrados_paginado(page, key, tipoCultivo):
    return modelo_cultivo.mostrar_cultivos_por_paginado(page, tipoCultivo, key)

def crear_rol(tipoRol):
    modelo_rol.crear_rol(tipoRol)

def crear_comentario(texto, idusuario, nombreusuario, idcaso, foto):
    modelo_coment.crear_comentario(texto, idusuario, nombreusuario, idcaso, foto)

def obtener_comentarios(idcaso):
    return modelo_coment.obtener_comentarios(idcaso)

def obtener_comentario(idcoment):
    return modelo_coment.obtener_comentario(idcoment)

def cambiar_comentario(idcoment, texto, foto):
    modelo_coment.cambiar_comentario(idcoment, texto, foto)

def eliminar_comentario(idcoment):
    modelo_coment.eliminar_comentario(idcoment)

def crear_evolucion(texto, idcaso, foto):
    modelo_evo.crear_evolucion(texto, idcaso, foto)

def obtener_evoluciones(idcaso):
    return modelo_evo.obtener_evoluciones(idcaso)

def obtener_evolucion(idevo):
    return modelo_evo.obtener_evolucion(idevo)

def cambiar_evolucion(idevo, texto, foto):
    modelo_evo.cambiar_evolucion(idevo, texto, foto)

def eliminar_evolucion(idevo):
    modelo_evo.eliminar_evolucion(idevo)
