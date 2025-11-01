---
title: KRE - Session-Based License Reports
---

<!-- PRDs:
- https://katalon.atlassian.net/wiki/spaces/ADMIN/pages/3681124354/PRD+WIP+Session-Based+KRE+-+Session+Usage+Report
- https://katalon.atlassian.net/wiki/spaces/ADMIN/pages/3974135930/PRD+WIP+Session-Based+TestClould+-+Session+Usage+Report 
-->

Learn about Katalon Session-Based License Reports (KRE only) in Katalon TestOps.

## Prerequisites

* Make sure you are an Account Admin or possess the relevant permissions. Go to [roles](/katalon-testops/administration-and-licensing/manage-systems/permissions/about-roles) or [permissions](/katalon-testops/administration-and-licensing/manage-systems/permissions/about-permissions) for more information or learn how to [assign an Account Admin here](/katalon-testops/administration-and-licensing/manage-administrators/assign-or-unassign-account-administrators).

---

## Session-Based: KRE - License Usage

The Session-Based KRE (Katalon Runtime Engine) Usage Report provides you with comprehensive visualization of your session-based license utilization patterns over time. This interactive report helps you monitor execution resource usage, identify peak demand periods, and optimize license allocation to ensure testing operations run efficiently.

### Key Metrics

The report displays three critical measurements:

- **Available Sessions**: A step area chart showing the total number of KRE session licenses available to your organization during each time interval, using the most current data point for accuracy.

- **Peak Usage**: Bar chart representation of the maximum number of concurrent sessions utilizing KRE licenses during each measured interval, highlighting resource demand spikes.

- **Average Peak**: Dotted line curve showing the average peak usage across the time period, calculated differently based on your selected interval:
  - For monthly views: average daily peak usage

### Analysis Capabilities

You can customize your analysis using configurable filters:
- Organization selection (including hierarchical views)
- Date range parameters
- Time interval granularity

The report includes interactive elements such as hover tooltips that reveal detailed metrics for specific data points, helping you examine usage patterns without changing your view configuration.

### Actionable Insights

Use this report to:
- Monitor periods of high demand to prevent resource constraints
- Identify underutilization that indicates potential cost-saving opportunities
- Plan license allocation based on historical usage patterns
- Make data-driven decisions about future license procurement

The visualization highlights usage gaps and peak demand periods, enabling you to make informed decisions about resource distribution and optimization across your testing environments.

### View the Session-Based: KRE - License Usage Report

1. Go to **Admin Settings > Account > License Utilization**. You can find Admin Settings at the upper right corner of the page, indicated by a cog icon.

2. Click on the **KRE - License Usage** report; it is immediately visible.

3. Optional: Add filters to customize your view as needed. 

4. Optional: Hover over the chart to view detailed data points.

<br/>

<img src="https://tw-cdn.katalon.com/katalon-testops/Administration and Licensing/Manage Accounts/License Utilization/Session Based License Reports KRE License Usage.png" alt="Session-Based: KRE - License Usage" width="1080"/>

<br/>

---

## TestCloud - License Usage

The Session-Based TestCloud Usage Report provides you with detailed visibility into your TestCloud license utilization patterns. This interactive visualization helps you monitor session resource usage, identify demand patterns, and optimize your license allocation to ensure efficient testing operations.

## Key Metrics

The report displays three essential measurements:

- **Available Sessions**: A step area chart showing your total TestCloud session licenses available during each time interval, using the most current allocation data.

- **Peak Usage**: Bar chart displaying the maximum number of concurrent TestCloud sessions during each measured interval, revealing when your demand approaches capacity limits.

- **Average Peak**: Dotted line curve representing the average peak usage across time periods, calculated as:
  - Monthly view: Average of daily peak usage values

## Analysis Tools

You can refine your analysis using:
- Organization filters to focus on specific teams or projects
- Date range selectors to examine historical patterns or recent trends
- Time interval controls to adjust the granularity of your data view

Interactive tooltips reveal detailed metrics when you hover over data points, allowing you to examine specific usage information without changing your view configuration.

## Practical Applications

This report helps you:
- Identify periods when testing demand approaches your license limits
- Discover underutilized resources that could be reallocated
- Plan capacity based on historical usage patterns
- Make data-driven decisions about future license investments

The visualization highlights both usage gaps and demand spikes, enabling you to proactively manage your testing resources.

### View the TestCloud - License Usage Report

1. Go to **Admin Settings > Account > License Utilization**. You can find Admin Settings at the upper right corner of the page, indicated by a cog icon.

2. Click on the **TestCloud - License Usage** report; it is immediately visible.

3. Optional: Add filters to customize your view as needed. 

4. Optional: Hover over the chart to view detailed data points.

<br/>

<img src="https://tw-cdn.katalon.com/katalon-testops/Administration and Licensing/Manage Accounts/License Utilization/Session Based TestCloud License Usage.png" alt="Session-Based: TestCloud - License Usage" width="1080"/>

<br/>

---

