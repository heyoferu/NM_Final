import matplotlib.pyplot as plt
import numpy as np

def plot_equation(x, y, equation):
    # Crea una figura y un eje
    fig,ax = plt.subplots()

    # Grafica los puntos de la tabla de valores
    ax.scatter(x, y, label='PUNTOS')

    ax.plot(x, y, 'r-', label='Ecuación')

    # Agrega un título y etiquetas de los ejes
    ax.set_title('Gráfica de la ecuación: ' + equation)
    ax.set_xlabel('x')
    ax.set_ylabel('y')

    # Agrega una leyenda
    ax.legend()

    # Muestra la gráfica
    plt.show()


