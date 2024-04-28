#Librerias
import numpy as np
import time


# Función para leer los datos del archivo y calcular min, max y promedio
def procesar_archivo(nombre_archivo):
    estaciones = {}
    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            estacion, temperatura = linea.strip().split(';')
            temperatura = float(temperatura)
            if estacion not in estaciones:
                estaciones[estacion] = [temperatura]
            else:
                estaciones[estacion].append(temperatura)
    
    resultados = {}
    for estacion, temperaturas in estaciones.items():
        min_temp = min(temperaturas)
        max_temp = max(temperaturas)
        promedio_temp = sum(temperaturas) / len(temperaturas)
        resultados[estacion] = (min_temp, max_temp, promedio_temp)
    
    return resultados

archivo_entrada = 'datos.txt'
# Medir el tiempo de ejecución
inicio_tiempo = time.time()

resultados = procesar_archivo(archivo_entrada)
# Calcular el tiempo de ejecución
tiempo_ejecucion = time.time() - inicio_tiempo

for estacion, (min_temp, max_temp, promedio_temp) in resultados.items():
    print(f"Estación: {estacion}, Temp. Mínima: {min_temp}, Temp. Máxima: {max_temp}, Promedio: {promedio_temp}")
print(f"Tiempo de ejecución: {tiempo_ejecucion} segundos")