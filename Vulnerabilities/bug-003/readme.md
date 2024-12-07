# Title: Opera Mini Browser Address Bar Spoof

## Description: 
While looking at Opera Mini for Android I found a critical bug which allow an attacker to spoof URL address bar and trick the victim to steal his credentials or any other act.

I decompiled the app using jadx-gui app and looked at the source code to find anything interesting, In one of the packages I found this

return new zoa("client_welcome_update", this.b + ' ' + b2 + " 🎉", 5000, "opera-mini://open?url=https%3A%2F%2Fwww.opera.com%2Fmobile%2Fmini");
Playing with the custom opera-mini://open:url= scheme was not that much interesting all it did was just a redirect to the given website in url parameter.

After so much fuzzing and different things I tried I found something really cool.

If a web page let's say example.com has a link to the custom scheme which points to a website with a downloadable file the webpage will still be our domain but the address bar will change to the link we set.

attacker.com -> click link to opera-mini://open?url=google.com/download
address bar changes to google.com/download
contents of the page is still from attacker.com and user can interact with it

## Author: Renwa

## Affected Browser(s): Opera Mini

## Severity: High

## Spoof Type: Internal-URI

## References: https://medium.com/@renwa/you-are-not-where-you-think-you-are-opera-browsers-address-bar-spoofing-vulnerabilities-aa36ad8321d8

## POC Photo/Video: bug-003.mp4

## Discovery Date: 2022-09-29

