from parseador_archivos import *
from funciones import *

corriendo = True
#guardo el parseo del csv en una variable
lista_proyectos = parse_csv(NOMBRE_ARCHIVO)
#convierto los datos a sus respectivos tipos
convertir_string_a_datos(lista_proyectos)
# este while imprime el menu de opciones
while(corriendo):
    opcion = int(input("MENU PRINCIPAL\n\n1)Ingresar un proyecto\n2)Modificar proyecto\n3)Cancelar un proyecto\n4)Comprobar proyectos\n5)Mostrar todos los proyectos\n6)Calcular presupuesto promedio\n7)Buscar proyecto por nombre\n8)Ordenar proyectos\n9)Retomar proyecto\n10)Reporte de proyectos por encima de un presupuesto\n11)Reporte de proyecto por nombre\n12)Salir\n13)Calcular el promedio de presupuesto de todos los proyectos cancelados en donde en su descripción tienen la palabra “Desarrollo” En caso de que no haya indicar error\n14)Realizar un top 3 de los proyectos activos con mayor presupuesto. Verificar qué haya la cantidad deseada de proyectos , sino indicar un mensaje de error.\n"))
    match opcion:
        case 1:
            crear_proyecto(lista_proyectos)
        case 2:
            proyecto_a_modificar = ingresar_id_a_modificar(lista_proyectos)
            modificar_proyecto(proyecto_a_modificar)
        case 3:
            cancelar_proyecto(lista_proyectos)
        case 4:
            comprobar_proyectos(lista_proyectos)
        case 5:
            mostrar_proyectos(lista_proyectos)
        case 6:
            calcular_promedio(lista_proyectos)
        case 7:
            nombre = pedir_nombre()
            lista_por_nombre = obtener_lista_por_nombre(lista_proyectos, nombre)
            mostrar_proyectos(lista_por_nombre)
        case 8:
            ordenar_lista(lista_proyectos)
        case 9:
            retomar_proyecto(lista_proyectos)
        case 10:
            generar_reporte_presupuesto(lista_proyectos)
        case 11:
            break
        case 12:
             convertir_datos_a_string(lista_proyectos)
             generar_csv(NOMBRE_ARCHIVO, lista_proyectos)
             crear_json_con_proyectos_finalizados(lista_proyectos)
             corriendo = False
        case 13:
           calcular_promedio_cancelados()
        case 14:
           calcular_top_3_activo()