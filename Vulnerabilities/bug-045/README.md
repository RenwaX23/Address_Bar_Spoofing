# Title: Yandex Browser iOS Address Bar Spoofing Using about:blank UR

## Description: 
 **steps**:
 
 Yandex Browser iOS shows end of the URI in about:blank instead showing the beginning this will allow address bar spoof by constructing a long payload with a hash fragment # and hiding the start
 
 Open in Yandex iOS
https://pwr.wtf/br2.html

 
 The issue is the browser instead of showing the start of the URI it shows the end of it by abusing that we can insert a spoofed origin in end of it using a hash fragment # and this will hide the about:blank part in the beginning
 
 Mitigation: Show start of the URL in the address bar
 
 **current_result**:
 
 Address bar shows
https://accounts.apple.com

 
 
 **expected_result**:
 
 Address bar showing about:blank#
https://accounts.goo..
.
 
 **category**:
 
 Mobile
 
 **vulnerability_type**:
 
 Mobile
 
 **target**:

## Author: Renwa

## Affected Browser(s): Yandex iOS

## Severity: Medium

## Spoof Type: about:blank-URI

## References: Author

## POC Photo/Video: bug-045.mp4/.mov/.png

## Discovery Date: 2024-10-23

