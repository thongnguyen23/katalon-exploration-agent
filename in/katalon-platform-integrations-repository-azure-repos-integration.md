---
title: "Azure Repos integration"
---

This document shows you how to set up an integration for Azure Repos within Katalon TestOps.

## Connect an Azure account to TestOps

You must have the **Account Admin** or **System Admin** role to perform this action.

To set up the connection:  
1. Go to **Admin Settings**. (You can find Admin Settings in the upper right corner of the page.)  
2. Navigate to **System > Integrations**, then click **+ Create Integration**.

<img alt="Navigate to TestOps admin integration view" src="https://tw-cdn.katalon.com/katalon-platform/integration/admin-integrations.png" width="700" />

3. In the **Available Integration** list, choose **Azure Repos**.

    ✅ A green check mark indicates that the integration is currently available.
    <img alt="Integration list" src="https://tw-cdn.katalon.com/katalon-platform/integration/integration-list.png" width="700" />


4. Fill in the required fields to establish the connection.  
    - **Integration Name**: A custom name for the integration (max 50 characters).  
    - **Organization Account URL**: The Azure Repos workspace URL that starts with `https://`.
        - Example: `https://dev.azure.com/your-workspace`  
    - **Personal Access Token**: Enter your Azure Repos PAT. To generate a PAT, refer to this [Azure Repos PAT documentation](https://learn.microsoft.com/en-us/azure/devops/organizations/accounts/use-personal-access-tokens-to-authenticate?view=azure-devops&tabs=Windows). Please make sure the PAT has required permissions.
    - **Description (Optional)**: Brief description of the integration (max 255 characters).  

    🔁 Service Hooks will be automatically created at the project level for real-time syncing and automation.

<img src="https://tw-cdn.katalon.com/katalon-platform/integration/repository/azure-repos-fields-account.png" alt="Azure Repos integration fields account level" width="900"/>

5. Click **Test Connection** to validate the integration.  
6. Once validated, click **Save**, or click **Cancel** to exit without saving any changes.

#### Result

To verify if the connection is active, navigate to **Admin > System > Integrations**. Your Azure Repos integration will be listed under the **Integration list**.  
- If the status initially shows as **Inactive**, reload the page to update the status to **Active**.  
- If the status shows **Error**, verify all required configuration fields, especially the Personal Access Token (PAT), and confirm it is valid and configured correctly in the account-level integration.

<img alt="Bitbucket clicks on Settings" src="https://tw-cdn.katalon.com/katalon-platform/integration/repository/bitbucket-list-admin.png" width="700" />

### Disconnect an Azure  connection
We only support disconnecting (not deleting) integrations to preserve data integrity, maintain audit history, and allow easy reactivation if needed.

For **any Azure connection**, modifying the connection will also update both **Azure DevOps and Azure Repos** if you have both configured.

:::info  When an integration is disconnected:  
- The status changes to **Inactive**.  
:::

1. Click **Disconnect** icon next to the connection you want to disconnect.
<img src="https://tw-cdn.katalon.com/katalon-platform/integration/git-disconnect-button.png" alt="Disconnect button" width="800"/>

2. A confirmation dialog will appear. Click **Disconnect** if you want to move forward.

### Reconnect an Azure connection

For **any Azure connection**, modifying the connection will also update both **Azure DevOps and Azure Repos** if you have both configured.

:::info After you re-connect an integration:  
- The status changes back to **Active**.  
- If the status shows **Error**, verify all required configuration fields and make necessary corrections.  
:::

1. Click **Reconnect** icon next to the connection you want to disconnect.
<img src="https://tw-cdn.katalon.com/katalon-platform/integration/azure-repos-reconnect.png" alt="Azure Repos reconnect button" width="800"/>

2. A confirmation dialog will appear. Click **Reconnect** if you want to move forward.

## Configure Azure Repos integration at Project level

:::caution requirements 
- You must have the **Project Admin** role to perform this action.
- You have connected an [Azure account at the Account-level](/katalon-platform/integrations/repository/azure-repos-integration#connect-an-azure-account-to-testops)
:::

1. Navigate to your **specific project's UI > Settings > Integrations**.

<img alt="Navigate to TestOps admin integration views" src="https://tw-cdn.katalon.com/katalon-platform/integration/project-integrations.png" width="700" />

2. Click the right edge of your **linked connection** and select **New configuration (Setting icon)**.

<img alt="Azure repos clicks on Settings" src="https://tw-cdn.katalon.com/katalon-platform/integration/repository/azure-repos-config.png" width="700" />

3. Fill in the required fields:  
- **Display Name**: A custom name for the linked project (max 50 characters).  
- **URL**: Navigate to the desired repository, branch, or directory from **the linked Azure Repos account**. 
    - For example: If you linked a connection under `https://dev.azure.com/katalon-test`, then the URL can point to a specific repository, branch, or directory. For instance:  
    `https://dev.azure.com/example-org/my-project/_git/my-repo?path=%2Ftests%2FTestCase&version=GBmain`  
- (Optional) Description: Brief description of the linked project (max 255 characters).  
- (Optional, but recommended) Select **Link existing test execution results with test cases having the exact same paths and names** to enable attaching existing test run results to test cases and suites with matching paths and names in TestOps.

<img src="https://tw-cdn.katalon.com/katalon-platform/integration/repository/bitbucket-fields-project.png" alt="Filling in required fields in System Integration UI" width="900"/>

4. Click **Proceed** to sync data and finalize the connection.  
    - If the status initially shows as **Inactive**, reload the page to update the status to **Active**.  
    - If you modify the connection details and click **Save**, your changes will be saved, but the status may remain **Inactive**. To sync data and finalize the connection, click **Proceed**.

5. [Optional] To edit an existing linked Azure Repos integration, click the **Edit (pen)** icon, make the necessary changes, and click **Proceed**. After editing, reload the page to ensure data is refreshed.

#### Result

Your Azure Repos is now active within your project.  
![Bitbucket linked projects](https://tw-cdn.katalon.com/katalon-platform/integration/repository/azure-repos-linked-project.png)

## View test cases or test suites synced from linked Azure Repos integration

To view test cases or test suites synced from the linked Azure Repos integration, navigate to **Tests > Test Cases/Test Suites**.

![Azure Devops linked in Tests folder](https://tw-cdn.katalon.com/katalon-platform/integration/repository/azure-repos-linked-tests.png)

## Archive a linked Azure Repos integration

You must have the **Project Admin** role to perform this action.

:::info  
When an integration is archived:  
- The status changes to **Archived**.  
- The integration no longer appears in the **Test Cases/Test Suites** module.  
- Any scheduled test runs in the **Execution** module will be automatically canceled at runtime.  
:::

To archive a linked Azure Repos integration:  
1. Navigate to your **specific project's UI > Settings > Integrations**.
2. Click the right edge of your **linked connection** and select **Archive** icon.
![Archive Bitbucket project](https://tw-cdn.katalon.com/katalon-platform/integration/repository/azure-repos-archive.png)

3. A confirmation dialog will appear. Click **Archive** if you want to move forward.  
![Confirmed unarchive box](https://tw-cdn.katalon.com/katalon-platform/integration/repository/azure-repos-archive-confirm.png)

## Unarchive a linked Azure Repos integration

You must have the **Project Admin** role to perform this action.

:::info  
After you unarchive an integration:  
- The status might appear as **Inactive**. Reload the page to update it to **Active**.  
- If the status shows **Error**, verify all required configuration fields and make necessary corrections.  
:::

To unarchive a linked Azure Repos integration:  
1. Navigate to your **specific project's UI > Settings > Integrations**.
2. Click the right edge of your **linked connection** and select **Unarchive** icon.
![Showing unarchive icon in System Integration list](https://tw-cdn.katalon.com/katalon-platform/integration/repository/azure-repos-unarchive.png)

3. A confirmation dialog will appear. Click **Unarchive** if you want to move forward.  
![Confirmed unarchive box](https://tw-cdn.katalon.com/katalon-platform/integration/repository/azure-repos-unarchive-confirm.png)
