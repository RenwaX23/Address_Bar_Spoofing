# Title: Safari Mac and iOS Address Bar Spoof

## Description: 
Detailed description
Hey Apple Team happy to send you my first report :)
Summary
There is a mishandling of about:blank URI in Safari browser which allows us by inserting a hash fragment and long white-space to hide the URI and insert our spoofed site and display arbitrary contents on in.
Expected results
The address bar only showing about:blank or empty URL or showing the about:blank#..... instead of truncating the beginning and showing last of the URL
Actual results
Address bar shows account.apple.com with a fake login page which can be used to account takeover
Technical Details
When displaying an about:blank URI followed by a long hash fragment let's say about:blank#AAAAAABBBBBBCCCCCCDDDD the browser truncates the beginning and it will show ...BBBCCCCCCDDDD inside the address bar. It should display about:blank#AAAAAABB.... this will make sure the user is in a blank page and not other site.

While investigating this and making the POC more realistic I had to find a way to so that our spoofed address is displayed in the middle of the URL and looks like a legitimate site, in the process I found a right whitespace \u2800 called Braille Pattern Blank by inserting multiple of these before the spoofed address and after it will make the attack unnoticeable to anyone.

In my POC code we open the about:blank page then will insert the fake login page as a POC since it will be treated as same-origin then when the user enters it's credentials we can takeover the account.
Mitigation
To patch this vulnerability I suggest when opening about:blank URIs truncate the end of the URL and not the beginning or you can just show a about:blank without the hash or query parameters of it


## Affected Browser(s): Safari

## Severity: High

## Spoof Type: about:blank-URI

## POC Photo/Video: bug-056.mp4/.mov/.png

## Discovery Date: 2024-10-15

