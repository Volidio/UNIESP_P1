import requests
from loguru import logger
from deep_translator import GoogleTranslator

URL = 'https://api.adviceslip.com/advice'
n_conselhos = int(input('digite a quantidade de conselhos: '))

try:
    for i in range(5):

        logger.info('Ciclo de chamada de API iniciado.')
        result = requests.get(URL)
        logger.success("Chamada de API realizada com sucesso.")

        id =result.json()['slip']['id']
        advice=result.json()['slip']['advice']

        traducao = GoogleTranslator (source='english',target='portuguese').translate(advice)
        logger.success('Tradução realizada com sucesso.')
        texto = f'{result.json()['slip']['id']} {result.json()['slip']['advice']}'

        with open('conselho.txt', 'a', encoding='UTF-8') as arquivo:
            arquivo.write(texto + '\n')
        logger.success('Registro no banco de dados (txt) realizado com sucesso. ')
except Exception as error:
    logger.exception(f'Error: {error}')
