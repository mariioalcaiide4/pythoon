import ZODB, ZODB.FileStorage, transaction
from persistent import Persistent

# Establecer conexión a la base de datos ZODB

class Libro(Persistent):
    def__init__(self, autor, editorial, titulo, formato, tamaño_archivo)
    self.autor = autor
    self.editorial = editorial
    self.titulo = titulo
    self.formato = formato
    self.tamaño_archivo = tamaño_archivo
    

almacenamiento = ZODB.FileStorage.FileStorage('1dam.fs') # Almacenamiento en archivo ("base de datos" + .fs)

db = ZODB.DB(almacenamiento)

connection = db.open() # Abrir la base de datos

root = connection.root() 

root['La novia gitana'] = Libro('Carmen Mola', 'Atresplayer', 'La novia gitana', 'PDF', '5GB')
transaction.commit()

root['La red purpura'] = Libro('Carmen Mola', 'Atresplayer', 'La red purpura', 'PDF', '4GB')
transaction.commit()

root['La nena'] = Libro('Carmen Mola', 'Atresplayer', 'La nena', 'PDF', '6GB')
transaction.commit()
