---
hide_title: true
title: Configure Azure DevOps Test Plans integration in Katalon Studio
---
import useBaseUrl from '@docusaurus/useBaseUrl';

# Configure Azure DevOps Test Plans integration in Katalon Studio 

Katalon Studio can natively integrate with the Azure Test Plans service of Azure DevOps (ADO). This integration helps you automatically submit test runs and results to ADO with release information (release stage and release ID), execution logs, reports, and images for analysis.

Before you proceed with the integration, below are key concepts you need to learn:

**What is a test point?**
A test point is a unique combination of a test case, test suite, configuration, and tester. Test cases by themselves are not executable. A test point is generated when you add a test case to a test suite. To learn more about test points, see the Microsoft document: <a href="https://docs.microsoft.com/en-us/azure/devops/test/new-test-plans-page?view=azure-devops#execute-tab" target="_blank">Execute tab</a>.
    
**What is a test configuration?**
A test configuration combines configuration variable values containing operating system information, browser, CPU type, database. For example, Windows 8 + 32-bit CPU or Windows 10 + 64-bit CPU. To learn more about the test configuration, see the Microsoft document: <a href="https://docs.microsoft.com/en-us/azure/devops/test/test-different-configurations?view=azure-devops" target="_blank">Test different configurations</a>.

## Requirements

Before you get started, ensure that you have the following requirements:

* An active Katalon Studio Enterprise license.
* Azure DevOps Server 2022 installed.
* A team collection set up.
* A Personal Access Token with full access permissions.

## Enable Azure DevOps Integration in Katalon Studio

To retrieve your test artifacts and create new test results directly on Azure DevOps, you need to integrate and authenticate your project with Azure Server first. 

Follow the steps to configure and authenticate your project with Azure Server in Katalon Studio:

1. In Katalon Studio, go to **Project > Settings > Integrations > Azure DevOps**.

2. In the dialog, check the **Enable Integration** box. The **Authentication** area can now be edited.
    1. Enter your credentials. Your credentials are encrypted by default.
    * Server URL:
        * For Azure DevOps Services (cloud): Use the format `https://dev.azure.com/{'{'}yourorganization{'}'}`.
        * For Azure DevOps Server 2022 (on-premises): Use the format `http(s)://{'{'}instance{'}'}/{'{'}collection{'}'}`.
        
          Examples:
            * `http://10.3.6.153/DefaultCollection/`
            * `https://10.3.6.153/DefaultCollection/`
            * `https://ec2amaz-q46tu5e/DefaultCollection/`
            
    * Personal Access Token: Your Personal Access Token. We recommend you create a Personal Access Token with full-access scopes. See Microsoft document: <a href="https://docs.microsoft.com/en-us/azure/devops/organizations/accounts/use-personal-access-tokens-to-authenticate?view=azure-devops&tabs=preview-page" target="_blank">Use personal access tokens</a> and <a href="https://docs.microsoft.com/en-us/azure/devops/integrate/get-started/authentication/oauth?view=azure-devops#scopes" target="_blank">Scopes</a>.

    3. Click **Connect**. If the connection to the Azure server is successful, the `Test Connection Succeeded` message appears:

        ![Test Connection Successful](https://tw-cdn.katalon.com/katalon-studio/integrations/test-management/azure-devops/ADO_Enable_integration.png)

2. After successfully authenticating your project with the Azure Server, navigate to the **Project** and **Test Plan** sections and select from the dropdown an ADO project and one or more test plans that you have access to.

    ![Select Project and Test Plan](https://tw-cdn.katalon.com/katalon-studio/integrations/test-management/azure-devops/ADO_Select_a_test_plan.png)
    
    To retrieve the latest projects list, click **Fetch Project**.

    ![Fetch Projects](https://tw-cdn.katalon.com/katalon-studio/integrations/test-management/azure-devops/ADO_Fetch_projects.png)

3. Navigate to the **Test Artifacts Mapping** and map test artifacts between Katalon Studio and ADO.
    1. In **Execution Status Mapping**, match test results in Katalon Studio with test outcomes in ADO.
    2. In **Test Configuration Mapping**, pair **Execution OS/Device**, **Execution Browser/App**, and **Execution Profile** in Katalon Studio with **Test Configuration in Azure DevOps**. This step is to map test cases with test points in ADO for result submission.

        ![Test Artifacts Mapping](https://tw-cdn.katalon.com/katalon-studio/integrations/test-management/azure-devops/KS_ADO_integration_Execution_Profile_Test_Config_Mapping.png)

        You can click **Add** or **Remove** to add or remove one or more items in each line item at your convenience.

4. Navigate to the **Submissions Options** section and configure the following:
    1. Select a test plan for the test run to be submitted. Name the test run. By default, the **Automatically submit test run** option is checked.

        <img src= "https://tw-cdn.katalon.com/katalon-studio/integrations/test-management/azure-devops/ADO_Auto_submit_test_run.png" alt="Automatically submit test run and name test run" width="400" />
    
    2. To add build and release information to test runs, enter the **Build Definition ID** or **Release Definition ID** (Release Definition ID was introduced in 8.1.0), then click **Verify** to confirm the value

        During runtime, Katalon Studio uses these pipeline definition IDs to get and pass the latest Build and Release to the corresponding properties of a test run.

        <img src= "https://tw-cdn.katalon.com/katalon-studio/integrations/test-management/azure-devops/Submission_options.png" alt="Submission options" width="500" />

    3. [Optional] Select **Include attachments when submitting test run** and decide what attachments to be sent together with a test run. You can select more than one:
        - **Applicable to**: Choose whether to include attachments **For all test executions** or **Only for test executions with failed test case(s)**. 
        - Attachment types: Check the boxes next to the attachment formats you want to receive, such as **Log file(s)**, **Screenshot(s)**, **HTML Report**, **PDF Report**, and **CSV Report**.

        <img src= "https://tw-cdn.katalon.com/katalon-studio/integrations/test-management/azure-devops/Include_attachments_formats.png" alt="Include attachments and select formats" width="300" />

    5. [Optional] With the associated test case ID and test configurations, more than one test point might be returned. These test points share the same test case ID and test configurations, but can still differ depending on the test suite and Tester. In this case, to decide whether Katalon Studio submits test results regardless of the number of test points returned, select **Submit test results for multiple test points with the same test case ID**.
    
        ![Select submission options](https://tw-cdn.katalon.com/katalon-studio/integrations/test-management/azure-devops/ADO-Select-submissions-options.png)
    
        > If multiple test configurations are assigned, multiple test points will be created. Select **Submit test results for multiple test points with the same test case ID** to send test results to Azure DevOps Server 2022.


    6. [Optional] Select **Override existing automation fields** if you want to override or update **Automated test name** and **Automated test storage fields** regardless of existing values.

        <img src= "https://tw-cdn.katalon.com/katalon-studio/integrations/test-management/azure-devops/Override_existing_automation_fields.png" alt="Select Override existing automation fields" width="400" />

5. To save your settings, click **Apply and Close**.

## Map test cases between Katalon Studio and Azure DevOps

To map test cases between Katalon Studio and Azure DevOps, do as follows:

1. In **Azure Test Plans**, open a test suite and note the test case IDs you want to map.

    ![View test case IDs in Azure Test Plans](https://tw-cdn.katalon.com/katalon-studio/integrations/test-management/azure-devops/ADO-View-TC-ID-in-Azure.png)
    
2. In Katalon Studio, open a test case and go to the **Integration** tab.
3. Enter one or more test case IDs of ADO. You can map a single test case ID in Katalon Studio to multiple ADO test cases by separating IDs with commas. 

    Example: ```12345, 67890```

    :::note
    Test cases can be retrieved from test plans you configured in **Project Settings** in Katalon Studio.
    :::

4. To check whether the test case IDs are valid, click **Verify**.

    ![Save your ADO test case](https://tw-cdn.katalon.com/katalon-studio/integrations/test-management/azure-devops/ADO-Verify-TC-ids.png)

5. Click **Save** to apply the mapping.

    :::note
    ADO test case IDs must belong to a test plan configured in **Project Settings** in Katalon Studio.
    :::

You can also dynamically assign test plan IDs, test run names, build IDs, and release definitions using command-line options when executing tests. See [Azure DevOps integration arguments](/katalon-studio/execute-tests/katalon-runtime-engine/command-line-syntax-in-katalon-runtime-engine#azure-devops-integration-arguments).

Once a mapped Katalon Studio test case is executed:
- A new test run is created in Azure DevOps.
- After test execution, Katalon Studio automatically updates Azure DevOps by creating a new test run and uploading results to the mapped test cases.

    ![ADO test results](https://tw-cdn.katalon.com/katalon-studio/integrations/test-management/azure-devops/ADO-Test-results.png)

- The Automation status in the **Steps** section is updated to `Automated`.

    ![Automation status in ADO Steps section](https://tw-cdn.katalon.com/katalon-studio/integrations/test-management/azure-devops/ADO_test_case_automation_status.png)

- As of Katalon Studio 10.3.1, the **Automated Test Name** (the name of the executed Katalon Studio test case) and the **Automated Test Storage** (the ID of the test case) fields in the **Associated Automation** section depend on whether the **Override existing automation fields** is enabled or disabled.

    ![Automation status in ADO Steps section](https://tw-cdn.katalon.com/katalon-studio/integrations/test-management/azure-devops/ADO_test_case_Associated_Automation.png)

    - If the **Override existing automation fields** is **enabled**, Katalon Studio fills in the fields when they are empty, and overwrites existing values with the latest executed test case details.
    - If the **Override existing automation fields** is **disabled**, Katalon Studio fills in the fields only when they are empty. Existing values are preserved and not overwritten.

## Troubleshooting

### Invalid or duplicate test case IDs are entered

When you enter a test case ID, you might encounter an invalid or duplicate test case ID error in the **Event Log**.

Azure DevOps enforces unique test case IDs across all test plans and suites, ensuring consistent identification and management of test cases throughout your projects. For more information, see the [following ADO documentation](https://learn.microsoft.com/en-us/azure/devops/test/copy-clone-test-items?view=azure-devops&tabs=browser).

To solve this issue, you can check the test case ID in question in the **Event Log**. To differentiate tests with similar objectives across different plans or releases, we recommend creating new test cases rather than reusing the same ID.

### Cannot create test results for Azure DevOps Test Case ID due to multiple Test Points returned

When you cannot upload test results to Azure DevOps, you might encounter the following error in the **Event Log**: `Cannot create test results for Azure DevOps Test Case ID=<test-case-ID> due to multiple Test Points returned.`

To solve this issue, you can check the IDs of the returned test points in the **Event Log** to readjust the test configuration, or allow sending test results anyway in project settings.

## Learn more with Katalon Academy

Go to the following course to learn how to integrate ADO with Katalon Studio: <a href="https://academy.katalon.com/courses/integrating-azure-devops/?utm_source=kat_docs&utm_medium=azure_devops_test_plans" target="_blank">Integrating Katalon Studio with Azure DevOps</a>.
