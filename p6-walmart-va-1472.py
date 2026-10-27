import matplotlib.pyplot as plt
import numpy as np

# JOSE SOLIS NC 1472
cant_productos = [100,150,200,300,500]
precio = [4000,7000, 9000, 12000, 18000]

plt.plot(cant_productos,precio)
plt.show()
# personaliza grafica

plt.plot(cant_productos,precio,color='blue',marker='o',linestyle='dashed',linewith=2,markersize=12)
plt.title("ventas de walmart 1389")

plt.show()
plt.xlabel("cant_prod")
plt.ylabel("precios")
plt.show()
