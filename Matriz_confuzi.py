import numpy as np

def Confusao(rotulos, calClass):
    linhas = len(calClass)
    matriz = np.zeros((2, 2))

    for i in range(linhas):
        if rotulos[i] == 1 and calClass[i] == 1:
            matriz[0, 0] += 1
        if rotulos[i] == 1 and calClass[i] == 2:
            matriz[0, 1] += 1
        if rotulos[i] == 2 and calClass[i] == 1:
            matriz[1, 0] += 1
        if rotulos[i] == 2 and calClass[i] == 2:
            matriz[1, 1] += 1
    
    return matriz
