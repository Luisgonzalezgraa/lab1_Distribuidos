#Librerias
from mpi4py import MPI
import numpy as np
import time

# Inicializar el comunicador MPI
comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

# Función para leer los datos del archivo y calcular min, max y promedio
def procesar_datos(nombre_archivo):
    # Leer datos del archivo
    with open(nombre_archivo, 'r') as archivo:
        estaciones = {}
        for linea in archivo:
            estacion, temperatura = linea.strip().split(';')
            temperatura = float(temperatura)
            if estacion not in estaciones:
                estaciones[estacion] = [temperatura]
            else:
                estaciones[estacion].append(temperatura)
    
    # Calcular min, max y promedio para cada estación
    resultados = {}
    for estacion, temperaturas in estaciones.items():
        min_temp = min(temperaturas)
        max_temp = max(temperaturas)
        promedio_temp = sum(temperaturas) / len(temperaturas)
        resultados[estacion] = (min_temp, max_temp, promedio_temp)
    
    return resultados

# Procesar los datos en paralelo
def procesar_datos_paralelo(nombre_archivo):
    # Leer datos y calcular parcialmente en cada proceso
    datos_parciales = comm.scatter([None] * size, root=0)
    datos_parciales = procesar_datos(nombre_archivo)
    
    # Recopilar todos los datos parciales en el proceso 0
    datos_totales = comm.gather(datos_parciales, root=0)
    
    # Consolidar los resultados en el proceso 0
    if rank == 0:
        resultados_finales = {}
        for datos_parciales in datos_totales:
            for estacion, (min_temp, max_temp, promedio_temp) in datos_parciales.items():
                if estacion not in resultados_finales:
                    resultados_finales[estacion] = [(min_temp, max_temp, promedio_temp)]
                else:
                    resultados_finales[estacion].append((min_temp, max_temp, promedio_temp))
        
        # Calcular los resultados finales
        for estacion, mediciones in resultados_finales.items():
            min_temp_total = min([medicion[0] for medicion in mediciones])
            max_temp_total = max([medicion[1] for medicion in mediciones])
            promedio_temp_total = sum([medicion[2] for medicion in mediciones]) / len(mediciones)
            resultados_finales[estacion] = (min_temp_total, max_temp_total, promedio_temp_total)
        
        return resultados_finales

# Nombre del archivo de entrada
nombre_archivo = 'datos.txt'

# Medir el tiempo de ejecución
inicio_tiempo = time.time()

# Procesar los datos en paralelo
resultados_finales = procesar_datos_paralelo(nombre_archivo)

# Calcular el tiempo de ejecución
tiempo_ejecucion = time.time() - inicio_tiempo

# Imprimir los resultados finales en el proceso 0
if rank == 0:
    for estacion, (min_temp, max_temp, promedio_temp) in resultados_finales.items():
        print(f"Estacion: {estacion}, Temp. minima: {min_temp}, Temp. maxima: {max_temp}, Promedio: {promedio_temp}")
    print(f"Tiempo de ejecucion: {tiempo_ejecucion} segundos")
