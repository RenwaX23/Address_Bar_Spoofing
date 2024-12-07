# Title: Opera Mac/Windows - New Window Address Bar Spoof using PictureInPicture

## Description: 
PictureInPicture
The new browser feature Picture-in-Picture allows websites to make a new window that is always on top and mostly used for displaying videos and video calls, now with the new update it treats it as a new window and you can add anything to like a normal webpage.

Bug
While checking Opera I noticed that there is a misconfiguration on how the windows is displayed, the browser doesn't set URL origin of the opened window and this allow us spoof the address bar to arbitrary domains and bypass the browser mechanism security.

Expected Behaviour
Chrome and the other browsers shows origin of the opener and this makes sure an attacker can't change or spoof the window.

## Author: Renwa

## Affected Browser(s): Opera 

## Severity: Medium

## Spoof Type: Window-Without-Address-Bar

## References: Author

## POC Photo/Video: bug-014.mp4

## Discovery Date: 2024-04-02

