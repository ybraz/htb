    # DNS Recon Tools

## NSLookup

O NSLookup (Name Server Lookup) é uma ferramenta de linha de comando que permite consultar servidores DNS para obter informações sobre um domínio, como endereços IP associados, registros MX (Mail Exchange), registros NS (Name Server), entre outros. Ela é amplamente usada para diagnóstico e resolução de problemas relacionados ao DNS, assim como para coleta de informações em atividades de segurança como reconhecimento (recon).

Os principais casos de uso do NSLookup incluem:
- Resolução de Domínios: Traduzir um nome de domínio em um ou mais endereços IP.
- Diagnóstico de DNS: Verificar se o DNS está respondendo corretamente e obter informações detalhadas sobre registros específicos.
- Coleta de Informações: Em pentests, o NSLookup pode ser usado para mapear a infraestrutura de um alvo, descobrindo servidores associados, registros de e-mail, etc.
- Verificação de Configuração DNS: Verificar quais servidores DNS estão configurados para um domínio e se os registros estão corretos.

Modo Interativo: Quando você executa nslookup sem parâmetros, ele entra em um modo interativo. Neste modo, você pode realizar múltiplas consultas sem precisar sair do programa.

Uma vez no modo interativo, você pode usar comandos como:
- `server <IP ou nome do servidor>`: Define qual servidor DNS será usado para as consultas.
- `set type=<tipo>`: Define o tipo de registro que você quer consultar, como A, MX, NS, etc.
- `exit`: Sai do modo interativo.

Consulta Simples: Você pode realizar consultas diretas sem entrar no modo interativo. Para isso, basta passar o domínio desejado como argumento.

```
nslookup example.com
```

Especificar Servidor DNS: Se você deseja consultar um domínio usando um servidor DNS específico, você pode fazê-lo diretamente na linha de comando.

```
nslookup example.com 8.8.8.8
```

Consulta de Registros Específicos: Você pode especificar o tipo de registro DNS que deseja consultar. Por exemplo, para consultar registros MX:

```
nslookup -query=MX example.com
```

Obter Informação sobre Servidores DNS: Para consultar quais são os servidores DNS autoritativos de um domínio, você pode usar o parâmetro -type=NS:

```
nslookup -type=NS example.com
```

## Dig

Dig é uma ferramenta de linha de comando utilizada para consultas DNS, permitindo aos usuários recuperar informações sobre registros DNS de um domínio, como registros A, MX, NS, TXT, e outros. É uma das ferramentas mais populares entre administradores de rede e profissionais de segurança para testar e depurar problemas de DNS. Além de ser poderosa e flexível, Dig é amplamente usada devido à sua simplicidade e capacidade de fornecer respostas detalhadas diretamente da linha de comando.

Dig é utilizado principalmente para:
- Consulta de Registros DNS: Obter detalhes sobre registros DNS específicos de um domínio, como registros A (endereços IP), MX (servidores de e-mail), NS (servidores de nomes), etc.
- Diagnóstico de Problemas DNS: Verificar se o DNS está funcionando corretamente, se os registros estão propagados e se os servidores DNS estão respondendo como esperado.
- Validação de Configurações DNS: Confirmar que as configurações DNS estão corretas, especialmente após alterações.
- Transferência de Zona DNS: Testar se a transferência de zona está habilitada para um domínio, o que pode expor toda a estrutura DNS de um alvo.
- Recuperação de Registros SOA: Verificar os registros Start of Authority (SOA) para obter informações sobre o servidor DNS principal e detalhes de zoneamento.

### Consulta Básica de Registros A:

Para realizar uma consulta DNS básica e obter o endereço IP (registro A) de um domínio:

```
dig example.com
```

Onde:
    example.com é o domínio alvo.

Isso retorna o(s) endereço(s) IP associado(s) ao domínio.

### Consulta de Registros Específicos:

Para consultar um tipo específico de registro DNS, como registros MX (servidores de e-mail):

```
dig example.com MX
```

Esse comando retorna os registros MX do domínio example.com.

Outros exemplos incluem:
    `dig example.com NS`: Para registros de servidores de nome (NS).
    `dig example.com TXT`: Para registros TXT, que podem incluir SPF, DKIM, etc.
    `dig example.com AAAA`: Para registros AAAA, que fornecem endereços IPv6.

### Consulta Usando um Servidor DNS Específico:

Você pode especificar um servidor DNS para realizar a consulta:

```
dig @8.8.8.8 example.com
```

Onde:
    @8.8.8.8 especifica que a consulta deve ser feita usando o servidor DNS público do Google.

### Consulta de Transferência de Zona:

Para testar se a transferência de zona está habilitada em um servidor DNS, o que pode expor toda a estrutura DNS do domínio:

```
dig @ns1.example.com example.com AXFR
```

Onde:
    AXFR é o comando para solicitar a transferência de zona.
    @ns1.example.com especifica o servidor DNS autoritativo.

### Consulta Detalhada (Verbose):

Para uma saída mais detalhada e completa, incluindo informações sobre a autoridade e o tempo de vida (TTL) dos registros:

```
dig +noall +answer example.com
```

Onde:
    +noall +answer reduz a saída para mostrar apenas a resposta essencial.

### Consulta de SOA (Start of Authority):

Para obter informações sobre o servidor DNS principal e a configuração de zoneamento:

```
dig example.com SOA
```

Esse comando retorna o registro SOA para example.com, que inclui detalhes como o servidor DNS primário, o e-mail do administrador, e os intervalos de atualização da zona.

### Pesquisa Reversa (PTR):

Para realizar uma consulta de DNS reversa e encontrar o nome de domínio associado a um endereço IP:

```
dig -x 8.8.8.8
```

Onde:
    -x especifica uma pesquisa reversa, e 8.8.8.8 é o endereço IP alvo.

## Host

Host é uma ferramenta de linha de comando usada para realizar consultas DNS, muito similar ao Dig, mas com uma interface mais simples e direta. Ela permite que você obtenha informações sobre registros DNS associados a um domínio, como registros A, MX, NS, entre outros. O comando Host é frequentemente usado para consultas rápidas de DNS, principalmente por sua simplicidade e facilidade de uso.

O comando Host é utilizado principalmente para:
- Consulta de Registros DNS: Obter informações sobre diferentes tipos de registros DNS de um domínio, como registros A, MX, NS, etc.
- Diagnóstico de DNS: Verificar se um domínio está resolvendo corretamente, se os servidores de nomes estão configurados adequadamente, entre outros problemas.
- Pesquisa Reversa (PTR): Encontrar o nome de domínio associado a um endereço IP através de uma consulta de DNS reversa.
- Transferência de Zona DNS: Testar se a transferência de zona está habilitada para um domínio, o que pode expor a estrutura DNS completa do alvo.
- Verificação de Registros SOA: Obter informações sobre o registro Start of Authority (SOA) de um domínio.

### Consulta Básica de Registros A:

Para realizar uma consulta básica e obter o endereço IP (registro A) de um domínio:

```
host example.com
```

Onde:
    example.com é o domínio alvo.

Esse comando retorna o(s) endereço(s) IP associado(s) ao domínio.

### Consulta de Registros Específicos:

Para consultar um tipo específico de registro DNS, como registros MX (servidores de e-mail):

```
host -t MX example.com
```

Onde:
    `-t MX` especifica que você deseja consultar registros MX.

Outros exemplos incluem:
    `host -t NS example.com`: Para registros de servidores de nome (NS).
    `host -t TXT example.com`: Para registros TXT.
    `host -t AAAA example.com`: Para registros AAAA (IPv6).

### Consulta Usando um Servidor DNS Específico:

Você pode especificar um servidor DNS diferente do padrão para realizar a consulta:

```
host example.com 8.8.8.8
```

Onde:
    8.8.8.8 é o servidor DNS do Google que será utilizado para a consulta.

### Transferência de Zona DNS:

Para testar se a transferência de zona está habilitada em um servidor DNS:

```
host -l example.com ns1.example.com
```

Onde:
    `-l` ativa a transferência de zona.
    `ns1.example.com` é o servidor DNS autoritativo.

### Pesquisa Reversa (PTR):

Para realizar uma consulta de DNS reversa e descobrir o nome de domínio associado a um endereço IP:

```
host 8.8.8.8
```

Esse comando retorna o nome de domínio associado ao IP 8.8.8.8.

### Verificação de Registros SOA:

Para obter informações sobre o registro SOA de um domínio:

```
host -t SOA example.com
```

Onde:
    `-t SOA` especifica que você deseja consultar o registro SOA.

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

## Fierce

Fierce é uma ferramenta de reconhecimento DNS usada principalmente para descobrir subdomínios e mapear a estrutura de rede de um alvo. Escrito em Perl, o Fierce não é exatamente uma ferramenta de "força bruta", mas sim uma ferramenta de reconhecimento que utiliza métodos inteligentes para localizar subdomínios e outros componentes da infraestrutura de um domínio. Ela é particularmente útil para encontrar servidores que não são facilmente visíveis através de simples consultas DNS, como servidores internos ou escondidos.

O Fierce é utilizado principalmente para:
- Descoberta de Subdomínios: Identificar subdomínios de um domínio alvo, o que pode revelar outros servidores e serviços associados ao domínio.
- Mapeamento de Rede: Obter uma visão geral da infraestrutura de rede de um alvo, como blocos de IP e servidores ocultos.
- Reconhecimento Passivo: Coletar informações sobre a infraestrutura do alvo sem realizar ações agressivas que possam ser facilmente detectadas.
- Identificação de Firewall ou Filtragem: Determinar a presença de firewalls ou outros mecanismos de filtragem que podem bloquear ou restringir o acesso.

### Busca de Subdomínios:

O uso básico do Fierce envolve passar o domínio alvo para realizar a descoberta de subdomínios:

```
fierce -dns example.com
```

Onde:
    -dns especifica o domínio a ser investigado.

### Especificar Servidor DNS:

Caso você queira usar um servidor DNS específico para as consultas:

```
fierce -dns example.com -dnsserver 8.8.8.8
```

Onde:
    -dnsserver define o servidor DNS a ser usado para as consultas.

### Determinar o Alcance IP de um Subdomínio:

O Fierce pode tentar descobrir o alcance de endereços IP ao redor de um determinado subdomínio, útil para mapear a rede:

```
fierce -dns example.com -range 192.168.1.0/24
```

Onde:
    -range especifica o intervalo de IPs a ser investigado.

### Output para um Arquivo:

Você pode salvar a saída da busca em um arquivo para análise posterior:

```
fierce -dns example.com > resultado.txt
```

Onde:
    > resultado.txt redireciona a saída para um arquivo.
    
### Busca de Subdomínios com Timeout:

Defina um tempo limite para consultas DNS, o que pode ser útil se você estiver enfrentando um servidor DNS lento ou se quiser evitar que o script fique preso em uma consulta:

```
fierce -dns example.com -timeout 2
```

Onde:
    -timeout define o tempo limite em segundos para cada consulta DNS.

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

## Sublist3r

Sublist3r é uma ferramenta projetada para enumerar subdomínios de um domínio utilizando diversas fontes públicas. Escrito em Python, ele agrupa resultados de múltiplas fontes como motores de busca (Google, Bing, Yahoo), APIs de serviços DNS, e outras ferramentas, para fornecer uma lista abrangente de subdomínios. O Sublist3r é particularmente útil na fase de reconhecimento de um teste de penetração, ajudando a mapear a superfície de ataque de um domínio ao identificar servidores e serviços que podem não ser imediatamente visíveis.

Sublist3r é utilizado principalmente para:
- Descoberta de Subdomínios: Identificar subdomínios associados a um domínio alvo utilizando múltiplas fontes e técnicas.
- Mapeamento de Superfície de Ataque: Obter uma visão mais completa da infraestrutura de um alvo, revelando subdomínios que podem ser potenciais pontos de entrada.
- Verificação de Subdomínios: Usar a ferramenta para verificar a presença de subdomínios conhecidos e garantir que eles ainda estão ativos ou acessíveis.

### Descoberta Básica de Subdomínios:

O uso básico do Sublist3r envolve apenas passar o domínio que você deseja explorar:

```
sublist3r -d example.com
```

Onde:
    -d especifica o domínio a ser investigado.

### Especificar Número de Threads:

Para acelerar o processo de descoberta, você pode especificar o número de threads a serem usadas:

```
sublist3r -d example.com -t 10
```

Onde:
    -t define o número de threads (por padrão, ele usa 10 threads).

### Salvar Resultados em um Arquivo:

Você pode salvar a lista de subdomínios descobertos em um arquivo para análise posterior:

```
sublist3r -d example.com -o subdomains.txt
```

Onde:
    -o especifica o nome do arquivo de saída.

### Incluir Ferramentas Específicas:

Você pode especificar quais ferramentas ou serviços de terceiros deseja usar durante a busca. Por exemplo, para usar apenas Google e Bing:

```
sublist3r -d example.com -e google,bing
```

Onde:
    -e permite especificar quais mecanismos de busca ou serviços utilizar (por padrão, o Sublist3r usa vários).

### Executar um Scan de Portas Simples:

Após descobrir subdomínios, o Sublist3r pode realizar um scan básico de portas para identificar se esses subdomínios têm serviços ativos:

```
sublist3r -d example.com -p 80,443
```

Onde:
    -p permite especificar as portas a serem escaneadas (por padrão, verifica as portas 80 e 443).

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
    
# VHost Recon Tools

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

