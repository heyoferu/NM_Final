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
        
    selection = input("Type the number method:\t")

    match selection:
        case 1:
            pass

menu()
