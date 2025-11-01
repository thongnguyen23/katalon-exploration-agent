---
title: Connect KRE Agent to your project
---

A Katalon Agent manages a local server to execute scheduled test runs in your local environment. Katalon TestOps provides compatible Agents for different execution environments. By installing an Agent on your test machine, you create a local test environment where you can run your tests.

There are two levels for managing KRE Agents in TestOps:
- Account level: the Account Admin/System Admin can create new agents, view agent list and details, and configure the maximum number of concurrent sessions.
- Project level: the Project Admin can view the list and details of agents, and connect agents to the project.

This guide shows you how-to connect KRE Agents to your project.

:::caution Prerequisites
- KRE Agents are created and set up in your Account. If not, refer to this guide: [Create and manage KRE Agents](/katalon-platform/administer/administration-and-licensing-alternate/manage-systems/configurations/create-and-manage-kre-agents).
- Make sure you have the Project Admin role. Refer to this document for more details: [Project level roles](/katalon-platform/administer/administration-and-licensing-alternate/about-administration#project-level-roles).
:::

## Set up connection
---

In [Katalon TestOps](https://platform.katalon.com/login), go to **Settings** > **TestCloud** and select the **KRE Agents** tab.

<img src="https://tw-cdn.katalon.com/katalon-testops/Administration and Licensing/Manage Systems/Configurations/manage-kre-agents/connect-agent-to-project.png" alt="Configure KRE Agent in Project level" width="1080" /><br/>

To view Agent details, click the name of the desired Agent. A pop-up window will open on the right side of the screen displaying the details.

Click the **Connected** - **Disconnected** toggle to set up connection for the agent and your project. Once connected, you can create automated test runs with this Agent. For instructions, refer to [Create automated test run](/katalon-platform/execute/automated-executions/create-an-automated-test-run).



