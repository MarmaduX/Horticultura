CREATE TABLE Rol (
  idRol INTEGER PRIMARY KEY AUTOINCREMENT,
  tipoRol varchar(20)
);

INSERT INTO Rol (tipoRol) VALUES ("Usuario Común");
INSERT INTO Rol (tipoRol) VALUES ("Usuario Administrador");

CREATE TABLE Usuario (
    idUsuario INTEGER PRIMARY KEY AUTOINCREMENT,
    nombreCompleto varchar(50),
    correo varchar(50),
    nombreUsuario varchar(50),
    contraseña varchar(50)
);
CREATE TABLE Caso (
  idCaso INTEGER PRIMARY KEY AUTOINCREMENT,
  tipoCultivo varchar(50),
  nombrePlanta varchar(50),
  foto VARBINARY(200),
  descripcionCaso varchar(200),
  estado varchar(50),
  evolucionCaso varchar(50),
  fechaActualizacion SmallDateTime, 
  recomendaciones varchar(200)
);
CREATE TABLE Cultivo (
  idPlanta INTEGER PRIMARY KEY AUTOINCREMENT,
  nombreCientifico varchar(50), 
  tipoCultivo varchar(50),
  foto VARBINARY (200), 
  descripcionCultivo varchar(200),
  plagas varchar(200),
  enfermedades varchar(200)
);

ALTER TABLE Usuario ADD idRol INTEGER REFERENCES Rol (idRol) default 1;
ALTER TABLE Caso ADD usuarioPropietario INTEger REFERENCES Usuario (idusuario);
ALTER TABLE Caso ADD usuarioEspecialista INTEger REFERENCES Usuario (idusuario);


 
