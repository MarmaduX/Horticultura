from Datos.basededatos import BaseDeDatos

def crear_rol(tipoRol):
    crear_rol_sql = f"""
       INSERT INTO Rol(tipoRol)
       VALUES ('{tipoRol}')
    """
    bd = BaseDeDatos()
    bd.ejecutar_sql(crear_rol_sql)