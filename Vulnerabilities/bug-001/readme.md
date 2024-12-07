# Title: Bypassing CVE-2019-10875 or, Xiaomi's Mint Browser's URL Spoofing patch

## Description: 
A friend and fellow researcher Renwa disclosed a 0day in Xiaomi's Mi and Mint Browsers. He asked me to write about this on my blog since it's very similar to my previous find. He just found a bypass that lets him use the same trick that I used before,

Intro
His exploit/PoC is just the same as mine. Domain stays same, query parameter same. But attacker's domain needs a subdomain same as the name of the query parameter. 

That's where he outsmarted Xiaomi's fix with a simple trick.

Who are still affected?
Mi Browser has not received the security patch. Neither has Mint Browser on Xiaomi's App Store. 
Shady Security Patch? - Why? because it was so inadequate and easy to bypass!
Too soon? Just after that big news about Xiaomi Browser Vulnerability broke. Makes one question about Xiaomi's overall credibility and security patching. How on earth could someone make such a fix that could be bypassed with just so little an effort? The patch seems shady since it could be bypassed so easily, don't agree? See self. I have published a video PoC of the same.

Renwa pinged me yesterday  about his new bypass of Mint Browser's patch in response to my URL spoofing vulnerability that I disclosed a few days back. This got me curious. I was not aware of this because the UPDATED version of Mint (1.6.3) wasn't available on Mi Appstore. I came to know from him that they released the patched version on Google Playstore on the 5th of April, 2019.

His exploit is based on the fact that Xiaomi developers wrote some bad regex rules to patch my previous URL spoofing attack that failed on the onslaught of a new trick to circumvent the same. Was it intentional again :P?

The fix didn't work anyways. Is this how Xiaomi puts things into production? Didn't they test for similar secuity issues or, what? They don't do it for Global products ;) or, what?

Because, they either have started learning regex or, don't know how to patch security issues on their Browser products.


How?
Renwa's 0day utilises the fact that their new Regex rules which were supposed to fix the previous problem, namely, CVE-2019-10875 were not sufficient, not only that, it was not the appropriate measure. 

He bypassed their protection by using my previous trick including the target domain in 'q' parameter but, the only thing he included this time, the wittiest part is that it struck his mind what if he changes the *subdomain name* on the phishing domain to the target domain name? Guess what? Their patch failed to prevent this new bypass/attack. Renwa's assumption was right!


New PoC or, attack vector that succeeds my older one
http://google.com.phishing-site.com/?q=google.com that spoofs google.com as an example

## Author: Renwa

## Affected Browser(s): Xiaomi Mint

## Severity: High

## Spoof Type: Search-Engine

## References: https://www.andmp.com/2019/04/bypassing-cve-2019-10875-or-xiaomis.html

## POC Photo/Video: bug-001.mp4

## Discovery Date: 2019-04-07

