import requests
import pandas as pd
from api_key import api_key

key = api_key
symbol = 'MGLU3.SA'  # Símbolo para Magazine Luiza na B3 com Alpha Vantage

# URL para pegar dados diários
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&outputsize=compact&apikey={key}'

# Requisição
response = requests.get(url)
data = response.json()

# Extração dos dados de preço
if 'Time Series (Daily)' in data:
    df = pd.DataFrame.from_dict(data['Time Series (Daily)'], orient='index')
    df = df.rename(columns={
        '1. open': 'abertura',
        '2. high': 'alta',
        '3. low': 'baixa',
        '4. close': 'fechamento',
        '5. volume': 'volume'
    })
    df.index = pd.to_datetime(df.index)
    df = df.sort_index()
    df = df.astype(float)
    print(df.tail())
else:
    print("Erro ao buscar dados:", data.get("Error Message", data))
    ##############


