ventas=[]
pago= ("efectivo" ,"credito" ,"debito","transferencia")
import csv
def registrar_venta():
    precio_total=0
    nombre_producto = nombre()
    cantidad=canridad()
    valor_uni= valor_unitario()
    forma_pago=forma_de_pago()
    precio_total= cantidad * valor_uni
    venta=[nombre_producto,cantidad,valor_uni,pago[forma_pago-1],precio_total]
    ventas.append(venta)
    print(f"su total es:",precio_total)

def reporte_ventas():
    print("\nREPORTE DE VENTAS")
    
    for lulo in ventas:
        print(f"nombre: {lulo[0]}, cantidad: {lulo[1]}, valor unitario: {lulo[2]}, forma pago: {lulo[3]}, total: {lulo[4]}")

def csv_ventas():
    with open("archivo_csv", mode='w', newline='') as archivo:
        escritor_csv = csv.writer(archivo)
        escritor_csv.writerow(["Producto", "\tCantidad vendida","\tMonto vendido"])
        for lulo in ventas:
            escritor_csv.writerow([lulo[0], "\t""\t""\t""\t" ,lulo[1], "\t""\t""\t""\t""\t",lulo[4]])

def reporte_csv():
    with open("reporte_csv", mode='w', newline='') as archivos:
        escritor_csv = csv.writer(archivos)
        escritor_csv.writerow(["forma de pago", "\tCantidad vendida","\tMonto vendido"])
        for lulo in ventas:
            escritor_csv.writerow([lulo[4], "\t""\t""\t""\t" ,lulo[1], "\t""\t""\t""\t""\t",lulo[3]])

#validacion
def nombre():
    while True:
        nombre=input("ingresa nombre del producto: ")
        if len(nombre.strip())>=3 and nombre.isalpha:
            return nombre
        else:
            print("el nombre del producto debe tener almenos 3 letras")

def canridad():
    while True:
        try:
            cantidad = int(input("ingrese cantidad de producto: "))
            if cantidad>=1 and cantidad<=10:
                return cantidad
            else:
                print("no puedes llevar mas de 10 o menos de 1 producto")
        except:
            print("ingrese numeros enteros porfavor")

def valor_unitario():
    while True:
        try:
            unitario = int(input("ingrese valor unitario del producto: "))
            if unitario>=590 and unitario<=20000:
                return unitario
            else:
                print("el precio del producto no puede ser menor a 590 o superios a 20000")
        except:
            print("ingrese numeros enteros sin punto o coma")

def forma_de_pago():
    while True:
        try:
            forma_pago = int(input("forma de pago 1.efectivo 2.credito 3.debito 4.transferencia"))
            if forma_pago in(1,2,3,4):
                return forma_pago
            else:
                print("ingrese un numero del 1 al 4")
        except:
            print("ingrese un numero entero")


