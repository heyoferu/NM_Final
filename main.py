from Error import error, errorRel
from Bisection import bisec
from newtonRaphson import NR
from Newton import newton
from Jacobi import jacobi
from gaussSeidel import gs
from Lagrangage import lagrange
from trap import trap
from simp2 import S1_2
from Euler import euler
def menu():
    # initial menu
    # 
    numericMethods = [
        "Error absoluto",
        "Error relativo",
        "Bisec",
        "Newton-Raphson",
        "Jacobi",
        "Newton",
        "Gauss-Seidel",
        "Lagrange",
        "Trapecio",
        "Simpson 1/3",
        "Euler"
    ]

    for i in numericMethods:
        print(numericMethods.index(f"{i}")+1," )",i)
        
    selection = int(input("Type the number method:\t"))

    match selection:
        case 1:
            print("Error absoluto")
            error()

        case 2:
            print("Error relativo")
            errorRel(180,5)

        case 3:
            print("Bisección")
            bisec(1,2,10)

        case 4:
            print("Newton-Raphson")
            NR(10,4)
        case 5:
            print("Jacobi")
            jacobi()
        case 6:
            print("Newton")
            newton()
        case 7:
            print("Gauss-seidel")
            gs()
        case 8:
            print("Lagrange")
            lagrange()
        case 9:
            print("Trapecio")
            trap()
        case 10:
            print("Simpson 1/3")
            S1_2()
        case 11:
            print("Euler")
            euler()
menu()
