# Title: Safari Browser Address Bar Spoof Using Redirect

## Description: 
Summary
There is a vulnerability in Safari that allows an attacker to spoof the address bar using a redirect, google.com redirects to attacker.com then attacker redirects the page to a sleep page and the address bar changes to google.com with contents of attacker site
Steps to reproduce
1. Open in Safari https://www.google.com/amp/s/hax.guesser.team/jj/renwa/ 

Video POC:
Screen Recording 2024-10-17 at 2.38.25 PM.mov
Expected results
Address bar showing hax.guesser.team
Actual results
Address bar shows google.com
Technical details
The attack flow is like this 
- Victim opens google.com/redirect_to=attacker.com
- The address bar now is attacker.com then the page will redirect to a never loading page that will sleep and won't load
- Address bar changes to current page Referer which is google.com

In my example I'm using /amp/s/ endpoint to redirect to my site, open redirects are mostly out of scope in bug bounty programs so they are everywhere, here is another POC using YouTube

https://youtube.com/signin?next=https%3A%2F%2Faccounts.youtube.com%2Faccounts%2FSetSID%3Fcontinue%3Dhttps%3A%2F%2Fwww.google.com/amp/s/hax.guesser.team/jj/renwa/

Also another trick I used in this attack is using a Chinese text on the page that will automatically shows the Translation Available to hide the attacker.com domain from victim in the first second before we spoof the address bar.

## Affected Browser(s): Safari

## Severity: Medium

## Spoof Type: URL-Freeze

## POC Photo/Video: bug-061.mp4/.mov/.png

## Discovery Date: 2024-10-17

