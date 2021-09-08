from Datos.basededatos import BaseDeDatos

def crear_usuario(nombre, email, usuario, clave):
    crear_usuario_sql = f"""
        INSERT INTO Usuario(nombreCompleto, correo, nombreUsuario, contraseña)
        VALUES ('{nombre}', '{email}', '{usuario}', '{clave}')
    """
    bd = BaseDeDatos()
    bd.ejecutar_sql(crear_usuario_sql)   

