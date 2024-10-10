import pymysql

conexion = pymysql.connect(host='localhost', user='usuario', passwd='usuario', database='1dam')
cursor = conexion.cursor()
cursor.execute(
    "INSERT INTO Libros (nombre, autor, genero, fecha_publicacio, editorial) VALUES (%s, %s, %s, %s, %s)",
    ("Platero y yo", "Juan Ramón Jimenez", "Aventura", "1914", "Alianza Editorial")
)
conexion.commit()
cursor.execute("SELECT * FROM Libros")
for fila in cursor.fetchall():
    print(fila)

conexion.close(); 