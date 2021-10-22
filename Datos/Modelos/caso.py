from Datos.basededatos import BaseDeDatos
import pymysql

def crear_caso(tipoCultivo, nombrePlanta, foto, descripcionCaso, estado, evolucionCaso, fechaActualizacion, idUsuario):
    crear_caso_sql = f"""
        INSERT INTO Caso(tipoCultivo, nombrePlanta, foto, descripcionCaso, estado, evolucionCaso, fechaActualizacion, recomendaciones, usuarioPropietario)
        VALUES ('{tipoCultivo}', '{nombrePlanta}', '{foto}', '{descripcionCaso}', '{estado}', '{evolucionCaso}', '{fechaActualizacion}', "Aun no tiene una recomendacion", '{idUsuario}')       
    """
    bd = BaseDeDatos()
    bd.ejecutar_sql(crear_caso_sql)

def obtener_recien(iduser, date):
    obtener_recien_sql = f"""
        SELECT * FROM Caso WHERE fechaActualizacion='{date}' AND usuarioPropietario = '{iduser}'
    """
    bd = BaseDeDatos()
    devolver = []
    devolver = bd.ejecutar_sql(obtener_recien_sql)
    return devolver

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

def mostrar_casos(keyword=None):
    mostrar_casos_sql = "SELECT * FROM Caso"
    if keyword:
       mostrar_casos_sql = mostrar_casos_sql + " where nombrePlanta like '%" + keyword + "%'"
    bd = BaseDeDatos()
    return bd.ejecutar_sql(mostrar_casos_sql)

def mostrar_casos_paginado(page, keyword=None):
    mostrar_casos_sql = "SELECT * FROM Caso"
    if keyword:
       mostrar_casos_sql = mostrar_casos_sql + " where nombrePlanta like '%" + keyword + "%'"
    start = (int(page) - 1) * 10
    mostrar_casos_sql = mostrar_casos_sql + " limit " + str(start) + ",10"
    bd = BaseDeDatos()
    return bd.ejecutar_sql(mostrar_casos_sql)

def mostrar_casos_usuario(idUsuario):
    mostrar_caso_por_sql = f"""
        SELECT * FROM Caso WHERE usuarioPropietario = '{idUsuario}'
    """
    bd = BaseDeDatos()
    return bd.ejecutar_sql(mostrar_caso_por_sql)

def mostrar_casos_especialista(idUsuario):
    mostrar_caso_por_sql = f"""
        SELECT * FROM Caso WHERE usuarioEspecialista = '{idUsuario}'
    """
    bd = BaseDeDatos()
    return bd.ejecutar_sql(mostrar_caso_por_sql)

def mostrar_casos_por(tipo, key=None):
    mostrar_casos_sql = f"""
        SELECT * FROM Caso where tipoCultivo = '{tipo}'
    """
    if key:
       mostrar_casos_sql = mostrar_casos_sql + " and nombrePlanta like '%" + key + "%'"
    bd = BaseDeDatos()
    return bd.ejecutar_sql(mostrar_casos_sql)

def mostrar_casos_por_paginado(page, tipo, keyword=None):
    mostrar_casos_sql = f"SELECT * FROM Caso where tipoCultivo = '{tipo}'"
    if keyword:
       mostrar_casos_sql = mostrar_casos_sql + " and nombrePlanta like '%" + keyword + "%'"
    start = (int(page) - 1) * 10
    mostrar_casos_sql = mostrar_casos_sql + " limit " + str(start) + ",10"
    bd = BaseDeDatos()
    return bd.ejecutar_sql(mostrar_casos_sql)

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