# Title: Opera GX For Android URL Spoof/Freeze

## Description: 
While looking at Opera GX for android I found another address bar spoof which allow an attacker trick a victim to send his credentials on spoofed origin.

I noticed something weird with GX, when there is an Arabic character in url combined with a normal a-z character the browser will hang and doesn't do anything but the url will be set to value we set.
For example copy this URL and paste it inside the browser
http://سgoogle.com

It won't be considered a real vulnerability if we tell the victim to copy and paste this into the address bar, Luckily I found another way we can abuse to get our desired result. With putting the text inside a textarea and tabbing on search it will be shown on the address bar.


## Author: Renwa

## Affected Browser(s): Opera GX Mobile

## Severity: Low

## Spoof Type: URL-Freeze

## References: https://medium.com/@renwa/you-are-not-where-you-think-you-are-opera-browsers-address-bar-spoofing-vulnerabilities-aa36ad8321d8

## POC Photo/Video: bug-005.mp4

## Discovery Date: 2022-10-27

