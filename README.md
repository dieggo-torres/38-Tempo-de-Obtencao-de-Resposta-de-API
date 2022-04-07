# [Avançado] Obtenção de Tempo de Resposta de API
<img alt="" src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white">

Este programa faz uma requisição para a API de moedas do [Awesome API](https://docs.awesomeapi.com.br/api-de-moedas) a fim de obter a cotação do dólar americano (USD).
Além de obter a cotação dessa moeda em reais brasileiro (BRL), o programa calcula o tempo de execução da função faz a referida requisição.

Para obter o tempo de execução da função, usei uma função decoradora.

## Bibliotecas Usadas

- requests
- locale
- time