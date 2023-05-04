from math import e as euler
from sympy import *
from prettytable import PrettyTable
from gui import create_table


def bisec(xi,xu, iteration):

    tabla = []
    headers = ["xi","xu","xr"]
    eq = input("Type equation:\t")
    f = lambda x: parse_expr(eq).subs('x',x)

    for i in range(iteration):            
            xr = (xi + xu) / 2

            
            tabla.append([xi,xu,xr])
            
            if f(xi) * f(xr) < 0:
                xu = xr

            if f(xi) * f(xr) > 0:
                xi = xr

            if f(xi) * f(xr) == 0:
                 break

    create_table(headers,tabla)
