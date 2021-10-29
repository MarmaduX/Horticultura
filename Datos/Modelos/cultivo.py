from Datos.basededatos import BaseDeDatos


def crear_cultivo(nombreCientifico, tipoCultivo, foto, descripcionCultivo, plagas, enfermedades):
    crear_cultivo_sql = f"""
        INSERT INTO Cultivo(nombreCientifico, tipoCultivo, foto, descripcionCultivo, plagas, enfermedades)
        VALUES ('{nombreCientifico}', '{tipoCultivo}', '{foto}', '{descripcionCultivo}', '{plagas}', '{enfermedades}')
    """
    bd = BaseDeDatos()
    bd.ejecutar_sql(crear_cultivo_sql)

def editar_cultivo(idPlanta, nombreCientifico, tipoCultivo, foto, descripcionCultivo, plagas, enfermedades):
    editar_cultivo_sql = f"""
        UPDATE Cultivo SET nombreCientifico='{nombreCientifico}', tipoCultivo='{tipoCultivo}', foto='{foto}', descripcionCultivo='{descripcionCultivo}', plagas='{plagas}', enfermedades='{enfermedades}'
        WHERE idPlanta = '{idPlanta}'
    """
    bd = BaseDeDatos()
    bd.ejecutar_sql(editar_cultivo_sql)

def ver_cultivos():
    ver_cultivos_sql = f"""
        SELECT * FROM Cultivo
    """
    bd = BaseDeDatos()
    return bd.ejecutar_sql(ver_cultivos_sql)

def mostrar_cultivo(idPlanta):
    mostrar_cultivo_sql = f"""
        SELECT * FROM Cultivo WHERE idPlanta='{idPlanta}'
    """
    bd = BaseDeDatos()
    return bd.ejecutar_sql(mostrar_cultivo_sql)

def eliminar_cultivo(idPlanta):
    eliminar_cultivo_sql = f"""
        DELETE FROM Cultivo WHERE idPlanta='{idPlanta}'
    """
    bd = BaseDeDatos()
    bd.ejecutar_sql(eliminar_cultivo_sql)

def mostrar_cultivo_por(tipoCultivo):
    mostrar_cultivo_por_sql = f"""
        SELECT * FROM Cultivo WHERE tipoCultivo='{tipoCultivo}'
    """
    bd = BaseDeDatos()
    return bd.ejecutar_sql(mostrar_cultivo_por_sql)
