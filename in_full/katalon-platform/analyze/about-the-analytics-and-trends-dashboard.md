---
title: About the Analytics & Trends Dashboard
---

This explains the Analytics & Trends Dashboard and its components.

## Prerequisites

<!-- Reusable component import-->
import Reusable from '@site/src/components/reusable-content/testops/testlead-tester.mdx';

<Reusable />

---

# Overview

The **Analytics & Trends Dashboard** gives you a consolidated view of your testing activities across your project. This visual interface aggregates key metrics and trends, enabling you to monitor testing progress efficiently.

The dashboard presents testing data through organized charts and statistics that highlight performance patterns and potential issues. You can quickly assess overall project health, track completion rates, and identify testing bottlenecks without navigating through multiple screens.

The at-a-glance format helps you maintain continuous awareness of your testing status throughout the development lifecycle.

---

## View the Analytics & Trends Dashboard

Find this feature by going to **Home** > **Analytics & Trends**.

<br/>

<img src="https://tw-cdn.katalon.com/katalon-testops/Home/Internal Env Analytics and Trends Home.png" alt="The Analytics & Trends Dashboard in Katalon TestOps." width="1080"/>

<p align="center"><em>This is a sample of the Analytics & Trends Dashboard using the default Katalon template.</em></p>

<br/>

You can search for specific data by using the date picker at the top of the dashboard, or search by Interval. The default interval is weekly. You can click on **Reset** to remove these filters. 

<br/>

<img src="https://tw-cdn.katalon.com/katalon-testops/Home/Internal Env Search Parameters Annotated.png" alt="The Analytics & Trends Dashboard in Katalon TestOps." width="1080"/>

<br/>

Access detailed information for any chart on this screen by clicking the expand icon (**[ ]**) in the chart header. This action opens an enhanced version of the report with more comprehensive metrics and additional data points as it shows in the Reports section. 

You could also navigate to each widget's full report by clicking on the link at the bottom of each **Widget Details** popup panel.

<br/>

<img src="https://tw-cdn.katalon.com/katalon-testops/Home/Internal Env Widget Details Link Annotated.png" alt="The expanded report link from the Analytics & Trends Dashboard in Katalon TestOps." width="1080"/>

<p align="center"><em>The full report link at the lower left corner of each Widget Details popup panel is highlighted.</em></p>

<br/>

This feature eliminates the need for manual navigation to the Reports section by allowing you to access comprehensive testing details directly within the Analytics & Trends Dashboard interface. 

The expanded views centralize all necessary metrics in full detail within one location, streamlining your workflow and enabling informed decision-making without switching between application sections. 

---

<br/>

# About the Analytics & Trends Dashboard Components

This dashboard displays the following widgets:


**Test Execution Results Distribution**: View the distribution of test results across all statuses (Passed, Failed, etc.), including the total execution count and percentages in a pie chart.

<br/>

<img src="https://tw-cdn.katalon.com/katalon-testops/Home/Internal Env Test Execution Results Distribution Widget.png" alt="The Test Execution Results Distribution chart in Katalon TestOps." width="500"/>

<br/>
<br/>

**Test Execution Results Trend**: Track daily test execution results with a breakdown of passed, failed, error, incomplete, blocked, and skipped tests in a stacked bar chart.

<br/>

<img src="https://tw-cdn.katalon.com/katalon-testops/Home/Internal Env Test Execution Results Trend.png" alt="The Test Execution Results Trend chart in Katalon TestOps." width="500"/>

<br/>
<br/>

**Test Coverage by Configuration**: View test execution coverage across operating systems and browsers, showing the execution count for each.

<br/>

<img src="https://tw-cdn.katalon.com/katalon-testops/Home/Internal Env Test Coverage By Configuration.png" alt="The Test Coverage by Configuration chart in Katalon TestOps." width="500"/>

<br/>

**Defects Activity Trend**: Track the daily number of defects created (bar), closed (bar), and the accumulated number of open defects (line) over time in a combined line and bar chart.

<br/>

<img src="https://tw-cdn.katalon.com/katalon-testops/Home/Internal Env Defects Activity Trend.png" alt="The Defects Activity Trend chart in Katalon TestOps." width="500"/>

<br/>
<br/>

**Open Defects Distribution by Priority**: View the total count of open defects, categorized by priority levels (e.g. High, Medium, Low) in a pie chart.

<br/>

<img src="https://tw-cdn.katalon.com/katalon-testops/Home/Internal Env Open Defects Distribution by Priority.png" alt="The Open Defects Distribution by Priority chart in Katalon TestOps." width="500"/>

<br/>
<br/>

**Test Cases Publishing Activity**: Track the daily publishing activity of test cases. Shows the number of test cases in each publishing status (e.g., Draft, Review, Published) for all test cases created or edited within the selected time range in a stacked bar chart.

<br/>

<img src="https://tw-cdn.katalon.com/katalon-testops/Home/Internal Env Test Cases Publishing Activity.png" alt="The Test Cases Publishing Activity chart in Katalon TestOps." width="500"/>

<br/>

**Published Test Cases Distribution by Type**: View the distribution of published test cases, categorized by type (Manual only, Automated only, Manual & Automated) in a pie chart.

<br/>

<img src="https://tw-cdn.katalon.com/katalon-testops/Home/Internal Env Published Test Cases Distribution by Type.png" alt="The Published Test Cases Distribution by Type chart in Katalon TestOps." width="500"/>

<br/>

**Test Case Distribution by Execution Status**: View the distribution of test case across all execution statuses (Passed, Failed, etc.), including the total test case count and percentages in a pie chart.

<br/>

<img src="https://tw-cdn.katalon.com/katalon-testops/Home/Internal Env Test Case Distribution by Execution Status.png" alt="The Test Case Distribution by Execution Status chart in Katalon TestOps." width="500"/>

<br/>

## Edit the Analytics & Trends Dashboard

You can edit the Analytics & Trends Dashboard to customize the widgets and the layout.

1. Go to its **Settings** by clicking on the gear icon in the top right corner of the dashboard.

<br/>

<img src="https://tw-cdn.katalon.com/katalon-testops/Home/Internal Env Analytics and Trends Settings.png" alt="The Widget Settings button in Katalon TestOps." width="500"/>

<br/>

2. Click on **Edit dashboard**. The screen displays the widgets that you can add or remove from the dashboard.

<br/>

<img src="https://tw-cdn.katalon.com/katalon-testops/Home/Internal Env Edit Widgets Analytics and Trends.png" alt="The Edit Widgets button in Katalon TestOps." width="500"/>

<br/>

3. Drag a widget from the **Widget Library** to a free space in the editable dashboard. 

    Or to remove a widget, hover on it and click on the **Delete Widget** button represented by a trash icon.

4. Click on the **Save** button to apply the changes or click on **Discard Changes** and confirm the changes.

:::note
- You can click on **Settings > Use Katalon's Template** to reset the dashboard to its default layout.
:::

---

## Results 

A notification confirms that you have saved the changes. The widget is now added and visible in the dashboard.