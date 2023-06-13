import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#CSV
dt = pd.read_csv('ventas.csv')
#dt = np.loadtxt('ventas.csv', delimiter=",", dtype=str)
uProd = ['facecream', 'facewash', 'toothpaste', 'bathingsoap', 'shampoo', 'moisturizer']
mes = dt['month_number']

# Iterar sobre cada i y trazar la línea correspondiente
for i in uProd:
    uVendidas = dt[i]
    plt.plot(mes, uVendidas, marker='o', label=i.capitalize())

# Nombre ejes X - Y
plt.title('Unidades vendidas por mes')
plt.xlabel('Número de mes')
plt.ylabel('Unidades vendidas')
plt.xticks(np.arange(min(mes), max(mes)+1, 1.0))
plt.legend()

#Show grafico
plt.show()