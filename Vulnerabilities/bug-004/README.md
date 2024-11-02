# Title: Brave iOS Address Bar Spoofing Using about:blank URI

## Description: 
##Summary:
Brave iOS shows end of the URI in about:blank instead showing the beginning this will allow address bar spoof by constructing a long payload with a hash fragment # and hiding the start

## Products affected:
Brave Browser iOS

## Steps To Reproduce:
Open in Brave iOS `https://REDACTED`

## Supporting Material/References:
Video POC

{F3690294}

## Expected results
Address bar showing `about:blank#https://accounts.goo...`

## Actual results
Address bar shows `https://accounts.apple.com`

## Technical Details
The issue is the browser instead of showing the start of the URI it shows the end of it by abusing that we can insert a spoofed origin in end of it using a hash fragment # and this will hide the about:blank part in the beginning 



## Mitigation
Show start of the URL in the address bar

## Impact

Address Bar Spoofing will trick the victim into thinking they are on a legitimate origin and this allow stealing credentials and breaking one of the main browser security mechanisms.

## Author: Renwa

## Affected Browser(s): Brave

## Severity: Medium

## Spoof Type: non-http scheme

## References: N/A

## POC Photo/Video: 

## Discovery Date: 2024-10-19

