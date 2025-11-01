---
title: Desktop browser testing with TestCloud
---

TestCloud supports desktop browser testing across multiple browsers on Windows, macOS and Linux. The desktop test environments include: Chrome, Chrome (headless), Edge Chromium, Firefox, Firefox (headless), Safari (macOS only) and IE (Windows only).

Desktop browsers on TestCloud are accessible from both Katalon Studio and TestOps. This guide shows you how to run TestCloud desktop browser tests in Studio, TestOps, and KRE.

- An active Katalon TestCloud subscription or trial. See [TestCloud Trial](https://docs.katalon.com/katalon-platform/administer/katalon-platform-packages/testcloud-feature-comparison).

## Run tests on desktop browsers in Studio

To run desktop browser tests in a TestCloud environment, follow these steps:

**For Test Suite**

1. Open a test suite.
2. In the main toolbar, click the dropdown arrow of the *Run* button and select TestCloud.The **TestCloud Configuration** dialog appears as below. Specify the OS, browser, and browser version for **Desktop Browsers** environment. Then click **Run**.
    
    <img alt="Select execution environment" width="200" src="https://docs.katalon.com/2af21b60-c18e-11ed-a4d3-0242cfbc79b5/KS_select_execution_env.png" />
    
    <img alt="TestCloud configuration dialog" width="600" src="https://docs.katalon.com/de35d260-a550-11ee-b8c3-0242c7a41fd4/KS_TestCloud_dialog.png" />
    

**For Test Suite Collection (TSC)**

1. Open a TSC and double-click the **Run with** row of the individual test suite.
    
    <img alt="Click Run with column" width="600" src="https://docs.katalon.com/436f928c-218c-44f0-9f3e-470a0406a696/ks-testcloud-double-click-run-with-row.png" />
    
    The **Select an environment** dialog appears as below. Choose **TestCloud** as your test environment, then click OK.
    
    <img alt="Select TestCloud environment in KS" width="300" src="https://docs.katalon.com/a05cea6b-e3ff-4d49-816d-02e7b6404ea9/select-testcloud-env-in-ks.png" />
    
2. Double-click the **Run Configuration** row of the TSC to prompt the **TestCloud Configuration** dialog.
3. In the **TestCloud Configuration** dialog, specify the OS, browser, and browser version for **Desktop Browsers** environment.
    
    <img alt="TestCloud configuration dialog in KS" width="500" src="https://docs.katalon.com/de35d260-a550-11ee-b8c3-0242c7a41fd4/KS_TestCloud_dialog.png" />
    
4. Click **Run**.

## Run test on desktop browsers in TestOps

To run desktop browser tests in a TestCloud environment, follow these steps:

1. Sign in to Katalon TestOps and go to your project.
2. Go to **Test Execution** > **Schedule Test Run**.
    
    The **Schedule Test Run** dialog pops up.
    
3. In the **Environment** section, click the drop-down menu and select **More options**.
    
    <img alt="Click More options" width="600" src="https://docs.katalon.com/0d3821f0-2c37-11ee-bd4d-0242c7a41fd4/TC_environment_select_more_options_button.png" />
    
4. You should see the dialog below. Select the **Desktop Browsers** tab and select your environment.For example, you can execute your tests on Chrome browser version 128 of a macOS machine.
    
    <img alt="Desktop browser environments on TestOps" width="700" src="https://docs.katalon.com/e2e7dfc0-691f-4665-88af-0df6c4f7a720/tc-desktop-browser-environment.png" />
    
5. Click **Save** to return to the **Schedule Test Run** dialog.
6. Fill in the required fields and click **Run** to trigger the test run.
    
    <img alt="Schedule desktop browser test on TestOps" width="500" src="https://docs.katalon.com/ecbefb6f-ebe5-4cd8-b5b2-3ceeeaa01475/tc-desktop-browser-test-on-testops.png" />

## Run tests on desktop browsers in Katalon Runtime Engine

When running tests from KRE to TestCloud environments, you only need a TestCloud subscription; a KRE license is not required.

To run desktop browser tests with Katalon Runtime Engine, we recommend using Command Builder in Katalon Studio to generate the commands. For detailed instruction, refer to: [Command Builder in Katalon Studio](https://docs.katalon.com/katalon-studio/execute-tests/katalon-runtime-engine/get-started-with-katalon-runtime-engine).

After you have declared the required information, specify the mobile browser environment in the **Run Configuration** section and generate the command to run with KRE.

<img alt= "Command Builder in Katalon Studio" src="https://tw-cdn.katalon.com/katalon-testcloud/KS-command-builder-desktop-browsers.png" width="600" />