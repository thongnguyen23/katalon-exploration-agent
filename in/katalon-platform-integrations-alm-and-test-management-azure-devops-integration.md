---
title: Azure DevOps integration
---

This document shows you how to set up an integration for Azure DevOps within Katalon TestOps.

## Connect an Azure account to TestOps

You must have the **Account Admin** or **System Admin** role to perform this action.

To set up the connection:  
1. Go to **Admin Settings**. (You can find Admin Settings in the upper right corner of the page.)  
2. Navigate to **System > Integrations**, then click **+ Create Integration**.

<img alt="Navigate to TestOps admin integration view" src="https://tw-cdn.katalon.com/katalon-platform/integration/admin-integrations.png" width="700" />

3. In the **Available Integration** list, choose **Azure DevOps**.

    ✅ A green check mark indicates that the integration is currently available.
    <img alt="Integration list" src="https://tw-cdn.katalon.com/katalon-platform/integration/integration-list.png" width="700" />

4. Fill in the required fields to establish the connection.  
    - **Integration Name**: A custom name for the integration (max 50 characters).  
    - **Organization Account URL**: The Azure DevOps workspace URL.  
        - Example: `https://dev.azure.com/your-workspace`  
        - Must start with `https://`  
    - **Personal Access Token (PAT)**: Enter your Azure PAT. To generate a PAT, refer to this [documentation](https://learn.microsoft.com/en-us/azure/devops/organizations/accounts/use-personal-access-tokens-to-authenticate?view=azure-devops&tabs=Windows). Please make sure the PAT has required permissions.
    <details> 
        <summary> ✅ **Azure DevOps Permissions Required for Katalon TestOps Integration** </summary>
        | **Integration Feature** | **Required Permissions** | **Notes** |
        | --- | --- | --- |
        | **Manual Sync** | `Read Project and Team`, `Read Work Items`, `Read Analytics` <br/> Access level: at least **Basic** | Required to fetch test and work item data. |
        | **Link Defect** | `Read Project and Team`, `Read Work Items` | Enables linking ADO work items to TestOps. |
        | **Create Defect** | `Read Project and Team`, `Read & write Work Items` | Needed to create new ADO work items (e.g., bugs) from TestOps. |
        | **Push Test Result** | `Read Project and Team`, `Read & write Test Management` | Enables pushing test execution data from TestOps to ADO. |
        | **Link Test Case to KS** | `Read Project and Team`, `Read & write Test Management` | Required to associate Katalon Studio test cases with ADO test cases. |
        | **Handle Webhook Events** | `Read Project and Team`, `Read Work Items`, `Read Analytics`<br/> Access level: at least **Basic** | Needed for syncing ADO events to TestOps. |
        | **Webhook Setup** | Member of the **Project Collection Administrators** group | Required only for configuring webhooks from ADO to TestOps. |        
    </details>
    - **Description (Optional)**: Brief description of the integration (max 255 characters).  

    🔁 Service Hooks will be automatically created at the project level for real-time syncing and automation.

<img src="https://tw-cdn.katalon.com/katalon-platform/integration/alm/azure-devops-account-fields.png" alt="Filling in required fields in System Integration UI" width="900"/>

5. Click **Test Connection** to validate the integration.  
6. Once validated, click **Save**, or click **Cancel** to exit without saving any changes.

#### Result

To verify if the connection is active, navigate to **Admin > System > Integrations**. Your Azure DevOps integration will be listed under the **Integration list**.  
- If the status initially shows as **Inactive**, reload the page to update the status to **Active**.  
- If the status shows **Error**, verify all required configuration fields, especially the Personal Access Token (PAT), and confirm it is valid and configured correctly in the account-level integration.

<img src="https://tw-cdn.katalon.com/katalon-platform/integration/alm/azure-devops-list-account.png" alt="List of linked integrations" width="900"/>

### Disconnect an Azure connection

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
<img src="https://tw-cdn.katalon.com/katalon-platform/integration/ado-reconnect.png" alt="ADO reconnect button" width="800"/>

2. A confirmation dialog will appear. Click **Reconnect** if you want to move forward.


## Configure Azure DevOps integration at Project level

:::caution requirements 
- You must have the **Project Admin** role to perform this action.
- You have connected an [Azure account at the Account-level](/katalon-platform/integrations/alm-and-test-management/azure-devops-integration#connect-an-azure-account-to-testops)
:::


1. Navigate to your **specific project's UI > Settings > Integrations**.
<img alt="Navigate to TestOps admin integration views" src="https://tw-cdn.katalon.com/katalon-platform/integration/project-integrations.png" width="700" />

2. Click the right edge of your **linked connection** and select **New configuration (Setting icon)**.

<img alt="Azure devops clicks on Settings" src="https://tw-cdn.katalon.com/katalon-platform/integration/alm/azure-devops-config.png" width="700" />

3. Fill in the required fields:
    #### Step 1: Select the Project and Team
    - **Project**: Select the ADO Project to link from the dropdown list. This defines which work items will be synced to Katalon TestOps. 
    - (Optional) Team: Select a team to link to enhance collaboration.
    - (Optional) Description: Brief description of the linked project (max 255 characters).  
    <br/>
    #### Step 2: Additional integration settings
    
    This section helps you customize synchronization between Katalon TestOps and Azure DevOps for streamlined traceability across test cases, requirements, and bugs.

    - Tick on **Pull Requirements (enable generation of test cases from requirements and links requirements with test cases for traceability)** to enable this feature.
    - Tick on **Bug Mapping (Pull bugs from ADO)** to enable this feature.

    :::warning notes
    Ticking on either feature will enable/disable the corresponding section in the next steps.
    :::

    <img src="https://tw-cdn.katalon.com/katalon-platform/integration/alm/azure-devops-project-fields-12.png" alt="Filling in required fields in System Integration UI" width="900"/> <br/>

    #### Step 3: Map Iteration Path to Release and Sprint
    :::caution info
    - This step is enable only if Pull Requirements and/or Bug Mapping is selected **(Step 2)**
    - By default, the Tiers refer to work item hierarchies, where Tier 1 is an Epic, Tier 2 is a Feature, Tier 3 is a User Story, and Tier 4 is a Task. This may vary depending on your project's configuration.
    :::
    This section allows you to choose the [iteration path](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/set-iteration-paths-sprints?view=azure-devops&tabs=browser) to map to a Release and Sprint in TestOps. Based on your selected project and mapped iteration paths, TestOps will generate release and sprints accordingly. Here, you can toggle the **Full path** option--the complete hierarchical path of an item--to ensure that resources and items are clearly and unambiguously identified.

    - Select the **Release/Sprint** from the dropdown list and the corresponding iteration path.

        Notes: To enable **For ADO - Team Board**, you must select a Team (in Step 1). 

    <img src="https://tw-cdn.katalon.com/katalon-testops/integration/Azure%20DevOps/ADO%20Full%20Path%20Annotated.png" alt="Filling in required fields in System Integration UI" width="900"/> <br/>

    #### Step 4: Common fields and Values Mapping
    This section allows you to map priority for effective issue prioritization and resource allocation, ensuring clear prioritization based on urgency (e.g., High, Medium, Low). Consistent mapping helps maintain workflow efficiency and prevents misalignment that could lead to inefficiencies.

    Map **ADO Priority** (levels 1 to 4) to your chosen **TestOps Priority** levels based on your workflow.
    
    <img src="https://tw-cdn.katalon.com/katalon-platform/integration/alm/azure-devops-field4.png" alt="Filling in required fields in System Integration UI" width="900"/> <br/>

    #### Step 5: Requirement Fields and Values Mapping
    :::caution info
    This step is enable only if **Pull Requirements** is selected (Step 2)
    :::
    This section allows you to select up to three date fields to set the Release Date, with the system using the first available date in your order of selection. You can also set an ADO State's equivalent TestOps Status.

    - **Release Date for Requirement** (Optional): Select three ADO fields as potential sources for the release date of a requirement. These fields are used **in a priority order (left to right)** to determine the release date:
        - Field 1 (e.g., Release End Date): This is the **highest priority** field. The system will first check if this date is available for the work item. If it is, this will be used as the release date.
        - Field 2 (e.g., Sprint End Date): If Field 1 is not available or empty, the system will fall back to this second-priority field to determine the release date.
        - Field 3 (e.g., Resolved Date): If both Field 1 and Field 2 are unavailable, the system will use this third-priority field as the release date.
    
    - Map **ADO State** to your chosen **TestOps Status**.
    
    - **Work Item Types**: Select Work Item Types to be synced.

    <br/> <img src="https://tw-cdn.katalon.com/katalon-platform/integration/alm/azure-devops-project-field-5.png" alt="Filling in required fields in System Integration UI" width="900"/> <br/>
    #### Step 6: Bug Fields and Values Mapping
    :::caution info
    This step is enable only if **Bug Mapping** is selected (Step 2)
    :::
    This section allows you to map the fields and values of bugs to the corresponding fields and values in Katalon TestOps.

    - Map **ADO Severity** levels to your chosen **TestOps Severity** levels based on your workflow.
    - Map **ADO State** to your chosen **TestOps Status**.

    <img src="https://tw-cdn.katalon.com/katalon-platform/integration/alm/ado-step6.png" alt="Filling in required fields in System Integration UI" width="900"/> <br/>


4. Click **Proceed** to sync data and finalize the connection.  
    - If the status initially shows as **Inactive**, reload the page to update the status to **Active**.  
    - If you modify the connection details and click **Save**, your changes will be saved, but the status may remain **Inactive**. To sync data and finalize the connection, click **Proceed**.

5. [Optional] To edit an existing linked Azure DevOps integration, click the **Edit (pen)** icon, make the necessary changes, and click **Proceed**. After editing, reload the page to ensure data is refreshed.

#### Result

Your Azure DevOps integration is now active within your project.  
<img src="https://tw-cdn.katalon.com/katalon-platform/integration/alm/azure-devops-linked-project.png" alt="Azure Devops linked project shows in UI" width="900"/> <br/>

## View release plans synced from linked Azure DevOps integration

To view release plans synced from linked Azure DevOps integration:

1. Navigate to your **specific project's UI > Plans**.
2. In the top-right **dropdown menu**, select the linked Azure DevOps integration.
3. Click the **Sync** button to fetch the latest data.

<img src="https://tw-cdn.katalon.com/katalon-platform/integration/alm/jra-result.png" alt="Jira linked in Plans module" width="1000"/>

## Archive a linked Azure DevOps integration

You must have the **Project Admin** role to perform this action.

:::info  
When an integration is archived:  
- The status changes to **Archived**.  
- The integration no longer appears in the **Plans** module.  
:::

To archive a linked Azure DevOps integration:  
1. Navigate to your **specific project's UI > Settings > Integrations**.
2. Click the right edge of your **linked connection** and select **Archive** icon.
![Archive Bitbucket project](https://tw-cdn.katalon.com/katalon-platform/integration/alm/azure-devops-archive.png)

3. A confirmation dialog will appear. Click **Archive** if you want to move forward.  
![Confirmed unarchive box](https://tw-cdn.katalon.com/katalon-platform/integration/alm/azure-devops-archive-confirm.png)

## Unarchive a linked Azure DevOps integration

You must have the **Project Admin** role to perform this action.

:::info  
After you unarchive an integration:  
- The status might appear as **Inactive**. Reload the page to update it to **Active**.  
- If the status shows **Error**, verify all required configuration fields and make necessary corrections.  
:::

To unarchive a linked Azure DevOps integration:  
1. Navigate to your **specific project's UI > Settings > Integrations**.
2. Click the right edge of your **linked connection** and select **Unarchive** icon.
![Showing unarchive icon in System Integration list](https://tw-cdn.katalon.com/katalon-platform/integration/alm/azure-devops-unarchive.png)

3. A confirmation dialog will appear. Click **Unarchive** if you want to move forward.  
![Confirmed unarchive box](https://tw-cdn.katalon.com/katalon-platform/integration/alm/azure-devops-unarchive-confirn.png)
