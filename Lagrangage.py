from sympy import *
from gui import create_table
from test import plot_equation
x = []
y = []

def lagrange():
    n = int(input("N puntos:\t"))
    points = []

    for i in range(n):
        points.append([float(input(f"Escribir punto {i+1}X:\t")), float(input(f"Escribir punto {i+1}Y:\t"))])

    polynomio = ""
    for i in range(n):
        xi, yi = points[i]; term = str(yi)
        for j in range(n):
            if i != j: xj, yj = points[j]; term = "(" + term + "* (x - " + str(xj) + ")) / (" + str(xi - xj) + ")"
        if i == 0:
            polynomio += term
        else:
            polynomio += " + " + term

    polynomio = str(simplify(polynomio))
    for i in range(n):
        x.append(points[i][0])
        y.append(points[i][1])
        
    plot_equation(x,y,polynomio)