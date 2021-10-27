from Datos.basededatos import BaseDeDatos

def crear_evolucion(texto, idcaso, foto):
    crear_evolucion_sql = f"""
        INSERT INTO Evolucion(texto, caso, foto)
	    VALUES ('{texto}', '{idcaso}', '{foto}')
    """
    bd = BaseDeDatos()
    bd.ejecutar_sql(crear_evolucion_sql)

def obtener_evolucion(idcaso):
    obtener_evolucion_sql = f"""
        SELECT * FROM Evolucion WHERE caso = '{idcaso}'
    """
    bd = BaseDeDatos()
    comentarios = []
    comentarios = bd.ejecutar_sql(obtener_evolucion_sql)
    return comentarios

def cambiar_evolucion(idevo, texto, foto):
    cambiar_evolucion_sql = f"""
        UPDATE Evolucion SET texto = '{texto}', foto = '{foto}'
        WHERE evolucionid = '{idevo}'
    """
    bd = BaseDeDatos()
    bd.ejecutar_sql(cambiar_evolucion_sql)

def eliinar_evolucion(idevo):
    eliinar_evolucion_sql = f"""
        DELETE FROM Evolucion WHERE evolucionid = '{idevo}'
    """
    bd = BaseDeDatos()
    bd.ejecutar_sql(eliinar_evolucion_sql)
