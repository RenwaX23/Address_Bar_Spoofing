# Title: Firefox Mobile iOS Full Address Bar Spoof Using Server-Side Redirect to internal://local/errorpage

## Description: 
Hey Firefox Team

While looking at Firefox for iOS I noticed that using a server-side redirect (307,308...) we can redirect the browser to any location including local URIs, digging deeper I found out that Firefox uses internal://local/errorpage to deliver errors about if the page fails to load, When an error is happening the address bar will become value of url parameter which is present inside the internal URI and also another thing is that the origin of the tab will become the redirector. Here is in a simple manner:

User visits ff.php and taps a button
New tab is opened pointing to ff.php?redirect which will do a server-side redirect to internal://local/errorpage?url=https://www.google.com/login&code=0&domain=&description=Redirection%20to%20URL%20with%20a%20scheme%20that%20is%20not%20HTTP(S)&timestamp=1732440620327
Address bar of the tap will become www.google.com/login which we have set it inside the url parameter
Origin of the opened tab will become the redirector which was attacker.site
Using cross-window reference we access the tab and change it's contents to a fake login page
Now address bar is Google and contents are controlled by the attacker
POC: https://pwr.wtf/arc/ff.php

Video POC: ScreenRecording_11-24-2024 18-32-54_1.mp4

POC Source Code: https://pwr.wtf/arc/ff.php?source=1

Mitigation: Don't allow server-side redirects internal://

Thanks
Renwa

## Author: Renwa

## Affected Browser(s): Firefox iOS

## Severity: High

## Spoof Type: Internal-URI

## References: Author

## POC Photo/Video: bug-042.mp4/.mov/.png

## Discovery Date: 2024-11-24

