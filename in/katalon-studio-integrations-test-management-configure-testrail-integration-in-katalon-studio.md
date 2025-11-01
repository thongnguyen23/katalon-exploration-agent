---
hide_title: true
title: Configure TestRail integration in Katalon Studio
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# Configure TestRail integration in Katalon Studio 

The **TestRail Integration** plugin establishes the connection between Katalon Studio and TestRail to deliver the following advanced capabilities:

- In TestRail, you can view test results of test suites executed in Katalon Studio.
- In Katalon Studio, you can query test cases associated with test runs of TestRail in the dynamic test suite.

:::note Notes
- From version 8.5.5, your TestRail password is encrypted. If you open your project in Katalon Studio version before 8.5.5, you might need to re-en ter your TestRail password.
- The TestRail Integration plugin only supports integrating Katalon Studio with TestRail Cloud.
:::

This tutorial shows you how to configure TestRail integration.

## Requirements
- An active Katalon Studio Enterprise license.
- The TestRail Integration plugin installed. You can find the latest version of the TestRail plugin (version 1.1.4) here: [TestRail Integration plugin](https://store.katalon.com/product/13/TestRail-Integration).

## Enable TestRail integration in Katalon Studio

To enable the integration of Katalon Studio with TestRail, you need to configure both your TestRail site and Katalon Studio, do as follows:

1. Enable the TestRail API. 

    Log in to your account, go to **Administration > Site Settings > API**, and check the **Enable API** option. Then click **Save Settings**.

    <img className="image" src={useBaseUrl("/91d45c10-22b2-11ed-9930-0242fe3e4a3f/KS-enable-API-in-Testrail.png")} alt="Enable API in TestRail" />

2. Enable the TestRail Integration plugin. 

    1. In Katalon Studio, go to the main menu, select **Project > Settings > Plugins > TestRail** and check the Enable TestRail option.
    2. Enter the credentials required for Authentication:
        - **URL**: Your TestRail instance. For example, `https://<example>.testrail.io`.
        - **Username**: Your TestRail username.
        - **Password**: Your TestRail password.
        - **Project**: your TestRail project ID (an integer). To get the project ID, open your TestRail project in the browser and view the ID at the end of the URL.

        For example, for the project with the URL `https://company.testrail.io/index.php?/projects/overview/1`, the project ID here is 1.

    3. Click **Test Connection** to verify your TestRail account.

        <img src="https://tw-cdn.katalon.com/katalon-studio/integrations/test-management/testrail/Enter_TestRail_credentials.png" alt="Enter your TestRail credentials" width="700" />

    4. Click **Appy and Close**.
    
You have successfully enabled TestRail integration in Katalon Studio.

## Map test cases between Katalon Studio and TestRail

To map a test case between Katalon Studio and TestRail, you need to get the TestRail test case ID. Do as follows:

1. To retrieve the TestRail test case ID, open your project in TestRail, then go to the **Test Cases** tab.
Here you can see the list of test cases and their IDs.

<img className="image" width={850} src={useBaseUrl("/91d19cf0-22b2-11ed-9930-0242fe3e4a3f/KS-Test-Case-list-Testrail.png")} alt="TestRail test case list" /> 

2. In Katalon Studio, open the test case you want to map, switch to the **Integration** tab, and specify the respective test case ID in TestRail (only the integer part).

<img className="image" width={850} src={useBaseUrl("/91d06470-22b2-11ed-9930-0242fe3e4a3f/KS-TestRail-Integration-tab-in-Studio.png")} alt="specify the respective test case ID in TestRail" /> 

    :::note
    Katalon Studio version 10.3.1 now supports multiple TestRail case IDs for mapping. Ensure that you separate each ID by a comma or semicolon.

    <img src= "https://tw-cdn.katalon.com/katalon-studio/integrations/test-management/testrail/Support_multiple_TestRail_IDs.png" alt="Support multiple TestRail IDs for mapping" width="600" />
    :::

3. Save the Katalon Studio test cases.

You have successfully map test cases between Katalon Studio and TestRail.

For more information, see [Upload test execution results from Katalon Studio to TestRail](/katalon-studio/integrations/test-analysis/upload-test-execution-results-from-katalon-studio-to-testrail).

## Map TestRail custom required field to Katalon Studio

:::note Requirements
- Make sure you are using Katalon Studio Enterprise version 10.2.3 and later.
- Install the latest TestRail Integration plugin (version 1.1.4). Download it here: [TestRail Integration plugin](https://store.katalon.com/product/13/TestRail-Integration).
- Ensure that you have enabled the API option on the TestRail server. See Step 1 of [Enable TestRail integration in Katalon Studio](#enable-testrail-integration-in-katalon-studio).
:::

If you configure a required custom field in TestRail and use Katalon Studio to upload test results, you may encounter issues when executing a test suite and pushing results to TestRail. To prevent this, make sure the custom field is correctly mapped in Katalon Studio Project Settings under the TestRail configuration section.

1. In TestRail, create your custom field. For more information about creating custom fields in TestRail, see the following software documentation: [Configuring custom fields](https://support.testrail.com/hc/en-us/articles/7373850291220-Configuring-custom-fields#h_01HSK9TCATKMFMW33V09N8RCJ4).

2. Verify if the custom field is showing in **Customizations > Result Fields** list under **Custom type**. 

    In the example below, you can see the custom required field `Test Execution Unit`.

    <img src="https://tw-cdn.katalon.com/katalon-studio/integrations/test-management/testrail/TestRail_Customizations.png" alt="TestRail custom field" width="700" />

3. In Katalon Studio, go to **Project > Settings > Plugins > TestRail**.

4. Use the **Custom fields mapping** section to manually enter the custom TestRail field in the first column to your Katalon predefined variable in the second column. Use **Add**, **Delete** and **Clear** buttons to edit or update your mapping variables

    <img src="https://tw-cdn.katalon.com/katalon-studio/integrations/test-management/testrail/TestRail_dialog.png" alt="Custom field mappings" width="500" />  
    
    Refer to the following predefined variables when mapping to TestRail fields:

| Name of field      | Value      |
| ------------- | ------------- |
| `testSuite.description` | Test suite description. |
| `hostName` | Host name. |
| `os` | Operating system. |
| `browser` | Browser's name and version. |
| `deviceId` | ID of the executed device. |
| `deviceName` | Name of the executed device. |
| `suiteName` | Name of the test suite. |
| `executionProfile` | Execution profile used during the test. |
| `startTime` | Start time of the test execution. |
| `duration` | Duration of the test execution. |
| `totalPassed` | Total passed test cases. |
| `totalFailed` | Total failed test cases. |
| `totalError` | Total error test cases. |
| `totalIncomplete` | Total incomplete test cases. |
| `totalSkipped` | Total skipped test cases. |

5. Click **Apply** or **Apply and Close** to save your changes.

You have successfully mapped your TestRail custom required field to Katalon Studio.

Click **Restore to Defaults** to reset your TestRail configuration to default settings.

## Query test cases linked to TestRail in a dynamic test suite

<div xmlns="http://www.w3.org/1999/xhtml" className="section prereq p"><ul className="ul"><li className="li"><p className="p">You have enabled the TestRail integration   with <span className="ph">Katalon Studio</span>. See: <a className="xref" href=" /katalon-studio/integrations/test-management/configure-testrail-integration-in-katalon-studio#enable-testrail-integration-in-katalon-studio">Configure TestRail integration in <span className="ph">Katalon Studio</span></a>.</p></li></ul></div>

When the TestRail Integration plugin is enabled, the Query Provider in the dynamic test suite is updated with the TestRail query syntax standard. This allows you to query test cases associated with the TestRail test runs in the dynamic test suite.

To learn more about query syntax in the dynamic test suite, you can refer to this guide: [Dynamic Test Suite](/katalon-studio/manage-test-artifacts/dynamic-test-suite/manage-dynamic-test-suites-in-katalon-studio).

Follow these steps:

1. Open a dynamic test suite in Katalon Studio.
2. In the **Query** text box, enter the ID of a TestRail test run, then click on the **Preview** button.

    <img className="image" src={useBaseUrl("/928adad0-22b2-11ed-9930-0242fe3e4a3f/KS-Quey-TestRail-test-cases-in-dynamic-test-suite.png")} alt="Query TestRail test run in dynamic test suite" />
