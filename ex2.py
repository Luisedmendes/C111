import numpy as np

# Exercicio 1


# 1
# print(np.linspace(0, 1, num=21))

# # 2
# pares_0_51 = np.arange(start=0, stop=52, step=2)
# pares_100_50 = np.arange(start=100, stop=49, step=-2)
# print(pares_0_51)
# # array_combined = np.concatenate[pares_0_51, pares_100_50]  # type: ignore
# # print(array_combined)

# # 3
# print(np.sort(array_combined)[::-1])

# # 4
# mtrz = np.ones((3, 4))
# print(mtrz.ravel())  

# # 5
# random_matriz = np.random.randint(1, 10, (4, 5))

# linhas = random_matriz.shape[0]
# colunas = random_matriz.shape[1]
# total_elementos = random_matriz.size

# print("linhas:", linhas, "colunas:", colunas)
# print("Total:", total_elementos)

# resultado = "par de elementos" if total_elementos % 2 == 0 else "ímpar"
# print(resultado)

# # Exercicio 2

# # 1
np.random.seed(5)

array_floats = np.random.uniform(low=-1, high=1, size=10)

print("Array com a parte inteira:", np.floor(array_floats * 100))

# # 2
np.random.seed(10)

matriz = np.random.randint(1, 51, size=(4, 4))

print("Matriz 4x4:")
print(matriz)

# 3

print("Média das linhas:", matriz.mean(axis=1))
print("Média das colunas:", matriz.mean(axis=0))


# print("Maior média entre as linhas:", np.max(matriz.mean(axis=1)))
# print("Maior média entre as colunas:", np.max(matriz.mean(axis=0)))

# # 4
numeros, contagem = np.unique(matriz, return_counts=True)

# print("Números que aparecem 2 vezes:", numeros[contagem == 2])
