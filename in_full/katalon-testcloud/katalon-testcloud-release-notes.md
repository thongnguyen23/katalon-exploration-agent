---
title: Katalon TestCloud Release Notes
---

## September 11, 2025

### New features
- Introduced Parallel Test Case Execution: The capability to run individual test case in parallel within a test suite or across test suites, filling all available sessions. This enhancement speeds up your test runs by executing multiple test cases at the same time, optimizing resource use while keeping a buffer of sessions available. Learn more in our documentation: [Parallel test case execution](/katalon-testcloud/parallel-test-case-execution).
- Support `passcode` capability for private device: Users need to pass the desired cap in Project settings to enable passcode feature in the `katalon:options`.

## August 27, 2025

### Enhancements
- Improved automated test run creation with advanced environment configuration:
  - Support configuring OS and device using Regular Expression (RegEx).
  - Mixed UI & API testing with tunnel.
  - Improved flow and stability for mobile application testing.
  - Select multiple configurations for a single test suite, while maintaining a single configuration per suite in a test suite collection.
- Improved display of the application version and build number for better visibility and clarity.
- Improved error message when a deprecated Appium version is entered.
 
## July 31, 2025

### New features
- Introduced **Smart Retry** feature: Automatically re-executes tests that fail due to infrastructure or deployment errors (`5xx` status codes). This intelligent mechanism ensures your critical test runs complete successfully without manual intervention.
- Added the ability to terminate TestCloud execution from Katalon Studio and TestOps directly in [TestCloud Web App](https://cloud.katalon.com/).
- Supported displaying the **File name** of the mobile app in the **Application** page. This allows users to quickly differentiate between various builds of an application, even if they share the same app name.
  
### Enhancements
- Updated latest value of Appium version to `2.12.1` or `2.13.1` depending on the device model.

### Fixes
- Fixed the issue where Tunnel client shows successful connection but fails to connect over UDP due to network restrictions.

## July 16, 2025

### New features
- Introduced Private database testing using TestCloud tunnel. This feature allows users to connect to their private resources (e.g., databases, SSH services, internal APIs) when running data-driven tests. Learn more about this feature: [Private database testing](/katalon-testcloud/local-testing-with-testcloud/private-database-testing).

### Enhancements
- Added support for `timezone` capability: Users can ensure their AUT performs as expected by customizing different time zones for their AUT. Refer to this guide for more details: [Configure time zones](/katalon-testcloud/advanced-use-cases/configure-time-zones).
- Added support to execute test with KRE 10.2.3 for TestCloud on TestOps.
- Added Safari version 18 and 19 compatibilities on macOS.

### Fixes
- Fixed an issue where the build version number was lost after editing the configuration.
- No error message was shown when the Git repository failed to clone.


## July 9, 2025

### Enhancements
- [TestCloud Tunnel] Improve the performance of tunnel client to remain active across sessions.


## June 25, 2025

### New features
- [TestCloud execution monitor] Introduced **Network Logs**: where you can view the browser’s detailed performance data, real-time record of all API calls, network requests, and responses exchanged between the application under test (web, mobile, API) and its backend services during an automated test run. It includes request/response headers, bodies, status codes, and timings in the HAR format. Learn more at [Network logs](/katalon-testcloud/debug/view-network-and-performance-data#network-logs).
- [TestCloud execution monitor] Introduced **App Profiling**: a board of comprehensive metrics (CPU usage, Memory usage, Disk usage, Network usage, Temperature, Battery consumed, Rendering, Frame issues, Responsiveness, etc.) that provides unparalleled visibility. Learn more at [App profiling](/katalon-testcloud/debug/view-network-and-performance-data#app-profiling).

### Enhancements
- Improved the device queuing mechanism to reduce the risk of timeouts and prevent unnecessary test failures. This ensures your overall success rate where your tests will run when resources are fully ready.
- Added Chrome 134, 135, 136, 137 and Firefox 135, 136, 137, 138 compatibilities for Linux.
- Removed `beta` label for Live Testing in the [TestCloud Web App](https://cloud.katalon.com/).

### Fixes
- Fixed the issue where the app's metadata is not displayed on the monitor view.
- Videos and logs were not collected when a session was cancelled.
- Fixed the issue where the file extension was missing in the video downloaded from [TestCloud Web App](https://cloud.katalon.com/).

## June 11, 2025

### New features
- Introduced Live Testing feature that supports all environments available in Katalon TestCloud, including desktop browsers, mobile browsers, and mobile native applications. You can try Live Testing with your existing TestCloud subscription on [TestOps](https://platform.katalon.com) or [TestCloud Web app](https://cloud.katalon.com).
  - Live Testing allows manual testers to perform manual testing on remote environments without the hassle of setting up local devices. 
  - **Advanced Testing Capabilities**: Supporting Camera Image Injection, Biometrics authentication, IP geolocation, GPS location, and Network throttling ensures comprehensive coverage of real-world scenarios.
  - **Enhanced Device Control**: The ability to manage font settings (idle timeout, timezone, language), recent apps, volume, and rotation provides complete control, clipboard fetching, ensuring flexibility and ease of use.
  - **Switch Device Feature**: This feature is nothing short of extraordinary. It provides users with seamless transitions and significantly enhances the testing process.
  - **Developer Tools Access**: Enabling users to work directly with DevTools adds immense value for debugging and fine-tuning.
  - Take screenshot and record video for a session
- [Real-time TestCloud execution monitor] View Selenium/Appium commands after the test finishes.
  - Click a screenshot taking command to view the corresponding screenshot and video timestamp.
- Added support to configure KRE agents at the Account level and Project level. See [Create and manage KRE Agents](/katalon-platform/administer/administration-and-licensing-alternate/manage-systems/configurations/create-and-manage-kre-agents) and [Connect KRE Agent to your project](/katalon-platform/administer/administration-and-licensing-alternate/manage-projects/connect-kre-agent-to-your-project).

### Enhancements
- Video recordings now include the test suite name in their file path, making it easier to identify which suite they belong to.
- [TestCloud keywords plugin] When running a mixed web & app test, you can now view two separate videos - one for web and one for app execution in the **File** tab after the test run completes.
  
### Fixes
- Fixed the issue where sessions were stopped even when `closeBrowser` or `closeApplication` steps were disabled in the test case, ensuring these steps are ignored and the session remains open.

## May 14, 2025

### Enhancements

- **Live TestCloud Executions Monitoring and Live Video Streaming**:
  - Displays video recordings, Selenium/Appium logs, and device logs after test executions triggered from TestOps or Katalon Studio.
    - Known limitation: This feature is not yet supported on Linux and macOS.
- Specified `lalest` tags for KRE  by versions in **Advanced settings** of the **Schedule Test Run** dialog. There are 3 `latest` options:
  - Latest: the newest KRE version that is compatible with TestCloud
  - Latest 9.x: newest version of 9.x
  - Latest 10.x: newest version of 10.x
  - **Default selection**: Latest 10.x
  - For existing schedules are configured with the `latest` tag will be migrated to latest 9.x (9.7.5)
  
### Fixes
- Unable to parse execution sessions from a zipped script repository.
- KRE logs were not uploaded after cancelling sessions that are executed with a zipped repo.
- 400 error code thrown when searching with keywords that contains space in the **Application Repository**.

## April 23, 2025

### New features

- Introduced **Live Video Streaming**: You can now watch real-time video feed of your web or app as your automated tests run. This feature allows users to visually monitor the test progress and spot any UI issues, errors, or unexpected behavior instantly, without having to wait for the test to finish.
  - Known limitation: This feature is not yet supported on Linux and macOS. Nevertheless, users can view videos with macOS after the tests finish (for KS executions). 
- SmartWait and SmartLocator are supported when running tests on TestCloud from Katalon Studio 9.x, 10.x, and TestOps.
- Enable KRE 9.7.5, 10.1.1, and 10.1.2 for TestCloud executions on TestOps. 

### Enhancements

- You can now customize TestCloud environments using Regular Expression includes OS version and device name. 
- You can now update the application for multiple or all test suites within a test suite collection without needing to reselect devices.

### Fixes

- Fixed an issue where disabled test suites in a test suite collection were still executed when retriggering a test run configuration.

## April 9, 2025

### New features

- Introduced **Live TestCloud Execution Monitoring (Phase 1)**: this feature allows you to to observe and interact with TestCloud test execution in real-time as they are running on remote devices or virtual machines.
  - Faster Debugging: Quickly identify and diagnose issues as they occur.
  - Increased Efficiency: Reduce the time spent waiting for test results and manually reproducing issues.  
  - Enhanced Visibility: Gain a deeper understanding of how your tests are performing in different environments.
  - Better Quality: Identify and fix bugs earlier in the development cycle.
  - Known limitations: 
    - Live testing: logs, videos, environments will be empty
    - Linux: no logs, videos. This will be addressed in phase 3
    - Executions triggered from TestOps: no video. This will be addressed in phase 2

### Enhancements

- [TestCloud Tunnel] Removed active tunnel sessions if the relay endpoints are no longer valid; Tunnel metadata is updated correctly when no active tunnel; Implementing a re-connection mechanism to handle flaky connections.
- [New TestCloud Automation Hub]:
  - Displayed `katalon:caps` in Log Viewer
  - Displayed exact device and browser version when running/recording tests with Any Device, Public and Private Device
  - Supported BiDi/Sel4 functions tests
  - Improved Queue timeout status and message 
  - Get test artifacts when sessions are idle timeout

## February 26, 2025

### New features

* Introduced **TestCloud Automation Hub** (Beta), a faster and more reliable solution for running Selenium tests in TestCloud.
  * Better performance – Faster test execution.
  * Higher availability to ensure consistent uptime.
  * Improved scalability to handle larger workloads efficiently.
  * Unified execution for Katalon Studio, TestCloud Agent, and KRE.
  * **Supported features**
    * All TestCloud environments (Windows, Linux, macOS, mobile browsers, native mobile apps).
    * Mobile Record & Playback.
    * TestCloud keywords from the TestCloud keyword plugin.
  * The option is available from Katalon Studio 10.1.0 onwards. To enable the new Hub, once Katalon TestCloud integration is enabled, you can switch between the legacy and new Hub in **Project Settings**. The legacy Hub is selected by default.
  * **Limitations**
    * The Upload File keyword is not supported on Linux.
    * Private/local testing is unavailable.
* You can now customize mobile OS version when executing tests with TestCloud using regular expression.
* Added support for TestCloud tunnel and HTTP2/TCP type connection.

### Enhancements

* [Linux] Added support for Chrome 131, 132 and Firefox 132, 133, 134.
* Users can find which device was run when the ‘Any’ option is selected in the name of videos and logs:  `...<browser/platformName>_<deviceName>_<test case name>....`. For example , `1_android_Pixel 9 Pro XL_Simple Start App 3 times_1736841461001_1736841355004.mp4`.
* KRE 10.1.0 is now available for running tests with TestCloud on TestOps. However, due to significant changes from KRE 9.x to 10.0, we will keep KRE 9.7.4 as the latest version until there is higher demand for KRE 10.x.
  * If you select 'latest', but the browser is supported by KRE 8.x, the test will still run with KRE 8.x.
  * If you explicitly select KRE 10.1.0, the test will run with KRE 10.1.0.
* [Live Testing] Setting URL field is required for Mobile Browser Live Testing.
* Resolved compatibility issues with HTTP proxy.

### Fixes

* Error *"Browser execution env not found"* displayed when running when running tests on macOS Safari versions earlier than 17.
* The version and build icons in **Application Repository** did not display as expected.

## January 15, 2025

### New features

* Introduced the new Mobile Live Testing (Beta) with support for Mobile App and Mobile Browser testing. The following features are supported:

  * **Advanced Testing Capabilities**: Camera Image Injection, Biometrics authentication, IP geolocation, GPS location, and Network throttling to ensure comprehensive coverage of real-world scenarios.
  * **Enhanced Device Control**: The ability to manage font settings (idle timeout, timezone, language), recent apps, volume, and rotation provides complete control, clipboard fetching, ensuring flexibility and ease of use.
  * **Switch Device feature**: Seamless transitions and significantly enhances the testing process.
  * **Developer Tools Access**: You can work directly with DevTools adds immense value for debugging and fine-tuning.
  * Taking screenshot and Session video recording.
  
* Introduced the new [TestCloud Web App](https://cloud.katalon.com). You can access Mobile Live Testing, view TestCloud session information, and upload and manage applications that are used for automation testing.

### Enhancements

* [TestOps] Added support for KRE 10.0.1 and 9.7.4 for test execution with TestCloud on TestOps.
  
* [TestOps] Revised tooltips across the **Application Repository** and **Schedule Test Run** dialog for consistency and clear information about app versions and builds for iOS and Android.

* [Katalon Studio] Added support video recording when running with TestCloud Linux.

* [Katalon Studio] Reports (HTML, PDF) now display the name of the actual device used during test execution when the 'Any' option is selected from the TestCloud device list.

* Screenshots and test artifacts are now uploaded to TestOps even if the test session times out or is canceled while running on Windows, macOS, or mobile environments.

* Updated default value of Appium version.

### Fixes

* Fixed the issue when running tests with Katalon Studio 10.x sometimes throws invalid device or a "404 Not Found" error.

* Displayed incorrect device name in **Summary** tab.
  
## November 27, 2024


### New features

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">Added support for Selenium 4.</p></li><li className="li"><p className="p">Added support for Katalon Runtime Engine (KRE) 10.0.0. However, due to major changes between KRE 9.x and 10.0,  the  KRE version for the <span className="ph uicontrol">Latest</span> option is 9.7.3 until we observe high demand on KRE 10.0.</p></li></ul> 

### Enhancements

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">Improved performance and stability when collecting test artifacts.</p></li><li className="li"><p className="p">[TestCloud Keyword plugin] Added Katalon Studio and KRE version 10.0.0 compatibilities.</p></li><li className="li"><p className="p">[TestOps] Added <code className="ph codeph">runFromTestCloud = true</code> capability to <code className="ph codeph">katalon:options</code> for KRE version 10.x.</p></li><li className="li"><p className="p">Improved format consistency for desired capabilities configuration by nesting all desired capabilities in  <span className="ph uicontrol">Dictionary Property Builder</span> of <code className="ph codeph">katalon:options</code>.</p></li></ul> 

## November 6, 2024


### Enhancements

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><div className="p">Rearranged  device list within the same OS version  based on availability status:<ul className="ul"><li className="li"><p className="p">From High,   Medium, to Low availability</p></li><li className="li"><p className="p">For devices with the same availability status, we arrange by alphabetical order.</p></li></ul></div></li><li className="li"><p className="p">Enabled the <span className="ph uicontrol">Terminate</span> button in the <span className="ph uicontrol">History</span> page for tests run on Local Agent.</p></li><li className="li"><p className="p">Added <code className="ph codeph">profiling:true</code> desired capability to track key performance metrics for mobile applications during automated testing, such as CPU consumption and network usage.</p></li><li className="li"><p className="p">You can upload mobile app up to 1GB in size. If a file exceeds the 1GB limit, an error message will appear.</p></li></ul> 

## October 16, 2024


### Enhancements

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">Users can configure Appium version in the TestCloud desired capabilities settings using <code className="ph codeph">appiumVersion</code>. If not specified, by default, TestCloud automatically selects the appropriate Appium version based on the device's OS.</p></li><li className="li"><p className="p">Minor enhancements with TestCloud desired capabilities.</p></li></ul> 

### Fixes

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">[Private device] Fixed the issue where Katalon Studio did not recognize the Private device license and the test execution failed with <code className="ph codeph">Not enough parallel quota</code> message.</p></li></ul> 

## September 25, 2024


### New features

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">When executing a test suite collection, users can now select specific mobile app for each test suite instead of one app for all test suites.</p></li></ul> 

### Enhancements

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">Added support for Chrome, Firefox, and Edge browser versions 125, 126, and 127 on Windows, Linux, and macOS.</p></li></ul> 

### Fixes

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">Resolved an issue of no video generated after a mobile native app test execution.</p></li><li className="li"><p className="p">Resolved the error message issue when executing a native app session on Katalon Studio with an unavailable device.</p></li><li className="li"><p className="p">Fixed an issue regarding <code className="ph codeph">goog:chromeOptions</code> capability when running mobile browser test on Katalon Studio.</p></li><li className="li"><p className="p">Fixed an issue where the tunnel client status remained 'Active' due to user actions or desktop task termination.</p></li></ul> 

## August 28th, 2024


### Fixes

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">[Native mobile application testing] Fixed the issue where the <em className="ph i">"Invalid app ID"</em> error message  did not appear when    starting a session with a device that has an invalid app ID.</p></li></ul> 

## August 14, 2024


### Enhancements

<div xmlns="http://www.w3.org/1999/xhtml" className="p">TestCloud Tunnel:<ul className="ul"><li className="li">When scheduling from the <span className="ph uicontrol">Schedule Test Run</span> dialog, users can choose which tunnel to run local tests from the list of available tunnels.</li><li className="li">Users can execute UI tests that also include API calls by checking the <span className="ph uicontrol">Also Include API Calls</span> option.</li><li className="li">The new tunnel version comes with enhanced performance and stability.</li></ul></div>

### Fixes

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">Resolved the naming issues of test report video.</li><li className="li">Resolved the issue where the <span className="ph uicontrol">Schedule Test Run</span> dialog could not display more than 300 test suite collections.</li></ul> 

## July 30, 2024


### Enhancements

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Upgraded Appium to version 2.4 to ensure compatibility with Katalon Studio keywords.</p> 

## July 10, 2024


### New features

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">Supported the Katalon TestCloud Keywords plugin on Katalon Store to help users automatically load TestCloud keywords into Katalon projects. This eliminated the need for manual definition of keywords. See: <a className="xref j-external-link" href="https://store.katalon.com/product/394/Katalon-TestCloud-Keywords" target="_blank">Katalon Store</a> and <a className="xref" href="/katalon-testcloud/advanced-use-cases/download-and-verify-files">Download and verify files</a>.</p></li><li className="li"><p className="p">Supported beta and dev versions of browsers on Windows and macOS. These un-official versions are tagged with <kbd className="ph userinput">dev</kbd> or <kbd className="ph userinput">beta</kbd> when you select execution environment in the <span className="ph uicontrol">Schedule Test Run</span> dialog.</p></li></ul> 

### Enhancements

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">Supported KRE 9.6 as the latest version for TestCloud execution.</p></li><li className="li"><p className="p">Allowed Organization Owner and Admin to turn off tunnel clients. Previously, only the user who initiated a tunnel client could stop it. This is particularly helpful if the original owner is no longer part of the team, ensuring efficient resource utilization and security.</p></li></ul> 

### Fixes

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">Native mobile application testing: Added error message when the application does not match the device's OS. Previously, users had to wait for 15 minutes.</p></li><li className="li"><p className="p">Testing with private devices: Added clearer error message when the device is de-allocated.</p></li></ul> 

## July 3, 2024


### Fixes

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Fixed execution errors with web service tests on private domain with TestCloud tunnel.</p> 

## May 29, 2024


### New features

<p xmlns="http://www.w3.org/1999/xhtml" className="p">TestCloud private device: Introduced TestCloud private mobile devices that are dedicated to your organization, allowing you to have more control over the test devices with a private environment, enhanced data privacy, and better session retention. See: <a className="xref" href="/katalon-testcloud/private-mobile-devices/use-testcloud-private-mobile-devices">Use TestCloud private mobile devices</a>.</p> 

### Enhancements

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Supported Katalon Runtime Engine 9.4.0 as the latest version for TestCloud.</p> 

### Fixes

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Fixed the issue where video recording are not named correctly when executing test suite with <span className="ph uicontrol">Retry after executing all</span> option.</p> 

## May 22, 2024


### Enhancements

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Updated latest browser version for Windows, Linux, and macOS (Chrome 124, Firefox 124, and Edge 124).</p> 

## April 24, 2024


### Enhancements

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">Updated latest browser version for Windows, Linux, and macOS (Chrome 123, Firefox 123, and Edge 123).</p></li><li className="li"><p className="p">Users can copy the application ID of uploaded mobile application to clipboard with the <em className="ph i">Copy AppID to clipboard</em> button in Application repository.</p></li></ul> 

### Fixes

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">Naming of video reports: Fixed the issue with misnaming video reports when using the <code className="ph codeph">openBrowser</code> and <code className="ph codeph">startApplication</code> keywords.</p></li><li className="li"><p className="p">Fixed incorrect Visual testing statuses in the <span className="ph uicontrol">History</span> page.</p></li></ul> 

## April 1, 2024


### New Features

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">Supported setting geographic location. Users can dynamically set geolocation for web and mobile test execution. See: <a className="xref" href="/katalon-testcloud/advanced-use-cases/set-geographic-location">Set geographic location</a>.</p></li><li className="li"><p className="p">Supported network throttling. Users can simulate network conditions for web and mobile test execution. See: <a className="xref" href="/katalon-testcloud/advanced-use-cases/configure-network-throttling">Configure network throttling</a>.</p></li></ul> 

### Enhancements

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">Updated latest browser version for Windows, Linux, and macOS with Chrome 122, Firefox 122, and Edge 122.</p></li><li className="li"><p className="p">Supported executing with KRE version 8.6.9 and 9.3.2 in TestCloud environment.</p></li></ul> 

## March 14, 2024


### Enhancements

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Mobile native application testing: When users select a mobile application build in the <span className="ph uicontrol">Schedule Test Run</span> dialog, the builds are displayed along with their upload dates. This help users distinguish between multiple builds of the same application version.</p> 

## February 28, 2024


### New features

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">Added keywords for simulating biometric authentication in mobile testing. See: <a className="xref" href="/katalon-testcloud/advanced-use-cases/biometric-authentication-for-native-mobile-application">Biometric authentication</a>.</p></li><li className="li"><p className="p">Updated the latest browser version for Windows, Linux and macOS, with Chrome 121, Firefox 121, Edge 121.</p></li></ul> 

### Enhancements

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">Supported Smart Wait: When Smart Wait is enabled in a project in Katalon Studio, TestCloud can execute test suites of the project with Smart Wait.</p></li><li className="li"><p className="p">Supported Katalon Runtime Engine 9.3 as the latest version in Test Run Scheduler.</p></li></ul> 

### Fixes

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">History page: Fixed the issue where duplicated profiles are displayed in a row.</p></li><li className="li"><p className="p">History page: Displayed the full list of failed test results <span className="ph uicontrol">Failed Test Result</span> and <span className="ph uicontrol">Sessions</span>, instead of limiting to only 50 items.</p></li></ul> 

## January 31, 2024


### New features

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">Introduced the new <span className="ph uicontrol">History</span> interface that helps users easily track, search, and filter all created test runs. See: <a className="xref" href="/katalon-platform/execute/view-execution-history">View execution history</a>. </p></li><li className="li"><p className="p">Updated the latest browser version for Windows, Linux and macOS, with Chrome 120, Firefox 120, Edge 120, and Safari 17.</p></li><li className="li"><p className="p">Enabled executing tests from uploaded zip repositories.</p></li></ul> 

### Enhancements

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">Users can now run test suite collection in TestCloud with the pre-configured <span className="ph uicontrol">retry</span> setting for each test suite from Katalon Studio.</p></li><li className="li"><p className="p">Mobile testing can be executed successfully with mobile devices that are compatible with Appium 2.x.</p></li><li className="li"><p className="p">Katalon Runtime Engine 9.2 is now available as the latest version in TestCloud.</p></li></ul> 

### Fixes

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">Fixed broken TestCloud Tunnel Configuration page.</p></li><li className="li"><p className="p">Revised the Test Environments section to display TestCloud environments specific to the current project.</p></li></ul> 

## December 6, 2023


### Enhancements

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">Supported UTF-8 encoding for test scripts. You can now run test scripts that contain special characters in TestCloud in Chrome 119, Firefox 119, and Microsoft Edge 119.</p></li><li className="li"><p className="p">Supported the latest browser versions on Windows, Linux, and macOS, with Chrome 119, Firefox 119, and Microsoft Edge 119.</p></li></ul> 

## November 21, 2023


### New features

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Added the Camera injection keyword that simulates capturing images in mobile applications. See: <a className="xref" href="/katalon-testcloud/advanced-use-cases/camera-image-injection">Camera image injection</a>. </p> 

### Enhancements

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">Users can execute test in TestCloud with the latest version of Katalon Runtime Engine (KRE). In the <span className="ph uicontrol">Schedule Test Run</span> dialog, if you select "latest" for KRE version in <span className="ph uicontrol">Advanced Settings</span>, the scheduler will automatically select the latest KRE version that supports your test environments.</p></li><li className="li"><p className="p">Allowed uploading multiple versions of a mobile native application with the same application ID. All the versions of an application are displayed in the Application Repository.</p></li><li className="li"><p className="p">Provided <code className="ph codeph">FileExecutor</code> custom keyword to download and verify files when executing WebUI tests with TestCloud. See: <a className="xref" href="/katalon-testcloud/advanced-use-cases/download-and-verify-files">Download and verify files</a>.</p></li></ul> 

## October 25, 2023


### Enhancements

<div xmlns="http://www.w3.org/1999/xhtml" className="p"><ul className="ul"><li className="li">Updated latest browser versions for Windows, Linux and macOS (Chrome 117, 118; Firefox 117, 118; Edge Chromium 117, 118) for TestCloud environment in TestOps and Katalon Studio.</li><li className="li">[TestOps] Users can always see video recording when executing in Linux without enabling Screen Recording from Katalon Studio, regardless it passed or failed.</li><li className="li">[TestOps] When executing tests with Windows, macOS, and mobile environments, users can see proper video recording in the <span className="ph uicontrol">Test Result</span> section.</li><li className="li"><p className="p">Addressed the API key expiration:</p><ul className="ul"><li className="li">Updated API key that saved in TestCloud tunnel configuration to system API key.</li><li className="li">If the user has only expired API key, they can't schedule test or trigger a test run until they has at least one active API key in their API key list.</li></ul></li></ul></div>

## September 27, 2023


### Enhancements

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">Added Chrome 117 on Linux for Cloud Studio test execution.</li><li className="li">Users can identify which video recording belongs to which test case when executing mobile testing.</li><li className="li">Adjusted the default time out value in the <span className="ph uicontrol">Schedule Test Run</span> dialog to 180 minutes.</li></ul> 

## September 13, 2023


### Enhancements

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Update latest browser versions for Windows, Linux and macOS (Chrome 116, Firefox 116, Edge Chromium 116) for TestCloud environment in TestOps and Katalon Studio.</p> 

## August 30, 2023


### New features

<div xmlns="http://www.w3.org/1999/xhtml" className="p"><ul className="ul"><li className="li">When executing Cloud Studio test suites in TestCloud environments, users can take screenshot using the <code className="ph codeph">takeScreenshot</code> keyword then view this screenshot, along with the screenshots in the <span className="ph uicontrol">Files</span> tab of Test Run. </li><li className="li">A screenshot is automatically taken and displayed at every failed test step in log. Users can view screenshots in the <span className="ph uicontrol">Test Result</span> tab of Test Run.</li></ul></div>

### Enhancements

<div xmlns="http://www.w3.org/1999/xhtml" className="p"><ul className="ul"><li className="li">Renamed <span className="ph uicontrol">Use TestCloud</span> tunnel toggle to <span className="ph uicontrol">Private/Local Testing </span>.</li><li className="li">When the <span className="ph uicontrol">Private/Local Testing</span> toggle is turned on, the status of available TestCloud Tunnel is displayed. If no tunnel is configured, there is a link to navigate to the TestCloud Tunnel setup section.</li></ul></div>

## August 16, 2023


### Enhancements

<p xmlns="http://www.w3.org/1999/xhtml" className="p">All Cloud Studio users have 4 TestCloud parallel sessions:</p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">These sessions are distributed between Cloud Studio test case editor and Cloud Studio test suites execution in TestCloud environment.</li><li className="li">If a user runs out of 4 parallel sessions, the execution with Cloud Studio test suites can be queued but Cloud Studio test cases execution in debug mode (test case editor) won't be created.</li><li className="li">This session limit is independent of Katalon Studio tests.</li></ul> 

## August 2, 2023


### Enhancements

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">User can execute tests with Cloud Studio test suites stored in the Katalon Cloud default test storage and view test results / reports. See: <a className="xref" href="#">January 19th 2021</a>.</p>User can execute tests with Cloud Studio test suites stored in the Katalon Cloud default test storage and view test results / reports. See: <a className="xref" href="#">January 19th 2021</a>.</li><li className="li">Turned off the <span className="ph uicontrol">Repeat</span> toggle by default in the <span className="ph uicontrol">Schedule Test Run</span> dialog. This helps users avoid repeating test runs and exceeding TestCloud quota unintentionally.</li></ul> 

## July 12, 2023


### Enhancements

<p xmlns="http://www.w3.org/1999/xhtml" className="p">You can now select the <span className="ph uicontrol">Web Service</span> option when selecting the execution environment for individual test suites in a test suite collection.</p> 

## June 21, 2023


### New features

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Users can execute tests with TestCloud environments in CI/CD tools using Katalon Runtime Engine (KRE) commands without a KRE license; only TestCloud subscription or trial is required. Executing tests on TestCloud mobile browsers from CI/CD pipelines is limited to test suite collection.</p> 

### Enhancements

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Users can schedule test run in TestCloud environment with the latest browser versions: Chrome (111-114), Firefox (111-114), and Microsoft Edge (111-114) for Windows and Linux; Firefox (111-113) and Microsoft Edge (111) for macOS. See: <a className="xref" href="/katalon-testcloud/supported-environments-for-katalon-testcloud#id_2">Supported browsers</a>.</p> 

## April 25, 2023


### New features

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Users can run tests on Edge browser in IE mode with <span className="ph">TestCloud</span> environment from <span className="ph">TestOps</span>.</p> 

## March 28, 2023


### Enhancements

<div xmlns="http://www.w3.org/1999/xhtml" className="p"><ul className="ul"><li className="li"><p className="p">Users can schedule test run in TestCloud environment with the latest browser versions of Chrome (108-110) , Firefox (107-110) on Windows, Linux and macOS; Edge Chromium (108-110) on Window and macOS.</p></li><li className="li"><div className="p">Improved the test scheduling dialog:<ul className="ul"><li className="li"><p className="p">Users can see the environments configured for test suites when running a test suite collection.</p></li><li className="li"><p className="p">Users can save or cancel environment configuration.</p></li></ul></div></li></ul></div>

## March 1, 2023


### New features

<div xmlns="http://www.w3.org/1999/xhtml" className="p"><ul className="ul"><li className="li"><p className="p">Enabled scheduling tests on Safari browser from Katalon Studio.</p></li></ul></div>

### Enhancements

<div xmlns="http://www.w3.org/1999/xhtml" className="p"><ul className="ul"><li className="li"><p className="p">Improved sample mobile test projects for iOS and Android. Users can connect sample mobile projects to run with TestCloud environment in TestOps.</p></li><li className="li"><p className="p">Launched a new interface of the test scheduling dialog in TestOps. The new interface helps improve navigation in test scheduling flow. See: <a className="xref" href="#">January 19th 2021</a>.</p></li></ul></div>

## December 15, 2022


### Enhancements

<div xmlns="http://www.w3.org/1999/xhtml" className="p"><ul className="ul"><li className="li"><p className="p">Added new versions of Chrome (104-107), Firefox (103-106), and Edge Chromium (104-107) for Windows, Linux, and macOS. See <a className="xref" href="/katalon-testcloud/supported-environments-for-katalon-testcloud#id_2">Supported browsers</a>.</p></li><li className="li"><p className="p">Added a banner on the top of the Katalon TestOps page to notify trial users when their TestCloud free trial is about to be expired. </p></li></ul></div>

## November 29, 2022


### New features

<div xmlns="http://www.w3.org/1999/xhtml" className="p"><ul className="ul"><li className="li"><p className="p">Enabled scheduling tests on macOS from Katalon TestOps.</p></li><li className="li"><p className="p">Enabled scheduling tests on Safari version 10-16 from Katalon TestOps.</p></li><li className="li"><p className="p">Enabled executing tests on Internet Explorer version 11 (IE mode in Microsoft Edge) from Katalon Studio.</p></li><li className="li"><p className="p">Added the option to set desired capabilities for browsers and applications. When executing your test with TestCloud environment on TestOps, these desired capabilities would be applied. See <a className="xref" href="/katalon-testcloud/set-desired-capabilities-for-testcloud-environment">Set desired capabilities for TestCloud environment</a>.</p></li></ul></div>

## October 3, 2022


### New features

- Introduced the capability to override execution environment of individual test suite when executing a test suite collection. 
- Introduced Mobile Native App testing, which allows users to upload mobile applications to TestOps and schedule automated mobile tests. See: [Mobile native app testing with TestCloud](/katalon-testcloud/mobile-native-app-testing/mobile-native-app-testing-with-testcloud).

## September 5, 2022

### New features

- Introduced the beta version of Mobile Browser Testing that allows you to schedule test on mobile browsers of iOS and Android. See: [Run test on mobile browsers in TestOps](/katalon-testcloud/web-testing/mobile-browser-testing-with-testcloud#run-test-on-mobile-browsers-in-testops).

## GA Release - April 6, 2022


### New features

- Enabled scheduling tests on the TestCloud Windows environment from Katalon Studio.
- Enabled scheduling tests in TestCloud headless browsers environment from Katalon TestOps.
- Enabled scheduling tests on websites behind a proxy.

### Enhancements

- Removed warning about untrusted files when setting up TestCloud tunnel on macOS/Windows.
- Improved performance and stability when running test suite collections.
- Improved Windows node start-up time by pre-building Selenium Grid Docker Image when building TestCloud AMI instead of downloading the Docker Image every time.
- UI/UX improvement when running TestCloud via Katalon TestOps.

### Fixes

- [Bug] Unauthorized tunnel management API access.

## Trial Period - January 20, 2022


### New features

- Introduced TestCloud trial period as the new multi-browser testing environment in Katalon Studio, Katalon TestOps, and Katalon Runtime Engine. See: [Integrate TestCloud with Studio](/katalon-testcloud/integrations/enable-testcloud-integration-in-katalon-studio).
  - Enabled users to use TestCloud tunnel to execute tests in both public and private domains. See: [TestCloud tunnel](/katalon-testcloud/local-testing-with-testcloud).
  - Allowed users to contact Katalon at success@katalon.com to buy extra usage quota when running out of free trial package quota.
- Supported new versions of Chrome (96, 97), Firefox (95, 96), Microsoft Edge (96, 97).

### Enhancements from Beta version

- Stabilized TestCloud tunnel performance for testing in private domains: 
  - Improved resilience of TestCloud proxy server.
  - Queued up the execution if the number of requests exceeds the parallel quota.
- [UI] Displayed the **Trial** tag for the TestCloud option when scheduling test runs in TestOps.
- [UI] Displayed the **TestCloud** option when clicking on **Run** to execute tests in Katalon Studio.
