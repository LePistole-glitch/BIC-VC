n = int(input("Ingresa un Numero"))
impar = 1
suma = ""
resultado = 0
i = 1

while(i<n+1):
    for x in range(i):
        resultado = resultado + impar
        suma = suma + " + " + str(impar) 
        impar = impar+2
        
    print(str(i) + "^3 = " + suma + " = " + str(resultado))
    suma = ""
    i = i+1
    resultado = 0