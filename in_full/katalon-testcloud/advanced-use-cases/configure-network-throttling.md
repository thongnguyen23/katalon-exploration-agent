---
title: Configure network throttling
---

:::caution Requirements
- You have installed the Katalon TestCloud Keywords plugin to automatically load all TestCloud keywords into your project without having to manually define them. If you have not, visit Katalon Store: [Katalon TestCloud keywords](https://store.katalon.com/product/397/Katalon-TestCloud-Keywords).
- This keyword is applicable for desktop browser testing (Windows, macOS), mobile browser testing, and mobile native app testing.
:::

There might be scenarios where you would have to check the functionality of your website or mobile app on poor network conditions or even offline. Such networks have variable upload and download speeds which can alter how your website performs on different browsers.

With Network throttling feature, you can test the performance and behavior of your website under different network conditions by simulating different network profiles.

The `ThrottleNetworkExecutor` contains 2 keywords for the following use cases:

1. `setNetworkProfile`:
    - When testing with **mobile app**, the keyword throttles network for mobile devices by profile.
        
        | **Profile Name** | **Download Speed** | **Upload Speed** | **Latency** |
        | --- | --- | --- | --- |
        | 2g-gprs-poor | 20 Kbps | 6 Kbps | 1000 ms |
        | 2g-gprs-good | 50 Kbps | 16 Kbps | 500 ms |
        | 3g-umts-poor | 200 Kbps | 64 Kbps | 400 ms |
        | 4g-lte-poor | 1 Mbps | 500 Kbps | 200 ms |
        | 3g-umts-good | 5 Mbps | 2 Mbps | 100 ms |
        | 4g-lte-good | 15 Mbps | 7 Mbps | 70 ms |
        | 4g-lte-advanced-good | 25 Mbps | 12 Mbps | 20 ms |

    - When testing with **web**, the keyword throttle network for web browsers by profile.
        
        | **Profile Name** | **Download Speed** | **Upload Speed** | **Latency** |
        | --- | --- | --- | --- |
        | offline | 0 Kbps | 0 Kbps | 0 ms |
        | GPRS | 50 Kbps | 20 Kbps | 500 ms |
        | Regular 2G | 250 Kbps | 50 Kbps | 300 ms |
        | Good 2G | 450 Kbps | 150 Kbps | 150 ms |
        | Regular 3G | 750 Kbps | 250 Kbps | 100 ms |
        | Good 3G | 1 Mbps | 750 Kbps | 20 ms |
        | Regular 4G | 4 Mbps | 3 Mbps | 20 ms |
        | DSL | 2 Mbps | 1 Mbps | 5 ms |

2. `customNetworkProfile`: provide arbitrary values for network throttling.

--- 

To configure network throttling with TestCloud, follow these steps:

1. In Katalon Studio, click the **Profile** drop-down and select **Reload Plugins** to make sure the plugin is installed.
    
    <img width="500" alt="Reload plugins" src="https://tw-cdn.katalon.com/katalon-testcloud/advanced-use-cases/KS_TestCloud_plugin.png" />
    
2. Go to **Project Settings** > **Desired Capabilities** > **TestCloud**.
3. In the TestCloud table, add a `katalon:options` property, set **Type** as `Dictionary`, then click the `...`.
    
    <img width="600" alt="Desired capabilities table" src="https://tw-cdn.katalon.com/katalon-testcloud/advanced-use-cases/KS_TestCloud_desired_caps_menu.png" />
    
4. In the **Dictionary Property Builder**, set the boolean `enableNetworkThrottling=True` desired capability for your project. Then, click **OK**.
    
    <img width="600" alt="Network throttling desired cap" src="https://tw-cdn.katalon.com/katalon-testcloud/advanced-use-cases/KS_TestCloud_network_throttling.png" />
    
5. Add the `ThrottleNetworkExecutor` keyword to your test case as needed.
    
    <img width="600" alt="Add network throttling keyword to test case" src="https://tw-cdn.katalon.com/katalon-testcloud/advanced-use-cases/add-testcloud-custom-keyword.png" />
    
6. Configure your TestCloud environment and run the test.