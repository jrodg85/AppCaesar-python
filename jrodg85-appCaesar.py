# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 09:11:32 2023

@author: usriaml
"""

fraseEstudio=""
opcionMenu=""

print("Bienvenido a AppCaesar:")

def introduzcaUnaFrase():
    global fraseEstudio
    #print("pasa por funcion introduzca una frase")
    fraseEstudio=input("Introduzca Frase de estudio: ")
    seleccionMenu()

def contarConsonantesDeLaFrase():
    print("pasa por funcion Contar cuantas consonantes hay en el texto")
    seleccionMenu()

def contarVocalesDeLaFrase():
    print("pasa por funcion Contar cuantas vocales hay en el texto")
    seleccionMenu()

def mostrarParaCadaLetraCuantasVecesSeRepite(): 
    print("pasa por la funcion Mostrar para cada letra cuantas veces se repite (diccionario) ")
    seleccionMenu()

def mostrarLaFraseCodificadaConClaveCaesar():
    print("pasa por la funcion Mostrar la frase codificada con clave Caesar")
    seleccionMenu()
    
def salirDeAppCaesar():
    print("pasa por la funcion Salir del programa")
    print("borrando datos almacenados")
    global opcionMenu
    del (opcionMenu)
    global fraseEstudio
    del(fraseEstudio) 
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
        print("Ha seleccionado opcion 1")
        introduzcaUnaFrase()
    elif opcionMenu=="2":
        print("Ha seleccionado opcion 2")
        contarConsonantesDeLaFrase()
    elif opcionMenu=="3":
        print("Ha seleccionado opcion 3")
        contarVocalesDeLaFrase()
    elif opcionMenu=="4":
        print("Ha seleccionado opcion 4")
        mostrarParaCadaLetraCuantasVecesSeRepite()
    elif opcionMenu=="5":
        print("Ha seleccionado opcion 5")
        mostrarLaFraseCodificadaConClaveCaesar()
    elif opcionMenu=="6":
        print("Ha seleccionado opcion 6")
        verFraseEstudio()
    elif opcionMenu=="7":
        print("Ha seleccionado opcion 7")
        salirDeAppCaesar()
    else:
        print("Seleccion incorrecta, ha seleccionado ", opcionMenu)
        seleccionMenu()

seleccionMenu()
