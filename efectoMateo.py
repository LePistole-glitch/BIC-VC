import numpy as np
import matplotlib.pyplot as plt

mes = ["Enero", "Febrero", "Febrero","Febrero","Febrero","Febrero","Febrero", "Marzo", "Marzo", "Marzo", "Abril", "Abril",
        "Julio", "Sepiembre", "Octubre", "Noviembre", "Diciembre", "Diciembre","Diciembre","Diciembre","Diciembre"]
plt.xlabel('MESES')
plt.ylabel("CANTIDAD")
plt.hist(mes, color="red")
plt.show()