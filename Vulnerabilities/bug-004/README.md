# Title: Full Address Bar Spoofing in Opera Touch and Opera GX Mobile

## Description: 
When you search for something using the address bar it will automatically redirect you to google and the search is reflected in address bar.

While testing I found out the app will change the address bar even if the user redirects from another site, it will just check if the domain starts with www.google.tld.tld (tld) is accepted as anything then the path starts with /search?client=ms-opera-touch-android&q=anything

Combining these 2 bugs I was able to spoof full address bar in the victim browser.

POC:
https://www.google.pwr.wtf/search?q=https://www.google.com/login&client=ms-opera-touch-android

## Author: Renwa

## Affected Browser(s): Opera GX Mobile

## Severity: High

## Spoof Type: Search-Engine

## References: https://medium.com/@renwa/you-are-not-where-you-think-you-are-opera-browsers-address-bar-spoofing-vulnerabilities-aa36ad8321d8

## POC Photo/Video: bug-004.mp4

## Discovery Date: 2022-10-06

