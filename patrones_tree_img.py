#Mauricio Torres Díaz
#Usando tree desicion para encontrar patrones
#Examen 31-Mayo-2023

import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.tree import export_graphviz
import pydotplus
from IPython.display import Image

# Leer los datos desde el archivo CSV
data = pd.read_csv('mall_customers.csv')

# Seleccionar las características relevantes para el análisis de árboles de decisión
X = data[['age', 'annual_income']]
y = data['spending_score']

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear un modelo de árbol de decisión y ajustarlo a los datos de entrenamiento
decision_tree = DecisionTreeRegressor(random_state=42)
decision_tree.fit(X_train, y_train)

# Realizar predicciones en el conjunto de prueba
y_pred = decision_tree.predict(X_test)

# Calcular el error cuadrático medio (MSE)
mse = mean_squared_error(y_test, y_pred)
print("Error cuadrático medio (MSE):", mse)

# Generar el gráfico del árbol de decisión en formato DOT
dot_data = export_graphviz(decision_tree, out_file=None,
                           feature_names=X.columns,
                           filled=True, rounded=True,
                           special_characters=True)

# Crear el gráfico del árbol de decisión
graph = pydotplus.graph_from_dot_data(dot_data)

# Guardar el gráfico en formato PNG
graph.write_png('decision_tree.png')

# Mostrar el gráfico del árbol de decisión
Image(graph.create_png())
