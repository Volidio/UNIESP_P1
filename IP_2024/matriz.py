matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matriz)
print(matriz[1])
print(matriz[1][2])

for i in range(len(matriz)): #vai percorrer
    for j in range(len(matriz[i])): 
        print(matriz[i][j])

