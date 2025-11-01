---
title: Create an automated test run
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Create an automated test run

This document shows you how to create an automated test run.

## Prerequisites

- Make sure you have the Test Lead or Tester role. Go to [roles](/katalon-testops/administration-and-licensing/manage-systems/permissions/about-roles) or [permissions](/katalon-testops/administration-and-licensing/manage-systems/permissions/about-permissions) for more information or learn how to [assign a Project Admin here](/katalon-testops/administration-and-licensing/manage-administrators/assign-or-unassign-project-administrators).  

---

Create an automated test run by going to **Execution > + Create > Create Automated Test Run**.

1. Go to **Executions**. The Executions list appears by default.
2. Click on **+ Create**.
3. Click on **Create Automated Test Run**. The Create Automated Test Run page appears.

<br/>

<img src="https://tw-cdn.katalon.com/katalon-testops/Execution/Automated Executions/Create Automated Test Run March 26 2025.png" alt="Create an automated test run." width="1080"/>

<br/>

4. Input the following details:

* **Test Run Name:** The name of the test run
* **Creator:** This is set to the current user by default
* **Release Version (optional):** The associated release
* **Sprint (optional):** The associated sprint


5. Select test suites you want to run by clicking on **Select Test Suites**. A list of test suites appears; click **Save** when done.

    Alternatively, you can use **Command Line Mode**:
    - Select your repository.
    - Issue **Katalon Commands**: Execute tests with Katalon Studio. To generate a command, see: [Command Syntax](/katalon-studio/execute-tests/katalon-runtime-engine/command-line-syntax-in-katalon-runtime-engine) and [Command Builder](/katalon-studio/execute-tests/katalon-runtime-engine/get-started-with-katalon-runtime-engine#id_10).
    - Issue **Generic Commands**: Execute tests with other frameworks outside of Katalon Studio (e.g., Pytest).

<img src="https://tw-cdn.katalon.com/katalon-testops/Execution/Automated Executions/Enter Command Line Automated Test Run March 26 2025.png" alt="Select your repository." width="1080"/>

<br/>



6. Select the configurations you want to run by clicking on **Select Configurations**. A list of configurations appears.Click **Save** when done.

<br/>

<img src="https://tw-cdn.katalon.com/katalon-testops/Execution/Automated Executions/Select Configurations Automated Test Run March 26 2025.png" alt="Select configurations." width="1080"/>

<br/>

Choose between **Cloud Hosted** or **Self Hosted** configurations. 

7. Optionally, you can click on **Advanced Settings** to use [Visual Testing](/katalon-platform/analyze/analytics/visual-testing/visual-testing-overview#testops-visual-testing). 

<Tabs>

<TabItem value="Schedule an automated test run" label="Schedule" default>

### Schedule an automated test run

8. Click on **Schedule** to delay the test run to a later date or to create a recurring schedule for it.

<br/>
    
<img src="https://tw-cdn.katalon.com/katalon-testops/Execution/Automated Executions/Schedule Automated Test Run March 26 2025.png" alt="Schedule a manual test." width="1080"/>

<br/>

9. The Schedule Test Run dilaog box appears. Click **Schedule**. 

<br/>

### Result

A notification confirms that you have successfully scheduled an automated test run.
</TabItem>

<TabItem value="Instantly execute an automated test run" label="Run Now" default>

### Instantly execute an automated test run

8. Click on **Run Now** to instantly execute the automated test run.

<br/>
    
<img src="https://tw-cdn.katalon.com/katalon-testops/Execution/Automated Executions/Automated Test Run Running March 26 2025.png" alt="Instantly execute an automated test run." width="1080"/>
<p align="center"><em>An automated test run in progress.</em></p>

<br/>

:::note tip
- You can terminate a running execution by clicking on the **Terminate** button on the upper right corner of its overview page.
:::

<br/>

### Result

A notification confirms that you have successfully started an automated test run.

</TabItem>

</Tabs>
