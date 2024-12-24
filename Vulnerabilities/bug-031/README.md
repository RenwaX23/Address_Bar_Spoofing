# Title: Arc Search Android Full Address Bar Spoof Using Custom Port Website Hanging

## Description: 
While looking at Arc for android I found a high severity vulnerability which allows us to spoof the address bar of the browser, We all know port 80 is for http and 443 for https but what will happen if we open a website with another port like https://google.com:81/ ? You can try it and the tab will just hang without getting any response back.
When opening a new tab (window) in Arc android the browser will change the address bar to the url before finishing page load and making sure the address is reachable or valid with this quirk we can open a new tab pointing to a website with port 81 then change contents of the tab using document.write and keep the URL as the spoofed address.

Pseudo Code:

1. User visits our site
2. New tab is opened pointing to google.com:81
3. New tab URL is now google.com but it will never load because the address is unreachable
4. Since the tab hasn't been loaded yet the origin will be same-origin and we can override its contents using document.write()
5. Address bar now shows google.com with our spoofed content

## Author: Renwa

## Affected Browser(s): Arc Android

## Severity: High

## Spoof Type: URL-Freeze

## References: Author

## POC Photo/Video: bug-031.mp4/.mov/.png

## Discovery Date: 2024-11-15

