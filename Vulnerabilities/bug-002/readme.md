# Title: 0day Alert: URL Spoofing Bypassed for latest Mint Browser 1.6.4

## Description: 
Yesterday, I published about Mint's 1.6.3 being vulnerable to the same flaw that I reported to Xiaomi, even after Xiaomi pushed a fix on the 5th of April, 2019. The fix could be bypassed with little effort neatly.

In a matter of few hours, my friend Renwa bypassed Xiaomi's Mint's latest patch (on PLAYSTORE release) leading to a new 0day.

Who are affected?
Mi Browser and Mint Browser (upto 1.6.4)

Intro
Renwa discovered it and told me about it. This becomes the 2nd zero day discovered in a row in the Mint Browser and Mi Browser. 

Renwa found a bypass to the previous patch by Xiaomi team, by simply adding the target domain name to the phishing domain making it the subdomain of the phishing/attacker's domain. Which proved that Xiaomi's patch was insufficient and above all meaningless. 

But, the same day he came up with a new exploit which makes use of Unprintable Characters to bypass Xiaomi's new security patch in response to yesterday's 0day.


Trick/Bypass
By using Unprintable Characters %e2%80%8c, appended to the URL query parameter.

## Author: Renwa

## Affected Browser(s): Xiaomi Mint

## Severity: High

## Spoof Type: Search-Engine

## References: https://www.andmp.com/2019/04/0day-alert-url-spoofing-bypass-for.html

## POC Photo/Video: bug-002.mp4

## Discovery Date: 2019-04-08

