# Title: Safari Mac/iOS Full Address Bar Spoof Using Tab Hanging and Invalid URLS

## Description: 
Summary
When we open a new tab pointing to an invalid URL like blob: the tab address bar will be empty then inside the newly created tab we open third tab pointing to another invalid URL blob: which again the address bar will be empty, since the tabs are same-origin we change contents of the third tab w spoof page then redirect the page to apple.com:81 which the address is unreachable and it will never load. The address bar can't be empty and will revert back to apple.com with our spoofed content. With a normal webpage when this happens the address will become opener origin but with this invalid tabs the address bar is empty which confuses the browser and sets it to the apple.com domain.
Expected results
Address bar showing https://pwr.wtf or about:blank
Actual results
Address bar showing apple.com

## Affected Browser(s): Safari

## Severity: Medium

## Spoof Type: URL-Freeze

## POC Photo/Video: bug-055.mp4/.mov/.png

## Discovery Date: 2024-11-26

