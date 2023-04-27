# Fernando Antonio Hernandez Zoma
# 3M LIDTS


def eabs(value_r,value_apx): # funcion error absoluto; recibe como argumento el valor real y valor aproximado
    return abs(value_r - value_apx) # retorna el valor absoluto de la resta de ambos

def emul(measures): # funcion para calcular el error de una lista de medidas

    # variables
    # media    # sumatoria de (L-media) ** 2
    media = 0; sumo = 0
    
    # sumatoria de medidas
    for i in range(len(measures)): 
        media += measures[i]
    
    media = media / len(measures) # media de las medidas

    # sumatoria de (medida - media) al cuadrado
    for i in range(len(measures)):
        sumo += (measures[i] - media)**2

    # retorna el error con dos decimales

    # [WIP]: it will return a n digits of decimals 
    return round((sumo / (len(measures) * (len(measures) - 1))) ** 0.5, 2)


def erel(value_r,e): # error relativo
    return round((e / value_r) * 100, 2)


while True:
    print("Error menu".center(70))

    print("(1) Calcular el error absoluto de un valor real y un aproximado")
    print("(2) Calcular el error de n medidas")
    print("(3) Calcular el error relativo de n medidas")

    a = int(input("Seleccione la opcion deseada:\n"))

    match a:
        case 1:
            a = float(input("Escriba el valor real:\t"))
            b = float(input("Escriba el valor aproximado:\t"))

            print(f"El resultado es:\t{eabs(a,b)}")

        case 2:
            n = int(input("Numero de medidas:\t"))
            x = []

            for i in range(n):
                x.append(float(input(f"Medida {i+1}:\t")))
            
            print(f"El resultado es:\t{emul(x)}")

        case 3:
            a = float(input("Escriba el valor real:\t"))
            b = float(input("Escriba el valor aproximado:\t"))

            print(f"El resultado es:\t{erel(a,b)}")