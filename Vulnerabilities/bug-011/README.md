# Title: Opera Mini - Address Bar Spoof with opera-mini://open?url=data:

## Description: 
While looking at Opera Mini for Android I found a critical Address Bar spoof which allow us to change the bar to any url without any user interaction.

The special internal scheme opera-mini://open?url= can open any URLs so we use this to open data: URLs and trick the address bar thinking its a valid domain.

## Author: Renwa

## Affected Browser(s): Opera Mini

## Severity: Medium

## Spoof Type: Internal-URI

## References: https://medium.com/@renwa/you-are-not-where-you-think-you-are-opera-browsers-address-bar-spoofing-vulnerabilities-aa36ad8321d8

## POC Photo/Video: bug-011.mp4

## Discovery Date: 2023-03-22

