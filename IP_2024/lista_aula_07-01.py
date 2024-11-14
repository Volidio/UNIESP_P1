# Escreva um algoritmo que permita a leitura dos nomes de 5 clubes de futebol e armazene os nomes lidos em um vetor. Após isto, o algoritmo deve permitir a leitura de mais 1 nome qualquer de clube e depois escrever a mensagem ACHEI, se o nome estiver entre os 5 nomes lidos anteriormente (guardados no vetor), ou NÃO ACHEI caso contrário.

times_de_futebol = ["paysandu", "flamengo", "vasco", "belo", "gremio"]
clube_verificador = input ("digite seu clube: ")
confirmação_de_busca = False
for times in times_de_futebol:
    if times.upper() == clube_verificador.upper():
        confirmação_de_busca = True
if confirmação_de_busca:
    print("achei")
else:
    print("não achei") 

if clube_verificador in times:
    print ("achei")
else:
    print ("não achei")

notas_de_alunos = [4,5,6,3,6]
for notas in notas_de_alunos:
    print (notas)
média= 24/5
print(média)
#3 alunos com notas acima da média 5;6;6