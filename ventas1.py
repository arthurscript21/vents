
from funciones_ventas import *

while True:
    print("registrar venta")
    print("ver ventas")
    print("ver ventas en csv")
    print("nocreporte en csv")
    print("salir")
    opt=int(input("ingrese una opcion: "))
    if opt == 1:
        registrar_venta()
    elif opt == 2:
        reporte_ventas()
    elif opt == 3:
        csv_ventas()
    elif opt == 4:
        reporte_csv()
    elif opt == 5:
        pass
