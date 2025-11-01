---
title: Configure Appium version
---

TestCloud provides the flexibility to specify the desired Appium version to match your testing requirements. By default, TestCloud automatically selects the appropriate Appium version based on the device's operating system. However, you also have the option to explicitly define the version by using the `appiumVersion` capability in your test scripts.

The supported Appium versions include:

- `latest`: `2.12.1` for iOS 15 and above, and all Android versions; or `2.13.1` based on compatible model
- `default`: `2.2.1` for iOS below 15. `2.4.1` for iOS 15 and above, and all Android versions
- Specific Appium versions: `2.11.2`, `2.10.3`, `2.5.4`, `2.4.1`, `1.22`

:::note
- It is recommended to always declare the suitable and supported `appiumVersion` for your device OS in the desired capabilities settings to avoid errors. It is recommended to use `latest` or `default`.
- For iOS 17 and above, use Appium version `2.11.2` and above to ensure the best compatibility and performance.
:::

1. In Katalon Studio, go to **Project** > **Settings** > **Desired Capabilities** and select **TestCloud**.
2. In the TestCloud settings table, add the `katalon:options` property and set the **Type** as **Dictionary**.
    1. In the **Value** column, add the `appiumVersion` capability with **String** value type, then specify the version tag.
    <img width="800" alt="Set Appium version for TestCloud" src="https://docs.katalon.com/f35c579e-186f-41ec-8d94-0bfea4c07a2e/testcloud-appium-version-desired-caps.png" />
    
3. Click **OK** and **Apply & Close** to save the settings.
4. Configure your TestCloud mobile environment and run the test.