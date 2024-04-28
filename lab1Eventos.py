#Librerias
import time
import random

def simular_eventos_lectura_archivo(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            yield linea.strip()
            # Simular retraso entre eventos
            time.sleep(random.uniform(0.001, 0.01))

def procesar_evento(evento):
    estacion, temperatura = evento.split(';')
    return estacion, float(temperatura)

def calcular_estadisticas(datos):
    estaciones = {}
    for estacion, temperatura in datos:
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

archivo_entrada = 'datos2.txt'
# Medir el tiempo de ejecución
inicio_tiempo = time.time()
eventos = simular_eventos_lectura_archivo(archivo_entrada)

for evento in eventos:
    datos = procesar_evento(evento)
    resultados = calcular_estadisticas([datos])
    for estacion, (min_temp, max_temp, promedio_temp) in resultados.items():
        print(f"Estación: {estacion}, Temp. Mínima: {min_temp}, Temp. Máxima: {max_temp}, Promedio: {promedio_temp}")

# Calcular el tiempo de ejecución
tiempo_ejecucion = time.time() - inicio_tiempo
print(f"Tiempo de ejecución: {tiempo_ejecucion} segundos")