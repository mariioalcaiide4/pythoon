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

class DataManager:
    def __init__(self, ruta_archivo, tipo_archivo='json'):
        self.ruta_archivo = ruta_archivo
        self.tipo_archivo = tipo_archivo
        self.version = 1
        self.transaccion_activa = False
        self.copia_datos = None    
        
        # Cargar datos si el archivo existe, o inicializar un diccionario vacío
        
        if os.path.exists(ruta_archivo):
            self.datos = self.leer_archivo()
            logging.info(f"Archivo {tipo_archivo.upper()} cargado con éxito. Versión actual:{self.version}")
        else:
            self.datos = []
            self._guardar_archivo()
            
    def _leer_archivo(self):
        if self.tipo_archivo == 'json':
            with open(self.ruta_archivo, 'r') as archivo:
                return json.load(archivo)
        elif self.tipo_archivo == 'csv':
            info = []
            with open(self.ruta_archivo, mode='r') as archivo1:
                lector = csv.DictReader(archivo1)    
                for fila in lector:
                    info.append(fila)
            return info        
        else:
            raise ValueError("Formato no válido. Solo JSON o CSV")
    
    def _guardar_archivo(self):
        if self.tipo_archivo == 'json':
            with open(self.ruta_archivo, 'w') as archivo:
                json.dump(self.datos, archivo, indent=4 )    
        elif self.tipo_archivo == 'csv':
            with open(self.ruta_archivo, mode='w', newline='') as archivo:
                escritor = csv.DictWriter(archivo, fieldnames=self.datos[0].keys())
                escritor.writeheader()
                escritor.writerows(self.datos)
                logging.info(f"Archivo {tipo_archivo.upper()} guardado con éxito. Versión actual:{self.version}")
                
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
        self._guardar_archivo
        logging.info("Transacción confirmada y cambios guardados")
        
    def revertir_transaccion(self):
        if not self.transaccion_activa:
            raise Exception("No hay una transaccion activa para revertir")    
        self.datos = self.copia_datos # Volver a la copia de seguridad
        self.transaccion_activa = False
        self.copia_datos = None
        logging.warning("Transacción revertida. Los cambios no fueron guardados")
        