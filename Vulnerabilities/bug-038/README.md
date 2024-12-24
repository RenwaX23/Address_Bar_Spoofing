# Title: XSS in arcmobile-internal:// using Server-Side Redirect to Javascript: URI to Full Address Bar Spoof in Arc Search iOS

## Description: 
If we open a webpage like example.com/file.php and the server redirect us to a javascript: URI like javascript:alert(origin) the address bar will be changed to the JS URI and when the user refreshes the page XSS will trigger in context of arcmobile-internal:// which is internal URI used by Arc Search to handle errors and also address bar value.

When we get an error or anything that the browser can't display the URL internal URL will be like this: ( arcmobile-internal://error?original_url=https://accounts.google.com/&reason=Redirection%20to%20URL%20with%20a%20scheme%20that%20is%20not%20HTTP(S)&auth_uuid=abcd.abcd....&has_displayed=true ) The address bar of the page will be set according to value of original_url, Now if we get an XSS on the internal URI we have full control over the address bar display any content we want.

Now here is the attack flow we have:

- User visits poc.php and taps on a button
- New tab open is opened pointing to a php file that server-side redirects to javascript:eval(payload)
- The tab is now in context origin of arcmobile-internal:// with the address bar being the XSS payload
- User refreshes the page because the error and XSS payload triggers
- Using the XSS we open a new tab pointing to arcmobile-internal://error?original_url=https://accounts.google.com/&reason=Redirection%20to%20URL%20with%20a%20scheme%20that%20is%20not%20HTTP(S)&auth_uuid=abcd.abcd....&has_displayed=true
- We stop loading the tab using win.stop() and change it's contents to a fake login page
- URL now is accouns.google.com and contents are a fake login that we have created

## Author: Renwa

## Affected Browser(s): Arc iOS

## Severity: Medium

## Spoof Type: Internal-XSS

## References: Author

## POC Photo/Video: bug-038.mp4/.mov/.png

## Discovery Date: 2024-11-22

