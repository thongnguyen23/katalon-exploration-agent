---
hide_title: true
title: 'Katalon Studio Release Notes: Version 10.x'
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# Katalon Studio Release Notes: Version 10.x

<div xmlns="http://www.w3.org/1999/xhtml" className="note note note_note"><span className="note__title">Note:</span> <ul className="ul"><li className="li"><p className="p">The in-app upgrade from version 9.x to 10.x is not available. To download the latest version 10.x, go to Katalon website: <a className="xref j-external-link" href="https://katalon.com/download/" target="_blank">Download Katalon Studio</a>.</p></li><li className="li"><p className="p">Katalon Studio 10.x now adopts Selenium 4, bringing major changes to align with the W3C WebDriver standard. For a complete overview of these updates and required migration actions, see <a className="xref" href="/katalon-studio/get-started/workspace-settings/migrate-katalon-studio-from-9.x-to-10.0.0">Migrate Katalon Studio from 9.x to 10.0.0</a>.</p></li><li className="li"><p className="p">Windows Desktop application testing is temporarily unavailable in version 10.x. For more details, see <a className="xref" href="/katalon-platform/troubleshooting/troubleshooting-common-execution-issues/windows-desktop-app-testing-unavailable-in-katalon-studio-10.x">FAQs</a>.</p></li><li className="li"><p className="p">Custom keywords have been reintroduced in the free edition starting from version 10.0.0.</p></li><li className="li"><p className="p">Docker <code className="ph codeph">latest</code> and <code className="ph codeph">latest-slim</code> tags now point to the latest version 10.x.</p></li></ul></div>

## Version 10.3.1

Release date: August 20, 2025

Katalon Studio version 10.3.1 is a patch release featuring key bug fixes and performance improvements aimed at enhancing stability and overall functionality. This update addresses Smart Wait timeout issues, improves recorder handling for custom date pickers, enhances license management, and resolves several execution-related defects to deliver a smoother, more reliable testing experience.

### New Features

- [Mobile Testing] Implemented support for new scroll to text mobile keyword functionality.
- [Web Testing] Added new `WebUI.jsClick` keyword for JavaScript-based click operations.
- Added a re-login button that uses saved login credentials when a forced logout occurs.
- Implemented a new **Remember Me** option in login dialog with auto-session refresh and retry logic.
- [TestCloud] Added the beta or dev version information next to the browser version number in the TestCloud Configuration dialog (in test suite and test suite collection), Report Summary, Execution Environment, and report files (HTML, PDF, CSV, JUnit).

### Enhancements

- [Reporting]
    - Added ability to customize TestOps test run names directly from KRE command line.
    - Enhanced TestRail integration with support for mapping multiple TestRail IDs.
- [Smart Wait] Resolved timeout override issues when Smart Wait is enabled to ensure correct elapsed time matching.
- [Web Recorder Plus] Improved Recorder Plus to better capture `setText` actions for web elements with custom date pickers.
- [ADO Integration] Added option to choose whether to override existing automated test name and storage values.
- Added Chrome 139, Edge 139, and Firefox 141 compatibilities.
- Updated all JDBC libraries to the latest supported versions.
- Updated WebDriverManager from version 6.1.0 to 6.2.0.
- Added project trust dialog when opening untrusted KS projects for enhanced security.

### Fixes

- [Mobile Testing]
    - Corrected incorrect locator capture note URL in Mobile Object Spy.
    - Fixed `Cannot hide keyboard` issue on iOS devices.
    - Resolved Mobile **Tap and Hold** hanging indefinitely on incorrect locators.
    - In iOS, keyword `uncheckElement` did not work in version 10.2.3, although it functioned correctly in the revious version.
    - Fixed `ScrollToText` keyword throwing `StackOverflowError` with long list items in Appium.
    - Fixed incorrect timeout handling logic for mobile `waitForElementNotPresent` keyword.
- [Smart Wait]
    - Fixed client timeout to remote server being limited to 3 minutes in KS 10.x.
    - Stopped sending `getTitle` requests to remote server after test termination or missing closeBrowser step.
    - Fixed `waitForAngularLoad` keyword not working properly.
    - Corrected timeout logic for `waitForElementNotPresent` keyword across all KS versions.
    - Fixed 30-second delay when Spy/Recorder highlights elements with Smart Wait enabled.
    - Fixed `Web Element is null` error when running projects created from KS 10.2.4 or earlier versions.
    - Fixed Smart Wait functionality to work properly on Remote and TestCloud execution environments.
- Fixed browser opening issues when `webSocketUrl=false` desired capabilities are added in Chrome.
- Resolved inability to run tests on Chrome Active Browser due to `DevToolsActivePort` errors.
- Fixed `ScrollToElement` using JavaScript, which causes incorrect website display when scrolling.
- Fixed proxy settings being deleted when opening two (2) KS instances on one machine.
- Fixed `NullPointerException` when response size is too large.
- Resolved intermittent `unable to resolve class katalon.pages.platform.common.Filter` exception when executing a test suite.
- [File Path and System issues]
    - Added proper file and folder path length validation on Windows systems.
    - Fixed inability to open KS in Windows Server 2016 from KS 10.2.3 due to SWT DLL errors.
    - Resolved Java update errors during execution.
- [TestCloud] In remote execution:
    - Fixed test cases incorrectly showing `SKIPPED` status when running from TestCloud only.
    - Resolved missing test suite collection report folder in email attachments for ADO integration.
    - Fixed missing **Execution by** information in HTML reports when executing with TestCloud.
- [Onboarding]
    - Enhanced error message triggered when the Onboarding Tour crashed since Recorder Plus was using an active browser.
    - Fixed default URL being changed when starting Onboarding Tour after recording other pages.
- [Reporting] 
    - Fixed incorrect browser information display in email reports when running with TestCloud.
    - Resolved WEBM video generation issues on macOS/Linux with Chrome.
    - Fixed directory validation issues when generating browser-based recordings.
    - Fixed `showReferences` functionality after renaming parent object folders containing dots.
- Fixed KS not importing all values from Postman requests.
- Fixed errors when adding `.jar` files to Katalon Studio.
- Resolved KSE crashes when adding custom keywords in test cases.
- Resolved insecure deserialization vulnerability when opening malicious projects with `entityReference.index`.

### Changes
- Windows Desktop App testing now requires a Trial or Enterprise license.

## Version 10.3.0

Release date: July 30, 2025

Katalon Studio 10.3.0 delivers substantial upgrades across core testing features, including improved web execution and performance, support for mobile test self-healing, and expanded StudioAssist AI capabilities.

This release also introduces the beta version of desktop application testing—now available without requiring WinAppDriver—along with a redesigned onboarding experience to help users get started more efficiently. Additionally, users can benefit from a refreshed email report template UI, enhanced Recorder Plus features, and a new ability to save API response bodies directly from the Response tab.

### New Features

- [API Testing]
    - Introduced a new option to save API response bodies as files. Includes a **Save Response Body as File** link in the **Response** tab.
    - Response headers now appear in table format for better readability, and large response bodies are displayed more clearly.

    <img src= "https://tw-cdn.katalon.com/katalon-studio/release-notes/version-10.x/KS_10_3_api-save-response-as-file.gif" alt="Save Response Body as File" width="600" />

- [Mobile Testing]
    - Added support for Self-Healing in Mobile Testing to improve resilience for mobile test scripts.
    - Added support image-based locator capture for Mobile Recorder and Spy, allowing fallback recognition via reference images.

    <img src= "https://tw-cdn.katalon.com/katalon-studio/release-notes/version-10.x/Mobile+Self+Healing+Part+1.gif" alt="Self Healing support in Mobile Testing" width="600" />

    <img src= "https://tw-cdn.katalon.com/katalon-studio/release-notes/version-10.x/Mobile+Self-Healing+Part+2.gif" alt="Self Healing support in Mobile Testing" width="600" />

- Revamped the Onboarding Experience and added a Knowledge Hub to simplify how users get started:
    - The old onboarding tours from the Start Page, **Walkthrough** tab, and **Tutorial** section have been removed.
    - A new basic onboarding tour, focused on the Web Recorder, is now available.
    - The updated Knowledge Hub offers quick access to documentation, tutorials, community, and support resources to help new users onboard with Studio faster.

    <img src= "https://tw-cdn.katalon.com/katalon-studio/release-notes/version-10.x/Katalon+Studio+Onboarding+Part+1.gif" alt="New Katalon Studio Onboarding" width="600" />

    <img src= "https://tw-cdn.katalon.com/katalon-studio/release-notes/version-10.x/Katalon+Studio+Onboarding+Part+2.gif" alt="New Katalon Studio Onboarding" width="600" />

    <img src= "https://tw-cdn.katalon.com/katalon-studio/release-notes/version-10.x/Katalon+Studio+Onboarding+Part+3.gif" alt="New Katalon Studio Onboarding" width="600" />

### Enhancements

- Introduced the ability to automatically update Azure DevOps (ADO) Test Cases upon test execution by setting the Automation status to `Automated` and adding the executed test case name in the **Associated Automation** section. This eliminates manual updates and improves visibility of automated test coverage in ADO.
- [Reporting]
    - Introduced a new test suite and test suite collection email report template with a modern UI look and more data displayed.
    - Supports the ability to preview test suite and test suite collection email body reports while editing templates.
    - Added profile information to HTML reports for test suites and test suite collections, as well as to email reports.
    - Added the ability to use an external advanced template for email report.
    - Slightly improved the Log Viewer UI with a new implementation using WebView.
    - Introduced new mechanism to display only `fail`, `error`, and `incomplete` test cases in the Test Case table of the email report, and added support for including a test suite summary table in the Test Suite Collection (TSC) email report template.
- [StudioAssist]
    - Now supports Google Gemini integration using both personal keys and a shared organization key set by an admin, and fully compatible with the `gemini-2.5-flash` model.
    - Now supports for OpenAI-compatible providers using both personal keys and a shared organization key set by an admin.
    - Added an option to use custom keywords as project context for StudioAssist. This will help you reuse existing custom keywords for code generation and get more accurate AI suggestions.
    - When generating or explaining code via script editor, StudioAssist now also uses custom keywords, object IDs, and all content of current uploaded file as additional context.
    - Added a new setting to enable or disable follow-up question suggestions in StudioAssist responses, which now automatically suggest related follow-up queries.
    - Improved UI and error messages for chat interface and error handling.

        <img src="https://tw-cdn.katalon.com/katalon-studio/release-notes/version-10.x/StudioAssist_error_handling_message1.png" alt="StudioAssist error message - Issue processing request" width="600" />
        
        <br/> 

        <img src= "https://tw-cdn.katalon.com/katalon-studio/release-notes/version-10.x/StudioAssist_error_handling_message2.png" alt="StudioAssist error message - Took long response" width="600" />

        <br/> 

        <img src= "https://tw-cdn.katalon.com/katalon-studio/release-notes/version-10.x/StudioAssist_error_handling_message3.png" alt="tudioAssist error message - Length of message" width="600" />

    - Continued improvements to StudioAssist prompts to enhance guidance and response relevance.

        <img src= "https://tw-cdn.katalon.com/katalon-studio/release-notes/version-10.x/StudioAssist_support_portal_help.png" alt="New Katalon Studio Onboarding" width="400" />

- Improved the way we generate the test object naming for better readability in Katalon Recorder.
- Introduced a new setting in Web Recorder Plus that allows user to configure ignoring pattern when generating locator.

    <img src= "https://tw-cdn.katalon.com/katalon-studio/release-notes/version-10.x/Web_Recorder_Plus_exclude_patterns_locator.png" alt="Web Recorder Plus exclude patterns feature" width="400" />

- Improved text verification for Flutter `semantic-node` elements without `innerText`, enabling keyword `verifyText` to accurately detect and validate text values when testing Flutter apps.
- Improved Recorder Plus mechanism to capture shadow DOM elements in Flutter-based web app.
- Re-enabled Windows Desktop Testing (Beta) for basic test cases with the following improvements:
    - Added new Windows keywords `takeScreenshot` and `takeElementScreenshot` using FlaUI.
    - Added support to keywords `StartApplication` and `CloseApplication` with FlaUI webdriver.
- Improved Smart Wait to Reduce Test Flakiness and Improve Execution Speed
- Free users can now continue using Katalon Studio Enterprise package after Trial plan ends (with limited feature access).
- Added Chrome 138, Edge 138, and Firefox 140 compatibilities.
- [Console Mode] Added the following UI/UX improvements: 
    - Add a scroll bar to **Generate Command** dialog.
    - Now auto-generates License Server URL when detected that the user logs in with an On-Premise license.
- [WebUI Self-Healing] Automatically excludes `Verify` and `Wait` keyword types from Self-healing attempts by default, reducing unnecessary fallback behavior for non-critical validations and improving execution clarity.
- [WebUI] Enhanced screenshot capture accuracy for `Take Screenshot` keywords by leveraging Chrome BiDi protocol and Selenium 4 improvements, resulting in more consistent and visually accurate screenshots during test execution.

### Fixes
- [Web Recorder and Spy]
    - Resolved an issue where captured hover actions failed when involving multiple nested hover levels.
    - Fixed a problem where Spy Plus captured only one object when two different object types were present.
    - Addressed an issue where switching to a different website during recording or spying caused Spy to stop functioning.
    - Prevented redundant **Mouse Over** action triggered after clicking an object followed by a Tab key sequence.
    - Eliminated duplicate **Mouse Hover** actions caused by tab switching during recording.
    - Fixed error occurring after installing the Katalon Studio Recording Engine (KRE) plugin.
    - Corrected failure to start recording with an active browser after changing the application port setting.
    - Improved object recognition when multiple elements have nearly identical attributes — Spy now captures all distinct objects.
    - Fixed an issue where using **Attribute** as a selector prevented Recorder and Spy Plus from highlighting or finding objects.
    - Resolved invalid locator errors when using the `@text` attribute in locators.
    - Improved fallback suggestions in Self-Healing for Recorder Plus locators.
    - Fixed Recorder Plus failures when executing test cases during an active recording session.
    - Resolved inability to capture object images while using **Active Browser** mode.
    - Addressed highlight issues on tables, dropdown lists, and combobox controls.
    - Restored support for keyword `WebUI.SelectOptionByValue`, which was missing in versions 8.6.5 and 8.6.6 in Web Recorder.
    - Fixed Spy Plus issues where navigating to another website during a session would cause Spy to stop working.
    - Addressed a dependency regression that caused automation to accept `beforeunload` prompts unexpectedly.
- [StudioAssist]
    - Updated StudioAssist to properly display a `No internet connection` message instead of raw error text.
    - Fixed a MacOS-only issue where the copy function in StudioAssist Chat did not work unless the chatbot was focused.
    - Resolved intermittent issues where requests with the current file and attachments failed to send.
    - Fixed an error that caused StudioAssist to stop working when switching between **Keyword** and **Debug** modes.
    - Updated prompt behavior to avoid generating scripts with unsupported Groovy versions.
- [Smart Wait & Performance]
    - Resolved a bug where Smart Wait triggered unnecessarily on every action involving Angular 14 test objects.
    - Addressed a conflict where Smart Wait caused navigation steps to exceed two minutes.
    - Fixed excessive Smart Wait calls during execution with local Appium and Android devices.
    - Resolved an issue where Katalon Studio froze when uploading test reports with test suite-level data binding.
- [Reports]
    - Fixed email subject not recognizing `${totalFailed}` and `${totalPassed}` variables in test suite and test suite collection.
    - Addressed inconsistencies between test results and test reports for BDD test cases.
    - Resolved `WARNING: The isStretchWithOverflow attribute is deprecated. Use the textAdjust attribute instead.` error when generating PDF report on 10.2.1 only.
    - Fixed an issue where mobile native app test results were not updated in Azure DevOps when using KSE 10.x.
    - Fixed an issue in the Katalon Jenkins Plugin where stopping a job failed to terminate related processes, causing device conflicts and overlapping test sessions.
- [System and Browser issues]
    - Confirmed `save <className>.java` dialog appears when saving java class in `Include/scripts/groovy` folder.
    - Fixed error `firefoxAddonSocket is null` when switching Spy from another browser to Firefox.
    - Addressed a Z-index layering issue on Linux where StudioAssist text overlapped the Start Page.
    - Resolved incorrect URL navigation when recording in KCU 2.2.2 with an already open browser.
    - Prevented the **Test Suite Collection** window from auto-switching to the **Results** tab when toggling between windows.
    - Migrated legacy HTTP clients to `ApacheHttpClient` to centralize proxy setup flows.
    - Removed unnecessary `setN()` method calls from OpenAI integrations.
- In mobile test execution, corrected unclear messages when using the `selectListItemByIndex` keyword for Android.
- Fixed a session termination issue that prevented applications from closing correctly in TestCloud.
- Resolved a failure to execute or record mobile tests on HeadSpin in version 10 (worked in version 9).
- Fixed an issue where `verifyElementNotPresent` did not trigger self-healing, even when applicable.
- [BDD Testing] Fixed an issue where custom keywords could not be executed in BDD tests unless they were placed in the default package.
- [Mobile Testing] Resolved an issue that prevented Katalon Studio from launching existing applications on a device from a Chinese smartphone manufacturer.
- Since 10.3.0, we have re-adjusted the methods name in MobileTestObject. Deprecated methods have been replaced as follows: 

    | Deprecated API  | Replaced with   |
    |------------|------------|
    | `public String getMobileLocator()` | `public String getLocator()` |
    | `public void setMobileLocator(String mobileLocator)` | `public void setLocator(String locator)` |
    | `public MobileLocatorStrategy getMobileLocatorStrategy()` | `public LocatorStrategy getLocatorStrategy()` |
    | `public void setMobileLocatorStrategy(MobileLocatorStrategy mls)` | `public void setLocatorStrategy(LocatorStrategy ls)` |

### Known Issues
- Setting the `webSocketUrl=false` desired capability in Chrome currently prevents the browser from launching. To resolve this issue, replace `configuration\resources\extensions\Smar Wait.zip` with [this Smart Wait file](https://tw-cdn.katalon.com/katalon-studio/release-notes/version-10.x/Smart+Wait.zip).
- Recorded or existing test scripts created in earlier versions of Katalon Studio may fail when executed in version 10.3.0, resulting in the following error: `Caused by: java.lang.NullPointerException: Cannot invoke org.openqa.selenium.WebElement.clear() because webElement is null`. As a workaround, go to **Project Settings > Execution > WebUI > select Apply and Close** and rerun the test.

## Version 10.2.4

Release date: July 11, 2025

This release focuses on important authentication fixes when using On-Premises version 2.1.8, and updates embedded WebDrivers to support the latest supported browser versions.

### Enhancement
- Added Chrome 138, Edge 138, and Firefox 140 compatibilities.

### Fix

- Fixed an issue in Katalon Studio Enterprise 10.2.3 where TestOps authentication override failed on On-Premises environments due to incorrect server configuration, now fully tested and resolved for KSE and KRE.

## Version 10.2.3

Release date: June 30, 2025

This release introduces customizable StudioAssist settings, major performance and UI enhancements, extended browser and platform support, and a wide range of bug fixes across StudioAssist, Web, Mobile, Reporting, and Platform integration features.

### New Features
- [StudioAssist] Introduced StudioAssist settings to customize engineering prompts for a more tailored AI-assisted experience.

### Enhancements
- [StudioAssist] 
    - Upgraded AI backend to **GPT-4.1 mini**.
    - Optimized prompts for code generation and explanation, particularly for handling personal keys.
- [Mobile Testing] Support mobile object attributes editing:
    - Added a **Generate** button to Mobile Object editor.
    - Enabled editing of mobile object property values.
- Supports TestRail with custom required fields.
- Improved logging for report uploads across qTest, Azure, TestOps.
- Enabled **gzip** encoding for Selenium (Appium) clients to optimize network performance.
- `WebUI.authenticate` keyword is now supported on TestCloud, remote, and localhost test runs.
- [Reporting]
    - Adjusted Test Suite Collection (TSC) status display in HTML reports.
    - Improved logging during PDF report generation.
- Updated WebDriverManager from 6.0.0 to 6.1.0.
- Added Chrome 137, Edge 137, and Firefox 139 compatibilities.
- [UX/UI]
    - Refreshed UI and icons in the **About Katalon Studio** dialog.
    - Prevented TestOps connection when `apiKey` is missing in CLI.
    - Release update check now respects Admin-level control.
    - Added capability to capture raw screenshots on test execution failures.
- Resolved hanging issues in:
    - Creating or modifying test objects.
    - Saving test cases and keywords.
    - Renaming test cases and test objects.

### Fixes
- [Web Testing]
    - Fixed screenshots not being captured on errors (`FailureHandling=Optional`)
    - Resolved malfunctioning `WebUI.authenticate()` keyword.
    - When using `selectOptionByValue`, after selecting success, Katalon Studio Enterprise checked its state and always failed.
    - Browser-based recording caused incomplete execution and reporting.
    - Chrome 137 compatibility issues with sample projects.
    - `WebUI.takeScreenshotAsCheckpoint` keyword failed when executed via Sauce Labs.
    - Fixed issue where web testing on Android failed due to error `Original error: invalid argument: cannot parse capability: goog:chromeOptions`.
- [Mobile Testing]
    - `Mobile.getDeviceOS()` keyword returns null when run with TestCloud, HeadSpin devices and all Cloud/Remote platforms.
    - In iOS, **Hide Keyboard** action failed in Mobile Recorder.
    - Cannot record/spy mobile using application ID.
    - In iOS, **Tap and Hold** keyword does not work, it just taps but does not hold at specific time.
    - Capture Screenshots on errors instead of warning (`FailureHandling=Optional`).
    - Saving selected objects unintentionally saved all captured objects.
- The Test Suite Collection window switches to result tab automatically when going to and from another window.
- [Reporting]
    - Secure Storage - Cucumber Reports failed to mask protected values.
    - JUnit test suite report used incorrect timestamp formats.
    - HTML reports had inconsistent execution statuses.
    - Test Suite Collection HTML report loses key info when in expanded view.
    - Test Suite statuses were inconsistent in the Test Suite Collection HTML report.
    - There are missing test step description in new HTML report.
    - On occasion, when a test case fails, status is displayed as `Failed` instead of `Warning`.
    - Trimmed unwanted spaces in AI config fields.
    - Explain code was wrong when explaining a regular expression in the sample.
- [TestOps]
    - Katalon Studio Enterprise not reporting result quota exceeded.
    - Resolved the issue preventing automatic report uploads in OP TestOps Agent environments.
- Onboarding Tour shown empty **Warning** dialog when going through API Tour.
- Authentication is not supported for SOCKS proxy, KSE could not go through SOCKS proxy when configured with Authentication.
- On occasion, the WebDriver instance doesn't have a session ID.
- Katalon Studio Enterprise not reporting result quota exceeded.
- Katalon Runtime Engine occasionally throws `ArrayIndexOutOfBoundsException` error in console log when running a test suite collection.
- Fixed error exception when using `katalon-studio-ctrf-report-plugin` plugin.
- Unable to run Katalon Runtime Engine with **only** TestCloud license.
- Using wrong `orgId` when fetching TestOps integration configuration.
- Test cases failed unexpectedly in version 10.
- Self Healing is not working for Custom Capabilities if the `Remote` caps is empty.
- Missing suite when scheduling on TestOps due to a crash in `ExecutionReportScanner.scanReportFolder`.
- In Katalon Runtime Engine, when running on CI/CD with GitHub action, the following error message appears: `WARNING: Secure coding is not enabled for restorable state! Enable secure coding by implementing NSApplicationDelegate.applicationSupportsSecureRestorableState: and returning YES`.
- Intermittent missing Test Report after running a test suite collection with Katalon Runtime Engine.
- In macOS, occasionally Katalon Studio is not responding when opening the Declaration function.
- Linux Test run is terminated when the running process consumes huge memory.
- Windows Test run disconnects the DevTools/debugging connection when consuming out of memory.
- When executing a test run using CMD, Ctrl+C doesn't terminate the execution.
- The loading screen while starting KS is reversed after upgrading Eclipse.
- In macOS, test case renaming errors occur from second attempt onward.
- When clicking on `Configure Specific Project Setting...`, it causes a `nullpointer` exception.

### Known limitation
    - Browser hang issue occurs when launching Chrome version 135 and above in Katalon Studio. From Chrome 136 onward, security restrictions prevent using the default profile folder. Refer to the following documentation for the workaround: [Katalon Compact Utility for Katalon Studio](katalon-studio/record-and-spy/webui-record-and-spy-utilities/katalon-compact-utility-for-katalon-studio).

## Version 10.2.2

Release date: June 18, 2025

### Fixes
- Remove **Chrome for Testing** for recording and execution. Katalon Studio now reverts to using Chrome as usual.
- Added the argument `-disable-features=DisableLoadExtensionCommandLineSwitch` in Desired Capabilities to address the issues with Chrome 137.

## Version 10.2.1

Release date: May 31, 2025

### Fix
- Katalon Studio’s Web Recorder [failed to launch on Chrome version 137](https://katalon-inc.my.site.com/support/article/Recorder-Fails-to-Launch-on-Chrome-137) due to changes in browser automation protocols, including the removal of the `--load-extension` flag. 

  Starting with this version, Katalon Studio uses Selenium Manager instead of Web Driver Manager for Chrome browser, enabling support for **Chrome for Testing**. During both recording and execution, Katalon automatically downloads the compatible Chrome version the latest version (or specified version) of Chrome for Testing, restoring full functionality with Chrome v137 and later.

  On the first launch, Katalon Studio will download Chrome for Testing, so starting the browser may take longer.

  To change this behavior, launch Chrome with `binary` desired capability specifying the desired Chrome binary location and add the following `args` as shown in the screenshot below:
  
  ```jsx
    --disable-features=DisableLoadExtensionCommandLineSwitch
    ```
  
  <img src= "https://tw-cdn.katalon.com/katalon-studio/release-notes/version-10.x/disable_chrome_extension.png" alt="Disable Chrome extension" width="700" />

  You can also specify a Chrome binary location using the `binary` capability to control which version of Chrome for Testing is launched.

  :::note
  For detailed steps on setting up your desired capabilities, see: [Set up Desired Capabilities for WebUI Testing in Katalon Studio](/katalon-studio/manage-projects/project-settings/desired-capabilities/set-up-desired-capabilities-for-webui-testing-in-katalon-studio#ariaid-title1)
  :::

### Known issue
- In some secured or network-restricted environments, users may be restricted from downloading the WebDriver due to network or firewall policies. To ensure proper functionality, your IT team will need to whitelist the following URLs:
    - `https://storage.googleapis.com`
    - `https://googlechromelabs.github.io/chrome-for-testing/known-good-versions-with-downloads.json`

## Version 10.2.0

Release date: April 23, 2025

### New features

- [StudioAssist]
    - [StudioAssist chat] Added test object IDs as StudioAssist context.
    - [StudioAssist chat] Auto-use content in the focus tab as context.
    - Support file attachments in StudioAssist chat conversation.
    - Added the ability to customize tags that are auto-added to test cases using AI.
    - Added the ability to use StudioAssist with an OpenAI/Azure OpenAI key shared across the Organization. This configuration will be done in TestOps version 3. See [Configure a default or organization-specific AI key](/katalon-platform/administer/administration-and-licensing-alternate/manage-systems/configurations/configure-ai-services#configure-a-default-or-organization-specific-ai-key).
- [Report]
    - Introduced a new test suite HTML report template. [View sample test suite report](https://tw-cdn.katalon.com/katalon-studio/Test+report/View+test+reports/View+and+customize+execution+log+in+Katalon+Studio/Sample_Test_Suite_Report_Template.html).
    - Added an option to split the HTML report into smaller files to reduce memory consumption and loading time.
    - Added an option to auto-generate the Console logs file in the report folder.
- [ADO Integration] Azure DevOps now allows you to link multiple test cases from multiple test plans.
Introduce protected global variables for secure storage. The values of protected global variables are saved outside of the Studio project and masked in logs and reports.
- Added an option to override protected global variables during Katalon Runtime Engine (KRE) runtime.
- Introduced Kerberos support for Proxy Authentication (Beta). See [Kerberos proxy authentication (Beta)](/katalon-studio/katalon-studio-enterprise-and-katalon-runtime-engine-license/configure-proxy-authentication#kerberos-proxy-authentication-beta).

### Enhancements

- [StudioAssist]
    - Support currently available OpenAI models: GPT-4o, o3-mini, o1.
    - Added a **Settings** icon and displayed the current AI service in the chat window.
    - Improved StudioAssist message when there is no internet connection.
- [Jira plugin] Allow users to remove linked issues in test cases.
- [Mobile] Add Mobile Keyword "Press Home" in the Mobile Recorder **Available Actions**.
- [Report]
    - Specify iteration names for Data Driven Testing (DDT) is now supported for PDF and CSV reports.
    - Masked variables are now marked as asterisks in HTML and PDF reports.
    - Test Suite Listener (Before & After Test Suites) is now included in HTML, CSV, and JUnit report files.
    - [UI] Adjust the position of the report project setting page and add an option to go back to the old report template.
    - Updated the SLF4J logging lib provider to resolve issues related to logs.
    - Improved PDF report generation process to better support large test execution.
    - [UI] Auto-refresh data in 3 columns in the **Test Case** table and **Analytics** tab in test suite results when integration info changes.
- [Execution]
    - Improved the flow to auto-update webdrivers when running a test suite collection.
    - Automatically save test cases before execution when running a test suite collection.
    - Filter organizations that belong to an account in the select Org step when logging into Katalon Studio.
    - [UI] Added sorting function in the **Profile** section for Global variables. This applies to **Name** and **Protected** columns.
    - Updated WebDriverManager from 5.9.2 to 6.0.0.
    - Upgraded to Selenium 4.28.
    - Added Chrome 135, Edge 135, and Firefox 137 compatibilities.
    - Updated all the latest docs links in the Katalon Studio application.

### Security compliance

- Update Katalon Studio updater - `commons-io:commons-io` to version 2.15.1.
- Refactored dependencies for some Katalon bundles to resolve vulnerabilities.
- Upgraded to `org.eclipse.jetty:jetty-http@12.0.18`.
- Upgraded to `org.eclipse.jetty:jetty-server@12.0.18`.
- Upgraded to `io.cucumber:datatable-dependencies@1.1.16`.

### Fixes

- Resolved the issue where **Self-healing** could not work with custom **Desired Capabilities**.
- Console | Run test with **Debug from here** does not log running steps in **Console log** at runtime.
- Missed all the logs of test steps, and strange logs were generated in the console.
- Script code vanishes when a test case is renamed.
- [StudioAssist]
    - Error `User is not authorized to access this resource with an explicit deny` appears when the user picks a license from a random org.
    - StudioAssist did not work with OpenAI reasoning models.
    - Unable to answer questions related to automation testing in StudioAssist chat.
- The JUnit report format did not match the standard for reporting skipped tests.
- Sample project failed when executed on Chrome 135.
- [KCU] Unable to run a test with Edge Chromium because of strict policy.
- [TestCloud] `No Session Found` error when executing test cases in a test suite.
- [Mobile]
    - Using the wrong app ID when the Android and iOS apps have the same name.
    - Locator Strategy set to `Android UI View Tag` unexpectedly switched to `Android UI AUtomator`, causing recording issues.

### Changes

- When moving a test case in Katalon Studio, relevant artifacts are also moved in the script folder of that test case.
- Upgraded Ubuntu in Docker image from 20.04 to 24.04.
- Use the selected project for TestCloud integration instead of the Organization.
- Upgraded to Eclipse 2024-06.

### Known limitations

- When using the option to split the HTML report into small `.js` files, the data folder containing `.js` files is not included when sending emails. It means that when you split the  HTML report into smaller `.js` files and send an email report, it only sends the summary HTML report, and the test steps will be missing.
- [StudioAssist|Katalon AI] - Unable to list out all of the objects in a large project.

## Version 10.1.1
Release date: March 12, 2025

### Enhancements

 - Officially supports parameterizing associated Azure DevOps (ADO) Test Case IDs. For more details, see <a className="xref" href="katalon-studio/test-objects/mobile-test-objects/parameterize-mobile-test-object-properties-in-katalon-studio">Parameterize Azure DevOps Test Case ID List in Katalon Studio</a>
 - We have added a new **Execution Profile** column in the Azure DevOps Test Configuration Mapping to improve test result accuracy and management. This enhancement provides testers with additional context by displaying the selected Execution Profile alongside the Execution Environment for each test execution, ensuring better traceability and informed decision-making.
 - Introduced the ability to add a Jira issue directly to an existing test case, improving issue traceability and test case management.
 - Upgraded to JRE version 17.0.14+7 in Katalon Studio (KS) and Katalon Runtime Engine (KRE) for improved security and performance.
 - Introduced the ability to switch between the in-app and system browsers for enhanced flexibility: <img src="https://tw-cdn.katalon.com/katalon-studio/release-notes/KS_switch_inapp_browser_config.png" alt="Switch in-app to browser" width="400" />
 - Added support for the latest browser versions:
     - Chrome 134
     - Edge 134
     - Firefox 136
     - Gecko 0.36.0
 - Upgraded to Node.js 20.1, addressing the `Node version 10 is out of life` warning when running Azure DevOps pipelines.
 - Improved the performance of **Log Viewer** and **Job Progress** by updating the Java logging library to fix incorrect log file parsing issues.   
  
### Fixes

- No error message was displayed when cloning a Sample Project with a duplicated project name or incorrect drive/location.
- Fixed an issue where importing test cases from Jira failed with the error: `An internal error occurred during: "Importing issues."`.
- Resolved an issue where Jira integration failed with the error: `The current user does not have administrator permission.`.
- Fixed an issue where Android applications failed to start when using a wildcard to exclude hosts in **Windows > Katalon Studio Preferences > Katalon > Proxy > System**.
- Resolved a TestCloud license activation failure when executing tests with KRE on GitLab Docker, which resulted in the error:`java.lang.IllegalStateException: Expected BEGIN_OBJECT but was STRING at line 1 column 1 path $.`.
- Fixed a bug where the Start Page appeared blank after reloading.
- Resolved an issue where the Start Page was broken in offline mode when opening a new project.
- Corrected the release note link in the Start Page offline mode.
- Fixed incorrect behavior when selecting/unselecting checkboxes in **Self-Healing Insight**.
- Fixed an issue where tests failed to start in Chrome due to SOCK proxy issues.
- Resolved an issue preventing test execution in Edge Chromium v133.0.3065.51 on Windows.
- Fixed an error when parsing test reports containing special Unicode characters, which previously resulted in:`javax.xml.stream.XMLStreamException: ParseError at...`.
- Resolved an issue in which the `-g_VARIABLE` argument in KSR Docker execution failed to override global variable values.

### Changes

- Removed the logic to check the Organization ID when activating Katalon Studio/Katalon Runtime Engine.
- Removed the logic to filter projects by Organization in TestOps integration settings. The list of Projects in TestOps integration is now all Projects that belong to the User in the Account that they selected to log in to Katalon Studio with.
- Removed the TestOps integration dialog that automatically pops up when creating a new project.

## Version 10.1.0
Release date: January 21, 2025

### New features

Introduced StudioAssist chat window and improved StudioAssist accuracy by upgrading to the GPT 4o-mini model. You can now instantly access and chat with StudioAssist from within your Katalon Studio app. See [StudioAssist chat window](/katalon-studio/create-test-cases/studioassist-chat-window).

### Enhancements

- [Email report]:

    - The email summary report now includes the numbers of skipped and incomplete test cases.

    - In **Project Settings > Email > Template > Test Suite**, you can now add the `${test_case_result_table}` variable in the Test Suite's email body template to display a detailed table of test case IDs and their results in an email report.

    - When images are split out of the HTML file, the **PNG files** option is now auto-selected in **Project > Settings > Email** for projects created in version 10.1.0 and later.

- [HTML report] Added **Attach reference images using linked screenshots (not embedded) to reduce report file size** option in **Project > Settings > Plugins > Report** to split images as reference files instead of embedding them directly into the HTML test suite report. This option helps reduce the file size of a HTML test suite report.
- [Video recording]:

    - Video recordings now use the test case name as the file name instead of sequential numbers.

    - In **Project > Settings > Execution**, added new video format options, including `webM` and `mp4`, for browser-based recorder.

- Added **Tap at position** on Mobile Recorder Available Action.
- Added a new mobile keyword: [Mobile] Press Keycode.
- Added the **Platform** value to the **Result** section in Report history.

- Updated logs and report files to display detailed browser versions instead of rounded versions.

- Added the Data Binding section to JUnit Report.xml and CSV reports.

- Debug mode now generates reports in HTML, PDF, and CSV formats.

- StudioAssist now uses GPT-4o-mini instead of GPT-3.5-turbo to deliver more accurate responses.

- Upgraded JRE to version 17.0.13+11 in Katalon Studio and Katalon Runtime Engine.

- Set the default encoding to UTF-8 for reports generated in the Katalon Runtime Engine. This ensures support for special characters in reports, including when running tests scheduled from TestOps or locally on a VM machine.

- Test reports now display the actual device used when selecting the **Any** option in TestCloud for mobile browsers and native apps.

- Added the `respectSystemAlerts = true` configuration to Appium’s settings to capture system alert and permission dialogs during iOS testing.

- Adjusted default video codecs to improve compatibility with common media players. MP4 and MOV now use H.264, while WebM uses VP9 for better compression efficiency.

- Updated `.har` file names to reflect Web Service (WS) request names instead of sequential numbering.

- [TestOps integration] Added support for parallel asset uploading, retry mechanism, and detailed logging to enhance upload speed and reliability in TestOps integration.

- Embedded WebDrivers have been updated to support the latest browser versions: Chrome 132, and Firefox 134.

- Renamed all `3.0.17-fat.jar`​ files to `​3.0.17.jar`​ to resolve classpath issues without requiring manual updates.

- [TestCloud] Introduced a setting to switch between legacy and new TestCloud Hub configurations in **Project > Settings > Katalon Platform**. This option is available when **Enable Katalon TestCloud Integration** checkbox is ticked, but this feature is not yet accessible to all users.

- Automatically tags AI-generated test cases with `GenAI`. The icon of test cases tagged only with GenAI changes to purple.

- Updated the CDN links for EdgeDriver downloads.
- [KRE] Added support to enable TestOps integration directly from the CI/CD pipeline.
- You can send test results to Azure DevOps Server 2022 when running tests from KSE.

### Fixes

- The **Use first row as header** option in **Data Files** did not function correctly when linking test data to a checkpoint.

- [KRE]:

    - Using a global variable in the email report template threw an error: `System is unable to email report. Reason: groovy.lang.MissingPropertyException: No such property: G_email for class: Script1`.

    - KRE did not generate HTML, PDF, or CSV report files when running tests with offline activation.

- The user profile displayed the wrong name after switching organizations and logging in with another account.

- Dragging and dropping a class from one package to another caused the class to disappear instead of moving it.

- Canceling an action in the **Mobile Recorder** did not stop the object-capturing process.

- Closing a project did not automatically close the associated README file.

- The **Name** field was not automatically focused when creating a new project.

- The error `Failed to install the WebDriverAgent` occurred when importing provisioning profiles from Xcode 16.

- StudioAssist did not work after the token was refreshed. The "Unauthorized" error appeared during attempts to explain or generate code.

- Objects could not be highlighted correctly when using **Mobile Object Spy**.

- Self-Healing incorrectly marked the test step as passed by recovering a failed object using the Smart Locator, even though the locator contained an empty item, and the object could not be found.
- The **TestCloud** option in **Run** dropdown menu of a test case disappeared.

### Changes

- Updated the banner for StudioAssist on the **Start Page** to introduce the new chat window feature.

- Removed the Internet Explorer (IE) option from **Web Recorder** and **Object Spy**.

- [UI Changes] Removed the Gitter chat and Survicate feedback options.

- [StudioAssist Preferences] Updated **Max token** to **Max completion token** to align with OpenAI's new parameter. **Max completion token** now limits the number of tokens returned in a response. The default value has been increased from 2000 to 16000 to provide more detailed and comprehensive responses.

### Known limitations

- Reloading the **Start Page** results in a blank page.
- When opening an existing project already integrated with TestCloud, the **TestCloud** option does not appear in the **Run** menu. This happens when the logged-in user does not have access to the project ID specified in the TestOps integration.
- [StudioAssist chat window]:

    - StudioAssist doesn't pull information from Katalon documentation. For complex or uncommon queries, you may need to refer to Katalon documentation manually.
    - StudioAssist lacks awareness of test object libraries, variables, or test cases. You should specify details in your question to ensure correct outputs.
    - StudioAssist supports one conversation at a time. Use **Clear conversation** regularly to prevent context errors. Closing the chat also clears the conversation.
    - Responses may be inaccurate. Verify outputs and rate them as **Good** or **Not Relevant** to improve StudioAssist. Your feedback is not used to train the AI model or track your conversations.
    - On Windows, there is no functioning hotkey to open the StudioAssist chat window.



## <a id="concept-6psyssdb" class="anchor_top_offset"/>Version 10.0.1

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Release date: December 5, 2024</p> 

### New features

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><div className="p">Introduced Katalon Web Recorder Plus (beta) - a new recording engine in Studio that helps you capture more reliable locators, test on more complex scenarios of shadow DOM/iframe, and support Flutter-based web AUT. To learn more about this beta feature, see <a className="xref" href="/katalon-studio/record-and-spy/webui-record-and-spy-utilities/katalon-web-recorder-plus">Katalon Web Recorder Plus</a>.<ul className="ul"><li className="li"><p className="p">Recorder Plus is available for <span className="ph uicontrol">Web Recorder</span> and <span className="ph uicontrol">Object Spy</span> with Chrome and Edge Chromium, both on <span className="ph uicontrol">Active Browsers</span> and <span className="ph uicontrol">New Browsers</span>.</p></li></ul></div></li></ul> 

### Enhancements

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><div className="p">[TestCloud]:<ul className="ul"><li className="li"><p className="p">You can now run a test case with TestCloud mobile browser and desktop browser environment.</p></li><li className="li"><p className="p">Changed the availability of private devices from MEDIUM to HIGH in the TestCloud mobile device list.</p></li><li className="li"><p className="p">Added a note <code className="ph codeph">(*): This device has limited availability and may take longer to load.</code> in the Mobile Browser tab of the TestCloud Configuration dialog.</p></li><li className="li"><p className="p">Added execution session id in the console log when executing with TestCloud Mobile native app.</p></li></ul></div></li><li className="li"><p className="p">Added support for mobile testing with Android 15 official.</p></li><li className="li"><div className="p">[Web testing]:<ul className="ul"><li className="li"><p className="p">Added Chrome 131, Edge 131, and Firefox 132 compatibilities.</p></li><li className="li"><p className="p">Web Recorder and Object Spy using Firefox browser is now up-to-date as when using Chrome and Edge browser.</p></li><li className="li"><p className="p">Officially supported keyword: <code className="ph codeph">WebUI.scrollFromViewportOffset</code>. See: <a className="xref" href="/katalon-studio/keywords/keyword-description-in-katalon-studio/web-ui-keywords/webui-scroll-from-viewport-offset">[WebUI] Scroll From Viewport Offset</a>. </p></li></ul></div></li><li className="li"><p className="p">Supported JDBC Databricks integration.</p></li></ul> 

### Fixes

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">The <span className="ph uicontrol">Default value</span> of test case variables were not auto-updated when the file in the reference call was changed.</p></li><li className="li"><div className="p">[Web Recorder]:<ul className="ul"><li className="li"><p className="p">Clicking the <span className="ph uicontrol">Stop</span> button during playback in Web Recorder did not terminate the playback process.</p></li><li className="li"><p className="p">Error <code className="ph codeph">Your browser version or type does not support the BiDirectional WebDriver Protocol which is required for Smart Locator functionality. Please update your browser or switch to a compatible one.</code> when playback captured script in Web Recorder.</p></li><li className="li"><p className="p">Playback in the <span className="ph uicontrol">Recorder</span> dialog used both BiDi and internal recorder extensions when starting a new browser, instead of using only one as expected.</p></li><li className="li"><p className="p">Unable to record step for select value in the drop-down list of the website <code className="ph codeph">https://opensource-demo.orangehrmlive.com/web/index.php/auth/login</code>.</p></li><li className="li"><p className="p"><code className="ph codeph">Delay Between Actions</code> did not work if SmartWait was disabled.</p></li></ul></div></li></ul> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">Creating a new folder in <span className="ph uicontrol">Test Explorer</span> caused Katalon Studio to freeze.</p></li><li className="li"><p className="p">[KRE] Unable to override argument values from the command line to the <code className="ph codeph">console.properties</code> file.</p></li><li className="li"><p className="p">Closing and cleaning up a project did not clear the <span className="ph uicontrol">Request History</span>.</p></li><li className="li"><p className="p"><code className="ph codeph">CustomKeywords</code> descriptions were truncated in <span className="ph uicontrol">Manual</span> mode and did not display fully.</p></li><li className="li"><p className="p">Unable to import certain Postman collections into Katalon Studio.</p></li><li className="li"><p className="p">Opening a new project after modifying a Test Suite Collection did not push through, even after saving changes via the <span className="ph uicontrol">Save Resource</span> dialog.</p></li><li className="li"><div className="p">[Mobile]:<ul className="ul"><li className="li"><p className="p">Adjusting the time for the <code className="ph codeph">Mobile.tapAndHold</code> keyword in Mobile Recorder caused the captured Test Object to be removed.</p></li><li className="li"><p className="p">The <code className="ph codeph">Mobile.doubleTap</code> keyword did not work on Android apps.</p></li><li className="li"><p className="p">The long name warning shows twice when captured in the Mobile Recorder.</p></li><li className="li"><p className="p">Unable to start mobile recording with app ID input for a remote mobile device.</p></li></ul> </div></li><li className="li"><p className="p">Adding a p12 keystore under <span className="ph menucascade"><span className="ph uicontrol">Project</span><abbr title="and then"> &gt; </abbr><span className="ph uicontrol">Settings</span><abbr title="and then"> &gt; </abbr><span className="ph uicontrol">Network</span></span>  caused API testing to fail with the error: <code className="ph codeph">Could not initialize class org.apache.commons.ssl.KeyMaterial</code>.</p></li><li className="li"><p className="p">Katalon Studio failed to return to default content after handling an alert, causing subsequent Test Objects to be unrecognized.</p></li><li className="li"><p className="p">In the <span className="ph uicontrol">Manual</span> tab, adding a new test step did not automatically focus the cursor, requiring users to click on the step before typing.</p></li><li className="li"><div className="p">[JDBC]:<ul className="ul"><li className="li"><p className="p">JDBC properties in the <span className="ph uicontrol">Set Connection Properties for JDBC Driver</span> section, under <span className="ph menucascade"><span className="ph uicontrol">Project</span><abbr title="and then"> &gt; </abbr><span className="ph uicontrol">Settings</span><abbr title="and then"> &gt; </abbr><span className="ph uicontrol">Database</span></span>, were not correctly applied when reusing the global database connection.</p></li><li className="li"><p className="p">Unable to fetch data from SolidDB using the solidDB JDBC driver, despite successfully establishing a connection.</p></li><li className="li"><p className="p">Unable to connect to the database via JDBC when the <span className="ph uicontrol">Secure User and Password</span> option was unchecked.</p></li><li className="li"><p className="p">Unable to connect to Databricks using the JDBC driver due to unsupported <code className="ph codeph">setAutoCommit</code> functionality in Katalon Studio.</p></li></ul></div></li><li className="li"><p className="p">Unable to get the <code className="ph codeph">time</code> value in the Har file.</p></li><li className="li"><p className="p">Error <code className="ph codeph">Unable to create the selected preference page</code> appeared when navigating to <span className="ph menucascade"><span className="ph uicontrol">Katalon Studio Enterprise</span><abbr title="and then"> &gt; </abbr><span className="ph uicontrol">Settings...</span><abbr title="and then"> &gt; </abbr><span className="ph uicontrol">Cucumber</span><abbr title="and then"> &gt; </abbr><span className="ph uicontrol">Java</span></span>.</p></li><li className="li"><p className="p">[BDD testing] Step navigation from a BDD feature file to the corresponding step definition did not work. </p></li><li className="li"><p className="p">Response size in KB was displayed incorrectly for API calls.</p></li><li className="li"><p className="p">Error <code className="ph codeph">Unable to create the request object</code> occurred when starting step 2 of the API tour on macOS.</p></li><li className="li"><p className="p">Jira integration sent test results to Xray tests even when result sending was disabled.</p></li><li className="li"><p className="p">Error <code className="ph codeph">TestObject called before the type class is set</code> occurred when restoring a session with an open custom keyword file using the TestObject type.</p></li><li className="li"><p className="p">The list of devices was reset when reopening the TestCloud Configuration dialog of a test suite collection.</p></li><li className="li"><p className="p">The <code className="ph codeph">Save All</code> button did not save all changes made to a Web Service object after updating an authentication token.</p></li><li className="li"><p className="p">TestCloud failed to run web test cases on iOS devices.</p></li></ul> 

### Changes

- [UI Changes]:
    - Added a new **Preferences** page to enable or disable experimental features, starting with the Katalon Web Recorder Plus (beta). You can see the new page under **Katalon Studio** > **Settings...** > **Preferences** > **Katalon** > **Beta Features**.
    - Added a new static button with a call-to-action to review Katalon Studio on G2.
        <img src="https://docs.katalon.com/4fdace4f-af1c-4870-a52f-7a71b746d387/CTA_to_review_on_G2_1.png" width="500" alt="Added a new static button with a call-to-action to review Katalon Studio on G2"/> <br/>
        
- In Katalon Studio Web Recorder Plus (Beta), attributes like `src` and `href` are automatically escaped using `CSS.escape()` function. This adds backslashes (`\`) before special characters like slashes (`/`) and dots (`.`) to enhance stability and compatibility. Do note that these backslashes will not affect the execution of your test scripts. To learn more about the standard escaping function, refer to the following MDN documentation on `CSS.escape()`: [CSS: escape() static method](https://developer.mozilla.org/en-US/docs/Web/API/CSS/escape_static).
- Testing with Android 15:
    - Horizontal swipes in scripts may fail on Android 15 due to the swipe-back gesture, which triggers a return to the previous screen. To workaround this issue, on your device, navigate to **Settings** > **System** > **Navigation mode**, switch to **3-button navigation**, and then switch back to **Gesture navigation**. If the issue persists, reboot the device.
    - When using the `takeElementScreenshot` keyword, it occasionally fails with the following error message displayed: `com.assertthat.selenium_shutterbug.utils.web.ElementOutsideViewportException: Requested element is outside the viewport`, even if the element previously passed.

### Known limitations

<div xmlns="http://www.w3.org/1999/xhtml" className="p"><ul className="ul"><li className="li"><p className="p">[BDD testing] Unable to rename a <code className="ph codeph">.feature</code> file after it has been run.</p></li></ul></div>

## <a id="concept-h2xv4q0v" class="anchor_top_offset"/>Version 10.0.0

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Release date: October 30, 2024</p> 

### New features

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">Upgraded Katalon Studio to Selenium 4.22.</p></li><li className="li"><p className="p">Upgraded Java Client to version 9.2.3.</p></li><li className="li"><p className="p">Upgraded Appium server to version 2.11.1.</p></li><li className="li"><div className="p">Updated drivers' versions:<ul className="ul"><li className="li"><p className="p">Appium XCUITest Driver for iOS: 7.21.1</p></li><li className="li"><p className="p">Appium UiAutomator2 Driver for Android: 3.7.0</p></li></ul></div></li><li className="li"><div className="p">[Smart Wait and Smart Locator]:<ul className="ul"><li className="li"><p className="p">You can now execute scripts containing Smart Locator without installing an extension.</p></li><li className="li"><p className="p">You can now execute scripts using the Smart Wait function without installing an extension.</p></li><li className="li"><p className="p">Added support for enabling or disabling BiDi by adding the following desired capability: <code className="ph codeph">"webSocketUrl": true/false</code>, as shown in the sample screenshot below.<img className="image" width={600} src={useBaseUrl("/6fd6d09e-367b-416d-9c82-ed6f422904e5/Set_webSocketUrl__false.png")} /></p></li></ul></div></li><li className="li"><p className="p">Added support for mobile testing with iOS 18 official.</p></li><li className="li"><div className="p">Added new keywords:<ul className="ul"><li className="li"><p className="p"><code className="ph codeph">WebUI.newTab</code></p></li><li className="li"><p className="p"><code className="ph codeph">WebUI.scrollFromViewportOffset</code> (beta)</p></li></ul></div></li><li className="li"><p className="p">Added support for Katalon Runtime Engine Docker image on the ARM64 platform.</p></li></ul> 

### Enhancements

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">Added the <span className="ph uicontrol">Excludes</span> field to the Proxy setting in the Login dialog.</p></li><li className="li"><div className="p">[TestCloud]:<ul className="ul"><li className="li"><p className="p">Added the option to record, spy, and execute with randomly selected high-availability mobile devices.</p></li><li className="li"><p className="p">Added the ability to view and execute with private devices on TestCloud.</p></li></ul></div></li><li className="li"><p className="p">Added Chrome 130, Edge 130, and Firefox 131 compatibilities.</p></li><li className="li"><div className="p">[Security Compliance]:<ul className="ul"><li className="li"><p className="p">Updated WebDriverManager to version 5.9.2.</p></li><li className="li"><p className="p">Addressed multiple high-severity CVEs in <code className="ph codeph">dnsjava-2.1.8.jar</code>.</p></li><li className="li"><p className="p">Upgraded <code className="ph codeph">graphql-java_17.5.0.jar</code> to newer version.</p></li></ul></div></li></ul> 

### Fixes

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">Error when running recorded test steps on Web Recorder for the second time.</p></li><li className="li"><p className="p">[Email report] Unable to send email reports to recipients configured in the test suite while executing tests with KRE.</p></li><li className="li"><p className="p">Alert and confirmation dialogs disappeared too quickly for <code className="ph codeph">WebUI.acceptAlert</code> to interact.</p></li><li className="li"><div className="p">[Web Testing]:<ul className="ul"><li className="li"><p className="p"><code className="ph codeph">switchToWindowTitle</code> took too long to execute.</p></li><li className="li"><p className="p">Issue with width/height returned when using <code className="ph codeph">getViewportHeight</code> &amp; <code className="ph codeph">getViewportWidth</code>.</p></li></ul></div></li><li className="li"><div className="p">[Test Cloud]:<ul className="ul"><li className="li"><p className="p">TestCloud Device list was not reset to the first OS version when switching OS.</p></li><li className="li"><p className="p">Medium/low selected device was not retained when reopening the run dialog.</p></li><li className="li"><p className="p"><code className="ph codeph">-orgID</code> showed different values in the command line and TestCloud log information.</p></li></ul></div></li><li className="li"><p className="p"><span className="ph uicontrol">Enable Katalon Platform Integration</span> automatically enabled after closing the TestOps integration dialog.</p></li><li className="li"><p className="p">Katalon Studio unable to detect <code className="ph codeph">dateutil</code> in scripts.</p></li><li className="li"><div className="p">[Mobile]:<ul className="ul"><li className="li"><p className="p">Issues with <code className="ph codeph">Mobile.swipe</code> keyword.</p></li><li className="li"><p className="p"><code className="ph codeph">Mobile.pinchToZoomInAtPosition</code> keyword not working.</p></li><li className="li"><p className="p">[Mobile Recorder] Error during <span className="ph uicontrol">Swipe</span> action in Recorder tool when using Appium 2.x.</p></li><li className="li"><p className="p">Not able to swipe pop-ups.</p></li><li className="li"><p className="p">Tooltip display issues and difficulty clicking <span className="ph uicontrol">See</span> document hyperlink.</p></li><li className="li"><p className="p">Error when double-clicking an object in <span className="ph uicontrol">Mobile Recorder</span>.</p></li><li className="li"><p className="p"><code className="ph codeph">Mobile.dragAndDrop</code> keyword not working on Android Emulator.</p></li></ul></div></li><li className="li"><p className="p">Open notification in iOS partially dragged instead of fully opening.</p></li><li className="li"><p className="p">[Remote] Recorder/Spy tools unresponsive when starting a remote session without Application Path/ID.</p></li><li className="li"><p className="p">Incorrect Custom Desired capability for Edge.</p></li><li className="li"><p className="p">Object data type changes on formatting test file with <kbd className="ph userinput">Ctrl</kbd> + <kbd className="ph userinput">Shift</kbd> + <kbd className="ph userinput">F</kbd>.</p></li><li className="li"><p className="p">Unable to track dynamic test suite and data binding.</p></li><li className="li"><p className="p">Previously opened tabs not automatically reopened in Katalon Studio, except Test Cases tabs.</p></li><li className="li"><p className="p">Multi-threading issues in Katalon Studio version 9.x.</p></li><li className="li"><p className="p"><span className="ph uicontrol">Import from OpenAPI/Swagger</span> icon on the main menu disabled when navigating to <span className="ph uicontrol">Verification</span> or <span className="ph uicontrol">Validation</span> tab.</p></li><li className="li"><p className="p"><code className="ph codeph">WARNING: The 'isStretchWithOverflow' attribute is deprecated. Use the 'textAdjust' attribute instead.</code> was thrown when generating PDF reports on 9.7.0.</p></li><li className="li"><p className="p">Added <span className="ph uicontrol">HTTP Header</span> was removed automatically after modifying <span className="ph uicontrol">HTTP Body</span> in a Web Service Request.</p></li><li className="li"><p className="p"><span className="ph uicontrol">Close</span> and <span className="ph uicontrol">Close &amp; Clean up</span> project options did not work when there was an unsaved Test Suite Collection.</p></li><li className="li"><p className="p"><span className="ph uicontrol">About</span> dialog showed null in its title.</p></li><li className="li"><p className="p"><span className="ph uicontrol">Take Screenshot when execution failed</span> option was turned off by default.</p></li><li className="li"><p className="p">Recorded scripts could not be executed on Katalon Recorder.</p></li><li className="li"><p className="p">Error <code className="ph codeph">faultCode=PARSER_ERROR:....Invalid byte 1 of 1-byte UTF-8 sequence.</code> occurred when running SOAP requests with validation.</p></li><li className="li"><p className="p">Clicking <span className="ph uicontrol">Explore Analytics</span> in Studio Walkthrough did not initiate any action.</p></li><li className="li"><p className="p">Installer for Katalon Studio Enterprise and Katalon Studio extracted with duplicate folder names.</p></li><li className="li"><p className="p">[Git integration] Tracking branch was changed after pulling code from a different branch.</p></li><li className="li"><p className="p">[API] Missing space between <span className="ph uicontrol">Bearer</span> and token occurred when adding Bearer Authorization Header.</p></li><li className="li"><p className="p">Only one local plugin was loaded when reloading plugins.</p></li><li className="li"><p className="p">[Mac] Web Recorder window was minimized when clicking <span className="ph uicontrol">Record</span> button or rerunning the recorded script.</p></li><li className="li"><p className="p"><span className="ph uicontrol">Use system proxy configuration</span> option did not work on Windows.</p></li><li className="li"><p className="p">Error occurred when logging into Katalon Studio with proxy set to use <code className="ph codeph">.pac</code> file.</p></li><li className="li"><p className="p"><span className="ph uicontrol">Excludes</span> value required reloading after saving and reopening advanced settings.</p></li><li className="li"><p className="p">Log parsing errors in HAR file were encountered.</p></li><li className="li"><p className="p">Plugin did not reload when running Katalon Runtime Engine with TestCloud license only.</p></li><li className="li"><p className="p">Internal error occurred during <code className="ph codeph">Downloading Update...". 'byte[] org.apache.commons.io.IOUtils.byteArray()</code> when downloading version 9.7.2 from 9.6.0.</p></li></ul> 

### Changes

<div xmlns="http://www.w3.org/1999/xhtml" className="p"><ul className="ul"><li className="li"><div className="p">Application names updated:<ul className="ul"><li className="li"><p className="p">Free Edition: Katalon Studio</p></li><li className="li"><p className="p">Enterprise Edition: Katalon Studio Enterprise</p></li><li className="li"><p className="p">Apple Silicon Chip: Removed the <code className="ph codeph">Arm64</code> suffix.</p></li></ul></div></li><li className="li"><p className="p">Updated <code className="ph codeph">MobileBy</code> to <code className="ph codeph">AppiumBy</code> class.</p></li><li className="li"><p className="p">Adjusted offline license and On-Premises flow where login dialog is triggered.</p></li><li className="li"><p className="p">Ordered test cases alphabetically in Dynamic Test Suite.</p></li><li className="li"><p className="p">Any test case referencing <code className="ph codeph">SmartWaitWebDriver</code> will encounter a runtime error as the class has been removed.</p></li><li className="li"><p className="p">Updated <code className="ph codeph">WebUI.setViewPortSize</code> to align with <code className="ph codeph">WebUI.getViewportWidth</code> and <code className="ph codeph">WebUI.getViewportHeight</code>, ensuring consistent viewport size results.</p></li><li className="li"><p className="p">The <code className="ph codeph">licenseServer.properties</code> file has been removed as of version 10.0.0.</p></li><li className="li"><p className="p">Corrected the behavior of <code className="ph codeph">setViewportSize</code> to ensure that the values returned by <code className="ph codeph">getViewportWidth</code> and <code className="ph codeph">getViewportHeight</code> are consistent with the dimensions set by <code className="ph codeph">setViewportSize</code>. Note: When using the <code className="ph codeph">--window-size</code> in Desired Capabilities, <code className="ph codeph">getViewportWidth</code> and <code className="ph codeph">getViewportHeight</code> may return different values because this setting adjusts the window size, not the viewport size.</p></li><li className="li"><div className="p">Refactored <code className="ph codeph">DriverFactory</code>. Moved <code className="ph codeph">getChromeDriverPath</code> to <code className="ph codeph">ChromeDriverUtil</code>. To use <code className="ph codeph">getChromeDriverPath()</code>, add <code className="ph codeph"> import com.kms.katalon.core.webui.driver.chrome</code> and retrieve the path with:<pre className="pre codeblock"><code>String chromeDriverPath = ChromeDriverUtil.getChromeDriverPath() </code></pre></div></li><li className="li"><div className="p">Based on Selenium 4 documentation, test capabilities that are not structured to be W3C compliant may prevent a session from starting. The following list outlines the W3C WebDriver standard capabilities:<ul className="ul"><li className="li"><p className="p"><code className="ph codeph">browserName</code></p></li><li className="li"><p className="p"><code className="ph codeph">browserVersion</code> (replaces <code className="ph codeph">version</code>)</p></li><li className="li"><p className="p"><code className="ph codeph">platformName</code> (replaces <code className="ph codeph">platform</code>)</p></li><li className="li"><p className="p"><code className="ph codeph">acceptInsecureCerts</code></p></li><li className="li"><p className="p"><code className="ph codeph">pageLoadStrategy</code></p></li><li className="li"><p className="p"><code className="ph codeph">proxy</code></p></li><li className="li"><p className="p"><code className="ph codeph">timeouts</code></p></li><li className="li"><p className="p"><code className="ph codeph">unhandledPromptBehavior</code></p></li></ul></div></li><li className="li"><p className="p">Any capability not listed above must include a vendor prefix. For example, when running on TestCloud, using <code className="ph codeph">app</code> and <code className="ph codeph">deviceName</code> in desired capabilities can disrupt the session creation process. The correct format for custom capabilities requires a vendor prefix, such as <code className="ph codeph">katalon:option</code> for Katalon.</p></li></ul></div>

### Known limitations

<div xmlns="http://www.w3.org/1999/xhtml" className="p"><ul className="ul"><li className="li"><p className="p">Katalon Compact Utility (KCU) is not supported with BiDi due to a Chrome limitation with profile management.</p></li><li className="li"><p className="p">When using BiDi, a BiDi-CDP Mapper tab opens to start the connection.</p></li><li className="li"><div className="p">BiDi does not work with Incognito mode in Chrome and Edge Chromium. Attempting to open a session in Incognito mode with BiDi enabled causes the browser session to open briefly and then close automatically. This issue affects: Chrome, Edge Chromium, and Chrome Headless. Workaround:<ul className="ul"><li className="li"><p className="p">Set <code className="ph codeph">webSocketUrl = false</code> in desired capabilities to disable BiDi if Incognito mode is required.</p></li></ul></div></li><li className="li"><p className="p">BiDi does not work with custom profiles in Chrome and Edge Chromium. Attempting to open a session with a custom profile and BiDi enabled causes the session to fail with an initialization error.</p></li><li className="li"><p className="p">Docker image on linux/arm64 supports Firefox version 129 instead of the latest version 131.</p></li><li className="li"><p className="p">Removal of <code className="ph codeph">AbstractEventListener</code>, <code className="ph codeph">EventFiringWebDriver</code>, and <code className="ph codeph">WebDriverEventListener</code> in Selenium. Follow Selenium documentation to migrate test scripts that use these classes: <a className="xref j-external-link" href="https://www.selenium.dev/blog/2023/java-removal-of-deprecated-events-classes/" target="_blank">Removal of AbstractEventListener + EventFiringWebDriver + WebDriverEventListener</a>.</p></li><li className="li"><div className="p">Simple dialogs (alert/prompt) handler behavior: The <code className="ph codeph">unhandledPromptBehavior</code> capability, which defaults to "dismiss and notify" per W3C standards, dismisses simple dialogs automatically. Workaround:<ul className="ul"><li className="li"><p className="p">Set <code className="ph codeph">unhandledPromptBehavior</code> to <code className="ph codeph">ignore</code> so that you can handle dialogs manually.</p></li></ul></div></li><li className="li"><div className="p">Install dependencies: Node installation failed during dependency setup, including manual installation (without Katalon Studio). A warning may appear stating, <code className="ph codeph">The post-install step did not complete successfully</code>. Workaround:<ul className="ul"><li className="li"><div className="p">Run the following commands to resolve the issue:<pre className="pre codeblock"><code>/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"{"\n"}brew update{"\n"}brew uninstall node{"\n"}brew install node{"\n"}</code></pre></div></li></ul></div></li></ul></div>
