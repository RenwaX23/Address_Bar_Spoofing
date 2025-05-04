# Title: Safari Mac Address Bar Spoof Using Cursor Overlap

## Description: 
# What is required to reproduce the issue?
Visiting a website and mouse over a button

# Summary
Hey Safari Team, the Safari browser unlike other browsers (Chrome, Firefox) doesn't have any custom cursor boundary check to make sure it doesn't cross Line of Death of the browser and overlap the main browser functionalities. By abusing this we can create a custom 128x128 pixels cursor and place it directly over the address bar to show a spoofed image displaying `icloud.com` origin when the user hovers over a button placed beneath the address bar. The users cursor is placed on the page but the custom big one we have set it to be bigger and top of the page so it goes above the current boundaries which results in this spoofing.

# Steps to reproduce
1. Visit `https://rx23.io/poc/safari/4.html`
2. Mouse over the button
3. Address bar spoofed to `icloud.com`

# Expected results
Custom cursor doesn't cross the page boundaries

# Actual results
Address bar spoofed to `icloud.com`

## Affected Browser(s): Safari

## Severity: Low

## Spoof Type: overlap

## POC Photo/Video: bug-058.mp4/.mov/.png

## Discovery Date: 2025-05-05

