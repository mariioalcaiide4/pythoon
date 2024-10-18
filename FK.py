import pymysql
from pymysql import MySQLError

try:
    conexion = pymysql.connect(
        host='localhost', 
        user='usuario', 
        passwd='usuario', 
        database='1dam')
    
    cursor = conexion.cursor()

    sql_crear_proveedores = """
    CREATE TABLE IF NOT EXISTS Proveedores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    direccion VARCHAR(100)
    )
    """
    cursor.execute(sql_crear_proveedores)
    sql_alter_herramientas = """
    ALTER TABLE Libros ADD proveedor_id INT,
    ADD CONSTRAINT fk_proveedor
    FOREIGN KEY (proveedor_id) REFERENCES Proveedores(id)
    """
    cursor.execute(sql_alter_herramientas)
    print("Relación entre Libros y Proveedores creada.")
except MySQLError as e:
    print("Error de conexion: {e}")