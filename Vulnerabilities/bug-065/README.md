# Title: Arc iOS Full Address Bar Spoof Using Search Functionality and Race Condition

## Description: 
Summary:
Hey Arc Team, happy to send you another report. When a user searches for something the browser will redirect to (google.com/search?q=%s) and the browser address bar will change to value of the query (%s), while investigating this I noticed when the user taps on the G logo or the Arc in bottom right there is a small window which the origin of the window will be cleared and it can be overridden with the window reference by another origin while the address bar still remains value of the search query.
Vulnerability pseudo code
User visits attacker.com which will open a new tab pointing to (google.com/search?q=apple.com)
Address bar will change to apple.com with page contents of Google search
Attacker site will constantly check for the tab origin to when the user taps on the G logo or the Arc logo
After origin clear attacker's site has control over the tab with the spoofed address bar and its own contents
Victim will get spoofed into thinking it's a legitimate apple.com site and sends his credentials
Previous attack
This attack is similar to my previous search engine trick which was rewarded as a High severity here is the report for reference:
Image F4533365: image.png 455.40 KiB
Zoom in Zoom out Copy Download

Steps To Reproduce:
Open in Arc iOS and tap on the button https://rx23.io/poc/arc/4.html
Tap on the G or the Arc logo in bottom right
Address bar spoofed to account.google.com with a fake login page

## Affected Browser(s): Arc iOS

## Severity: High

## Spoof Type: Search-Engine

## POC Photo/Video: bug-065.mp4/.mov/.png

## Discovery Date: 2025-07-07

