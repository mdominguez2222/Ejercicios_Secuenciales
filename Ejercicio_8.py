#Un vendedor recibe un sueldo base mas un 10% extra por comisión de sus ventas, el vendedor desea saber cuanto dinero obtendrá por concepto de
#comisiones por las tres ventas que realiza en el mes y el total que recibirá en el mes tomando en cuenta su sueldo base y comisiones.

sueldo = 0
venta1 = 0
venta2 = 0
venta3 = 0

venta1 = int (input("¿Cuánto vale la primera venta?: \n"))
venta2 = int (input("¿Cuánto vale la segunda venta?: \n"))
venta3 = int (input("¿Cuánto vale la tercera venta?: \n"))

print (f"La comisión de ventas es de {(venta1+venta2+venta3)*1.1} €")

sueldo = int (input ("¿De cuánto es el sueldo?: \n"))

print (f"En total recibirá {((venta1+venta2+venta3)*1.1)+sueldo} €")
