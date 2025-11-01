---
title: Reports Overview
---
import DocCardList from '@theme/DocCardList'; 
import {useCurrentSidebarCategory} from '@docusaurus/theme-common'; 

export default function TroubleshootingIndex() {

  const category = useCurrentSidebarCategory();

  // Skip the first item (index 0)
  const items = category.items.slice(1);

  return <DocCardList items={items} />;
}

<!-- import { TestOpsG2_TabNameValue, TestOpsG2_TabNameLabel, TestOpsG3_TabNameValue, TestOpsG3_TabNameLabel } from "../../../../reusable-component";
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

<Tabs>
  <TabItem value={TestOpsG2_TabNameValue} label={TestOpsG2_TabNameLabel} >

Katalon reports provide dynamic perspectives and insights into your automated testing activities. 
<br/>

## View test reports

After finishing a test execution, you can view test reports in both Katalon Studio and Katalon TestOps. 
At the initial step, you can view the execution log in Katalon Studio. This helps you to quickly pinpoint the root causes of any issues when troubleshooting automation test execution. See:

- [View and customize execution log in Katalon Studio](/katalon-studio/test-reports/view-test-reports/view-and-customize-execution-log-in-katalon-studio)
- [View test suite and test suite collection reports in Katalon Studio](/katalon-studio/test-reports/view-test-reports/view-test-suite-and-test-suite-collection-reports-in-katalon-studio)
  
For advanced reports and test activity management, you can view the test run results in Katalon TestOps. This is where you can:

- Analyze and compare with your previous test runs. See: [Test runs reports overview](/katalon-platform/analyze/reports/view-test-reports/test-runs-reports-overview).
- Manage your team by analyzing recent test activities, upcoming releases, productivity, quality of test cases, platform coverage, requirement coverage, and local test environments. See: [TestOps dashboard](/katalon-platform/analyze/reports/view-test-reports/view-testops-dashboard/testops-dashboard-overview).
- View test cases, defects, and requirements in one central location with the traceability matrix. See: [View traceability matrix in Katalon TestOps](/katalon-platform/analyze/reports/view-test-reports/view-traceability-matrix-in-katalon-testops).
- View BDD test results in Katalon TestOps. See: [View BDD test results in TestOps](/katalon-platform/analyze/reports/view-test-reports/view-bdd-test-results-in-testops).
- View API performance anomalies. See: [Detect abnormal Web Services in Katalon TestOps](/katalon-platform/analyze/reports/view-test-reports/detect-abnormal-web-services-in-katalon-testops).

## Generate test reports

Katalon TestOps allows you to generate test reports into other formats such as HTML, CSV, PDF, and JUnit. 
You can also generate screen-based and browser-based videos in Katalon Studio reports to quickly troubleshoot failed test cases. See:

- [Generate browser-based videos in Katalon Studio reports](/katalon-studio/test-reports/generate-test-reports/generate-browser-based-videos-in-katalon-studio-reports)
- [Generate screen-based videos in Katalon Studio reports](/katalon-studio/test-reports/generate-test-reports/generate-screen-based-videos-in-katalon-studio-reports)

## Upload test reports

Wherever you conduct a test execution in Katalon TestOps, test results are automatically uploaded to Katalon TestOps.
In case the results fail to upload automatically, you can do so manually from Katalon Studio. See: .  
You can also upload test reports to Katalon TestOps from other frameworks such as: [Mocha](/katalon-platform/analyze/reports/upload-test-reports/upload-reports-from-other-framework/upload-test-reports-from-mocha-to-katalon-testops), [Jest](/katalon-platform/analyze/reports/upload-test-reports/upload-reports-from-other-framework/upload-test-reports-from-jest-to-katalon-testops), [Jasmine](/katalon-platform/analyze/reports/upload-test-reports/upload-reports-from-other-framework/upload-test-reports-from-jasmine-to-katalon-testops), [Pytest](/katalon-platform/analyze/reports/upload-test-reports/upload-reports-from-other-framework/upload-test-reports-from-pytest-to-katalon-testops).

## Manage reports

Katalon allows you to share test reports via email in Katalon Studio and Katalon TestOps. See: [Share test reports via email in Katalon Studio](/katalon-studio/test-reports/share-test-reports-via-email-in-katalon-studio).
Besides that, you can [override test run results status](/katalon-platform/analyze/reports/manage-reports/override-test-results-status-in-katalon-testops) and [filter test runs by build name](/katalon-platform/analyze/reports/manage-reports/filter-test-run-list-by-build-name-in-katalon-testops) in Katalon TestOps.
  </TabItem>

  <TabItem value={TestOpsG3_TabNameValue} label={TestOpsG3_TabNameLabel} default>

This document shows you what the All Reports section is and how to use it.

## Prerequisites

- You need the Test Lead or Tester role to perform these actions. Go to [Roles](/katalon-platform/administer/administration-and-licensing-alternate/manage-systems/permissions/about-roles) or [Permissions](/katalon-platform/administer/administration-and-licensing-alternate/manage-systems/permissions/about-permissions) for more information or learn how to [assign a Project Admin here](/katalon-platform/administer/administration-and-licensing-alternate/manage-administrators/assign-or-unassign-project-administrators)

---

View all available dashboards and metrics about your data from **Reports > All Reports**. All Reports is a centralized repository for all dashboards and metrics within your project, enabling you to efficiently manage and view analytics from one convenient location.

## View All Reports

Go to **Reports > All Reports**. The Reports list displays all metrics in a list, including details such as the metric's creator, when it was created, and when it was last modified.

There are two versions of the All Reports page, the type of which can be toggled from the selections available in the upper left corner:

**Grid view:**

<img src="https://tw-cdn.katalon.com/katalon-testops/Reports/All Reports/Reports All Reports Grid.png" alt="The All Reports page in Katalon TestOps." width="1080"/>

**List view:**

<img src="https://tw-cdn.katalon.com/katalon-testops/Reports/All Reports/Reports All Reports List.png" alt="The All Reports page in Katalon TestOps." width="1080"/>

<br/>

You can also search for a specific report by entering a keyword in the search bar.

  </TabItem>

</Tabs> -->