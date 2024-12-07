# Title: Brave iOS Address Bar Spoofing Using blob: URI

## Description: 
Brave iOS shows end of the URI in blob: instead showing the beginning this will allow address bar spoof by constructing a long payload with a hash fragment # and hiding the start
Expected results
Address bar showing blob:https://pwr.wtf/08b3ff17-c14f-4171-b362-e93797ed4ff8#https://www.acco...
Actual results
Address bar shows www.account.apple.com
Technical Details
The issue is the browser instead of showing the start of the URI it shows the end of it by abusing that we can insert a spoofed origin in end of it using a hash fragment # and this will hide it's from a blob: URI

## Author: Renwa

## Affected Browser(s): Brave

## Severity: Medium

## Spoof Type: blob:-URI

## References: Author

## POC Photo/Video: bug-015.mp4

## Discovery Date: 2024-10-17

