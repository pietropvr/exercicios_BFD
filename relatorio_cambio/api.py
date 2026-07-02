import requests
from datetime import datetime, timedelta

def consultar_moeda(moeda_input):
    # A BrasilAPI usa apenas a sigla (ex: USD), então removemos o -BRL se o usuário digitar
    moeda = moeda_input.replace("-BRL", "").upper()
    
    # A BrasilAPI retorna erro 404 em finais de semana. 
    # O loop abaixo tenta buscar hoje; se der erro, volta até 5 dias para achar um dia útil.
    for dias_atras in range(5):
        data_busca = (datetime.now() - timedelta(days=dias_atras)).strftime("%Y-%m-%d")
        url = f"https://brasilapi.com.br/api/cambio/v1/cotacao/{moeda}/{data_busca}"
        
        resposta = requests.get(url)
        
        if resposta.status_code == 200:
            dados = resposta.json()
            # A API retorna uma lista de cotações no dia. Pegamos a última (fechamento/mais recente).
            ultima_cotacao = dados['cotacoes'][-1] 
            return {
                "compra": ultima_cotacao['cotacao_compra'],
                "venda": ultima_cotacao['cotacao_venda']
            }
            
    return None # Retorna vazio caso dê erro após todas as tentativas
