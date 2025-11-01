---
title: Create a local test environment with an Agent (Legacy)
---
import useBaseUrl from '@docusaurus/useBaseUrl';
import Reusable from '@site/src/reusable/Reusable.mdx';

<Reusable />
This shows you how you can create and manage a local test environment with an Agent using Windows or Mac.

A Katalon Agent manages a local server for executing the scheduled test runs in a local test environment. Katalon TestOps supports compatible Agents for different executing environments.When you install the Agent in your local test machine, you have created a local test environment where you can run or execute your tests.

## Prerequisites

- You have a verified Katalon account.
- You have installed [Git SCM](https://git-scm.com/downloads).
<!-- Add permissions prerequisite when confirmed -->

---

## Download and Install an Agent from Katalon TestOps

1. Sign in to [Katalon TestOps](https://testops.katalon.io/login).

2. Go to **TestOps Settings > Organization Setup**.

    <img src="https://tw-cdn.katalon.com/katalon-testops/Execution/Local Test Environments/Local Agent Step 2.png" alt="Set up a local agent in Katalon TestOps" width="500"/>

    <br/>

    This shows the **Test Environments** page. It also lists the agents you have.

    <img src="https://tw-cdn.katalon.com/katalon-testops/Execution/Local Test Environments/Local Agent Step 2a.png" alt="The Test Environments page" width="1080"/>

<br/>

3. Click on **Create Local Test Environment**. Alternatively you can click on **Agent Setup** to go to the same page.
   
   This shows the **Agent Setup** page.

    <img src="https://tw-cdn.katalon.com/katalon-testops/Execution/Local Test Environments/Local Agent Step 3.png" alt="The Agent Setup page" width="1080"/>

    <br/>

4. In **Select OS**, choose your operating system (Windows, macOS, etc.), then click **Download Agent**.
   
   - You have downloaded the Agent file (.zip file) to your computer. Unzip it and keep it open for now.

5. In the **Agent Name** section, create a name for the Agent (e.g., **My Agent**).

6. In the **Katalon API Key** section, select default or create your own.

7. Open any command line interface and navigate to the directory containing the Agent executable file.

8. Go back to the Agent Setup page and copy and paste the command labeled **Bash** to your command line interface. Hit Enter or Return.

9. Use the next command labeled **Bash** to start the agent. Hit Enter or Return.

10. After the agent successfully starts, assign your agent to a project. To learn how, see: [Manage the Agent status](#manage-the-agent-status).

---

### Set up an Agent in a Windows local machine

To set up an Agent in a Windows local machine, do as follows:

1. Unzip the Agent file you have downloaded.

   <img src="https://tw-cdn.katalon.com/katalon-testops/Execution/Local Test Environments/Windows Local Agent Step 1.png" alt="Unzip the Agent file within Windows" width="1080"/>

   <br/>

2. Open your command line interface and navigate to the directory containing the Agent executable file.

    <img src="https://tw-cdn.katalon.com/katalon-testops/Execution/Local Test Environments/Windows Local Agent Step 2.png" alt="The command line interface within Windows" width="700"/>

   <br/>
   

3. Copy the command in the **Generate configuration** section on the **Agent Setup** page, and then paste it into the command window. Hit *Enter* to run the command.
   
   <img src="https://tw-cdn.katalon.com/katalon-testops/Execution/Local Test Environments/Windows Local Agent Step 3.png" alt="The command line interface within Windows" width="700"/>

   <br/>

4. Copy the command in the **Start an agent** section, and paste it into the command window. Hit *Enter* to run the command.

   <img src="https://tw-cdn.katalon.com/katalon-testops/Execution/Local Test Environments/Windows Local Agent Step 4.png" alt="The command line interface within Windows" width="700"/>

   <br/>

### Results

You have successfully set up your Agent on Windows. The next step is to view or manage your Agent's linked Projects. See: [Manage the Agent status](#manage-the-agent-status).

---

### Set up an Agent in a macOS local machine

1. Unzip the Agent file you have downloaded.

2. Right-click on the Agent file and select **New Terminal at Folder**.

<img src="https://tw-cdn.katalon.com/katalon-testops/Execution/Local Test Environments/MacOS Local Agent Step 2.png" alt="The command line interface within Mac" width="700"/>

<br/>

3. Copy the command in the **Generate configuration** section on the **Agent Setup** page, and paste it into the Terminal. Hit *Return* on the keyboard to run the command.
   
    Make sure you have **enabled Terminal for Developer Tools** in the Security & Privacy settings of your macOS.

<img src="https://tw-cdn.katalon.com/katalon-testops/Execution/Local Test Environments/MacOS Local Agent Step 3.png" alt="The command line interface within Mac" width="700"/>

<br/>

4. Copy the command in the **Start an agent** section, and paste it into the Terminal. Hit *Return* to run the command.

<img src="https://tw-cdn.katalon.com/katalon-testops/Execution/Local Test Environments/MacOS Local Agent Step 4.png" alt="The command line interface within Mac" width="700"/>

<br/>

### Results

You have successfully set up your Agent on Mac. The next step is to view or manage your Agent's linked Projects. See: [Manage the Agent status](#manage-the-agent-status).

---

## Manage the Agent status

1. Log in to [TestOps](https://testops.katalon.io/login) and go to **Settings > Organization Setup > Test Environments**.

2. Click on the **Name** of your Agent to navigate to its **Agent Details** page. In the example below, "My Agent" is the name of the Agent.

    <img src="https://tw-cdn.katalon.com/katalon-testops/Execution/Local Test Environments/Manage Agent Status Step 2.png" alt="Manage the agent status in TestOps" width="500"/>

    <br/>

   The **Agent Details** page shows.
   
   <img src="https://tw-cdn.katalon.com/katalon-testops/Execution/Local Test Environments/Manage Agent Status Step 2a.png" alt="The command line interface within Windows" width="1080"/>

    <br/>

## Link or un-link a Project to an Agent

3. Navigate down to the **Linked Projects** section and click on the dropdown menu to assign projects you would like to link this agent to. Once they are linked, you will see them as tags. In the example below, the projects "First Project" and "Second Project" are shown as tags below the dropdown menu.

   <img src="https://tw-cdn.katalon.com/katalon-testops/Execution/Local Test Environments/Link Project to Agent Step 1.png" alt="Link Agent to Project" width="1080"/>

4. To remove a linked project, click on the **x** next to the project name. This action deletes the project tag, which means that the project is now un-linked.
   
:::note
- You can link your projects back any time.
:::

### Results
You have linked your agent to a project. Now you can [Schedule test runs](/katalon-platform/execute/test-execution-with-testops/schedule-test-runs-in-testops).

---

## Agent Authentication

Agents use `serverurl` and `apikey` in *agentconfig* to:
- Activate Katalon Runtime Engine.
- Send test results to Katalon TestOps.

To locate the `serverurl` and `apikey` of your agent, navigate to the **Generate configuration** section on the **Agent Setup** page, as shown in the example below.

   <img src="https://tw-cdn.katalon.com/katalon-testops/Execution/Local Test Environments/Agent Authentication.png" alt="Agent Authentication" width="1080"/>

   <br/>

---

## Configure proxy for Agents

You can set up proxy for the Agent in the *agentconfig* file, using the `proxy` option. For example, `proxy=http://localhost:8080`.

---

## Next steps

- [Schedule Test Runs](/katalon-platform/execute/test-execution-with-testops/schedule-test-runs-in-testops).
