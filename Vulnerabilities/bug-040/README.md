# Title: FireFox Mobile Address Bar Spoof Using Long Subdomain

## Description: 
Hey Firefox Team

Description
FireFox on Mobile both iOS and Android doesn't handle URL view correctly when using a long subdomain, It shows beginning of the URL instead of the end meaning https://www.account.google.com.attacker.com inside the browser it displays it as www.account.google.com... This allows address bar spoof and tricking the user into thinking they are on a legitimate google site.

POC
The impact and the bug is obvious you can use this page to see the problem so I hadn't created a full POC:

Open in FireFox Mobile: http://account.login.google.com.github.io
You can also test https: and click on accept risk: https://account.login.google.com.github.io

Image POC
Galaxy S10 and iPhone 16
(poc_both.png)

Mitigation
Show end of the site instead of the beginning, it needs to show ...google.com.github.io

Thanks
Renwa

## Author: Renwa

## Affected Browser(s): Firefox Mobile

## Severity: Medium

## Spoof Type: Long-Subdomain

## References: Author

## POC Photo/Video: bug-040.mp4/.mov/.png

## Discovery Date: 2024-10-18

