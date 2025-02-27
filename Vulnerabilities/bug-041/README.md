# Title: Firefox Mobile iOS Full Address Bar Spoof Using Open in New Tab and Javascript: URI

## Description: 
Hey Firefox Team

When a URL is javascript://google.com/ and we use (Open in New tab) feature in iOS the new tab is opened and the address bar will be google.com, using this bug we can enter a new line (%0a) and execute our script to insert a fake form or anything else want to be displayed inside the page as the URL will be google.com.

User visits a webpage
Inside the page we have a link saying open me inside a new tab
New tap get's opened which is a Javascript URI and our script executes
The script will change contents of the page to a fake login page
User will enter his credentials thinking it's on a legitimate origin
POC: https://pwr.wtf/arc/fx.php

Video POC: ScreenRecording_11-25-2024 14-35-53_1.mp4

POC Source Code: https://pwr.wtf/arc/fx.php?source=1

Mitigation: If the URL is not http(s) don't change the address keep it empty or about:blank

Thanks
Renwa

## Author: Renwa

## Affected Browser(s): Firefox iOS

## Severity: Medium

## Spoof Type: javascript:-URI

## References: Author

## POC Photo/Video: bug-041.mp4/.mov/.png

## Discovery Date: 2024-11-25

