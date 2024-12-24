# Title: Coinbase Wallet App For iOS Address Bar Origin Spoof

## Description: 
Description:
The Coinbase wallet app doesn't correctly show the origin and the address of a initiate request which allow an attacker to spoof the domain and trick a user into thinking they are on a legitimate domain.
The browser app if the domain is long it will truncate the end of it and only shows the beginning, for example: https://www.google.com.pwr.wtf inside the browser it will display as www.google.com... this is a great risk and explained very well in Chromium documentation about how to show a URL and display it correctly for security issues: https://chromium.googlesource.com/chromium/src/+/HEAD/docs/security/url_display_guidelines/url_display_guidelines.md#simplify


Impact:
An attacker can create a malicious subdomain and hide it's main domain from a victim to trick them into thinking they're on a legitimate site and initiate transactions and steal funds from users, the address bar is a key source information and spoofing this is critical to the application and trustworthiness of integrity.
Steps To Reproduce:
Open inside the Wallet browser app https://pwr.wtf/slaw.html#x
Click to login to Google
Address bar spoofed to account.google.com
Browsers or Application Versions:
Coinbase Wallet Version 29.22

Mitigation
As explained in chromium docs the URL shouldn't truncate the end but rather the beginning instead of showing google.com... it must show ...le.com.pwr.wtf

Impact
An attacker can create a malicious subdomain and hide it's main domain from a victim to trick them into thinking they're on a legitimate site and initiate transactions and steal funds from users, the address bar is a key source information and spoofing this is critical to the application and trustworthiness of integrity.

## Author: Renwa

## Affected Browser(s): Coinbase Wallet

## Severity: Medium

## Spoof Type: Long-Subdomain

## References: Author

## POC Photo/Video: bug-023.mp4/.mov/.png

## Discovery Date: 2024-12-11

