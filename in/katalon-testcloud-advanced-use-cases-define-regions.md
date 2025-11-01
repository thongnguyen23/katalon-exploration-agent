---
title: Define regions
---

In case you want to customize where your automated test session will run and evaluate how your AUT behaves across different regions, TestCloud supports the `region` capability. This allows you to run test on real devices and desktops hosted in specific location.

Currently, TestCloud supports three regions: Europe - `EU`, USA - `US` and Asia-Pacific - `AP`.

1. In Katalon Studio, go to **Project** > **Settings** > **Desired Capabilities** and select **TestCloud**.
2. In the TestCloud settings table, add the `katalon:options` property and set the **Type** as **Dictionary**.
    1. In the **Value** column, add the `region` capability with **String** value type, then specify the region short form. For example, `AP` for Asia-Pacific.
   <img width="600" alt="Configure time zone capability" src="https://tw-cdn.katalon.com/katalon-testcloud/advanced-use-cases/tc-configure-time-zone-and-region.png" />
3. Click **OK** and **Apply & Close** to save the settings.
4. Configure your TestCloud environment and run the test.