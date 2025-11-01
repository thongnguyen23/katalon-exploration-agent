---
title: Set desired capabilities for TestCloud environment
---

When running web or mobile tests in **TestCloud** environments, where you set desired capabilities depends on two factors:
- The **execution source** (TestOps or Katalon Studio)
- The **test environment** (desktop, mobile, or cross-platform)

This guide shows you how to configure desired capabilities based on your execution settings.

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

<Tabs>
  <TabItem value="testops" label="Run from TestOps" default>

  ### For Linux

  To run desktop browser tests  on Linux, define desired capabilities just as you would for local execution in Katalon Studio:
  - Go to **Project Settings** > **Desired Capabilities** > **WebUI**
  - Choose your browser: **Chrome**, **Firefox**, or **Edge**
  
  For detailed instructions, refer to [Set up desired capabilities for WebUI testing in Katalon Studio](https://docs.katalon.com/katalon-studio/manage-projects/project-settings/desired-capabilities/set-up-desired-capabilities-for-webui-testing-in-katalon-studio).


  ### For Windows/macOS or Mobile

  To run desktop browser tests on Windows/macOS or mobile browser/app tests, set the capabilities in **Project Settings** > **Desired Capabilities** > **TestCloud**. This applies for all non-Linux environments when executed from TestOps.
  <img src="https://tw-cdn.katalon.com/katalon-testcloud/tc-desired-caps-table.png" width="600" alt="TestCloud desired capabilities table" /> <br/>

  ### Cross-platform

  For test runs that target multiple platforms, set desired capabilities as follows:
  - **Linux**: Set capabilities in **WebUI** (Chrome/Firefox/Edge)
  - **Windows/macOS**, **mobile browser**, **mobile app**: Set capabilities in **Project Settings** > **Desired Capabilities** > **Remote**.
  <img src="https://tw-cdn.katalon.com/katalon-testcloud/testcloud-cross-platform-remote.png" width="600" alt="Remote desired caps settings" />

  </TabItem>

  <TabItem value="ks" label="Run from Katalon Studio">

  If your tests are triggered directly from Katalon Studio, set desired capabilities in **Project Settings** > **Desired Capabilities** > **TestCloud**. This will apply to all platform: Linux, Windows/macOS, or mobile.

  <img src="https://tw-cdn.katalon.com/katalon-testcloud/tc-desired-caps-table.png" width="600" alt="TestCloud desired capabilities table" />

  </TabItem>
</Tabs>

---

## **Supported desired capabilities**

### Desktop Browser

The following are exemplary capabilities supported for desktop browser testing.

- `acceptInsecureCerts`: Bypass or implicitly trust TLS certificates that are not recognized by the browser’s certificate authority.
- **Browser-specific** (`goog:chromeOptions`, `moz:firefoxOptions`, or `ms:edgeOptions`): <br/>
  - `profile.password_manager_leak_detection`: Bypass the "Change your password" popup.
  - `profile.managed_default_content_settings.javascript`: Disable JavaScript during automated test runs.
- `katalon:options` capabilities that are supported for TestCloud only on Windows/macOS (not supported for Linux): <br/>
  
  - `geoLocation`
  - `enableNetwork`
  - `enableNetworkThrottling`

### Mobile

The following are exemplary capabilities supported for mobile testing.

- `appium:autoGrantPermissions`: Automatically grant all permissions required by the app.
- `appium:autoAcceptAlerts`: Automatically accept all system alerts (e.g., tap “Continue”).
- `appium:autoDismissAlerts`: Automatically dismiss all system alerts (e.g., tap “Don't allow”).
- The following `katalon:options` capabilities are supported for TestCloud only on Windows/macOS (not supported for Linux): <br/>

  - `enableImageInjection`
  - `enableBiometricsAuthentication`
  - `geoLocation`
  - `enableNetwork`
  - `enableNetworkThrottling`
  - `enableAppProfiling`
  - `appiumVersion`