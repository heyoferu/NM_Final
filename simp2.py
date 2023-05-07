import matplotlib.pyplot as plt
from tabulate import tabulate as tb
from math import e
import numpy as np

def S1_2():
    headers = ["i","x","y"]
    data = []
    equation = input("Escriba la ecuación:\t")
    a = float(input("Escriba el punto A:\t"))
    b = float(input("Escriba el punto B:\t"))
    n = float(input("Escriba el número de subintervalos:\t"))

    incremental = (b - a) / n
    i = 1
    x = a
    xs = []
    ys = []

    while x <= b:
        y = eval(equation)
        xs.append(x)
        ys.append(y)
        data.append([i,x,y])
        x += incremental

    x_range = np.linspace(a - 1*(b-a), b + 1*(b-a), 1000)
    y_range = [eval(equation) for x in x_range]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

    ax1.plot(x_range, y_range, '-', linewidth=2)
    ax1.plot(xs, ys, 'o', color='blue')
    for i in range(len(xs)):
        ax1.vlines(xs[i], ymin=0, ymax=ys[i], colors='r', linestyles='dashed', linewidth=1)

    ax1.fill_between(xs, ys, alpha=0.2)
    ax1.set_title('Gráfica de la ecuación con líneas verticales en cada punto')
    ax1.set_xlabel('x')
    ax1.set_ylabel('y')

    headers = ["i","x","y"]
    data = [[i+1, xs[i], ys[i]] for i in range(len(xs))]
    table = tb(data, headers, tablefmt="pipe", floatfmt=".2f")
    ax2.axis('off')
    ax2.text(0.5, 0.5, table, va='center', ha='center', fontfamily='monospace', fontsize=10, transform=ax2.transAxes)
    plt.title('Gráfica de la ecuación')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()
