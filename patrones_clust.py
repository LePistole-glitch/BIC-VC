import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Leer los datos desde el archivo CSV
data = pd.read_csv('mall_customers.csv')

# Seleccionar las características relevantes para el análisis de clustering
X = data[['age', 'annual_income', 'spending_score']]

# Determinar el número óptimo de clusters utilizando el método del codo
inertia = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X)
    inertia.append(kmeans.inertia_)

# Graficar la curva de codo
plt.plot(range(1, 11), inertia, marker='o')
plt.xlabel('Número de clusters')
plt.ylabel('Inercia')
plt.title('Método del codo')
plt.show()

# Utilizar el número óptimo de clusters para realizar el clustering
kmeans = KMeans(n_clusters=5, random_state=42)
kmeans.fit(X)

# Agregar la etiqueta de cluster a los datos
data['cluster'] = kmeans.labels_

# Imprimir los resultados del clustering
print(data[['customer_id', 'age', 'annual_income', 'spending_score', 'cluster']])
