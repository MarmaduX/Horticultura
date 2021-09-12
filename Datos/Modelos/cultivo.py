from Datos.basededatos import BaseDeDatos


def crear_cultivo(nombreCientifico, tipoCultivo, foto, descripcionCultivo, plagas, enfermedades):
    crear_cultivo_sql = f"""
        INSERT INTO Cultivo(nombreCientifico, tipoCultivo, foto, descripcionCultivo, plagas, enfermedades)
        VALUES ('{nombreCientifico}', '{tipoCultivo}', '{foto}', '{descripcionCultivo}', '{plagas}', '{enfermedades}')
    """
    bd = BaseDeDatos()
    bd.ejecutar_sql(crear_cultivo_sql)