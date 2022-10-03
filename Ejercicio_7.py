#7.Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos corresponde.
#Por ejemplo: 1000 minutos son 16 horas y 40 minutos.

min = 0

min = int (input("¿Cuántos minutos son?: \n"))

print (f"Los {min} minutos son {int(min/60)} horas y {min%60} minutos")   #Con los corchetes podemos meter las operaciones sin cerrar comillas
 #con el int, evitamos los decimales en las horas
 #con % ponemos el resto de decimales

