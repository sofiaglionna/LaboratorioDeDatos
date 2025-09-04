import csv
import pandas as pd
import numpy as np


def leer_parque(nombre_archivo,parque) -> list[dict]:
    with open(nombre_archivo) as f:
        filas = csv.reader(f)

        encabezado = next(filas)

        indice_parques = encabezado.index("espacio_ve") # Debería devolver "k" que es donde estan los parqies.
        
        parqueData = []  

        for fila in filas:
            if fila[indice_parques] == parque:
                arbolData = dict(zip(encabezado,fila)) # Armo el diccionario de cada fila.
                parqueData.append(arbolData)

    # Creo un diccionario con tantas claves como columas. Cada diccionario contiene la información de 1 árbol.

    return parqueData

arboles = leer_parque("arbolado-en-espacios-verdes.csv", "REPÚBLICA SOCIALISTA DE VIETNAM")
#print(arboles)

def especies(lista_arboles: list[dict]):
    listaEspecies = []

    for arbol in lista_arboles:
        listaEspecies.append(arbol['nombre_com'])

    return listaEspecies

def especiesSinRepetidos(lista_arboles):
    listaEspeciesSinRepetidos = []

    for arbol in lista_arboles:
        especie = arbol['nombre_com']
        if especie not in listaEspeciesSinRepetidos:
            listaEspeciesSinRepetidos.append(especie)

    return listaEspeciesSinRepetidos

#lista = leer_parque("arbolado-en-espacios-verdes.csv", "CENTENARIO")
#print(especies(arboles))

def contar_ejemplares(lista_arboles):
    dictEspecies = {}
    listaDeEspecies = especies(lista_arboles)

    for especie in listaDeEspecies:
        if especie in dictEspecies:
            dictEspecies[especie] = dictEspecies[especie] + 1
        else:
            dictEspecies[especie] = 1

    return dictEspecies

#print(contar_ejemplares(arboles))

def obtener_alturas(lista_arboles, especie):
    listaAlturas = []

    for arbol in lista_arboles:
        if arbol['nombre_com'] == especie:
            listaAlturas.append(int(arbol['altura_tot'])) # Paso la altura (str) a un int, ya que luego lo voy a usar para calcular el promedio.

    return listaAlturas

def promedio(alturas):
    total = 0
    cant = 0
    for altura in alturas:
        total = total + altura
        cant = cant + 1
    return (total/cant)

def masAlto(alturas):
    max = 0
    for altura in alturas:
        if altura > max:
            max = altura
    return max

lista = leer_parque("arbolado-en-espacios-verdes.csv", "GENERAL PAZ")
alturas = obtener_alturas(lista, 'Jacarandá')
#print(masAlto(alturas))
#print(promedio(alturas))
#CENTENARIO -> Más Alto: 18 mts || Promedio = 8.96 mts
#GENERAL PAZ -> Más Alto: 16 mts || Promedio = 10.2 mts

def obtener_inclinaciones(lista_arboles, especie):
    listaInclinaciones = []
    for arbol in lista_arboles:
        if arbol['nombre_com'] == especie:
            inclinacion = arbol['inclinacio']
            listaInclinaciones.append(int(inclinacion))

    return listaInclinaciones

#print(obtener_inclinaciones(lista, 'Jacarandá'))

def especimen_mas_inclinado(lista_arboles):
    inclinacionMax = 0
    especimen_mas_inclinado = 'Ninguno'

    for arbol in lista_arboles:
        inclinacion = int(arbol['inclinacio'])
        if inclinacion > inclinacionMax:
            inclinacionMax = inclinacion
            especimen_mas_inclinado = arbol['nombre_com']


    return especimen_mas_inclinado, inclinacionMax

lista1 = leer_parque("arbolado-en-espacios-verdes.csv", "EJERCITO DE LOS ANDES")
especimen, inclinacion = especimen_mas_inclinado(lista1)
#print(f"El árbol más inclinado es {especimen}, con una inclinación de {inclinacion}°") # Sin la 'f' al principio, no lee los valores 'especimen' e 'inclinacion'

def especie_promedio_mas_inclinada(lista_arboles):

    especiesEnLista = especiesSinRepetidos(lista_arboles)
    promedioMasInclinado = 0
    especieMasInclinada = ''

    for especie in especiesEnLista:
        promedioEspecie = promedio(obtener_inclinaciones(lista_arboles,especie))
        if promedioEspecie > promedioMasInclinado:
            promedioMasInclinado = promedioEspecie
            especieMasInclinada = especie

    return especieMasInclinada, promedioMasInclinado
        
especimen, promedioInclinacion = especie_promedio_mas_inclinada(lista1)
#print(f'La especie mas inclinada es {especimen}, con una inclinacion promedio de {inclinacion}°')


# Cambiamos de archivo: "arbolado-publico-lineal-2017-2018.csv"

########################### Armo DataFrames permanentes ############################################

df_vereda = pd.read_csv("arbolado-publico-lineal-2017-2018.csv")
df_parque = pd.read_csv("arbolado-en-espacios-verdes.csv")

#Armar un DataFrame data_arboles_veredas que tenga solamente las siguiente
#columnas: 'nombre_cientifico', 'ancho_acera', 'diametro_altura_pecho', 'altura_arbol'

data_arboles_veredas = df_vereda[["nombre_cientifico", "ancho_acera", "diametro_altura_pecho", "altura_arbol"]]

#Para cada dataset, armar otro seleccionando solamente las filas correspondientes
#a las tipas (llamalos df_tipas_parques y df_tipas_veredas, respectivamente) y las
#columnas correspondientes al diámetro a la altura del pecho y alturas.

df_tipas_parques = df_parque[df_parque['nombre_com'] == 'Tipuana Tipu'].copy()
df_tipas_veredas = df_vereda[df_vereda['nombre_cientifico'] == 'Tipuana tipu'].copy()

parques = df_tipas_parques[["diametro", "altura_tot"]].copy()
veredas = df_tipas_veredas[["diametro_altura_pecho", "altura_arbol"]].copy()

# El .copy() crea una copia independiente. Si no lo pusiera, seria solo una vista del df original.
# --> df_tipas_veredas tiene (9330 rows x 4 columns) Aparece "Tipuana tipu" 9330 veces

print(df_tipas_parques)

#Usar como
#copias (usando .copy()) para poder trabajar en estos nuevos dataframes sin
#modificar los dataframes grandes originales. Renombrar las columnas necesarias
#para que se llamen igual en ambos dataframes.




















    