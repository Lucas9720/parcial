from parseador_archivos import *
from funciones import *

corriendo = True

# este while imprime el menu de opciones
while(corriendo):
    opcion = int(input("MENU PRINCIPAL\n\n1)Ingresar un proyecto \n2)Modificar proyecto \n3)Eliminar un proyecto \n4)Comprobar proyectos \n5)Mostrar todos los proyectos \n6)Calcular presupuesto promedio \n7)Buscar proyecto por nombre \n8)Ordenar proyectos \n9)Retomar proyecto \n10)Reporte de proyectos por encima de un presupuesto \n11)Reporte de proyecto por nombre \n12)Mostrar presupuesto promedio de proyectos finalizados durante la Copa Qatar 2022 \n13)Mostrar presupuesto promedio de proyectos que hayan durado más de 2 años \n14)Salir del programa\n"))
    match opcion:
        case 1:
            crear_proyecto()
        case 2:
            break
        case 3:
            break
        case 4:
            break
        case 5:
            break
        case 6:
            break
        case 7:
            break
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