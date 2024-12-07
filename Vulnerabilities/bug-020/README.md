# Title: Edge - Mac - Address Bar Spoofing using Picture-in-Picture

## Description: 
Hey Edge Team, happy to send you my first report.

Picture in Picture
The new browser feature Picture-in-Picture allows websites to make a new window that is always on top and mostly used for displaying videos and video calls, now with the new update it treats it as a new window and you can add anything to like a normal webpage.

Edge in Mac
While testing the feature inside Edge on Mac OS I noticed that when you create a new Picture-in-Picture the window doesn't have an omnibox nor an address bar, just a borderless window floating and we can insert anything we want to it. This itself is a vulnerability which allows an attacker to create a custom address bar and display it inside the window and display whatever content below it tricking users thinking they're on a real origin.

Here is a simple POC showing this simple attack.

﻿https://pwr.wtf/arv/ax.html﻿

Screenshot demonstrating both a real window and a fake spoofed Picture-in-Picture window, can you spot which one is the real one?

More Misconfiguration
If we look at the feature specification it states that:

The Picture-in-Picture window never outlives the opening window.
The Picture-in-Picture window position cannot be set by the website.
While checking Edge I noticed that it doesn't follow these specifications and we can do:

Open a new Window and it outlives the current window
We can set size and position using a normal resizeTo() function 
Attack
With these we can construct a real attack and fully spoof contents of any origin like this:

Open a Picture-in-Picture window
Open a new window pointing to login.live.com
Set size and location of the PIP window to entire contents of the page 
The URL address and omnibox now are true but we have spoofed the contents of it.
Expected Behaviour - FIx
Like Chrome or Edge on Windows 

PIP must also have an omnibox and display origin of it
The window must not outlive the current window
Size and position must be restricted to not fully cover the page

## Author: Renwa

## Affected Browser(s): Edge Mac

## Severity: Medium

## Spoof Type: Window-Withour-Address-Bar

## References: Author

## POC Photo/Video: bug-020.mp4/.mov/.png

## Discovery Date: 2024-03-27

