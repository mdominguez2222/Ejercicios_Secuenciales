#20.Diseñar un algoritmo que nos diga el dinero que tenemos (en euros y céntimos) después de pedirnos cuantas monedas tenemos (de 2€, 1€, 50 céntimos, 20
#céntimos o 10 céntimos).

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