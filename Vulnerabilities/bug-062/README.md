# Title: Firefox Desktop Address Bar Spoof Using Search Query (bypass fix in bug 1970997)

## Description: 
This bug is bypass for the patch in bug 1970997 & bug 1974410
So the proposed patch is checking the origin of the search engine with the redirected site, if origin changes then remove the search query from the URL, this is a flawed approach because these search engines have thousands of functionalities and sub-pages which we can us for spoofing attacks: image crawls, video embed, file upload, content injection, XSS or any other bugs.

Using Wikipedia we can create a fully HTML page with any content and use it for our spoof.

Steps to Reproduce:

Open https://rx23.io/test/dice.html and Click on the button
Paste what you have copied inside the address bar or just make a normal search query
Go back to first tab then to the search tab
Address bar is spoofed to the value you pasted or the search query you made with our HTML

## Affected Browser(s): Firefox 

## Severity: Low

## Spoof Type: Search-Engine

## POC Photo/Video: bug-062.mp4/.mov/.png

## Discovery Date: 2025-07-09

