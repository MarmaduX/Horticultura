from Datos.basededatos import BaseDeDatos

def verificar_correo(email):
    verificar_correo_sql = f"""
        SELECT * FROM Usuario WHERE correo = "{email}" 
    """
    bd = BaseDeDatos()
    existe = []
    existe = bd.ejecutar_sql(verificar_correo_sql)
    return existe

def verificar_clave(id, clave):
    verificar_correo_sql = f"""
        SELECT * FROM Usuario WHERE idUsuario = "{id}" and contraseña = "{clave}"
    """
    bd = BaseDeDatos()
    existe = []
    existe = bd.ejecutar_sql(verificar_correo_sql)
    return existe
    
def verificar_usuario(usuario):
    verificar_usuario_sql = f"""
        SELECT * FROM Usuario WHERE nombreUsuario = "{usuario}" 
    """
    bd = BaseDeDatos()
    existe = []
    existe = bd.ejecutar_sql(verificar_usuario_sql)
    return existe

def crear_usuario(nombreCompleto, correo, nombreUsuario, contraseña):
    crear_usuario_sql = f"""
        INSERT INTO Usuario(nombreCompleto, correo, nombreUsuario, contraseña)
        VALUES ('{nombreCompleto}', '{correo}', '{nombreUsuario}', '{contraseña}')
    """
    bd = BaseDeDatos()
    bd.ejecutar_sql(crear_usuario_sql)

def modificar_usuario(idUsuario, nombre, usuario, correo, contraseña):
    modificar_usuario_sql = f"""
        UPDATE Usuario SET nombreUsuario = '{usuario}', nombreCompleto = '{nombre}', correo = '{correo}', contraseña = '{contraseña}'
        WHERE idUsuario = '{idUsuario}'
    """
    bd = BaseDeDatos()
    bd.ejecutar_sql(modificar_usuario_sql)

def eliminar_usuario(idUsuario):
    eliminar_usuario_sql = f"""
        DELETE FROM Usuario WHERE idUsuario = '{idUsuario}'
    """
    bd = BaseDeDatos()
    bd.ejecutar_sql(eliminar_usuario_sql)

def login(nombreUsuario, clave):
    ingresar_sql = f"""
        SELECT * FROM Usuario WHERE nombreUsuario = '{nombreUsuario}' AND contraseña = '{clave}'
    """
    bd = BaseDeDatos()
    existe = []
    existe = bd.ejecutar_sql(ingresar_sql)
    return existe
