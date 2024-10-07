import pymysql

conexion = pymysql.connect ( 
		host='localhost', 
		user='usuario', 
		password = "usuario", 
		db='1dam',) 

cursor = conexion.cursor()

		