import pymysql
from pymysql import MySQLError

try:
    # Conectarse a la base de datos usando pymysql
    conexion = pymysql.connect(
        host='localhost',
        user='usuario',
        password='usuario',
        database='1dam'
    )
    if conexion.open:  # Verifica si la conexión está abierta
        print("Conexión a la base de datos exitosa")
except MySQLError as e:
    print(f"Error de conexión: {e}")
finally:
    if conexion.open:  # Verifica si la conexión sigue abierta
        conexion.close()
        print("Conexión cerrada")
