from gui import create_table
def error():
    headers = ["medidas"]
    n = int(input("Cantidad de medidas:\t"))
    measures = []
    for i in range(n):
        measures.append(float(input(f"Medida {i+1}:\t")))

    media = 0; sumo = 0
    
    for i in range(len(measures)): 
        media += measures[i]
    
    media = media / len(measures)

    for i in range(len(measures)):
        sumo += (measures[i] - media)**2
    
    final = round((sumo / (len(measures) * (len(measures) - 1))) ** 0.5, 2)
    measures.append(f"Error: {final}")
    create_table(headers,measures)


def errorRel():
    value_r = float(input("Valor exacto:\t"))
    e = float(input("Error:\t"))
    result = round((e / value_r) * 100, 2)
    tabla = [result]
    create_table(["error"],tabla)
