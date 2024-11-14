filename = "meu_arquivo.txt"

mensagem = input('Digite sua mensagem!')

with open (filename, 'w', encoding= 'UTF-8') as arquivo:
    arquivo.write(mensagem + '\n')

with open (filename, 'r', encoding= 'UTF-8') as file:
    conteudo = file.read()
    print(conteudo)