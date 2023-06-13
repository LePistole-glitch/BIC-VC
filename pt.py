import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

data = pd.read_csv('mall_customers.csv')
X = data[['age', 'annual_income']]
y = data['spending_score']

#datos
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#árbol de decisión 
decision_tree = DecisionTreeRegressor(random_state=42)
decision_tree.fit(X_train, y_train)
y_pred = decision_tree.predict(X_test)

#(MSE)
mse = mean_squared_error(y_test, y_pred)
print("Error cuadrático medio:", mse)
plt.scatter(X_test['age'], y_test, color='b', label='Actual')
plt.scatter(X_test['age'], y_pred, color='r', label='Predicción')
plt.legend()
plt.show()
