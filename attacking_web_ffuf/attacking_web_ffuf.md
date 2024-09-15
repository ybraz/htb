# Attacking Web Applications With FFUF

## Introduction

The term fuzzing refers to the process of sending random or semi-random data to an application in order to find vulnerabilities. Fuzzing is a powerful technique for finding bugs and vulnerabilities in software. It is often used to test the security of web applications, as well as other types of software.

We usually utilize pre-defined wordlists of commonly used terms for each type of test for web fuzzing to see if the webserver would accept them. 

Example: /opt/useful/SecLists/Discovery/Web-Content/directory-list-2.3-medium.txt

FFUF is a fast web fuzzer written in Go. It is designed to be simple to use, yet powerful enough to handle a wide range of fuzzing tasks. FFUF can be used to test web applications for a variety of vulnerabilities, including SQL injection, cross-site scripting, and command injection.

## FFUF Help

```bash
Yuri Braz@htb[/htb]$ ffuf -h

HTTP OPTIONS:
  -H               Header `"Name: Value"`, separated by colon. Multiple -H flags are accepted.
  -X               HTTP method to use (default: GET)
  -b               Cookie data `"NAME1=VALUE1; NAME2=VALUE2"` for copy as curl functionality.
  -d               POST data
  -recursion       Scan recursively. Only FUZZ keyword is supported, and URL (-u) has to end in it. (default: false)
  -recursion-depth Maximum recursion depth. (default: 0)
  -u               Target URL
...SNIP...

MATCHER OPTIONS:
  -mc              Match HTTP status codes, or "all" for everything. (default: 200,204,301,302,307,401,403)
  -ms              Match HTTP response size
...SNIP...

FILTER OPTIONS:
  -fc              Filter HTTP status codes from response. Comma separated list of codes and ranges
  -fs              Filter HTTP response size. Comma separated list of sizes and ranges
...SNIP...

INPUT OPTIONS:
...SNIP...
  -w               Wordlist file path and (optional) keyword separated by colon. eg. '/path/to/wordlist:KEYWORD'

OUTPUT OPTIONS:
  -o               Write output to file
...SNIP...

EXAMPLE USAGE:
  Fuzz file paths from wordlist.txt, match all responses but filter out those with content-size 42.
  Colored, verbose output.
    ffuf -w wordlist.txt -u https://example.org/FUZZ -mc all -fs 42 -c -v
...SNIP...
```

## Directory Fuzzing

Directory fuzzing is a common technique used to find hidden directories on a web server. FFUF can be used to perform directory fuzzing by providing a wordlist of common directory names and URLs to test.

```bash
ffuf -w /opt/useful/SecLists/Discovery/Web-Content/directory-list-2.3-medium.txt -u http://example.com/FUZZ
```

## Page Fuzzing

Before we identify pages, we must first find out what types of pages the website uses, like .html, .aspx, .php, or something else. We can use the following command to find out:

```bash
ffuf -w /opt/useful/SecLists/Discovery/Web-Content/web-extensions.txt -u http://SERVER_IP:PORT/blog/indexFUZZ
```

> Note: The wordlist we chose already contains a dot (.), so we will not have to add the dot after "index" in our fuzzing.

Once identified the extensions used by the website, we can use the following command to fuzz the pages:

```bash
ffuf -w /opt/useful/SecLists/Discovery/Web-Content/directory-list-2.3-small.txt:FUZZ -u http://SERVER_IP:PORT/blog/FUZZ.php
```

## Recursive Fuzzing

Recursive fuzzing is a technique used to find hidden directories and files on a web server by recursively following links found in the responses of the initial requests. FFUF can be used to perform recursive fuzzing by providing the `-recursion` flag.

When we scan recursively, it automatically starts another scan under any newly identified directories that may have on their pages until it has fuzzed the main website and all of its subdirectories.

```bash
ffuf -w /opt/useful/SecLists/Discovery/Web-Content/directory-list-2.3-medium.txt -u http://SERVER_IP:PORT/FUZZ -recursion -recursion-depth 1 -e .php -v
```

## Sub-domain Fuzzing

Sub-domain fuzzing is a technique used to find hidden sub-domains on a web server. FFUF can be used to perform sub-domain fuzzing by providing a wordlist of common sub-domain names and URLs to test.

```bash
ffuf -w /opt/useful/SecLists/Discovery/DNS/subdomains-top1million-5000.txt -u http://FUZZ.example.com
```

In the SecLists repo, there is a specific section for sub-domain wordlists, consisting of common words usually used for sub-domains. We can find it in SecLists/Discovery/DNS/. In our case, we would be using a shorter wordlist, which is subdomains-top1million-5000.txt. If we want to extend our scan, we can pick a larger list.

## Vhost Fuzzing

Vhost fuzzing is a technique used to find hidden virtual hosts on a web server. FFUF can be used to perform vhost fuzzing by providing a wordlist of common virtual host names and URLs to test.
- To scan for VHosts, without manually adding the entire wordlist to our /etc/hosts, we will be fuzzing HTTP headers, specifically the Host: header. To do that, we can use the -H flag to specify a header and will use the FUZZ keyword.

```bash
ffuf -w /opt/useful/SecLists/Discovery/DNS/subdomains-top1million-5000.txt -u http://academy.htb:PORT/ -H 'Host: FUZZ.academy.htb
```

The key difference between VHosts and sub-domains is that a VHost is basically a 'sub-domain' served on the same server and has the same IP, such that a single IP could be serving two or more different websites.

## Filtering Results

FFUF allows us to filter the results based on the HTTP status code and the size of the response. We can use the `-mc` flag to match HTTP status codes and the `-ms` flag to match HTTP response size.

```bash
ffuf -w /opt/useful/SecLists/Discovery/Web-Content/directory-list-2.3-medium.txt -u http://example.com/FUZZ -mc 200,301,302 -ms 42
```

We can also filter the results based on the HTTP status code and the size of the response. We can use the `-fc` flag to filter HTTP status codes and the `-fs` flag to filter HTTP response size.

```bash
ffuf -w /opt/useful/SecLists/Discovery/Web-Content/directory-list-2.3-medium.txt -u http://example.com/FUZZ -fc 404,403 -fs 42
```

## Parameter Fuzzing - GET

Parameter fuzzing is a technique used to find hidden parameters on a web server. FFUF can be used to perform parameter fuzzing by providing a wordlist of common parameter names and URLs to test.

```bash
ffuf -w /opt/useful/SecLists/Discovery/Web-Content/burp-parameter-names.txt -u http://example.com/index.php?FUZZ=test
```

## Parameter Fuzzing - POST

Parameter fuzzing can also be performed on POST requests by providing the POST data using the `-d` flag.

```bash
ffuf -w /opt/useful/SecLists/Discovery/Web-Content/common.txt -u http://example.com/index.php -X POST -d "username=admin&password=FUZZ"
```

