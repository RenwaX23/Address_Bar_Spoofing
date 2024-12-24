# Title: Stored XSS in search.arc.net to Address Bar Spoof in Arc iOS and Potential UXSS

## Description: 
When we search for something inside Arc Search and use brows for me feature the browser will grab some links and send a POST request to open-ai-chat-omega.vercel.app then the AI will respond to us and the results are shown on the page. We an also share these results by clicking share or copy link URL which will send a second POST request to search.arc.net/api/share with a bunch of JSON data which then later will be processed by server side and returns us an ID to view later in other Arc browsers.

When another user opens the search results link the address bar of his browser will be changed to the search query and the results are previously set by us that we have sent in the POST request, while testing I found a stored XSS in link handlings of search results. When the results contain a link it will be inserted directly into <a href> without any security checks which will result in XSS by sending a javascript: URI.

Now we have XSS in context of search results and search.arc.net when clicked on a link, we also have full control over the address bar and what to be displayed with these 2 combinations we have full address bar spoof.

- XSS payload inserted into url parameter of POST request of /api/share 
- Shareable link sent to victim and address changed to google.com
- User clicks the link and XSS triggers
- Clear current page data by navigating to a slow page that will never load
- Display our HTML/JS content to steal credentials 
- User enters login data since the address bar is still google.com

## Author: Renwa

## Affected Browser(s): Arc iOS

## Severity: Medium

## Spoof Type: Search-Engine

## References: Author

## POC Photo/Video: bug-039.mp4/.mov/.png

## Discovery Date: 2024-11-16

