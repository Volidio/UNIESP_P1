lista_de_compras=[]
def adicionar_item(Lista_de_compras: list) -> list:
        novo_item = input("digite o novo item a ser adicionado: ")
        Lista_de_compras = Lista_de_compras + [novo_item]

        return Lista_de_compras

def exibir_lista(Lista_de_compras):
        
        for i in range(len(lista_de_compras)):
            print(f'{i+1} - {lista_de_compras[i]}')

def remover_item(Lista_de_compras: list) -> list:
        remover = int(input('digite o código do item: ')) - 1

        del Lista_de_compras[remover]

        return Lista_de_compras

opção= 2

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

         lista_de_compras = adicionar_item(Lista_de_compras=lista_de_compras)

    #remover
    elif opção == 2:
        print('\n ==>REMOVA UM ITEM<==')
        exibir_lista(Lista_de_compras=lista_de_compras)
        
        print('\n =====')
        lista_de_compras=remover_item(Lista_de_compras=lista_de_compras)

    #listar
    elif opção == 3:
        print('\n ==>LISTA COMPLETA<==')
        exibir_lista(Lista_de_compras=lista_de_compras)