---
title: Generate automated tests with TestPak extension
---

This document introduces the TestPak extension and explains how to use it to convert manual tests to automated tests.

:::caution Requirements
- You have an active TrueTest license.
- You have an active TestOps license.
- TrueTest has been configured in the relevant Application Under Test (AUT). If not, refer to this configuration guide: [Configure TrueTest Agent](/katalon-truetest/test-case-generation-with-truetest/configure-truetest-agent).
:::

The TestPak Extension is a Chrome add-on that lets you record your manual test runs in TestOps and instantly generate automated test scripts from them.

With TestPak and TrueTest, you can:

- Convert passed manual test cases into automated ones with a single click.
- Automatically link each generated script to its original manual test case for full traceability.
- Build maintainable scripts using TrueTest’s shared object repository and functions.
The TestPak Extension is a Chrome add-on that lets you record your manual test runs in TestOps and instantly generate automated test scripts from them.

With TestPak and TrueTest, you can:

- Convert passed manual test cases into automated ones with a single click.
- Automatically link each generated script to its original manual test case for full traceability.
- Build maintainable scripts using TrueTest’s shared object repository and functions.

You can also filter manual execution sessions when creating user journey maps, helping you visualize real user flows.

Follow the steps below to create a manual test run, install the extension, and generate your first automated scripts.

---
You can also filter manual execution sessions when creating user journey maps, helping you visualize real user flows.

Follow the steps below to create a manual test run, install the extension, and generate your first automated scripts.

---

## Create a manual test run

Follow this guide to create a manual test run: [Create a manual test run](/katalon-platform/execute/manual-executions/create-a-manual-test-run). After creating a manual test case, proceed with the next section.
Follow this guide to create a manual test run: [Create a manual test run](/katalon-platform/execute/manual-executions/create-a-manual-test-run). After creating a manual test case, proceed with the next section.

## Install TestPak extension
The TestPak Extension allows QA testers to capture user interactions during executing manual test cases within their application under test (AUT). These actions from the manual test cases will be converted to automated test cases.
<img src="https://tw-cdn.katalon.com/truetest/manual-to-automated/testpak-extension-chrome-store.png" width="1080" alt="TestPak extension on Chrome Store" />

1. In the **Create Manual Test Run** page, click **Run Now** to launch the test. 
<img src="https://tw-cdn.katalon.com/truetest/manual-to-automated/create-manual-test-case-screen.png" width="800" alt="Create manual test run page" />

2. If you selected Chrome in **Configurations**, the **Enable Test Session Recording** dialog will appear. Click **Install Extension** to direct to the Chrome web store page. 
<img src="https://tw-cdn.katalon.com/truetest/manual-to-automated/install-testpak-extension-dialog.png" width="800" alt="Install TestPak extension dialog" /><br/>

3. Add the TestPak Extension to Chrome, and you’ll be redirected back to TestOps with a confirmation dialog once the installation is complete. 
   - You only need to install once. After the extension is added to Chrome, it will remain installed for future test runs.
<img src="https://tw-cdn.katalon.com/truetest/manual-to-automated/testpak-extension-success-installation.png" width="500" alt="TestPak success installation dialog" />
The TestPak Extension allows QA testers to capture user interactions during executing manual test cases within their application under test (AUT). These actions from the manual test cases will be converted to automated test cases.
<img src="https://tw-cdn.katalon.com/truetest/manual-to-automated/testpak-extension-chrome-store.png" width="1080" alt="TestPak extension on Chrome Store" />

1. In the **Create Manual Test Run** page, click **Run Now** to launch the test. 
<img src="https://tw-cdn.katalon.com/truetest/manual-to-automated/create-manual-test-case-screen.png" width="800" alt="Create manual test run page" />

2. If you selected Chrome in **Configurations**, the **Enable Test Session Recording** dialog will appear. Click **Install Extension** to direct to the Chrome web store page. 
<img src="https://tw-cdn.katalon.com/truetest/manual-to-automated/install-testpak-extension-dialog.png" width="800" alt="Install TestPak extension dialog" /><br/>

3. Add the TestPak Extension to Chrome, and you’ll be redirected back to TestOps with a confirmation dialog once the installation is complete. 
   - You only need to install once. After the extension is added to Chrome, it will remain installed for future test runs.
<img src="https://tw-cdn.katalon.com/truetest/manual-to-automated/testpak-extension-success-installation.png" width="500" alt="TestPak success installation dialog" />

## Execute test cases

1. Click **Start Testing** in the dialog. The browser will launch, and the TestPak panel will display the details of the current test case.
2. Select the test environment with TrueTest enabled, then click **Start**.
   <img src="https://tw-cdn.katalon.com/truetest/manual-to-automated/testpak-panel-select-environment.png" width="250" alt="Select TrueTest environment" />
3. Follow the test steps as written. 
4. Compare actual behavior with the **Expected Results**, then mark the **Test Case Result** as `Passed` or `Failed` accordingly. 
5. (Optional) You can click **Retest** to reset the recording of the test cases. This will clear all existing test step results, reset the previous testing duration, and restart the timer for a new execution.
   <img src="https://tw-cdn.katalon.com/truetest/manual-to-automated/click-retest.png" width="300" alt="Click retest" />
6. When done, click **Next Test Case** to continue.
   - Any test case that is not assigned a test result will be considered as **Skipped**. Click **Confirm** to continue regardless.
7. Once all test cases are marked with a result, you are prompted with the **End Test Run** dialog. Click **End** to finish the test run.
   <img src="https://tw-cdn.katalon.com/truetest/manual-to-automated/end-test-run-dialog.png" width="300" alt="End test run dialog" />
1. Click **Start Testing** in the dialog. The browser will launch, and the TestPak panel will display the details of the current test case.
2. Select the test environment with TrueTest enabled, then click **Start**.
   <img src="https://tw-cdn.katalon.com/truetest/manual-to-automated/testpak-panel-select-environment.png" width="250" alt="Select TrueTest environment" />
3. Follow the test steps as written. 
4. Compare actual behavior with the **Expected Results**, then mark the **Test Case Result** as `Passed` or `Failed` accordingly. 
5. (Optional) You can click **Retest** to reset the recording of the test cases. This will clear all existing test step results, reset the previous testing duration, and restart the timer for a new execution.
   <img src="https://tw-cdn.katalon.com/truetest/manual-to-automated/click-retest.png" width="300" alt="Click retest" />
6. When done, click **Next Test Case** to continue.
   - Any test case that is not assigned a test result will be considered as **Skipped**. Click **Confirm** to continue regardless.
7. Once all test cases are marked with a result, you are prompted with the **End Test Run** dialog. Click **End** to finish the test run.
   <img src="https://tw-cdn.katalon.com/truetest/manual-to-automated/end-test-run-dialog.png" width="300" alt="End test run dialog" />

## Generate automated tests
After the test run finishes, you’ll be prompted to generate automated test cases from test cases with `Passed` result and no linked automated tests. 

1. When prompted, click **Generate Now** to proceed. Alternatively, you can manually trigger the process by clicking **Generate Automated Test Cases**.
   <img src="https://tw-cdn.katalon.com/truetest/manual-to-automated/ready-to-automate-dialog.png" width="800" alt="Ready to automate dialog" />
2. In the **Generate Automated Test Cases** dialog:
    1. Select an **Assignee**: This assignee will receive a notification when the automated tests are ready.
    2. Select the manual test cases you want to convert to automated, then click **Generate**.Select the manual test cases you want to convert to automated, then click **Generate**.
   <img src="https://tw-cdn.katalon.com/truetest/manual-to-automated/generate-auto-test-case-dialog.png" width="500" alt="Generate automated test cases dialog" />

#### Result
A notification box will confirm that automation generation has started. Once it completes, navigate to **Tests** > **Test Cases** to view the generated test cases.

The generated test cases are stored in the registered script repository. 

By default, they have the **Draft** status. You can download them to review and optionally edit them in Katalon Studio, then publish them as official automated test cases.

<img src="https://tw-cdn.katalon.com/truetest/manual-to-automated/view-generated-auto-test-cases.png" width="800" alt="View generated test cases in script repo" />

---

## Next steps
- After you’ve used the TestPak extension to generate automated test cases, you can review flows created from the manual execution sessions. You can filter flows by their source, for example, by *User Sessions* or by *Manual Execution*.
    - You’ll also have the ability to **retain** flows (including manual flows) that you still need, or **archive** (or mark obsolete) those you no longer want. This helps you keep your flow data relevant and clean.
    For more details, see [Review user journey map](/katalon-truetest/test-case-generation-with-truetest/generate-user-journey#view-user-journey-map).
## Next steps
- After you’ve used the TestPak extension to generate automated test cases, you can review flows created from the manual execution sessions. You can filter flows by their source, for example, by *User Sessions* or by *Manual Execution*.
    - You’ll also have the ability to **retain** flows (including manual flows) that you still need, or **archive** (or mark obsolete) those you no longer want. This helps you keep your flow data relevant and clean.
    For more details, see [Review user journey map](/katalon-truetest/test-case-generation-with-truetest/generate-user-journey#view-user-journey-map).

