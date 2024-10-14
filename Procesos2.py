import pymysql

conexion = pymysql.connect(host='localhost', user='usuario', passwd='usuario', database='1dam')
cursor = conexion.cursor()
cursor.execute(
   """
    CREATE TABLE IF NOT EXISTS Proveedores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    direccion VARCHAR(100)
    )
    """
)
cursor.execute(
    """
    ALTER TABLE Libros ADD proveedor_id INT,
    ADD CONSTRAINT fk_proveedor
    FOREIGN KEY (proveedor_id) REFERENCES Proveedores(id)
    """
)    
conexion.commit()
print("Relación entre Libros y Proveedores exitosa")
conexion.close(); 