# Title: Chrome/Brave/Yandex  iOS Address Bar Spoof Using 2 RTL (Arabic Characters) Subdomain

## Description: 
The issue arises when using 2 RTL characters in different level subdomains and in between add a domain that we want to spoof. First we add a RTL character then any domain we want to spoof and in the end we add another RTL character that will confuse the address bar and mixes up the RTL LTR showing of the URL.

### REPRODUCTION CASE
- Using Browser open `https://xn--llb.login.wwww.accounts.google.com.xn--llb.pwr.wtf/`

### Expected Result
- Address bar showing `ە.login.wwww.accounts.google.com.ە.pwr.wtf/`

### ctual Result
- Address Bar shows `pwr.wtf.ە.ogin.wwww.accounts.google.com...`


## Author: Renwa

## Affected Browser(s): Chrome/Brave/Yandex/Edge iOS

## Severity: Medium

## Spoof Type: rtl-subdomain

## References: N/A

## POC Photo/Video: 

## Discovery Date: 2024-10-19

