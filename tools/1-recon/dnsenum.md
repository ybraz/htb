## DNSenum

DNSenum é uma ferramenta escrita em Perl usada para realizar um reconhecimento abrangente de DNS em um domínio. Ela é projetada para descobrir subdomínios, listar registros DNS, identificar servidores DNS, realizar transferências de zona e muito mais. DNSenum é particularmente útil em fases iniciais de um teste de penetração, onde o objetivo é mapear completamente a infraestrutura de um alvo, especialmente através da descoberta de subdomínios e servidores relacionados.

DNSenum é utilizado principalmente para:
- Descoberta de Subdomínios: Enumerar subdomínios de um domínio alvo, ajudando a mapear a superfície de ataque.
- Transferência de Zona DNS: Testar se a transferência de zona está habilitada, o que pode expor informações críticas sobre a infraestrutura de um alvo.
- Coleta de Registros DNS: Listar todos os registros DNS de um domínio, como A, AAAA, MX, NS, SOA, entre outros.
- Mapeamento de Sub-redes: Descobrir sub-redes associadas ao domínio alvo.
- Verificação de Registros de WHOIS: Obter informações sobre registros WHOIS associados ao domínio e seus servidores.

### Descoberta Básica de Subdomínios:

Para realizar uma enumeração básica de subdomínios:

```
dnsenum example.com
```

Onde:
    example.com é o domínio alvo.

### Transferência de Zona DNS:

Testar se a transferência de zona está habilitada para o domínio:

```
dnsenum --enum example.com
```

Onde:
    --enum ativa a enumeração completa, incluindo testes de transferência de zona.

### Especificar um Servidor DNS:

Você pode especificar um servidor DNS específico para realizar as consultas:

```
dnsenum --dnsserver 8.8.8.8 example.com
```

Onde:
    --dnsserver permite definir qual servidor DNS será usado.

### Descobrir Subdomínios Usando Força Bruta:

Para usar força bruta na descoberta de subdomínios, usando um arquivo de dicionário:

```
dnsenum --enum -f subdomains.txt example.com
```

Onde:
    -f subdomains.txt especifica o arquivo de dicionário a ser usado para força bruta.

### Salvando Resultados em um Arquivo:

Você pode salvar a saída da enumeração em um arquivo para análise posterior:

```
dnsenum --enum -o resultado.xml example.com
```

Onde:
    -o especifica o arquivo de saída (neste caso, um arquivo XML).

### Verificar WHOIS:

Para coletar informações WHOIS associadas ao domínio e seus servidores:

```
dnsenum --whois example.com
```

Onde:
    --whois ativa a coleta de informações WHOIS.