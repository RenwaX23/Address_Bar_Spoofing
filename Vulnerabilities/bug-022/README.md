# Title: Zerion Wallet App For iOS Address Bar and Wallet Confirmation Origin Spoof

## Description: 
Brief/Intro
The Zerion wallet app doesn't correctly show the origin and the address of a initiate request which allow an attacker to spoof the domain and trick a user into thinking they are on a legitimate domain.

Vulnerability Details
The browser app along with the wallet if the domain is long it will truncate the end of it and only shows the beginning, for example: https://www.google.com.pwr.wtf inside the browser it will display as www.google.com... and also inside the wallet confirmation it will displayed as www.google.co... this is a great risk and explained very well in Chromium documentation about how to show a URL and display it correctly for security issues: https://chromium.googlesource.com/chromium/src/+/HEAD/docs/security/url_display_guidelines/url_display_guidelines.md#simplify

Impact Details
An attacker can create a malicious subdomain and hide it's main domain from a victim to trick them into thinking they're on a legitimate site and initiate transactions and steal funds from users, the address bar and origin of the wallet is a key source information and spoofing this is critical to the application and trustworthiness of integrity.

References
https://chromium.googlesource.com/chromium/src/+/HEAD/docs/security/url_display_guidelines/url_display_guidelines.md#simplify
https://www.trendmicro.com/vinfo/us/security/definition/address-bar-spoofing
Proof of Concept
Proof of Concept
Open inside the browser https://www.google.com.pwr.wtf/

## Author: Renwa

## Affected Browser(s): Zerion Wallet

## Severity: Medium

## Spoof Type: Long-Subdomain

## References: Author

## POC Photo/Video: bug-022.mp4/.mov/.png

## Discovery Date: 2024-11-04

