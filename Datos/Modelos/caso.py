from Datos.basededatos import BaseDeDatos


def crear_caso(tipoCultivo, nombrePlanta, foto, descripcionCaso, estado, evolucionCaso, fechaActualizacion, recomendaciones):
    crear_caso_sql = f"""
        INSERT INTO Caso(tipoCultivo, nombrePlanta, foto, descripcionCaso, estado, evolucionCaso, fechaActualizacion, recomendaciones)
        VALUES ('{tipoCultivo}', '{nombrePlanta}', '{foto}', '{descripcionCaso}', '{estado}', '{evolucionCaso}', '{fechaActualizacion}', '{recomendaciones}')       
    """
    bd = BaseDeDatos()
    bd.ejecutar_sql(crear_caso_sql)