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