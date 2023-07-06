from funciones import *

while True:
    ver_menu()
    opcion = validar_opcion()
    if opcion == 1:
        comprar_entradas()
    elif opcion == 2:
        ver_escenario_sleep()
    elif opcion == 3:
        ver_listado()
    elif opcion == 4:
        mostrar_ganancias()
    else: 
        salir()
        break