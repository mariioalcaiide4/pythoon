import mysql.connector
conexion = mysql.connector.connect(host='localhost', user='usuario', password='usuario', database='1dam')
print("Conexión Establecida")
cursor = conexion.cursor()
cursor.execute(
    "INSERT INTO Libros (titulo, autor, formato, tamaño_archivo, editorial) VALUES (%s, %s, %s, %s, %s)",
    ("Platero y yo", "Juan Ramón Jimenez", "PDF", "108MB", "Alianza Editorial")
)
conexion.commit()

cursor.execute("SELECT * FROM Libros")

print(cursor.fetchone())
print(cursor.fetchone())
print(cursor.fetchone())
print(cursor.fetchone())
print(cursor.fetchone())

cursor.close()
cursor2 = conexion.cursor()
cursor2.execute(
    "INSERT INTO Libros (titulo, autor, formato, tamaño_archivo, editorial) VALUES (%s, %s, %s, %s, %s)",
    ("Juanito Alimaña", "Voltio", "PDF", "250MB", "Pikirko Editorial")
)  

cursor2.execute("SELECT * FROM Libros")

print(cursor2.fetchone())
print(cursor2.fetchone())
print(cursor2.fetchone())
print(cursor2.fetchone())
print(cursor2.fetchone())

cursor2.close
conexion.close
print("Conexion cerrada") 