import numpy as np
import KNN as knn
import Normalizacao as normaliza
import Matriz_confuzi as confusao
import Contas as contas
import carregar_dados as loader 
import Curva_roc as curoc

def main():
    print("Escolha o valor de K:\n")
    k = int(input("\t1, 3, 5\n"))


    class1 = 0
    class2 = 0

    base = loader.carregar_base_dados('Statlog.m')
    rotulos = np.loadtxt('ClasseS.txt')

    coluna = 2
    normal = normaliza.Normaliza(base)
    linha, coluna = normal.shape
    tamanho = int(linha * 0.1)
    dados = np.zeros((tamanho, coluna))
        

    #print("dados", dados, "tamanho", tamanho, "linha: ", linha)
    
    i = 0
    while i < linha and (class1 == 0 or class2 == 0):
        if rotulos[i] == 1 and class1 == 0:
            class1 += 1
        elif rotulos[i] == 2 and class2 == 0:
            class2 += 1
        i += 1

    label = np.zeros(tamanho)
    while i < tamanho and (class1 < tamanho and class2 < tamanho):
        if rotulos[i] == 1 and class1 < tamanho:
            dados[class1 - 1, :] = normal[i, :]
            label[class1 - 1] = rotulos[i]
            class1 += 1
        elif rotulos[i] == 2 and class2 < tamanho:
            dados[class1 + class2 - 1, :] = normal[i, :]
            label[class1 + class2 - 1] = rotulos[i]
            class2 += 1
        else:
            continue
        i += 1
        if class1 >= tamanho or class2 >= tamanho:
            break

    
    print("classe 1: ", class1, ", classe 2:", class2)
    tamanho = class1 + class2
    dados = dados[:tamanho, :]
    label = label[:tamanho]

    print("dados", dados, "tamanho", tamanho, "linha: ", linha)
    calcClass = knn.knn(dados, normal, label, k)
    print("rotulo", calcClass)
    matrizConf = confusao.Confusao(rotulos, calcClass)
    print("matriz de confusao: ", matrizConf)
    contas.Contas(matrizConf)
    curoc.plot_roc_curve(rotulos, calcClass)

if __name__ == '__main__':
    main()
