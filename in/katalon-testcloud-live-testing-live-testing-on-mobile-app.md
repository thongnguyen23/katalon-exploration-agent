---
title: "Live testing on mobile app"
---

:::info Prerequisites
- You have an active Katalon TestCloud Live Testing subscription or trial.
:::

Live manual testing is the process of manually interacting in real-time on a live environment. With TestCloud Mobile Live Testing, you can manually perform actions on real iOS and Android devices. This allows you to validate app functionality, and ensure a seamless user experience across a wide range of devices.

Some of the live app testing features include:

* Camera Image Injection, Biometrics authentication, IP geolocation, GPS location, and Network throttling to ensure comprehensive coverage of real-world scenarios.
* Switch Device feature for seamless transitions and significantly enhances the testing process.
* Taking screenshot and session video recording that you can download.

## Perform live testing on mobile app

Follows these steps to perform live testing on mobile app with TestCloud devices.

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

<Tabs>
  <TabItem value="testcloud_web_app" label="TestCloud Web App" default>

1. Log in to the [TestCloud Live Testing](https://cloud.katalon.com/) site. You will arrive at **TestCloud Live Test** homepage.
   <img src="https://tw-cdn.katalon.com/katalon-testcloud/testcloud-live-testing/testcloud-live-test-main-screen.png" alt="Live testing homepage" width="800" />
2. In the left sidebar, expand the **Live Testing** menu and select **Mobile App**.
    <img src="https://tw-cdn.katalon.com/katalon-testcloud/testcloud-live-testing/testcloud-live-mobile-app-screen.png" alt="Live mobile app test configuration page" width="800" />

  </TabItem>
  <TabItem value="testops_gen3" label="TestOps">

1. In [Katalon TestOps](http://platform.katalon.io/) home page, select **TestCloud**. This will direct you to TestCloud Live Testing page.
2. Select **Mobile App**.
   <img src="https://tw-cdn.katalon.com/katalon-testcloud/testcloud-live-testing/live-mobile-app-gen3.png" alt="Live mobile app configuration page" width="800" />
   
  </TabItem>
</Tabs>

3. Specify your device:

    a. Choose an OS: Android or iOS.

    b. Upload your app directly from your machine, or from a URL.

    c. Select the **Brand**, **Device**, and **OS version**. You can also use the search bar to select your device.

4. Click **Start** to launch your session. 
5. Interact with the device screen using the action sidebar.
    <img src="https://tw-cdn.katalon.com/katalon-testcloud/testcloud-live-testing/testcloud-live-mobile-app-test.png" alt="Live mobile app test screen" width="800" />
6. When you're done, click **End Session** to close your current session.

### App settings

Click the settings icon to open the **App settings** dialog. Here you can enable Biometric Authentication and Image Injection features to ensure the app handles authentication methods and media-related processes accurately, providing thorough validation of the app functionality.

<img src="https://tw-cdn.katalon.com/katalon-testcloud/testcloud-live-testing/testcloud-app-settings-dialog.png" alt="Live mobile test app settings" width="700" />


## Action menu

This section explains the available actions when testing on a mobile device.

| Name | Description |
| ---- | ----------- |
| **Home** | Open the device home screen. |
| **App Controls** | The App Controls feature provides programmatic control over the applications installed on the real device:<ul><li>Install New App: Programmatically install new applications on the test device without manual intervention.</li><li>Kill Existing App: Terminate running apps to test scenarios like crash recovery, app restart, or handling unexpected closures.</li><li>Uninstall App: Uninstall the app to validate installation flows, or clean up the environment between tests.</li></ul> |
| **Screenshot** | Take a snapshot of the current screen. The screenshot will be saved in the gallery. |
| **Record Session** | Record your entire test session for detailed analysis and playback. Click on the Record Session button to begin recording. A timer will display the recording duration, helping you pinpoint specific moments during playback. To end the recording, click the Stop button. The recorded video will be saved automatically in the gallery for review. |
| **Gallery** | All screenshots and video recordings from test sessions are stored in the Gallery. To download the screenshots or videos to your local machine, click on the Download icon. **Download All** will download all screenshots and videos. |
| **IP Geolocation** | Simulate website and mobile experiences from over 45 countries by using local IP addresses. This allows you to verify localization features such as language translation, currency change, and time zone changes reflect accurately according to different locations. |
| **GPS Location** | Simulate specific device locations using exact GPS coordinates to evaluate location-based app scenarios. You can enter your preferred location by entering the name of the location, or specify the exact location by entering the latitude and longitude of the location. |
| **Network Throttling** | This feature enables you to test the performance and behavior of your website under different network conditions by simulating different real-world network profiles (2G, 3G, LTE). |
| **Files and Media** | Directly upload files and media from your local machine to the testing environment. |
| **Device Controls** | <ul><li>**Volume:** Adjust the device volume directly within your test session to test audio-related features, such as media playback or notifications.</li><li>**Rotate:** Rotate the device between portrait and landscape to test the responsiveness and adaptability of your web application.</li></ul> |
| **Settings** | <ul><li>**Idle Timeout:** Set the idle timeout for your test session. The minium timeout is 5 minutes and the maximum limit is 45 minutes.</li><li>**Time Zone:** Test how your AUT performs in different time zones.</li><li>**Language:** Set the language for the device's keyboard.</li></ul> |
| **Switch** | Opens the **Device Configuration** window. Click **Switch** to easily change the devices, browsers, and OS versions without ending your current session. |
| **End Session** | Clicking the end session button will close your current session. |