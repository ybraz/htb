# Session Security

## Introduction

A user session can be defined as a sequence of requests originating from the same client and the associated responses during a specific time period. Modern web applications need to maintain user sessions to keep track of information and status about each user. User sessions facilitate the assignment of access or authorization rights, localization settings, etc., while users interact with an application, pre, and post-authentication.

HTTP is a stateless communication protocol, and as such, any request-response transaction is unrelated to other transactions. This means that each request should carry all needed information for the server to act upon it appropriately, and the session state resides on the client's side only.

For the reason above, web applications utilize cookies, URL parameters, URL arguments (on GET requests), body arguments (on POST requests), and other proprietary solutions for session tracking and management purposes.

A unique session identifier (Session ID) or token is the basis upon which user sessions are generated and distinguished.

We should clarify that if an attacker obtains a session identifier, this can result in session hijacking, where the attacker can essentially impersonate the victim in the web application.

A session identifier's security level depends on its:
- Validity Scope (a secure session identifier should be valid for one session only)
- Randomness (a secure session identifier should be generated through a robust random number/string generation algorithm so that it cannot be predicted)
- Validity Time (a secure session identifier should expire after a certain amount of time)

There are different types of session attacks, such as:
- Session Fixation: The attacker sets the session identifier for the victim before the victim logs in.
- Session Hijacking: The attacker steals the session identifier from the victim.
- XSS (Cross-Site Scripting): The attacker steals the session identifier using a cross-site scripting attack.
- CSFR (Cross-Site Request Forgery): Cross-Site Request Forgery (CSRF or XSRF) is an attack that forces an end-user to execute inadvertent actions on a web application in which they are currently authenticated. This attack is usually mounted with the help of attacker-crafted web pages that the victim must visit or interact with. These web pages contain malicious requests that essentially inherit the identity and privileges of the victim to perform an undesired function on the victim's behalf.
- Open Redirect: The attacker steals the session identifier using an open redirect attack.

```bash
ybraz@htb[/htb]$ IP=ENTER SPAWNED TARGET IP HERE
ybraz@htb[/htb]$ printf "%s\t%s\n\n" "$IP" "xss.htb.net csrf.htb.net oredirect.htb.net minilab.htb.net" | sudo tee -a /etc/hosts
```

## Session Hijacking

In session hijacking attacks, the attacker takes advantage of insecure session identifiers, finds a way to obtain them, and uses them to authenticate to the server and impersonate the victim.

An attacker can obtain a victim's session identifier using several methods, with the most common being:
- Passive Traffic Sniffing
- Cross-Site Scripting (XSS)
- Browser history or log-diving
- Read access to a database containing session information

## Session Fixation

In session fixation attacks, the attacker sets the session identifier for the victim before the victim logs in. The attacker can set the session identifier in the victim's browser by sending a link to the victim, which contains the session identifier.

Such bugs usually occur when session identifiers (such as cookies) are being accepted from URL Query Strings or Post Data (more on that in a bit).

Session Fixation attacks are usually mounted in three stages:
1. Attacker manages to obtain a valid session identifier
2. Attacker manages to fixate a valid session identifier
3. Attacker tricks the victim into establishing a session using the abovementioned session identifier

Session Identifier (Session ID): This identifier is simply a value that represents a session on the server. It can be assigned to anyone visiting the website, even if they haven’t logged in yet. So, the attacker can obtain a valid session ID, but they still don’t have access to the victim’s account, as this session ID is not authenticated.

Authenticated Session: For a session to be useful to the attacker (i.e., for them to access the victim’s information), the session must be associated with the victim's login. This only happens when the victim actually logs into the site, linking the session ID to their account.

## Cross-Site Scripting (XSS)

Cross-Site Scripting (XSS) is a type of security vulnerability that allows attackers to inject malicious scripts into web pages viewed by other users. The attacker can use XSS to steal session identifiers from other users.

For a Cross-Site Scripting (XSS) attack to result in session cookie leakage, the following requirements must be fulfilled:
- Session cookies should be carried in all HTTP requests
- Session cookies should be accessible by JavaScript code (the HTTPOnly attribute should be missing)

## Cross-Site Request Forgery (CSRF)

Cross-Site Request Forgery (CSRF or XSRF) is an attack that forces an end-user to execute inadvertent actions on a web application in which they are currently authenticated. This attack is usually mounted with the help of attacker-crafted web pages that the victim must visit or interact with, leveraging the lack of anti-CSRF security mechanisms. These web pages contain malicious requests that essentially inherit the identity and privileges of the victim to perform an undesired function on the victim's behalf. CSRF attacks generally target functions that cause a state change on the server but can also be used to access sensitive data.

