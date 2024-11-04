import ZODB, ZODB.FileStorage, transaction

# Establecer conexión a la base de datos ZODB

almacenamiento = ZODB.FileStorage.FileStorage('1dam.fs') # Almacenamiento en archivo ("base de datos" + .fs)

db = ZODB.DB(almacenamiento)

connection = db.open() # Abrir la base de datos

root = connection.root() # Conectar por root a la base de datos

root['libreria'] = ['IT', 'El Cóndor', 'Harry Potter'] # 

transaction.commit() # Confirmar los cambios y recuperar la lista almacenada y mostrarla

print(root['libreria']) 

# Cerrar la conexión y la base de datos

connection.close()

db.close()
