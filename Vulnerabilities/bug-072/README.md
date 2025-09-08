# Title: Firefox Address Bar Spoof with Long Subdomain and Popup

## Description: 
The issue is simple, when opening a popup with a long subdomain the address bar prioritizes the beginning and hides the true origin of the URL. for example: (https://accounts.google.com.attacker.com) when we open it inside a small pop-up the address bar displays (https://accounts.google.com).

The address bar should display (https://...ogle.com.attacker.com) or maybe (https://accounts.google.com....) even I don't recommend this choice

POC: https://rx23.io/poc/firefox/2.html (It might not work perfectly for you as the pop-up width is crucial for the origin spoof, check the screenshot for how it should be)

## Affected Browser(s): Firefox

## Severity: Medium

## Spoof Type: Long-Subdomain

## POC Photo/Video: bug-072.mp4/.mov/.png

## Discovery Date: 2025-03-01

