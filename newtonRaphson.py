from sympy import *
from tabulate import tabulate as tb
from math import e, log
from gui import create_table

def NR(iterations,x):
    table = []
    f = input("Type equation:\t")
    dx = str(diff(f))

    for i in range(iterations):
        table.append([])
        table[i].append(eval(f))
        table[i].append(eval(dx))
        table[i].append(x - (eval(f) / eval(dx)))
        table[i].append(
            abs(
            ((x - (eval(f) / eval(dx))) - x) / (x - (eval(f) / eval(dx)))
            )
        )
        table[i].append(
            abs(
            ((x - (eval(f) / eval(dx))) - x) / (x - (eval(f) / eval(dx)))
            ) * 100
        )

    
        x = x - (eval(f) / eval(dx))

    create_table(["fx","dx","xi + 1","e","e%"],table)