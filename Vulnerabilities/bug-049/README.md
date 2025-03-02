# Title: OKX App iOS-Android dApp Address Bar Origin Soof

## Description: 
Hey OKX Security Team, Happy to send you my first report.
Summary
The browser functionality inside the OKX dapp doesn't properly check the navigation process and this allows an attacker to spoof origins and steal user data in multiple ways.
Steps To Reproduce
Open this URL inside OKX dApp Browser: https://pwr.wtf/00dec/1.html
Address bar and origin manipulated to opensea.io
Technical Details
Browsers are complex technology and consist of many parts and functionalities, Address bar is a key evidence of the current origin and spoofing it will impact the integrity of information and the app trustworthiness. Usually address bar value is determined on current origin and what website the user is on but during navigations the browser might change the address bar to destined location before the page load ends and that's the issue with OKX browser which updates the address bar based on next location and navigation before page load and check if the address or origin is reachable.
This is what happens:
User is on attacker.com and taps on a link which points to opensea.io:81 (opensea.io:81 is unreachable because the port is invalid and it will never load)
Browser changes address bar to opensea.io
The destined location will never load and eventually will just show an error page after couple seconds
Address bar is changed to opensea.io but contents on the page is still from attacker.com
User thinks the navigation ended and he is on a legitimate origin and will trust the website
In my POC i'm constantly redirecting to opensea.io:81 because we don't get an error and the browser address bar is spoofed forever until the tab is closed.
Impact
Address bar is the main part of knowing what origin you're on and what to trust, and if this can be spoofed or changed in any way it's impossible for the user to spot he has been spoofed. OKX app is a critical app and it's web3 compatible which makes the attack more critical because an attacker can use this bug to steal NFTs, crypto currency, wallet information, funds from users and more. We can spoof the url to any origin we want and show any content, If the url is changed to opensea.io, coinbase.com, binance.com... and there is a fake login page it's impossible to know you have been spoofed and every user will fall for it and we can takeover thousands of accounts.
Mitigation
The issue is the browser changes the address bar before navigation and the page loads completely to patch this vulnerability I suggest to change this mechanism so that when a navigation happens don't change the address bar until the page loads and the address is reachable, this way redirecting to invalid urls or slow loading pages won't change the address bar until the page loads and then the contents won't be from the attacker but the destined location origin.
Thanks

## Author: Renwa

## Affected Browser(s): OKX

## Severity: High

## Spoof Type: URL-Freeze

## References: 0

## POC Photo/Video: bug-049.mp4/.mov/.png

## Discovery Date: 2024-12-11

