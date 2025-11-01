---
title: Enable TestCloud integration in Katalon Studio
---

:::caution Requirements
- You have an active TestCloud license or trial.
- You have an active Katalon Studio Enterprise license.
:::

This document shows you how to set up TestCloud integration in Katalon Studio.

---

1. In Katalon Studio main toolbar, click the Katalon button.
    <img src="https://tw-cdn.katalon.com/katalon-testcloud/KS_Katalon_Platform_integration_button.png" alt="TestOps integration button" width="500" />
    Alternatively, you can go to **Project** > **Settings** > **Katalon Platform** to access the settings.
    
2. Tick the **Enable Katalon Platform Integration** and **Enable TestCloud Integration** checkboxes.Additionally, from Katalon Studio 10.1.0 onwards, you can enable the new TestCloud Hub for better test execution performance.
    <img src="https://tw-cdn.katalon.com/katalon-testcloud/testcloud-integration-enabled-in-ks.png" alt="Enable TestCloud integration" width="700" />
    
    Once the connection is successful, you should see the message *"Integrate with TestCloud successfully!"*.
    
3. Choose your **Project** from the dropdown menu of the Organization you belong to.
  :::note
  If you want to execute tests in TestCloud environment, you need to choose the Organization that has an active TestCloud subscription or trial.
  :::
4. Click **Apply & Close**.

You can start running tests in TestCloud environments: desktop browsers, mobile browsers, or mobile native apps depending on your subscription.