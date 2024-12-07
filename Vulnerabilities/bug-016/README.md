# Title: Brave iOS Address Bar Spoofing Using about:blank URI

## Description: 
Brave iOS shows end of the URI in about:blank instead showing the beginning this will allow address bar spoof by constructing a long payload with a hash fragment # and hiding the start
Expected results
Address bar showing about:blank#https://accounts.goo...
Actual results
Address bar shows https://accounts.apple.com
Technical Details
The issue is the browser instead of showing the start of the URI it shows the end of it by abusing that we can insert a spoofed origin in end of it using a hash fragment # and this will hide the about:blank part in the beginning

## Author: Renwa

## Affected Browser(s): Brave

## Severity: Medium

## Spoof Type: about:blank-URI

## References: Author

## POC Photo/Video: bug-016.mp4

## Discovery Date: 2024-10-19

