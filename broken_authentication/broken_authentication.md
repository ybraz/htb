# Broken Authentication

## Introduction

Authentication is defined as "The process of verifying a claim that a system entity or system resource has a certain attribute value" in RFC 4949. 

Authentication is a critical part of any application. It is the process of verifying the identity of a user or a system. It is the process of confirming that the user is who they claim to be.

Authentication:
- Determines whether users are who they claim to be.
- Challenges the user to validate credentials (for example, through a password, a pin, a smart card, or a biometric device).
- Usually done before authorization.
- It usually needs the user's login details
- Generally, transmits info through an ID token 

Authorization:
- Determines what users can and cannot access.
- Verifies whether access is allowed throught policies and rules.
- Usually done after successful authentication.
- While it needs user's privilege or security levels.
- Generally, transmits info through an access token

Information technology systems can implement different authentication methods. Typically, they can be divided into the following three major categories:

    Knowledge-based authentication
    Ownership-based authentication
    Inherence-based authentication

**Knowledge:** Authentication based on knowledge factors relies on something that the user knows to prove their identity. The user provides information such as passwords, passphrases, PINs, or answers to security questions.
Ownership

**Ownership:** Authentication based on ownership factors relies on something the user possesses. The user proves their identity by proving the ownership of a physical object or device, such as ID cards, security tokens, or smartphones with authentication apps. 
Inherence

**Inherence:** Lastly, authentication based on inherence factors relies on something the user is or does. This includes biometric factors such as fingerprints, facial patterns, and voice recognition, or signatures. Biometric authentication is highly effective since biometric traits are inherently tied to an individual user.

Single-factor authentication relies solely on a single methods. For instance, password authentication solely relies on knowledge of the password. As such, it is a single-factor authentication method.

On the other hand, multi-factor authentication (MFA) involves multiple authentication methods. For instance, if a web application requires a password and a time-based one-time password (TOTP), it relies on knowledge of the password and ownership of the TOTP device for authentication. In the particular case when exactly two factors are required, MFA is commonly referred to as 2-factor authentication (2FA).

## Enumerating Users

The first step in the authentication process is to enumerate the users. This involves identifying the users who are allowed to access the system. The system should maintain a list of authorized users and their corresponding credentials. The credentials can be in the form of usernames, passwords, or other authentication tokens.

Web developers frequently overlook user enumeration vectors, assuming that information such as usernames is not confidential. However, usernames can be considered confidential if they are the primary identifier required for authentication in web applications.

Protection against username enumeration attacks can have an impact on user experience. A web application revealing whether a username exists may help a legitimate user identify that they failed to type their username correctly.

To obtain a list of valid users, an attacker typically requires a wordlist of usernames to test. Usernames are often far less complicated than passwords. They rarely contain special characters when they are not email addresses. A list of common users allows an attacker to narrow the scope of a brute-force attack or carry out targeted attacks (leveraging OSINT) against support employees or users.

If a web application reveals whether a username exists, an attacker can use this information to identify valid usernames. This information can be used to launch a password spraying attack, where a small number of common passwords are tested against a large number of usernames.

Let us exploit this difference in error messages returned and use SecLists's wordlist xato-net-10-million-usernames.txt to enumerate valid users with ffuf. We can specify the wordlist with the -w parameter, the POST data with the -d parameter, and the keyword FUZZ in the username to fuzz valid users. Finally, we can filter out invalid users by removing responses containing the string Unknown user:

'''bash
$ ffuf -w /opt/useful/SecLists/Usernames/xato-net-10-million-usernames.txt -u http://172.17.0.2/index.php -X POST -H "Content-Type: application/x-www-form-urlencoded" -d "username=FUZZ&password=invalid" -fr "Unknown user"

<SNIP>

[Status: 200, Size: 3271, Words: 754, Lines: 103, Duration: 310ms]
    * FUZZ: consuelo
'''

## Brute-Forcing Passwords

Once the attacker has enumerated valid users, the next step is to brute-force the passwords. Brute-forcing is a trial-and-error method used to obtain information such as a user password or personal identification number (PIN). In a brute-force attack, the attacker systematically checks all possible keys or passwords until the correct one is found.

Passwords remain one of the most common online authentication methods, yet they are plagued with many issues. One prominent issue is password reuse, where individuals use the same password across multiple accounts. This practice poses a significant security risk because if one account is compromised, attackers can potentially gain access to other accounts with the same credentials.

Another issue is weak passwords. Weak passwords are easy to guess or crack using automated tools. Passwords such as "password,", "123456," and "qwerty" are commonly used and easily guessed. Passwords that are too short, lack complexity, or are based on dictionary words are also considered weak. 

To brute-force passwords, attackers typically use wordlists or password dictionaries. These wordlists contain common passwords, dictionary words, and leaked passwords from data breaches. Attackers can also generate custom wordlists based on information gathered from social media, OSINT, or password policies.

Let us use the rockyou.txt wordlist to brute-force the password for the user consuelo. We can specify the wordlist with the -w parameter, the POST data with the -d parameter, and the keyword FUZZ in the password to fuzz valid passwords. Finally, we can filter out invalid passwords by removing responses containing the string Invalid password:

'''bash
$ ffuf -w /opt/useful/SecLists/Passwords/Leaked-Databases/rockyou.txt -u http://172.17.0.2/index.php -X POST -H "Content-Type: application/x-www-form-urlencoded" -d "username=consuelo&password=FUZZ" -fr "Invalid password"
'''

If a web application enforces a password policy, we should ensure that our wordlist only contains passwords that match the implemented password policy. Otherwise, we are wasting valuable time with passwords that users cannot use on the web application, as the password policy does not allow them.

For example, if a policy stablishes that passwords must be at least 10 characters long, contain at least one uppercase letter, one lowercase letter and one number, we should filter our wordlist to only include passwords that meet these requirements.

'''bash
$ grep -E "^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{10,}$" /opt/useful/SecLists/Passwords/Leaked-Databases/rockyou.txt > /opt/useful/SecLists/Passwords/Leaked-Databases/rockyou_filtered.txt

$ grep '[[:upper:]]' /opt/useful/SecLists/Passwords/Leaked-Databases/rockyou.txt | grep '[[:lower:]]' | grep '[[:digit:]]' | grep -E '.{10}' > custom wordlist.txt

'''

Upon providing an incorrect username, the login response contains the message (substring) "Invalid username", therefore, we can use this information to build our ffuf command to brute-force the user's password:

'''bash
$ ffuf -w ./custom_wordlist.txt -u http://172.17.0.2/index.php -X POST -H "Content-Type: application/x-www-form-urlencoded" -d "username=admin&password=FUZZ" -fr "Invalid username"

<SNIP>

[Status: 302, Size: 0, Words: 1, Lines: 1, Duration: 4764ms]
    * FUZZ: Buttercup1
'''

## Brute-Forcing Password Reset Tokens

Password reset mechanisms are a common feature in web applications. They allow users to reset their passwords if they forget them. Typically, the user provides an email address or username, and the application sends a password reset link or token to the user's email address. The user can then use the link or token to reset their password.

Reset tokens (in the form of a code or temporary password) are secret data generated by an application when a user requests a password reset. The user can then change their password by presenting the reset token.

Attackers can abuse password reset mechanisms to gain unauthorized access to user accounts. If an attacker can predict or brute-force the reset token, they can reset the password and take over the account. To prevent this, applications should generate secure reset tokens that are hard to guess.

To identify weak reset tokens, we typically need to create an account on the target web application, request a password reset token, and then analyze it. In this example, let us assume we have received the following password reset e-mail:

'''
Hello,

We have received a request to reset the password associated with your account. To proceed with resetting your password, please follow the instructions below:

1. Click on the following link to reset your password: Click

2. If the above link doesn't work, copy and paste the following URL into your web browser: http://weak_reset.htb/reset_password.php?token=7351

Please note that this link will expire in 24 hours, so please complete the password reset process as soon as possible. If you did not request a password reset, please disregard this e-mail.

Thank you.
'''

As we can see, the password reset link contains the reset token in the GET-parameter token. In this example, the token is 7351. Given that the token consists of only a 4-digit number, there can be only 10,000 possible values. This allows us to hijack users' accounts by requesting a password reset and then brute-forcing the token.

## Brute-Forcing 2FA Codes

2FA makes it significantly more difficult for attackers to access an account even if they manage to obtain the user's credentials. By requiring users to provide a second form of authentication, such as a one-time code generated by an authenticator app or sent via SMS, 2FA mitigates the risk of unauthorized access. This extra layer of security significantly enhances the overall security posture of an account, reducing the likelihood of successful account breaches.

However, 2FA is not foolproof. Attackers can still bypass 2FA by exploiting vulnerabilities in the implementation of 2FA mechanisms. For example, attackers can intercept SMS messages containing 2FA codes using SIM swapping attacks or social engineering techniques. They can also exploit vulnerabilities in the 2FA implementation to bypass the 2FA check.

To bypass 2FA, attackers can brute-force the 2FA codes. 2FA codes are typically time-based one-time passwords (TOTPs) generated by authenticator apps such as Google Authenticator or Authy. These codes are valid for a short period (usually 30 seconds) and change every time a new code is generated.

## Weak Brute-Force Protection

Web applications often implement brute-force protection mechanisms to prevent attackers from brute-forcing user credentials. These mechanisms typically include rate limiting, account lockouts, and CAPTCHAs. While these mechanisms can help mitigate brute-force attacks, they are not foolproof and can be bypassed by attackers.

Rate limiting restricts the number of login attempts a user can make within a certain time frame. If the user exceeds the limit, they are temporarily blocked from making further login attempts. Attackers can bypass rate limiting by using multiple IP addresses or rotating proxies to distribute the attack across different sources.

Account lockouts temporarily lock a user's account after a certain number of failed login attempts. The account remains locked until the user resets their password or contacts support. Attackers can bypass account lockouts by targeting multiple user accounts simultaneously, preventing any single account from being locked out.

Completely Automated Public Turing test to tell Computers and Humans Apart (CAPTCHA) are used to distinguish between human users and automated bots. Users are required to solve a challenge, such as identifying distorted text or selecting images, to prove they are human. Attackers can bypass CAPTCHAs by using automated tools that solve the challenges or by outsourcing the challenges to human operators.

## Default Credentials

Many web applications are set up with default credentials that are rarely changed by users. Default credentials are often used during the initial setup of the application and are intended to be changed by the user after installation. However, users frequently neglect to change the default credentials, leaving the application vulnerable to unauthorized access.

Attackers can exploit default credentials to gain unauthorized access to web applications. They can use default usernames and passwords to log in to the application and take control of the system. To prevent this, users should always change the default credentials to unique, strong passwords.

Default credentials are often published in documentation or online forums, making them easily accessible to attackers. Attackers can use tools like Shodan to scan the internet for devices or services that are using default credentials. Once they identify a target, they can attempt to log in using the default credentials and gain access to the system.

Many platforms provide lists of default credentials for a wide variety of web applications. Such an example is the web database maintained by CIRT.net.

Further resources include [SecLists Default Credentials](https://github.com/danielmiessler/SecLists/tree/master/Passwords/Default-Credentials) as well as the [SCADA](https://github.com/scadastrangelove/SCADAPASS/tree/master) GitHub repository which contains a list of default passwords for a variety of different vendors.

## Vulnerable Password Reset

Password reset mechanisms are a common feature in web applications. They allow users to reset their passwords if they forget them. Typically, the user provides an email address or username, and the application sends a password reset link or token to the user's email address. The user can then use the link or token to reset their password.

Often, web applications authenticate users who have lost their passwords by requesting that they answer one or multiple security questions. During registration, users provide answers to predefined and generic security questions, disallowing users from entering custom ones. Therefore, within the same web application, the security questions of all users will be the same, allowing attackers to abuse them.

Another instance of a flawed password reset logic occurs when a user can manipulate a potentially hidden parameter to reset the password of a different account.

## Authentication Bypass via Direct Access

Authentication bypass via direct access is a vulnerability that allows an attacker to access restricted resources without providing valid credentials. This vulnerability typically occurs when an application fails to properly enforce authentication controls on sensitive resources.

Attackers can exploit authentication bypass vulnerabilities to gain unauthorized access to sensitive data or functionality. By directly accessing restricted resources without authentication, attackers can bypass security controls and perform unauthorized actions.

To prevent authentication bypass vulnerabilities, developers should ensure that all sensitive resources are properly protected by authentication controls. Access to sensitive resources should be restricted to authenticated users only, and proper authorization checks should be performed to verify that the authenticated user has the necessary permissions to access the resource.

## Authentication Bypass via Parameter Modification

An authentication implementation can be flawed if it depends on the presence or value of an HTTP parameter, introducing authentication vulnerabilities. Attackers can exploit these vulnerabilities by manipulating the parameters to bypass authentication controls and gain unauthorized access to sensitive resources.

This type of vulnerability is closely related to authorization issues such as Insecure Direct Object Reference (IDOR) vulnerabilities, where attackers can manipulate parameters to access unauthorized resources. By modifying parameters, attackers can bypass authentication controls and access sensitive data or functionality without providing valid credentials.

## Attacking Session Tokens

