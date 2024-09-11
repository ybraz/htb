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