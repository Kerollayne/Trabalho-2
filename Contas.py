import numpy as np

def Contas(matriz):
    TPR = matriz[0, 0] / (matriz[0, 0] + matriz[0, 1])
    FPR = matriz[1, 0] / (matriz[1, 0] + matriz[1, 1])
    ACC = (matriz[0, 0] + matriz[1, 1]) / (matriz[0, 0] + matriz[0, 1] + matriz[1, 0] + matriz[1, 1])
    print(" TPR", TPR, "FRP", FPR, "ACC", ACC)
    v = np.array([FPR, TPR])
   

