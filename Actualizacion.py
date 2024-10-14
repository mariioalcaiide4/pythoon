import pymysql

conexion = pymysql.connect(host='localhost', user='usuario', passwd='usuario', database='1dam')
cursor = conexion.cursor()
cursor.execute(    
"""
    UPDATE Libros SET editorial = 'Juan Ávila Editorial' WHERE nombre = 'Platero y yo'
"""
)
conexion.commit()
print(cursor.rowcount, "registro(s) actualizado(s)")
conexion.close(); 