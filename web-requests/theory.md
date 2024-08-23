# Web Requests

## HyperText Transfer Protocol (HTTP)

HTTP is an application-level protocol used to access the World Wide Web resources. HTTP communication consists of a client and a server, where the client requests the server for a resource. The server processes the requests and returns the requested resource.
- Default port: 80
- We enter a ==Fully Qualified Domain Name (FQDN)== as a ==Uniform Resource Locator (URL)== to reach the website

### HTTP Flow

1. The client sends a request to a DNS server to resolve the domain name to an IP address.
2. The client sends an HTTP request to the server.
3. The server processes the request and sends an HTTP response back to the client.
4. The client receives the response and processes it.

### cURL

cURL is a command-line tool used to transfer data using various protocols. It supports HTTP, HTTPS, FTP, FTPS, and more. cURL is widely used to test web servers and troubleshoot network issues. 

cURL commands:
- `curl http://example.com`: Sends an HTTP GET request to the server.
- `curl -X POST http://example.com`: Sends an HTTP POST request to the server.
- `curl -I http://example.com`: Sends a HEAD request to the server and displays the response headers.
- `curl -v http://example.com`: Displays detailed information about the request and response.
- `curl -o file.txt http://example.com`: Saves the response to a file.
- `curl -u username:password http://example.com`: Sends the request with basic authentication.
- `curl -H "Content-Type: application/json" http://example.com`: Sends a request with a custom header.
- `curl -s http://example.com`: Silences the progress meter.
- `curl -h`: Displays the help menu.
- `curl -k https://example.com`: Sends an HTTPS request without verifying the SSL certificate.

## HTTPS

HTTPS is a secure version of HTTP that encrypts the data exchanged between the client and the server. HTTPS uses SSL/TLS protocols to secure the communication. HTTPS is widely used to protect sensitive information such as login credentials, payment details, and personal information.
- https://tools.ietf.org/html/rfc2818
- Websites that enforce HTTPS have a padlock icon in the address bar.
- Default port: 443 through Moved Permanently (301) redirection

### HTTPS Flow

1. The client sends an HTTPS request to the server.
2. The server responds with its SSL certificate.
3. The client verifies the certificate and generates a session key.
4. The client encrypts the session key with the server's public key and sends it to the server.
5. The server decrypts the session key using its private key.
6. The client and server communicate securely using the session key.

### SSL/TLS Handshake

The SSL/TLS handshake is a process that establishes a secure connection between the client and the server. The handshake consists of the following steps:

1. ClientHello: The client sends a message to the server with its supported SSL/TLS versions, ciphersuites, and other parameters.
2. ServerHello: The server responds with its selected SSL/TLS version, ciphersuite, and other parameters.
3. Certificate: The server sends its SSL certificate to the client.
4. Key Exchange: The client and server exchange keys to establish a secure connection.
5. Finished: The client and server exchange messages to confirm that the handshake is complete.


