import pandas as pd
import duckdb as dd

"""
Created on Wed Sep 24 09:12:46 2025

@author: Sofía
"""

#%%-----------
#Archivos .csv importados

departamento = pd.read_csv("departamento.csv")    
casos = pd.read_csv("casos.csv")  
grupoetario = pd.read_csv("grupoetario.csv")   
provincia = pd.read_csv("provincia.csv") 
tipoevento = pd.read_csv("tipoevento.csv") 

#%%-----------
#=============================================================================
# Ejercicios A - Consultas sobre una tabla
#=============================================================================
# Aa.- Listar sólo los nombres de todos los departamentos que hay en la tabla departamento (dejando los registros repetidos).

Aa = """
    SELECT descripcion
    FROM departamento
"""

dfAa = dd.sql(Aa).df()

# Ab.- Listar sólo los nombres de todos los departamentos que hay en la tabla departamento (eliminando los registros repetidos)

Ab = """
    SELECT DISTINCT descripcion
    FROM departamento
"""

dfAb = dd.sql(Ab).df()

# Ac.- Listar sólo los códigos de departamento y sus nombres, de todos los departamentos que hay en la tabla departamento

Ac = """
    SELECT DISTINCT id, descripcion
    FROM departamento
"""

dfAc = dd.sql(Ac).df()

# Ad.- Listar todas las columnas de la tabla departamento.

Ad = """
    SELECT DISTINCT *
    FROM departamento
"""

dfAd = dd.sql(Ad).df()

# Ae.- Listar los códigos de departamento y nombres de todos los departamentos que hay en la tabla departamento. 
# Utilizar los siguientes alias para las columnas: codigo_depto y nombre_depto, respectivamente.

Ae = """
    SELECT DISTINCT id as codigo_depto, descripcion as nombre_depto
    FROM departamento
"""

dfAe = dd.sql(Ae).df()

# Af.- Listar los registros de la tabla departamento cuyo código de provincia es igual a 54

Af = """
    SELECT DISTINCT *
    FROM departamento
    WHERE id_provincia = 54
"""

dfAf = dd.sql(Af).df()

# Ag.- Listar los registros de la tabla departamento cuyo código de provincia es igual a 22, 78 u 86.

Ag = """
    SELECT DISTINCT *
    FROM departamento
    WHERE id_provincia = 22 OR id_provincia = 78 OR id_provincia = 86
"""

dfAg = dd.sql(Ag).df()

# Ah.- Listar los registros de la tabla departamento cuyos códigos de provincia se encuentren entre el 50 y el 59 (ambos valores inclusive).

Ah = """
    SELECT DISTINCT *
    FROM departamento
    WHERE id_provincia > 49 AND id_provincia < 60
"""

dfAh = dd.sql(Ah).df()

#%%-----------
#=============================================================================
# Ejercicios B - Consultas multitabla (INNER JOIN)
#=============================================================================

# Ba.- Devolver una lista con los códigos y nombres de departamentos, asociados al nombre de la provincia al que pertenecen.

aux1 = """
    SELECT DISTINCT *
    FROM departamento, provincia
    WHERE departamento.id_provincia = provincia.id
"""

dfaux1 = dd.sql(aux1).df()

Ba = """
    SELECT DISTINCT id, descripcion, descripcion_1 as nombre_provincia
    FROM dfaux1
"""

dfBa = dd.sql(Ba).df()

# Bb.- Devolver una lista con los códigos y nombres de departamentos, asociados al nombre de la provincia al que pertenecen.
# es el mismo ejercicio que el anterior????

# Bc.- Devolver los casos registrados en la provincia de “Chaco”.

Bc = """
    SELECT DISTINCT *
    FROM dfBa
    WHERE nombre_provincia = 'Chaco'
"""
dfBc = dd.sql(Bc).df()

# Bd.- Devolver aquellos casos de la provincia de “Buenos Aires” cuyo campo cantidad supere los 10 casos.


DeptoBSAS = """
    SELECT DISTINCT *
    FROM dfBa
    WHERE nombre_provincia = 'Buenos Aires'
"""
dfDeptoBSAS = dd.sql(DeptoBSAS).df()

CasosBSAS = """
    SELECT DISTINCT *
    FROM casos, dfDeptoBSAS
    WHERE casos.id_depto = dfDeptoBSAS.id
"""
dfCasosBSAS = dd.sql(CasosBSAS).df()

Bd = """
    SELECT DISTINCT id,id_tipoevento,anio,semana_epidemiologica,id_depto,id_grupoetario,cantidad
    FROM dfCasosBSAS
    WHERE cantidad > 10
"""
dfBd = dd.sql(Bd).df()

#%%-----------
#=============================================================================
# Ejercicios C - Consultas multitabla (OUTER JOIN)
#=============================================================================

# Ca.- Devolver un listado con los nombres de los departamentos que no tienen ningún caso asociado.

deptoXcasos = """
    SELECT DISTINCT *
    FROM casos
    LEFT OUTER JOIN departamento
    ON departamento.id = casos.id_depto
"""
dfdeptoXcasos = dd.sql(deptoXcasos).df()

deptoSinCasos = """
    SELECT DISTINCT descripcion
    FROM dfdeptoXcasos
    WHERE id_depto = NULL
"""
dfCa = dd.sql(deptoSinCasos).df()

# Cb.- Devolver un listado con los tipos de evento que no tienen ningún caso asociado.

TipoEventoXCasos = """
    SELECT DISTINCT *
    FROM tipoevento
    LEFT OUTER JOIN casos
    ON tipoevento.id = casos.id_tipoevento
"""
dfTipoEventoXCasos = dd.sql(TipoEventoXCasos).df()

EventosConCasos = """
    SELECT DISTINCT descripcion
    FROM dfTipoEventoXCasos
"""
dfEventosConCasos = dd.sql(EventosConCasos).df()

#No entiendo este ejercicio.

#%%-----------
#=============================================================================
# Ejercicios D - Consultas resumen
#=============================================================================

# Da.- Calcular la cantidad total de casos que hay en la tabla casos

Da = """
    SELECT count(id) AS cant_casos
    FROM casos
"""
dfDa = dd.sql(Da).df()

# Db.-  Calcular la cantidad total de casos que hay en la tabla casos para cada año y cada tipo de caso. 
# Presentar la información de la siguiente manera: descripción del tipo de caso, año y cantidad. 
# Ordenarlo por tipo de caso (ascendente) y año (ascendente).

CasoConDescripcionTipoDeCaso = """
    SELECT DISTINCT *
    FROM casos
    INNER JOIN tipoevento
    ON casos.id_tipoevento = tipoevento.id
"""
dfTipoDeCaso = dd.sql(CasoConDescripcionTipoDeCaso).df()

Db = """
    SELECT descripcion, anio, COUNT(*) AS cant_casos
    FROM dfTipoDeCaso
    GROUP BY descripcion, anio
    ORDER BY cant_casos ASC
"""
dfDb = dd.sql(Db).df()

# Dc.- Misma consulta que el ítem anterior, pero sólo para el año 2019.

año2019 = """
    SELECT DISTINCT * 
    FROM dfTipoDeCaso
    WHERE anio = 2019
"""
df2019 = dd.sql(año2019).df()
Dc = """
    SELECT descripcion, anio, COUNT(*) AS cant_casos
    FROM df2019
    GROUP BY descripcion, anio
    ORDER BY cant_casos ASC
"""
dfDc = dd.sql(Dc).df()

# Dd.- Calcular la cantidad total de departamentos que hay por provincia. Presentar la información ordenada por código de provincia.

CantDptosXProvincia = """
    SELECT id_provincia, COUNT(*) AS cant_departamentos
    FROM departamento
    GROUP BY id_provincia
    ORDER BY cant_departamentos DESC
"""
dfDd = dd.sql(CantDptosXProvincia).df()

# De.- Listar los departamentos con menos cantidad de casos en el año 2019.

De = """
    SELECT anio, id_depto, COUNT(*) AS cant_casos
    FROM df2019
    GROUP BY anio, id_depto
    ORDER BY cant_casos ASC
"""
dfDe = dd.sql(De).df()

# Df.-  Listar los departamentos con más cantidad de casos en el año 2020.

anio2020 = """
    SELECT *
    FROM casos
    WHERE anio = 2020
"""
df2020 = dd.sql(anio2020).df()

Df = """
    SELECT anio, id_depto, COUNT(*) AS cant_casos2020
    FROM df2020
    GROUP BY anio, id_depto
    ORDER BY cant_casos2020 DESC
"""
dfDf = dd.sql(Df).df()





























