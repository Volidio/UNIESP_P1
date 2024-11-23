from sys import argv


def lerArquivo(arquivo):
    with open(arquivo,'r') as conteudoArquivo: #Abre o arquivo no modo 'r' de leitura
        conteudo = conteudoArquivo.read()
    print(f'Conteudo do arquivo: {conteudo}')

def adicionarTextoNoArquivo(arquivo, texto):
    with open(arquivo, 'a') as conteudoArquivo: #Abre o arquivo no modo 'a' para adicionar texto sem sobrescrever
        conteudoArquivo.write(texto)

def escreverNoArquivo(arquivo, texto):
    with open(arquivo, 'w') as conteudoArquivo: #Abre o arquivo no modo 'w' para escrever texto, caso tenha conteudo no arquivo ele sere sobreescrito.
        conteudoArquivo.write(texto)

if __name__ == '__main__':
    
    arquivoDeTexto = 'exemplo.txt'
    
    texto = input('Digite o texto que voce quer escrever no arquivo "exemplo.txt": ')
    adicionarTextoNoArquivo(arquivoDeTexto, texto)
    lerArquivo(arquivoDeTexto)
    
    texto2 = input('Digite mais texto para colocar no arquivo: ')
    adicionarTextoNoArquivo(arquivoDeTexto, texto2)
    lerArquivo(arquivoDeTexto)

    texto3 = input('Digite texto para sobreescrever todo arquivo: ')
    escreverNoArquivo(arquivoDeTexto, texto3)
    lerArquivo(arquivoDeTexto)