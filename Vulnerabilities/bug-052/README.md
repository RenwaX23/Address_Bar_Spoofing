# Title: Safari New Window Address Bar Spoof With a Subdomain or Long Domain

## Description: 
Summary
If the user is on a long domain/multiple subdomains or the page is embedded inside an iframe (example: idmsa.apple.com.rx23.io) if we request a new empty window to be opened like this window.open("", "", "width=300,height=300") the address bar inside the newly created window will show the beginning instead of the end meaning the user will see idmsa.apple.com, then using window_reference.document.body.innerHTML we change contents of the page to display anything we want to spoof users and takeover their accounts.
Steps to reproduce
1.  Go to https://rx23.io/poc/safari/2.html or https://idmsa.apple.com.rx23.io/x.html and click on the Sign in button
2. Address bar in the new window shows idmsa.apple.com
Expected results
Address bar showing ...apple.com.rx23.io
Actual results
Address bar shows idmsa.apple.com

## Author: Renwa

## Affected Browser(s): Safari

## Severity: Medium

## Spoof Type: Long-Subdomain

## POC Photo/Video: bug-052.mp4/.mov/.png

## Discovery Date: 2025-02-8

