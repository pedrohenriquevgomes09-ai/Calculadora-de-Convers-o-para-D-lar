import requests
try:
    url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"
    resposta = requests.get(url)
    dados = resposta.json()
    cotacao = float(dados["USDBRL"]["bid"])
except:
    print ('Erro ao buscar cotação. Usando valor padrão.')
    cotacao = 5.26
carteira = float(input('Quando você tem na carteria? '))
dolar = carteira / cotacao 
print (f'Cotação atual: {cotacao}')
print(f'Você pode comprar {dolar:.2f} dólares')


