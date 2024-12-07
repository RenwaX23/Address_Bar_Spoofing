# Title: Opera for Android Address Bar Spoof

## Description: 
Description
While looking at Opera for Android implantation of how address bar is displayed and full screen display I found a vulnerability which allow us to fully spoof the address bar.

Vulnerability
In browsers we can request full screen using javascript or clicking on full screen view inside a video, the browser will change the view to full screen which hides everything including the address bar.

Testing how Opera handles full screen view I noticed that there isn't any notification which alerts the user his view is changed to fullscreen. This is the heart of the bug and very serious actually below I demonstrate it more clearly.

Testing the same functionality inside Chrome and other browsers I found they have a mitigation for it:

Chrome for Android:

Opera GX for Mobile:

Opera for Android didn't prompt anything when changing to fullscreen.

## Author: Renwa

## Affected Browser(s): Opera Android

## Severity: Low

## Spoof Type: Fullscreen

## References: https://medium.com/@renwa/you-are-not-where-you-think-you-are-opera-browsers-address-bar-spoofing-vulnerabilities-aa36ad8321d8

## POC Photo/Video: bug-007.mp4

## Discovery Date: 2023-02-06

