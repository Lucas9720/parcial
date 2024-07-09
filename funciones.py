#Alumno: Lucas Gabriel Nuñez
#dni: 40129239
#division: 314

from datetime import datetime
from parseador_archivos import *
from typing import Dict

NOMBRE_ARCHIVO = "Proyectos.csv"
FORMATO = "%d-%m-%Y"
id_autoincremental = 0
#guardo el parseo del csv en una variable
lista_proyectos = parse_csv(NOMBRE_ARCHIVO)

def convertir_a_flotante(cadena):
    # Eliminar el símbolo '$' y las comas ','
    cadena_limpia = cadena.replace('$', '').replace(',', '').replace('"', '')
    # Convertir la cadena limpia a flotante
    return float(cadena_limpia)

def convertir_string_a_datos(lista_proyectos: list):
    global FORMATO
    for proyecto in lista_proyectos:
        proyecto['Fecha de inicio'] = datetime.strptime(proyecto['Fecha de inicio'], FORMATO)
        proyecto['Presupuesto'] = convertir_a_flotante(proyecto['Presupuesto'])

def convertir_datos_a_string(lista_proyectos: list):
    global FORMATO
    for proyecto in lista_proyectos:
        fecha_inicio = proyecto['Fecha de inicio'].strftime(FORMATO)
        proyecto['Fecha de inicio'] = str(fecha_inicio)
        presupuesto= proyecto['Presupuesto']
        # convierto el presupuesto a string agrandole el signo pesos y las comas
        proyecto['Presupuesto'] = f"${presupuesto:,.2f}"


def validar_presupuesto(presupuesto: float) -> bool:
    # Verificar que el presupuesto sea un valor numérico entero no menor a $500000
    if isinstance(presupuesto, float) and presupuesto >= 500000:
        return True
    else:
        return False
    
def validar_texto(texto: str, limite: int) -> bool:
    # Verificar que la descripción no exceda los 200 caracteres
    if len(texto) > limite:
        return False

    # Verificar que la descripción solo contenga caracteres alfanuméricos y espacios
    for char in texto:
        if not (char.isalnum() or char.isspace()):
            return False

    return True

#valida que la fecha este en el formato correcto
def validar_fecha(fecha: str) -> bool:
    global FORMATO
    
    try:
        # Convertir las cadenas de texto en objetos de fecha
        datetime.strptime(fecha, FORMATO)

        return True
    except ValueError:
        # Si hay un error en la conversión de la fecha, no es una fecha válida
        return False

def validar_rango_fechas(fecha_inicio: datetime, fecha_finalizacion: str) -> bool:
    global FORMATO
    
    finalizacion = datetime.strptime(fecha_finalizacion, FORMATO)
    
    # Verificar que la fecha de finalización no sea anterior a la fecha de inicio
    return finalizacion >= fecha_inicio

#valida si el estado ingresado por parametro es Activo, Cancelado o Finalizado, en caso de que no, retorna false
def validar_estado(estado: str):
   #valida que el usuario no ingrese otro estado que no este disponible
   return estado == "Activo" or estado == "Cancelado" or estado ==  "Finalizado"

def pedir_nombre() -> str:
    # pido el nombre al usuario
    nombre = input("ingrese el nombre del proyecto: ")
    while (not validar_texto(nombre, 30)): #si el usuario ingresa un nombre de mas de 30 caracteres, se le pedira de nuevo
        nombre = input("por favor ingrese un nombre valido: ")
    return nombre

def pedir_descripcion() -> str:
    # pido la descripcion al usuario
    descripcion = input("ingrese la descripcion: ")
    while (not validar_texto(descripcion, 200)): #si el usuario ingresa una descripcion mayor a 200 caracteres, se le pedira de nuevo 
        descripcion = input("por favor ingrese una descripcion valida: ")
    return descripcion

def pedir_presupuesto() -> float:
     # pido el presupuesto al usuario
    presupuesto = float(input("ingrese el presupuesto: "))
    while (not validar_presupuesto(presupuesto)): #  # Verificar que el presupuesto sea un valor numérico entero no menor a $500000
        presupuesto = float(input("por favor ingrese el presupuesto: "))
    return float(presupuesto)

def pedir_fecha_inicio() -> datetime:
    # pido la fecha de inicio y finalizacion 
    fecha_de_inicio = input("ingrese la fecha de inicio en formato: dd-mm-aaaa: ")
    while not (validar_fecha(fecha_de_inicio)): #si el usuario no ingresa una fecha en formato dd-mm-aaaa se le pide de nuevo
        fecha_de_inicio = input("Por favor. ingrese la fecha de inicio en formato: dd-mm-aaaa: ")
    return  datetime.strptime(fecha_de_inicio, FORMATO)
    
def pedir_fecha_fin(fecha_inicio: datetime) -> datetime:
     #valido que la fecha de finalizacion este en el formato correcto y no sea anterior a la fecha de inicio
    fecha_de_finalizacion = input("ingrese la fecha de finalizacion en formato: dd-mm-aaaa: ")
    while not (validar_fecha(fecha_de_finalizacion) and validar_rango_fechas(fecha_inicio, fecha_de_finalizacion)): 
        fecha_de_finalizacion = input("Por favor. ingrese la fecha de finalizacion en formato: dd-mm-aaaa y posterior a la fecha de inicio: ")    
    return datetime.strptime(fecha_de_finalizacion, FORMATO)

def pedir_estado() -> str:
    ## pido estado al usuario
    estado_nuevo = input("Ingrese el nuevo estado del proyecto(Activo, Finalizado o Cancelado): ")
    while not validar_estado(estado_nuevo):
        estado_nuevo = input("Por favor, ingrese un estado válido: ")
    return estado_nuevo

def crear_proyecto(lista_proyectos: list):
    nombre = pedir_nombre()
    
    descripcion = pedir_descripcion()

    presupuesto = pedir_presupuesto()
    
    fecha_de_inicio = pedir_fecha_inicio()

    fecha_de_finalizacion = pedir_fecha_fin(fecha_de_inicio)

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

def ingresar_id_a_modificar(lista_proyectos: list):
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
            nombre_nuevo = pedir_nombre()
            proyecto["Nombre del Proyecto"] = nombre_nuevo
        case 2:
            descripcion_nueva = pedir_descripcion()
            proyecto["Descripción"] = descripcion_nueva
        case 3:
            fecha_inicio_nueva = pedir_fecha_inicio()
            proyecto["Fecha de inicio"] = fecha_inicio_nueva
        case 4:
            fecha_fin_nueva = pedir_fecha_fin(proyecto["Fecha de inicio"])
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
    fecha_hoy_str = fecha_hoy.strftime("%d-%m-%Y")
    fecha_hoy_formateada = datetime.strptime(fecha_hoy_str, FORMATO)

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

        print(f"| {id} | {nombre} | {descripcion} | ${presupuesto:,.2f} | {fecha_inicio} | {fecha_fin} | {estado} |\n")

def calcular_promedio(lista_proyectos: list):
    presupuesto_total = 0
    #recorro todos los proyectos y voy sumando sus presupuestos
    for proyecto in lista_proyectos:
       presupuesto = proyecto['Presupuesto']
       presupuesto_total += presupuesto
    #para sacar el promedio calculo la suma de todos los presupuestos divido la cantidad de proyectos   
    resultado = presupuesto_total / len(lista_proyectos)
    print(f"el promedio presupuestario es: ${resultado:,.2f}")

def ingresar_id_a_modificar(lista_proyectos: list):
    id = input("ingrese el id: ")
    
    # Buscar el diccionario que contiene el valor especificado en la clave "id"
    resultado = next((item for item in lista_proyectos if item["id"] == id), None)
    
    while(resultado is None):
        id = input("El id no existe, ingrese el id: ")
        resultado = next((item for item in lista_proyectos if item["id"] == id), None) 
    
    return resultado

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
    
    match(key):
        #La función lambda es una función anónima que toma un argumento x (donde x es un diccionario en lista_proyectos) y devuelve el valor asociado a la clave 'Nombre del Proyecto'
        case 1:
            lista_ordenada = sorted(lista_proyectos, key=lambda x: x['Nombre del Proyecto'], reverse=forma_de_ordenamiento)
        case 2:
            lista_ordenada = sorted(lista_proyectos, key=lambda x: x['Presupuesto'], reverse=forma_de_ordenamiento)
        case 3:
            lista_ordenada = sorted(lista_proyectos, key=lambda x: x['Fecha de inicio'], reverse=forma_de_ordenamiento)
    
    lista_proyectos = []
    lista_proyectos = lista_ordenada
    mostrar_proyectos(lista_proyectos)

def retomar_proyecto(lista_proyectos: list):
    lista_cancelados = []
    #obtengo la fecha de hoy
    fecha_hoy = datetime.today()
    #paso a string la fecha de hoy
    fecha_hoy_str = fecha_hoy.strftime("%d-%m-%Y")
    #la formateo en formato "dd-mm-aaaa"
    fecha_hoy_formateada = datetime.strptime(fecha_hoy_str, FORMATO)

    #busco en la lista los proyectos que esten en estado cancelado y verifico que la fecha dd finalizacion no haya pasado
    for proyecto in lista_proyectos:
        if proyecto["Estado"] == "Cancelado" and validar_rango_fechas(fecha_hoy_formateada, proyecto["Fecha de Fin"]):
            lista_cancelados.append(proyecto)
    mostrar_proyectos(lista_cancelados)

    #le pido al usuario el id
    id_activar = input("ingrese el id a activar: ")
    proyecto_activar = next((item for item in lista_cancelados if item["id"] == id_activar), None) 
    while(not proyecto_activar): # si el usuario ingreso un id no existente, se lo pide de nuevo
        id_activar = input("ingrese un id a activar que figure en la lista: ")
        proyecto_activar = next((item for item in lista_cancelados if item["id"] == id_activar), None)
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

    calcular_promedio(lista_proyectos)

def calcular_top_3_activo(lista_proyectos: list):
    lista_top_3 = []

    #Obtengo los mejores presupuestos
    lista_top = sorted(lista_proyectos, key=lambda x: x['Presupuesto'], reverse=True)

    #aplico el filtro de estado activo
    for proyecto in lista_top:
      if proyecto["Estado"] == "Activo":
          lista_top_3.append(proyecto)


    mostrar_proyectos(lista_top_3)

def crear_json_con_proyectos_finalizados(lista_proyectos: list):
    lista_finalizados = []
    for proyecto in lista_proyectos:
        if proyecto["Estado"] == "Finalizado": #busca un proyecto con estado finalizado y lo guarda
            lista_finalizados.append(proyecto)

    generar_json("ProyectosFinalizados.json", lista_finalizados)

def obtener_proyectos_presupuesto(lista_proyectos: list, presupuesto: float):
    lista_proyectos_superan_presupuesto = []
    for proyecto in lista_proyectos:
        if float(proyecto["Presupuesto"]) > presupuesto:
            lista_proyectos_superan_presupuesto.append(proyecto)
    
    return lista_proyectos_superan_presupuesto


# Función para generar el reporte con presupuesto
def generar_reporte_presupuesto(lista_proyectos: list):
    # Pedir al usuario que ingrese el presupuesto
    presupuesto = float(input("Ingrese el presupuesto mínimo para filtrar proyectos: "))
    
    # Filtrar proyectos que superen el presupuesto
    proyectos_filtrados = obtener_proyectos_presupuesto(lista_proyectos, presupuesto)
    
    # Obtener la fecha de solicitud del reporte
    fecha_solicitud = datetime.today().strftime(FORMATO)
    
    # Contar la cantidad de proyectos que coinciden con el criterio
    cantidad_proyectos = len(proyectos_filtrados)
    
    # Generar el contenido del reporte
    contenido_reporte = f"Fecha de solicitud: {fecha_solicitud}\n"

    # guardo la cantidad de reportes
    numero_reporte = obtener_num_reporte()
    contenido_reporte += f"Número de reporte: {numero_reporte + 1}\n"

    contenido_reporte += f"Cantidad de proyectos que superan el presupuesto de {presupuesto}: {cantidad_proyectos}\n"
    contenido_reporte += "Listado de proyectos:\n"

    contenido_reporte += "| id | Nombre del Proyecto | Descripción | Presupuesto | Fecha de Inicio | Fecha de Fin | Estado |\n"
    
    for proyecto in proyectos_filtrados:
        id = proyecto["id"]
        nombre = proyecto["Nombre del Proyecto"]
        descripcion = proyecto["Descripción"]
        actual_presupuesto = proyecto["Presupuesto"]
        fecha_inicio = proyecto["Fecha de inicio"]
        fecha_fin = proyecto["Fecha de Fin"]
        estado = proyecto["Estado"]
        contenido_reporte += f"| {id} | {nombre} | {descripcion} | ${actual_presupuesto:,.2f} | {fecha_inicio} | {fecha_fin} | {estado} |\n"
    
    # Guardar el reporte en un archivo de texto
    guardar_reporte(contenido_reporte)

def guardar_numero_reporte(reporte_num: int):
    lista =[{"numeroDeReporte" : reporte_num}]
    generar_json("contadorReportes.json",lista)

def obtener_num_reporte() -> int:
    num_reporte_actual = 0
    lista = parsear_json("contadorReportes.json")
    if lista:
        num_reporte_actual = lista[0]["numeroDeReporte"]
    return num_reporte_actual

# Función para guardar el reporte en un archivo de texto
def guardar_reporte(contenido):
    numero_reporte = obtener_num_reporte() + 1
    nombre_archivo = f"reporte{numero_reporte}.txt"
    with open(nombre_archivo, 'w') as archivo:
        archivo.write(contenido)
    guardar_numero_reporte(numero_reporte)

def generar_reporte_nombre(lista_proyectos: list):
    nombre = pedir_nombre()

    # obtengo una lista de proyectos con el nombre que ingreso el usuario
    proyectos_filtrados = obtener_lista_por_nombre(lista_proyectos, nombre)

        # Obtener la fecha de solicitud del reporte
    fecha_solicitud = datetime.today().strftime(FORMATO)
    
    # Contar la cantidad de proyectos que coinciden con el criterio
    cantidad_proyectos = len(proyectos_filtrados)
    
    # Generar el contenido del reporte
    contenido_reporte = f"Fecha de solicitud: {fecha_solicitud}\n"

    # guardo la cantidad de reportes
    numero_reporte = obtener_num_reporte()
    contenido_reporte += f"Número de reporte: {numero_reporte + 1}\n"

    contenido_reporte += f"Cantidad de proyectos que tienen el nombre {nombre}: {cantidad_proyectos}\n"
    contenido_reporte += "Listado de proyectos:\n"

    contenido_reporte += "| id | Nombre del Proyecto | Descripción | Presupuesto | Fecha de Inicio | Fecha de Fin | Estado |\n"
    for proyecto in proyectos_filtrados:
        id = proyecto["id"]
        nombre = proyecto["Nombre del Proyecto"]
        descripcion = proyecto["Descripción"]
        presupuesto = proyecto["Presupuesto"]
        fecha_inicio = proyecto["Fecha de inicio"]
        fecha_fin = proyecto["Fecha de Fin"]
        estado = proyecto["Estado"]
        contenido_reporte += f"| {id} | {nombre} | {descripcion} | ${presupuesto:,.2f} | {fecha_inicio} | {fecha_fin} | {estado} |\n"
    
    # Guardar el reporte en un archivo de texto
    guardar_reporte(contenido_reporte)



def obtener_lista_por_nombre(lista_proyectos: list, nombre: str):
    lista_presupuestos_nombre = []

    for proyecto in lista_proyectos:
       if proyecto['Nombre del Proyecto'] == nombre:
           lista_presupuestos_nombre.append(proyecto)
    return lista_presupuestos_nombre