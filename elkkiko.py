import csv

class CSVManejo:


    def leer_csv(self, file_path):
        try:
            with open(file_path, mode='r', newline='') as f:
                lector = csv.DictReader(f)

# Creamos el objeto lector para leer filas

                filas = [] # Creamos una lista vacia
                for row in lector: # Recorremos la lista fila por fila
                    filas.append(row) # Metemos en la lista cada fila
                return filas # Devolvemos la lista con las filas
        except Exception as e:
            print("Error leyendo el archivo CSV {e}")


    def escribir_csv(self, file_path, datos, fieldnames):
        try:
            with open(file_path, mode='w', newline='') as f:
                boligrafo = csv.DictWriter(f, fieldnames = fieldnames)
                boligrafo.writeheader()
                boligrafo.writerow(datos)
        except Exception as e:
            print("Error escribiendo en el archivo CSV {e}")


# Uso

csv_handler = CSVManejo()

file_path = 'data.csv'

datos = {
    "Nombre": "Mario",
    "Apellido": "Alcaide",
    "Sexo": "Masculino",
    "Edad": "19" }

fieldnames = ["Nombre", "Apellido", "Sexo", "Edad"]

csv_handler.escribir_csv(file_path, datos, fieldnames)
contenido_csv = csv_handler.leer_csv(file_path)
print(contenido_csv)
