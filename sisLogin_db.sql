-- CREATE DATABASE sisLogin;
-- USE sisLogin;

CREATE TABLE Usuario (
	Id_Usuario INT IDENTITY(1,1) PRIMARY KEY,
	Usuario VARCHAR(50) NOT NULL UNIQUE,
	Nombre VARCHAR(100),
	Apellido VARCHAR(100),
	Contraseña VARCHAR(255) NOT NULL,
	Correo VARCHAR(100) UNIQUE,
	Telefono VARCHAR(20),
	FechaRegistro DATETIME2 DEFAULT SYSDATETIME(),
	Estado NVARCHAR(10) NOT NULL DEFAULT N'Activo',
    CONSTRAINT chk_estado CHECK (Estado IN (N'Activo', N'Inactivo'))
);
