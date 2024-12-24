# Title: Arc Search iOS Address Bar Spoof Using Search Functionality

## Description: 
Inside Arc Search for iOS when you tap the address bar and search for something it will redirect you to google searches and the address bar will be what you have typed, for example when you search for (arc test) it will redirect you to http://www.google.com/search?q=arc+test and the address bar will show (arc test). While testing this and playing with different parameters I found out that not just google.com but other TLDs were also allowed to change the address bar for example http://www.google.iq/search?q=arc+test will behave the same as it was .com and the address bar is changed to search value.

With this it mind I looked for how the browser chooses which TLDs to accept as a google domain and it looked like the check is google.(TLD, gTLD and second-level domain) now we have a potential vulnerability so in my domain registrar I searched for available google domains and luckily it got back some results but the cheapest one was google.gen.nz which is a second-level domain name.

Immediately I purchased the domain for $17 and started my test, I set up the /search endpoint then opened it inside Arc Search and luckily bingo we got the results we wanted. Now we can spoof the address bar to show anything we want. Summary of what's happening:

1. We own domain google.gen.nz and /search endpoint returns a login page
2. Load http://www.google.gen.nz/search?q=accounts.google.com inside the browser
3. Browser thinks this is a google search and changed the address bar to value of q parameter which is accounts.google.com
4. Address bar now is accounts.google.com but the contents are from google.gen.nz which we own

## Author: Renwa

## Affected Browser(s): Arc iOS

## Severity: High

## Spoof Type: Search-Engine

## References: Author

## POC Photo/Video: bug-030.mp4/.mov/.png

## Discovery Date: 2024-11-14

