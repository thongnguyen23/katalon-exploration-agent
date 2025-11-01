---
title: View Test Failure Analysis Report
---

<!--
- Previously: View Failure Rate Report
- Release notes: https://katalon.atlassian.net/wiki/spaces/PM/pages/3442442241/RA+TestOps+Gen+3+-+GA+Release+20240918
- Doc: https://katalon.atlassian.net/wiki/spaces/PRA/pages/3065840111/RA+Failure+Rate 
-->

This shows you what the Test Failure Analysis Report is and how to use it.

## Prerequisites

- You must possess the Test Lead or Tester role to perform this action. Go to [Roles](/katalon-testops/administration-and-licensing/manage-administrators/assign-or-unassign-account-administrators) or [Permissions](/katalon-testops/administration-and-licensing/manage-systems/permissions/about-permissions) for more information or learn how to [assign a Project Admin here](/katalon-testops/administration-and-licensing/manage-administrators/assign-or-unassign-project-administrators)

---

This report displays test failure frequency distribution in a histogram format to facilitate identification of unstable or problematic test cases. The visualization plots failure percentage (x-axis) against the number of test cases (y-axis), enabling efficient categorization of test reliability patterns. It also displays a list of test cases. Find it in **Reports** > **All Reports** > **Test Failure Analysis**.

## View Test Failure Analysis

1. Go to **Reports** > **All Reports** > **Test Failure Analysis**.

<br/>

<img src="https://tw-cdn.katalon.com/katalon-testops/Reports/All Reports/Report Types/Report Test Failure Analysis.png" alt="The Failure Rate Report page in Katalon TestOps." width="1080"/>

<br/>

2. Enter search parameters to filter for specific test runs. You can enter:
- Input dates
- Select release: Allows you to filter for test run based on its assosciated release.
- Select **Profile**.
- Click on **+ Add more** to view more filters. They are:
     - Select Test Suite
     - Select Test Suite Collection
     - Select Test Run Status
     - Select Executor
     - Select Operating System
     - Select Browser

3. Click on **Apply** to narrow your search or **Reset** to reset all filters.