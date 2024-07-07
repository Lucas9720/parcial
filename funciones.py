from datetime import datetime
from parseador_archivos import *

NOMBRE_ARCHIVO = "Proyectos.csv"
id_autoincremental = 0

def validar_nombre(nombre: str) -> bool:
    # Verificar que el nombre no exceda los 30 caracteres
    if len(nombre) > 30:
        return False

    # Verificar que el nombre solo contenga caracteres alfabéticos
    for char in nombre:
        if not char.isalpha():
            return False

    return True

def validar_presupuesto(presupuesto: int) -> bool:
    # Verificar que el presupuesto sea un valor numérico entero no menor a $500000
    if isinstance(presupuesto, int) and presupuesto >= 500000:
        return True
    else:
        return False
    
def validar_descripcion(descripcion: str) -> bool:
    # Verificar que la descripción no exceda los 200 caracteres
    if len(descripcion) > 200:
        return False

    # Verificar que la descripción solo contenga caracteres alfanuméricos y espacios
    for char in descripcion:
        if not (char.isalnum() or char.isspace()):
            return False

    return True

def validar_fecha(fecha: str) -> bool:
    formato = "%d/%m/%Y"
    
    try:
        # Convertir las cadenas de texto en objetos de fecha
        datetime.strptime(fecha, formato)

        return True
    except ValueError:
        # Si hay un error en la conversión de la fecha, no es una fecha válida
        return False

def validar_rango_fechas(fecha_inicio: str, fecha_finalizacion: str) -> bool:
    formato = "%d/%m/%Y"
    
    # Convertir las cadenas de texto en objetos de fecha
    inicio = datetime.strptime(fecha_inicio, formato)
    finalizacion = datetime.strptime(fecha_finalizacion, formato)
    
    # Verificar que la fecha de finalización no sea anterior a la fecha de inicio
    return finalizacion >= inicio



def crear_proyecto():
    # pido el nombre al usuario
    nombre = input("ingrese el nombre del proyecto: ")
    while not (validar_nombre(nombre)):
        nombre = input("por favor ingrese un nombre valido: ")
    
    # pido la descripcion al usuario
    descripcion = input("ingrese la descripcion: ")
    while not (validar_descripcion(descripcion)):
        descripcion = input("por favor ingrese una descripcion valida: ")
    
    # pido el presupuesto al usuario
    presupuesto = int(input("ingrese el presupuesto: "))
    while not (validar_presupuesto(presupuesto)):
        presupuesto = input("por favor ingrese el presupuesto: ")
    
    # pido la fecha de inicio y finalizacion 
    fecha_de_inicio = input("ingrese la fecha de inicio en formato: dd/mm/aaaa: ")
    while not (validar_fecha(fecha_de_inicio)):
        fecha_de_inicio = input("Por favor. ingrese la fecha de inicio en formato: dd/mm/aaaa: ")

    #valido que la fecha de finalizacion este en el formato correcto y no sea anterior a la fecha de inicio
    fecha_de_finalizacion = input("ingrese la fecha de inicio en formato: dd/mm/aaaa: ")
    while not (validar_fecha(fecha_de_finalizacion) and validar_rango_fechas(fecha_de_inicio, fecha_de_finalizacion)):
        fecha_de_finalizacion = input("Por favor. ingrese la fecha de inicio en formato: dd/mm/aaaa y posterior a la fecha de inicio: ")
    
    #guardo el parseo del csv en una variable
    lista_proyectos = parse_csv(NOMBRE_ARCHIVO)

    #verifico cuantos ids tiene la lista
    cantidad_ids = len(lista_proyectos)

    #agrego el nuevo proyecto a la lista
    id_autoincremental = cantidad_ids + 1
    nuevo_proyecto = { "id": id_autoincremental, 
                      "Nombre del Proyecto": nombre, 
                      "Descripción": descripcion,
                      "Fecha de inicio": fecha_de_inicio,
                      "Fecha de Fin": fecha_de_finalizacion,
                      "Presupuesto": presupuesto,
                      "Estado": "ACTIVO"}
    lista_proyectos.append(nuevo_proyecto)

    generar_csv(NOMBRE_ARCHIVO, lista_proyectos)
    print("proyecto agregado exitosamente")





    
    
    






            