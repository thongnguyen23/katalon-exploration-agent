---
title: Create and manage KRE Agents
---

A Katalon Agent manages a local server for executing the scheduled test runs in a local test environment. Katalon TestOps supports compatible Agents for different executing environments. When you install the Agent in your local test machine, you have created a local test environment where you can run or execute your tests.

There are two sections to manage KRE agents:
- Account level: the Account Admin/System Admin can create new agents, view agent list and details of each agent, and configure max concurrent sessions.
- Project level: the Project Admin view the list and details of agents, and connect agents to the project.

This guide shows you how-to set up KRE Agents in your Account.


:::caution Prerequisites
- Make sure you are an Account Admin or System Admin. Go to [roles](/katalon-testops/administration-and-licensing/manage-systems/permissions/about-roles) or [permissions](/katalon-testops/administration-and-licensing/manage-systems/permissions/about-permissions) for more information or learn how to [assign an Account Admin here](/katalon-testops/administration-and-licensing/manage-administrators/assign-or-unassign-account-administrators).
:::

## Set up KRE Agents
---

1. In [Katalon TestOps](https://platform.katalon.com/login), go to **Admin Settings** > **System Configuration** > **TestCloud** and select the **KRE Agents** tab.
   <img src="https://tw-cdn.katalon.com/katalon-testops/Administration and Licensing/Manage Systems/Configurations/manage-kre-agents/kre-agents-in-system-config-gen3.png" alt="Configure KRE Agent in Account level" width="800" />
    
2. In the upper right corner, select **Learn how to set up an Agent** to open the set up dialog with instructions.
   <img src="https://tw-cdn.katalon.com/katalon-testops/Administration and Licensing/Manage Systems/Configurations/manage-kre-agents/setup-kre-agent-guide.png" alt="Setup KRE Agent guide" width="400" />
 
    1. **Select OS**: choose your operating system, then click **Download Agent**.
       - The `.zip` Agent file is downloaded to your computer. Unzip it and keep it open for now.
    2. **Agent Name**: provide a name for the Agent (e.g., **BankingCore360**).
    3. **Katalon API Key**: select an existing key or create your own.
    4. Open any command line interface and navigate to the directory containing the Agent executable file.
    5. Run the **Bash** commands in your command line interface (CLI). The commands will generate the configuration and start the Agent.
    6. After the agent starts successfully, click the settings icon (⚙️) to configure its maximum concurrent sessions. 
   
To setup automated test runs, proceed to [Connect the KRE Agent to your project](/katalon-platform/administer/administration-and-licensing-alternate/manage-projects/connect-kre-agent-to-your-project).