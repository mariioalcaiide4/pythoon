import pymysql

conexion = pymysql.connect(host='localhost', user='usuario', passwd='usuario', database='1dam')
cursor = conexion.cursor()
cursor.execute("SELECT * FROM Libros LIMIT 5")
primera_fila = cursor.fetchone()
print(primera_fila)