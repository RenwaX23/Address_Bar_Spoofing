# Title: Arc iOS Full Address Bar Spoof Using Timing Attack

## Description: 
Summary:
This bug is Critical and similar to #3239495 , in Arc iOS we can fully spoof the address bar by opening a blank page, redirect to a site we want to spoof and immediately change it's contents.
Attack pseudo code:
Open a new tab pointing to about:blank
Using the window reference we change its location to https://google.com after 100ms
Immediately we change the contents of the tab to a spoof login page using window reference and document.write()
The issue is when we redirect to another domain the address bar is changed immediately to the value of destined location but the origin of the opened tab is still from the opener which we could set arbitrary DOM with a spoofed URL bar.

## Affected Browser(s): Arc iOS

## Severity: High

## Spoof Type: URL-Freeze

## POC Photo/Video: bug-064.mp4/.mov/.png

## Discovery Date: 2025-08-26

