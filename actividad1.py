from peewee import MySQLDatabase, Model, CharField, IntegerField
    
db = MySQLDatabase(
    '1dam',     # Nombre de la base de datos
    user='usuario', # Usuario de MySQL
    password='usuario', # Contraseña de MySQL
    host='localhost', # Host
    port=3306 # Puerto por defecto de MySQL
)
    # Conectar a la base de datos
db.connect()
print("Conexión exitosa a la base de datos.")

class Libro(Model):
    
    autor = CharField()
    editorial = CharField()
    titulo = CharField()
    formato = CharField()
    tamaño_archivo = CharField()
    
    class Meta:
        database = db # Base de datos
        table_name = 'Libros' # Nombre de la tabla en la base de datos

def tabla_existe(Libros):
    consulta = "SELECT COUNT(*) FROM information_schema.tables WHERE table_schema = %s AND table_name = %s"
    cursor = db.execute_sql(consulta, ('1dam', 'Libros'))
    resultado = cursor.fetchone()
    return resultado[0] > 0

if tabla_existe(Libro._meta.table_name):
    print(f"La tabla '{Libro._meta.table_name}' existe.")
    db.drop_tables([Libro], cascade=True)
    print(f"Tabla '{Libro._meta.table_name}' eliminada con éxito.")
else:
    print(f"La tabla '{Libro._meta.table_name}' no existe.")


db.create_tables([Libro])

print("Tabla 'Libros' creada o ya existente.")

Libro.create(autor='Julia Navarrete', editorial='Éxitos', titulo='El niño que perdio la guerrilla', formato='PDF', tamaño_archivo='2GB')

Libro.create(autor='Lope de Vega', editorial='Anónimo', titulo='Fuente Ovejuna', formato='PDF', tamaño_archivo='1GB')

Libro.create(autor='Jose Zorrilla', editorial='Anónimo', titulo='Don Juan Tenorio', formato='PDF', tamaño_archivo='2GB')

Libro.create(autor='Leopoldo Alas', editorial='Anónimo', titulo='La Regenta', formato='PDF', tamaño_archivo='500MB')

Libro.create(autor='Miguel Delibes', editorial='Anónimo', titulo='El camino', formato='PDF', tamaño_archivo='720MB')


print("Libros insertados en la base de datos.")
