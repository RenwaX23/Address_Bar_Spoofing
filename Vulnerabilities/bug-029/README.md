# Title: Arc Search iOS Full Address Bar Spoof Using Blob: URI 

## Description: 
Hey Arc Team, happy to send you another report.

While using Arc on my iPhone I noticed when a web page is redirecting top window to blob: uri the URL bar will only show last part of it, for example blob:https://pwr.wtf/aee077ca-a499-47e9-8d2c-7daa5a89b020#spoof.arc.net the URL bar will show spoof.arc.net making it a great way to spoof it, when testing this I encountered a problem which was this:
As you can see the page says Not Secure which will make our attack not successful, but luckily I found a way to bypass that too, by redirecting the page to another page that will take ages to load, in my demo I created a sleep.php page which it will take 40 seconds to load this way it will hide the Not Secure part and the URL will display the full spoofed site.

## Author: Renwa

## Affected Browser(s): Arc iOS

## Severity: Medium

## Spoof Type: blob:-URI

## References: Author

## POC Photo/Video: bug-029.mp4/.mov/.png

## Discovery Date: 2024-10-15

