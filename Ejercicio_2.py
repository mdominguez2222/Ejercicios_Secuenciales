#2.Calcular el perímetro y área de un rectángulo dada su base y su altura.

base = 0
altura = 0

base = (int) (input("¿Cuál es la base?: \n"))
altura = (int) (input("¿Cuál es la altura?: \n"))

print ("El perímetro es:", ((base*2)+(altura*2)))
print ("El área es:", (base*altura))