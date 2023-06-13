import numpy as np
import matplotlib.pyplot as plt

listaDados = []
listaDadosDos = []

media = 0
mediaDos = 0

for i in range(10000):
    listaDados.append(np.random.randint(1, 7))
    listaDadosDos.append(np.random.randint(1, 7))

for i in range(10000):
    media = media + listaDados[i]
    mediaDos = mediaDos + listaDadosDos[i]


media = media/10000
mediaDos = mediaDos/10000
desvEstandar = np.std(listaDados)
desvEstandarDos = np.std(listaDadosDos)

print("Media: ", media)
print("desv: ", desvEstandar)

print("Media Dado Dos: ", mediaDos)
print("desv  Dado Dos: ", desvEstandarDos)


plt.hist(listaDados , bins=range(1, 8), align='left', rwidth=0.5, color="red")
plt.hist(listaDadosDos, bins=range(1, 8), align='left', rwidth=0.5, color="green")

plt.show()