from Datos.basededatos import BaseDeDatos


def crear_caso(tipoCultivo, nombrePlanta, foto, descripcionCaso, estado, evolucionCaso, fechaActualizacion, idUsuario):
    crear_caso_sql = f"""
        INSERT INTO Caso(tipoCultivo, nombrePlanta, foto, descripcionCaso, estado, evolucionCaso, fechaActualizacion, usuarioPropietario)
        VALUES ('{tipoCultivo}', '{nombrePlanta}', '{foto}', '{descripcionCaso}', '{estado}', '{evolucionCaso}', '{fechaActualizacion}', '{idUsuario}')       
    """
    bd = BaseDeDatos()
    bd.ejecutar_sql(crear_caso_sql)

def modificar_caso(idCaso, tipoCultivo, nombrePlanta, foto, descripcionCaso, estado, evolucionCaso, fecha):
    modificar_caso_sql = f"""
        UPDATE Caso SET tipoCultivo = '{tipoCultivo}', nombrePlanta = '{nombrePlanta}', foto = '{foto}', descripcionCaso = '{descripcionCaso}', estado = '{estado}', evolucionCaso = '{evolucionCaso}', fechaActualizacion = '{fecha}'
        WHERE idCaso = '{idCaso}'
    """
    bd = BaseDeDatos()
    bd.ejecutar_sql(modificar_caso_sql)

def eliminar_caso(idCaso):
    eliminar_caso_sql = f"""
        DELETE FROM Caso WHERE idCaso = '{idCaso}'
    """
    bd = BaseDeDatos()
    bd.ejecutar_sql(eliminar_caso_sql)

def ver_caso(idCaso):
    ver_caso_sql = f"""
        SELECT * FROM Caso WHERE idCaso = '{idCaso}'
    """
    bd = BaseDeDatos()
    return bd.ejecutar_sql(ver_caso_sql)

def mostrar_casos():
    mostrar_casos_sql = f"""
        SELECT * FROM Caso
    """
    bd = BaseDeDatos()
    return bd.ejecutar_sql(mostrar_casos_sql)

def mostrar_casos_usuario(idUsuario):
    mostrar_caso_por_sql = f"""
        SELECT * FROM Caso WHERE usuarioPropietario = '{idUsuario}'
    """
    bd = BaseDeDatos()
    return bd.ejecutar_sql(mostrar_caso_por_sql)

def mostrar_casos_por(tipoCultivo):
    mostrar_casos_por_sql = f"""
        SELECT * FROM Caso WHERE tipoCultivo = '{tipoCultivo}'
    """
    bd = BaseDeDatos()
    return bd.ejecutar_sql(mostrar_casos_por_sql)

def registrar_recomendacion(idCaso, recomendaciones, estado, fechaActualizacion, especialista):
    registrar_recomendacion_sql = f"""
        UPDATE Caso SET recomendaciones = '{recomendaciones}', estado = '{estado}', fechaActualizacion = '{fechaActualizacion}', usuarioEspecialista = '{especialista}'
        WHERE idCaso= '{idCaso}'
    """
    bd = BaseDeDatos()
    bd.ejecutar_sql(registrar_recomendacion_sql)

def pasar_a_resuelto_un_caso(idCaso, estado, fechaActualizacion):
    pasar_a_resuelto_un_caso_sql = f"""
        UPDATE Caso SET estado= '{estado}', fechaActualizacion= '{fechaActualizacion}'
        WHERE idCaso = '{idCaso}'
    """
    bd = BaseDeDatos()
    bd.ejecutar_sql(pasar_a_resuelto_un_caso_sql)