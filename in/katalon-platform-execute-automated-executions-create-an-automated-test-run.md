---
title: "Automated Test Run"
---

Automated test runs let you **validate your application continuously and consistently** without manual effort. Instead of running test suites one by one locally, you can orchestrate test runs in **TestOps**, configure environments, schedule them, and track results over time.

**Key benefits:**

- **Centralized execution**: All runs managed in TestOps, no need to rely on local machines.
- **Scalable environments**: Choose cloud-hosted or self-hosted agents depending on your infra.
- **Flexible triggers**: Run instantly or schedule to align with CI/CD pipelines, sprints, or releases.
- **Deeper insights**: Link test runs with releases, sprints, and builds to track quality trends.
## Understanding Test Run Types

When creating a test run, you must choose a **Test Run Type**. Choosing the correct type ensures that your tests are executed in the right runtime with the right dependencies. Each type corresponds to a different kind of testing environment:

- **Desktop & Mobile Browser**
    - For functional tests on web applications.
    - Runs across OS + browser combinations (e.g., Chrome on Windows, Safari on macOS).
- **Mobile Native Ap**
    - For testing Android/iOS apps.
    - Requires uploading the app (APK/IPA) and configuring devices/emulators.
- **Web Services**
    - For testing APIs and backend services.
    - Runs in your chosen local/cloud agent environment, validating requests and responses.
<img src="https://tw-cdn.katalon.com/katalon-platform/automated-test-run/test-run-type.png" alt="Test Run Types List" />

## Configurations
A test run in TestOps requires you to configure how, where, and with what parameters the tests will execute. These configurations ensure that your automation adapts to your infrastructure, scales effectively, and produces reliable results.

TestOps test runs always rely on an execution agent—the runtime environment responsible for running your tests. The right choice depends on convenience, compliance requirements, and the infrastructure available to your team.

> **Rule of Thumb**:
> - Use **Cloud-hosted** for convenience and scalability.
> - Use **Self-hosted/KRE** for compliance, local dependencies, or CI/CD integrations.

### Cloud-hosted Agents (TestCloud)

- Managed by Katalon.
- Scales instantly across browsers, OS, and devices.
- Best for fast setup and zero maintenance.

### Self-hosted Agents
- Installed on your infrastructure (on-prem, VM, private cloud).
- Best for secure or restricted environments, or when you need tests to run inside your own network.
- Supports both UI Mode (Studio artifacts) and Command Line Mode (KRE/other frameworks).

<!-- ### Katalon Runtime Engine (KRE) Agents

- KRE powers execution without Studio’s UI.
- Works with both **UI Mode** and **Command Line Mode**.
- Multiple versions can be registered in TestOps for compatibility with different projects. -->

---

## Profiles in Test Runs

Profiles (from Katalon Studio Execution Profiles) let you **parameterize test data and environments**:

- Store variables such as URLs, credentials, API keys.
- Allow the same test suite to run across Dev, QA, Staging, or Prod-like setups.
- Selected in UI Mode via dropdown, or passed in CLI with `executionProfile`.

---

## Two Configuration Modes: UI Mode vs Command Line Mode

When setting up a test run, you have **two ways** to configure execution:

**Rule of thumb**

Start with **UI mode** for Katalon-managed tests, use **Command Line mode** when integrating with external tools or advanced CI/CD workflows.

### 1. Setting Up with UI Mode
- **What it is**: Guided setup in the TestOps web UI. Best for most teams who want a clear, form-based approach.
- **When to use**:
    - You want to select test suites directly.
    - You need environment selection (browsers, mobile devices, API agent).
    - You plan to use TestOps’ **advanced settings** (visual testing, private/local testing, KRE version).
- **Advantages**: User-friendly, no syntax needed, quick setup.
- **Limitations**: Tied to Katalon Studio artifacts (Test Suites/Test Suite Collections).

<img src="https://tw-cdn.katalon.com/katalon-platform/automated-test-run/UI-mode.png" alt="UI mode - Create automated test run"/>


Follow these steps to create a run with UI Mode:

1. Go to **Executions** → Click **+ Create > Create Automated Test Run**.
2. Fill in details:
    - **Test Run Name**
    - **Creator** (default: current user)
    - **Release/Sprint** (optional, for tracking coverage).
3. Select **Test Run Type**: Desktop & Mobile Browser, Mobile Native App, or Web Services.
4. Click **Select Tests** → pick test suites and test suite collections from the repository.
    <img src="https://tw-cdn.katalon.com/katalon-testops/Execution/automated-execution/select-tests-screen.png" alt="Select test suites/test suite collections"/>
5. Select the **Profile.**
6. Configure **environment settings** depending on the type:
    - **Standalone suites**: You can configure multiple environments.
    - **Test Suite Collection (TSC)**:
        - TSC configurations are defined by the user in **Katalon Studio**.
        - When you select a TSC and schedule it in **TestOps**, the system will automatically apply the configurations that were previously set in Katalon Studio (including test suites, profiles, environments, and execution modes).
        - However, if you manually update any configuration of the TSC in **TestOps**, that TSC’s configurations will no longer sync with the one in Katalon Studio.
    <img src="https://tw-cdn.katalon.com/katalon-platform/automated-test-run/multiple-config.png" alt="Select multiple config for a test suite"/>
7. (Optional) Set up **Parallelize Test Cases**:
    - This toggle enables execution of individual test cases in parallel within a test suite or across multiple suites, maximizing usage of available sessions for speed and efficiency. Unlike Test Suite Collection (TSC) execution modes, this feature works at the test case level.
    - TestCloud optimizes resource allocation while maintaining a buffer of available sessions. For example, if you have 10 test suites each containing 10 test cases, TestCloud continuously analyzes the queue and distributes test cases across your available licenses until all are used.
    
    **Important:**
        - Your test cases must be independent to avoid unpredictable failures.
        - To learn more, please refer to this [document](/katalon-testcloud/parallel-test-case-execution).
    <img src="https://tw-cdn.katalon.com/katalon-platform/automated-test-run/true-parallel.png" alt="True Parallel mode"/>
    
    For **Test Suite Collection:**
    
    When **Parallelize Test Cases** is toggled on, the collection will default to **Parallelize Test Cases**. To choose the two run mode below, you have to untoggle **Parallelize Test Cases**.
        - **Parallel mode**: Runs multiple test suites in parallel, limited by your available TestCloud session quota.
        - **Sequential mode**: Runs one test suite after another.
    <img src="https://tw-cdn.katalon.com/katalon-platform/automated-test-run/tsc-run-mode.png" alt="TSC Run mode"/>


### 2. Setting Up with Command Line Mode

- **What it is**: Runs tests via command syntax (Katalon Runtime Engine or other frameworks).
- **When to use**:
    - You need **more flexibility**, e.g., passing custom arguments.
    - You run **non-Katalon frameworks** (e.g., Pytest, JUnit).
    - You want consistency with existing **CI/CD scripts**.
- **Advantages**: Supports any framework, highly customizable.
- **Limitations**: Requires familiarity with CLI and execution syntax.
<img src="https://tw-cdn.katalon.com/katalon-platform/automated-test-run/cli-mode.png" alt="CLI mode" />

Instead of selecting tests in the UI, you configure commands.

1. On the **Create Automated Test Run** screen → choose **Command Line Mode**.
2. Select repository.
3. Provide commands:
    - **Katalon Commands**: For Katalon Studio/KRE tests. Use [Command Builder](https://www.notion.so/katalon-studio/execute-tests/katalon-runtime-engine/get-started-with-katalon-runtime-engine) for syntax help.
    - **Generic Commands**: For non-Katalon frameworks (e.g., Pytest).
## Advanced Settings
After setting up your test run configurations, you can further customize how your tests behave through **Advanced Settings**. These options give you greater control over how tests are executed, including environment preferences, visual testing, and secure access to private or local applications.

<img src="https://tw-cdn.katalon.com/katalon-testops/Execution/automated-execution/advanced-settings-gen3.png" alt="Advanced settings section" width="1080" />

- **Visual Testing**: Helps your application’s **UI looks correct**, not just functions correctly.
    When enabled in a test run. Enable this when you need to catch **UI layout or design issues** across browsers, devices, and environments in addition to functional checks.
    - A **baseline screenshot collection** is created (first run).
    - Future runs **compare screenshots** against the baseline to detect visual changes.
    - Differences are flagged in TestOps, where you can **approve changes** (update baseline) or **reject them** (log as regressions).
    - For more information, please refer to the [Visual Testing document](/katalon-platform/analyze/analytics/visual-testing/visual-testing-overview#testops-visual-testing) for more information. 
- **Katalon Runtime Engine Version**: Choose the version to ensure compatibility.
- **Private/Local Testing**: To customize how your tests connect to private or local environments, switch the Private/Local Testing toggle on.

    To run with TestCloud Tunnel, select Private/Local Testing, then choose a specific tunnel to execute the test or use Auto-selected tunnel. With the auto-select option, TestCloud will use the most available tunnel, prioritizing private tunnels over shared tunnels. For more information, please refer to the [TestCloud document](/katalon-testcloud/local-testing-with-testcloud).

    In case your tests also perform API calls, check the Also Include API Calls option.

    Alternatively, you can opt for the TestCloud IPs Whitelisting option. This allows TestCloud to directly access your app without a tunnel connection.

## Execution Triggers: Run Now vs Schedule

When you finish setup, you decide how the run should start:

- **Run Now**
    - Immediately triggers execution.
    - Best for ad-hoc validation or smoke checks.
- **Schedule**
    - Delays or repeats the execution.
    - **Modes available**:
        - **One-time run**: pick a future date/time.
        - **Recurring run**: repeat by day, week, or custom cron schedule.
    - Best for regression, nightly runs, or aligning with sprint/release cadence.
<img src="https://tw-cdn.katalon.com/katalon-platform/automated-test-run/schedule-run.png" alt="Schedule Test Run" width="500"/>