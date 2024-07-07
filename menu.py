from parseador_archivos import *
from funciones import *

corriendo = True

# este while imprime el menu de opciones
while(corriendo):
    opcion = int(input("MENU PRINCIPAL\n\n1)Ingresar un proyecto \n2)Modificar proyecto \n3)Cancelar un proyecto \n4)Comprobar proyectos \n5)Mostrar todos los proyectos \n6)Calcular presupuesto promedio \n7)Buscar proyecto por nombre \n8)Ordenar proyectos \n9)Retomar proyecto \n10)Reporte de proyectos por encima de un presupuesto \n11)Reporte de proyecto por nombre \n12)Mostrar presupuesto promedio de proyectos finalizados durante la Copa Qatar 2022 \n13)Mostrar presupuesto promedio de proyectos que hayan durado más de 2 años \n14)Salir del programa\n"))
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
            break
        case 9:
            break
        case 10:
            break
        case 11:
            break
        case 12:
            break
        case 13:
            break
        case 14:
            corriendo = False