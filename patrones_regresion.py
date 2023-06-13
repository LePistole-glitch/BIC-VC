import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Leer los datos desde el archivo CSV
data = pd.read_csv('mall_customers.csv')

# Seleccionar las características relevantes para el análisis de regresión
X = data[['age', 'annual_income']]
y = data['spending_score']

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear un modelo de regresión lineal y ajustarlo a los datos de entrenamiento
regression_model = LinearRegression()
regression_model.fit(X_train, y_train)

# Realizar predicciones en el conjunto de prueba
y_pred = regression_model.predict(X_test)

# Calcular el error cuadrático medio (MSE)
mse = mean_squared_error(y_test, y_pred)
print("Error cuadrático medio (MSE):", mse)

# Visualizar los resultados
plt.scatter(X_test['age'], y_test, color='b', label='Actual')
plt.scatter(X_test['age'], y_pred, color='r', label='Predicción')
plt.xlabel('Edad')
plt.ylabel('Puntaje de gasto')
plt.legend()
plt.show()
