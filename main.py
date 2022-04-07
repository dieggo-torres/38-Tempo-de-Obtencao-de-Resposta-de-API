import requests
import locale
import time

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')


def tempo_execucao_decorator(function):
    def wrapper_function():
        instante_inicial = time.time()
        function()
        instante_final = time.time()
        print(f'Tempo de execução: {instante_final - instante_inicial}')

    return wrapper_function


@tempo_execucao_decorator
def obter_cotacao_dolar():
    link = 'https://economia.awesomeapi.com.br/json/last/USD-BRL'
    requisicao = requests.get(link)
    if requisicao:
        cotacao = requisicao.json()["USD"]["bid"]
        cotacao = float(cotacao)
        print(f'Cotação: {locale.currency(cotacao, symbol=True)}')
    else:
        print('Combinação de moedas inexistente na API.')
        return


if __name__ == '__main__':
    obter_cotacao_dolar()
