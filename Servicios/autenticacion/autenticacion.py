from Datos.Modelos import usuarios as modelo_usuario, cultivo as modelo_cultivo, caso as modelo_caso, rol as modelo_rol

def crear_caso(tipoCultivo, nombrePlanta, foto, descripcionCaso, estado, evolucionCaso, fechaActualizacion, recomendaciones, idUs):
    modelo_caso.crear_caso(tipoCultivo, nombrePlanta, foto, descripcionCaso, estado, evolucionCaso, fechaActualizacion, recomendaciones, idUs)

def modificar_caso(idCaso, tipoCultivo, nombrePlanta, foto, caso, estado, evolucionCaso, fechaActualizacion, recomendaciones, especialsita):
    modelo_caso.modificar_caso(idCaso, tipoCultivo, nombrePlanta, foto, caso, estado, evolucionCaso, fechaActualizacion, recomendaciones, especialsita)

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

def registrar_recomendacion(idCaso, recomendaciones, estado, fechaActualizacion):
    modelo_caso.registrar_recomendacion(idCaso, recomendaciones, estado, fechaActualizacion)

def pasar_a_resuelto_un_caso(idCaso, estado, fechaActualizacion):
    modelo_caso.pasar_a_resuelto_un_caso(idCaso, estado, fechaActualizacion)

def crear_usuario(nombre, email, usuario, clave):
    modelo_usuario.crear_usuario(nombre, email, usuario, clave)

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


