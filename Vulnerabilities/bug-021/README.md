# Title: Edge Mobile (Android-iOS) Address Bar Spoof Using Bing Search

## Description: 
Intro
While looking at Edge mobile I found an address bar spoof issue using the Bing search functionality, this allows an attacker to control the address bar and change the page contents.

Bing Search
In Edge mobile when we search for something like test the browser will redirect to https://www.bing.com/search?q=test and URL bar is changed to test , this itself is not a vulnerability but rather a useful functionality but chaining with other Bing functions we can get address bar spoof.

Bing Images/Videos
The mobile app doesn't correctly check for the Bing search URL but rather anything bing,com/?q=query will change the address bar to query this brings attack vector, we can demonstrate two examples using Bing Images search results and Videos.

We can host a malicious image on our domain then when Bing crawler crawls the image it will be hosted on bing.com/th/… then by adding ?q=www.google.com we can spoof the address bar thinking its on google.com and displaying our image.

We can also use the Copilot to create our desired image and use it for spoofing.

Bing also has a functionality which embeds videos inside itself without need to leave the search results this also brings a new attack vector we upload a malicious video which will be embedded inside bing.com and use the ?q= parameter to spoof the URL

Full Content Control
While researching into this I wanted something more powerful rather than image/video so while looking I found bing.com/qsml.aspx?query=anything which is a search suggestion page that returns our full input inside body of the page without any limitation now with just adding ?q= parameter to it we can have full address bar spoof with arbitrary body contents.

## Author: Renwa

## Affected Browser(s): Edge Mobile

## Severity: Medium

## Spoof Type: Search-Engine

## References: Author

## POC Photo/Video: bug-021.mp4/.mov/.png

## Discovery Date: 2024-04-13

