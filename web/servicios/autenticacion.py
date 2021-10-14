import requests

from web.servicios import rest_api

def valirdar_credenciales(usuario, clave):
    body = {"nombre": usuario,
           "clave": clave}
    respuesta = requests.post(f'{rest_api.API_URL}/login', json=body)
    return = respuesta.status_code == 200


def crear_usuario(usuario, clave):
    body = {"nombre": usuario,
            "clave": clave}
    respuesta = requests.post(f'{rest_api.API_URL}/usuarios', json=body)
    return respuesta.status_code == 200


def obtener_usuarios():
    respuesta = requests.get(f'{rest_api.API_URL}/usuarios')
    return respuesta.json()

def crear_cultivo(nombreCientífico, tipoCultivo, descripción, plagas, enfermedades):
    body = {"nombreCientífico": nombreCientífico,
            "tipoCultivo": tipoCultivo,
            "descripción": descripción,
            "plagas": plagas,
            "enfermedades": enfermedades}
    respuesta = request.post(f'{rest_api.API_URL}/cultivos', json=body)
    return respuesta.status_code == 200

def modificar_cultivo(nombreCientífico, tipoCultivo, descripción,plagas, enfermedades):
    body = {"nombreCientífico": nombreCientífico,
            "tipoCultivo": tipoCultivo,
            "descripción": descripción,
            "plagas": plagas,
            "enfermedades": enfermedades}
    respuesta = request.put(f'{rest_api.API_URL}/cultivos', json=body)
    return respuesta.status_code == 200

def listar_cultivos(nombreCientífico, tipoCultivo, descripción, plagas, enfermedades):
    body = {"nombreCientífico": nombreCientífico,
            "tipoCultivo": tipoCultivo,
            "descripción": descripción,
            "plagas": plagas,
            "enfermedades": enfermedades}
    respuesta = request.get(f'{rest_api.API_URL}/cultivos', json=body)
    return respuesta.status_code == 200

def mostrar_cultivos(nombreCultivo, tipoCultivo):
    body = {"nombreCultivo": nombreCultivo,
            "tipoCultivo": tipoCultivo}
    respuesta = request.get(f'{rest_api.API_URL}/cutlivos', json=body)
    return respuesta.status_code == 200

def mostrar_cultivo_por(nombreCientífico, tipoCultivo, descripción, plagas, enfermedades):
    body = {"nombreCientífico": nombreCientífico,
            "tipoCultivo": tipoCultivo,
            "descripción": descripción,
            "plagas": plagas,
            "enfermedades": enfermedades}
    respuesta = request.get(f'{rest_api.API_URL}/cultivos', json=body)
    return respuesta.status_code == 200

def eliminar_cultivo():
    body = {}
    respuesta = request.delete(f'{rest_api.API_URL}/cultivos')