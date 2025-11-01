---
title: Release Health Dashboard
---
<!--- PRD: https://katalon.atlassian.net/wiki/spaces/PRA/pages/3815702729/PRD+-+TestOps+Release+Dashboard+-+Phase+1 -->

This explains what the Release Health Dashboard and its components.

:::caution requirements
You must possess the Test Lead, Tester, or Member role to view this page.
:::

## Overview

The **Release Health Dashboard** provides you with a consolidated view of your release quality metrics and testing progress. This dashboard transforms complex testing data into actionable insights, helping you determine release readiness at a glance.

This dashboard serves as your central hub for release quality assessment. It organizes critical quality data to answer two fundamental questions about your release cycle:

- What testing work remains incomplete?
- Does the release meet quality thresholds for deployment?

The Release Health Dashboard eliminates the need to compile quality data from multiple sources, reducing the complexity of release decisions. By presenting critical metrics in a unified interface, it enables quick identification of quality issues and supports data-driven release planning.

---

## View the Release Health Dashboard

Find this feature by going to **Home** > **Release Health**.

<br/>

<img src="https://tw-cdn.katalon.com/katalon-testops/Home/Release Quality Dashboard March 21 2025.png" alt="The Release Quality Dashboard in Katalon TestOps." width="1080"/>


Select your **Sprint** or **Release** in the dropdown menu to view the release health metrics for the selected Iteration.

You could also click on **View more** to go to **Plans** and view your sprint/release details.

<br/>

<img src="https://tw-cdn.katalon.com/katalon-testops/Home/Sprint Release Dropdown View More And Expand Annotated March 21 2025.png" alt="The Release Health Dashboard in Katalon TestOps." width="1080"/>
<p align="center"><em>The Iterations are shown. The expand icon ([↗]) and View more button are highlighted.</em></p>

<br/>


You can access detailed information for any visualization on this screen by clicking the expand icon (**[↗]**) in the chart header. This action opens a new tab of the report with more comprehensive metrics and additional data points as it shows in the Reports section.

This feature eliminates navigation to the Reports section by allowing you to access comprehensive testing details directly within the Release Health Dashboard interface. It centralizes all necessary metrics in one location, streamlining your workflow and enabling informed decision-making without switching between application sections. 

---

<br/>

<!--- PRD: https://katalon.atlassian.net/wiki/spaces/PRA/pages/3815702729/PRD+-+TestOps+Release+Dashboard+-+Phase+1 -->

## Release Health Components

:::note Icon Legend:
- Click on the eye icon (👁) to view more details.
- Click on the highlight (🖋️) icon to identify related charts.
::: 

<br/>

This dashboard displays the following information:

**Release Readiness**: This provides an overall assessment of your release quality status based on thresholds. The status displays as **Ready** (Green) when all criteria are met and **At risk** (Red) when any criteria are not met.

<br/>

<img src="https://tw-cdn.katalon.com/katalon-testops/Home/Release Readiness March 21 2025.png" alt="The Release Readiness chart in Katalon TestOps." width="500"/>

<br/>


**Release Blocking Defects**: This displays the number of open defects that could potentially block your release according to priority levels.

<br/>

<img src="https://tw-cdn.katalon.com/katalon-testops/Home/Release Blocking Defects March 21 2025.png" alt="The Release Blocking Defects chart in Katalon TestOps." width="500"/>

<br/>

**Requirement Coverage**: The minimum allowed percentage of requirements needed to be covered by test cases.
<!--- Formula: (Requirements with tests / Total requirements) × 100% -->

<br/>

<img src="https://tw-cdn.katalon.com/katalon-testops/Home/Requirement Coverage 2 March 21 2025.png" alt="The Requirement Coverage chart in Katalon TestOps." width="500"/>

<br/>

**Test Execution Pass Rate**: The minimum allowed percentage of test cases that need to pass.
<!--- Formula: (Passed tests / Total planned tests) × 100% -->

<br/>

<img src="https://tw-cdn.katalon.com/katalon-testops/Home/Test Execution Pass Rate March 21 2025.png" alt="The Test Execution Pass Rate chart in Katalon TestOps." width="500"/>

<br/>

**Test Case Distribution by Execution Status**: A pie chart that displays test cases organized by execution result (Passed, Failed, etc.), showing both counts and percentages for each status category. You can use this to quickly assess your overall test quality and identify problematic areas. This links to the [Test Case Execution](/katalon-platform/analyze/reports/view-test-case-execution-status-report) report.

<br/>

<img src="https://tw-cdn.katalon.com/katalon-testops/Home/Test Case Distribution by Execution Status March 21 2025.png" alt="The Test Case Distribution by Execution Status chart in Katalon TestOps." width="500"/>

<br/>

**Open Defects Distribution by Priority**: A pie chart that displays defects organized by priority levels. This links to the [Total Defects During Period by Status](/katalon-platform/analyze/reports/view-defect-status-analysis-report#view-total-defect-during-period-by-status) report.

<br/>

<img src="https://tw-cdn.katalon.com/katalon-testops/Home/Open Defects Distribution by Priority March 21 2025.png" alt="The Open Defects Distribution by Priority chart in Katalon TestOps." width="500"/>

<br/>   

**Requirement Coverage Summary**: A quanititative metrics panel that categorizes requirements as Fully Covered (all tests published and passed), Partially Covered (tests in development or with mixed results), or Not Covered (no published linked tests), displaying both counts and percentages for each status. This links to the [Requirement Coverage](/katalon-platform/analyze/reports/view-requirement-test-coverage-report) report.

<br/>

<img src="https://tw-cdn.katalon.com/katalon-testops/Home/Requirement Coverage Summary March 21 2025.png" alt="The Requirement Coverage Summary chart in Katalon TestOps." width="500"/>

<br/>

**Requirement Coverage Trend**: A bar chart that tracks three metrics through your iteration: Test Coverage (% of requirements with linked, published test cases), Execution Coverage (% with executed tests), and Pass Coverage (% with passing tests). It spans iteration dates, with higher values indicating better testing progress. This links to the [Requirement Coverage](/katalon-platform/analyze/reports/view-requirement-test-coverage-report) report.

<br/>

<img src="https://tw-cdn.katalon.com/katalon-testops/Home/Requirement Coverage Trend March 21 2025.png" alt="The Requirement Coverage Trend chart in Katalon TestOps." width="500"/>

<br/>

**Test Coverage by Configuration**: View test execution coverage across operating systems and browsers, displaying the executions count for each. This links to the [Configuration Coverage](/katalon-platform/analyze/reports/view-configuration-coverage-report) report.

<br/>

<img src="https://tw-cdn.katalon.com/katalon-testops/Home/Test Coverage by Configuration 2 March 21 2025.png" alt="The Test Coverage by Configuration chart in Katalon TestOps." width="500"/>

<br/>
