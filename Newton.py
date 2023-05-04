from prettytable import PrettyTable
from sympy import diff, Symbol
from math import *
from gui import create_table

def newton():
    tabla = []
    root_eval = lambda ec,dx: x - (ec / dx)
    ecuacion = input("Escriba la ecuación:\t")

    var = Symbol('x')

    derivada = diff(ecuacion, var)
    print(derivada)

    x_a = 0
    x = float(input("Valor inicial:\t"))

    i = 0
    while True:
        ec_eval = eval(ecuacion)
        dx_eval = eval(str(derivada))
        root = root_eval(ec_eval,dx_eval)
        
        x_a = x
        x = root

        tabla.append([ec_eval,dx_eval,x])

        if x_a == x:
            break
        i += 1
    create_table([ecuacion,str(derivada),"xn"],tabla)
    