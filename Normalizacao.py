import numpy as np

def Normaliza(base):
    l, c = base.shape
    normal = np.zeros((l, c))
    MAIOR = 0
    MENOR = np.inf
    for i in range(l):
        for j in range(c):
            # Pega o maior e o menor valor para fazer a conta da Normalização
            if (MAIOR < base[i,j]):
                MAIOR = base[i,j]
            if (MENOR > base[i,j]):
                MENOR = base[i,j]
    for i in range(l):
        for j in range(c):
            normal[i,j]  = (base[i,j] - MENOR) / (MAIOR - MENOR)
    return normal
