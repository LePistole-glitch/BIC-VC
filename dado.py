#ALUMNO: CHAVEZ ARIAS JESUS
#No.Control: 19141132
import random as rm
contador = 1

numberUno = rm.randint(1, 6)
numberDos = rm.randint(1, 6)
sumaNumeros = numberUno + numberDos
if sumaNumeros == 7 or sumaNumeros == 11:
    print("Ganaste!, obstuviste un: "+str(sumaNumeros))
elif sumaNumeros == 2 or sumaNumeros == 3 or sumaNumeros == 12:
    print("Perdiste!, obstuviste un: "+str(sumaNumeros))
else:
    print("Numero Punto "+str(sumaNumeros)+" !!!")
    numeroPunto = sumaNumeros
    while(True):
        numberUno = rm.randint(1, 6)
        numberDos = rm.randint(1, 6)
        sumaNumeros = numberUno + numberDos
        contador = contador + 1
        if sumaNumeros == numeroPunto:
            print("Ganaste!, obstuviste un: "+str(sumaNumeros)+" que es el Punto!")
            print("En un total de "+str(contador)+" de jugadas!")

            break
        elif sumaNumeros == 7:
            print("Perdiste!, obstuviste un: "+str(sumaNumeros)+" !")
            print("En un total de "+str(contador)+" de jugadas!")

            break


