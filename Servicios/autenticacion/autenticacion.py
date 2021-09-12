from Datos.Modelos import usuarios as modelo_usuario, cultivo as modelo_cultivo, caso as modelo_caso, rol as modelo_rol

def crear_caso(tipoCultivo, nombrePlanta, foto, descripcionCaso, estado, evolucionCaso, fechaActualizacion, recomendaciones):
    modelo_caso.crear_caso(tipoCultivo, nombrePlanta, foto, descripcionCaso, estado, evolucionCaso, fechaActualizacion, recomendaciones)

def crear_usuario(nombre, email, usuario, clave):
    modelo_usuario.crear_usuario(nombre, email, usuario, clave)

def crear_cultivo(nombreCientifico, tipoCultivo, foto, descripcionCultivo, plagas, enfermedades):
    modelo_cultivo.crear_cultivo(nombreCientifico, tipoCultivo, foto, descripcionCultivo, plagas, enfermedades)

def crear_rol(tipoRol):
    modelo_rol.crear_rol(tipoRol)
