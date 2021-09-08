import sqlite3

sql_tabla_rol = '''CREATE TABLE Rol (
        idRol INTEGER PRIMARY KEY AUTOINCREMENT,
        tipoRol varchar(20)
    );'''

sql_valores_rol = '''INSERT INTO Rol (tipoRol) VALUES ("Usuario Común");
    INSERT INTO Rol (tipoRol) VALUES ("Usuario Administrador");
    '''

sql_tabla_usuario = '''CREATE TABLE Usuario (
        idUsuario INTEGER PRIMARY KEY AUTOINCREMENT,
        nombreCompleto varchar(50),
        correo varchar(50),
        nombreUsuario varchar(50),
        contraseña varchar(50)
    );'''

sql_tabla_caso = '''CREATE TABLE Caso (
        idCaso INTEGER PRIMARY KEY AUTOINCREMENT,
        tipoCultivo varchar(50),
        nombrePlanta varchar(50),
        foto VARBINARY(200),
        descripcionCaso varchar(200),
        estado varchar(50),
        evolucionCaso varchar(50),
        fechaActualizacion SmallDateTime, 
        recomendaciones varchar(200)
    );'''

sql_tabla_cultivo = '''CREATE TABLE Cultivo (
        idPlanta INTEGER PRIMARY KEY AUTOINCREMENT,
        nombreCientifico varchar(50), 
        tipoCultivo varchar(50),
        foto VARBINARY (200), 
        descripcionCultivo varchar(200),
        plagas varchar(200),
        enfermedades varchar(200)
    );'''

sql_tabla_alters = '''ALTER TABLE Usuario ADD idRol INTEGER REFERENCES Rol (idRol) default 1;
    ALTER TABLE Caso ADD usuarioPropietario INTEger REFERENCES Usuario (idusuario);
    ALTER TABLE Caso ADD usuarioEspecialista INTEger REFERENCES Usuario (idusuario);
    '''

if __name__ == '__main__':
    try:
        print('Creando Base de Datos...')
        conexion = sqlite3.connect('..\Horticultura\horticultura.db')

        print('Creando Tablas...')
        conexion.executescript(sql_tabla_rol)
        conexion.executescript(sql_valores_rol)
        conexion.executescript(sql_tabla_usuario)
        conexion.executescript(sql_tabla_caso)
        conexion.executescript(sql_tabla_cultivo)
        conexion.executescript(sql_tabla_alters)

        conexion.close()
        print('Creacion finalizada.')
    except Exception as e:
        print(f'Error creando base de datos:{e}', e)