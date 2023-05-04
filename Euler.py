from prettytable import PrettyTable
from sympy import *
from gui import create_table
table = []

print("*** EULER METHOD ***\nIngrese los siguientes datos:\n")
coordinates = str(input("Punto Inicial:\t\t")).split(",")
valorF, h = float(input("Valor Final:\t\t")), float(input("Incrementos (h):\t"))
fx = str(input("Función:\t\t"))         # Function

x, y = float(coordinates[0]), float(coordinates[1])     # Coordenadas
fxy, c = eval(fx), int(0)                               # Función evaluada, contador
table.append([x, y, fxy])                              # Tabla para PRETTY TABLE
arrayTable = [[x, y, fxy]]                              # Guarda los datsos

while x <= valorF-h:
    x, y = (c+1)*h, arrayTable[c][1] + h *(arrayTable[c][2])
    fxy = eval(fx)
    table.append([x, y, fxy])
    arrayTable.append([x, y, fxy])
    c += 1

create_table(["X", "Y", "f(x,y)"],table)
