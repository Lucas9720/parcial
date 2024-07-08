import os
import json
import csv

def parse_csv(nombre_archivo: str):
    lista_elementos = []
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo, "r", newline='', encoding='utf-8') as archivo:
            contenido = archivo.read()
            lineas = contenido.splitlines()
            
            # Obtener las claves desde la primera línea
            lista_claves = lineas[0].split(',')
            
            # Iterar sobre las líneas restantes (datos)
            for linea in lineas[1:]:
                # Dividir la línea en valores, preservando los valores entre comillas
                valores = csv.reader([linea]).__next__()
                
                # Crear un diccionario para almacenar los datos de esta línea
                dict_aux = {}
                for i in range(len(lista_claves)):
                    dict_aux[lista_claves[i].strip()] = valores[i].strip()  # Eliminar espacios alrededor de los valores
                
                lista_elementos.append(dict_aux)
                
        return lista_elementos
    else:
        return "archivo no encontrado"


def generar_csv(nombre_archivo: str, lista: list):
    if len(lista) > 0:
        separador = ","
        lista_claves = list(lista[0].keys())
        cabecera = separador.join(lista_claves)
        
        with open(nombre_archivo, "w") as archivo:
            archivo.write(cabecera + "\n") 
            for elemento in lista:
                lista_valores = []
                for clave in lista_claves:
                    valor = elemento[clave]
                    # Si la clave es "Presupuesto", guardar el valor entre comillas
                    if clave == "Presupuesto":
                        valor = f'"{valor}"'
                    lista_valores.append(str(valor))
                
                dato = separador.join(lista_valores)
                dato += "\n"
                archivo.write(dato)

def parsear_json(nombre_archivo: str):
    try:
        with open(nombre_archivo, "r") as archivo:
            lista_elementos = json.load(archivo)
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no fue encontrado.")
        lista_elementos = []  # Retornar una lista vacía en caso de error
    except json.JSONDecodeError:
        print(f"Error: El archivo '{nombre_archivo}' no contiene un JSON válido.")
        lista_elementos = []  # Retornar una lista vacía en caso de error
    
    return lista_elementos


def generar_json(nombre_archivo: str, lista: list):
    with open(nombre_archivo, "w") as archivo:
        json.dump(lista, archivo, indent= 4)

