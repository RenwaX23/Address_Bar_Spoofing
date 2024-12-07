# Title: Iframe Injection in GX Corner to Address Bar Spoofing in Opera GX

## Description: 
Intro
There is an ifarme injection vulnerability in GX Corner which allows an attacker to host any content on the site much like defacing, this allows us to redirect the victim to a URL that doesn't have an address bar and thinking they are on a trusted origin.

Iframe Injection
While browsing GX Corner and checking wayback machine and other recon tools to find any parameters, I found about the playlist functionality which allow us to embed youtube videos inside the site which we submit inside the URL like this

https://gxcorner.games/?playlist=https://www.youtube.com%2Fembed%2FTiuopnWnU78&playlist=https%3A%2F%2Fwww.youtube.com%2Fembed%2FX3na0g9g-cwr&currentIndex=0

The app will create an iframe pointing to supplied URL without any check, the responsible code:

function Bu(n) {
    let e, t, r, i, s;
    return {
        c() {
            e = E("iframe"),
            y(e, "title", n[1]),
            y(e, "fetchpriority", "low"),
            Ct(e.src, t = n[22](n[0], n[7] || n[5] && !n[6])) || y(e, "src", t),
            y(e, "allow", r = "fullscreen " + n[17]),
            y(e, "scrolling", "no"),
            y(e, "width", n[9]),
            y(e, "height", n[8]),
            y(e, "class", "svelte-pdg4go"),
            M(e, "loaded", n[11])
        },
        m(l, o) {
            $(l, e, o),
            n[25](e),
            i || (s = Y(e, "load", n[20]),
            i = !0)
        },
        p(l, o) {
            o[0] & 2 && y(e, "title", l[1]),
            o[0] & 225 && !Ct(e.src, t = l[22](l[0], l[7] || l[5] && !l[6])) && y(e, "src", t),
            o[0] & 131072 && r !== (r = "fullscreen " + l[17]) && y(e, "allow", r),
            o[0] & 512 && y(e, "width", l[9]),
            o[0] & 256 && y(e, "height", l[8]),
            o[0] & 2048 && M(e, "loaded", l[11])
        },
        d(l) {
            l && k(e),
            n[25](null),
            i = !1,
            s()
        }
    }
}
There is only one check which prevent us from getting full XSS which is here

function S(I, P) {
        return P & 8 && (s = null),
        s == null && (s = !I[3].startsWith("https://")),
        s ? 0 : 1
    }
Now lets try to submit a URL to our host

https://gxcorner.games/games?playlist=https://example.com/&playlist=https%3A%2F%2Fwww.youtube.com%2Fembed%2FX3na0g9g-cwr&currentIndex=0

image-2024-02-19T21:17:10.219Z.png

As you can see there isn't any check on the host of the iframe we can supply and URL and it will be displayed inside GX Corner.

Adress Bar Manipulation
Notice anything weird from the previous screenshot

image-2024-02-19T21:18:25.413Z.png

By default GX Corner doesn't have any address bar and the browser hides it from us, using this trick with the iframe injection we can trick the victim to think he is on any trusted origin since we have hidden the URL from it.

## Author: Renwa

## Affected Browser(s): Opera GX

## Severity: Low

## Spoof Type: Window-Without-Address-Bar

## References: Author

## POC Photo/Video: bug-012.mp4

## Discovery Date: 2024-02-19

