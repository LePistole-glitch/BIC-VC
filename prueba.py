# Un programa de Python para demostrar las operaciones del árbol KD
import math
import sys

# Número de dimensiones
k = 2
#contador de iteraciones!
cont = 1
#Lista con el ListHoja Hoja!
ListHoja = []
# Una estructura para representar un nodo del árbol kd
class Node:
    def __init__(self, point):
        self.point = point
        self.left = None
        self.right = None

# Un método para crear un nodo del árbol KD
def newNode(point):
    return Node(point)

# Inserta un nuevo nodo y devuelve la raíz del árbol modificado
# El parámetro depth se utiliza para decidir el eje de comparación
def insertRec(root, point, depth):
    # ¿El árbol está vacío?
    if not root:
        return newNode(point)

    # Calcula la dimensión actual (cd) de la comparación
    cd = depth % k

    # Compara el nuevo punto con la raíz en la dimensión actual 'cd'
    # y decide el subárbol izquierdo o derecho
    if point[cd] < root.point[cd]:
        root.left = insertRec(root.left, point, depth + 1)
    else:
        root.right = insertRec(root.right, point, depth + 1)

    return root

# Función para insertar un nuevo punto con un punto dado en
# El árbol KD y devuelve una nueva raíz. Principalmente usa la función recursiva "insertRec()"
def insert(root, point):
    return insertRec(root, point, 0)

# Un método de utilidad para determinar si dos puntos son iguales
# en el espacio dimensional k
def arePointsSame(point1, point2):
    # Compara los valores de coordenadas individuales
    for i in range(k):
        if point1[i] != point2[i]:
            return False

    return True

# Busca un punto representado por "point[]" en el árbol KD.
# El parámetro depth se utiliza para determinar el eje actual.
def searchRec(root, point, depth):
    # Casos base
    global cont, ListHoja
    #cont = 1
    if not root:
        return False
    if arePointsSame(root.point, point):
        return True

    # La dimensión actual se calcula utilizando la profundidad actual y el total de
    # dimensiones (k)
    cd = depth % k
    ListHoja = root.point
    # Compara el punto con la raíz con respecto a cd (dimensión actual)
    if point[cd] < root.point[cd]:
        cont = cont + 1
        return searchRec(root.left, point, depth + 1)
    cont = cont + 1    
    return searchRec(root.right, point, depth + 1)

# Busca un punto en el árbol KD. Principalmente utiliza
# searchRec()
def search(root, point):
    # Pasa la profundidad actual como 0
    return searchRec(root, point, 0)
#Distancia entrre dos puntos SIN LA RAIZ CUADRADA
def distSqrt(a, b):
    return (((b[0]-a[0])**2)+((b[1]-a[1])**2))  

# Programa principal para probar las funciones anteriores
if __name__ == '__main__':
    pn1 = int(input("Ingresa el punto personalizado No 1: "))
    pn2 = int(input("Ingresa el punto personalizado No 2: "))
    root = None
    points = [[3, 6], [17, 15], [13, 15], [6, 12], [9, 1], [2, 7], [10, 19]]
    #pnsLista = [pn1, pn2]

    n = len(points)

    for i in range(n):
        root = insert(root, points[i])

    point1 = [pn1, pn2] #[10, 19]

    if search(root, point1):
        print("Encontrado")
    else:
        print("No esta en la lista predefinida! ", points)
        print("Punto mas cercano: ", ListHoja)
        euclidianaDist = math.sqrt(distSqrt(point1, ListHoja))
        print("Distancia euclidiana: ", round(euclidianaDist, 3)) 
    print("Iteraciones: ",cont)