import json

diccionario = {"DNI": 12345679, "fecha_de_nacimiento": "16/06/96"} 
class JSONManejo:

    def leer_json(self, self_path):
        try:
            with open(self_path, 'r') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error leyendo JSON: {e}")

    def escribir_json(self, self_path, diccionario):
        try:
            with open("data.json", 'w') as f:
                json.dump(diccionario, f)
        except Exception as e:
            print(f"Error escribiendo sobre JSON: {e}")




#Uso

json_handler = JSONManejo()
data = json_handler.escribir_json('data.json', diccionario)
data = json_handler.leer_json('data.json')
print(data)
