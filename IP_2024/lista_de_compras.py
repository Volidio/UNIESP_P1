#No mundo moderno, a organização é fundamental, e uma lista de compras inteligente pode facilitar muito a vida. O objetivo deste projeto é criar um programa em Python que utilize um vetor para armazenar uma lista de compras. Mas não para por aí! O programa deve permitir ao usuário adicionar itens à lista, remover itens, exibir a lista atualizada.

#custom tk inter

#Inicializar um vetor vazio para armazenar os itens da lista de compras.
#Criar um menu de opções para o usuário, com as seguintes funcionalidades:
#Adicionar item: Ler o nome do item e a categoria e adicionar ao vetor.
#Remover item: Ler o nome do item a ser removido e removê-lo do vetor.
#Exibir lista: Exibir a lista de compras atualizada na tela.
#Sair: Encerrar o programa.

#Criar um loop que exiba o menu repetidamente até que o usuário escolha a opção "Sair".

lista_de_compras=[]
opção = 2

while opção != 0: #ou while True
    print("\n ======================")
    print("1 - adicionar novo item")
    print('2 - remover item')
    print('3 - exibir lista completa')
    print('0 - sair')
    opção = int(input('digite a opção desejada: '))
    
    #adicionar
    if opção == 1:
         print('\n ==>ADICIONAR ITEM<==')
         #lista_de_compras = lista_de_compras + [novoitem]
         novo_item = input("digite o novo item a ser adicionar: ")
         lista_de_compras = lista_de_compras + [novo_item]

    #remover
    elif opção == 2:
        print('\n ==>REMOVA UM ITEM<==')
        for i in range(len(lista_de_compras)):
            print(f'{i+1} - {lista_de_compras[i]}')
        
        print('\n =====')
        remover = int(input('digite o código do item: ')) - 1
        del lista_de_compras[remover]

    #listar
    elif opção == 3:
        print('\n ==>LISTA COMPLETA<==')
        for i in range(len(lista_de_compras)):
            print(f'{i+1} - {lista_de_compras[i]}')

