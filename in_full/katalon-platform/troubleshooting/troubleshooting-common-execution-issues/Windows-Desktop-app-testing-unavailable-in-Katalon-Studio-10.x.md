---
hide_title: true
title: Windows Desktop app testing unavailable in Katalon Studio 10.x
---

# Windows Desktop app testing unavailable in Katalon Studio 10.x

Windows Desktop app testing remains temporarily unavailable in Katalon Studio versions 10.0.0 to 10.2.x due to incompatibilities between Selenium 4 and WinAppDriver.

WinAppDriver, which is required for Desktop app testing, has not yet been updated to support the W3C WebDriver protocol that Katalon Studio 10.x (Selenium 4) uses.

Starting version 10.3.0, Windows Desktop app testing is now available in **beta** with a new built-in driver based on the FlaUI library, replacing WinAppDriver. This driver supports basic record, spy, and execution functionality and does not require separate installation.

- If you need stable Windows Desktop testing, continue using Katalon Studio 9.x.
- For more information on feature availability, limitations, and supported application types, see the [Katalon Studio Release Notes: Version 10.x](/katalon-studio/release-notes/katalon-studio-release-notes-version-10.x).

