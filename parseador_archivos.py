import os
import json

def parse_csv(nombre_archivo: str):
    lista_elementos = []
    lista_claves = []
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo, "r") as archivo:
            columnas = archivo.readline()
            columnas = columnas.replace("\n", "")
            lista_claves = columnas.split(",")
            for linea in archivo:
                linea_aux = linea.replace("\n", "")
                lista_valores = linea_aux.split(",")
                dict_aux = {}

                for i in range(len(lista_claves)):
                    dict_aux[lista_claves[i]] = lista_valores[i]
                
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
                lista_valores = list(elemento.values())
                for i in range(len(lista_valores)):
                    lista_valores[i] = str(lista_valores[i])
                
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

