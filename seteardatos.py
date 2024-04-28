import random
#Funcion que sirve para generar datos aleatorios de rango 1 a 45 grados
def generar_datos(nombre_archivo, cantidad_datos):
    estaciones = ["Hamburg", "Bulawayo", "Palembang", "St. John's", "Cracow", 
                  "Bridgetown", "Istanbul", "Roseau", "Conakry", "Istanbul"]
    
    with open(nombre_archivo, 'w') as archivo:
        for _ in range(cantidad_datos):
            estacion = random.choice(estaciones)
            temperatura = round(random.uniform(1.0, 45.0), 1)
            archivo.write(f"{estacion};{temperatura}\n")

nombre_archivo = 'datos.txt'
cantidad_datos = 3240004
#se llama a la funcion
generar_datos(nombre_archivo, cantidad_datos)
#se imprime si se puedo setear
print(f"Archivo '{nombre_archivo}' creado exitosamente con {cantidad_datos} datos.")