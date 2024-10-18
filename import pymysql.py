import pymysql
import time
import random

start_time = time.time()
end_time = time.time()

conexion = pymysql.connect(host ="localhost", user ="usuario", password ="usuario", database ="1dam")
cursor = conexion.cursor()

with conexion.cursor() as cursor:
    
    autor = {'Garcilaso de la Vega', 'Stephen King', 'Antonio Escohotado', 'Miguel de la Fuente' }
    tamaño_archivo = {'>1GB', '>10GB', '500MB', '300MB'}
    formato = {'PDF', 'EPUB', 'AZW', 'MOBI'}
    editorial = {'Édebe', 'Aliance', 'Universe', 'Sintesis'}
    titulo = f"Libro {i+1}"
    
    for i in range(10000):
        autor = random.choice(autor)
        tamaño_archivo = random.choice(tamaño_archivo)
        formato = random.choice(formato)
        editorial = random.choice(editorial)
        titulo = random.choice(titulo)
        
