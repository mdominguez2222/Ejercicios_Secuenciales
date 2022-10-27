#1.Escribir un programa que pregunte al usuario su nombre, y luego lo salude.

def ejer1():
    nombre = ""
    nombre = input("¿Cómo te llamas?: \n")
    print("Buenos días",nombre)
ejer1()







#2.Calcular el perímetro y área de un rectángulo dada su base y su altura.

def calculaArea(base:int, altura:int):

    return ((base*2)+(altura*2))


def calculaPerimetro(base:int, altura:int):
    return (base*altura)

        
       #Devuelvo una lista con [area,perimetro]

def calculaAreaYPerimetro(base:int, altura:int):

    vPerimetro = []
    
    vPerimetro.append(calculaArea(base,altura))
    vPerimetro.append(calculaPerimetro(base,altura))
    return vPerimetro

#Principal   

base = int(input("Dime el área: \n"))
altura = int(input("Dime la altura: \n"))

vNum = calculaAreaYPerimetro(base,altura)

print("El área es:", vNum[0])
print("El perímetro es:", vNum[1])







#3.Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.

def ejer3(cateto1:int, cateto2:int):
    from cmath import sqrt
    
    return sqrt(((cateto1*cateto1)+(cateto2*cateto2)))


#4.Dados dos números, mostrar la suma, resta, división y multiplicación de ambos.

def ejer4():
    
    numero1 = 0
    numero2 = 0

    numero1 = (int) (input ("Dime un número: \n"))
    numero2 = (int) (input ("Dime otro número: \n"))

    print ("La suma es:", (numero1+numero2))
    print ("La resta es:", (numero1-numero2))
    print ("La división es:", (numero1/numero2))
    print ("La multiplicación es:", (numero1*numero2))
ejer4()



#5.Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius.
#Recordar que la fórmula para la conversión es: C = (F-32)*5/9

def ejer5():
    grados = 0

    grados = (int) (input("¿Cuántos grados Fahrenheit quieres convertir?: \n"))

    print ("Es igual a:", ((grados-32)*5/9), "grados Celsius")
ejer5()



#6.Calcular la media de tres números pedidos por teclado.

def ejer6():
    num1 = 0
    num2 = 0
    num3 = 0

    num1 = int (input("Dime un número: \n"))
    num2 = int (input("Dime otro número: \n"))
    num3 = int (input("Dime otro número: \n"))

    print ("La media es:",((num1+num2+num3)/3))
ejer6()



#7.Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos corresponde.
#Por ejemplo: 1000 minutos son 16 horas y 40 minutos.

def ejer7():
    min = 0

    min = int (input("¿Cuántos minutos son?: \n"))

    print (f"Los {min} minutos son {int(min/60)} horas y {min%60} minutos")  
ejer7()



#8.Un vendedor recibe un sueldo base mas un 10% extra por comisión de sus ventas, el vendedor desea saber cuanto dinero obtendrá por concepto de
#comisiones por las tres ventas que realiza en el mes y el total que recibirá en el mes tomando en cuenta su sueldo base y comisiones.

def ejer8():
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
ejer8()



#9.Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuanto deberá pagar finalmente por su compra.

def ejer9():
    preciocompra = 0

    preciocompra = (int) (input("¿De cuánto ha sido su compra?: \n"))
    print (f"El total de su compra es de {(preciocompra*0.15)} €")
ejer9()



#10.Un alumno desea saber cual será su calificación final en la materia de Algoritmos. Dicha calificación se compone de los siguientes porcentajes:
#55% del promedio de sus tres calificaciones parciales.
#30% de la calificación del examen final.
#15% de la calificación de un trabajo final.

def ejer10():
    parcial1 = 0
    parcial2 = 0
    parcial3 = 0
    examen = 0
    trabajo = 0

    parcial1 = int(input("Calificación de su primer parcial: \n"))
    parcial2 = int(input("Calificación de su segundo parcial: \n"))
    parcial3 = int(input("Calificación de su tercer parcial: \n"))

    examen = int(input("Calificación de su examen final: \n"))

    trabajo = int(input("Calificación de su trabajo final: \n"))

    print (f"Su calificación final es {(((parcial1+parcial2+parcial3)/3)*0.55)+(examen*0.3)+(trabajo*0.15)}")
ejer10()



#20.Diseñar un algoritmo que nos diga el dinero que tenemos (en euros y céntimos) después de pedirnos cuantas monedas tenemos (de 2€, 1€, 50 céntimos, 20
#céntimos o 10 céntimos)

def ejer20():
    mon2 = 0
    mon1 = 0
    cent50 = 0
    cent2 = 0
    cent1 = 0

    mon2 = int (input("Monedas de 2€: \n"))
    mon1 = int (input("Monedas de 1€: \n"))
    cent50 = int(input("Monedas de 50 céntimos: \n"))
    cent2 = int(input("Monedas de 20 céntimos: \n"))
    cent1 = int(input("Monedas de 10 céntimos: \n"))

    print (f"Tienes {(mon2*2)+mon1} € y {(cent50*50)+(cent1*10)+(cent2*20)} céntimos")
ejer20()