#Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.

from cmath import sqrt

cateto1 = 0
cateto2 = 0


cateto1 = (int) (input("¿Cuál es el cateto A?: \n"))
cateto2 = (int) (input("¿Cuál es el cateto B?: \n"))

print ("La hipotenusa es ",sqrt(((cateto1*cateto1)+(cateto2*cateto2))))