## Gubuster

O Gobuster é uma ferramenta de linha de comando, escrita em Go, utilizada principalmente para realizar força bruta em diretórios e arquivos em servidores web, além de também ser empregada para enumerar subdomínios e vhosts. Ele é amplamente usado em pentests e auditorias de segurança para descobrir recursos ocultos em um servidor que podem não estar facilmente acessíveis através de navegação convencional.

Os principais casos de uso do Gobuster incluem:
- Força Bruta em Diretórios e Arquivos: Descobrir diretórios e arquivos ocultos em um servidor web que não estão listados publicamente.
- Enumeração de Subdomínios: Identificar subdomínios de um domínio principal, o que pode revelar novos vetores de ataque.
- Reconhecimento de Vhosts: Enumerar virtual hosts configurados em um servidor para identificar domínios adicionais que podem estar hospedados no mesmo servidor.
- Busca por Parâmetros e URLs: Identificar parâmetros GET ou POST que podem ser explorados para injeção de SQL, XSS, etc.

### Modo para Diretórios e Arquivos

Para realizar força bruta em diretórios e arquivos de um servidor web, use o modo dir.

```
gobuster dir -u http://example.com -w /path/to/wordlist.txt -t 50
```

-dir: Define o modo de força bruta em diretórios e arquivos.
-u: Especifica a URL alvo.
-w: Define a wordlist que será utilizada para tentar descobrir diretórios e arquivos.
-t: Especifica o número de threads para a execução (aumenta a velocidade da força bruta).

### Modo para Subdomínios

Para enumerar subdomínios, use o modo dns.

```
gobuster dns -d example.com -w /path/to/wordlist.txt -t 50
```

-dns: Define o modo de enumeração de subdomínios.
-d: Especifica o domínio alvo.
-w: Define a wordlist com possíveis subdomínios.
-t: Especifica o número de threads.

### Modo para Vhosts

Para realizar reconhecimento de vhosts (virtual hosts), use o modo vhost.

```
gobuster vhost -u http://example.com -w /path/to/wordlist.txt -t 50
```

-vhost: Define o modo de enumeração de virtual hosts.
-u: Especifica a URL base do alvo.
-w: Define a wordlist com possíveis nomes de vhosts.
-t: Especifica o número de threads.

### Adicionar Cabeçalhos HTTP Personalizados

Você pode adicionar cabeçalhos HTTP personalizados às requisições, como tokens de autenticação ou cookies.

```
gobuster dir -u http://example.com -w /path/to/wordlist.txt -t 50 -H "Authorization: Bearer your_token_here"
```

-H "Header: Value": Adiciona um cabeçalho HTTP personalizado.