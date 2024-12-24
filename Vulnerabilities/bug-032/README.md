# Title: Arc Searc Android Address Bar Spoof Using Long Subdomain

## Description: 
The address bar is misconfigured in Arc Search for Android which allows URL Spoof, when a website has long URL it's not possible to load all the URL inside the address bar so it must truncate it, for example: www.google.com.pwr.wtf it must show ...gle.com.pwr.wtf this will discard the beginning and shows the top parent domain, But Arc Android truncates the end of the URL which now the browser will show www.google.com... 

This allows address bar spoof and the user thinking they're on google.com domain, This is well documented in Chromium URL display guidelines which you can read more about it: https://chromium.googlesource.com/chromium/src/+/HEAD/docs/security/url_display_guidelines/url_display_guidelines.md#simplify

## Author: Renwa

## Affected Browser(s): Arc Android

## Severity: Medium

## Spoof Type: Long-Subdomain

## References: Author

## POC Photo/Video: bug-032.mp4/.mov/.png

## Discovery Date: 2024-11-15

