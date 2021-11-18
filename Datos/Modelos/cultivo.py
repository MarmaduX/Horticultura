from Datos.basededatos import BaseDeDatos


def crear_cultivo(nombreCientifico, tipoCultivo, foto, descripcionCultivo, plagas, enfermedades):
    crear_cultivo_sql = f"""
        INSERT INTO Cultivo(nombreCientifico, tipoCultivo, foto, descripcion, plagas, enfermedades)
        VALUES ('{nombreCientifico}', '{tipoCultivo}', '{foto}', '{descripcionCultivo}', '{plagas}', '{enfermedades}')
    """
    bd = BaseDeDatos()
    bd.ejecutar_sql(crear_cultivo_sql)

def editar_cultivo(idPlanta, nombreCientifico, tipoCultivo, foto, descripcionCultivo, plagas, enfermedades):
    editar_cultivo_sql = f"""
        UPDATE Cultivo SET nombreCientifico='{nombreCientifico}', tipoCultivo='{tipoCultivo}', foto='{foto}', descripcion='{descripcionCultivo}', plagas='{plagas}', enfermedades='{enfermedades}'
        WHERE idPlanta = '{idPlanta}'
    """
    bd = BaseDeDatos()
    bd.ejecutar_sql(editar_cultivo_sql)

def ver_cultivos(keyword=None):
    ver_cultivos_sql = "SELECT * FROM Cultivo"
    if keyword:
       ver_cultivos_sql = ver_cultivos_sql + " where nombreCientifico like '%" + keyword + "%'"
    bd = BaseDeDatos()
    devolver = []
    devolver = bd.ejecutar_sql(ver_cultivos_sql)
    return devolver

def ver_cultivos_paginado(page, keyword=None):
    ver_cultivos_sql = "SELECT * FROM Cultivo"
    if keyword:
       ver_cultivos_sql = ver_cultivos_sql + " where nombreCientifico like '%" + keyword + "%'"
    start = (int(page) - 1) * 10
    ver_cultivos_sql = ver_cultivos_sql + " limit " + str(start) + ",10"
    bd = BaseDeDatos()
    return bd.ejecutar_sql(ver_cultivos_sql)

def ver_cultivo(nombre):
    ver_cultivo_sql = f"""
        SELECT * FROM Cultivo WHERE nombreCientifico = '{nombre}'
    """
    bd = BaseDeDatos()
    devolver = []
    devolver = bd.ejecutar_sql(ver_cultivo_sql)
    return devolver

def mostrar_cultivo(idPlanta):
    mostrar_cultivo_sql = f"""
        SELECT * FROM Cultivo WHERE idPlanta='{idPlanta}'
    """
    bd = BaseDeDatos()
    devolver = []
    devolver = bd.ejecutar_sql(mostrar_cultivo_sql)
    return devolver

def ver_cultivos_por_id(idPlanta):
    ver_cultivos_por_id_sql = f"""
SELECT * FROM Cultivo WHERE idPlanta='{idPlanta}'
"""
    bd = BaseDeDatos()
    devolver = []
    devolver = bd.ejecutar_sql(ver_cultivos_por_id_sql)
    return devolver

def eliminar_cultivo(idPlanta):
    eliminar_cultivo_sql = f"""
        DELETE FROM Cultivo WHERE idPlanta='{idPlanta}'
    """
    bd = BaseDeDatos()
    bd.ejecutar_sql(eliminar_cultivo_sql)

def mostrar_cultivos_por(tipoCultivo, key=None):
    mostrar_cultivo_por_sql = f"""
        SELECT * FROM Cultivo WHERE tipoCultivo='{tipoCultivo}'
    """
    if key:
       mostrar_cultivo_por_sql = mostrar_cultivo_por_sql + " and nombreCientifico like '%" + key + "%'"
    bd = BaseDeDatos()
    devolver = []
    devolver = bd.ejecutar_sql(mostrar_cultivo_por_sql)
    return devolver

def mostrar_cultivos_por_paginado(page, tipo, keyword=None):
    mostrar_cultivo_por_sql = f"SELECT * FROM Cultivo where tipoCultivo = '{tipo}'"
    if keyword:
       mostrar_cultivo_por_sql = mostrar_cultivo_por_sql + " and nombreCientifico like '%" + keyword + "%'"
    start = (int(page) - 1) * 10
    mostrar_cultivo_por_sql = mostrar_cultivo_por_sql + " limit " + str(start) + ",10"
    bd = BaseDeDatos()
    return bd.ejecutar_sql(mostrar_cultivo_por_sql)