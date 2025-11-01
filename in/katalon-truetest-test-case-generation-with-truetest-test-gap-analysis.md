---
title: Test Gap Analysis
---

**Test Gap Analysis** feature in TrueTest allows you to discover how well your tests match actual user behavior. Test Gap Analysis helps you find and fix missing test coverage by highlighting which user actions in production are not tested yet. This makes it easy to spot uncovered flows and create tests for them, ensuring your tests are based on real user behavior.

## How it works

Test Gap Analysis works by comparing two user journey maps from different environments:

- **Primary User Journey Map**: typically represents the production environment, where real users interact with your application. This map shows actual usage patterns that you want to ensure are properly tested.
- **Secondary User Journey Map**: usually represents your testing environment, reflecting the user flows that have already been tested, often based on the latest application version.

**Key benefits**
- Give testers direct, actionable insight into real user behavior
- Filter out noise and focus only on untested flows that matter
- Automatically generate test cases to close the coverage gap
- Improve test efficiency and reduce the risk of escaped defects

## Use Test Gap Analysis

:::caution Prerequisites
- You already have at least 2 generated journey maps.
- The feature is applicable for maps that have the **Active** or **Archived** status.
:::

This section explain how to use the Test Gap Analysis feature. 
1. Navigate to **Test** > **Journey Maps** > and click **Analyze coverage gap**.
2. In the **Analyze Coverage Gap** dialog, choose a **Primary** and a **Secondary** map.
:::info
- To speed up gap analysis, TrueTest pre-generates results for common comparisons (between two **Active** maps or recent **Archived** maps). When these are selected, results display almost instantly after clicking Analyze.
- For older **Archived** maps, the analysis process may take longer, and you'll receive an email notification once results are ready.
:::
<img src="https://tw-cdn.katalon.com/truetest/test-gap-analysis/analyze-coverage-gap-dialog.png" alt="Analyze coverage gap dialog" width="500" />

3. Click **Analyze**. TrueTest will compare both maps and display the flows. 
    - **Orange paths and boxes** show actions and pages available in production but not covered in the testing environment (**Secondary** map).
    - The **Flows panel** on the left summarizes the uncovered user journeys. Use filters to focus on flows without test cases.
    - Click **Swap** to switch the **Primary** and **Secondary** maps if needed.

<img src="https://tw-cdn.katalon.com/truetest/test-gap-analysis/converage-gap-analysis.png" alt="Coverage gap analysis" width="800" /><br/>

4. Click the **Generate test cases** link in the **Coverage Gap** panel. This will take you directly to the **List View** with all uncovered flows selected automatically.
5. Review the selected flows, then click **+ Generate test cases**. TrueTest will create test cases accordingly.
    :::tip
    Check the **Estimated Remaining** section to see how much of your coverage gap still needs attention based on uncovered flows, pages, and actions.
    :::
<img src="https://tw-cdn.katalon.com/truetest/test-gap-analysis/select-uncovered-flows.png" alt="Select uncovered flows" width="800" />