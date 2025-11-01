---
title: Test Failure Analysis Report
sidebar_custom_props:
    image: https://tw-cdn.katalon.com/katalon-platform/ra/reports/Thumbnail-Test-Failures-Analysis.svg
---
import Reusable from '@site/src/components/reusable-content/testops/testlead-tester.mdx';

This shows you what the Test Failure Analysis Report is and how to use it.

## Prerequisites

<Reusable />

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