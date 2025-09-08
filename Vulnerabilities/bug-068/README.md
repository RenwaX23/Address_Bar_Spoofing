# Title: MetaMask Wallet iOS - Browser Full Address Bar Spoof

## Description: 
Hey MetaMask Security team happy to send you my first report.
Summary:
When navigating to a new page inside the Browser of MetaMask app initiates Address Bar change before the next page load, using a race condition we can freeze the tab and spoof the origin.
Steps To Reproduce:
Open MetaMask App in Background
Open https://google.com/amp/s/pwr.wtf/krd.html Inside your default Browser
Origin Spoofed :)
or
Open MetaMask App
Open https://pwr.wtf/n.php Inside the Browser
Origin Spoofed
Technical Analysis and Moving Through the Code
I will try to explain my POC code here so you can know what's happening and faster patching the vulnerability.
Code 38 BytesUnwrap lines Copy Download
if(isset($_GET["sleep"])){
sleep(100);
This is just a small sleep() function to delay the load when the page has the ?sleep=1 parameter, we will use this later
<body onload=pwn();> adding a little delay for better reliability of the POC
j = setInterval(()=>{location=location.href+'?sleep=1'},100); Every 100 milliseconds the page will try to redirect to current location + ?sleep=1 parameter the page will never load because we have set a 100 seconds delay so the current page URL will be set to the PHP sleep location, this will change the URL but not navigation since it's not loaded yet.
jj = setInterval(()=>{location='//google.com'},5); Every 5 milliseconds the page now will try to navigate to google.com but since the page also tries to navigate to the sleep page the navigation won't happen but this will change the address bar to google.com now we have hang up the address bar that won't redirect to anywhere. ( I have used google.com just for POC you can use literally any domain and host even those which are not registred or invalid )
Code 63 BytesUnwrap lines Copy Download
document.body.innerHTML=`
<!DOCTYPE html>
<html lang="en">
....
This will create a fake login page after the spoof to any content we want
setTimeout(()=>{clearInterval(j);clearInterval(jj);},5000) after 5 seconds we will clear the intervals and navigation attempts to not hang up the page forever and crash the app, also this enables the victim to interact with the page and send us his credentials.
This Diagram will summarize the steps
Image F3613019: image.png 101.06 KiB
Zoom in Zoom out Copy Download

Mitigation
I don't really know how the browser is built and digging into the source code but patching this bug might take a lot of time or just a little code change, the main problem with the browser since I first tested is that the address bar is changing before completing navigation and fully displaying the page. With that any race condition or page freeze or even an infinite loop could possible spoof the address bar.
Severity
Address Bar Spoofing is usually High or Critical according to all browser vendors, also I checked the Hacktivity and saw someone also found this type of attack before.
Thanks
Renwa
Impact
Address Bar Spoofing allows us to fully spoof the URL bar of the browser and display an URL we want, This will trick the user thinking they are on a legitimate domain and insert their credentials or web3 account addresses. Since this application is also a Web3 based and there is a lot of funds allocated with it will make it more critical. I don't have much knowledge in Web3 security and applications but this can be used to a lot of cyber security attacks and steal user funds since the user will trust the address bar.

## Affected Browser(s): MetaMask iOS

## Severity: High

## Spoof Type: Tab-Hanging

## POC Photo/Video: bug-068.mp4/.mov/.png

## Discovery Date: 2024-09-18

