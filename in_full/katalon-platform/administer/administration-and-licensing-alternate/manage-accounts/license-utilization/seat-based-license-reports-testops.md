---
title: TestOps - Seat-Based License Reports
---

Learn about TestOps license utilization reports (seat-based) in Katalon TestOps.

:::tip requirements
You must be assigned the **Account Admin** role to view the following reports. Learn more about [roles](/katalon-platform/administer/administration-and-licensing-alternate/manage-systems/permissions/about-roles) and [permissions](/katalon-platform/administer/administration-and-licensing-alternate/manage-systems/permissions/about-permissions) or how to [assign an Account Admin here](/katalon-platform/administer/administration-and-licensing-alternate/manage-administrators/assign-or-unassign-account-administrators).
:::
---

## Seat-Based: TestOps - License Assignment and Activation History

The TestOps License Assignment and Activation History chart provides a comprehensive visualization of license allocation and user activation trends across your Account or Organization. This feature helps you monitor license utilization, identify usage patterns, and optimize resource allocation based on actual needs.

### Key Metrics Tracked
The chart displays three critical metrics over your selected timeframe:

- **Purchased**: Total licenses allocated to the selected organization. At the account level, this represents your total license purchases.
- **Assigned**: Total licenses distributed to users within the parent level and all child organizations.
- **Activated**: Total users who actively engaged with the system during the selected period (measured by login events or usage triggers).

:::note
- In the case of multiple reassignments or purchases during the selected timeframe, the last record will be displayed.
:::

### Analysis Capabilities
You can customize your view using configurable filters:

- Account or Organization 
- Date range 
- Time interval

These filters allow you to focus your analysis on specific organizational segments or timeframes relevant to your management needs.

### Actionable Insights
The visualization highlights:

- Usage gaps between purchased and assigned licenses
- Underutilization patterns where licenses are assigned but not activated
- Peak demand periods requiring additional resources

Interactive elements, such as hover tooltips, provide detailed data points for specific dates or metrics, enabling deeper analysis without changing views.

Use these insights to make informed decisions about license redistribution, procurement planning, and resource optimization across your organization.

### View the Seat-Based: TestOps - License Assignment and Activation History Report

1. Go to **Admin Settings > Account > License Utilization**. You can find Admin Settings at the upper right corner of the page, indicated by a cog icon.

2. Click on the **TestOps - License Assignment and Activation History** report; it is immediately visible.

3. Optional: Add filters to customize your view as needed. 

4. Optional: Hover over the chart to view detailed data points.

<br/>

<img src="https://tw-cdn.katalon.com/katalon-platform/admin/license-ultilization/testops-license-assignment-chart.png" alt="Seat-Based: TestOps - License Assignment and Activation History" width="1080"/>

<br/>

:::info Additional Information
- **User Activation** counts users who have logged in at least once after license assignment. Once activated, a user remains counted in all subsequent reporting periods, regardless of future login activity. This cumulative metric persists until license revocation or reassignment, providing an accurate view of your total activated user base over time.
- Whenever a user is unassigned from a license it resets the count of both assignment and activation.
:::

<br/>

---

## Seat-Based: TestOps - License Assignment Details

The TestOps - Assignment Details table provides you a detailed visibility into individual license assignments and usage activity across your organization. This interactive table lets you track license utilization at a granular level, identify inactive users, and make data-driven decisions about license allocation.

### Key Capabilities

The table gives you comprehensive control through several core functions:

- **Detailed License Monitoring**: View complete information about each license including assignment date, activation status, and license source.

- **Advanced Filtering Options**: Filter your license data by Organization, license source, user name, or email.

- **Flexible Data Export**: Export your filtered dataset to CSV format for offline analysis, reporting, or integration with other management tools.

Use this table to identify underutilized licenses, track user activity patterns, and optimize your license distribution based on actual usage data. The granular visibility helps you ensure compliant and cost-effective resource allocation across your organization.

### View the TestOps - License Assignment Details Table

1. Go to **Admin Settings > Account > License Utilization**. You can find Admin Settings at the upper right corner of the page, indicated by a cog icon.

2. Click on the **TestOps - License Assignment Details** report; it is immediately visible.

3. Optional: Add filters to customize your view as needed or click on **Reset Filters** to clear all filters and restore the default view.

4. Optional: Click on the **Export** button to export the data to a CSV file.

5. Optional: Click on a user to view their entire [User Detail Page](/katalon-testops/administration-and-licensing/manage-organizations/user-management/about-the-user-detail-page), giving you an overview of that user's specific information within TestOps.

<br/>

<img src="https://tw-cdn.katalon.com/katalon-platform/admin/license-ultilization/testops-assignment.png" alt="Seat-Based: TestOps - License Assignment Details Table" width="1080"/>

<br/>

### About the TestOps - Assignment Details Table

A detailed breakdown of its components is as follows:

- **User**: Full name of the user (e.g., John Smith).

- **Email**: Associated email address (e.g., johnsmith@sample.com).

- **License Source**: Organization or account where the license originates.

- **Organization**: Hierarchical Organization name to which the user belongs.

- **TestOps Project**: Associated Project for the user.

- **Last Assignment**: Most recent date when the license was assigned.

- **Last Active Use**: Most recent date when the license was actively used by the user.

----

## Seat-Based: TestOps - License Usage

The License Usage Chart provides you with an interactive visualization of license usage patterns across your Account or Organization over time. This feature helps you monitor allocation efficiency, track user engagement, and identify opportunities for license optimization.

### Key Capabilities

You can use this chart to:

- Visualize license assignment and user activity metrics on a timeline
- Track usage patterns across different organizational units
- Identify periods of underutilization or peak demand
- Compare actual usage against allocated resources

### Analysis Options

The interface allows you to customize your analysis with filtering options for:

- Organization selection 
- Date range 
- Time interval 

Each data point provides detailed information through interactive tooltips when hovering, enabling you to examine specific dates or trends without changing your view.

### Decision Support

The visualization helps you make informed decisions about license management by:

- Highlighting discrepancies between assigned licenses and active usage
- Identifying organizational units with underutilized resources
- Showing activation patterns that may indicate adoption issues
- Tracking usage trends that can inform future license procurement

You can use these insights to optimize license distribution, plan for upcoming needs, and ensure efficient resource allocation across your organization.

### View the TestOps - License Usage Report

1. Go to **Admin Settings > Account > License Utilization**. You can find Admin Settings at the upper right corner of the page, indicated by a cog icon.

2. Click on the **TestOps - License Usage** report; it is immediately visible.

3. Optional: Add filters to customize your view as needed. 

4. Optional: Hover over the chart to view detailed data points.

<br/>

<img src="https://tw-cdn.katalon.com/katalon-platform/admin/license-ultilization/testops-license-usage.png" alt="Seat-Based: TestOps - License Usage" width="1080"/>

<br/>

:::info Additional Information
- **About activity**: The count represents unique users who perform any system action during a 24-hour period. Users count only once per day regardless of activity volume, and all counts reset at midnight. This provides a precise measure of daily system engagement.
:::

<br/>

---
