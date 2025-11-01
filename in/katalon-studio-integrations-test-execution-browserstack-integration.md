---
title: "BrowserStack integration"
---

The BrowserStack integration helps you execute your tests on BrowserStack Selenium Grid from Katalon Studio instance. To integrate with BrowserStack, you need to execute your test scripts on a remote web server configured in desired capabilities. To learn more about setting up the remote server in desired capabilities, you can refer to this document: [Set up remote server in desired capabilities](/katalon-studio/manage-projects/project-settings/desired-capabilities/set-up-remote-server-in-desired-capabilities-in-katalon-studio).

This article demonstrates how to set up BrowserStack integration.

1. In Katalon Studio, go to **Project Settings** > **Desired Capabilities** > **Remote**. Add the following information:
   
    - **Remote server URL**: use the syntax `http://YOUR_USERNAME:YOUR_ACCESS_KEY@hub-cloud.browserstack.com/wd/hub`. You can find `YOUR_USERNAME` and `YOUR_ACCESS_KEY` values on the BrowserStack Dashboard.
        <img src="https://tw-cdn.katalon.com/katalon-studio/studio-integrations/browserstack-integration/browserstack-access-key.png" alt="BrowserStack access key" width="300" />
    - **Remote server type**: Choose Appium server, then iOS/Android Driver.
        <img src="https://tw-cdn.katalon.com/katalon-studio/studio-integrations/browserstack-integration/browserstack-remote-config.png" alt="BrowserStack remote configuration" width="500" />

2. Refer to [Browserstack Capabilities Generator](https://www.browserstack.com/docs/app-automate/capabilities) page to generate your desired caps. Make sure you select **Legacy** and **W3C Protocol** integration methods.
   <img src="https://tw-cdn.katalon.com/katalon-studio/studio-integrations/browserstack-integration/browserstack-cap-generator.png" alt="BrowserStack capabilities generator" width="600" />
3. Click **Add** to add the `appium:deviceName` and `platformName` values. Add other desired capabilities under a Dictionary-type property named `bstack:options`.
   <img src="https://tw-cdn.katalon.com/katalon-studio/studio-integrations/browserstack-integration/ks-browserstack-remote-caps.png" alt="BrowserStack desired capabilities" width="600" />

4.  Click **Apply and Close** to save the settings.
5.  Upload your mobile app to BrowserStack here: [Upload your app](https://app-automate.browserstack.com/dashboard/v2/get-started#upload-app). Then, copy the application value.
    <img src="https://tw-cdn.katalon.com/katalon-studio/studio-integrations/browserstack-integration/browserstack-upload-your-app.png" alt="Upload app to BrowserStack" width="600" />
6.  To execute your tests with Browserstack Selenium Grid, select **Record Mobile** > **Remote Devices**.
   <img src="https://tw-cdn.katalon.com/katalon-studio/Select_Remote_Devices.png" alt="Select remote devices" width="200" />
7.  Paste the application ID that you copied into the **Cloud Application ID**. Then you can start recording your test case. 

#### Result

You have successfully configured your BrowserStack integration. 
