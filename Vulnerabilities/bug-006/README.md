# Title: XSS in play.gx.games to RCE, Full Address Bar Spoof in Opera GX

## Description: 
Summary
A stored XSS issue in play.gx.games sandbox domain allowed me to communicate with Gaming Landing Page default extension which allowed me to get code execution in victim browser and full address bar spoof.

play.gx.games
Opera has built a new platform for gamers to play online on https://gx.games/, there is a plenty of games and features which you can play and contribute to the platform too.
Anyone can create games and publish it on the website by using GameMaker Studio which is also made by Opera, GMS uses its own programming language called GML Code this code translates to different platforms and also browser. In browser the code I think translates to WebAssembly then to Javascript. After creating the game and publishing it online anyone can play it on the platform, the game is embedded inside an iframe in a sandboxed domain play.gx.games.

GameMaker Studio
I'm already familiar with GMS and made some scripts in the past so I wanted to test if we can use the GML code to get any vulnerabilities inside play.gx.games domain after pushing the game online.
Played with everything and made some small scripts but my favorite function which I had a feeling there is something it was url_open(), from documentation: This will open the specified URL on the browser of the chosen target device, or, if you are using the HTML5 module, in the currently open browser. so basically it's just like window.open().
More tests I found out that url_open will translate to window.open inside a browser and got me thinking, url_open("javascript:alert(23)"); lets test it, I got:

hmm thats interesting but why blocked? yeah I forgot that in modern browsers window.open() requires user interaction now lets read GML documentation and find how to add an event listener to run our script only when we clicked on the page or any other object. It was easy just took me a half day to figure that out lol.

Testing it again and:

Boom what a lovely alert box now lets push our code to play.gx.games and it worked like expected we have now XSS on that sandbox domain.

XSS
What we can do with our lovely XSS? we can steal user info like his profile picture, username, user id and do CSRF actions behalf of him maybe change his bio and pp to I'm Noob Player in the end it's a sandboxed gaming website not a bank nothing interesting. The worse case might be spoofing to get user to enter his Opera credentials and send it to us but nah I'm always after more creative and critical bugs.
GameMaker, Opera GX and GX.games all are made by Opera and maybe same developers so there might be a connection with them and what could go wrong?

Gaming Landing Page
I wanted to test Opera GX browser like my previous bug to see if there is any hidden extensions which play.gx.games has access to it. run GX on mac with this option open /Applications/Opera\ GX.app --args --show-component-extension-options
Now lets dive into every extension and check its manifest.json file. Gaming Landing Page this extension caught my eye and lets look at it with this url chrome-extension://mpojjmidmnpcpopbebmecmjdkdbgdeke/manifest.json

"externally_connectable": {
    "matches": [
      "*://*.gxc.gg/*",
      "*://*.gmx.dev/*",
      "*://localhost:*/*",
      "*://*.gx.games/*",
      "*://*.creategx.games/*"
    ]
  }
Do you see what I see? externally_connectable means these origins can send message to this extension and luckily our XSS inside play.gx.games matches the domains, now it's time to read its code and what it does with the receives messages, minified version of the code:

if (request.command === 'closeTab') {
chrome.tabs.remove([sender.tab.id], () => {
          sendResponse();
          window.setTimeout(() => {
            this.ignore[sender.tab.id] = false;
          }, 5000);
        });
      }

if (request.command === 'authenticate') {
      try {
        opr.gamingPrivate.authenticate(
          request.randomString,
          new Uint8Array(Object.values(request.hash)),
          hash => {
            sendResponse({hash: Object.values(new Uint8Array(hash))});
            opr.gamingPrivate.gameStarted(sender.tab.id);
          },
        );

    const url = new URL(sender.url);
    if (
      request.command === 'openURL' &&
      (url.protocol === 'https:' || url.hostname === 'localhost')
    ) {
      opr.gamingPrivate.openURL(request.url, request.fullScreen, request.size);
      sendResponse();
    }
    if (request.command === 'product') {
      opr.operaBrowserPrivate.getProduct(product => {
        sendResponse({product});
      });
      return true;
    }
So we have 4 commands:

closeTab closed our tab, nothing
authenticate gives us user token which we can use for account takeover, not much
openURL opens a URL inside a new window that looks interesting
product sends back browser version, useless
Alright lets investigate openURL, it sends our data to opr.gamingPrivate.openURL() native function which has 3 parameters, url -string, fullScreen -boolean and size -no one knows
I was stuck in the third parameter for many days any giving parameter I gave it rejected even chatGPT couldn't answer it. one day I came back to it and gave it this object {'__proto__':23} and I got: Error at parameter 'size': Missing required property 'height'. now I send {'height':23} got Missing required property 'width finally given width and testing it.

We got our little cute window opened. Now what you just got yourself a duplicate of window.open() with a more complex way?
Don't demotivate me while there is life there is hope -probably a thirteen year old girl after her boyfriend cheated on her but greatest philosopher of all time Nietzsche once said Hope in reality is the worst of all evils because it prolongs the torments of man.

Enough talking lets spam all the inputs as long its free

At least window.open has origin but this one nothing.

Lets try RCE by file open vulnerability, trying to open an application on our system.

But nothing the file gets downloaded and saved into Downloads folder without opening it

Lets check File URI to see if we can load a file and read other files on the system

origin is null like opening a normal local file inside your browser, trying ftp, ldap, ms-office, you name it every possible schemes on Mac and Windows but nothing interesting its just like a our open() function but without URl restriction and user gesture needed.

## Author: Renwa

## Affected Browser(s): Opera GX

## Severity: Medium

## Spoof Type: Window-Without-Address-Bar

## References: https://medium.com/@renwa/you-are-not-where-you-think-you-are-opera-browsers-address-bar-spoofing-vulnerabilities-aa36ad8321d8

## POC Photo/Video: bug-006.mp4

## Discovery Date: 2023-01-10

