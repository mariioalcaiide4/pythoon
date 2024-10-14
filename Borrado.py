import pymysql

conexion = pymysql.connect(host='localhost', user='usuario', passwd='usuario', database='1dam')
cursor = conexion.cursor()
cursor.execute(    
"""
    DELETE FROM Libros WHERE editorial = 'Juan Ávila Editorial'
"""
)
conexion.commit()
print(cursor.rowcount, "registro(s) borrado(s)")
conexion.close(); 