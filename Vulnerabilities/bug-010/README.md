# Title: Opera GX Android - Address Bar Spoof with intent://vtp.operagx.gg/?url=

## Description: 
While looking at Opera GX for Mobile I found a critical vulnerability which allow us to fully spoof address bar of the browser without any user interaction.

Opera GX has a cool feature which allows you to send a video to your phone, when you open a video an icon shows up upon clicking will show a QR code link like this:

https://vtp.operagx.gg/?url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3D6Ejga4kJUts%26t%3D5s

Looking at the website this link will redirect to

intent://vtp.operagx.gg/?url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3D6Ejga4kJUts%26t%3D5s#Intent;scheme=https;category=android.intent.category.BROWSABLE;package=com.opera.gx;S.browser_fallback_url=https%3A%2F%2Fplay.google.com%2Fstore%2Fapps%2Fdetails%3Fid%3Dcom.opera.gx%26referrer%3Dutm_medium%253Dvtp%2526utm_content%253Dgoogle_play;end;

Playing with this intent I found out that you can also open other URIs inside the browser not only http/https.

One of the URIs caught my attention was data URLs https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/Data_URLs

Syntax of it is :
data:[<mediatype>][;base64],<data>

and example :
data:,Hello%2C%20World%21

Opening it inside the browser with the intent we found :

image-2023-03-22T20:32:04.243Z.png

As you can see our input is fully displayed inside the address bar and also with our content inside the page.

Playing with it I found a nice way which we can fully change the address bar and make it like a fully legit website, the URL I used:

data://login.auth.account.opera.com/,Opera.com is Down :(%0a%0d%0a%0dGo to https://new-opera.com/

Better understanding:

image-2023-03-22T20:28:23.860Z.png


## Author: Renwa

## Affected Browser(s): Opera GX Android

## Severity: Medium

## Spoof Type: Internal-URI

## References: https://medium.com/@renwa/you-are-not-where-you-think-you-are-opera-browsers-address-bar-spoofing-vulnerabilities-aa36ad8321d8

## POC Photo/Video: bug-010.mp4

## Discovery Date: 2023-03-22

