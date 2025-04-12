# Title: Safari Mac/iOS Browser Address Bar Spoof Using Search Engines

## Description: 
Summary
When a user searches for something inside the browser the address bar is changed to the search criteria this can be abused by using some quirks and search features to display our content and spoof the address to arbitrary origin
Expected results
Browser address bar shows google.com or bing.com
Actual results
Browser address bar shows www.apple.com with attacker contents
Technical Details
The browser also had a protection to not change the address bar to a domain I used a little trick to bypass that protection, by using a new line %0a along with a null byte %00 I was able to set arbitrary domains and spoof the URL.

For UX I know it's a great thing to change the address bar to the search criteria and he can revise it but the problem arises when the URL bar is also changed when a website redirect to search results.

Attacker.com redirects the page to google.com/search?q=spoof and the URL bar is changed to spoof this itself is not a vulnerability but chained with other issues can be a problematic.

While testing Safari I notices that the browser to change the address bar it checks *.google.com/search?q={change} this means all subdomains of google can be used and looking for features I found Google Sites which is hosted on sites.google.com and by appending /search parameter we can trick the browser to change the url bar to our spoofed origin and inside the page we display our content which we have inserted into google sites.

Another way was using lens.google.com which allows us to host any image and share it then using the ?q= parameter we set it to our desired spoof page.

Later I looked at Bing and other search engines and I found the same misconfiguration there too, Bing has an endpoint called qsml.apx allows us to set arbitrary text content and also Bing hosts the site crawled images inside bing.com using that we can also change the URL and display any Image we want.

These are 4 different ways to spoof the address bar and display contents on the browser, there is surely other and better ways but here I'm demonstrating the impact to prove the vulnerability/

## Affected Browser(s): Safari

## Severity: Medium

## Spoof Type: Search-Engine

## POC Photo/Video: bug-057.mp4/.mov/.png

## Discovery Date: 2024-10-17

