## DNSRecon

DNSRecon é uma ferramenta avançada de reconhecimento DNS escrita em Python, usada para realizar uma série de consultas DNS, coletando informações detalhadas sobre um domínio alvo. Ao contrário do nslookup, que é mais simples e direto, o DNSRecon é especificamente projetado para pentesters e profissionais de segurança, oferecendo um conjunto robusto de funcionalidades para explorar vulnerabilidades e obter uma visão completa da configuração DNS de um domínio.

DNSRecon é utilizado principalmente para:
- Consulta de Registros DNS: Recuperar todos os tipos de registros DNS (A, AAAA, MX, NS, SOA, TXT, etc.) de um domínio.
- Transferência de Zona: Testar se a zona DNS de um domínio pode ser transferida, o que pode expor informações sensíveis.
- Bruteforce DNS: Realizar ataques de força bruta para descobrir subdomínios.
- SRV Records Enumeration: Enumerar registros SRV para identificar serviços em execução no domínio.
- Cache Snooping: Testar se o cache de um servidor DNS pode ser acessado por um atacante.
- Verificação de DNSSEC: Testar se a configuração DNSSEC (DNS Security Extensions) está correta.

### Consulta de Registros DNS:

Você pode realizar consultas para recuperar todos os registros DNS associados a um domínio:

```
dnsrecon -d example.com -t std
```

Onde:
    -d especifica o domínio.
    -t std solicita a consulta padrão para obter todos os tipos principais de registros.

### Transferência de Zona:

Testar se uma transferência de zona está habilitada, o que poderia expor toda a estrutura DNS do domínio:

```
dnsrecon -d example.com -t axfr
```

Onde:
    -t axfr realiza o teste de transferência de zona.

### Bruteforce DNS:

Realizar um ataque de força bruta para descobrir subdomínios ocultos:

```
dnsrecon -d example.com -D subdomains.txt -t brt
```

Onde:
    -D subdomains.txt especifica o arquivo de dicionário de subdomínios.
    -t brt define o tipo de teste como bruteforce.

### Enumeração de Registros SRV:

Listar os registros SRV, que podem indicar serviços como SIP, LDAP, etc., que estão sendo executados:

```
dnsrecon -d example.com -t srv
```

Onde:
    -t srv consulta registros SRV.

### Verificação de DNSSEC:

Verificar se a configuração DNSSEC está implementada corretamente:

```
dnsrecon -d example.com -t dnssec
```

Onde:
    -t dnssec realiza a verificação do DNSSEC.

### Cache Snooping:

Testar se é possível acessar o cache de um servidor DNS, o que pode revelar quais domínios são frequentemente acessados:

```
dnsrecon -d example.com -t snoop
```

Onde:
    -t snoop executa o cache snooping.