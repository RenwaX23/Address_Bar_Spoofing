# Title: Yandex iOS Address Bar Spoofing Using blob: URI

## Description: 
**steps**:
 
 Yandex iOS shows end of the URI in blob: instead showing the beginning this will allow address bar spoof by constructing a long payload with a hash fragment # and hiding the start
 
 Open in Yandex browser iOS
https://pwr.wtf/br.html

 
 The issue is the browser instead of showing the start of the URI it shows the end of it by abusing that we can insert a spoofed origin in end of it using a hash fragment # and this will hide it's from a blob: URI
 
 Mitigation: Show start of the URL in the address bar
 
 
 **current_result**:
 
 Address bar shows
www.account.apple.com

 
 
 **expected_result**:
 
 Address bar showing blob:
https://pwr.wtf/08b3ff17-c14f-4171-b362-e93797ed4ff8#https://www.acco..
.
 
 
 **category**:
 
 Mobile
 
 **vulnerability_type**:
 
 Mobile
 
 **target**:

## Author: Renwa

## Affected Browser(s): Yandex iOS

## Severity: Medium

## Spoof Type: blob:-URI

## References: Author

## POC Photo/Video: bug-044.mp4/.mov/.png

## Discovery Date: 2024-10-23

