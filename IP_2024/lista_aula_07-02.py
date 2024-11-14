
alunos =  [5,10,8,7.5,9]
soma = 0
for i in range(len(alunos)):
    soma += alunos[i]

média = soma/len(alunos)
print(f'média da turma: {média}')