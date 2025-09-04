# Tarea 1
# Realizada por: Félix Soriano y Sofía Glionna

# Actividad 0)

empleado_01=[[20222333,45,2,20000],
            [33456234,40,0,25000],
            [45432345,41,1,10000]]

# Actividad 1)

def superanSalarioActividad01 (matriz,umbral):
    res = []
    for i in range (0,len(matriz)):
        if matriz[i][3] >= umbral:
            res.append(matriz[i])
    return res

# Actividad 2)

empleado_02=[[20222333,45,2,20000],
            [33456234,40,0,25000],
            [45432345,41,1,10000],
            [43967304,37,0,12000],
            [42236276,36,0,18000]]

#actividad 3)

empleado_03 = [[20222333,20000,45,2],
            [33456234,25000,40,0],
            [45432345,10000,41,1],
            [43967304,12000,37,0],
            [42236276,18000,36,0]]

def superanSalarioActual03 (matriz,umbral):
    res = []
    for i in range(0,len(matriz)):
        if matriz[i][1] >= umbral:
            res.append(empleado_02[i])
    return res

# Actividad 4)

empleado_04 = [[20222333,33456234,45432345,43967304,42236276],
                 [20000,25000,10000,12000,18000],
                 [45,40,41,37,36],
                 [2,0,1,0,0]]

def superanSalarioActividad04 (matriz, umbral):
    res = []
    for i in range(0,len(matriz[1])):
        if matriz[1][i] >= umbral:
            res.append(empleado_02[i])
    return res

#actividad 5)

#1)

#a. No afectó en nada.

#b. Si se modifica el orden de las columnas, la función superanSalarioActividad01 deja de ser útil. 
# Por lo que implementamos superanSalarioActividad03 cambiando solamente la columna indexada.

#2) Debimos modificarla nuevamente para poder indexar los salarios que en este ejercicio se encuentran todos en una misma lista.
#Para lo que accedimos a la lista en concreto y fuimos avanzando sobre la misma. Como conservamos el orden de los salarios respecto
#al de los empleados (en la fila de salarios de la actividad 4, el salario que se encuentra en la posición i pertenece al empleado de la fila i en el resto de matrices)
#pudimos identificar en todo momento de qué empleado era cada salario, agregandolos al resultado.

#3) Principalmente facilitar la tarea del usuario, quien no tiene porqué conocer el código en cuestión, si no solo saber
# su utilidad. Además promueve la reutilización de la fución.