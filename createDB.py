import sqlite3

def createDataBase():
    con = sqlite3.connect('./anime.db')
    cur = con.cursor() 
    cur.executescript("""
    CREATE TABLE IF NOT EXISTS SERIES(
        ID_Serie INT AUTO_INCREMENT,
        Nombre VARCHAR(50) NOT NULL,
        PRIMARY KEY(ID_Serie)
    );

    CREATE TABLE IF NOT EXISTS ESTADOS(
        ID_Estado INT AUTO_INCREMENT,
        Nombre VARHCAR(20) NOT NULL,
        PRIMARY KEY(ID_Estado)
    );

    CREATE TABLE IF NOT EXISTS SEXOS(
        ID_Sexo INT AUTO_INCREMENT,
        Nombre VARCHAR(30) NOT NULL,
        PRIMARY KEY(ID_Sexo)
    );

    CREATE TABLE IF NOT EXISTS PERSONAJES(
        ID INT AUTO_INCREMENT,
        Nombre VARCHAR(30) NOT NULL,
        Apellido VARCHAR(39) NOT NULL,
        Pronunciacion VARCHAR(50),
        Serie VARCHAR(50) NOT NULL,
        Fecha_Nacimiento DATE NOT NULL,
        Poder VARCHAR(50) NOT NULL,
        Descrip_Vestimenta VARCHAR(100) NOT NULL,
        Edad INT NOT NULL,
        Altura FLOAT NOT NULL,
        Sexo INT NOT NULL,
        Estado INT NOT NULL,
        Direccion VARCHAR(100) NOT NULL,
        Latitud VARCHAR(20),
        Longitud VARCHAR(20),
        Foto VARCHAR(300),
        Frase VARCHAR(100),
        PRIMARY KEY(ID)

        FOREIGN KEY (Serie) REFERENCES SERIES(ID_Serie)
        FOREIGN KEY(Sexo) REFERENCES SEXOS(ID_Sexo)
        FOREIGN KEY(Estado) REFERENCES ESTADOS(ID_Estado)
    );

    CREATE VIEW IF NOT EXISTS vwPersonaje as
    SELECT p.ID, p.Nombre, p.Apellido, ss.Nombre as Serie, p.Edad, s.Nombre as Sexo, e.Nombre as Estado, p.Poder, p.Descrip_Vestimenta, p.Altura
    FROM PERSONAJES p
    JOIN SEXOS s ON (p.Sexo = s.ID_Sexo)
    JOIN SERIES ss ON (p.Serie = ss.ID_Serie)
    JOIN ESTADOS e ON (p.Estado = e.ID_Estado);

    CREATE VIEW IF NOT EXISTS vwSINGOS AS
    SELECT CASE
        WHEN CAST(substr(Fecha_Nacimiento, 6, 2) as INT) = 12 AND CAST(substr(Fecha_Nacimiento, 9, 2) as INT) >= 22 THEN 'CAPRICORNIO'
        WHEN CAST(substr(Fecha_Nacimiento, 6, 2) as INT) = 1 AND CAST(substr(Fecha_Nacimiento, 9, 2) as INT) <= 20 THEN 'CAPRICORNIO'
        WHEN CAST(substr(Fecha_Nacimiento, 6, 2) as INT) = 1 AND CAST(substr(Fecha_Nacimiento, 9, 2) as INT) >= 21 THEN 'ACUARIO'
        WHEN CAST(substr(Fecha_Nacimiento, 6, 2) as INT) = 2 AND CAST(substr(Fecha_Nacimiento, 9, 2) as INT) <= 19 THEN 'ACUARIO'
        WHEN CAST(substr(Fecha_Nacimiento, 6, 2) as INT) = 2 AND CAST(substr(Fecha_Nacimiento, 9, 2) as INT) >= 20 THEN 'PISCIS'
        WHEN CAST(substr(Fecha_Nacimiento, 6, 2) as INT) = 3 AND CAST(substr(Fecha_Nacimiento, 9, 2) as INT) <= 20 THEN 'PISCIS'
        WHEN CAST(substr(Fecha_Nacimiento, 6, 2) as INT) = 3 AND CAST(substr(Fecha_Nacimiento, 9, 2) as INT) >= 21 THEN 'ARIES'
        WHEN CAST(substr(Fecha_Nacimiento, 6, 2) as INT) = 4 AND CAST(substr(Fecha_Nacimiento, 9, 2) as INT) <= 20 THEN 'ARIES'
        WHEN CAST(substr(Fecha_Nacimiento, 6, 2) as INT) = 4 AND CAST(substr(Fecha_Nacimiento, 9, 2) as INT) >= 21 THEN 'TAURO'
        WHEN CAST(substr(Fecha_Nacimiento, 6, 2) as INT) = 5 AND CAST(substr(Fecha_Nacimiento, 9, 2) as INT) <= 21 THEN 'TAURO'
        WHEN CAST(substr(Fecha_Nacimiento, 6, 2) as INT) = 5 AND CAST(substr(Fecha_Nacimiento, 9, 2) as INT) >= 22 THEN 'GEMINIS'
        WHEN CAST(substr(Fecha_Nacimiento, 6, 2) as INT) = 6 AND CAST(substr(Fecha_Nacimiento, 9, 2) as INT) <= 21 THEN 'GEMINIS'
        WHEN CAST(substr(Fecha_Nacimiento, 6, 2) as INT) = 6 AND CAST(substr(Fecha_Nacimiento, 9, 2) as INT) >= 22 THEN 'CANCER'
        WHEN CAST(substr(Fecha_Nacimiento, 6, 2) as INT) = 7 AND CAST(substr(Fecha_Nacimiento, 9, 2) as INT) <= 23 THEN 'CANCER'
        WHEN CAST(substr(Fecha_Nacimiento, 6, 2) as INT) = 7 AND CAST(substr(Fecha_Nacimiento, 9, 2) as INT) >= 24 THEN 'LEO'
        WHEN CAST(substr(Fecha_Nacimiento, 6, 2) as INT) = 8 AND CAST(substr(Fecha_Nacimiento, 9, 2) as INT) <= 23 THEN 'LEO'
        WHEN CAST(substr(Fecha_Nacimiento, 6, 2) as INT) = 8 AND CAST(substr(Fecha_Nacimiento, 9, 2) as INT) >= 22 THEN 'VIRGO'
        WHEN CAST(substr(Fecha_Nacimiento, 6, 2) as INT) = 9 AND CAST(substr(Fecha_Nacimiento, 9, 2) as INT) <= 23 THEN 'VIRGO'
        WHEN CAST(substr(Fecha_Nacimiento, 6, 2) as INT) = 9 AND CAST(substr(Fecha_Nacimiento, 9, 2) as INT) >= 24 THEN 'LIBRA'
        WHEN CAST(substr(Fecha_Nacimiento, 6, 2) as INT) = 10 AND CAST(substr(Fecha_Nacimiento, 9, 2) as INT) <= 23 THEN 'LIBRA'
        WHEN CAST(substr(Fecha_Nacimiento, 6, 2) as INT) = 10 AND CAST(substr(Fecha_Nacimiento, 9, 2) as INT) >= 24 THEN 'ESCORPIO'
        WHEN CAST(substr(Fecha_Nacimiento, 6, 2) as INT) = 11 AND CAST(substr(Fecha_Nacimiento, 9, 2) as INT) <= 22 THEN 'ESCORPIO'
        WHEN CAST(substr(Fecha_Nacimiento, 6, 2) as INT) = 11 AND CAST(substr(Fecha_Nacimiento, 9, 2) as INT) >= 23 THEN 'SAGITARIO'
        WHEN CAST(substr(Fecha_Nacimiento, 6, 2) as INT) = 12 AND CAST(substr(Fecha_Nacimiento, 9, 2) as INT) <= 21 THEN 'SAGITARIO'
        ELSE 'NO DISPONIBLE'
        END AS SIGNO,p.ID, p.Nombre, p.Apellido, vwp.Serie, vwp.Sexo, vwp.Estado, p.Edad, p.Poder, p.Frase
    FROM PERSONAJES p, vwPersonaje vwp
    WHERE p.ID = vwp.ID
    ORDER BY SIGNO
    """)

    con.commit()
    con.close()
    pass
