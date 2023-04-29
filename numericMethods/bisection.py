from math import e as euler
from sympy import *
from tabulate import tabulate


def bisec(xi,xu, iteration):

    tabla = []
    eq = input("Type equation:\t")
    f = lambda x: parse_expr(eq).subs('x',x)

    for i in range(iteration):            
            xr = (xi + xu) / 2

            
            tabla.append([i,xi,xu,xr])
            
            if f(xi) * f(xr) < 0:
                xu = xr

            if f(xi) * f(xr) > 0:
                xi = xr

            if f(xi) * f(xr) == 0:
                 break

    return print(tabulate(tabla,headers=["i","xi","xu","xr"]))

