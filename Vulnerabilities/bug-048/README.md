# Title: Brave iOS Address Bar Spoof and Potential UXSS Using brave://open-url?url=

## Description: 
Summary:
The custom link handling for Brave iOS brave://open-url?url= doesn't check the scheme of the url input which allows us to insert javascript: and data: URIs and show them inside the address bar which can lead to spoofing attacks.
When using javascript: URI this can also be used to trick users into making it a bookmark and the URL will become a bookmarklet which can lead to UXSS.
This bug also spoofs Brave Rewards and Brave Shield
Also when using a custom scheme or internal URIs like mailto: and tel: the browser will parse the URL and shows an alert warning that this site wants to open external app, something like tel://google.com/123 it will show that google.com wants to make a phone call.
Products affected:
Brave iOS 1.71.1 (125)
Steps To Reproduce:
Using another browser open https://pwr.wtf/arc/w.html and Tap the page

## Author: Renwa

## Affected Browser(s): Brave iOS

## Severity: Low

## Spoof Type: Internal-URI

## References: a

## POC Photo/Video: bug-048.mp4/.mov/.png

## Discovery Date: 2024-12-08

