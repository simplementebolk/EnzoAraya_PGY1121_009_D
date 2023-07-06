import os
import msvcrt
import numpy
import time
#Listas

lista_ruts = []
lista_nombres = []
lista_apellidos = []
lista_filas = []
lista_columnas = []
lista_entradas_c = []
lista_tipo_entrada = []
lista_dinero_recaudado = []
total = 0
dinero_recaudado = 0

cantidad_platinum = 0
cantidad_gold = 0
cantidad_silver = 0

#Funciones Ver
def ver_menu():
    os.system('cls')
    print(""" 
        Menú
    Concierto VIP de:
      "Michael Jam"        

1. Comprar Entradas    
2. Mostrar ubicaciones disponibles    
3. Ver listado de asistentes    
4. Mostrar ganancias totales
5. Salir""")

def ver_precios():
    print("""
    
    Precios
    
1. Platinum $120.000    
2. Gold $80.000
3. Silver $50.000""")

escenario = numpy.zeros((10,10), int)

def ver_escenario_sleep():
    print("Se Mostrará el escenario por 10 segundos")
    for x in range(10):
        print(f" fila: {x+1}", end=" ")
        for y in range(10):
            print(escenario[x][y], end=" ")
        print()
    print("  COLUMNA 1 2 3 4 5 6 7 8 9 10")

    
    time.sleep(10)
    os.system('cls')

def ver_escenario():
    for x in range(10):
        print(f" fila: {x+1}", end=" ")
        for y in range(10):
            print(escenario[x][y], end=" ")
        print()
    print("  COLUMNA 1 2 3 4 5 6 7 8 9 10")   

#Funciones Validaciones
def validar_opcion():
    while True:
        try:
            opcion = int(input("Ingrese una opción: "))
            if opcion in (1,2,3,4,5):
                return opcion
            else:
                print("ERROR!!! INGRESE UNA OPCIÓN CORRECTA!!!")
        except:
            print("ERROR!!! INGRESE UNA OPCIÓN CORRECTA!!!")    

def validar_fila():
    while True:
        try:
            fila = int(input("Ingrese la fila(1-10): "))
            if fila in (1,2,3,4,5,6,7,8,9,10):
                return fila
            else:
                print("ERROR!! INGRESE UNA FILA CORRECTA")    
        except:
            print("ERROR!! INGRESE UNA FILA CORRECTA")  

def validar_columna():
    while True:
        try:
            columna = int(input("Ingrese la columna(1-10): "))
            if columna in (1,2,3,4,5,6,7,8,9,10):
                return columna
            else:
                print("ERROR!! INGRESE UNA COLUMNA CORRECTA")    
        except:
            print("ERROR!! INGRESE UNA COLUMNA CORRECTA")    

def validar_rut():
    while True:
        try:
            rut = int(input("Ingrese su rut sin punto ni digito verificador: "))
            if len(str(rut)) >= 7 and len(str(rut)) <= 8:
                return rut
            else:
                print("ERROR!!! INGRESE UN RUT VALIDO!!!")
        except:
            print("ERROR!! INGRESE UN RUT VALIDO!!!")

def validar_entradas():
    while True:
        try:
            cantidad_entradas = int(input("Ingrese cuantas entradas desea: "))
            if cantidad_entradas >=1 and cantidad_entradas <= 3:
                return cantidad_entradas
            else:
                print("ERROR!! INGRESE UNA CANTIDAD ENTRE 1 Y 3")
        except:         
            print("ERROR!! INGRESE UNA CANTIDAD ENTRE 1 Y 3")     

def validar_tipo_entrada():
    while True:
        try:
            tipo_entrada = int(input("""
    Ingrese el tipo de entrada que desea: """))
            if tipo_entrada in (1,2,3):
                return tipo_entrada
            else:
                print("ERROR!! INGRESE UNA ENTRADA VALIDA!!!")
        except:
            print("ERROR!! INGRESE UNA OPCION VALIDA")         

def validar_nombre():
    while True:
        nombre = input("Ingrese su nombre: ")
        if len(nombre) >= 3 and nombre.isalpha:
            return nombre
        else:
            print("ERROR!!! INGRESE UN NOMBRE CON 3 LETRAS O MAS!!!")

def validar_apellido():
    while True:
        apellido = input("Ingrese su Apellido: ")
        if len(apellido) >= 3 and apellido.isalpha:
            return apellido
        else:
            print("ERROR!!! INGRESE UN NOMBRE CON 3 LETRAS O MAS!!!")

#Funciones Del Menú
def comprar_entradas():
    if 0 not in escenario:
        print("ERROR!! NO HAY ESPACIOS DISPONIBLES")
        return
    rut = validar_rut()
    nombre = validar_nombre()
    apellido = validar_apellido()
    while True:
        ver_precios()
        tipo_entrada = validar_tipo_entrada()
        cantidad_entradas = validar_entradas()
        if tipo_entrada == 1:
            total = cantidad_entradas*120000
        elif tipo_entrada == 2:
            total = cantidad_entradas*80000
        elif tipo_entrada == 3:
            total = cantidad_entradas*50000
        ver_escenario()
        fila = validar_fila()
        columna = validar_columna()
        if escenario[fila-1][columna-1] == 0:
            escenario[fila-1][columna-1] = 1
            lista_ruts.append(rut)
            lista_nombres.append(nombre)
            lista_apellidos.append(apellido)
            lista_filas.append(fila)
            lista_columnas.append(columna)
            lista_entradas_c.append(cantidad_entradas)
            lista_tipo_entrada.append(tipo_entrada)
            lista_dinero_recaudado.append(dinero_recaudado)
            print("Gracias por su compra ^_^")
            print("Total: $",total) 
            print(f"Se ha registrado su Fila: {fila}")
            print(f"Se ha registrado su Columna: {columna}")
            time.sleep(5)

            break
        else:
            print("ERROR!! ESPACIO NO DISPONIBLE!!")

def mostrar_ganancias():
    print(dinero_recaudado)

def ver_listado():
    print("Asistentes:")
    print(lista_nombres)
    time.sleep(10)

def salir():
   
    print("Gracias por preferirnos")
    print("Nombre:")
    print("Apellido:")
    print("Fecha: 06/07/2023")