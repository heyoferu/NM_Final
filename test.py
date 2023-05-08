import matplotlib.pyplot as plt
import numpy as np

def plot_equation(x, y, equation):
    # Crea una figura y un eje
    fig,ax = plt.subplots()

    x_range = np.linspace(x[0],x[-1])
    y_range = [eval(equation) for x in x_range]

    # Grafica los puntos de la tabla de valores
    ax.scatter(x, y, label='PUNTOS')
    # Grafica la ecuacion
    ax.plot(x_range,y_range, color = "green")

    # Agrega un título y etiquetas de los ejes
    ax.set_title('Gráfica de la ecuación: ' + equation)
    ax.set_xlabel('x')
    ax.set_ylabel('y')

    # Agrega una leyenda
    ax.legend()

    # Muestra la gráfica
    plt.show()

def plot_equation2(x, y, equation):
    # Crea una figura y un eje
    fig,ax = plt.subplots()
    
    # Grafica los puntos de la tabla de valores
    ax.scatter(x, y, label='PUNTOS')
    # Grafica la ecuacion
    ax.plot(x,y, color = "green")

    # Agrega un título y etiquetas de los ejes
    ax.set_title('Gráfica de la ecuación: ' + equation)
    ax.set_xlabel('x')
    ax.set_ylabel('y')

    # Agrega una leyenda
    ax.legend()

    # Muestra la gráfica
    plt.show()

