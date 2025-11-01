---
hide_title: true
title: View Katalon Studio test results in Jira tickets
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# View Katalon Studio test results in Jira tickets

Katalon Studio integrates with Jira so you can automatically upload and view test execution results inside your Jira issues. This helps teams track test outcomes directly within their development and project management workflows.

## Prerequisites
- You have enabled Jira integration in Katalon Studio. See [Configure Jira integration in Katalon Studio](/katalon-studio/integrations/test-management/configure-jira-integration-in-katalon-studio).
- You have executed test suites in Katalon Studio with the Jira integration enabled.

## Upload Test Results to Jira

When executing a test suite in Katalon Studio, the execution results are automatically exported and uploaded to the linked Jira ticket as a `.zip` file attachment. These results are also tracked in the Katalon Platform panel within the Jira issue.

To view the test results in Jira:

1. Open the Jira issue linked with your test execution.
2. Navigate to **Katalon Platform** section and click **Katalon Studio Test Results** as shown below:

    <img src="https://tw-cdn.katalon.com/katalon-studio/integrations/test-analysis/jira/Click_Katalon_Studio_Test_Results.png" alt="View Katalon Studio test results in Jira tickets" width="400" />

3. You will see a list of uploaded execution result files with their execution status in `.zip` file format.

    <img src="https://tw-cdn.katalon.com/katalon-studio/integrations/test-analysis/jira/View_KS_Test_Results_file.png" alt="View Katalon Studio test results file" width="400" />

    - You can quickly find the test execution status via the JQL query. The syntax is as follows: `"Katalon Status"=status`.
    - For example, to search for all issues that have failed in the Katalon Studio test execution, type `"Katalon Status"=FAIL` in the search bar. Katalon - Studio supports five test statuses: **Passed**, **Failed**, **Incomplete**, **Error**, and **Skipped**.
    - When you view test results in Jira, ensure that you enable file attachments. To do this, follow instructions as given in the Jira document: [Configuring file attachments](https://confluence.atlassian.com/adminjiraserver/configuring-file-attachments-938847851.html).

 
