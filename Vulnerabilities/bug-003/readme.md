# Title: Safari iOS Full Address Bar Spoof Using Tab Hanging

## Description: 
# Summary

In Safari iOS there is an issue which when a tab is opened the browser will change the address bar before the page load and make sure the host is reachable, with this we can open a new tab pointing to `apple.com:81` port 81 is not reachable and the tab will hang forever, then we will stop the window and change the tab contents to our spoofed content we want since the origin will become `about:blank` and accessible from our tab, after changing tab contents we will redirect the tab back to `apple.com:81` which the browser will change the address bar to `apple.com` and with our contents.

# Steps to reproduce

- Open in Safari iOS `https://REDACTED`


# Expected results

Address bar showing `about:blank` or empty URL

# Actual results

Address bar shows `apple.com` with our contents displayed on the page 

# Mitigation 

Change the address bar to opener origin or about:blank or just show an empty URL

## Author: Renwa

## Affected Browser(s): Safari iOS

## Severity: High

## Spoof Type: address-hanging

## References: 

## POC Photo/Video: safari_hang.mp4

## Discovery Date: 2024-11-01

