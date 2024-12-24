# Title: Address Bar Spoofing using documentPictureInPicture

## Description: 
The new browser feature documentPictureInPicture allow us to embed HTML into a small opened window and keep open even when navigating through other origins, Arc poorly implemented it that the opened window doesn't have a size limit like Chrome and others, this will make the opened window on top of the main window and spoof all the UI including the Address Bar. We will create a new PIP that is the size of the current window and recreate the side panel with our controlled attributes that we want to spoof.

I have created an online poc you can test it out, sometimes works after a second try not sure the problem might need a little optimization.

## Author: Renwa

## Affected Browser(s): Arc Mac

## Severity: Medium

## Spoof Type: Window-Without-Address-Bar

## References: Author

## POC Photo/Video: bug-026.mp4/.mov/.png

## Discovery Date: 2024-10-08

