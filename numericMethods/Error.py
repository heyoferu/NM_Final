def error(measures):

    media = 0; sumo = 0
    
    for i in range(len(measures)): 
        media += measures[i]
    
    media = media / len(measures)

    for i in range(len(measures)):
        sumo += (measures[i] - media)**2

    return round((sumo / (len(measures) * (len(measures) - 1))) ** 0.5, 2)


def errorRel(value_r,e): 
    return round((e / value_r) * 100, 2)
