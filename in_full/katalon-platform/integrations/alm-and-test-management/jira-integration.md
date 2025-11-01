---
title: Jira integration
---

This document shows you how to set up an integration for Jira within Katalon TestOps.

## Connect a Jira account to TestOps

You must have the **Account Admin** or **System Admin** role to perform this action.

To set up the connection:  
1. Go to **Admin Settings**. (You can find Admin Settings in the upper right corner of the page.)  
2. Navigate to **System > Integrations**, then click **+ Create Integration**.

<img alt="Navigate to TestOps admin integration view" src="https://tw-cdn.katalon.com/katalon-platform/integration/admin-integrations.png" width="700" />

3. In the **Available Integration** list, choose **Jira**.

    ✅ A green check mark indicates that the integration is currently available.
    <img alt="Integration list" src="https://tw-cdn.katalon.com/katalon-platform/integration/integration-list.png" width="800" />

4. Fill in the required fields to establish the connection.  
    - **Integration Name**: A custom name for the integration (max 50 characters).  
    - **Organization URL**: The Jira Organization URL.  
        - Example: `https://katalon-product-demo.atlassian.net`  
        - Must start with `https://`  
    - **Personal Access Token (PAT)**: Enter your Jira PAT. To generate a PAT, refer to this [documentation](https://confluence.atlassian.com/enterprise/using-personal-access-tokens-1026032365.html). Please make sure the PAT has required permissions.
    <details> 
        <summary> ✅ **Jira Permissions Required for Katalon TestOps Integration** </summary>
        | **Integration Feature** | **Required Permission(s)** | **Notes** |
        | --- | --- | --- |
        | **Manual Sync** | `Browse Projects` | Allows TestOps to retrieve project data from Jira. |
        | **Link Defects** | `Browse Projects` | Enables linking Jira issues to TestOps test cases. |
        | **Create Defects** | `Browse Projects`, `Create Issues` | Additional permissions may be required depending on Jira field configurations (see below). |
        |  | *Optional:* `Assign Issues`, `Modify Reporter`, `Link Issues`, `Resolve Issues`, `Schedule Issues` | These become **required** if the corresponding fields (`Assignee`, `Reporter`, `Issue Links`, `Fix Versions`, `Due Date`) are marked as **required** in Jira. |
        | **Handle Webhook Events** | `Browse Projects` | Needed to associate Jira events with TestOps updates. |
        | **Webhook Setup** | `Administer Jira` (global permission) | Required only when configuring webhooks from Jira to TestOps. |
    </details>
    - **Description (Optional)**: Brief description of the integration (max 255 characters).  

    🔁 Service Hooks will be automatically created at the project level for real-time syncing and automation.

<img src="https://tw-cdn.katalon.com/katalon-platform/integration/alm/jira-fields-account.png" alt="Filling in required fields in System Integration UI" width="900"/>

5. Click **Test Connection** to validate the integration.  
6. Once validated, click **Save**, or click **Cancel** to exit without saving any changes.

#### Result

To verify if the connection is active, navigate to **Admin > System > Integrations**. Your Jira integration will be listed under the **Integration list**.  
- If the status initially shows as **Inactive**, reload the page to update the status to **Active**.  
- If the status shows **Error**, verify all required configuration fields, especially the Personal Access Token (PAT), and confirm it is valid and configured correctly in the account-level integration.

<img src="https://tw-cdn.katalon.com/katalon-platform/integration/alm/azure-devops-list-account.png" alt="List of linked integrations" width="900"/>

### Disconnect a Jira connection

We only support disconnecting (not deleting) integrations to preserve data integrity, maintain audit history, and allow easy reactivation if needed.

:::info  When an integration is disconnected:  
- The status changes to **Inactive**.  
:::

1. Click **Disconnect** icon next to the connection you want to disconnect.
<img src="https://tw-cdn.katalon.com/katalon-platform/integration/git-disconnect-button.png" alt="Disconnect button" width="800"/>

2. A confirmation dialog will appear. Click **Disconnect** if you want to move forward.

### Reconnect a Jira connection
:::info After you re-connect an integration:  
- The status changes back to **Active**.  
- If the status shows **Error**, verify all required configuration fields and make necessary corrections.  
:::

1. Click **Reconnect** icon next to the connection you want to disconnect.
<img src="https://tw-cdn.katalon.com/katalon-platform/integration/jira-reconnect.png" alt="Jira reconnect button" width="800"/>

2. A confirmation dialog will appear. Click **Reconnect** if you want to move forward.
## Configure Jira integration at Project level

:::caution requirements 
- You must have the **Project Admin** role to perform this action.
- You have connected a [Jira account at the Account-level](/katalon-platform/integrations/alm-and-test-management/jira-integration#connect-a-jira-account-to-testops)
:::

1. Navigate to your **specific project's UI > Settings > Integrations**.
<img alt="Navigate to TestOps admin integration views" src="https://tw-cdn.katalon.com/katalon-platform/integration/project-integrations.png" width="700" />

2. Click the right edge of your **linked connection** and select **New configuration (Setting icon)**.

<img alt="Jira clicks on Settings" src="https://tw-cdn.katalon.com/katalon-platform/integration/alm/jira-project-list.png" width="700" />

3. Fill in the required fields:
    #### Step 1: Select the Project and Board
    - **Project**: Select the Jira Project to link from the dropdown list. This defines which work items will be synced to Katalon TestOps. 
    - (Optional) **Board**: Select a board to link to enhance collaboration.
    - (Optional) Description: Brief description of the linked project (max 255 characters).  
    <br/>
    #### Step 2: Additional integration settings
    This section helps you customize synchronization between Katalon TestOps and Jira for streamlined traceability across test cases, requirements, and bugs.

    - Tick on **Pull Requirements (enable generation of test cases from requirements and links requirements with test cases for traceability)** to enable this feature.
    - Tick on **Bug Mapping (Pull bugs from Jira)** to enable this feature.
    <br/>
    :::warning notes
    Ticking on either feature will enable/disable the corresponding section in the next steps.
    :::

    <img src="https://tw-cdn.katalon.com/katalon-platform/integration/alm/jira-step12.png" alt="Filling in required fields in System Integration UI" width="900"/> <br/>

    #### Step 3: Release and Sprint Mapping
    :::caution note
    This step is enable only if **Pull Requirements and/or Bug Mapping is selected** (Step 2)
    :::
    In this step, you define how Release and Sprint data will be mapped from your Jira project.

    Note: **Sprint** will be disable if no board is selected (Step 1). 
    <img src="https://tw-cdn.katalon.com/katalon-platform/integration/alm/jira-step3.png" alt="Filling in required fields in System Integration UI" width="900"/> <br/>

    #### Step 4: Common Fields and Values Mapping
    :::caution notes
    This step is enable only if **Pull Requirements and/or Bug Mapping is selected** (Step 2)
    :::
    This section allows you to map priority for effective issue prioritization and resource allocation, ensuring clear prioritization based on urgency (e.g., High, Medium, Low). Consistent mapping helps maintain workflow efficiency and prevents misalignment that could lead to inefficiencies.

    Map **Jira Priority** levels your chosen **TestOps Priority** levels based on your workflow.
    
    <img src="https://tw-cdn.katalon.com/katalon-platform/integration/alm/jira-step-4.png" alt="Filling in required fields in System Integration UI" width="900"/> <br/>

    #### Step 5: Requirement Fields and Value Mapping
    :::caution notes
    This step is enable only if **Pull Requirements and/or Bug Mapping is selected** (Step 2)
    :::
    This section allows you to select up to three date fields to set the Release Date, with the system using the first available date in your order of selection. You can also set an Jira State's equivalent TestOps Status.

    - **Release Date for Requirement** (Optional): Select three Jira fields as potential sources for the release date of a requirement. These fields are used **in a priority order (left to right)** to determine the release date:
        - Field 1 (e.g., Fix Version Date): This is the **highest priority** field. The system will first check if this date is available for the work item. If it is, this will be used as the release date.
        - Field 2 (e.g., Sprint End Date): If Field 1 is not available or empty, the system will fall back to this second-priority field to determine the release date.
        - Field 3 (e.g., Resolved Date): If both Field 1 and Field 2 are unavailable, the system will use this third-priority field as the release date.
    - Map **Jira Status** to your chosen **TestOps State**

    - **Work Item Types**: Select Jira Work Item Types to be synced.

    <img src="https://tw-cdn.katalon.com/katalon-platform/integration/alm/jira-step5.png" alt="Filling in required fields in System Integration UI" width="900"/> <br/>
    #### Step 6: Bug Fields and Values Mapping
    :::caution notes
    This step is enable only if **Pull Requirements and/or Bug Mapping is selected** (Step 2)
    :::
    This section allows you to map the fields and values of bugs to the corresponding fields and values in Katalon TestOps.

    - Map **Jira Severity** levels to your chosen **TestOps Severity** levels based on your workflow.
    
    - Map **Jira Status** levels to your chosen **TestOps Status**. 

    - Select either **Jira Resolution** or **Jira Status** to your chosen TestOps Status.

    <img src="https://tw-cdn.katalon.com/katalon-platform/integration/alm/jira-step6.png" alt="Filling in required fields in System Integration UI" width="900"/> <br/>


4. Click **Proceed** to sync data and finalize the connection.  
    - If the status initially shows as **Inactive**, reload the page to update the status to **Active**.  
    - If you modify the connection details and click **Save**, your changes will be saved, but the status may remain **Inactive**. To sync data and finalize the connection, click **Proceed**.

5. [Optional] To edit an existing linked Jira integration, click the **Edit (pen)** icon, make the necessary changes, and click **Proceed**. After editing, reload the page to ensure data is refreshed.

#### Result

Your Jira integration is now active within your project.  
<img src="https://tw-cdn.katalon.com/katalon-platform/integration/alm/jira-project-linked.png" alt="Jira linked project shows in UI" width="900"/> <br/>

## View release plans synced from linked Jira Integration

To view release plans synced from linked Jira integration:

1. Navigate to your **specific project's UI > Plans**.
2. In the top-right **dropdown menu**, select the linked Jira integration.
3. Click the **Sync** button to fetch the latest data.

<img src="https://tw-cdn.katalon.com/katalon-platform/integration/alm/jra-result.png" alt="Jira linked in Plans module" width="1000"/>

## Archive a linked Jira integration

You must have the **Project Admin** role to perform this action.

:::info  
When an integration is archived:  
- The status changes to **Archived**.  
- The integration no longer appears in the **Plans** module.  
:::

To archive a linked Jira integration:  
1. Navigate to your **specific project's UI > Settings > Integrations**.
2. Hover over the right edge of your linked repository and click the **Archive** icon.  
![Archive Bitbucket project](https://tw-cdn.katalon.com/katalon-platform/integration/alm/jira-archive.png)

3. A confirmation dialog will appear. Click **Archive** if you want to move forward.  
![Confirmed unarchive box](https://tw-cdn.katalon.com/katalon-platform/integration/alm/jira-archive-confirm.png)

## Unarchive a linked Jira integration

You must have the **Project Admin** role to perform this action.

:::info  
After you unarchive an integration:  
- The status might appear as **Inactive**. Reload the page to update it to **Active**.  
- If the status shows **Error**, verify all required configuration fields and make necessary corrections.  
:::

To unarchive a linked Jira integration:  
1. Navigate to your **specific project's UI > Settings > Integrations**.
2. Hover over the right edge of your linked repository and click the **Unarchive** icon.  
![Showing unarchive icon in System Integration list](https://tw-cdn.katalon.com/katalon-platform/integration/alm/jira-unarchive.png)

3. A confirmation dialog will appear. Click **Unarchive** if you want to move forward.  
![Confirmed unarchive box](https://tw-cdn.katalon.com/katalon-platform/integration/alm/jira-unarchive-confirm.png)

## Related topics
- [View your Jira-synced Release timeline within TestOps](/katalon-platform/plan/about-the-sprint-release-timeline)

- [View your Jira-synced Requirements or its details](/katalon-platform/plan/about-the-sprint-release-timeline#view-requirement-details)

- [Learn about linkages to link requirements or test cases](/katalon-platform/create-tests/create-new-test-cases#edit-linkages)

- [Generate test cases with AI](/katalon-platform/create-tests/generate-test-cases-with-ai)

