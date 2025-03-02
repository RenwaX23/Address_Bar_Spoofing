# Title: Playstation 5 Browser Full Address Bar Spoofing

## Description: 
Summary:
By using a window.open trick with javascript URI we were able to spoof the full address bar of the browser and display any URL with any content we want tricking users to think they are on a legitimate site and share their credentials with us.
Steps To Reproduce:
Go to Messages feature inside the Console
Send this message to your friend pwr.wtf/ps
Click on the link
Address bar changed to google.com
Technical Details
When we open a new window using window.open() and the URL is a javascript URI javascript: the content of the page will be anything we want as we can use document.write() but the address bar will be the opener window URL, using this we can redirect the main window to any domain we want for example google.com and immediately open a new window pointing to a javascript URI and display our HTML content, the browser will update to address bar to google but the contents will be from the new opened window.
Impact
A web browser address bar spoofing vulnerability allows an attacker to manipulate the browser's address bar, making it display a false URL while the user is actually visiting a malicious site. This can trick users into thinking they are on a legitimate website, leading to phishing attacks, data theft, or the installation of malware. It undermines trust in the browser and poses a significant security risk, as users may unwittingly enter sensitive information such as passwords or credit card details.

## Author: Renwa

## Affected Browser(s): Playstation 5 Browser

## Severity: High

## Spoof Type: Javascript:-URI

## References: 0

## POC Photo/Video: bug-051.mp4/.mov/.png

## Discovery Date: 2024-10-8

