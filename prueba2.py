import numpy as np

# Crear un array de nombres de archivo
a = np.array(['elemento(10).jpg', 'elemento(11).jpg', 'elemento(1).jpg', 'elemento(2).jpg', 'elemento(3).jpg', 'elemento(4).jpg', 'elemento(5).jpg', 'elemento(6).jpg', 'elemento(7).jpg', 'elemento(8).jpgelemento(9).jpg'])

# Obtener los números entre paréntesis como enteros
numeros = np.array([int(x[x.find('(')+1:x.find(')')]) for x in a])

# Obtener los índices que ordenan los números
indices_ordenados = np.argsort(numeros)

# Ordenar el array de nombres de archivo según los índices
a_ordenado = a[indices_ordenados]

# Imprimir el array ordenado
print(a_ordenado)