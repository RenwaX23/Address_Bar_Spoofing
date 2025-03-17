# Title: Address Bar Spoof Using Invalid Protocol in Naver Whale iOS

## Description: 
Summary
Hey Whale browser team, when opening a custom invalid scheme inside the browser the address bar will be changed to that address and allows address bar spoof.

Details
When we open a new tab pointing to xhttps://google.com/ the browser will indicate a message open in external app and also will update the address bar to display the origin which it will choose google.com, since no navigation happened we can still access DOM of the tab and display our full contents to steal victim credentials which thinks he is on a legitimate origin.
Impact
Steal credentials from users thinking they are on a right website

## Affected Browser(s): NAVER Whale

## Severity: High

## Spoof Type: Invalid-Scheme

## POC Photo/Video: bug-052.mp4/.mov/.png

## Discovery Date: 2024-11-17

