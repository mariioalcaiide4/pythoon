import json
import csv
import logging
import os
from datetime import datetime
from copy import deepcopy

# Configuración del logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler("datos_log.log"),]
)

import json
import csv
import logging
import os
from datetime import datetime
from copy import deepcopy

# Configuración del logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler("datos_log.log")]
)

class Manejador:
    def __init__(self, ruta_archivo, tipo_archivo='json'):
        self.ruta_archivo = ruta_archivo
        self.tipo_archivo = tipo_archivo
        self.version = 1
        self.transaccion_activa = False
        self.copia_datos = None

        if os.path.exists(ruta_archivo):
            self.datos = self._leer_archivo()
            logging.info(f"Archivo {tipo_archivo.upper()} cargado con éxito. Versión actual: {self.version}")
        else:
            self.datos = []
            self._guardar_archivo()
            logging.info(f"Archivo {tipo_archivo.upper()} creado e inicializado vacío: {self.ruta_archivo}")

    def _leer_archivo(self):
        if self.tipo_archivo == 'json':
            try:
                with open(self.ruta_archivo, 'r') as archivo:
                    return json.load(archivo)
            except json.JSONDecodeError:
                logging.warning(f"Archivo JSON vacío o inválido: {self.ruta_archivo}. Se inicializa como vacío.")
                return []
        elif self.tipo_archivo == 'csv':
            info = []
            try:
                with open(self.ruta_archivo, mode='r') as archivo1:
                    lector = csv.DictReader(archivo1)
                    for fila in lector:
                        info.append(fila)
            except Exception as e:
                logging.warning(f"Archivo CSV vacío o inválido: {self.ruta_archivo}. Error: {e}")
                return []
            return info
        else:
            raise ValueError("Formato no válido. Solo JSON o CSV")

    def _guardar_archivo(self):
        if self.tipo_archivo == 'json':
            with open(self.ruta_archivo, 'w') as archivo:
                json.dump(self.datos, archivo, indent=4)
        elif self.tipo_archivo == 'csv':
            with open(self.ruta_archivo, mode='w', newline='') as archivo:
                if self.datos:
                    escritor = csv.DictWriter(archivo, fieldnames=self.datos[0].keys())
                    escritor.writeheader()
                    escritor.writerows(self.datos)
                else:
                    archivo.write("")

    def iniciar_transaccion(self):
        if self.transaccion_activa:
            raise Exception("Ya hay una transacción activa.")
        self.transaccion_activa = True
        self.copia_datos = deepcopy(self.datos)
        logging.info("Transacción iniciada.")

    def confirmar_transaccion(self):
        if not self.transaccion_activa:
            raise Exception("No hay transacción activa para confirmar")
        self.version += 1
        self.transaccion_activa = False
        self.copia_datos = None
        self._guardar_archivo()
        logging.info("Transacción confirmada y cambios guardados")

    def revertir_transaccion(self):
        if not self.transaccion_activa:
            raise Exception("No hay una transacción activa para revertir")
        self.datos = self.copia_datos
        self.transaccion_activa = False
        self.copia_datos = None
        logging.warning("Transacción revertida. Los cambios no fueron guardados")

    def leer_dato(self, clave, valor):
        return [dato for dato in self.datos if dato.get(clave) == valor]

    def escribir_dato(self, nuevo_dato):
        if not self.transaccion_activa:
            raise Exception("Debe iniciar una transacción antes de realizar cambios.")
        if self.datos and not isinstance(nuevo_dato, dict):
            raise ValueError("El nuevo dato debe ser un diccionario.")
        if self.datos and set(nuevo_dato.keys()) != set(self.datos[0].keys()):
            raise ValueError("El nuevo dato no tiene las mismas claves que los datos existentes.")
        self.datos.append(nuevo_dato)
        logging.info(f"Dato agregado: {nuevo_dato}")

    def eliminar_dato(self, clave, valor):
        if not self.transaccion_activa:
            raise Exception("Debe iniciar una transacción antes de realizar cambios")
        self.datos = [dato for dato in self.datos if dato.get(clave) != valor]

   

        
    def obtener_configuracion(self):
        return {
        "ruta_archivo" : self.ruta_archivo,
        "tipo_archivo" : self.tipo_archivo,
        "version" : self.version,
        "transaccion_archivo" : self.transaccion_activa}    
        
    def actualizar_configuracion(self, nueva_ruta, nuevo_tipo=None):
        if self.transaccion_activa:
            raise Exception("No se puede cambiar la configuración mientras una transacción esté activa")        
        self.ruta_archivo = nueva_ruta
        if nuevo_tipo:
            self.tipo_archivo = nuevo_tipo            
        logging.info(f"Configuración actualizada. Nueva ruta del archivo: {self.ruta_archivo}")    
        
class Libro:
    
    def __init__(self, titulo, genero, autor, año_publicacion):
        self.titulo = titulo,
        self.genero = genero,
        self.autor = autor,
        self.año_publicacion = año_publicacion            
    
    def to_dict(self):
        return {
            "titulo" : self.titulo,
            "genero" : self.genero,
            "autor" : self.autor,
            "año_publicacion" : self.año_publicacion
        }
    
if __name__== "__main__":
    libro1 = Libro("Sombras en el Alba", "Histórica", "María del Carmen Lopez", 2018)
    libro2 = Libro("El Enigma del Horizonte", "Ciencia ficción", "Joaquín Álvarez", 2022)   
    libro3 = Libro("Caminos de Sal y Luna", "Poesía", "Isabel Fernández", 2015)
    
    libros = [libro1.to_dict(), libro2.to_dict(), libro3.to_dict()]
    
    gestor = Manejador("libros.json", "json") 
    
    gestor.iniciar_transaccion()
    for libro in libros:
        gestor.escribir_dato(libro)
    gestor.confirmar_transaccion()    
    
    gestor.actualizar_configuracion("libros.csv", "csv")
    
    gestor.iniciar_transaccion()
    for libro in libros:
        gestor.escribir_dato(libro)
    gestor.confirmar_transaccion()