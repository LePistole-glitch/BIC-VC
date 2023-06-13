import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#Lectura del archivo
dt = pd.read_csv('ventas.csv')
#dt = np.loadtxt('ventas.csv', delimiter=",", dtype=str)

btotal = dt['total_profit']
mes = dt['month_number']
plt.title('Beneficio por mes')
plt.plot(mes, btotal)

# Nombre ejes X - Y
plt.xlabel('Mes')
plt.ylabel('---- Beneficio total ----')
plt.xticks(np.arange(min(mes), max(mes)+1, 1.0))
plt.show()