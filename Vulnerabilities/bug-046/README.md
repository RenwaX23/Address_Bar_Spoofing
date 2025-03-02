# Title: Yandex Browser iOS Address Bar Spoof Using 2 RTL (Arabic Characters) Subdomains

## Description: 
The issue arises when using 2 RTL characters in different level subdomains and in between add a domain that we want to spoof. First we add a RTL character then any domain we want to spoof and in the end we add another RTL character that will confuse the address bar and mixes up the RTL LTR showing of the URL.
 
 Open in browser:
https://xn--llb.login.wwww.accounts.google.com.xn--llb.pwr.wtf/

 
 
 **current_result**:
 
 Address Bar shows pwr.wtf.ە....accounts.google.com.ە
 
 
 **expected_result**:
 
 Address bar showing ....google.com.ە.pwr.wtf
 
 
 **category**:
 
 Mobile
 
 **vulnerability_type**:
 
 Mobile
 
 **target**:

## Author: Renwa

## Affected Browser(s): Yandex iOS

## Severity: Low

## Spoof Type: RTL-Character

## References: Author

## POC Photo/Video: bug-046.mp4/.mov/.png

## Discovery Date: 2024-10-23

