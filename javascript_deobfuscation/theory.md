# Javascript Deobfuscation

## Introduction

Javascript deobfuscation is the process of converting obfuscated Javascript code into a human-readable format. Obfuscation is a technique used to make code difficult to understand or reverse-engineer, often used by attackers to hide malicious code. Deobfuscation is essential for analyzing and understanding the behavior of obfuscated Javascript code, especially in the context of web security.

Most websites nowadays utilize JavaScript to perform their functions. While HTML is used to determine the website's main fields and parameters, and CSS is used to determine its design, JavaScript is used to perform any functions necessary to run the website. This happens in the background, and we only see the pretty front-end of the website and interact with it.

To obfuscate we can use, for example, the following tools:
- [Obfuscator.io](https://obfuscator.io/)
- [Javascript Obfuscator](https://javascriptobfuscator.com/Javascript-Obfuscator.aspx)
- [Beauty](https://beautifytools.com/javascript-obfuscator.php)

A common way of reducing the readability of a snippet of JavaScript code while keeping it fully functional is JavaScript minification. Code minification means having the entire code in a single (often very long) line. Code minification is more useful for longer code, as if our code only consisted of a single line, it would not look much different when minified.

Many tools can help us minify JavaScript code, like [javascript-minifier](https://javascript-minifier.com/).

A packer obfuscation tool usually attempts to convert all words and symbols of the code into a list or a dictionary and then refer to them using the (p,a,c,k,e,d) function to re-build the original code during execution. The (p,a,c,k,e,d) can be different from one packer to another. However, it usually contains a certain order in which the words and symbols of the original code were packed to know how to order them during execution.

Common deobfuscation tools are:
- [JSNice](http://jsnice.org/)
- [Prettier](https://prettier.io/)
- [js-beautify](https://beautifier.io/)
- [Unpacker](https://lelinhtinh.github.io/de4js/)
- [UnPacker](https://matthewfl.com/unPacker.html)

## Base 64 Encode and Decode

Base64 is a group of binary-to-text encoding schemes that represent binary data in an ASCII string format by translating it into a radix-64 representation. The term Base64 originates from a specific MIME content transfer encoding. Each base64 digit represents exactly 6 bits of data. Three 8-bit bytes (i.e., a total of 24 bits) can therefore be represented by four 6-bit base64 digits.

Base64 encoding is used in many situations to store or transfer data in environments that require ASCII strings, such as email systems, which do not support binary data. Base64 encoding is also used to encode binary data in XML documents.

To encode a string to base64, we can use the following code:

```bash
echo -n "Hello, World!" | base64
```

To decode a base64 string, we can use the following code:

```bash
echo -n "SGVsbG8sIFdvcmxkIQ==" | base64 -d
```
