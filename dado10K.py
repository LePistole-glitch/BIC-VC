import numpy as np
import matplotlib.pyplot as plt


listaDados = []
numberUno = 0
media = 0

for i in range(10000):
    numberUno = np.random.randint(1, 6)
    listaDados.append(numberUno)

for i in listaDados:
    media = media + listaDados[i]

media = media/len(listaDados)
desvEstandar = np.std(listaDados)
print("Media: ", media)
print("desv: ", desvEstandar)

plt.hist(listaDados, color="red")
plt.show()

