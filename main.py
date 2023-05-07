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

    print("-".center(70,"-"))
    print("METODOS NUMÉRICOS".center(70))
    print("-".center(70,"-"))
    print("Bienvenido al menú de Métodos realizados durante el semestre".center(70))
    print("Indica el número de tu selección".center(70))

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
        index = numericMethods.index(f"{i}")+1
        print("{:25}) {}".format(index,i))
        
    while True:
        try:
            selection = int(input("\n\t\tType the number method: \t"))
            print("_".center(70,"_"))
            break
        except ValueError:
            print("El valor ingresado no es numérico. Por favor, ingrese un número entero.")

    match selection:
        case 1:
            print("Error absoluto\n")
            error()

        case 2:
            print("Error relativo\n")
            errorRel(180,5)

        case 3:
            print("Bisección\n")
            bisec(1,2,10)

        case 4:
            print("Newton-Raphson\n")
            NR(10,4)
        case 5:
            print("Jacobi\n")
            jacobi()
        case 6:
            print("Newton\n")
            newton()
        case 7:
            print("Gauss-seidel\n")
            gs()
        case 8:
            print("Lagrange\n")
            lagrange()
        case 9:
            print("Trapecio\n")
            trap()
        case 10:
            print("Simpson 1/3\n")
            S1_2()
        case 11:
            print("Euler\n")
            euler()

# Menu loop
menu()
while True:
    try:
        print("\n¿Desea utilizar otro método?\n1. Continuar\n2. Terminar")
        option = int(input("\n> Selecciona: "))
    except ValueError:
        print("El valor ingresado no es numérico. Por favor, ingrese un número entero.")

    if option == 1:
        menu()
    elif option == 2:
        print("\n> Gracias por tanto, ¡vuelva pronto! :)")
        break

