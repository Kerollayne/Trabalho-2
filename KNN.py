import numpy as np

def knn(dados_treinamento, dados_teste, rotulos_treinamento, k):
    n_treinamento = dados_treinamento.shape[0]
    n_teste = dados_teste.shape[0]
    rotulos_teste = np.zeros(n_teste)

    for i in range(n_teste):
        distancias = np.sqrt(np.sum(np.power(dados_treinamento - dados_teste[i, :], 2), axis=1))
        indices_vizinhos = np.argsort(distancias)[:k]
        rotulos_vizinhos = rotulos_treinamento[indices_vizinhos]
        pesos_vizinhos = 1.0 / distancias[indices_vizinhos]
        soma_pesos = np.sum(pesos_vizinhos)
        probabilidades = np.zeros(np.unique(rotulos_treinamento).shape)

        for j in range(k):
            probabilidades[int(rotulos_vizinhos[j]) - 1] += pesos_vizinhos[j]

        rotulos_teste[i] = np.argmax(probabilidades) + 1

    return rotulos_teste#
