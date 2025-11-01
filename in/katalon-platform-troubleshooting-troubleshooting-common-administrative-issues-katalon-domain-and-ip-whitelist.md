---
title: Katalon domain and IP whitelist
---

This document lists out all the IP addresses and domains associated with Katalon services.

​If your systems or applications under test (AUT) are installed within a restricted network environment, you might need to whitelist these IPs and domains to ensure uninterrupted connection. The whitelist of your network should consider both outbound and inbound traffic.​ 

Outbound traffic is comprised of connections that originate from within your network, such as sending data to `admin.katalon.com` to activate licenses. Inbound traffic, conversely, is comprised of the traffic entering your network from external services, such as TestCloud accessing the AUT hosted inside your network. Therefore, domain whitelisting is often associated with outbound traffic and IP whitelisting for inbound traffic.​

You can whitelist the IPs and domains that are relevant to the testing use cases of your organization. 
For specific whitelists of TestCloud and TrueTest services, see: 
- [Network configuration for TestCloud](/katalon-testcloud/network-configuration-for-testcloud) 
- [Network configuration for TrueTest](/katalon-platform/create-tests/test-case-generation-with-truetest/network-configuration-for-truetest)

## Katalon domains

| Domain | Usage |
| ------ | ----- |
| <ul><li>`admin.katalon.com`</li><li>`login.katalon.com`</li><li></li>`testops.katalon.io`</ul> | Online license authentication and activation for Katalon Studio |
| `katalon-inc.my.site.com` | Customer Support Portal |
| `store.katalon.com` | Load installed plugins from Katalon Store |
| <ul><li>`update.katalon.com`</li><li>`katalon.com`</li></ul> | Send product usage and adoption, which helps us improve our products in the upcoming releases |
| <ul><li>`testops.katalon.io`</li><li>`<your-subdomain>.katalon.io`</li></ul> | Enable Katalon Studio - TestOps integration |
| `katalon-test.s3-accelerate.amazonaws.com` | Allow Katalon Studio to upload reports to TestOps |
| `download.katalon.com` | Allow TestOps to work with TestOps agents |
| `https://raw.githubusercontent.com/katalon-studio/katalon-studio/master/releases.json` | Allow TestOps to create test run types in Katalon Studio |
| `testcloud.katalon.com` | Execute tests with the TestCloud environments |
| `analytics.katalon.com` | Online license authentication and Katalon Studio - TestOps integration, for Katalon Studio versions below 8.2.5 |
| <ul><li>`tunnel-manager.katalon.com:443` (HTTPS)</li><li>`tunnel-proxy-1.katalon.com:2345` (QUIC)</li><li>`tunnel-proxy-2.katalon.com:2345` (QUIC)</li></ul> | TestCloud Tunnel |


## Katalon IP addresses

| IP | Usage |
| -- | ----- |
| <ul><li>54.146.187.152/32</li><li>18.204.240.9/32</li><li>35.174.93.205/32</li><li>52.45.203.41/32</li><li>52.203.34.201/32</li><li>35.172.81.5/32</li></ul> | Katalon TestOps services |
| <ul><li>52.22.58.98/32</li><li>44.212.203.215/32</li><li>54.161.107.199/32</li></ul> | Katalon Admin, AI features, Katalon Store, Jira Add-ons |
| <ul><li>34.197.223.43/32</li><li>54.82.166.185/32</li><li>54.197.235.86/32</li></ul> | Katalon TestCloud services |