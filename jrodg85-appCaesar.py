# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 09:11:32 2023

@author: jrodg85
"""

fraseEstudio=""
opcionMenu=""

print("Bienvenido a AppCaesar:")

import os

## Metodo de borrar pantalla encontrado en https://unipython.com/como-borrar-pantalla-en-python/
def borrarPantalla(): #Definimos la función estableciendo el nombre que queramos
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")
## wait for importado de la siguiente url https://es.stackoverflow.com/questions/277815/como-hago-un-presione-enter-para-continuar-en-python-3-linux
## De momento se queda comentado ya que en spider no funciona correctamente pero en la terminal funciona
import sys
import termios

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
    #print("pasa por funcion introduzca una frase")
    fraseEstudio=input("Introduzca Frase de estudio: ")
    seleccionMenu()

def contarConsonantesDeLaFrase():
    #print("pasa por funcion Contar cuantas consonantes hay en el texto")
    if fraseEstudio == "":
        print("""No hay frase de estudio.
Procediendo a introducir frase de estudio
Una vez introducida la frase volvera al menu principal.""")
        introduzcaUnaFrase()
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
        print(f"En la frase '{cadena}' hay {cantidad_consonantes} consonantes")
        print("Presione una tecla para continuar...")
# wait for comprobado que funciona en la terminal. dejamos esto de momento a 
# modo de pruebas con un input normal             
    wait_for("")
    borrarPantalla()
       # input ("pulsa enter para continuar // Modo pruebas ")
    seleccionMenu()

def contarVocalesDeLaFrase():
    print("pasa por funcion Contar cuantas vocales hay en el texto")
    if fraseEstudio == "":
        print("""No hay frase de estudio.
Procediendo a introducir frase de estudio
Una vez introducida la frase volvera al menu principal.""")
        introduzcaUnaFrase()
    else:
        contador = 0
        for letra in fraseEstudio:
            if letra.lower() in "aeiou":
                contador += 1
        print("En la frase '", fraseEstudio, "' hay ", contador, " vocales")
        print("Presione una tecla para continuar...")
    wait_for("")
    borrarPantalla()
    seleccionMenu()

def mostrarParaCadaLetraCuantasVecesSeRepite(): 
    print("pasa por la funcion Mostrar para cada letra cuantas veces se repite (diccionario) ")
    if fraseEstudio == "":
        print("""No hay frase de estudio.
Procediendo a introducir frase de estudio
Una vez introducida la frase volvera al menu principal.""")
        introduzcaUnaFrase()
    else:
    
        letras_dic = dict()  #Guarda repetición de letras
        for letra in fraseEstudio: #Por cada letra
            if letra in letras_dic: #Si ya estaba en el dic() significa que se repite
                if letras_dic[letra] == 1: 
                    letras_dic[letra] += 1 #Continua el conteo
            else:
                letras_dic[letra] = 1 #Si la letra no esta en el diccionario, la agrega
    

        print("""
El conjunto de letras es el siguiente.
""",letras_dic)
    
    
    
    
    
    
        
        
    seleccionMenu()

def mostrarLaFraseCodificadaConClaveCaesar():
    print("pasa por la funcion Mostrar la frase codificada con clave Caesar")
    seleccionMenu()
    
def salirDeAppCaesar():
    print("Pasa por la funcion Salir del programa.")
    print("Borrando datos almacenados.")
    global opcionMenu
    del (opcionMenu)
    global fraseEstudio
    del (fraseEstudio)
    print("Adios")

def verFraseEstudio():
    print ("La frase de estudio es: ", fraseEstudio)
    seleccionMenu()




def seleccionMenu():
    print("""
Seleccione una opción: 
    1 ==> Introduzca una frase. 
    2 ==> Contar cuantas consonantes hay en el texto. 
    3 ==> Contar cuantas vocales hay en el texto. 
    4 ==> Mostrar para cada letra cuantas veces se repite (diccionario). 
    5 ==> Mostrar la frase codificada con la clave 2. 
    6 ==> Ver la frase de estudio.
    7 ==> Salir del programa.
    """)
    opcionMenu=input("Selecione Opcion: ")
    if opcionMenu=="1":
        borrarPantalla()
        # print("Ha seleccionado opcion 1")
        introduzcaUnaFrase()
    elif opcionMenu=="2":
        borrarPantalla()
        # print("Ha seleccionado opcion 2")
        contarConsonantesDeLaFrase()
    elif opcionMenu=="3":
        borrarPantalla()
        print("Ha seleccionado opcion 3")
        contarVocalesDeLaFrase()
    elif opcionMenu=="4":
        borrarPantalla()
        print("Ha seleccionado opcion 4")
        mostrarParaCadaLetraCuantasVecesSeRepite()
    elif opcionMenu=="5":
        borrarPantalla()
        print("Ha seleccionado opcion 5")
        mostrarLaFraseCodificadaConClaveCaesar()
    elif opcionMenu=="6":
        borrarPantalla()
        print("Ha seleccionado opcion 6")
        verFraseEstudio()
    elif opcionMenu=="7":
        borrarPantalla()
        print("Ha seleccionado opcion 7")
        salirDeAppCaesar()
    else:
        borrarPantalla()
        print("Seleccion incorrecta, ha seleccionado ", opcionMenu)
        seleccionMenu()

borrarPantalla()
seleccionMenu()
