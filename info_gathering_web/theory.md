# Information Gathering - Web Edition

## Introduction

Web REconnaissance is the first phase of the Information Gathering process. It is the process of collecting as much information as possible about a target, for identifying possible weak points in the target network. This phase is the most important phase in the Information Gathering process, as it is the foundation of the penetration testing process. The more information you gather, the more you will be able to understand the target and the more you will be able to identify the weak points in the target network.

The primary goals of web reconnaissance are:
- Identifying Assets: Identify all the assets of the target network.
- Discovery hidden information: Locating sensitive information that might be inadverently exposed.
- Analysing the Attack Surface: Identifying the attack surface of the target network.
- Gathering Intelligence: Collecting information about the target network that can be used to identify potential vulnerabilities.

## Types of Reconnaissance

There are two types of reconnaissance:
- Passive Reconnaissance: In this type of reconnaissance, the attacker does not interact with the target network. The attacker collects information about the target network by using publicly available information.
- Active Reconnaissance: In this type of reconnaissance, the attacker interacts with the target network. The attacker collects information about the target network by using tools and techniques that interact with the target network.

In active reconnaissance, the attacker can use tools like Nmap, Nessus, and Metasploit to collect information about the target network. In passive reconnaissance, the attacker can use tools like Google, Shodan, and Censys to collect information about the target network.

In active reconnaissance, the attacker *directly interacts with the target system* to collect information about the target network. This interaction can take various forms:
- Port Scanning: The attacker scans the target network to identify open ports. Example: Using NMAP to scan the target network. Tools: NMAP, Nessus, Metasploit. Risc of Detection: High.
- Vulnerability Scanning: The attacker scans the target network to identify vulnerabilities. Example: Using Nessus to scan the target network. Tools: Nessus, OpenVAS, Nexpose. Risk of Detection: High.
- Network Mapping: The attacker maps the target network to identify the network topology. Example: Using NMAP to map the target network. Tools: NMAP, Netcat, Hping3. Risk of Detection: High.
- Banner Grabbing: The attacker grabs the banner of the target network to identify the services running on the target network. Example: Using Netcat to grab the banner of the target network. Tools: Netcat, NMAP, Hping3. Risk of Detection: Low.
- OS Finger Printing: The attacker fingerprints the target network to identify the operating system running on the target network. Example: Using NMAP to fingerprint the target network. Tools: NMAP, Xprobe2, P0f. Risk of Detection: High.
- Service Enumeration: The attacker enumerates the services running on the target network to identify the services running on the target network. Example: Using NMAP to enumerate the services running on the target network (-sV). Tools: NMAP, Netcat, Hping3. Risk of Detection: High.
- Web Spidering: The attacker spiders the target network to identify the web pages on the target network. Example: Using Burp Suite to spider the target network. Tools: Burp Suite, WebScarab, ZAP. Risk of Detection: Low.

In passive reconnaissance, the attacker *does not interact with the target system* to collect information about the target network. This interaction can take various forms:
- Search Engine Queries: The attacker uses Google to search for sensitive information about the target network. Example: Using Google to search for sensitive information about the target network. Tools: Google, Bing, Yahoo. Risk of Detection: Low.
- WHOIS Lookup: The attacker uses WHOIS to identify the owner of the target network. Example: Using WHOIS to identify the owner of the target network. Tools: WHOIS, DomainTools, WHOIS Lookup. Risk of Detection: Low.
- DNS Enumeration: The attacker enumerates the DNS records of the target network to identify the DNS records of the target network. Example: Using Dig to enumerate the DNS records of the target network. Tools: Dig, NSLookup, Host, dnsednum, fierce, dnsrecon. Risk of Detection: Low.
- Web Archive: The attacker uses the Wayback Machine to identify the historical data of the target network. Example: Using the Wayback Machine to identify the historical data of the target network. Tools: Wayback Machine, Archive.org, Web Archive. Risk of Detection: Low.
- Social Media: The attacker uses social media to identify the employees of the target network. Example: Using LinkedIn to identify the employees of the target network. Tools: LinkedIn, Facebook, Twitter. Risk of Detection: Low.
- Code Repository: The attacker uses code repositories to identify the source code of the target network. Example: Using GitHub to identify the source code of the target network. Tools: GitHub, GitLab, Bitbucket. Risk of Detection: Low.
- Email Harvesting: The attacker uses email harvesting to identify the email addresses of the target network. Example: Using theHarvester to identify the email addresses of the target network. Tools: theHarvester, Maltego, Recon-ng. Risk of Detection: Low.

## WHOIS

WHOIS is a widely used Internet record listing that identifies who owns a domain and how to get in contact with them. The Internet Corporation for Assigned Names and Numbers (ICANN) regulates domain name registration and ownership. WHOIS records have been kept since the 1980s.

Each WHOIS record typically includes the following information:
- Domain name: The domain name being registered.
- Registrar: The domain name registrar.
- Registrant contact information: The person or organization registering the domain.
- Administrative contact information: The person or organization responsible for managing the domain.
- Technical contact information: The person or organization responsible for technical matters related to the domain.
- Creation and expiration dates: The dates when the domain was created and when it expires.
- Name servers: The primary and secondary name servers for the domain.

In the 1970 Elizabeth Feinler of the Network Information Center (NIC) at SRI International created the first WHOIS tool. The WHOIS protocol was originally defined in RFC 812 in 1982. The protocol was later updated in RFC 3912 in 2004.

The formation of the Internet Corporation for Assigned Names and Numbers (ICANN) in 1998 led to the creation of a uniform WHOIS database. The database is maintained by the Internet Assigned Numbers Authority (IANA) and is available to the public on a "look-up" basis.

WHOIS data serves as a treasure trove of information for penetration testers. It can be used to identify the owner of a domain, the domain registrar, and the domain's expiration date. This information can be used to identify potential targets for social engineering attacks, phishing attacks, and other malicious activities.

## DNS Concepts

How DNS Works: 
1. User Request: A user enters "www.example.com" into their browser.
2. Recursive DNS Server: The browser sends the request to a recursive DNS server, often provided by the user's ISP. This server is responsible for resolving the domain name.
3. Checking Cache (Caching DNS Server): The recursive server checks its cache to see if it already has the IP address for "www.example.com." If it's cached, it returns the IP address to the user immediately. If not, it proceeds to query other servers.
4. Query to Root DNS Server: Since the IP is not in the cache, the recursive server queries a root DNS server. The root DNS server does not know the IP address but provides the address of the appropriate TLD DNS server, such as the ".com" TLD server.
5. Query to TLD DNS Server: The recursive server then queries the ".com" TLD DNS server, which knows the authoritative DNS server for "example.com."
6. Query to Authoritative DNS Server: The recursive server contacts the authoritative DNS server for "example.com," which holds the actual DNS records. This server responds with the IP address for "www.example.com."
7. Response Back to User: The recursive DNS server sends the IP address back to the user's browser.
8. Caching: The recursive server stores the IP address in its cache for future requests (acting as a caching DNS server).
9. Browser Connects: The browser uses the IP address to connect to the web server hosting "www.example.com," displaying the website to the user.

DNS Server Main Types:
- Recursive DNS Server: Resolves DNS queries by sequentially querying other DNS servers until it finds the authoritative answer, returning the final result to the client.
- Root DNS Server: Directs DNS queries to the appropriate TLD DNS server by responding with a list of TLD servers for a given query.
- TLD DNS Server: Manages the domains within a specific top-level domain (e.g., .com, .org) and directs queries to the appropriate authoritative DNS server.
- Authoritative DNS Server: Provides the actual DNS records for a specific domain, responding with the IP address or other DNS information.

DNS Records are used to map domain names to IP addresses. There are several types of DNS records:
- A Record: The A record maps a domain name to an IP address. Example: www.example.com -> 192.0.2.1
- CNAME Record: The CNAME record maps a domain name to another domain name. Example: www.example.com -> example.com
- MX Record: The MX record maps a domain name to a mail server. Example: example.com -> mail.example.com
- NS Record: The NS record maps a domain name to a name server. Example: example.com -> ns1.example.com
- PTR Record: The PTR record maps an IP address to a domain name. Example: 1.2.8.192.in-addr.arpa -> www.example.com
- SOA Record: The SOA record contains information about the domain name. Example: example.com -> ns1.example.com
- TXT Record: The TXT record contains text information about the domain name. Example: example.com -> "v=spf1 a mx -all"
- AAAA Record: The AAAA record maps a domain name to an IPv6 address. Example: www.example.com -> 2001:db8::1
- SRV Record: The SRV record maps a domain name to a service. Example: `_sip._`tcp.example.com -> sip.example.com
- NAPTR Record: The NAPTR record maps a domain name to a service. Example: example.com -> sip.example.com
- HINFO Record: The HINFO record contains information about the hardware and software of the domain name. Example: example.com -> "INTEL-386 LINUX"

### The hosts File

The hosts file is a text file that maps hostnames to IP addresses. It is used by the operating system to resolve hostnames before querying DNS servers. The hosts file is located at `/etc/hosts` on Unix-based systems and `C:\Windows\System32\drivers\etc\hosts` on Windows systems.

The hosts file can be used to override DNS resolution for specific hostnames. This can be useful for testing or blocking access to certain websites. Entries in the hosts file have the following format: 
```
<IP address> <hostname> [<alias>...]
```

Example:
```
127.0.0.1 localhost
192.168.1.10 devserver.local devserver
```

### Subdomains

Subdomains are prefixes added to a domain name, creating a new domain under the parent domain. Subdomains are used to organize and structure websites, services, or resources within a domain. Subdomains are created by adding a label before the domain name, separated by a dot.

Example:
- www.example.com: The subdomain "www" is used to host the main website for the domain "example.com."
- mail.example.com: The subdomain "mail" is used to host the email server for the domain "example.com."
- blog.example.com: The subdomain "blog" is used to host the blog for the domain "example.com."

Subdomain enumeration is the process of systematically identifying and listing all the subdomains associated with a domain. Subdomain enumeration is an essential part of reconnaissance, as it helps identify potential attack vectors, misconfigurations, or vulnerabilities in the target network.

From a DNS perspective, subdomains are typically represented as separate DNS records within the parent domain's zone file. Each subdomain may have its own DNS records, such as A, CNAME, MX, or TXT records, defining its configuration and mapping to IP addresses or other resources.

There are two main apporaches to subdomain enumeration:
- Passive Subdomain Enumeration: In passive subdomain enumeration, the attacker collects information about subdomains without directly interacting with the target network. This can be done using public sources, search engines, DNS records, or other online resources.
- Active Subdomain Enumeration: In active subdomain enumeration, the attacker interacts with the target network to identify subdomains. This can involve DNS queries, zone transfers, brute-forcing, or other techniques to discover subdomains.

### Key DNS Concepts

- Zone: A zone is a portion of the DNS namespace that is managed by a specific DNS server. A zone contains the DNS records for a specific domain or subdomain. The zone file, a text file that contains the DNS records for a zone, defines the resource records within this zone, providing information about the domain's DNS configuration.
- Zone Transfer: Zone transfer is the process of replicating a zone file from a primary DNS server to one or more secondary DNS servers. Zone transfers are used to synchronize DNS records across multiple servers, ensuring consistency and redundancy in the DNS infrastructure.
- DNSSEC: DNS Security Extensions (DNSSEC) is a set of security protocols that add cryptographic authentication to the DNS infrastructure. DNSSEC provides data integrity and authentication for DNS records, protecting against DNS spoofing and cache poisoning attacks.
- DNS Cache Poisoning: DNS cache poisoning is a type of attack that exploits vulnerabilities in the DNS infrastructure to inject malicious DNS records into the cache of a recursive DNS server. By poisoning the cache with fake DNS records, an attacker can redirect legitimate traffic to malicious websites, intercept sensitive information, or launch other attacks.
- DNS Spoofing: DNS spoofing is a type of attack that involves forging DNS responses to redirect legitimate traffic to malicious websites. By sending fake DNS responses with incorrect IP addresses, an attacker can trick users into visiting malicious websites, stealing sensitive information, or spreading malware.
- DNS Amplification: DNS amplification is a type of DDoS attack that exploits open DNS resolvers to overwhelm a target server with a large volume of DNS traffic. By sending spoofed DNS queries to open resolvers, an attacker can generate a massive amount of DNS responses, flooding the target server and causing a denial of service.
- DNS Tunneling: DNS tunneling is a technique that uses the DNS protocol to bypass network restrictions and exfiltrate data from a target network. By encoding data in DNS queries and responses, an attacker can establish a covert communication channel with a remote server, allowing them to transfer sensitive information without detection.
- DNS Sinkhole: A DNS sinkhole is a security mechanism that redirects malicious DNS traffic to a controlled server for analysis or blocking. By redirecting suspicious DNS queries to a sinkhole server, organizations can identify and mitigate threats, such as botnets, malware, or phishing attacks, before they reach the intended target.
- DNS Blackhole: A DNS blackhole is a security mechanism that blocks access to malicious or unwanted domains by redirecting DNS queries to a null address or sinkhole server. By blacklisting known malicious domains in the DNS configuration, organizations can prevent users from accessing harmful websites, protecting them from malware, phishing, or other threats.

## Subdomain Brute-Forcing

Subdomain brute-forcing is a technique used to discover subdomains associated with a target domain by systematically guessing and testing subdomain names. This process involves generating a list of potential subdomains and querying DNS servers to determine if they exist.

There are several tools available for subdomain brute-forcing, including:
- Sublist3r: Sublist3r is a subdomain enumeration tool that uses search engines, DNS queries, and other online sources to discover subdomains associated with a target domain.
- DNSRecon: DNSRecon is a DNS reconnaissance tool that performs subdomain enumeration, zone transfers, and other DNS-related tasks to gather information about a target domain.
- Fierce: Fierce is a DNS reconnaissance tool that locates non-contiguous IP space and performs domain enumeration to identify subdomains and other domain-related information.
- SubBrute: SubBrute is a subdomain enumeration tool that uses a wordlist to brute-force subdomains and identify potential targets for reconnaissance.
- Amass: Amass is a subdomain enumeration tool that combines DNS enumeration, web scraping, and other techniques to discover subdomains associated with a target domain.

## DNS Zone Transfer

DNS zone transfer is the process of replicating a zone file from a primary DNS server to one or more secondary DNS servers. Zone transfers are used to synchronize DNS records across multiple servers, ensuring consistency and redundancy in the DNS infrastructure.

Zone transfers are typically performed between authoritative DNS servers, allowing secondary servers to obtain a copy of the zone file from the primary server. This process helps distribute the workload, improve fault tolerance, and provide backup DNS services in case the primary server fails.

DNS zone transfers can be initiated using the following methods:
- AXFR (Full Transfer): AXFR is a DNS protocol command used to request a full zone transfer from a primary DNS server to a secondary DNS server. This command transfers all the DNS records in the zone file, providing a complete copy of the zone data.
- IXFR (Incremental Transfer): IXFR is a DNS protocol command used to request an incremental zone transfer from a primary DNS server to a secondary DNS server. This command transfers only the changes or updates to the zone file since the last transfer, reducing the amount of data transferred.

DNS zone transfer workflow:
1. Zone Transfer Request (AXFR): The secondary DNS server sends a zone transfer request to the primary DNS server, requesting a copy of the zone file.
2. SOA Record Transfer: The primary DNS server responds with the Start of Authority (SOA) record, providing information about the zone and the serial number of the zone file.
3. DNS Records Transmission: The primary DNS server sends the DNS records in the zone file to the secondary DNS server, like A, AAAA, MX, CNMAE, transferring the complete or incremental zone data.
4. Zone Transfer Completion: The secondary DNS server receives and stores the zone file, updating its DNS records to match the primary server's configuration.
5. Acknowledgment: The secondary DNS server sends an acknowledgment to the primary server, confirming the successful completion of the zone transfer.

The zone transfer vulnerability occurs when a misconfigured DNS server allows unauthorized zone transfers to external servers. This vulnerability can expose sensitive DNS records, such as internal IP addresses, hostnames, or other network information, to potential attackers.

## Virtual Hosts

Virtual hosts are used to host multiple websites on a single web server, allowing different domain names to be associated with the same IP address. Virtual hosts are commonly used to host multiple websites on a shared server, providing cost-effective hosting solutions and resource optimization.

Virtual hosts can be configured using the following methods:
- IP-Based Virtual Hosts: IP-based virtual hosts use different IP addresses to host multiple websites on the same server. Each website is associated with a unique IP address, allowing the server to differentiate between the sites based on the IP address.
- Name-Based Virtual Hosts: Name-based virtual hosts use the Host header in the HTTP request to determine which website to serve. The server matches the domain name in the Host header to the configured virtual host, allowing multiple websites to share the same IP address.
- Port-Based Virtual Hosts: Port-based virtual hosts use different port numbers to host multiple websites on the same server. Each website is associated with a unique port number, allowing the server to route traffic to the appropriate site based on the port number.
- SSL/TLS Virtual Hosts: SSL/TLS virtual hosts use different SSL certificates to host multiple secure websites on the same server. Each website is associated with a unique SSL certificate, allowing the server to provide secure connections for each site.

Virtual hosts are configured in the web server's configuration file, such as Apache's httpd.conf or Nginx's nginx.conf. Each virtual host configuration includes the following elements:
- ServerName: The domain name associated with the virtual host.
- DocumentRoot: The directory where the website files are stored.
- ErrorLog: The log file for recording errors related to the virtual host.
- CustomLog: The log file for recording access logs related to the virtual host.
- Directory: The directory-specific configuration settings for the virtual host.
- SSLCertificateFile: The path to the SSL certificate file for secure virtual hosts.
- SSLCertificateKeyFile: The path to the SSL private key file for secure virtual hosts.
- SSLCertificateChainFile: The path to the SSL certificate chain file for secure virtual hosts.
- ProxyPass: The reverse proxy configuration for forwarding requests to backend servers.

The key difference between VHosts and subdomains is that VHosts are used to host multiple websites on a single server, while subdomains are used to organize and structure websites within a domain. VHosts are configured at the web server level, while subdomains are configured at the DNS level.

If a virtual host does not have a DNS record, you can still access it by modifying the hosts file on your local machine. The hosts file maps domain names to IP addresses, allowing you to override DNS resolution and access websites hosted on virtual hosts without a public DNS record.

Websites often have subdomains that are not public and won't resolve to an IP address without the proper DNS configuration. By adding entries to the hosts file, you can access these internal subdomains directly from your local machine.
- Vhost fuzzing is a technique used to discover hidden virtual hosts on a web server by guessing and testing different domain names. This process involves generating a list of potential domain names and querying the web server to determine if they are associated with a virtual host.

### Virtual Host Discovery Tools

- DirBuster: DirBuster is a web application scanner that can be used to discover hidden directories and files on a web server. It can also be used to identify virtual hosts by brute-forcing domain names and checking for responses.
- Gobuster: Gobuster is a tool for directory and file brute-forcing that can be used to discover hidden paths and virtual hosts on a web server. It supports multiple modes, including directory, DNS, and VHost brute-forcing.
- Nikto: Nikto is a web server scanner that can be used to identify vulnerabilities and misconfigurations on a web server. It can also be used to discover virtual hosts by scanning for common hostnames and IP addresses.
- ffuf: ffuf is a fast web fuzzer that can be used to discover hidden paths and virtual hosts on a web server. It supports multiple modes, including directory, DNS, and VHost brute-forcing, making it a versatile tool for reconnaissance.

Gobuster command to brute-force virtual hosts:
```
gobuster vhost -u http://example.com -w subdomains.txt --append-domain
```

- The -u flag specifies the target URL to scan.
- The -w flag specifies the wordlist of subdomains to use for brute-forcing.
- The --append-domain flag appends the domain name to each subdomain in the wordlist.

ffuf command to brute-force virtual hosts:
```
ffuf -w subdomains.txt -u http://example.com -H "Host: FUZZ.example.com"
```

- The -w flag specifies the wordlist of subdomains to use for brute-forcing.
- The -u flag specifies the target URL to scan.
- The -H flag specifies the Host header to use for each request, replacing the FUZZ placeholder with the subdomain.

## Certificate Transparency Logs

Certificate Transparency (CT) is a security protocol that provides transparency and accountability for SSL/TLS certificates issued by Certificate Authorities (CAs). CT logs are publicly accessible repositories that store information about SSL/TLS certificates, allowing users to monitor and verify the issuance of certificates for domain names.

CT logs contain the following information about SSL/TLS certificates:
- Certificate Details: The details of the SSL/TLS certificate, including the domain name, public key, expiration date, and other metadata.
- Issuer Information: The information about the Certificate Authority (CA) that issued the certificate, including the CA's name, root certificate, and signing algorithm.
- Timestamps: The timestamps indicating when the certificate was issued, renewed, or revoked, providing a historical record of certificate events.
- Certificate Transparency Proof: The cryptographic proof that the certificate has been logged in a CT log, ensuring the integrity and authenticity of the certificate data.
- SCTs (Signed Certificate Timestamps): The signed timestamps provided by CT logs to prove that the certificate has been logged, allowing browsers to verify the certificate's transparency status.

CT Logs can be used for Web Reconnaissance in the following ways:
- Certificate Discovery: CT logs can be used to discover SSL/TLS certificates issued for a domain name, allowing users to monitor and verify the certificates associated with a website.
- Subdomain Enumeration: CT logs can be used to enumerate subdomains by searching for SSL/TLS certificates issued for different subdomains of a domain name.
- Certificate Monitoring: CT logs can be used to monitor SSL/TLS certificates for expiration dates, renewals, revocations, and other certificate events, ensuring the security and integrity of the certificates.
- Security Analysis: CT logs can be used to analyze the security posture of a website by identifying potential misconfigurations, vulnerabilities, or unauthorized certificates issued for the domain.
- Incident Response: CT logs can be used for incident response to investigate security incidents, such as unauthorized certificate issuances, domain hijacking, or other certificate-related threats.

CT logs are publicly accessible and can be queried using the following tools and resources:
- crt.sh: crt.sh is a web-based search engine for CT logs that allows users to search for SSL/TLS certificates issued for domain names and subdomains.
- Google Transparency Report: Google's Transparency Report provides information about SSL/TLS certificates logged in CT logs, allowing users to monitor certificate issuance and compliance.
- Certificate Transparency Monitoring Tools: There are various monitoring tools and services that provide real-time alerts and notifications for SSL/TLS certificates logged in CT logs, helping users track certificate events and changes.

To query CT logs for SSL/TLS certificates issued for a domain name, you can use the following command:
```
curl -s "https://crt.sh/?q=facebook.com&output=json" | jq -r '.[] | select(.name_value | contains("dev")) | .name_value' | sort -u
```

## Fingerprinting Web Servers

Web server fingerprinting is the process of identifying the type, version, and configuration of a web server by analyzing its response headers, error messages, and other characteristics. Web server fingerprinting can help identify potential vulnerabilities, misconfigurations, or security risks associated with the target server.

Web server fingerprinting techniques:
- Banner Grabbing: Banner grabbing is the process of retrieving the server banner or version information from the HTTP response headers. By analyzing the server banner, attackers can identify the type and version of the web server, helping them determine potential vulnerabilities or exploits.
- Error Messages: Error messages generated by the web server can provide valuable information about the server's configuration, software stack, or underlying technologies. By analyzing error messages, attackers can gather intelligence about the server and identify potential attack vectors.
- HTTP Headers: HTTP headers sent by the web server in the response can reveal information about the server's configuration, security features, or compliance with web standards. By analyzing HTTP headers, attackers can identify security headers, cookies, or other server-specific information.
- Probing for Specific Responses: Probing the web server for specific responses or behaviors can help identify unique characteristics or signatures associated with the server. By sending custom requests and analyzing the server's responses, attackers can gather intelligence about the server's configuration and behavior.

Web server fingerprinting tools:
- Nmap: Nmap is a network scanning tool that can be used to identify web servers, services, and open ports on a target network. Nmap's service detection feature can help identify the type and version of the web server running on a specific port.
- WhatWeb: WhatWeb is a web fingerprinting tool that can be used to identify web technologies, content management systems (CMS), and other web server characteristics. WhatWeb analyzes HTTP responses and HTML content to determine the server's fingerprint.
- Wappalyzer: Wappalyzer is a browser extension that can be used to identify web technologies, CMS, e-commerce platforms, and other web server characteristics. Wappalyzer analyzes the web page's content and scripts to determine the server's fingerprint.
- BuiltWith: BuiltWith is a web technology profiler that can be used to identify web technologies, frameworks, and libraries used by a website. BuiltWith analyzes the website's code, scripts, and resources to determine the server's fingerprint.
- wafw00f: wafw00f is a web application firewall (WAF) detection tool that can be used to identify WAFs, security plugins, and protection mechanisms used by a web server. wafw00f analyzes HTTP responses and headers to determine the server's fingerprint.
- Netcraft: Netcraft is an internet security and research company that provides tools and services for web server fingerprinting, phishing detection, and security analysis. Netcraft's Web Server Survey can help identify the type and version of web servers running on the internet.

### Nikto

Nikto is a web server scanner that can be used to identify vulnerabilities, misconfigurations, and security risks associated with web servers. Nikto performs comprehensive security scans of web servers, analyzing HTTP responses, headers, and error messages to identify potential issues.

Nikto features:
- Vulnerability Scanning: Nikto scans web servers for known vulnerabilities, misconfigurations, and security weaknesses that could be exploited by attackers. It checks for common vulnerabilities, such as outdated software, default credentials, and insecure configurations.
- Web Server Fingerprinting: Nikto identifies the type, version, and configuration of web servers by analyzing HTTP responses, headers, and error messages. It provides detailed information about the server's fingerprint, helping users understand the server's characteristics and potential risks.
- Security Checks: Nikto performs security checks on web servers to identify security headers, cookies, and other server-specific information that could impact the server's security posture. It analyzes the server's response to determine compliance with web standards and best practices.

Nikto command to scan a web server:
```
nikto -h http://example.com -Tuning b
```
- The -h flag specifies the target URL to scan.
- The -Tuning flag specifies the scan tuning level, with level b being the most comprehensive and aggressive.

Nikto command to scan a web server and save the output to a file:
```
nikto -h http://example.com -o nikto_output.txt
```
- The -o flag specifies the output file to save the scan results.

Nikto command to scan a web server and perform a comprehensive scan:
```
nikto -h http://example.com -o nikto_output.txt -C all
```
- The -C flag specifies the comprehensive scan mode, enabling all security checks and vulnerability tests.

Nikto command to scan a web server and perform a stealthy scan:
```
nikto -h http://example.com -o nikto_output.txt -Tuning 1
```
- The -Tuning flag specifies the scan tuning level, with level 1 being the most stealthy and level 3 being the most aggressive.


## DNS Security Extensions (DNSSEC)

DNS Security Extensions (DNSSEC) is a set of security protocols that add cryptographic authentication to the DNS infrastructure. DNSSEC provides data integrity and authentication for DNS records, protecting against DNS spoofing and cache poisoning attacks.

DNSSEC uses digital signatures to verify the authenticity of DNS records and ensure that the data has not been tampered with during transmission. By signing DNS records with cryptographic keys, DNSSEC helps prevent DNS spoofing, cache poisoning, and other DNS-related attacks.

DNSSEC provides the following security features:
- Data Integrity: DNSSEC ensures the integrity of DNS records by signing them with digital signatures, allowing resolvers to verify the authenticity of the data.
- Data Authentication: DNSSEC provides authentication for DNS records, allowing resolvers to validate the source of the data and prevent DNS spoofing attacks.
- Data Confidentiality: DNSSEC does not provide confidentiality for DNS data, as the focus is on data integrity and authentication rather than encryption.
- Key Management: DNSSEC uses cryptographic keys to sign and verify DNS records, requiring proper key management practices to ensure the security of the DNS infrastructure.
- Trust Chain: DNSSEC establishes a trust chain of cryptographic signatures from the root DNS zone to the authoritative DNS server, allowing resolvers to validate the authenticity of DNS records.
- Resource Records: DNSSEC introduces new resource record types, such as RRSIG, DNSKEY, NSEC, and DS records, to support cryptographic signing and verification of DNS data.
- Validation Process: DNS resolvers perform DNSSEC validation by verifying the digital signatures of DNS records, checking the chain of trust, and validating the cryptographic keys used in the process.

DNSSEC deployment involves the following steps:
1. Key Generation: Generate cryptographic keys for signing DNS records and establishing trust in the DNS infrastructure.
2. Key Signing: Sign DNS records with cryptographic keys to provide data integrity and authentication for the DNS data.
3. Zone Signing: Sign the entire DNS zone file with digital signatures to protect the zone data from tampering and ensure the authenticity of the records.
4. Key Distribution: Distribute the public keys used for DNSSEC signing to resolvers and clients to enable validation of DNS records.
5. Trust Anchor Configuration: Configure trust anchors in resolvers to establish a chain of trust from the root DNS zone to the authoritative DNS server.
6. Validation Process: Resolvers perform DNSSEC validation by verifying the digital signatures of DNS records, checking the chain of trust, and validating the cryptographic keys.

## DNS Enumeration

DNS enumeration is the process of locating all the DNS servers and their corresponding records for an organization. DNS enumeration is an important part of the information gathering process, as it can provide valuable information about the target network.

DNS enumeration can be performed using various tools and techniques, including:
- NSLookup: NSLookup is a command-line tool used to query DNS servers for information about domain names and IP addresses, making it helpful for basic DNS troubleshooting.
Example: nslookup example.com
- Dig: Dig (Domain Information Groper) is a command-line tool that queries DNS servers to retrieve detailed DNS records, such as A, MX, and CNAME records, often used for in-depth DNS diagnostics.
Example: dig example.com
- Host: Host is a simple command-line utility for performing DNS lookups, returning the IP addresses associated with a domain name or vice versa, and other DNS records.
Example: host example.com
- DNSRecon: DNSRecon is a tool used for DNS enumeration, gathering DNS records, performing zone transfers, and other DNS-related reconnaissance, commonly used in penetration testing.
Example: dnsrecon -d example.com
- Fierce: Fierce is a DNS reconnaissance tool used to locate non-contiguous IP space and perform domain enumeration, helping to identify subdomains and other domain-related information.
Example: fierce --domain example.com
- DNSenum: DNSenum is a tool for DNS enumeration, which gathers information such as subdomains, IP addresses, and other DNS records through various queries and brute-forcing.
Example: dnsenum example.com
- Recon-ng: Recon-ng is a full-featured web reconnaissance framework with modules for gathering open-source intelligence (OSINT) on targets, including DNS information and other domain-related data.
Example: recon-ng --module domains-hosts example.com
- Sublist3r: Sublist3r is a tool designed to enumerate subdomains of websites using search engines, DNS queries, and other online sources, useful for penetration testing and reconnaissance.
Example: sublist3r -d example.com
- TheHarvester: TheHarvester is an open-source intelligence gathering tool that collects information such as email addresses, subdomains, and IPs from public sources, often used for reconnaissance.
Example: theHarvester -d example.com -b google
- Shodan: Shodan is a search engine for internet-connected devices, often used to find information about servers, routers, and IoT devices that are publicly accessible, making it a valuable tool for security assessments.
Example: shodan search "apache" "country:US"

### The Domain Information Groper (Dig)

Dig (Domain Information Groper) is a command-line tool used to query DNS servers for information about domain names and IP addresses. Dig is commonly used for troubleshooting DNS-related issues, retrieving detailed DNS records, and performing DNS reconnaissance.

Basic Dig Commands:
- Query A Record: dig example.com
- Query MX Record: dig example.com MX
- Query NS Record: dig example.com NS
- Query CNAME Record: dig example.com CNAME
- Query SOA Record: dig example.com SOA
- Query TXT Record: dig example.com TXT
- Query AAAA Record: dig example.com AAAA
- Query PTR Record: dig -x 192.168.1.1
- Query All Records: dig example.com ANY

## Crawling

Crawling, often called spidering, is the automated process of systematically browsing the World Wide Web. Similar to how a spider crawls a web to collect information, a web crawler navigates the internet to index and retrieve data from websites.

The operation of a web crawler involves the following steps:
1. Seed URLs: The web crawler starts with a list of seed URLs, which are the initial web pages to be crawled.
2. URL Extraction: The web crawler extracts links from the seed URLs and adds them to a queue for further processing.
3. URL Processing: The web crawler retrieves the next URL from the queue and fetches the corresponding web page.
4. Content Extraction: The web crawler extracts content, links, and metadata from the web page for indexing and analysis.
5. Link Analysis: The web crawler follows the links on the web page, adding new URLs to the queue for crawling.
6. Indexing: The web crawler indexes the content and metadata of the web page, storing the information in a database or search index.
7. Repeat: The web crawler continues crawling the web, following links, extracting content, and indexing data from multiple websites.

Breadth-First Crawling: Breadth-first crawling is a web crawling strategy that explores the web in a broad and shallow manner, visiting multiple websites at the same depth level before moving to the next level. Breadth-first crawling is useful for discovering new websites and collecting a wide range of data from the web.

Depth-First Crawling: Depth-first crawling is a web crawling strategy that explores the web in a narrow and deep manner, visiting websites at the same depth level before moving to the next level. Depth-first crawling is useful for exploring a specific topic or following a specific path through the web.

### robots.txt

The robots.txt file is a text file placed in the root directory of a website to instruct web crawlers on which pages to crawl or avoid. The robots.txt file contains directives, such as User-agent and Disallow, to control the behavior of web crawlers when accessing the website.
- It adheres to the Robots Exclusion Protocol (REP), a standard for controlling web crawler behavior.

Example robots.txt file:
```
User-agent: *
Disallow: /private/
Crawl-delay: 10
Sitemap: https://example.com/sitemap.xml
```

- User-agent: Specifies the web crawler or user agent to which the directive applies. The wildcard (*) represents all web crawlers.
- Disallow: Specifies the URLs or directories that the web crawler should not access. The Disallow directive can be used to block specific paths or files from being crawled.
- Crawl-delay: Specifies the delay in seconds between successive requests to the website. The Crawl-delay directive can be used to limit the crawling speed of web crawlers.
- Sitemap: Specifies the location of the XML sitemap for the website. The Sitemap directive provides a reference to the sitemap file containing URLs to be crawled.

For web reconnaissance, the robots.txt file can provide valuable information about the website's structure, directories, and access restrictions. By analyzing the robots.txt file, attackers can identify sensitive directories, hidden paths, or other information that may be useful for reconnaissance or exploitation.

### Well-Knowb URIs

The .well-known standard, defined in RFC 8615, provides a way for web servers to expose metadata and resources in a well-known location on the server. The .well-known directory is used to store files and resources that are commonly accessed by clients, such as security policies, certificates, and other metadata.

Common .well-known URIs:
- /.well-known/acme-challenge: Used for the Automatic Certificate Management Environment (ACME) protocol to verify domain ownership during certificate issuance.
- /.well-known/apple-app-site-association: Used by iOS apps to associate web domains with app content for universal links.
- /.well-known/security.txt: Used to provide security contact information for reporting security vulnerabilities.
- /.well-known/robots.txt: Used to expose the robots.txt file for controlling web crawler behavior.
- /.well-known/captcha: Used to store CAPTCHA challenges and responses for verifying user interactions.
- /.well-known/openid-configuration: Used to expose OpenID Connect configuration information for authentication and authorization.

The Internet Assigned Numbers Authority (IANA) maintains a registry of well-known URIs, providing a standardized way to access common resources and metadata on the web.

## OSINT

Open-source intelligence (OSINT) is the practice of collecting and analyzing publicly available information from open sources to gather intelligence and insights about a target. OSINT sources include websites, social media, public records, news articles, and other publicly accessible data.

At its core, search engine discovery leverages the immense power of search algorithms to find information about a target. By using search engines like Google, Bing, or DuckDuckGo, analysts can uncover a wealth of information about a target, including websites, social media profiles, news articles, and other online resources.

Search Engine Operators:
- site: Limits search results to a specific website or domain. Example: site:example.com
- intitle: Searches for specific keywords in the title of a webpage. Example: intitle:example
- inurl: Searches for specific keywords in the URL of a webpage. Example: inurl:example
- filetype: Limits search results to specific file types, such as PDF, DOC, or XLS. Example: filetype:pdf
- link: Finds webpages that link to a specific URL. Example: link:example.com
- cache: Retrieves the cached version of a webpage stored by the search engine. Example: cache:example.com
- related: Finds websites related to a specific URL or domain. Example: related:example.com
- info: Provides information about a specific URL or domain. Example: info:example.com
- define: Retrieves the definition of a specific term or keyword. Example: define:example
- intext: Searches for specific keywords within the text of a webpage. Example: intext:example
- inbody: Searches for specific keywords within the body of a webpage. Example: inbody:example
- AND: Requires both terms to be present in the search results. Example: term1 AND term2
- OR: Requires either term to be present in the search results. Example: term1 OR term2
- NOT: Excludes a term from the search results. Example: term1 NOT term2

Google Dorking: Google Dorking is the practice of using advanced search operators to find specific information on Google. By using Google Dorks, analysts can uncover sensitive data, vulnerabilities, or misconfigurations on the web. 

Here are some common examples of Google Dorks, for more examples, refer to the Google Hacking Database (www.exploit-db.com/google-hacking-database):
- Finding Login Pages: site:example.com inurl:login / site:example.com (inurl:login OR inurl:admin)
- Identifying Exposed Files: site:example.com filetype:pdf / site:example.com (filetype:pdf OR filetype:doc)
- Uncovering Configuration Files: site:example.com intitle:"index of" / site:example.com (ext:conf OR ext:cnf)
- Locating Database Backups: site:example.com inurl:backup / site:example.com filetype:sql

## Web Archives

Web archives are repositories that store historical snapshots of websites, allowing users to access and view past versions of web pages. Web archives preserve the content, structure, and functionality of websites over time, providing a valuable resource for research, analysis, and digital preservation. It can be accessed using the Wayback Machine (archive.org), that has been archiving web pages since 1996.

The frequency of archiving depends on the website's popularity and update frequency. Popular websites are archived more frequently, while less popular sites may have fewer snapshots. The Wayback Machine allows users to browse archived web pages by entering the URL of the website and selecting a specific date or time period to view.

Why the Wayback Machine is useful for reconnaissance:
- Uncovering Hidden Assets and Vulnerabilities: The Wayback Machine can reveal hidden directories, files, or resources that are no longer accessible on the live website, helping identify potential attack vectors or misconfigurations.
- Tracking Changes and Identifying Patterns: The Wayback Machine allows users to track changes in website content, design, or functionality over time, helping identify trends, patterns, or historical events associated with the site.
- Gathering Intelligence: The Wayback Machine provides historical data about websites, including past versions, updates, and modifications, helping gather intelligence about the target's history, activities, or evolution.
- Stealthy Reconnaissance: The Wayback Machine allows users to perform reconnaissance on websites without directly accessing the live site, reducing the risk of detection or alerting the target to the reconnaissance activities.


