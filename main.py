from createDB import *
from methods import *

createDataBase()

while True:
    limpiar()
    print('---- Menu ----')
    print('Bienvenido/a a WikiAnime')
    print('1. Gestionar Personajes')
    print('2. Reportes')
    print('3. Configuraciones')
    print('4. Acerca De')
    print('5. Salir del programa')

    op = int(input(' \nIntroduce en número de la opción que quiere realizar\n> '))

    if op == 1:
        while True:
            try:
                limpiar()
                print('---- Gestionar Personajes ----')
                print('1. Registrar Personaje')
                print('2. Modificar Personaje')
                print('3. Eliminar Personaje')
                print('4. Volver')
                op = int(input('Introduce en número de la opción que quiere realizar\n> '))

                if op == 1:
                    registrar()
                elif op == 2:
                    modificar()
                elif op == 3:
                    eliminar()
                elif op == 4:
                    break
                else:
                    print('Opcion no valida')
            except ValueError:
                print('Valor no valido')
                time.sleep(3)
    elif op == 2:
        while True:
            try:
                limpiar()
                print('---- Reportes ----')
                print('1. Lista de personajes')
                print('2. Lista de personajes por signo zodiacal')
                print('3. Ubicacion de personajes')
                print('4. Ver carta del personaje en HTML')
                print('5. Lista de personajes por serie')
                print('6. Lista de personajes por estado')
                print('7. Volver')
                op = int(input(' \nIntroduce en número de la opción que quiere realizar\n> '))

                if op == 1:
                    listaDePersonajes()
                elif op == 2:
                    signoZodiacal()
                elif op == 3:
                    mapaPersonajes()
                elif op == 4:
                    htmlPersonaje()
                elif op == 5:
                    reportePorSerie()
                elif op == 6:
                    reportePorEstado()
                elif op == 7:
                    break
                else:
                    print('Opcion no valida')
            except ValueError:
                print('Valor no valido')
                time.sleep(3)
    elif op == 3:
        while True:
            try:
                limpiar()
                print('---- Configuraciones ----')
                print('1. Registrar Serie')
                print('2. Modificar Serie')
                print('3. Eliminar Serie')
                print(' ')
                print('4. Registrar Sexo')
                print('5. Modificar Sexo')
                print('6. Eliminar Sexo')
                print(' ')
                print('7. Registrar Estado')
                print('8. Modificar Estado')
                print('9. Eliminar Estado')
                print('10. Volver')
                op = int(input('Introduce en número de la opción que quiere realizar\n> '))

                if op == 1:
                    agregarRegistro('SERIES')
                elif op == 2:
                    modificarRegistro('SERIES', 'ID_Serie')
                elif op == 3:
                    eliminarRegistro('SERIES', 'ID_Serie')
                elif op == 4:
                    agregarRegistro('SEXOS')
                elif op == 5:
                    modificarRegistro('SEXOS', 'ID_Sexo')
                elif op == 6:
                    eliminarRegistro('SEXOS', 'ID_Sexo')
                elif op == 7:
                    agregarRegistro('ESTADOS')
                elif op == 8:
                    modificarRegistro('ESTADOS', 'ID_Estado')
                elif op == 9:
                    eliminarRegistro('ESTADOS', 'ID_Estado')
                elif op == 10:
                    break
                else:
                    print('Opcion no valida')
            except ValueError:
                print('Valor no valido')
                time.sleep(3)
    elif op == 4:
        acercaDe()
    elif op == 5:
        print('SALIENDO DEL PROGRAMA...')
        sleep(2)
        break
    else:
        print('Opcion no valida')
        