from math import e
import os
import time
import sqlite3
from prettytable import *
import folium
import webbrowser

con = sqlite3.connect('./anime.db')
cur = con.cursor()

m = folium.Map(location=[14.2795375, -91.1322556], zoom_start=4)

def limpiar():
    os.system('cls')
    pass

def verRegistrosDelaTabla(ntabla):
    cur.execute(f"SELECT * FROM {ntabla.upper()}")
    mytable = from_db_cursor(cur)
    print(mytable)

def confirmarModificacion(campo, valor):
    nv = input(f'El valor actual del campo {campo.upper()} es ({valor}), si no quiere modificar el valor presione ENTER\n> ')
    if nv == '':
        return valor
    else:
        return nv

def sleep(t):
    time.sleep(t)


# -------------------------------------- PERSONAJES --------------------------------------
def registrar():
    limpiar()
    print('---- Registrar Personaje ----')
    print('Lista de Personajes')
    verRegistrosDelaTabla('vwPersonaje')
    idPersonaje = int(input('Introduce el ID del personaje, para cancelar este proceso solo presiona ENTER\n> '))

    if idPersonaje == '':
        print('PROCESO CANCELADO')
        sleep(2)
    else:
        nombre = input('Introduce en NOMBRE del personaje\n> ')
        apellido = input('Introduce el APELLIDO del personaje\n> ')
        pronunciacion = input('Introduce la PRONUNCIACION del nombre del personaje\n> ')

        verRegistrosDelaTabla('SERIES')
        serie = int(input('Introduce el ID de la SERIE que pertenece el personaje\n> '))

        fecNaci = input('Introduce la FECHA DE NACIMIENTO del personaje (yyyy-mm-dd)\n> ')
        poder = input('Introduce el PODER principal del personaje\n> ')
        desVest = input('Introduce una DESCRIPCION de la VESTIMENTA del personaje\n> ')
        edad = int(input('Introduce la EDAD del personaje\n> '))
        altura = float(input('Introduce la ALTURA del personaje (metros)\n> '))

        verRegistrosDelaTabla('SEXOS')
        sexo = int(input('Introduce el ID del SEXO del personaje\n> '))

        verRegistrosDelaTabla('ESTADOS')
        estado = input('Introduce el ID del ESTADO del personaje\n> ')

        direccion = input('Introduce la DIRECCION del personaje\n> ')
        latitud = input('Introduce la LATITUDE de la ubicacion del personaje, si la ubicacion no existe en la tierra solo precione ENTER\n> ')
        longitud = input('Introduce la LONGITUD de la ubicacion del personaje, si la ubicacion no existe en la tierra solo precione ENTER\n> ')

        if latitud == '' and longitud == '':
            latitud = "18.1213598"
            longitud = "-71.4568437"
        
        foto = input('Introduce una URL de la FOTO del personaje\n> ')
        frase = input('Introduce la FRASE favorita del personaje\n>')

        datos = (
            idPersonaje,
            nombre,
            apellido,
            pronunciacion,
            serie,
            fecNaci,
            poder,
            desVest,
            edad,
            altura,
            sexo,
            estado,
            direccion,
            latitud,
            longitud,
            foto,
            frase
        )
        
        cur.execute("INSERT INTO PERSONAJES VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",datos)
        con.commit()
        
        print('PROCESO TERMINADO')
        time.sleep(3)
        pass

def modificar():
    registroExiste = False
    print('---- Modificar Personaje ----')
    print('Lista de personajes')
    verRegistrosDelaTabla('vwPersonaje')
    idPersonaje = int(input('Introduce el ID del personaje que quiere modificar, o presione ENTER para cancelar el proceso\n>'))
    if idPersonaje == '':
        print('PROCESO CANCELADO')
        sleep(2)
    else:
        cur.execute("SELECT * FROM PERSONAJES WHERE ID = {}".format(idPersonaje))
        registro = cur.fetchone()

        if registro:
            registroExiste = True

        if registroExiste:
            nombre = confirmarModificacion('Nombre', registro[1])
            apellido = confirmarModificacion('Apellido', registro[2])
            pronunciacion = confirmarModificacion('pronunciacion', registro[3])

            verRegistrosDelaTabla('SERIES')
            serie = int(confirmarModificacion('serie', registro[4]))

            fecNaci = confirmarModificacion('fecha nacimiento', registro[5])
            poder = confirmarModificacion('poder', registro[6])
            desVest = confirmarModificacion('vestimenta', registro[7])
            edad = int(confirmarModificacion('edad', registro[8]))
            altura = float(confirmarModificacion('altura', registro[9]))

            verRegistrosDelaTabla('SEXOS')
            sexo = int(confirmarModificacion('sexo', registro[10]))

            verRegistrosDelaTabla('ESTADOS')
            estado = int(confirmarModificacion('estado', registro[11]))

            direccion = confirmarModificacion('direccion', registro[12])
            latitud = confirmarModificacion('latitud', registro[13])
            longitud = confirmarModificacion('longitud', registro[14])
            foto = confirmarModificacion('foto', registro[15])
            frase = confirmarModificacion('frase', registro[16])

            cur.execute(f"""
            UPDATE PERSONAJES
            SET
            Nombre = '{nombre}',
            Apellido = '{apellido}',
            Pronunciacion = '{pronunciacion}',
            Serie = {serie},
            Fecha_Nacimiento = '{fecNaci}',
            Poder = '{poder}',
            Descrip_Vestimenta = '{desVest}',
            Edad = {edad},
            Altura = {altura},
            Sexo = {sexo},
            Estado = {estado},
            Direccion = '{direccion}',
            Latitud = '{latitud}',
            Longitud = '{longitud}',
            Foto = '{foto}',
            Frase = '{frase}'
            WHERE ID = {idPersonaje}
            """)
            con.commit()
            print('PROCESO COMPLETADO')
            sleep(2)
        else:
            print('EL PERSONAJE NO EXISTE')
            sleep(2)


def eliminar():
    registroExiste = False
    print('---- Eliminar Personaje ----')
    print('Lista de personajes')
    verRegistrosDelaTabla('vwPersonaje')
    idPersonaje = int(input('Introduce el ID del personaje que quiere eliminar, o presione ENTER para cancelar el proceso\n>'))
    if idPersonaje == '':
        print('PROCESO CANCELADO')
        sleep(2)
    else:
        cur.execute("SELECT * FROM PERSONAJES WHERE ID = {}".format(idPersonaje))
        registro = cur.fetchone()

        if registro:
            registroExiste = True

        if registroExiste:
            op = input('¿Esta seguro de quere eliminar el personaje? (s/n)')
            if op == 's' or op == 'S':
                cur.execute(f"DELETE FROM PERSONAJES WHERE ID = {idPersonaje}")
                con.commit()
                print('PROCESO COMPLETADO')
                sleep(2)
            else:
                print('PROCESO CANCELADO')
                sleep(2)
        else:
            print('EL PERSONAJE NO EXISTE')
            sleep(2)

# --------------------------------------- REPORTES ------------------------------
def listaDePersonajes():
    limpiar()
    print('Lista de personajes')
    verRegistrosDelaTabla('vwPersonaje')
    print('REPORTE COMPLETADO')
    input('Precione ENTER para terminar')


def signoZodiacal():
    limpiar()
    print('---- Signo Zodical ----')
    cur.execute("""
    SELECT SIGNO, count(ID) as Personajes
    FROM vwSINGOS 
    GROUP BY SIGNO
    """)
    mytable = from_db_cursor(cur)
    print(mytable)
    print('REPORTE COMPLETADO')
    input('Precione ENTER para terminar')



def mapaPersonajes():
    print('IMPORTANDO MAPA')
    cur.execute('SELECT Nombre, Latitud, Longitud FROM PERSONAJES')
    registros = cur.fetchall()
    for r in registros:
        folium.Marker(
            location=[float(r[1]), float(r[2])],
            popup=f"{r[0]}",
            icon=folium.Icon(icon="user", prifix='fas'),
        ).add_to(m)
    m.save('mapa.html')
    webbrowser.open('mapa.html')
    print('IMPORTACION COMPLETA')
    sleep(2)

def htmlPersonaje():
    print('---- Exportar personaje HTML')
    print('Lista de personajes')
    verRegistrosDelaTabla('vwPersonaje')
    idPersonaje = int(input('Introduce en ID del personaje que quiere exportar, o presione ENTER para cancelar\n> '))
    if idPersonaje == '':
        print('EXPORTACION CANCELADA')
        sleep(2)
    else:
        cur.execute(f"""
        SELECT p.ID, p.Nombre, p.Apellido, p.Pronunciacion, p.Frase, v.Serie, p.Fecha_Nacimiento, p.Descrip_Vestimenta, p.Edad, p.Altura, v.Sexo, v.Estado, p.Direccion, p.Latitud, p.Longitud, p.Foto
        FROM PERSONAJES p, vwPersonaje v
        WHERE p.ID = v.ID AND p.ID = {idPersonaje}
        """)
        registro = cur.fetchone()
        html = f"""
        <!DOCTYPE html>
        <html lang="es">

        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Personaje</title>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/css/bootstrap.min.css" rel="stylesheet"
                integrity="sha384-KyZXEAg3QhqLMpG8r+8fhAXLRk2vvoC2f3B09zVXn8CA5QIVfZOJ3BCsw2P0p/We" crossorigin="anonymous">
        </head>

        <body>
            <div class="container" style="display: flex; justify-content: center; align-items: center;">
                <div class="card my-5" style="width: 18rem;">
                    <img src="{registro[15]}" class="" alt="">
                    <div class="card-body">
                        <h4 class="card-title">{registro[1]} {registro[2]}</h4>

                        <h5 class="card-title">Pronunciacion</h5>
                        <p class="card-text">{registro[3]}</p>

                        <h5 class="card-title">Frase</h5>
                        <p class="card-text">{registro[4]}</p>

                        <h5 class="card-title">Serie</h5>
                        <p class="card-text">{registro[5]}</p>

                        <h5 class="card-title">Fecha Nacimiento</h5>
                        <p class="card-text">{registro[6]}</p>

                        <h5 class="card-title">Descripcion Vestimenta</h5>
                        <p class="card-text">{registro[7]}</p>

                        <h5 class="card-title">Edad</h5>
                        <p class="card-text">{registro[8]}</p>

                        <h5 class="card-title">Altura</h5>
                        <p class="card-text">{registro[9]}</p>

                        <h5 class="card-title">Sexo</h5>
                        <p class="card-text">{registro[10]}</p>

                        <h5 class="card-title">Estado</h5>
                        <p class="card-text">{registro[11]}</p>

                        <h5 class="card-title">Direccion</h5>
                        <p class="card-text">{registro[12]}</p>

                        <h5 class="card-title">Latitud</h5>
                        <p class="card-text">{registro[13]}</p>

                        <h5 class="card-title">Longitud</h5>
                        <p class="card-text">{registro[14]}</p>

                    </div>
                </div>
            </div>
        </body>

        </html>
        """
        f = open('index.html', 'w')
        f.write(html)
        f.close()
        webbrowser.open('index.html')
        print('EXPORTACION COMPLETA')
        sleep(2)


def reportePorSerie():
    limpiar()
    cur.execute(f"""
    SELECT Serie, COUNT(ID) as Personajes
    FROM vwPersonaje
	GROUP BY Serie
    ORDER BY Serie
    """)
    mytable = from_db_cursor(cur)
    print(mytable)
    print('REPORTE COMPLETADO')
    input('Precione ENTER para terminar')


def reportePorEstado():
    limpiar()
    cur.execute(f"""
    SELECT Estado, Nombre, Apellido, Edad, Sexo, Serie, Poder, Descrip_Vestimenta, Altura
    FROM vwPersonaje
    ORDER BY Estado
    """)
    mytable = from_db_cursor(cur)
    print(mytable)

    cur.execute(f"""
    SELECT Estado, COUNT(ID) Personajes
    FROM vwPersonaje
    GROUP BY Estado
    """)
    mytable = from_db_cursor(cur)
    print(mytable)
    print('REPORTE COMPLETADO')
    input('Precione ENTER para terminar')




# --------------------------------------- CONFIGURACIONES ------------------------------
def agregarRegistro(ntabla):
    limpiar()
    print(f'---- Agregar {ntabla}----')
    print(f'Lista de {ntabla}')
    verRegistrosDelaTabla(f'{ntabla.upper()}')
    identificador = int(input(f'Introduce el ID de nueva/o {ntabla}, o presione ENTER para cancelar\n> '))
    if identificador == '':
        print('PROCESO CANCELADO')
        sleep(2)
    else:
        nombre = input(f'Introduce el nombre de {ntabla}\n> ')
        registro = (identificador, nombre)
        cur.execute(f"INSERT INTO {ntabla.upper()} VALUES (?,?)",registro)
        con.commit()
        print('PROCESO COMPLETADO')
        sleep(2)

def modificarRegistro(ntabla,nllave):
    registroExiste = False
    print(f'---- Modificar {ntabla}----')
    print(f'Lista de {ntabla}')
    verRegistrosDelaTabla(f'{ntabla.upper()}')
    identificador = int(input(f'Introduce el ID de nueva/o {ntabla}, o presione ENTER para cancelar\n> '))
    if identificador == '':
        print('PROCESO CANCELADO')
        sleep(2)
    else:
        cur.execute(f"SELECT * FROM {ntabla.upper()} WHERE {nllave} = {identificador}")
        registro = cur.fetchone()

        if registro:
            registroExiste = True

        if registroExiste:
            nombre = confirmarModificacion('Nombre', registro[1])

            cur.execute(f"""
            UPDATE {ntabla.upper()}
            SET
            Nombre = '{nombre}'
            WHERE {nllave} = {identificador}
            """)
            con.commit()
            print('PROCESO COMPLETADO')
            sleep(2)
        else:
            print(f'{ntabla} NO EXISTE')
            sleep(2)

def eliminarRegistro(ntabla,nllave):
    registroExiste = False
    print(f'---- Eliminar {ntabla.upper()} ----')
    print(f'Lista de {ntabla}')
    verRegistrosDelaTabla(f'{ntabla.upper()}')
    identificador = int(input(f'Introduce el ID de {ntabla} que quiere eliminar, o presione ENTER para cancelar el proceso\n>'))
    if identificador == '':
        print('PROCESO CANCELADO')
        sleep(2)
    else:
        cur.execute(f"SELECT * FROM {ntabla.upper()} WHERE {nllave} = {identificador}")
        registro = cur.fetchone()

        if registro:
            registroExiste = True

        if registroExiste:
            op = input('¿Esta seguro de quere eliminar el personaje? (s/n)')
            if op == 's' or op == 'S':
                cur.execute(f"DELETE FROM {ntabla.upper()} WHERE {nllave} = {identificador}")
                con.commit()
                print('PROCESO COMPLETADO')
                sleep(2)
            else:
                print('PROCESO CANCELADO')
                sleep(2)
        else:
            print(f'EL {ntabla} NO EXISTE')
            sleep(2)


def acercaDe():
    limpiar()
    webbrowser.open('https://www.youtube.com/watch?v=qK-N9Yqj1Ds')