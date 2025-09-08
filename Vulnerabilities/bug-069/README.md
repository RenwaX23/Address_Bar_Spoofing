# Title: Brave iOS Address Bar Spoof with open-url and data: URI

## Description: 
Summary:
The brave://open-url?url= endpoint doesn't have any check on which protocols and urls allowed which we can abuse to open data: URI in top window and get an address bar spoof, inside the browser if it's a data: it will prioritize the beginning and we can make a URI like: data:google.com/,Spoof or data:text/html,google.com/spoof the user will be tricked into thinking the data: is a subdomain of google.com.
Products affected:
Brave iOS
Steps To Reproduce:
On an iOS device open in Safari https://rx23.io/poc/brave/3.html
Click on the button then Open Brave
Address spoofed

## Affected Browser(s): Brave iOS

## Severity: Low

## Spoof Type: data:-URI

## POC Photo/Video: bug-069.mp4/.mov/.png

## Discovery Date: 2025-07-17

