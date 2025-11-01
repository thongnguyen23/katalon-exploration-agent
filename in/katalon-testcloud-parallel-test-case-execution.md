---
title: Parallel test case execution
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

:::caution Requirements & Availability
- Make sure you have the Test Lead or Tester role. Go to [roles](/katalon-testops/administration-and-licensing/manage-systems/permissions/about-roles) or [permissions](/katalon-testops/administration-and-licensing/manage-systems/permissions/about-permissions) for more information or learn how to [assign a Project Admin here](/katalon-testops/administration-and-licensing/manage-administrators/assign-or-unassign-project-administrators). 
- This feature is only available for automated test run configured with TestCloud environments.
- Applies to Test Suites (TS) and Test Suite Collections (TSC). Currently not supported for dynamic test suite.
:::

## Introduction

Parallel Test Case Execution speeds up your test runs by executing multiple test cases at the same time.

Instead of running test cases one after another, TestCloud **splits them across available sessions** and completes your test suite faster.

TestCloud optimizes resource use while keeping a buffer of sessions available. For example, you have 10 test suites, each with 10 test cases. TestCloud continuously analyzes the queue and distributes test cases across the available licenses until all are used.

Katalon already provides execution modes in a Test Suite Collection (TSC), which determine how test suites are executed. Parallel Test Case Execution is distinct because it operates at the **test case level**, not just at the suite level. The following table highlights the key differences.

| **Mode** | **Scope** | **Description** |
| --- | --- | --- |
| **Parallel Test Case Execution** | Test Suite | <ul><li>Runs individual test cases in parallel within a suite or across suites, filling all available sessions.</li><li>Offers maximum speed and efficiency.</li></ul> |
| **Sequential (TSC)** | Test Suite Collection | Runs one test suite after another. |
| **Parallel (TSC)** | Test Suite Collection | Runs multiple test suites in parallel, limited by your available TestCloud session quota. |

## View available sessions

You can view your TestCloud sessions by visiting the [TestCloud Web App](https://cloud.katalon.com/) home page. The dashboard displays:

- The number of sessions purchased for each test run type (Desktop Browser, Mobile Browser, Mobile Native App).
- The number of sessions currently running.
- The number of sessions currently queued.

<img src="https://tw-cdn.katalon.com/katalon-testcloud/parallel-test-case-execution/testcloud-check-parallel-session.png" width="1080" alt="TestCloud web app home page" />


## Enable parallel test case execution

1. Go to **Executions**. The Executions list appears by default.
2. Click **+ Create** > **Create Automated Test Run**. The **Create Automated Test Run** page appears.
<img src="https://tw-cdn.katalon.com/katalon-testcloud/parallel-test-case-execution/create-automated-test-run-screen.png" alt="Create auto test run" width="1080"/>
<br/>

3. Input the following details:
- **Test Run Name:** The name of the test run
- **Release Version (optional):** The associated release
- **Sprint (optional):** The associated sprint

4. Select a **Test Run Type**: **Desktop & Mobile Browser**, **Mobile Native App** or **Web Services**.
5. Click **Select Tests** to select from the list of test suites, then click **Save** when you’re done.
<img src="https://tw-cdn.katalon.com/katalon-testops/Execution/automated-execution/select-tests-screen.png" alt="Select test suites" width="800" />

6. Enable the **Parallelize Test Cases** toggle.
<img src="https://tw-cdn.katalon.com/katalon-testcloud/parallel-test-case-execution/enable-parallel-test-case-toggle.png" alt="Enable parallel test case toggle" width="800"/>

7. Click the settings icon of each test suite to configure TestCloud environment. 
<img src="https://tw-cdn.katalon.com/katalon-testops/Execution/automated-execution/test-suite-information-screen.png" alt="Test suite information" width="800" />

:::note
- For standalone test suites, you can configure multiple environments. However, if a test suite is part of a test suite collection, you can assign only one environment per test suite.
:::

8. In the **Select Configurations** dialog, select **Cloud Hosted** and specify the environment as follows:

- For desktop browser, specify the OS, browser and browser version.
  <img src="https://tw-cdn.katalon.com/katalon-testops/Execution/automated-execution/configure-desktop-mobile-browser-environment.gif" alt="Desktop and mobile browser configuration" width="500" />
- For mobile native app, select a mobile app first, then specify the device configuration.
  <img src="https://tw-cdn.katalon.com/katalon-testops/Execution/automated-execution/configure-mobile-app-env.png" alt="Mobile app configuration" width="500" />
- For Web Services, choose the local test environment where you can run or execute your tests from the list of available Agents.
  <img src="https://tw-cdn.katalon.com/katalon-testops/Execution/automated-execution/web-services-configuration.png" alt="Web services configuration" width="500" />

9. In the **Automated Test Run** page, click **Run Now** to execute instantly or **Schedule** to create a recurring schedule for it.

## Best practices
Refer to the following recommendations to optimize your use of Parallel Test Case Execution.

- Your Account should have at least 3 available TestCloud licenses per test run type for optimal efficiency.
- To utilize available sessions, schedule runs across different environments (for example, Desktop Browser and Mobile Native App). Avoid scheduling two test runs of the same type with **Parallelize Test Cases** enabled, as only one can execute at a time.
- **Test cases must be independent**. If the second test case requires data created by the first test case, the test run might fail when running in test case level parallel mode.