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

## cURL

cURL is a command-line tool used to transfer data using various protocols. It supports HTTP, HTTPS, FTP, FTPS, and more. cURL is widely used to test web servers and troubleshoot network issues. 

cURL commands:
- `curl http://example.com`: Sends an HTTP GET request to the server.
- `curl -X POST http://example.com`: Sends an HTTP POST request to the server.
- `curl -d "param1=value1&param2=value2" http://example.com`: Sends a POST request with data.
- `curl -I http://example.com`: Sends a HEAD request to the server and displays the response headers.
- `curl -b "cookie1=value1; cookie2=value2" http://example.com`: Sends a request with cookies.
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

## HTTP Methods

HTTP defines several methods to indicate the desired action to be performed on a resource. The common HTTP methods are:
- GET: Retrieves data from the server.
- POST: Submits data to the server.
- PUT: Updates an existing resource.
- DELETE: Deletes a resource.
- HEAD: Retrieves response headers only.
- OPTIONS: Retrieves the supported HTTP methods.
- PATCH: Partially updates a resource.

Most modern web applications mainly rely on the GET and POST methods. However, any web application that utilizes REST APIs also rely on PUT and DELETE, which are used to update and delete data on the API endpoint, respectively.

## HTTP Status Codes

HTTP status codes indicate the status of the HTTP request. The common HTTP status codes are:
- 1xx: Informational
- 2xx: Success
- 3xx: Redirection
- 4xx: Client Error
- 5xx: Server Error

Common HTTP status codes:
- 200 OK: The request was successful.
- 201 Created: The resource was created.
- 204 No Content: The server successfully processed the request but did not return any content.
- 301 Moved Permanently: The resource has been moved permanently.
- 302 Found: The resource has been found.
- 400 Bad Request: The request was invalid.
- 401 Unauthorized: Authentication is required.
- 403 Forbidden: Access is forbidden.
- 404 Not Found: The resource was not found.
- 500 Internal Server Error: The server encountered an error.

## HTTP Headers

HTTP headers provide additional information about the request or response. The common HTTP headers are:

- `Content-Type`: Specifies the MIME type of the content.
- `Content-Length`: Specifies the length of the content in bytes.
- `User-Agent`: Specifies the user agent making the request.
- `Host`: Specifies the domain name of the server.
- `Accept`: Specifies the MIME types accepted by the client
- `Authorization`: Specifies the credentials for authentication.
- `Cache-Control`: Specifies caching directives.
- `Cookie`: Specifies the cookies sent by the server.
- `Location`: Specifies the URL for redirection.

### Security headers

- `Strict-Transport-Security`: Enforces the use of HTTPS.
- `Content-Security-Policy`: Specifies the content security policy. This header helps prevent cross-site scripting attacks. Instructs the browser to only load resources from specific origins.
- `X-Content-Type-Options`: Prevents browsers from MIME-sniffing a response away from the declared content-type.
- `X-Frame-Options`: Prevents clickjacking attacks by ensuring that a web page can only be displayed in a frame on the same origin as the page itself.
- `Referrer-Policy`: Controls how much referrer information should be included with requests.

## POST

The POST method is used to submit data to the server. Unlike HTTP Get, which places user parameters within the URL, in HTTP Post the data is sent in the body of the request. This has three main benefits:
1. Lack of logging: As POST requests may transfer large files, it would not be efficient for the server to log all uploaded files as part of the requested URL, as would be the case with GET requests.

2. Less Encondig Requirements: As the data is sent in the body of the request, there is no need to encode the data in the URL, which is required for GET requests. URLs are made to be shared.

3. More Data Can Be Sent: GET requests are limited by the URL length, which is typically 2048 characters. POST requests have no such limitation.
 
POST requests are commonly used to create new resources on the server. For example, when submitting a form on a website, the data is sent to the server using a POST reques.

## CRUD API

CRUD stands for Create, Read, Update, and Delete. A CRUD API is an API that provides endpoints to perform these operations on a resource. The common HTTP methods used in a CRUD API are:

- POST: Create a new resource.
- GET: Retrieve a resource.
- PUT: Update an existing resource.
- DELETE: Delete a resource.

CRUD APIs are widely used in web applications to interact with databases and perform operations on resources. For example, a blog application may have CRUD APIs to create, read, update, and delete blog posts.
