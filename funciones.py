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

def perdir_nombre() -> str:
    # pido el nombre al usuario
    nombre = input("ingrese el nombre del proyecto: ")
    while not (validar_nombre(nombre)):
        nombre = input("por favor ingrese un nombre valido: ")
    return nombre

def pedir_descripcion() -> str:
    # pido la descripcion al usuario
    descripcion = input("ingrese la descripcion: ")
    while not (validar_descripcion(descripcion)):
        descripcion = input("por favor ingrese una descripcion valida: ")
    return descripcion

def pedir_presupuesto() -> str:
     # pido el presupuesto al usuario
    presupuesto = int(input("ingrese el presupuesto: "))
    while not (validar_presupuesto(presupuesto)):
        presupuesto = input("por favor ingrese el presupuesto: ")
    return presupuesto

def pedir_fecha_inicio() -> str:
    # pido la fecha de inicio y finalizacion 
    fecha_de_inicio = input("ingrese la fecha de inicio en formato: dd-mm-aaaa: ")
    while not (validar_fecha(fecha_de_inicio)):
        fecha_de_inicio = input("Por favor. ingrese la fecha de inicio en formato: dd-mm-aaaa: ")
    return fecha_de_inicio
    
def pedir_fecha_fin() -> str:
     #valido que la fecha de finalizacion este en el formato correcto y no sea anterior a la fecha de inicio
    fecha_de_finalizacion = input("ingrese la fecha de finalizacion en formato: dd-mm-aaaa: ")
    while not (validar_fecha(fecha_de_finalizacion) and validar_rango_fechas(fecha_de_inicio, fecha_de_finalizacion)):
        fecha_de_finalizacion = input("Por favor. ingrese la fecha de finalizacion en formato: dd-mm-aaaa y posterior a la fecha de inicio: ")    
    return fecha_de_finalizacion

def pedir_estado() -> str:
    ## pido estado al usuario
    estado_nuevo = input("Ingrese el nuevo estado del proyecto(Activo, Finalizado o Cancelado): ")
    while not validar_estado(estado_nuevo):
        estado_nuevo = input("Por favor, ingrese un estado válido: ")
    return estado_nuevo

def crear_proyecto(lista_proyecto: list):
    nombre = perdir_nombre()
    
    descripcion = pedir_descripcion()

    presupuesto = pedir_presupuesto()
    
    fecha_de_inicio = pedir_fecha_inicio()

    fecha_de_finalizacion = pedir_fecha_fin()

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

def ingresar_id_a_modificar(lista_proyecto: list):
    id = input("ingrese el id: ")
    
    # Buscar el diccionario que contiene el valor especificado en la clave "id"
    resultado = next((item for item in lista_proyectos if item["id"] == id), None)
    
    while(resultado is None):
        id = input("El id no existe, ingrese el id: ")
        resultado = next((item for item in lista_proyectos if item["id"] == id), None)
    
    return resultado

#se ingresa un proyecto a modifica por parametro
def modificar_proyecto(proyecto: Dict):
    columna_a_modificar = int(input("Ingrese la opcion a modificar\n1 para 'Nombre del Proyecto'\n2 para 'Descripción'\n3 para 'Fecha de inicio'\n4 para 'Fecha de Fin'\n5 para 'Presupuesto'\n6 para 'Estado': "))
    while columna_a_modificar < 1 or columna_a_modificar > 6:
        columna_a_modificar =  int(input("Por favor, Ingrese una opcion correcta a modificar\n1 para 'Nombre del Proyecto'\n2 para 'Descripción'\n3 para 'Fecha de inicio'\n4 para 'Fecha de Fin'\n5 para 'Presupuesto'\n6 para 'Estado': "))

    match columna_a_modificar:
        case 1: 
            nombre_nuevo = perdir_nombre()
            proyecto["Nombre del Proyecto"] = nombre_nuevo
        case 2:
            descripcion_nueva = pedir_descripcion()
            proyecto["Descripción"] = descripcion_nueva
        case 3:
            fecha_inicio_nueva = pedir_fecha_inicio()
            proyecto["Fecha de inicio"] = fecha_inicio_nueva
        case 4:
            fecha_fin_nueva = pedir_fecha_fin()
            proyecto["Fecha de Fin"] = fecha_fin_nueva
        case 5:
            presupuesto_nuevo = pedir_presupuesto()
            proyecto["Presupuesto"] = presupuesto_nuevo
        case 6:
            estado_nuevo = pedir_estado()
            proyecto["Estado"] = estado_nuevo

# le pide al usuario un id, y en caso de que exista, se le modifica el estado a cancelado                
def cancelar_proyecto(lista_proyectos: list):
    proyecto = ingresar_id_a_modificar(lista_proyectos)
    proyecto["Estado"] = "Cancelado"

# Cambiará el estado de todos los proyectos cuya fecha de finalización ya haya sucedido.
def comprobar_proyectos(lista_proyectos: list):
    global FORMATO
    #obtengo la fecha de hoy en formato 'dd-mm-aaaa'
    fecha_hoy = datetime.today()
    fecha_hoy_formateada = fecha_hoy.strftime(FORMATO)

    #Recorro toda la lista
    for proyecto in lista_proyectos:
        #busco algun proyecto donde la fecha sea menor a la fecha de hoy
        if not validar_rango_fechas(fecha_hoy_formateada,proyecto['Fecha de Fin']):
            proyecto['Estado'] = "Finalizado"
    print("proyectos comprobados exitosamente")

def mostrar_proyectos(lista_proyectos: list):
    # Cabecera de la tabla
    print("| id | Nombre del Proyecto | Descripción | Presupuesto | Fecha de Inicio | Fecha de Fin | Estado |\n")
    
    # Recorriendo la lista de proyectos y mostrando cada proyecto
    for proyecto in lista_proyectos:
        id = proyecto["id"]
        nombre = proyecto["Nombre del Proyecto"]
        descripcion = proyecto["Descripción"]
        presupuesto = proyecto["Presupuesto"]
        fecha_inicio = proyecto["Fecha de inicio"]
        fecha_fin = proyecto["Fecha de Fin"]
        estado = proyecto["Estado"]
        
        # en caso de que fecha inicio sea datetime, le paso el formato correcto
        if isinstance(fecha_inicio, datetime):
            fecha_inicio = fecha_inicio.strftime(FORMATO)

        print(f"| {id} | {nombre} | {descripcion} | {presupuesto} | {fecha_inicio} | {fecha_fin} | {estado} |\n")

def calcular_promedio(lista_proyectos: list):
    presupuesto_total = 0
    #recorro todos los proyectos y voy sumando sus presupuestos
    for proyecto in lista_proyectos:
       presupuesto = int(proyecto['Presupuesto'])
       presupuesto_total += presupuesto
    #para sacar el promedio calculo la suma de todos los presupuestos divido la cantidad de proyectos   
    resultado = presupuesto_total / len(lista_proyectos)
    print(f"el promedio presupuestario es: {int(resultado)}")

def ingresar_id_a_modificar(lista_proyectos: list):
    id = input("ingrese el id: ")
    
    # Buscar el diccionario que contiene el valor especificado en la clave "id"
    resultado = next((item for item in lista_proyectos if item["id"] == id), None)
    
    while(resultado is None):
        id = input("El id no existe, ingrese el id: ")
        resultado = next((item for item in lista_proyectos if item["id"] == id), None) 
    
    return resultado

def ingresar_nombre_a_buscar(lista_proyectos: list):
    nombre_a_buscar = input("ingrese el nombre a buscar: ")
    proyecto = next((item for item in lista_proyectos if item["Nombre del Proyecto"] == nombre_a_buscar), None)

    while (proyecto is None):
        nombre_a_buscar = input("El proyecto ingresado no existe. ingrese el nombre a buscar: ")
        proyecto = next((item for item in lista_proyectos if item["Nombre del Proyecto"] == nombre_a_buscar), None)

    # Cabecera de la tabla
    print("| Nombre del Proyecto | Descripción | Presupuesto | Fecha de Inicio | Fecha de Fin | Estado |\n")
    print(f"| {proyecto['Nombre del Proyecto']} | {proyecto['Descripción']} | {proyecto['Presupuesto']} | {proyecto['Fecha de inicio']} | {proyecto['Fecha de Fin']} | {proyecto['Estado']} |")


def convertir_datos(lista):
    global FORMATO
    for proyecto in lista:
        proyecto['Presupuesto'] = float(proyecto['Presupuesto'])
        proyecto['Fecha de inicio'] = datetime.strptime(proyecto['Fecha de inicio'], FORMATO)

def ordenar_lista(lista_proyectos: list):
    lista_ordenada = []
    
    key = int(input("ingresar una opcion para ordenar, 1 por Nombre, 2 por presupuesto, 3 por fecha de inicio: "))
    while not (key == 1 or key == 2 or key == 3):
         key = int(input("Por favor ingrese una opcion correcta, 1 por Nombre, 2 por presupuesto, 3 por fecha de inicio: "))

    forma_de_ordenamiento =  int(input("ingrese una opcion de que forma ordenar, 1 para ascendente, 2 para descendente: "))
    while not (forma_de_ordenamiento == 1 or forma_de_ordenamiento == 2):
         forma_de_ordenamiento = int(input("Por favor ingrese una opcion correcta, 1 para ascendente, 2 para descendente: "))

    # En caso de que sea true, se ordenara de forma descendente, y si es false de forma ascendente.
    forma_de_ordenamiento = (forma_de_ordenamiento == 2)

    #parseo los datos de la lista
    convertir_datos(lista_proyectos)

    match(key):
        case 1:
            lista_ordenada = sorted(lista_proyectos, key=lambda x: x['Nombre del Proyecto'], reverse=forma_de_ordenamiento)
        case 2:
            lista_ordenada = sorted(lista_proyectos, key=lambda x: x['Presupuesto'], reverse=forma_de_ordenamiento)
        case 3:
            lista_ordenada = sorted(lista_proyectos, key=lambda x: x['Fecha de inicio'], reverse=forma_de_ordenamiento)
    
    lista_proyectos = []
    lista_proyectos = lista_ordenada
    mostrar_proyectos()

def retomar_proyecto(lista_proyectos: list):
    lista_cancelados = []
    for proyecto in lista_proyectos:
        if proyecto["Estado"] == "Cancelado":
            lista_cancelados.append(proyecto)
    mostrar_proyectos(lista_cancelados)

    id_activar = input("ingrese el id a activar: ")
    proyecto_activar = next((item for item in lista_proyectos if item["id"] == id_activar), None) 
    proyecto_activar["Estado"] = "Activo"

def calcular_promedio_cancelados(lista_proyectos: list):
    lista_nueva = []
    palabra = "desarrollo"

    # Buscar la palabra en la cadena
    for proyecto in lista_proyectos:
        if palabra in proyecto['Descripción'].lower() and proyecto['Estado'] == 'Cancelado':
            lista_nueva.append(proyecto)
    lista_proyectos = []
    lista_proyectos = lista_nueva

    calcular_promedio()

def calcular_top_3_activo(lista_proyectos: list):
    bandera = True
    presupuesto_mas_alto = 0

    for proyecto in lista_proyectos:
        if proyecto['Estado'] == 'Activo':
            if int(proyecto['Presupuesto']) > presupuesto_mas_alto or bandera:
                bandera = False
                presupuesto_mas_alto = int(proyecto['Presupuesto'])

    print(f"el presupuesto mas alto es {presupuesto_mas_alto}")

def crear_json_con_proyectos_finalizados(lista_proyectos: list):
    lista_finalizados = []
    for proyecto in lista_proyectos:
        if proyecto["Estado"] == "Finalizado":
            lista_finalizados.append(proyecto)

    generar_json("ProyectosFinalizados.json", lista_finalizados)

# Función para generar el reporte
def generar_reporte(lista_proyectos: list):
    # Pedir al usuario que ingrese el presupuesto
    presupuesto = float(input("Ingrese el presupuesto mínimo para filtrar proyectos: "))
    
    # Filtrar proyectos que superen el presupuesto
    proyectos_filtrados = [proyecto for proyecto in lista_proyectos if proyecto["Presupuesto"] > presupuesto]
    
    # Obtener la fecha de solicitud del reporte
    fecha_solicitud = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Contar la cantidad de proyectos que coinciden con el criterio
    cantidad_proyectos = len(proyectos_filtrados)
    
    # Generar el contenido del reporte
    contenido_reporte = f"Fecha de solicitud: {fecha_solicitud}\n"
    contenido_reporte += f"Número de reporte: {generar_numero_reporte()}\n"
    contenido_reporte += f"Cantidad de proyectos que superan el presupuesto de {presupuesto}: {cantidad_proyectos}\n"
    contenido_reporte += "Listado de proyectos:\n"
    
    for proyecto in proyectos_filtrados:
        contenido_reporte += f"- {proyecto}\n" 
    
    # Guardar el reporte en un archivo de texto
    guardar_reporte(contenido_reporte)

# Función para generar un número de reporte único
def generar_numero_reporte():
    # Implementación de generación de número de reporte (puedes ajustar según tus necesidades)
    # Por ejemplo, podría ser un número secuencial o basado en la fecha/hora actual
    return 1  # Aquí podrías implementar la lógica para generar un número único

# Función para guardar el reporte en un archivo de texto
def guardar_reporte(contenido):
    nombre_archivo = f"reporte_{generar_numero_reporte()}.txt"
    with open(nombre_archivo, 'w') as archivo:
        archivo.write(contenido)


            