from Datos.Modelos import usuarios as modelo_usuario, cultivo as modelo_cultivo, caso as modelo_caso, rol as modelo_rol

def crear_caso(tipoCultivo, nombrePlanta, foto, descripcionCaso, estado, evolucionCaso, fechaActualizacion, recomendaciones):
    modelo_caso.crear_caso(tipoCultivo, nombrePlanta, foto, descripcionCaso, estado, evolucionCaso, fechaActualizacion, recomendaciones)

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
