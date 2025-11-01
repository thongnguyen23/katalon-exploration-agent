---
title: "Create a Github integration"
---

:::note note
This integration supports only **one-way synchronization** (from GitHub to TestOps).
:::

This document shows you how to create an integration for Github within Katalon TestOps.

To set up the integration, the **Account Admin** or **System Admin** must first connect a GitHub account or organization and link the desired projects (repository, branch, or directory) to TestOps. Go to [Roles](/katalon-testops/administration-and-licensing/manage-administrators/assign-or-unassign-account-administrators) or [Permissions](/katalon-testops/administration-and-licensing/manage-systems/permissions/about-permissions) for more information or learn how to [assign an Account Admin here](/katalon-testops/administration-and-licensing/manage-administrators/assign-or-unassign-account-administrators).


## Connect a Github account to TestOps

### Prerequisites

You must possess the **Account Admin** or **Project Admin** role to perform this action.

---

To set up the connection:
1. Navigate to **Admin > System > System Integrations > Create Integration**.

2. In the **Available Integration** list, choose **Github**.
<img src="https://tw-cdn.katalon.com/katalon-testops/integration/github/avail-integration-list.png" alt="Filling required fields screen" width="700"/>


3. Fill in the required fields to establish the connection.

<img src="https://tw-cdn.katalon.com/katalon-testops/integration/github/fill-in-field-system-level.png" alt="List of available integrations" width="800" height="400"/>

- In the **Personal Access Token (PAT)** field, enter your GitHub PAT. To generate a PAT, refer to this [GitHub documentation](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) on creating a personal access token.

    - Ensure you create a **classic PAT** and select the **repo** scope to set the appropriate permissions.
    
    <img src="https://tw-cdn.katalon.com/katalon-testops/integration/github/Github-Personal_access_token_permission.png" alt="Get Personal access token from github" width="500"/>
    

5. Click **Test Connection** to validate the integration.

### Result

To verify if the connection is active, navigate to **Admin > System > System Integrations**. Your GitHub integration will be listed under the **Integration list**.

<img src="https://tw-cdn.katalon.com/katalon-testops/integration/github/linked-git-connection.png" alt="List of linked integration list" width="700"/>

## Link a Github repository to TestOps
Once an **Account Admin** sets up the GitHub connection, only **Project Admin** can configure project-level settings by linking specific repositories, branches, or directories to Katalon TestOps:

1. Navigate to **Admin > System > System Integrations** .

2. Hover over the right edge of your linked connection and click the **Setting** icon.

    - For example: If you have connected a Git connection called **Katalon-Repo-Test**.

<img src="https://tw-cdn.katalon.com/katalon-testops/integration/github/connect-project-screen.png" alt="List of linked connection" width="700"/>

3. Fill in the required fields. In the URL field, navigate to the desired repository, branch, or directory from the linked GitHub account. Copy and paste the URL into the field for your project.

<img src="https://tw-cdn.katalon.com/katalon-testops/integration/github/fill-in-project-level.png" alt="Filling in required fields in System Integration UI" width="700"/>

4. Click Proceed.

    - If the status initially shows as **Inactive**, reload the page to update the status to **Active**.
    - If you modify the connection details and click **Save**, the status may remain **Inactive** until you reload the page.

5. [Optional] To edit an existing project, click the **Edit (pen)** icon, make the necessary changes, and click **Proceed**.

### Result

Your linked project is now active.

<img src="https://tw-cdn.katalon.com/katalon-testops/integration/github/result-project-link.png" alt="Linked project successfully" width="700"/>

## View synced test cases/test suites

To view your synced test cases/test suites, go to **Tests > Test Cases/Test Suites**.

<img src="https://tw-cdn.katalon.com/katalon-testops/integration/github/view-linked-tc.png" alt="View linked Test cases screen" width="700"/>
