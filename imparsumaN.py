n = int(input("Ingresa un numero N: "))

primero = 1
var = 1

for i in range(1, n+1):
    print(str(i)+"^"+str(3)+" = ")

    for x in range(primero, i+1):
        if x%2!=0:
            print("+"+str(x))
            primero = x
    var = var + 1

