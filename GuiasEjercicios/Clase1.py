import csv


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















    