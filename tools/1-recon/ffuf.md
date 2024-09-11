## Ffuf

O FFUF (Fuzz Faster U Fool) é uma ferramenta de fuzzing rápida e flexível, desenvolvida para realizar força bruta em servidores web e APIs. Ela é amplamente utilizada em pentests e testes de segurança para descobrir diretórios, arquivos, parâmetros GET/POST, e outras entradas que podem ser exploradas em um servidor ou aplicação web. FFUF é conhecida por sua velocidade e capacidade de customização, permitindo que os usuários adaptem a ferramenta a uma ampla gama de cenários de ataque.

Os principais casos de uso do FFUF incluem:
- Força Bruta em Diretórios e Arquivos: Descobrir diretórios e arquivos ocultos em servidores web.
- Força Bruta em Parâmetros de URL: Identificar parâmetros GET ou POST que podem ser manipulados ou explorados.
- Enumeração de Subdomínios: Encontrar subdomínios de um domínio principal.
- Força Bruta em APIs: Descobrir endpoints e métodos ocultos em APIs.
- Fuzzing de Parâmetros: Testar diferentes entradas em parâmetros de requisição para identificar vulnerabilidades como SQL Injection ou XSS.

### Força Bruta em Diretórios e Arquivos

Para realizar força bruta em diretórios e arquivos de um servidor web, use o parâmetro -u para definir a URL alvo e -w para especificar a wordlist.

```
ffuf -u http://example.com/FUZZ -w /path/to/wordlist.txt -t 50
```

-u: Define a URL alvo, onde FUZZ é o marcador que será substituído pelos termos da wordlist.
-w: Especifica a wordlist que será utilizada para tentar descobrir diretórios e arquivos.
-t: Define o número de threads para a execução, o que aumenta a velocidade da força bruta.

### Força Bruta em Parâmetros de URL

Você pode usar o FFUF para descobrir parâmetros GET ou POST que podem estar escondidos ou serem vulneráveis.

```
ffuf -u http://example.com/index.php?FUZZ=test -w /path/to/wordlist.txt -t 50
```

-u: Define a URL alvo, onde FUZZ é o marcador para os parâmetros.
-w: Especifica a wordlist que será utilizada para tentar descobrir parâmetros.

### Força Bruta em Subdomínios

Para enumerar subdomínios de um domínio principal, você pode usar o FFUF da seguinte maneira:

```
ffuf -u http://FUZZ.example.com/ -w /path/to/wordlist.txt -t 50 -H "Host: FUZZ.example.com"
```

-u: Define a URL alvo, onde FUZZ é o marcador para os subdomínios.
-w: Especifica a wordlist com possíveis subdomínios.
-H: Define o cabeçalho Host para especificar o subdomínio em cada requisição.

### Filtro de Respostas

FFUF permite filtrar as respostas com base no código de status, tamanho do conteúdo ou palavras específicas, ajudando a identificar apenas as respostas relevantes.

```
ffuf -u http://example.com/FUZZ -w /path/to/wordlist.txt -t 50 -fc 404
```

-fc: Filtra as respostas por código de status HTTP (neste caso, exclui 404 Not Found).



## Comandos ffuf

    ffuf -h
    Exibe a ajuda do comando ffuf, mostrando as opções e sintaxe disponíveis.

    ffuf -w wordlist.txt:FUZZ -u http://SERVER_IP:PORT/FUZZ
    Realiza fuzzing de diretórios, testando diferentes caminhos com base na lista de palavras (wordlist).

    ffuf -w wordlist.txt:FUZZ -u http://SERVER_IP:PORT/indexFUZZ
    Faz fuzzing de extensões, buscando arquivos com extensões variadas baseadas na wordlist.

    ffuf -w wordlist.txt:FUZZ -u http://SERVER_IP:PORT/blog/FUZZ.php
    Fuzzing de páginas específicas, focando em um arquivo PHP com variações de nome.

    ffuf -w wordlist.txt:FUZZ -u http://SERVER_IP:PORT/FUZZ -recursion -recursion-depth 1 -e .php -v
    Executa fuzzing recursivo, explorando diretórios e arquivos com profundidade de 1 nível, verificando também arquivos com extensão PHP.

    ffuf -w wordlist.txt:FUZZ -u https://FUZZ.hackthebox.eu/
    Realiza fuzzing de subdomínios, testando variações para encontrar subdomínios ativos.

    ffuf -w wordlist.txt:FUZZ -u http://academy.htb:PORT/ -H 'Host: FUZZ.academy.htb' -fs xxx
    Fuzzing de VHosts (Virtual Hosts), testando diferentes hosts virtuais associados ao servidor.

    ffuf -w wordlist.txt:FUZZ -u http://admin.academy.htb:PORT/admin/admin.php?FUZZ=key -fs xxx
    Fuzzing de parâmetros GET, injetando diferentes parâmetros na URL.

    ffuf -w wordlist.txt:FUZZ -u http://admin.academy.htb:PORT/admin/admin.php -X POST -d 'FUZZ=key' -H 'Content-Type: application/x-www-form-urlencoded' -fs xxx
    Fuzzing de parâmetros POST, enviando diferentes dados em requisições POST.

    ffuf -w ids.txt:FUZZ -u http://admin.academy.htb:PORT/admin/admin.php -X POST -d 'id=FUZZ' -H 'Content-Type: application/x-www-form-urlencoded' -fs xxx
    Realiza fuzzing de valores específicos, testando diferentes IDs em um campo de formulário POST.

Wordlists

    /opt/useful/SecLists/Discovery/Web-Content/directory-list-2.3-small.txt
    Wordlist focada em diretórios e páginas da web.

    /opt/useful/SecLists/Discovery/Web-Content/web-extensions.txt
    Wordlist de extensões de arquivos web, usada para descobrir arquivos ocultos com diferentes extensões.

    /opt/useful/SecLists/Discovery/DNS/subdomains-top1million-5000.txt
    Wordlist para descoberta de subdomínios, útil para identificar subdomínios de um domínio principal.

    /opt/useful/SecLists/Discovery/Web-Content/burp-parameter-names.txt
    Wordlist para nomes de parâmetros, geralmente utilizada em testes de injeção de parâmetros.

Misc

    sudo sh -c 'echo "SERVER_IP academy.htb" >> /etc/hosts'
    Adiciona uma entrada DNS manual no arquivo /etc/hosts, associando um IP a um nome de host.

    for i in $(seq 1 1000); do echo $i >> ids.txt; done
    Cria uma wordlist com uma sequência numérica de 1 a 1000, geralmente usada para fuzzing de IDs.

    curl http://admin.academy.htb:PORT/admin/admin.php -X POST -d 'id=key' -H 'Content-Type: application/x-www-form-urlencoded'
    Exemplo de uso do comando curl para enviar uma requisição POST com um ID e um cabeçalho específico.