# Title: Address Bar Spoofing using data: URI

## Description: 
When displaying data: URIs we can trick the browser into displaying only our string and hide out the data: part, the scheme of data uri is like this data:text/html,content but we can also use data://google.com/,content the browser will think this is like a http scheme and only displays google.com and hiding the data: part and the contents of the page will be anything after the comma , 


## Author: Renwa

## Affected Browser(s): Arc Mac

## Severity: Medium

## Spoof Type: data:-URI

## References: Author

## POC Photo/Video: bug-025.mp4/.mov/.png

## Discovery Date: 2024-10-15

