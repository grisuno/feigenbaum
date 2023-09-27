# Importar las librerías necesarias
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Definir la función logística
def logistic(r, x):
    return r * x * (1 - x)

# Definir la función para calcular la constante de Feigenbaum
def feigenbaum(r_min, r_max, n_iter, n_skip):
    # Crear un array de valores de r entre r_min y r_max
    r = np.linspace(r_min, r_max, int((r_max - r_min) / 0.001))
    # Inicializar un array vacío para guardar los valores de x
    x = np.ones(len(r)) * 0.5
    # Iterar la función logística n_iter veces
    for i in range(n_iter):
        # Aplicar la función logística a cada elemento de x
        x = logistic(r, x)
        # Guardar los últimos n_skip valores de x para cada valor de r
        if i >= (n_iter - n_skip):
            plt.plot(r, x, ',k', alpha=0.25)
    # Devolver los arreglos R y X
    return r, x

# Definir la función para calcular el conjunto de Mandelbrot
def mandelbrot(x_min, x_max, y_min, y_max, max_iter):
    # Crear un array de valores complejos entre x_min + y_min * i y x_max + y_max * i
    c = np.linspace(x_min + y_min * 1j, x_max + y_max * 1j, 1000)
    # Inicializar un array vacío para guardar los valores de z
    z = np.zeros_like(c)
    # Inicializar un array vacío para guardar los valores de n
    n = np.zeros_like(c)
    # Iterar la función cuadrática compleja max_iter veces
    for i in range(max_iter):
        # Aplicar la función cuadrática compleja a cada elemento de z y c
        z = z**2 + c
        # Actualizar los valores de n donde z no ha divergido
        n[np.abs(z) < 2] = i + 1
    return n

# Crear un gráfico 3D combinado
def create_combined_plot():
    # Parámetros para el diagrama de bifurcación
    r_min, r_max = 2.5, 4.0
    n_iter, n_skip = 1000, 100
    R, X = feigenbaum(r_min, r_max, n_iter, n_skip)
    
    # Parámetros para el conjunto de Mandelbrot
    x_min, x_max, y_min, y_max, max_iter = -2.0, 0.5, -1.25, 1.25, 50
    n_points = min(len(R), len(X))  # Asegurarse de tener el mismo número de puntos
    R, X = R[:n_points], X[:n_points]  # Tomar solo los primeros n_points
    Y = np.linspace(x_min, x_max, len(X))
    
    # Crear la figura 3D
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    # Graficar el diagrama de bifurcación en el plano XY y el conjunto de Mandelbrot en el eje Z
    ax.plot(R, X, Y, color='b', alpha=0.5)
    
    # Etiquetas y título
    ax.set_xlabel('r')
    ax.set_ylabel('x')
    ax.set_zlabel('y (Iteraciones Mandelbrot)')
    ax.set_title('Diagrama de Bifurcación y Conjunto de Mandelbrot en 3D')
    
    # Mostrar el gráfico
    plt.show()

# Llamar a la función para crear el gráfico combinado
create_combined_plot()
