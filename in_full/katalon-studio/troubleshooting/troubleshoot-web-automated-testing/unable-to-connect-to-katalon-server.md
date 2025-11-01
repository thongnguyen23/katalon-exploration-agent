---
hide_title: true
title: Unable to connect to Katalon server
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="troubleshooting-298" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Unable to connect to Katalon server

#### Remedy

Allow the following .exe files to communicate through Windows Firewall. To learn more about allowing apps through Windows Firewall, you can refer to the Microsoft document here: [Risks of allowing apps through Windows Defender Firewall](https://support.microsoft.com/en-us/windows/risks-of-allowing-apps-through-windows-defender-firewall-654559af-3f54-3dcf-349f-71ccd90bcc5c).

- geckodriver.exe
- chromedriver.exe
- iedriverserver.exe

These executable files can be located in: `<Katalon Studio folder>\\configuration\\resources\\drivers`.

<img className="image" src={useBaseUrl("https://raw.githubusercontent.com/katalon-studio/docs-images/master/katalon-studio/docs/troubleshooting-web-automated-testing/Screen-Shot-2018-04-24-at-13.51.51.png")} /><br />

<img className="image" src={useBaseUrl("https://raw.githubusercontent.com/katalon-studio/docs-images/master/katalon-studio/docs/troubleshooting-web-automated-testing/Screen-Shot-2018-04-24-at-13.51.41.png")} /> <br/>

You may also need to add Google Chrome (chrome.exe) and Firefox (firefox.exe) in the worst case if your current Windows Firewall blocks them as well.

