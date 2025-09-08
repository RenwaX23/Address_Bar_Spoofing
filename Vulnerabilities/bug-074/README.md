# Title: Edge iOS Address Bar Spoof Using 2 RTL (Arabic Characters) Subdomains

## Description: 
Description
Summary:
The issue arises when using 2 RTL characters in different level subdomains and in between add a domain that we want to spoof. First we add a RTL character then any domain we want to spoof and in the end we add another RTL character that will confuse the address bar and mixes up the RTL LTR showing of the URL.

Steps To Reproduce:
Using Edge iOS open https://xn--llb.login.wwww.accounts.google.com.xn--llb.pwr.wtf/

Or http://xn--mgb.google.com.xn--mgb.pwr.wtf/
Supporting Material/References:
IMG_0124.PNG
IMG_0125.PNG
The SSL warning just needs to setup SSL nothing special

Expected Result
Address bar showing ە.login.wwww.accounts.google.com.ە.pwr.wtf

Actual Result
Address Bar shows pwr.wtf.ە.w.accounts.google.com...

## Affected Browser(s): Edge iOS

## Severity: Medium

## Spoof Type: RTL-Character

## POC Photo/Video: bug-074.mp4/.mov/.png

## Discovery Date: 2024-10-18

