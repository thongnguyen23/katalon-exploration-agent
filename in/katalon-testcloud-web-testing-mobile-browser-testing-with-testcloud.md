---
title: Mobile browser testing with TestCloud
---

TestCloud mobile browser testing supports built-in browser for each OS. The mobile test environments include built-in browser of each operating system (OS): Safari for iOS and Chrome for Android.

Mobile browsers on TestCloud are accessible from both TestOps and Katalon Studio.

This guide shows you how to run TestCloud mobile browser tests in Katalon Studio, TestOps, and Katalon Runtime Engine (KRE).

:::caution Requirements
- You have an active TestCloud subscription or a trial.
:::

## Run tests on mobile browsers in Studio

To run mobile browser tests in a TestCloud environment from Katalon Studio, follow these steps:

**For Test Suite**
1. Open a test suite.
2. In the main toolbar, click the dropdown arrow of the *Run* button and select TestCloud.
   <img src="https://tw-cdn.katalon.com/katalon-testcloud/mobile-browser-testing/select-testcloud.png" width="200" alt="Select TestCloud environment" /> <br/> 
   
   The TestCloud Configuration dialog appears as below. Specify the OS, browser, and browser version for Mobile Browsers environment. Then click **Run**.
   <img src="https://tw-cdn.katalon.com/katalon-testcloud/mobile-browser-testing/testcloud-configuration-dialog-ks.png" width="500" alt="TestCloud configuration dialog" />

**For Test Suite Collection (TSC)**
1. Open a TSC and double-click the **Run with** row of the individual test suite. 
   <img src="https://tw-cdn.katalon.com/katalon-testcloud/mobile-browser-testing/tsc-run-with-testcloud.png" width="800" alt="TestCloud configuration dialog" /> <br/> 
   The Select an environment dialog appears as below. Choose TestCloud as your test environment, then click **OK**.
   <img src="https://tw-cdn.katalon.com/katalon-testcloud/mobile-browser-testing/tsc-select-environment.png" width="300" alt="TestCloud configuration dialog" />
2. Double-click the **Run Configuration** row of the TSC to prompt the **TestCloud Configuration** dialog.
3. In the **TestCloud Configuration** dialog, specify the OS, browser, and browser version for **Mobile Browsers** environment.
   <img src="https://tw-cdn.katalon.com/katalon-testcloud/mobile-browser-testing/testcloud-configuration-dialog-ks.png" width="500" alt="TestCloud configuration dialog" />
4. Click **Run**.


## Run test on mobile browsers in TestOps

To run desktop browser tests in a TestCloud environment, follow these steps:

1. Sign in to Katalon TestOps and go to your project.
2. Go to **Test Execution** > **Schedule Test Run**.
    
    The **Schedule Test Run** dialog pops up.
    
3. In the **Environment** section, click the drop-down menu and select **More options**.
   <img src="https://tw-cdn.katalon.com/katalon-testcloud/mobile-browser-testing/click-more-options-in-testops.png" width="600" alt="Click More options" />
4. You should see the dialog below. Select the **Mobile Browsers** tab and select your mobile devices. For example, you can execute your tests on Safari browser of **iPhone 15 Pro Max** and **16 Pro**.
   <img src="https://tw-cdn.katalon.com/katalon-testcloud/mobile-browser-testing/configure-environment-in-testops.png" width="800" alt="Configure test environment for test suite" />
5. Click **Save** to return to the **Schedule Test Run** dialog.
6. Fill in the required fields and click **Run** to trigger the test run.
   <img src="https://tw-cdn.katalon.com/katalon-testcloud/mobile-browser-testing/schedule-test-run-dialog.png" width="600" alt="Schedule test run dialog in TestOps" />
7. To check the progress of your test runs, see: [View a test run summary](/katalon-platform/analyze/reports/view-test-reports/view-test-run-results/view-a-test-run-summary).


## Run tests on desktop browsers in Katalon Runtime Engine

When running tests from KRE to TestCloud environments, you only need a TestCloud subscription; a KRE license is not required.

To run desktop browser tests with Katalon Runtime Engine, we recommend using Command Builder in Katalon Studio to generate the commands. For detailed instruction, refer to: [Command Builder in Katalon Studio](https://docs.katalon.com/katalon-studio/execute-tests/katalon-runtime-engine/get-started-with-katalon-runtime-engine).

After you have declared the required information, specify the mobile browser environment in the **Run Configuration** section and generate the command to run with KRE.
<img src="https://tw-cdn.katalon.com/katalon-testcloud/mobile-browser-testing/set-command-builder-mobile-browser.png" width="700" alt="Set TestCloud environment with KRE" />