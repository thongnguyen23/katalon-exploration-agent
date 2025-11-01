---
title: Create a manual test run
---
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

This shows you how to create a manual test run and either execute or schedule it.

## Prerequisites[](https://docs.katalon.com/katalon-testops/manage-executions/manual-executions/add-test-results-for-manual-executions#prerequisites)

- Make sure you have the Test Lead or Tester role. Go to [roles](https://docs.katalon.com/katalon-testops/administration-and-licensing/manage-systems/permissions/about-roles) or [permissions](https://docs.katalon.com/katalon-testops/administration-and-licensing/manage-systems/permissions/about-permissions) for more information or learn how to [assign a Project Admin here](https://docs.katalon.com/katalon-testops/administration-and-licensing/manage-administrators/assign-or-unassign-project-administrators).

---

Create a manual test run by going to **Execution > + Create > Create Manual Test Run**. A manual test run allows testers to execute test cases step-by-step manually, which is useful when automated testing is not feasible.

## Create a manual test run

1. Go to **Executions**. The Executions list appears by default.
2. Click on **+ Create**.
3. Click on **Create Manual Test Run**.

<br/>
    
<img src="https://tw-cdn.katalon.com/katalon-testops/Execution/Manual Executions/Create Manual Test Run March 29 2025.png" alt="Create a manual test run." width="1080"/>

<br/>
    
4. Input the following details:

* **Test Run Name:** The name of the test run
* **Executor:** This is set to the current user by default
* **Release Version:** The associated release
* **Sprint (optional):** The associated sprint
* **Test Suites:** The test suites to be included in the test run
* **Configurations:** The configurations to be used in the test run

<br/>
    
<img src="https://tw-cdn.katalon.com/katalon-testops/Execution/Manual Executions/Create Manual Test Case Page 2 March 29 2025.png" alt="Create a manual test run's set up." width="1080"/>

<!---
Note for internal users: The section below will be tabulated, which means both columns of content will show under different sections. For more information, see: 
https://docusaurus.io/docs/markdown-features/tabs --->

## Schedule or execute a manual test run

<Tabs>

<TabItem value="Schedule a manual test run" label="Schedule" default>

### Schedule a manual test run

1. Click on **Schedule** to delay the test run to a later date or to create a recurring schedule for it.

<br/>
    
<img src="https://tw-cdn.katalon.com/katalon-testops/Execution/Manual Executions/Schedule Test Run Dialog March 29 2025.png" alt="Schedule a manual test." width="1080"/>

<br/>

2. The Schedule Test Run dilaog box appears. Click **Schedule**. 

<br/>

### Result

A notification confirms that you have successfully scheduled a manual test run. 
</TabItem>

<TabItem value="Instantly execute a manual test run" label="Run Now" default>

### Instantly execute a manual test run

1. Click on **Run Now** to instantly execute the manual test run.
2. TestPak opens. Click on **Start** to begin the test run.

<br/>
    
<img src="https://tw-cdn.katalon.com/katalon-testops/Execution/Manual Executions/Manual Test Case Run Now 2 March 29 2025.png" alt="Click on Run Now to instantly execute the manual test run." width="1080"/>

<br/>

3. Input your test results. To learn how, see: [Add test results for manual executions](https://docs.katalon.com/katalon-testops/manage-executions/manual-executions/add-test-results-for-manual-executions).

</TabItem>

</Tabs>