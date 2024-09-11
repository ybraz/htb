## TheHarvester

TheHarvester é uma ferramenta projetada para realizar coleta de informações sobre domínios, utilizando fontes públicas para reunir e enumerar e-mails, subdomínios, endereços IP, e muito mais. Escrito em Python, ele utiliza motores de busca (Google, Bing, Yahoo, etc.), bem como APIs e bancos de dados públicos para extrair informações úteis. TheHarvester é uma ferramenta essencial para a fase de reconhecimento em um teste de penetração, onde o objetivo é coletar o máximo de informações possível sobre o alvo.

TheHarvester é utilizado principalmente para:
- Descoberta de Subdomínios: Identificar subdomínios associados a um domínio alvo, o que pode ajudar a mapear a infraestrutura de rede.
- Coleta de Endereços de E-mail: Buscar e-mails associados a um domínio, que podem ser utilizados em ataques de phishing ou como vetores de exploração.
- Coleta de Endereços IP: Identificar endereços IP relacionados a um domínio alvo, auxiliando no mapeamento de sua infraestrutura.
- Identificação de Alvos Potenciais: Coletar informações que podem ser utilizadas para identificar alvos específicos dentro de uma organização, como administradores de sistema, desenvolvedores, etc.
- Reconhecimento Passivo: Coletar informações sem interação direta com o alvo, utilizando apenas fontes públicas.

### Coleta Básica de Informações:

Para realizar uma busca básica de informações sobre um domínio:

```
theharvester -d example.com -l 500 -b google
```

Onde:
    -d especifica o domínio alvo.
    -l define o limite de resultados a serem retornados (neste caso, 500).
    -b especifica o mecanismo de busca a ser usado (neste exemplo, Google).

### Coletar Subdomínios e Endereços IP:

Para coletar subdomínios e endereços IP associados a um domínio:

```
theharvester -d example.com -l 500 -b bing
```

Aqui, o TheHarvester usará o Bing para descobrir subdomínios e endereços IP associados ao domínio example.com.

### Coleta de E-mails:

Para focar na coleta de e-mails associados a um domínio:

```
theharvester -d example.com -l 100 -b google -e
```

Onde:
    -e indica que o foco deve ser na coleta de e-mails.

### Usar Múltiplas Fontes:

TheHarvester permite o uso de múltiplas fontes de uma só vez:

```
theharvester -d example.com -b google,bing,yahoo
```

Esse comando realiza buscas no Google, Bing e Yahoo simultaneamente para coletar informações sobre o domínio example.com.

### Salvar Resultados em um Arquivo:

Para salvar os resultados da coleta em um arquivo:

```
theharvester -d example.com -b google -f resultado.html
```

Onde:
    -f define o nome e o formato do arquivo de saída (neste caso, um arquivo HTML).

### Verificar DNS:

TheHarvester também pode realizar verificações DNS sobre os subdomínios encontrados:

```
theharvester -d example.com -b google -v
```

Onde:
    -v ativa a verificação de DNS, validando os subdomínios encontrados.