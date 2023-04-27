def menu():
    # initial menu
    # 
    numericMethods = [
        "Error",
        "Bisec"
    ]

    for i in numericMethods:
        print(i)
        
    selection = input("Type the number method:\t")

    match selection:
        case 1:
            pass

menu()
