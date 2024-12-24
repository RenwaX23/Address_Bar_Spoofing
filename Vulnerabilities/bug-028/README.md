# Title: Address Bar Spoof in Arc Search iOS

## Description: 
While looking at Arc browser for iOS I found a cool bug that allows us to spoof origin of any site we want and display our contents, the attack flow is like this:

1.We open a slow webpage in a new window that will not load or be very slow for example: bing.com:81 
2. Change contents of the opened window using document.write() that will stop the navigation and our content is displayed 
3. Redirect the tab to invalid scheme with our desired origin to spoof, for example: xhttp://google.com

The page now shows the origin is google.com and the page contents are what we have set in step 2 

## Author: Renwa

## Affected Browser(s): Arc iOS

## Severity: High

## Spoof Type: Invalid-Scheme

## References: Author

## POC Photo/Video: bug-028.mp4/.mov/.png

## Discovery Date: 2024-10-13

