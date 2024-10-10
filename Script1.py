import pymysql
import time
import random

start_time = time.time()
end_time = time.time()

conexion = pymysql.connect(host ="localhost", user ="usuario", password ="usuario", database ="1dam")
cursor = conexion.cursor()

with conexion.cursor() as cursor:
    
    autor = {'Garcilaso de la Vega', 'Stephen King', 'Antonio Escohotado', 'Miguel de la Fuente' }
    genero = {'Terror', 'Aventura', 'Suspense', 'Comedia'}
    fecha_publicacio = {'90s', '80s', '70s', '1900'}
    editorial = {'Édebe', 'Aliance', 'Pikiko', 'Sintesis'}
    nombre = f"Libro {i+1}"
    
    for i in range(10000):
        autor = random.choice(autor)
        genero = random.choice(genero)
        fecha_publicacio = random.choice(fecha_publicacio)
        editorial = random.choice(editorial)
        
cursor.execute (
    "INSERT INTO Libros "
    
    
    
)        
        
        

    
    

