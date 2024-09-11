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