---
hide_title: true
title: View test suite and test suite collection reports in Katalon Studio
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# View test suite and test suite collection reports in Katalon Studio

## Test suite report

You can view reports directly inside each test suite page.

After executing a test suite, to see the test suite report, go to the **Result** tab.

<img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/test-suite-report/KS-835-REPORTS-Test-suite-results-tab.png")} alt="Results tab" />

<table xmlns="http://www.w3.org/1999/xhtml" className="table anchor_top_offset" id="id_1__55310d43-052a-4321-8708-c158e93402d0"><caption /><thead className="thead"><tr className><th className="entry anchor_top_offset" id="id_1__55310d43-052a-4321-8708-c158e93402d0__entry__1">Component</th><th className="entry anchor_top_offset" id="id_1__55310d43-052a-4321-8708-c158e93402d0__entry__2">Description</th></tr></thead><tbody className="tbody"><tr className><td className="entry" headers="id_1__55310d43-052a-4321-8708-c158e93402d0__entry__1 id_1__55310d43-052a-4321-8708-c158e93402d0__entry__2 ">Test cases table</td><td className="entry" headers="id_1__55310d43-052a-4321-8708-c158e93402d0__entry__1 id_1__55310d43-052a-4321-8708-c158e93402d0__entry__2 ">List of executed test cases.</td></tr><tr className><td className="entry" headers="id_1__55310d43-052a-4321-8708-c158e93402d0__entry__1 id_1__55310d43-052a-4321-8708-c158e93402d0__entry__2 ">Summary tab</td><td className="entry" headers="id_1__55310d43-052a-4321-8708-c158e93402d0__entry__1 id_1__55310d43-052a-4321-8708-c158e93402d0__entry__2 ">Information of the executed environment and summary of the execution result.</td></tr><tr className><td className="entry" headers="id_1__55310d43-052a-4321-8708-c158e93402d0__entry__1 id_1__55310d43-052a-4321-8708-c158e93402d0__entry__2 ">Execution Settings tab</td><td className="entry" headers="id_1__55310d43-052a-4321-8708-c158e93402d0__entry__1 id_1__55310d43-052a-4321-8708-c158e93402d0__entry__2 "><p className="p">Settings of execution browsers/devices. For example:</p><p className="p"><img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/test-suite-report/KS-835-REPORTS-Execution-settings.png")} /><br /><br /></p></td></tr><tr className><td className="entry" headers="id_1__55310d43-052a-4321-8708-c158e93402d0__entry__1 id_1__55310d43-052a-4321-8708-c158e93402d0__entry__2 ">Execution Environment tab</td><td className="entry" headers="id_1__55310d43-052a-4321-8708-c158e93402d0__entry__1 id_1__55310d43-052a-4321-8708-c158e93402d0__entry__2 "><p className="p">Other information about the executed system. For example:</p><p className="p"><img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/test-suite-report/KS-835-REPORTS-Execution-environment.png")} /><br /><br /></p></td></tr></tbody></table> 

### Test cases table

The summary information of all executed iterations done in the test suite is displayed here. Each time when a test case is executed with a test data row is considered an iteration.

<img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/test-suite-report/KS-835-REPORT-test-case-table.png")} alt="Test cases list" />

You can filter reports based on their execution status:
 
<table xmlns="http://www.w3.org/1999/xhtml" className="table anchor_top_offset" id="id_1__0d6213b6-55a4-455e-957d-fccbec843284"><caption /><thead className="thead"><tr className><th className="entry anchor_top_offset" id="id_1__0d6213b6-55a4-455e-957d-fccbec843284__entry__1">Filter</th><th className="entry anchor_top_offset" id="id_1__0d6213b6-55a4-455e-957d-fccbec843284__entry__2">Description</th></tr></thead><tbody className="tbody"><tr className><td className="entry" headers="id_1__0d6213b6-55a4-455e-957d-fccbec843284__entry__1 id_1__0d6213b6-55a4-455e-957d-fccbec843284__entry__2 ">Passed</td><td className="entry" headers="id_1__0d6213b6-55a4-455e-957d-fccbec843284__entry__1 id_1__0d6213b6-55a4-455e-957d-fccbec843284__entry__2 ">Show only iterations which are passed.</td></tr><tr className><td className="entry" headers="id_1__0d6213b6-55a4-455e-957d-fccbec843284__entry__1 id_1__0d6213b6-55a4-455e-957d-fccbec843284__entry__2 ">Failed</td><td className="entry" headers="id_1__0d6213b6-55a4-455e-957d-fccbec843284__entry__1 id_1__0d6213b6-55a4-455e-957d-fccbec843284__entry__2 ">Show only iterations which are failed.</td></tr><tr className><td className="entry" headers="id_1__0d6213b6-55a4-455e-957d-fccbec843284__entry__1 id_1__0d6213b6-55a4-455e-957d-fccbec843284__entry__2 ">Error</td><td className="entry" headers="id_1__0d6213b6-55a4-455e-957d-fccbec843284__entry__1 id_1__0d6213b6-55a4-455e-957d-fccbec843284__entry__2 ">Show only iterations having errors.</td></tr><tr className><td className="entry" headers="id_1__0d6213b6-55a4-455e-957d-fccbec843284__entry__1 id_1__0d6213b6-55a4-455e-957d-fccbec843284__entry__2 ">Incomplete</td><td className="entry" headers="id_1__0d6213b6-55a4-455e-957d-fccbec843284__entry__1 id_1__0d6213b6-55a4-455e-957d-fccbec843284__entry__2 ">Show only incomplete iterations.</td></tr><tr className><td className="entry" headers="id_1__0d6213b6-55a4-455e-957d-fccbec843284__entry__1 id_1__0d6213b6-55a4-455e-957d-fccbec843284__entry__2 ">Skipped</td><td className="entry" headers="id_1__0d6213b6-55a4-455e-957d-fccbec843284__entry__1 id_1__0d6213b6-55a4-455e-957d-fccbec843284__entry__2 ">Show only skipped iterations.</td></tr></tbody></table>

If qTest and JIRA are configured in project settings, you can submit data to those systems. To learn more about qTest and Jira integration, you can refer to the following documents:

- [qTest Integration](/katalon-studio/integrations/test-management/configure-qtest-integration-in-katalon-studio)
- [JIRA Integration](/katalon-studio/integrations/test-management/configure-jira-integration-in-katalon-studio)

### Test suite summary

This section gives the summary information of the test suite:

<img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/test-suite-report/KS-835-REPORTS-Summary.png")} alt="Test suite summary" />

<table xmlns="http://www.w3.org/1999/xhtml" className="table anchor_top_offset" id="id_1__ec0a1418-5780-4744-a003-f917e12df753"><caption /><thead className="thead"><tr className><th className="entry anchor_top_offset" id="id_1__ec0a1418-5780-4744-a003-f917e12df753__entry__1">Field</th><th className="entry anchor_top_offset" id="id_1__ec0a1418-5780-4744-a003-f917e12df753__entry__2">Description</th></tr></thead><tbody className="tbody"><tr className><td className="entry" headers="id_1__ec0a1418-5780-4744-a003-f917e12df753__entry__1 id_1__ec0a1418-5780-4744-a003-f917e12df753__entry__2 "><strong className="ph b">Test Suite ID</strong></td><td className="entry" headers="id_1__ec0a1418-5780-4744-a003-f917e12df753__entry__1 id_1__ec0a1418-5780-4744-a003-f917e12df753__entry__2 ">The ID of the executed test suite in Katalon Studio.</td></tr><tr className><td className="entry" headers="id_1__ec0a1418-5780-4744-a003-f917e12df753__entry__1 id_1__ec0a1418-5780-4744-a003-f917e12df753__entry__2 "><strong className="ph b">Hostname</strong></td><td className="entry" headers="id_1__ec0a1418-5780-4744-a003-f917e12df753__entry__1 id_1__ec0a1418-5780-4744-a003-f917e12df753__entry__2 ">The hostname of the environment where the test suite was executed.</td></tr><tr className><td className="entry" headers="id_1__ec0a1418-5780-4744-a003-f917e12df753__entry__1 id_1__ec0a1418-5780-4744-a003-f917e12df753__entry__2 "><strong className="ph b">Local OS</strong></td><td className="entry" headers="id_1__ec0a1418-5780-4744-a003-f917e12df753__entry__1 id_1__ec0a1418-5780-4744-a003-f917e12df753__entry__2 ">The OS used to open Katalon Studio.</td></tr><tr className><td className="entry" headers="id_1__ec0a1418-5780-4744-a003-f917e12df753__entry__1 id_1__ec0a1418-5780-4744-a003-f917e12df753__entry__2 "><strong className="ph b">Platform</strong></td><td className="entry" headers="id_1__ec0a1418-5780-4744-a003-f917e12df753__entry__1 id_1__ec0a1418-5780-4744-a003-f917e12df753__entry__2 ">The OS, browser, and browser version used to execute the test.</td></tr><tr className><td className="entry" headers="id_1__ec0a1418-5780-4744-a003-f917e12df753__entry__1 id_1__ec0a1418-5780-4744-a003-f917e12df753__entry__2 "><strong className="ph b">Start / End / Elapse</strong></td><td className="entry" headers="id_1__ec0a1418-5780-4744-a003-f917e12df753__entry__1 id_1__ec0a1418-5780-4744-a003-f917e12df753__entry__2 ">Execution start/end date time and duration.</td></tr><tr className><td className="entry" headers="id_1__ec0a1418-5780-4744-a003-f917e12df753__entry__1 id_1__ec0a1418-5780-4744-a003-f917e12df753__entry__2 "><strong className="ph b">Total TC</strong></td><td className="entry" headers="id_1__ec0a1418-5780-4744-a003-f917e12df753__entry__1 id_1__ec0a1418-5780-4744-a003-f917e12df753__entry__2 ">Total number of test cases and their execution status.</td></tr></tbody></table> 

### Test case log details

To view details of the executed logs, in the **Test Case Table**, select an iteration and click **Show Test Case Details**.

<img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/test-suite-report/KS-835-REPORT-Show-test-case-details.png")} alt="Show Test Cases Details" />

1. **Test Log**: Details regarding all the executed steps and their status are displayed in this tab.

  <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/test-suite-report/KS-835-REPORT-test-log.png")} width={650} alt="Test log tab" />

  | Component | Description |
  | ------------ | ------------- |
  | Test Log **Information** tab | Information of the test step selected in the **Test Case**'s Log section: <ul><li>The **Name** of the test step (the name of the keyword used in the test step).</li><li>Execution **Start/End** date time and duration.</li><li>The **Description** of the test step.</li><li>Any system **Message** raised when the test step was executed.</li></ul> |
  | Test Log **Image** tab | The screenshot taken from the application under test, it is captured in either of the following situations: <ul><li>An error occurs during test execution.</li><li>The take screenshot keyword is used. To learn more about the take screenshot keyword, you can refer to the following document: [[WebUI] Take Screenshot](/katalon-studio/keywords/keyword-description-in-katalon-studio/web-ui-keywords/webui-take-screenshot).</li></ul> |

  <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/test-suite-report/KS-835-REPORT-image-tab.png")} width={600} alt="test log image tab" />

  You can determine which type of information to be displayed by using the provided filters:

  <table className="table anchor_top_offset" id="id_1__0e02d6e8-3418-4e35-9841-dd0a63994591"><caption /><thead className="thead"><tr className><th className="entry anchor_top_offset" id="id_1__0e02d6e8-3418-4e35-9841-dd0a63994591__entry__1">Filter</th><th className="entry anchor_top_offset" id="id_1__0e02d6e8-3418-4e35-9841-dd0a63994591__entry__2">Description</th></tr></thead><tbody className="tbody"><tr className><td className="entry" headers="id_1__0e02d6e8-3418-4e35-9841-dd0a63994591__entry__1 id_1__0e02d6e8-3418-4e35-9841-dd0a63994591__entry__2 ">Info</td><td className="entry" headers="id_1__0e02d6e8-3418-4e35-9841-dd0a63994591__entry__1 id_1__0e02d6e8-3418-4e35-9841-dd0a63994591__entry__2 ">Show the messages logged for information/reference.</td></tr><tr className><td className="entry" headers="id_1__0e02d6e8-3418-4e35-9841-dd0a63994591__entry__1 id_1__0e02d6e8-3418-4e35-9841-dd0a63994591__entry__2 ">Passed</td><td className="entry" headers="id_1__0e02d6e8-3418-4e35-9841-dd0a63994591__entry__1 id_1__0e02d6e8-3418-4e35-9841-dd0a63994591__entry__2 ">Show the steps which are successfully executed.</td></tr><tr className><td className="entry" headers="id_1__0e02d6e8-3418-4e35-9841-dd0a63994591__entry__1 id_1__0e02d6e8-3418-4e35-9841-dd0a63994591__entry__2 ">Failed</td><td className="entry" headers="id_1__0e02d6e8-3418-4e35-9841-dd0a63994591__entry__1 id_1__0e02d6e8-3418-4e35-9841-dd0a63994591__entry__2 ">Show the steps which are failed to execute.</td></tr><tr className><td className="entry" headers="id_1__0e02d6e8-3418-4e35-9841-dd0a63994591__entry__1 id_1__0e02d6e8-3418-4e35-9841-dd0a63994591__entry__2 ">Error</td><td className="entry" headers="id_1__0e02d6e8-3418-4e35-9841-dd0a63994591__entry__1 id_1__0e02d6e8-3418-4e35-9841-dd0a63994591__entry__2 ">Show the steps having errors.</td></tr><tr className><td className="entry" headers="id_1__0e02d6e8-3418-4e35-9841-dd0a63994591__entry__1 id_1__0e02d6e8-3418-4e35-9841-dd0a63994591__entry__2 ">Incomplete</td><td className="entry" headers="id_1__0e02d6e8-3418-4e35-9841-dd0a63994591__entry__1 id_1__0e02d6e8-3418-4e35-9841-dd0a63994591__entry__2 ">Show incomplete steps due to other factors such as wrong syntax, power shortage, disconnected network, etc...</td></tr><tr className><td className="entry" headers="id_1__0e02d6e8-3418-4e35-9841-dd0a63994591__entry__1 id_1__0e02d6e8-3418-4e35-9841-dd0a63994591__entry__2 ">Warning</td><td className="entry" headers="id_1__0e02d6e8-3418-4e35-9841-dd0a63994591__entry__1 id_1__0e02d6e8-3418-4e35-9841-dd0a63994591__entry__2 ">Show the steps which have warning status.</td></tr><tr className><td className="entry" headers="id_1__0e02d6e8-3418-4e35-9841-dd0a63994591__entry__1 id_1__0e02d6e8-3418-4e35-9841-dd0a63994591__entry__2 ">Not Run</td><td className="entry" headers="id_1__0e02d6e8-3418-4e35-9841-dd0a63994591__entry__1 id_1__0e02d6e8-3418-4e35-9841-dd0a63994591__entry__2 ">Show the skipped steps.</td></tr></tbody></table>

  If you have configured Jira integration, you can submit a ticket to this system. For further details, you can refer to this document: [Submit an issue to Jira](/katalon-studio/integrations/test-analysis/jira/submit-an-issue-from-katalon-studio-to-jira).

  Screenshots are taken for the failed steps, and you can hover the mouse cursor over the attachment icon to review.

2. **Information**: You can find the summary information of the test case in this tab.

  <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/test-suite-report/KS-835-REPORT-information-tab.png")} width={600} alt="Information tab" />

  <table className="table anchor_top_offset" id="id_1__c79e469d-77bd-4222-bc19-22f9d3621642"><caption /><colgroup><col /><col /></colgroup><thead className="thead"><tr className><th className="entry anchor_top_offset" id="id_1__c79e469d-77bd-4222-bc19-22f9d3621642__entry__1">Field</th><th className="entry anchor_top_offset" id="id_1__c79e469d-77bd-4222-bc19-22f9d3621642__entry__2">Description</th></tr></thead><tbody className="tbody"><tr className><td className="entry" headers="id_1__c79e469d-77bd-4222-bc19-22f9d3621642__entry__1 id_1__c79e469d-77bd-4222-bc19-22f9d3621642__entry__2 "><span className="ph uicontrol">Test Case ID</span></td><td className="entry" headers="id_1__c79e469d-77bd-4222-bc19-22f9d3621642__entry__1 id_1__c79e469d-77bd-4222-bc19-22f9d3621642__entry__2 ">The ID of the executed test case in Katalon Studio.</td></tr><tr className><td className="entry" headers="id_1__c79e469d-77bd-4222-bc19-22f9d3621642__entry__1 id_1__c79e469d-77bd-4222-bc19-22f9d3621642__entry__2 "><span className="ph uicontrol">Start / End / Elapse</span></td><td className="entry" headers="id_1__c79e469d-77bd-4222-bc19-22f9d3621642__entry__1 id_1__c79e469d-77bd-4222-bc19-22f9d3621642__entry__2 ">Execution start/end date time and duration.</td></tr><tr className><td className="entry" headers="id_1__c79e469d-77bd-4222-bc19-22f9d3621642__entry__1 id_1__c79e469d-77bd-4222-bc19-22f9d3621642__entry__2 "><span className="ph uicontrol">Description</span></td><td className="entry" headers="id_1__c79e469d-77bd-4222-bc19-22f9d3621642__entry__1 id_1__c79e469d-77bd-4222-bc19-22f9d3621642__entry__2 ">The description of the test case.</td></tr><tr className><td className="entry" headers="id_1__c79e469d-77bd-4222-bc19-22f9d3621642__entry__1 id_1__c79e469d-77bd-4222-bc19-22f9d3621642__entry__2 "><span className="ph uicontrol">Message</span></td><td className="entry" headers="id_1__c79e469d-77bd-4222-bc19-22f9d3621642__entry__1 id_1__c79e469d-77bd-4222-bc19-22f9d3621642__entry__2 ">Any system message raised when this iteration was executed.</td></tr></tbody></table>

3. **Integration**: The information regarding qTest or JIRA integration of this iteration is displayed in this tab.

  <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/test-suite-report/integration-tab.png")} width={400} alt="Integration tab" />

## Test suite collection report

You can view reports directly inside each test suite collection page. Test suite collection reports are only available for Katalon Studio Enterprise users.

After executing a test suite collection, to see the test suite collection report, go to the **Result** tab.

<img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/test-suite-report/KS-REPORTS-Results-of-the-TSC.png")} alt="Test suite collection report" />

<table xmlns="http://www.w3.org/1999/xhtml" className="table anchor_top_offset" id="id_5__8b3f671a-3935-440c-8664-9681a8b8a5c7"><caption /><colgroup><col /><col /></colgroup><thead className="thead"><tr className><th className="entry anchor_top_offset" id="id_5__8b3f671a-3935-440c-8664-9681a8b8a5c7__entry__1">Field</th><th className="entry anchor_top_offset" id="id_5__8b3f671a-3935-440c-8664-9681a8b8a5c7__entry__2">Description</th></tr></thead><tbody className="tbody"><tr className><td className="entry" headers="id_5__8b3f671a-3935-440c-8664-9681a8b8a5c7__entry__1 id_5__8b3f671a-3935-440c-8664-9681a8b8a5c7__entry__2 "><span className="ph uicontrol">ID</span></td><td className="entry" headers="id_5__8b3f671a-3935-440c-8664-9681a8b8a5c7__entry__1 id_5__8b3f671a-3935-440c-8664-9681a8b8a5c7__entry__2 ">The ID of the executed test suite in Katalon Studio.</td></tr><tr className><td className="entry" headers="id_5__8b3f671a-3935-440c-8664-9681a8b8a5c7__entry__1 id_5__8b3f671a-3935-440c-8664-9681a8b8a5c7__entry__2 "><span className="ph uicontrol">Environment</span></td><td className="entry" headers="id_5__8b3f671a-3935-440c-8664-9681a8b8a5c7__entry__1 id_5__8b3f671a-3935-440c-8664-9681a8b8a5c7__entry__2 ">The environment in which the test suite is executed.</td></tr><tr className><td className="entry" headers="id_5__8b3f671a-3935-440c-8664-9681a8b8a5c7__entry__1 id_5__8b3f671a-3935-440c-8664-9681a8b8a5c7__entry__2 "><span className="ph uicontrol">Status</span></td><td className="entry" headers="id_5__8b3f671a-3935-440c-8664-9681a8b8a5c7__entry__1 id_5__8b3f671a-3935-440c-8664-9681a8b8a5c7__entry__2 ">Information about whether the execution is completed or not.</td></tr><tr className><td className="entry" headers="id_5__8b3f671a-3935-440c-8664-9681a8b8a5c7__entry__1 id_5__8b3f671a-3935-440c-8664-9681a8b8a5c7__entry__2 "><span className="ph uicontrol">Failed Tests / Total</span></td><td className="entry" headers="id_5__8b3f671a-3935-440c-8664-9681a8b8a5c7__entry__1 id_5__8b3f671a-3935-440c-8664-9681a8b8a5c7__entry__2 ">Total test cases in the test suite and the number of failed test cases, if any.</td></tr><tr className><td className="entry" headers="id_5__8b3f671a-3935-440c-8664-9681a8b8a5c7__entry__1 id_5__8b3f671a-3935-440c-8664-9681a8b8a5c7__entry__2 "><span className="ph uicontrol">Test Suite Details</span></td><td className="entry" headers="id_5__8b3f671a-3935-440c-8664-9681a8b8a5c7__entry__1 id_5__8b3f671a-3935-440c-8664-9681a8b8a5c7__entry__2 ">Shows test suite reports, see above: <a className="xref" href="/katalon-studio/test-reports/view-test-reports/view-test-suite-and-test-suite-collection-reports-in-katalon-studio#id_1">Test suite reports</a>.</td></tr></tbody></table> 

## Report history

:::note
Report History is only available for Katalon Studio Enterprise users.
:::

Once a test suite/test suite collection finishes its execution, a report is automatically generated and stored in the Reports folder.

For example:

<img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/test-suite-report/KS-825-REPORT-history.png")} width={500} alt="Test suite history reports" />

The report is named with the following naming convention: `YYYYMMDD_HHmmss`, corresponding to the date and time of the start of the execution.

## Report settings

### Automatically generate reports

This feature enables auto-generation of reports in the selected format.

Follow the steps to automatically generate test reports for you after test execution:

1. Go to **Project > Settings > Report**.

2. Select your preferred format/s for the reports generated after each test suite execution. You can select at least one of the following available formats:

  ![Automatically generate test reports](https://tw-cdn.katalon.com/katalon-studio/Test+report/View+test+suite+and+test+suite+collection+reports+in+Katalon+Studio/KS_automatically_generate_reports.png)

  - HTML (`.html`) - Provides a comprehensive, browser-viewable summary of test results.
  - CSV (`.csv`) - Spreadsheet-friendly format ideal for data analysis and integration with other tools. This is useful for creating custom dashboards or importing into reporting systems (e.g., Excel, BI tools)
  - PDF (`.pdf`) - Printable, static snapshot of the test execution summary, which is ideal for sharing with stakeholders or archiving formal testing evidence.
  - Console logs (`console0.log`) - Captures raw execution logs output by Katalon Studio during runtime and is useful for debugging, error tracing, and detailed execution review. When the primary log file exceeds the configured max size (e.g., 10MB), additional files like `console1.log`, `console2.log`, etc., are generated.

:::note
- The CSV and PDF options are available for test suite reports only.
- When exporting test reports to PDF file, special characters will be converted to UTF-8 format.
:::

3. Click **Apply** or **Apply and Close** to save and apply your report configuration.

### HTML report file structure

When test executions are long or contain many screenshots, the report size may become too large, potentially causing issues when generating or viewing it.

To address this, enable the following option for HTML reports: **Attach reference images using linked screenshots (not embedded) to reduce report file size**. This option reduces HTML report size by saving screenshots as separate files in the Reports folder. The HTML report will reference these images via relative paths instead of embedding them.

<img title="Attach reference images using linked screenshots (not embedded) to reduce report file size" alt="Attach reference images using linked screenshots (not embedded) to reduce report file size" src="https://tw-cdn.katalon.com/katalon-studio/Test+report/View+test+reports/KS_Test_report_attach_reference_images.png"/>

Below is an example comparison of file sizes for an HTML report:

- Without enabling the option: The report size is  271,7 MB (with screenshots embedded).

  <img src={useBaseUrl("https://tw-cdn.katalon.com/katalon-studio/Test%20report/View%20test%20suite%20and%20test%20suite%20collection%20reports%20in%20Katalon%20Studio/Screenshot_embedded_report.jpg")} width={700} alt="HTML report without option enabled" />

  - With the option enabled: The report size is reduced to 468 KB (with screenshots linked).

  <img className="image" src={useBaseUrl("https://tw-cdn.katalon.com/katalon-studio/Test%20report/View%20test%20suite%20and%20test%20suite%20collection%20reports%20in%20Katalon%20Studio/Screenshot_linked_report.jpg")} width={700} alt="HTML report with option enabled"  />

:::note
When sharing reports, always zip the entire **Reports** folder to ensure all linked assets (like images) are included. 

Log file settings only affect the size and speed of log generation. They do not change the content of the logs and are intended for advanced users. 
:::

### Apply new report template and split report

You can now opt in to use Katalon Studio’s modernized HTML report template by selecting the **Apply new report template** option. This updated format improves readability and usability with a clean layout, status-based filtering, numbered test steps, and expand/collapse functionality. 

![Apply new report template](https://tw-cdn.katalon.com/katalon-studio/Test+report/View+test+suite+and+test+suite+collection+reports+in+Katalon+Studio/KS_apply_new_template_split_report.png)

Click here to view a sample test suite report in the new template: [Sample test suite report (HTML)](https://tw-cdn.katalon.com/katalon-studio/Test+report/View+test+reports/View+and+customize+execution+log+in+Katalon+Studio/Sample_Test_Suite_Report_Template.html).

To improve performance when handling large test reports, enable the **Split the report into files for faster loading** option. This advanced setting generates a lightweight overview HTML file containing test case summaries, along with multiple `.js` files that store the detailed results for each test case. This structure reduces memory usage and loading time. Even if some `.js` files are missing, the report overview will still be viewable.

:::note
- When sharing the report, make sure to zip the entire report folder—including the HTML and `.js` files. Otherwise, detailed test steps will not be displayed. 
- Email reporting with this new format is not fully supported yet; only the summary will be included in the email, not the full report.
:::

## Manually export reports

For test suite collections, you can export to HTML format only. 

To manually export reports, follow these steps:

1. Open the **Result** view of a test suite or a test suite collection.

2. On the top right corner, select E**xport** report. Then, choose a format to export.

<img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/test-suite-report/KS-REPORTS-Export-reports-manually.png")} alt="Manually export reports" />

:::warning attention
You may encounter errors when generating HTML reports with large sizes.
:::

- Generating reports larger than 1 GB might cause the error `java.lang.OutOfMemoryError: Java heap space`, and PDF reports might not be generated.
- HTML reports larger than 512 MB might not be rendered and displayed well on a browser, however, the HTML report still includes full information about test execution.

The recommended size for HTML reports is 500 MB. For large executions, you might want to reduce the amount of screenshots taken, avoid taking full-page screenshots, or enable the **Attach reference images using linked screenshots (not embedded) to reduce report file size** option.
:::

## Customize Log File Settings

Katalon Studio offers configurable system properties that let users manage how log files are generated, stored, and buffered. These settings are particularly useful for optimizing performance and storage during large-scale or long-running test executions by controlling log file size, retention limits, and buffering behavior.

By default, when the `console0.txt` file exceeds 10MB, Katalon Studio automatically splits the log into sequential files (e.g., `console1.log`, `console2.log`, etc.). 

To customize this behavior, follow the steps below:

1. Open the `katalon.ini` file in a text editor.

2. Add the desired `-D` system properties below the `-vmargs` line.

  For example: 

  ```
  -vmargs
  -DmaxLogFileSize=5242880
  -DmaxLogFile=100
  -DlogRecordQueueSize=10000
  -DbatchLogRecordSize=5000
  ```

Refer to the following table for system properties you can use to customize log behavior:

| Property | Description | Default Value | Example Configuration |
|----------|----------| ----------|----------|
| `-DmaxLogFileSize`    | Sets the maximum size (in bytes) a log file can reach before a new one is created.   | 10MB| `-DmaxLogFileSize=5242880` (5MB) |
| `-DmaxLogFile`    | Defines the maximum number of log files to retain. Older logs are deleted beyond this limit.   | 2000 | `-DmaxLogFile=100` |
| `-DlogRecordQueueSize`    | Specifies the size of the queue that holds log records before they are processed.   | 7000 | `-DlogRecordQueueSize=10000` |
| `-DbatchLogRecordSize`    | Determines how many log records are processed in a single batch.   | 3000 | `-DbatchLogRecordSize=5000` |

See the following recommendations below for best practices:

- The first two properties (`maxLogFileSize`, `maxLogFile`) are the most commonly used. Adjust the queue and batch sizes only if needed for advanced troubleshooting.
- Only adjust `-DlogRecordQueueSize` and `-DbatchLogRecordSize` if you are troubleshooting log buffer warnings.
  
  :::tip
  You may encounter the following log warnings when adjusting `-DlogRecordQueueSize` and `-DbatchLogRecordSize`:

  ```
  The buffer of log file is full. The stdout line is dropped and won't be in the log file.
  The buffer of log file is full. The stderr line is dropped and won't be in the log file.
  ```

  To resolve this, increase the following values to:

  ```
  -DlogRecordQueueSize=10000
  -DbatchLogRecordSize=5000
  ```
  :::

- Restart Katalon Studio after applying any changes to `katalon.ini`.

## Log Viewer

Execute a test suite and observe the **Log Viewer** after the test execution completes. The generated reports are the same as the settings you have configured above: 
<img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/Basic%20Report/log-viewer.png")} width={391} alt="Report generator in the log viewer" />

You can view the generated reports in `<project_folder>\Reports\<execution_folder>` after the test execution finishes.

- Test suite report folder: <img className="image" width={700} src={useBaseUrl("https://tw-cdn.katalon.com/katalon-studio/Test%20report/View%20test%20suite%20and%20test%20suite%20collection%20reports%20in%20Katalon%20Studio/testsuite-report-folder.png")} alt="test suite report" />

- Test suite collection report folder: <img className="image" width={700} src={useBaseUrl("https://tw-cdn.katalon.com/katalon-studio/Test%20report/View%20test%20suite%20and%20test%20suite%20collection%20reports%20in%20Katalon%20Studio/testsuite-collection-report-folder.png")} alt="test suite collection report" />

## Get generated reports location at runtime

To retrieve current generated reports location, you can use the sample code below:

```
import com.kms.katalon.core.configuration.RunConfiguration{"\n"}RunConfiguration.getReportFolder(){"\n"}
```

You can also retrieve other information through the RunConfiguration package, see: [Katalon Javadocs: RunConfiguration](https://api-docs.katalon.com/com/kms/katalon/core/configuration/RunConfiguration.html)
           
## Video capturing

:::note
- K-Lite Codec is recommended to play the Katalon Studio test execution videos. You can download K-Lite Codec on the Codec Guide website: [K-Lite Codec](https://www.codecguide.com/download_kl.htm).
- Support execution at the test suite level.
- Support all browsers except for Remote, Headless, Kobiton, and Custom. For remote or headless browsers, it's recommended to use [Katalium Server](/docs//katalon-platform/plugins-and-add-ons/katalium-server/katalium-server---execute-katalon-studio-scripts-on-remote-machines) to view captured sessions.
- Recording parallel execution is NOT supported yet.
- Recording parallel execution is NOT supported yet.
- On Linux, videos recorded in Katalon Studio require VLC for playback, except for WebM files, which can be opened in most browsers.
:::

Debugging can be time-consuming and challenging for many automation testers. Katalon Studio helps solve this problem by supporting you with the ability to capture test execution via video format. You can enable the video capturing feature in **Project Settings**.

To learn how to work with Katalon Studio’s video capturing feature, see:

- [Generate browser-based videos in Katalon Studio reports](/katalon-studio/test-reports/generate-test-reports/generate-browser-based-videos-in-katalon-studio-reports)
- [Generate screen-based videos in Katalon Studio reports](/katalon-studio/test-reports/generate-test-reports/generate-screen-based-videos-in-katalon-studio-reports)

After executing a test suite, go to the **Result** tab. The test cases table displays each test case along with its attached video.

To play the video, click the play icon in the Video column. Test step descriptions are embedded as subtitles:

<img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/test-suite-report/KS-835-REPORTS-Enable-video-recording.png")} alt="View video capturing" />

By watching how the automated test was executed, the testing team can identify exactly where the test failed. Thus, time and resources are managed more efficiently and effectively.

Learn about test suite reports, exporting, and more in our Katalon Academy course: [Katalon Studio: How To Work With Execution Logs and Test Reports](https://academy.katalon.com/courses/software-test-reporting/?utm_source=kat_docs&utm_medium=test_suite_report).
