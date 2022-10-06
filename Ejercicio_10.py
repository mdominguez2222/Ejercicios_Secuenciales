#10.Un alumno desea saber cual será su calificación final en la materia de Algoritmos. Dicha calificación se compone de los siguientes porcentajes:
#55% del promedio de sus tres calificaciones parciales.
#30% de la calificación del examen final.
#15% de la calificación de un trabajo final.

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



