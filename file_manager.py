import os 
import json 

def read_json():
    if not os.path.isfile('task.json'):
        with open('task.json', 'w') as file:
            json.dump([], file) # creamos un arreglo vacio en un nuevo archivo json en caso de que no se encuentre el JSON principal
        
    with open('task.json', 'r') as file:
        return json.load(file) # retornamos el contenido del archivo JSON pero en formato de objeto gracias a la funcion load


def write_json(data):
    with open('task.json', 'w') as file:
        json.dump(data, file) # escribimos el contenido del arreglo data en el archivo JSON

