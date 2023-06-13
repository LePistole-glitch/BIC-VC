import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#CSV
data = pd.read_csv('ventas.csv')
#dt = np.loadtxt('ventas.csv', delimiter=",", dtype=str)

btotal = data['total_profit']
mes = data['month_number']
plt.title('Beneficio total por mes')
plt.plot(mes, btotal, linestyle=':', color='red', marker='o', markerfacecolor='black', markeredgecolor='red')
# Nombre ejes X - Y
plt.xlabel('Número de mes')
plt.ylabel('---- Beneficio total ----')
plt.xticks(np.arange(min(mes), max(mes)+1, 1.0))
plt.legend(['Beneficio total'], loc='lower right')

#show grafico
plt.show()