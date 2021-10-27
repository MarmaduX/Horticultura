from Datos.basededatos import BaseDeDatos


def crear_comentario(texto, idusuario, nombreusuario, idcaso, foto):
    crear_comentario_sql = f"""
        INSERT INTO Comentarios(texto, usuario, usuarioname, caso, foto)
	    VALUES ('{texto}', '{idusuario}', '{nombreusuario}', '{idcaso}', '{foto}')
    """
    bd = BaseDeDatos()
    bd.ejecutar_sql(crear_comentario_sql)

def obtener_comentarios(idcaso):
    obtener_comentario_sql = f"""
        SELECT * FROM Comentarios WHERE caso = '{idcaso}'
    """
    bd = BaseDeDatos()
    comentarios = []
    comentarios = bd.ejecutar_sql(obtener_comentario_sql)
    return comentarios

def obtener_comentario(idcoment):
    obtener_comentario_sql = f"""
        SELECT * FROM Comentarios WHERE comentid = '{idcoment}'
    """
    bd = BaseDeDatos()
    comentarios = []
    comentarios = bd.ejecutar_sql(obtener_comentario_sql)
    return comentarios

def cambiar_comentario(idcoment, texto, foto):
    cambiar_comentario_sql = f"""
        UPDATE Comentarios SET texto = '{texto}', foto = '{foto}'
        WHERE comentid = '{idcoment}'
    """
    bd = BaseDeDatos()
    bd.ejecutar_sql(cambiar_comentario_sql)


def eliminar_comentario(idcoment):
    eliminar_comentario_sql = f"""
        DELETE FROM Comentarios WHERE comentid = '{idcoment}'
    """
    bd = BaseDeDatos()
    bd.ejecutar_sql(eliminar_comentario_sql)
