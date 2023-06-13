#Osvaldo Pérez Ochoa
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

# Cargar los datos
data = pd.read_csv('C:\\Periodo Enero-Junio 2023\\CIENCIA DE DATOS\\Programas\\Matplotlib\\mall_customers.csv')

# Seleccionar características relevantes para clasificación y predicción
X = data[['age', 'annual_income', 'spending_score']].values
y = data['gender'].values

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear el clasificador de Árbol de Decisión con control de la profundidad
max_depth = 3  # Profundidad máxima del árbol
clf = DecisionTreeClassifier(max_depth=max_depth)

# Entrenar el clasificador
clf.fit(X_train, y_train)

# Realizar predicciones en los datos de prueba
y_pred = clf.predict(X_test)

# Calcular la precisión de clasificación
accuracy = accuracy_score(y_test, y_pred)
print('Precisión de clasificación:', accuracy)

# Crear nuevos datos para hacer predicciones
new_data = [[64, 19, 3], [40, 30, 20], [35, 15, 90]]

# Realizar predicciones en los nuevos datos
new_predictions = clf.predict(new_data)

# Imprimir las predicciones
print('Predicciones para los nuevos datos:', new_predictions)

# Visualizar el árbol de decisión
plt.figure(figsize=(10, 6))
plot_tree(clf, feature_names=['age', 'annual_income', 'spending_score'], class_names=['Female', 'Male'], filled=True)
plt.title('Árbol de Decisión (Profundidad: {})'.format(max_depth))
plt.show()