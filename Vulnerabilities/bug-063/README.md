# Title: Rabby Wallet iOS Browser Address Bar Origin Spoof to Account Takeovers

## Description: 
Description
The impact of fund lose is involving the web2 part of the browser and not communicating with the wallet, As we know exchanges and most of crypto sites beside the web3 and wallet part it also uses web2 for login and access to funds, For instance this bug can be used to steal account details of coinbase or binance accounts which we will change the browser address bar to those sites and the contents will be a fake login page which the user will never know it's on a spoofed site and will trust the address bar for indicating the origin.
Details
Bug Description
The browser functionality inside the Rabby app doesn't properly check the navigation process and this allows an attacker to spoof origins and steal user data in multiple ways. Browsers are comlex technology and consist of many parts and functionalities, Address bar is a key evidence of the current origin and spoofing it will impact the integrity of information and the app trustworthiness. Usually address bar value is determined on current origin and what website the user is on but during navigations the browser might change the address bar to destined location before the page load ends and that's the issue with Rabby browser which updates the address bar based on next location and navigation before page load and check if the address or origin is reachable. This is what happens:

User is on attacker.com and taps on a link which points to google.com:81 (google.com:81 is unreachable because the port is invalid and it will never load)
Browser changes address bar to google.com
The destined location will never load and eventually will just show an error page after couple seconds
Address bar is changed to google.com but contents on the page is still from attacker.com
User thinks the navigation ended and he is on a legitimate origin and will trust the website
Impact
PoC
Open this URL inside Rabby iOS Browser: https://rx23.io/poc/rabby/1.html
Address bar and origin manipulated to google.com
References
https://www.trendmicro.com/vinfo/us/security/definition/address-bar-spoofing

Solution
The issue is the browser changes the address bar before navigation and the page loads completely to patch this vulnerability I suggest to change this mechanism so that when a navigation happens don't change the address bar until the page loads and the address is reachable, this way redirecting to invalid urls or slow loading pages won't change the address bar until the page loads and then the contents won't be from the attacker but the destined location origin.

## Affected Browser(s): Rabby Wallet

## Severity: High

## Spoof Type: Tab-Hanging

## POC Photo/Video: bug-063.mp4/.mov/.png

## Discovery Date: 2025-07-11

