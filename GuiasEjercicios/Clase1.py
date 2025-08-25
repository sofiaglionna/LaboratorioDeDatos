import csv


def leer_parque(nombre_archivo,parque) -> list[dict]:
    with open(nombre_archivo) as f:
        filas = csv.reader(f)

        encabezado = next(filas)

        indice_parques = encabezado.index("espacio_ve") #Deberia devolver "k" que es donde estan los parqies
        
        parqueData = []  

        for fila in filas:
            if fila[indice_parques] == parque:
                arbolData = dict(zip(encabezado,fila)) #armo el diccionario de cada fila
                parqueData.append(arbolData)

    #creo un diccionario con tantas claves como columas. Los valores son los datos de esas columnas

    return parqueData

arboles = leer_parque("arbolado-en-espacios-verdes.csv", "CENTENARIO")
#print(len(arboles))

def especies(lista_arboles: list[dict]):
    listaEspecies = []

    for arbol in lista_arboles:
        listaEspecies.append(arbol['nombre_com'])

    return listaEspecies

#lista = leer_parque("arbolado-en-espacios-verdes.csv", "CENTENARIO")
#print(especies(lista))

def contar_ejemplares(lista_arboles):
    dictEspecies = {}
    listaDeEspecies = especies(lista_arboles)

    for especie in listaDeEspecies:
        if especie in dictEspecies:
            dictEspecies[especie] = dictEspecies[especie] + 1
        else:
            dictEspecies[especie] = 1

    return dictEspecies


#print(contar_ejemplares(lista))

def obtener_alturas(lista_arboles, especie):
    listaAlturas = []

    for arbol in lista_arboles:
        if arbol['nombre_com'] == especie:
            listaAlturas.append(arbol['altura_tot'])

    return listaAlturas

lista = leer_parque("arbolado-en-espacios-verdes.csv", "CENTENARIO")
alturas = obtener_alturas(lista, 'Jacarandá')

def promedio(alturas):
    total = 0
    cant = 0
    for altura in alturas:
        total = total + altura
        cant = cant + 1
    return (total/cant)

print(promedio(alturas))

#DEBO PASARLO A INT PQ ESTAN EN INT!!








    