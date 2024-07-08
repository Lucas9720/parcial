from parseador_archivos import *
from funciones import *

corriendo = True

# este while imprime el menu de opciones
while(corriendo):
    opcion = int(input("MENU PRINCIPAL\n\n1)Ingresar un proyecto\n2)Modificar proyecto\n3)Cancelar un proyecto\n4)Comprobar proyectos\n5)Mostrar todos los proyectos\n6)Calcular presupuesto promedio\n7)Buscar proyecto por nombre\n8)Ordenar proyectos\n9)Retomar proyecto\n10)Reporte de proyectos por encima de un presupuesto\n11)Reporte de proyecto por nombre\n12)Salir\n13)Calcular el promedio de presupuesto de todos los proyectos cancelados en donde en su descripción tienen la palabra “Desarrollo” En caso de que no haya indicar error\n14)Realizar un top 3 de los proyectos activos con mayor presupuesto. Verificar qué haya la cantidad deseada de proyectos , sino indicar un mensaje de error.\n"))
    match opcion:
        case 1:
            crear_proyecto()
        case 2:
            proyecto_a_modificar = ingresar_id_a_modificar()
            modificar_proyecto(proyecto_a_modificar)
        case 3:
            cancelar_proyecto()
        case 4:
            comprobar_proyectos()
        case 5:
            mostrar_proyectos()
        case 6:
            calcular_promedio()
        case 7:
            ingresar_nombre_a_buscar()
        case 8:
            ordenar_lista()
        case 9:
            retomar_proyecto()
        case 10:
            break
        case 11:
            break
        case 12:
             corriendo = False
        case 13:
           calcular_promedio_cancelados()
        case 14:
           calcular_top_3_activo()