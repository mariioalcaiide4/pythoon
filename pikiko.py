import csv
import json

class ConvertidorArchivos:

    def json_to_csv(self, json_file, csv_file):
        try:
            with open(json_file, mode='r') as f:
                data = json.load(f)
            with open(csv_open, mode='w') as f2:
                fieldnames = list(data[0].keys())
                boligrafo = csv.DictWriter(f2, fieldnames = fieldnames)
                boligrafo.writeheader()
                boligrafo.writerow(data)

        except Exception as e:       
            print(f"Error leyendo JSON {e}")
            
convertidor = ConvertidorArchivos()
convertidor.json_to_csv('data.csv', 'data.json')
