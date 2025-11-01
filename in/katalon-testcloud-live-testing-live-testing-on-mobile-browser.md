---
title: "Live testing on mobile browser"
---

:::info Prerequisites
- You have an active Katalon TestCloud Live Testing subscription or trial.
:::

Live testing is the process of manually interacting on a live environment. TestCloud live mobile browser testing enables testers to perform real-time testing across multiple devices, operating systems, and browsers directly from their machine. This feature simplifies the process of verifying web applications against diverse screen sizes, hardware capabilities, and network conditions.

Some of the live browser testing features include:

* Switch Device feature for seamless transitions and significantly enhances the testing process.
* Taking screenshot and session video recording that you can download.

This guide shows you how to perform live mobile browser testing.

### Perform live testing on mobile browser
You can access live mobile browser testing from [TestCloud web app](https://cloud.katalon.com/) or [Katalon TestOps](https://platform.katalon.io/).

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

<Tabs>
  <TabItem value="testcloud_web_app" label="TestCloud Web App" default>

1. Log in to the [TestCloud Live Testing](https://cloud.katalon.com/) site. You will arrive at **TestCloud Live Test** homepage.
   <img src="https://tw-cdn.katalon.com/katalon-testcloud/testcloud-live-testing/testcloud-live-test-main-screen.png" alt="Live testing homepage" width="800" />
2. In the left sidebar, go to **Live Testing > Mobile Browser**. This will open the device selection page.
   <img src="https://tw-cdn.katalon.com/katalon-testcloud/testcloud-live-testing/testcloud-mobile-browser-list.png" alt="Live mobile browser test configuration page" width="800" />

  </TabItem>
  <TabItem value="testops_gen3" label="TestOps">

1. In [Katalon TestOps](http://platform.katalon.io/) home page, select **TestCloud**. This will direct you to TestCloud Live Testing page.
2. Select **Mobile Browser**.
   <img src="https://tw-cdn.katalon.com/katalon-testcloud/testcloud-live-testing/live-mobile-browser-gen3.png" alt="Live mobile browser test configuration page" width="800" />
   
  </TabItem>
</Tabs>


3. Enter the Application URL and select a device:
    
    a. Provide the URL of your application under test (AUT).
    
    b. Choose the target device for testing.

    c. Switch between Android and iOS platforms as needed.
    
    d. Select a platform-specific browser to test your application.

4. Click **Start** to launch your session. 
5. Interact with the device screen in real time using the action sidebar.
    <img src="https://tw-cdn.katalon.com/katalon-testcloud/testcloud-live-testing/testcloud-mobile-browser-test-screen.png" alt="Live mobile browser test screen" width="800" />
6. When you're done, click **End Session** to close your current session.

## Action menu
This section explains the available actions when testing on a mobile device.

| Name | Description |
| ---- | ----------- |
| **Home** | Open the device home screen. |
| **Screenshot** | Take a snapshot of the current screen. The screenshot will be saved in the gallery. |
| **Record Session** | Record your entire test session for detailed analysis and playback. Click on the Record Session button to begin recording. A timer will display the recording duration, helping you pinpoint specific moments during playback. To end the recording, click the Stop button. The recorded video will be saved automatically in the gallery for review. |
| **Gallery** | All screenshots and video recordings from test sessions are stored in the Gallery. Select Gallery from the left toolbar to access the saved screenshots and videos. To download the screenshots or videos to your local machine, click on the Download icon. **Download All** will download all screenshots and videos. |
| **IP Geolocation** | Simulate website and mobile experiences from over 45 countries by using local IP addresses. This allows you to verify localization features such as language translation, currency change, and time zone changes reflect accurately according to different locations. |
| **GPS Location** | Simulate specific device locations using exact GPS coordinates to evaluate location-based app scenarios. You can enter your preferred location by entering the name of the location, or specify the exact location by entering the latitude and longitude of the location. |
| **Network Throttling** | This feature enables you to test the performance and behavior of your website under different network conditions by simulating different real-world network profiles (2G, 3G, LTE). |
| **Device Controls** | <ul><li>**Volume:** Adjust the device volume directly within your test session to test audio-related features, such as media playback or notifications.</li><li>**Rotate:** Rotate the device between portrait and landscape to test the responsiveness and adaptability of your web application.</li></ul> |
| **Settings** | <ul><li>**Idle Timeout:** Set the idle timeout for your test session. The minium timeout is 5 minutes and the maximum limit is 45 minutes.</li><li>**Time Zone:** Test how your AUT performs in different time zones.</li><li>**Language:** Set the language for the device's keyboard.</li></ul> |
| **Switch** | Opens the **Device Configuration** window. Click **Switch** to easily change the devices, browsers, and OS versions without ending your current session. |
| **End Session** | Clicking the end session button will close your current session. |