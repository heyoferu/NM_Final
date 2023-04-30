from sympy import *
from tabulate import tabulate as tb
def NR(iterations,n):
    table = []
    eq = input("Type equation:\t")
    f = lambda x: parse_expr(eq).subs('x',x)
    dx = lambda x: diff(eq).subs('x',x)

    for i in range(iterations):
        table.append([])
        table[i].append(i)
        table[i].append(f(n))
        table[i].append(dx(n))
        table[i].append(n - (f(n) / dx(n)))
        table[i].append(
            abs(
            ((n - (f(n) / dx(n))) - n) / (n - (f(n) / dx(n)))
            )
        )
        table[i].append(
            abs(
            ((n - (f(n) / dx(n))) - n) / (n - (f(n) / dx(n)))
            ) * 100
        )

    
        n = n - (f(n) / dx(n))

    return print(tb(NR(1,10),headers=["i","fx","dx","xi + 1","e","e%"]))
