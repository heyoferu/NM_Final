from prettytable import PrettyTable
from sympy import symbols,solve,parse_expr

table = PrettyTable()
headers = []

e_abs = lambda x_new, x_old: (abs((x_new - x_old) / x_new)) * 100

eqs = input("Type the equations separated by comma:\t").split(",")
xn = input("type the literals:\t").split(",")
eq_solved = []
xn_values = []
toAdd = []

for i in range(len(xn)):
    headers.append(xn[i])
    headers.append(f"E{i+1}")

for i in range(len(xn)):
    xn_values.append(float(input(f"Type value of {xn[i]}:\t")))

for i in range(len(eqs)):
    x = symbols(xn[i])
    eq_temp = solve(parse_expr(eqs[i].split("=")[0]) - parse_expr(eqs[i].split("=")[1]),x)[0]; print(eq_temp)
    eq_solved.append(str(eq_temp))

for eq in range(len(eq_solved)):
    for i in range(len(xn)):
        temp = eq_solved[eq].replace(xn[i],f"xn_values[{i}]")
        eq_solved[eq] = temp

n = int(input("Numéro de iteraciones:\t"))
c = 0

while c <= n:
    toAdd.clear()
    for i in range(len(xn)):

        x_old = xn_values[i]
        x_new = eval(eq_solved[i])
        print(x_new)
        error = e_abs(x_new,x_old)

        toAdd.append(x_new)
        toAdd.append(error)

        xn_values[i] = x_new

    table.add_row(toAdd)

    c += 1

table.field_names = headers
print(table)