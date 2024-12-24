# Title: Arc Search Android Full Address Bar Spoof by Redirecting to a 204 No Content Page

## Description: 
While testing the android app I noticed when a webpage (example.com/test.html) redirects current page to another origin or page which have a 204 no content response the address bar will be changed to the other origin but the contents and the tab will still be on our current site.

- We host a website and redirect to a 204 response code page
- Address bar will be changed to the other origin 
- We change current page contents to a malicious login 

## Author: Renwa

## Affected Browser(s): Arc Android

## Severity: High

## Spoof Type: URL-Freeze

## References: Author

## POC Photo/Video: bug-034.mp4/.mov/.png

## Discovery Date: 2024-11-16

