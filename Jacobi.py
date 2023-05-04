from prettytable import PrettyTable
from sympy import symbols,solve,parse_expr
from gui import create_table
def jacobi():
    table = []
    tableError = []
    headers = []

    e_abs = lambda x_new, x_pre: (abs((x_new - x_pre) / x_new)) * 100


    eqs = input("Type the equations separated by comma:\t").split(",")
    xn = input("type the vars:\t").split(",")

    req = []
    req_v = []
    eq_solved = []
    xn_values = []
    temp_values = []
    final_values = []
    errors = []
    final_error = []
    error_headers = []
    toAdd = []

    for i in range(len(xn)):
        headers.append(xn[i])
        headers.append(f"E{i+1}")

    for i in range(len(xn)):
        xn_values.append(float(input(f"Type value of {xn[i]}:\t")))

    for i in range(len(eqs)):
        x = symbols(xn[i])
        eq_temp = solve(parse_expr(eqs[i].split("=")[0]) - parse_expr(eqs[i].split("=")[1]),x)[0]
        eq_solved.append(str(eq_temp))


    for i in range(len(xn)):
        eq_temp = eqs[i].split('=')
        req.append(eq_temp[0])
        req_v.append(int(eq_temp[1]))

    for eq in range(len(eq_solved)):
        for i in range(len(xn)):
            temp = eq_solved[eq].replace(xn[i],f"xn_values[{i}]")
            temp2 = req[eq].replace(xn[i],f"xn_values[{i}]")
            eq_solved[eq] = temp
            req[eq] = temp2

    e = float(input("Type the error percent:\t"))

    while True:
        for i in range(len(xn)):
            x_old = xn_values[i]
            x_new = eval(eq_solved[i])
            error = e_abs(x_new,x_old)
            temp_values.append(x_new)
            toAdd.append(x_new)
            toAdd.append(error)
            errors.append(error)

        xn_values = temp_values.copy()
        table.append(toAdd.copy())
        toAdd.clear()
        temp_values.clear()

        if all(ei < e for ei in errors):
            for i in range(len(xn)):
                final_values.append(eval(req[i]))

            for i in range(len(xn)):
                new_error = e_abs(final_values[i],req_v[i])
                final_error.append(new_error)

            for i in range(len(final_error)):
                error_headers.append(f"E{i+1}")

            tableError.append(final_error.copy())

            break

        errors.clear()
    
    create_table(headers,table)
    create_table(error_headers,tableError)

