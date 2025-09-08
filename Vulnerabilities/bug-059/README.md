# Title: Safari Address Bar Spoof Using blob: URI

## Description: 
What is required to reproduce the issue?
Victim visiting a site
Summary
Safari shows end of the URI in blob: this will allow address bar spoof using unicode whitespace \u2800
Steps to reproduce
- Open in Safari Mac https://pwr.wtf/dice.html
Video POC
mac_blob.mov
Expected results
Address bar showing blob:https://pwr.wtf/08b3ff17-c14f-4171-b362-e93797ed4ff8#%E2%A0%80%E2....
Actual results
Address bar shows account.apple.com
Technical Details
The issue is the browser instead of showing the start of the URI it shows the end of it by abusing that we can insert multiple whitespaces \u2800 and insert the spoofed url account.apple.com and in the end we also insert the white spaces to bring the URL to the middle like other origins.

## Affected Browser(s): Safari

## Severity: High

## Spoof Type: blob:-URI

## POC Photo/Video: bug-059.mp4/.mov/.png

## Discovery Date: 2024-10-15

