import re

# Função para verificar se uma senha atende à política
def is_valid_password(password):
    if len(password) != 12:
        return False
    if not re.search(r'[0-9]', password):  # Pelo menos um dígito
        return False
    if not re.search(r'[a-z]', password):  # Pelo menos uma letra minúscula
        return False
    if not re.search(r'[A-Z]', password):  # Pelo menos uma letra maiúscula
        return False
    if re.search(r'[^a-zA-Z0-9]', password):  # Sem caracteres especiais
        return False
    return True

# Abrindo o arquivo rockyou.txt e filtrando as senhas válidas
with open('rockyou.txt', 'r', encoding='utf-8', errors='ignore') as file:
    valid_passwords = [line.strip() for line in file if is_valid_password(line.strip())]

# Salvando a lista de senhas válidas em um novo arquivo
with open('valid_passwords.txt', 'w') as output_file:
    for password in valid_passwords:
        output_file.write(password + '\n')

print(f"Total de senhas válidas encontradas: {len(valid_passwords)}")

