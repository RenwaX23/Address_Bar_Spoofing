# Title: Google App iOS Full Address Bar Spoof

## Description: 
Using the Google app for iOS when navigating to a site from the search or entering the URL manually the address bar only shows the origin of it, this is normally when the scheme is http/https but if we open a new tab with location of about:blank the address bar now doesn't have an origin it will display the full URL, and the issue is also arises that if the URL is too long the UI will show the end of it, for example opening about:blank#(multiple _spaces) google.com the address bar display (multiple _spaces) google.com and hides the about:blank# part making the address bar spoofed and a user thinks it's on google.com

POC
When creating a POC I encountered a problem which when opening a URL with about:blank#test the app immediately closed the tab and got an error but I found a solution to this problem by creating an about:blank page then from there creating a second about:blank#test which didn't get any errors, also the app doesn't have popup blocking protection making the attack without any user interaction.

Online POC open in Google app iOS: https://pwr.wtf/br2.html

Video POC: ScreenRecording_10-31-2024 11-02-43_1.mp4

## Author: Renwa

## Affected Browser(s): Google iOS

## Severity: Medium

## Spoof Type: about:blank-URI

## References: A

## POC Photo/Video: bug-047.mp4/.mov/.png

## Discovery Date: 2024-11-02

