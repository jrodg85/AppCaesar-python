# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 09:11:32 2023

@author: usriaml
"""
opcionMenu=""
fraseEstudio=""

print("Bienvenido a AppCaesar:")

def introduzcaUnaFrase():
    print("pasa por funcion introduzca una frase")
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
    print("Adios")

def seleccionMenu():
    print("Seleccione una opción: \n1 ==> Introduzca una frase. \n2 ==> Contar cuantas consonantes hay en el texto. \n3 ==> Contar cuantas vocales hay en el texto. \n4 ==> Mostrar para cada letra cuantas veces se repite (diccionario). \n5 ==> Mostrar la frase codificada con la clave 2. \n6 ==> Salir del programa.")
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
        salirDeAppCaesar()
    else:
        print("Seleccion incorrecta, ha seleccionado ", opcionMenu)
        seleccionMenu()
seleccionMenu()
