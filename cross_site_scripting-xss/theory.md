# Cross-Site Scripting (XSS)

## What is XSS?

Cross-Site Scripting (XSS) is a security vulnerability that allows an attacker to inject malicious scripts into web pages viewed by other users. The attacker can use XSS to steal sensitive information, deface websites, redirect users to malicious websites, and perform other malicious activities.

XSS vulnerabilities take advantage of a flaw in user input sanitization to "write" JavaScript code to the page and execute it on the client side, leading to several types of attacks.

When a vulnerable web application does not properly sanitize user input, a malicious user can inject extra JavaScript code in an input field (e.g., comment/reply), so once another user views the same page, they unknowingly execute the malicious JavaScript code.

> XSS vulnerabilities are solely executed on the client-side and hence do not directly affect the back-end server.

A basic example of an XSS attack is having the target user unwittingly send their session cookie to the attacker's web server. Another example is having the target's browser execute API calls that lead to a malicious action, like changing the user's password to a password of the attacker's choosing. 

## Types of XSS

There are three main types of XSS attacks:

1. **Stored XSS**: The attacker injects a script into a web application's database. When another user visits the page, the script is executed in the context of the victim's session.

2. **Reflected XSS**: The attacker injects a script into a URL that is reflected back to the user. The user clicks on the URL, and the script is executed in the context of the user's session.

3. **DOM-based XSS**: The attacker injects a script into the DOM (Document Object Model) of the web page. The script is executed in the context of the victim's session when the page is loaded  (e.g., through client-side HTTP parameters or anchor tags).

## Stored XSS

Stored XSS, also known as persistent XSS, is a type of XSS attack where the malicious script is stored on the target server (e.g., in a database) and executed when a user visits the affected page.

If our injected XSS payload gets stored in the back-end database and retrieved upon visiting the page, this means that our XSS attack is persistent and may affect any user that visits the page.

> This makes this type of XSS attack more dangerous than reflected XSS, as it can affect multiple users.

## Reflected XSS

Reflected XSS, also known as non-persistent XSS, is a type of XSS attack where the malicious script is reflected off the web server and executed in the context of the victim's session. Reflected XSS vulnerabilities **occur when our input reaches the back-end server and gets returned to us without being filtered or sanitized**.

In this type of attack, the attacker crafts a malicious URL containing the XSS payload and sends it to the victim. The victim clicks on the URL, and the script is executed in the context of the victim's session.

> Reflected XSS attacks are usually short-lived and only affect users who click on the malicious URL, because of this they are called Non-Persistent XSS attacks.

## DOM-based XSS

DOM-based XSS, also known as client-side XSS, is a type of XSS attack where the malicious script is injected into the DOM (Document Object Model) of the web page. The script is executed in the context of the victim's session when the page is loaded.

In this type of attack, the attacker injects a script that is executed by the victim's browser when the page is loaded. The script can access the DOM and perform actions on the page, such as stealing cookies or redirecting the user to a malicious website.

Some of the commonly used JavaScript functions to write to DOM objects are:
- document.write()
- DOM.innerHTML
- DOM.outerHTML

> DOM-based XSS attacks are executed on the client-side and do not require the server to be involved in the attack.

## Tools for Detecting XSS

There are several tools available for detecting XSS vulnerabilities in web applications:

1. **Burp Suite**: A popular web application security testing tool that includes a scanner for detecting XSS vulnerabilities.

2. **OWASP ZAP (Zed Attack Proxy)**: An open-source web application security scanner that includes a scanner for detecting XSS vulnerabilities.

3. **Netsparker**: A web application security scanner that includes a scanner for detecting XSS vulnerabilities.

4. **Acunetix**: A web application security scanner that includes a scanner for detecting XSS vulnerabilities.

5. **XSS Strike**: A tool for detecting and exploiting XSS vulnerabilities in web applications. https://github.com/s0md3v/XSStrike.git

## Prevention of XSS

To prevent XSS attacks, web developers should follow best practices for input validation and output encoding:

1. **Input Validation**: Validate and sanitize all user input to prevent malicious scripts from being injected into the application.

2. **Output Encoding**: Encode all output data to prevent XSS attacks. Use encoding functions like `htmlspecialchars()` in PHP, `encodeURIComponent()` in JavaScript, and `escape()` in Java.

3. **Content Security Policy (CSP)**: Implement a Content Security Policy to restrict the sources from which scripts can be loaded on a web page.

4. **HTTPOnly Cookies**: Use the `HttpOnly` flag on cookies to prevent client-side scripts from accessing them.

5. **X-XSS-Protection Header**: Set the `X-XSS-Protection` header to enable the XSS filter in the browser.

6. **X-Content-Type-Options Header**: Set the `X-Content-Type-Options` header to prevent MIME-sniffing attacks.

7. **X-Frame-Options Header**: Set the `X-Frame-Options` header to prevent clickjacking attacks.

8. **Use Libraries**: Use secure libraries and frameworks that provide built-in protection against XSS attacks.

By following these best practices, web developers can reduce the risk of XSS vulnerabilities in their web applications and protect users from malicious attacks.