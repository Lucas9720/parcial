from datetime import datetime
from parseador_archivos import *
from typing import Dict

NOMBRE_ARCHIVO = "Proyectos.csv"
FORMATO = "%d-%m-%Y"
id_autoincremental = 0
#guardo el parseo del csv en una variable
lista_proyectos = parse_csv(NOMBRE_ARCHIVO)

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
    global FORMATO
    
    try:
        # Convertir las cadenas de texto en objetos de fecha
        datetime.strptime(fecha, FORMATO)

        return True
    except ValueError:
        # Si hay un error en la conversión de la fecha, no es una fecha válida
        return False

def validar_rango_fechas(fecha_inicio: str, fecha_finalizacion: str) -> bool:
    global FORMATO
    
    # Convertir las cadenas de texto en objetos de fecha
    inicio = datetime.strptime(fecha_inicio, FORMATO)
    finalizacion = datetime.strptime(fecha_finalizacion, FORMATO)
    
    # Verificar que la fecha de finalización no sea anterior a la fecha de inicio
    return finalizacion >= inicio

#valida si el estado ingresado por parametro es Activo, Cancelado o Finalizado, en caso de que no, retorna false
def validar_estado(estado: str):
   return estado == "Activo" or estado == "Cancelado" or estado ==  "Finalizado"

def crear_proyecto():
    global lista_proyectos
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
    fecha_de_inicio = input("ingrese la fecha de inicio en formato: dd-mm-aaaa: ")
    while not (validar_fecha(fecha_de_inicio)):
        fecha_de_inicio = input("Por favor. ingrese la fecha de inicio en formato: dd-mm-aaaa: ")

    #valido que la fecha de finalizacion este en el formato correcto y no sea anterior a la fecha de inicio
    fecha_de_finalizacion = input("ingrese la fecha de inicio en formato: dd-mm-aaaa: ")
    while not (validar_fecha(fecha_de_finalizacion) and validar_rango_fechas(fecha_de_inicio, fecha_de_finalizacion)):
        fecha_de_finalizacion = input("Por favor. ingrese la fecha de inicio en formato: dd-mm-aaaa y posterior a la fecha de inicio: ")

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

def ingresar_id_a_modificar():
    global lista_proyectos

    id = input("ingrese el id: ")
    
    # Buscar el diccionario que contiene el valor especificado en la clave "id"
    resultado = next((item for item in lista_proyectos if item["id"] == id), None)
    
    while(resultado is None):
        id = input("El id no existe, ingrese el id: ")
    
    return resultado

#se ingresa un proyecto a modifica por parametro
def modificar_proyecto(proyecto: Dict):
    global lista_proyectos

    columna_a_modificar = int(input("Ingrese la opcion a modificar\n1 para 'Nombre del Proyecto'\n2 para 'Descripción'\n3 para 'Fecha de inicio'\n4 para 'Fecha de Fin'\n5 para 'Presupuesto'\n6 para 'Estado': "))
    while columna_a_modificar < 1 or columna_a_modificar > 6:
        columna_a_modificar =  int(input("Por favor, Ingrese una opcion correcta a modificar\n1 para 'Nombre del Proyecto'\n2 para 'Descripción'\n3 para 'Fecha de inicio'\n4 para 'Fecha de Fin'\n5 para 'Presupuesto'\n6 para 'Estado': "))

    match columna_a_modificar:
        case 1: 
            nombre_nuevo = input("ingrese el nuevo nombre del proyecto: ")
            while not (validar_nombre(nombre_nuevo)):
                 nombre_nuevo = input("por favor ingrese un nombre valido: ")
        
            proyecto["Nombre del Proyecto"] = nombre_nuevo
            generar_csv(NOMBRE_ARCHIVO, lista_proyectos)
            print("el proyecto modifico el nombre exitosamente")
    
        case 2:
            descripcion_nueva = input("Ingrese la nueva descripción del proyecto: ")
            while not validar_descripcion(descripcion_nueva):
                descripcion_nueva = input("Por favor, ingrese una descripción válida: ")
            
            proyecto["Descripción"] = descripcion_nueva
            generar_csv(NOMBRE_ARCHIVO, lista_proyectos)
            print("El proyecto modificó la descripción exitosamente.")
        
        case 3:
            fecha_inicio_nueva = input("Ingrese la nueva fecha de inicio (DD-MM-AAAA): ")
            while not validar_fecha(fecha_inicio_nueva):
                fecha_inicio_nueva = input("Por favor, ingrese una fecha de inicio válida (DD-MM-AAAA): ")
            
            proyecto["Fecha de inicio"] = fecha_inicio_nueva
            generar_csv(NOMBRE_ARCHIVO, lista_proyectos)
            print("El proyecto modificó la fecha de inicio exitosamente.")
        
        case 4:
            fecha_fin_nueva = input("Ingrese la nueva fecha de fin (DD-MM-AAAA): ")
            while not validar_fecha(fecha_fin_nueva):
                fecha_fin_nueva = input("Por favor, ingrese una fecha de fin válida (DD-MM-AAAA): ")
            
            proyecto["Fecha de Fin"] = fecha_fin_nueva
            generar_csv(NOMBRE_ARCHIVO, lista_proyectos)
            print("El proyecto modificó la fecha de fin exitosamente.")
        
        case 5:
            presupuesto_nuevo = int(input("Ingrese el nuevo presupuesto (entero no menor a $500000): "))
            while not validar_presupuesto(presupuesto_nuevo):
                presupuesto_nuevo = int(input("Por favor, ingrese un presupuesto válido (entero no menor a $500000): "))
            
            proyecto["Presupuesto"] = presupuesto_nuevo
            generar_csv(NOMBRE_ARCHIVO, lista_proyectos)
            print("El proyecto modificó el presupuesto exitosamente.")
        
        case 6:
            estado_nuevo = input("Ingrese el nuevo estado del proyecto(Activo, Finalizado o Cancelado): ")
            while not validar_estado(estado_nuevo):
                estado_nuevo = input("Por favor, ingrese un estado válido: ")
            
            proyecto["Estado"] = estado_nuevo
            generar_csv(NOMBRE_ARCHIVO, lista_proyectos)
            print("El proyecto modificó el estado exitosamente.")

# le pide al usuario un id, y en caso de que exista, se le modifica el estado a cancelado                
def cancelar_proyecto():
    global lista_proyectos
    proyecto = ingresar_id_a_modificar()
    proyecto["Estado"] = "Cancelado"
    generar_csv(NOMBRE_ARCHIVO, lista_proyectos)
    print("proyecto cancelado exitosamente")

# Cambiará el estado de todos los proyectos cuya fecha de finalización ya haya sucedido.
def comprobar_proyectos():
    global FORMATO
    global lista_proyectos
    #obtengo la fecha de hoy en formato 'dd-mm-aaaa'
    fecha_hoy = datetime.today()
    fecha_hoy_formateada = fecha_hoy.strftime(FORMATO)

    #Recorro toda la lista
    for proyecto in lista_proyectos:
        #busco algun proyecto donde la fecha sea menor a la fecha de hoy
        if not validar_rango_fechas(fecha_hoy_formateada,proyecto['Fecha de Fin']):
            proyecto['Estado'] = "Finalizado"
    generar_csv(NOMBRE_ARCHIVO, lista_proyectos)
    print("proyectos comprobados exitosamente")

def mostrar_proyectos():
    global lista_proyectos
    
    # Cabecera de la tabla
    print("| Nombre del Proyecto | Descripción | Presupuesto | Fecha de Inicio | Fecha de Fin | Estado |\n")
    
    # Recorriendo la lista de proyectos y mostrando cada proyecto
    for proyecto in lista_proyectos:
        nombre = proyecto.get("Nombre del Proyecto", "")
        descripcion = proyecto.get("Descripción", "")
        presupuesto = proyecto.get("Presupuesto", "")
        fecha_inicio = proyecto.get("Fecha de Inicio", "")
        fecha_fin = proyecto.get("Fecha de Fin", "")
        estado = proyecto.get("Estado", "")
        
        # Imprimiendo cada proyecto con el formato deseado
        print(f"| {nombre} | {descripcion} | {presupuesto} | {fecha_inicio} | {fecha_fin} | {estado} |\n")

    

    
    
    






            