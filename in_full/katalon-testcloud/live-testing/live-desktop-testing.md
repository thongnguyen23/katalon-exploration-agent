---
title: Live testing on desktop
---

:::info Prerequisites
- You have an active Katalon TestCloud Live Testing subscription or trial.
:::

Live manual testing involves interacting with applications in real time on a live environment. With TestCloud Desktop Live Testing, you can manually perform actions directly on real desktop browsers of macOS and Windows operating systems. This allows you to validate application functionality and ensure a consistent, seamless user experience across various desktop environments.

Some of the live desktop testing features include:
- Switching desktop environment: seamless transitions between operating systems, browsers, and screen resolutions to enhance the testing process.
- Taking screenshot and session video recording that you can download instantly.

## Perform live testing on desktop

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

<Tabs>
  <TabItem value="testcloud_web_app" label="TestCloud Web App" default>

Log in to [TestCloud Live Testing](https://cloud.katalon.com/) site. Navigate to the **Live Testing** section and select **Live Desktop**.

<img src="https://tw-cdn.katalon.com/katalon-testcloud/testcloud-live-testing/testcloud-live-desktop-specify-environment.gif" alt="Specify desktop environment" />

  </TabItem>
  <TabItem value="testops_gen3" label="TestOps">

In [Katalon TestOps](http://platform.katalon.io/) home page, select **TestCloud** > **Desktop Browser**.
   <img src="https://tw-cdn.katalon.com/katalon-testcloud/testcloud-live-testing/live-desktop-browser-gen3.png" alt="Live mobile app test configuration page" width="800" />
  </TabItem>
</Tabs>

Do the following steps:
  1. Enter the **URL of the website**.
     
  2. Select your **Operating System (OS)**: you can expand between the macOS or Windows panels to show supported versions.
     
  3. Select the **browser and browser version** from the list of vailable web browsers and their corresponding versions.
     
  4. Select **screen resolution**: This allows you to test responsive design scenarios and see how your application behaves across various screen sizes.
     
  5. Click **Start** to launch your session.
     
  6. Interact with the AUT using the action sidebar.
   <img src="https://tw-cdn.katalon.com/katalon-testcloud/testcloud-live-testing/testcloud-live-desktop-test-actions.gif" alt="Perform test steps in live desktop" />

  7. When you're done, click **End Session** to close your current session.


## Action menu

This section explains the available actions when testing on a desktope environment.

| Name | Description |
| ---- | ----------- |
| **Screenshot** | Take a snapshot of the current screen. The screenshot will be saved in the gallery. |
| **Record Session** | Record your entire test session for detailed analysis and playback. Upon clicking the Record Session button, a timer will display the recording duration, helping you pinpoint specific moments during playback. To end the recording, click the Stop button. The recorded video will be saved automatically in the gallery for review. |
| **Gallery** | All screenshots and video recordings from test sessions are stored in the Gallery. To download the screenshots or videos to your local machine, click on the Download icon. **Download All** will download all screenshots and videos. |
| **Resolution** | Adjust the screen sizes and resolutions to ensure your AUT looks and behaves correctly on different device configuration. |
| **IP Geolocation** | Simulate website and mobile experiences from over 45 countries by using local IP addresses. This allows you to verify localization features such as language translation, currency change, and time zone changes reflect accurately according to different locations. |
| **Files and Media** | <ul><li>Upload files and media from your local machine to the testing environment.</li><li>Download all files from the Download tab to your local machine.</li></ul> |
| **Chrome Extensions** | Extend browser functionality with custom tools to enhance the testing capabilities and coverages. These extensions can help automate repetitive tasks, assist in accessibility checks, and integrate AI tools into your workflow. |
| **Screen Reader** |  Ensure that applications are usable for all users and compliant to accessibility standards like WCAG (Web Content Accessibility Guidelines). |
| **Settings** | <ul><li>**Idle Timeout:** Set the idle timeout for your test session. The minium timeout is 5 minutes and the maximum limit is 45 minutes.</li><li>**Time Zone:** Test how your AUT performs in different time zones.</li><li>**Keyboard Input:** Set the language for the device's keyboard.</li></ul> |
| **Switch** | Opens the **Device Configuration** window. Click **Switch** to easily change the OS versions, browsers, and resolutions without ending your current session. |
| **End Session** | Clicking the end session button will close your current session. |