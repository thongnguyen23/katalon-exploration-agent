---
title: Set custom session attributes
---

While TrueTest captures user interaction data on an AUT, this data is often generic and lacks the business-specific context teams need, such as user roles, feature flags, experiment groups, or user IDs.

To improve the relevance and accuracy of generated test cases, TrueTest allows users to inject custom attributes into a user session. These attributes are attached to the session metadata and stored alongside interaction data in TrueTest.

## Use cases

A few use cases where you can leverage this feature are:

- User role-based testing: Sessions are tagged with `userRole: admin`, `userRole: viewer`, etc. Testers generate separate test cases for different roles to ensure coverage of role-specific behavior or access controls.
- User-level debugging: Sessions are tagged with `userId: 87654`. QA can quickly isolate and analyze issues reported by specific users, then generate a test case that replicates the exact path they took.
- A/B experiment validation: Sessions are labeled with `experimentGroup: A` or `experimentGroup: B`. QA filters by group to generate tests tailored to each variation and ensure both versions are functionally covered.

This document shows you how to set up custom session attributes and use them in your generated user sessions.

## Installation

Add the following snippet to your HTML `<head>`. Replace with your own client code in the `client-code` field.

```jsx
<script defer async client-code="KA-2477-2" src="https://static.katalon.com/libs/traffic-agent/v1/traffic-agent.min.js"></script>
<script src="https://static.katalon.com/libs/traffic-agent/v1/truetest-sdk.min.js"></script>
```

## Set custom attributes

Follow this template to inject attributes via JavaScript.

```jsx
TrueTest.setSessionAttributes({
  userRole: "admin", 
  experimentGroup: "B",
  userId: "user_1234",
});
```

:::note
- Only **key-value pairs** are supported.
- Each **key can have only one value** per session. Arrays or lists of values are not supported.
- If a key is set multiple times, only the **last value is retained**.
:::

## Generate map with custom attributes filter

1. When creating a new user journey map, define queries in the **Filter by user session attributes** field to target specific sessions based on your custom attributes. 

<img width="500" alt="Generate map with attributes filter" src="https://tw-cdn.katalon.com/truetest/custom-session-attributes/generate-map-with-attribute-filter.png" />

- You can combine multiple conditions using `AND`/`OR`.
- Example query:

```jsx
userRole = 'admin' AND experimentGroup = 'B'
```

2. After you generated the journey map, you can filter the user flows with predefined attributes of the related user sessions.
<img width="800" alt="Filter by attributes" src="https://tw-cdn.katalon.com/truetest/custom-session-attributes/truetest-filter-by-attributes.png" /> 

Click the **View test steps** button to view custom attributes for each flow if they are available.
<img width="800" alt="View session attributes in Flow view" src="https://tw-cdn.katalon.com/truetest/custom-session-attributes/truetest-view-session-attributes-in-flow-view.png" />

## Known limitations

- **Data transmission**: Custom attributes collected by the agent will be sent as per individual request. Performance optimization through request bundling will be planned for a future version.
- **Data privacy**: By default, TrueTest does not store or retain any sensitive information. All test case generation filters out sensitive data automatically. However, if you manually add them via custom attributes, those attributes will be stored as entered. We recommend avoiding the use of sensitive data in custom attributes.
- **Conditional Test Generation**: Currently, custom attributes can only be used for capturing and filtering sessions, not for analytics or conditional test generation.
- **Delayed “No Data” Error**: In some cases, when you generate a map with a custom attribute filter, they have to wait, only to get a "no data" error message later. This happens because we first download all sessions in the time range, *then* check if they match the attribute filter, instead of validating everything at once.