import numpy as np
import string

def genContra(longitud):
    pwd = ""   
    
    #Creacion de listas con chr 
    listaLetra = np.array(list(string.ascii_lowercase))   
    listaUpper = np.array(list(string.ascii_uppercase))
    listaNumer = np.array(['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'])
    listaEspec = np.array(['ñ', ' ', chr(33), chr(34), chr(35), chr(36), chr(37), chr(38), chr(39), chr(40), chr(41), chr(42), chr(43), chr(44), chr(45), chr(46), chr(47), chr(58), chr(59), chr(60), chr(61), chr(62), chr(63), chr(64), chr(91), chr(92), chr(93), chr(94), chr(95), chr(96), chr(123), chr(124), chr(125), chr(126)])

    for i in range(longitud):
        #Seleccion entre cada iteracion una lista con num random 
        #y concatenarla a la cadena
        numArray = np.random.randint(0, 101)
        if numArray > 0 and numArray <= 25:
            index = np.random.randint(0, len(listaLetra)-1)
            pwd = pwd + str(listaLetra[index])
        elif numArray > 25 and numArray <= 50:
            index = np.random.randint(0, len(listaUpper)-1)
            pwd = pwd + str(listaUpper[index])
        elif numArray > 50 and numArray <= 75:
            index = np.random.randint(0, len(listaNumer)-1)
            pwd = pwd + str(listaNumer[index])
        else:
            index = np.random.randint(0, len(listaEspec)-1)
            pwd = pwd + str(listaEspec[index])
    return pwd

if __name__ == "__main__":
    long = int(input("Ingresa el tamanio del password a generar: "))
    print(genContra(long))

