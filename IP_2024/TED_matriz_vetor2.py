from random import randint
from copy import deepcopy

matriz_a, matriz_b, matriz_temp = [],[],[]
soma_total = 0

for _ in range(10):
    for i in range (10):
        matriz_temp.append(randint(0,10))
    matriz_a.append(matriz_temp)
    matriz_temp = []


for linha in matriz_a:
    for valor in linha:
        soma_total += valor

matriz_b = deepcopy(matriz_a)


for x,i in enumerate(matriz_b):
    for posicao,valor in enumerate(i):
        matriz_b[x][posicao] = valor*3


print(f'matriz_a {matriz_a}\n')
print(f'Soma total {soma_total}\n')
print(f'matriz_b {matriz_b}')
