import pymysql 

def mysqlconnect(): 
	# To connect MySQL database 
	conn = pymysql.connect( 
		host='localhost', 
		user='usuario', 
		password = "usuario", 
		db='1dam', 
		) 
	
	cur = conn.cursor() 
	cur.execute("select @@version") 
	output = cur.fetchall() 
	print(output) 
	
# Driver Code 
if __name__ == "__main__" : 
	mysqlconnect()
 
if mysqlconnect == True:
    print("Conexión exitosa")
    conn.close()
else:
    print("Conexión fallida")
    conn.close()
