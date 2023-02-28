# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 09:11:32 2023

@author: jrodg85
"""
import sys
import termios
import os

fraseEstudio=""
opcionMenu=""

def noHayFraseEstudio():
        print("""No hay frase de estudio.
Procediendo a introducir frase de estudio
Una vez introducida la frase volvera al menu principal.""")
        introduzcaUnaFrase()
        
def volverAMenuPrincipal():
    wait_for("")
    borrarPantalla()
    seleccionMenu()

## Metodo de borrar pantalla encontrado en https://unipython.com/como-borrar-pantalla-en-python/
def borrarPantalla(): #Definimos la función estableciendo el nombre que queramos
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")

## wait for importado de la siguiente url https://es.stackoverflow.com/questions/277815/como-hago-un-presione-enter-para-continuar-en-python-3-linux
## De momento se queda comentado ya que en spider no funciona correctamente pero en la terminal funciona
def wait_for(mess, *keys):
    file_descriptor = sys.stdin.fileno()
    old = termios.tcgetattr(file_descriptor)
    new = old[:]
    try:
        new[3] &= ~(termios.ICANON | termios.ECHO)
        termios.tcsetattr(file_descriptor, termios.TCSADRAIN, new)
        print(mess, end="")
        while True:
            letra = sys.stdin.read(1)
            if not keys or letra in keys:
                print()
                break
    finally:
        termios.tcsetattr(file_descriptor, termios.TCSADRAIN, old)

def introduzcaUnaFrase():
    global fraseEstudio
    fraseEstudio=input("Introduzca clave: ")
    borrarPantalla()
    verFraseEstudio()
    print("Presione una tecla para continuar...")
    volverAMenuPrincipal()

def contarConsonantesDeLaFrase():
    if fraseEstudio == "":
        noHayFraseEstudio()
    else:
        ## metodo para contar consonantes en la URL https://parzibyte.me/blog/2020/10/18/python-contar-consonantes-cadena/
        def es_vocal(letra):
            return letra in "aeiou"
        cadena = fraseEstudio
        # Comenzamos convirtiendo a minúsculas, así nos ahorramos comparaciones
        cadena_minuscula = cadena.lower()
        cantidad_consonantes = 0
        for letra in cadena_minuscula:
            if letra.isalpha() and not es_vocal(letra):
                cantidad_consonantes += 1
        print(f""""En la frase '{cadena}' hay {cantidad_consonantes} consonantes
Presione una tecla para continuar...""")
        volverAMenuPrincipal()

def contarVocalesDeLaFrase():
    if fraseEstudio == "":
        noHayFraseEstudio()
    else:
        ## método para contar consonantes de la URL https://parzibyte.me/blog/2020/10/12/contar-vocales-python/
        contador = 0
        for letra in fraseEstudio:
            if letra.lower() in "aeiou":
                contador += 1
        print("En la frase '", fraseEstudio, "' hay ", contador, """ vocales"
Presione una tecla para continuar...""")
        volverAMenuPrincipal()

def mostrarParaCadaLetraCuantasVecesSeRepite():
    if fraseEstudio == "":
        noHayFraseEstudio()
    else:
    # fuente para la realizacion del metodo tomada de la URL https://es.stackoverflow.com/questions/444688/contar-caracteres-repetidos-en-una-cadena
        letras_dic = dict()  #Guarda repetición de letras
        for letra in fraseEstudio.lower(): #Por cada letra
            if letra in letras_dic: #Si ya estaba en el dic() significa que se repite
                if letras_dic[letra] >= 1: #He tenido que cambiar de la fuente original, no es == sino >=
                    letras_dic[letra] += 1 #Continua el conteo
            else:
                letras_dic[letra] = 1 #Si la letra no esta en el diccionario, la agrega
        print("""
El conjunto de letras es el siguiente.
""",letras_dic, """)
Presione una tecla para continuar...""")
        volverAMenuPrincipal()

def codificadcionClaveCaesarRotacion2():
    global opcionMenu
    if fraseEstudio == "":
        print("""No hay frase de estudio.
Procediendo a introducir frase de estudio
Una vez introducida la frase volvera al menu principal.""")
        introduzcaUnaFrase()
    else:
        # Fuente utilizada para este apartado, es la siguiente URL https://parzibyte.me/blog/2018/12/10/cifrado-cesar-python/
        mensaje=fraseEstudio
        rotaciones=2
        alfabeto = "abcdefghijklmnopqrstuvwxyz"
        alfabeto_mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        longitud_alfabeto = len(alfabeto)
        codificado = ""
        if opcionMenu=="5":
            for letra in mensaje:
                if not letra.isalpha() or letra.lower() == 'ñ':
                    codificado += letra
                    continue
                valor_letra = ord(letra)
                # Suponemos que es minúscula, así que esto comienza en 97(a) y se usará el alfabeto en minúsculas
                alfabeto_a_usar = alfabeto
                limite = 97  # Pero si es mayúscula, comienza en 65(A) y se usa en mayúsculas
                if letra.isupper():
                    limite = 65
                    alfabeto_a_usar = alfabeto_mayusculas
    
                # Rotamos la letra
                posicion = (valor_letra - limite + rotaciones) % longitud_alfabeto
    
                # Convertimos el entero resultante a letra y lo concatenamos
                codificado += alfabeto_a_usar[posicion]
            print("La frase '", fraseEstudio, "' tiene como codigo la siguiente frase: \n", codificado,"""
    Presione una tecla para continuar...""")
            volverAMenuPrincipal()
        elif opcionMenu=="6":
            for letra in mensaje:
                if not letra.isalpha() or letra.lower() == 'ñ':
                    codificado += letra
                    continue
                valor_letra = ord(letra)
                # Suponemos que es minúscula, así que esto comienza en 97(a) y se usará el alfabeto en minúsculas
                alfabeto_a_usar = alfabeto
                limite = 97  # Pero si es mayúscula, comienza en 65(A) y se usa en mayúsculas
                if letra.isupper():
                    limite = 65
                    alfabeto_a_usar = alfabeto_mayusculas
    
                # Rotamos la letra
                posicion = (valor_letra - limite - rotaciones) % longitud_alfabeto
    
                # Convertimos el entero resultante a letra y lo concatenamos
                codificado += alfabeto_a_usar[posicion]
            print("La frase '", fraseEstudio, "' tiene decodificado la siguiente frase: \n", codificado,"""
    Presione una tecla para continuar...""")
            volverAMenuPrincipal()
    
def salirDeAppCaesar():
    print("borrando datos almacenados")
    global opcionMenu
    del (opcionMenu)
    global fraseEstudio
    del (fraseEstudio)
    print("Adios")
    exit()

def verFraseEstudio():
    print ("La frase de estudio es: '", fraseEstudio,"""'
Presione una tecla para continuar...""")
    volverAMenuPrincipal()

def seleccionMenu():
    global opcionMenu
    print("""
Seleccione una opción:
    1 ==> Introduzca una frase.
    2 ==> Contar cuantas consonantes hay en el texto.
    3 ==> Contar cuantas vocales hay en el texto.
    4 ==> Mostrar para cada letra cuantas veces se repite (diccionario).
    5 ==> Mostrar la frase codificada con la clave 2.
    6 ==> Al insertar una frase codificada, esta la decodificará con clave 2.
    7 ==> Ver la frase de estudio.
    8 ==> Salir del programa.
    """)
    opcionMenu=input("Selecione Opcion: ")
    if opcionMenu=="1":
        introduzcaUnaFrase()
    elif opcionMenu=="2":
        contarConsonantesDeLaFrase()
    elif opcionMenu=="3":
        contarVocalesDeLaFrase()
    elif opcionMenu=="4":
        mostrarParaCadaLetraCuantasVecesSeRepite()
    elif ((opcionMenu=="5")or(opcionMenu=="6")):
        codificadcionClaveCaesarRotacion2()
    elif opcionMenu=="7":
        verFraseEstudio()
    elif opcionMenu=="8":
        salirDeAppCaesar()
    else:
        print("Seleccion incorrecta, ha seleccionado ", opcionMenu)
        seleccionMenu()

borrarPantalla()
print("Bienvenido a AppCaesar:")
seleccionMenu()
