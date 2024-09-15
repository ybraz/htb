# Server-Side Attacks

## Introduction

Server-side attacks are attacks that are performed on the server side of a client-server system. These attacks are performed by exploiting vulnerabilities in the server software or the server configuration. Server-side attacks can be used to gain unauthorized access to the server, steal sensitive information, or disrupt the server's operation.

## Types of Server-Side Attacks

There are several types of server-side attacks that can be used to compromise a server. Some of the most common types of server-side attacks include:

1. Server-Side Request Forgery (SSRF): SSRF is an attack that allows an attacker to send a request from the server to another server on the internal network or the internet. This vulnerability often occurs when an application makes HTTP requests to other servers based on user input. Successful exploitation of SSRF can enable an attacker to access internal systems, bypass firewalls, and retrieve sensitive information.

2. Server-Side Template Injection (SSTI): SSTI is an attack that allows an attacker to inject malicious code into a server-side template. This attack can be used to execute arbitrary code on the server and gain unauthorized access to the server.

3. Server-Side Include (SSI) Injection: SSI injection is an attack that allows an attacker to inject malicious code into a server-side include file. SSI directives instruct the webserver to include additional content dynamically. SSI injection can lead to data leakage or even remote code execution.

4. XSLT Server-Suite Transformation (XSLT SST) Attack: XSLT (Extensible Stylesheet Language Transformations) server-side injection is a vulnerability that arises when an attacker can manipulate XSLT transformations performed on the server. XSLT is a language used to transform XML documents into other formats, such as HTML, and is commonly employed in web applications to generate content dynamically. In the context of XSLT server-side injection, attackers exploit weaknesses in how XSLT transformations are handled, allowing them to inject and execute arbitrary code on the server.

## SSRF 

Suppose a web server fetches remote resources based on user input. In that case, an attacker might be able to coerce the server into making requests to arbitrary URLs supplied by the attacker, i.e., the web server is vulnerable to SSRF.

To exploit SSRF, an attacker can provide a malicious URL as input to the vulnerable application. The application will then make a request to the malicious URL, allowing the attacker to access internal systems, bypass firewalls, and retrieve sensitive information.

Example:

```bash
ffuf -w ../SecLists/Discovery/Web-Content/raft-small-words.txt -u http://10.129.87.11/index.php -X POST -H "Content-Type: application/x-www-form-urlencoded" -d "dateserver=http://dateserver.htb/FUZZ.php&date=2024-01-01" -fr "Server at dateserver.htb Port 80"
```

In many real-world SSRF vulnerabilities, the response is not directly displayed to us. These instances are called *blind SSRF vulnerabilities* because we cannot see the response. In such cases, we can use the Burp Collaborator to check if the server is making requests to the malicious URL. Therefore, the impact of blind SSRF vulnerabilities is generally significantly lower due to the severely restricted exploitation vectors.

