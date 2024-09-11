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