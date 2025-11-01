---
title: Generate steps with AI
---
<!-- PRD: https://katalon.atlassian.net/wiki/spaces/SG/pages/3878388438/PRD+-+AI+Test+Case+Generator+From+Requirement -->

Learn how you can turn your Jira requirements into editable test cases with steps automatically. 

## Prerequisites

-  Make sure you have the Test Lead or Tester role. Go to [roles](/katalon-testops/administration-and-licensing/manage-systems/permissions/about-roles) or [permissions](/katalon-testops/administration-and-licensing/manage-systems/permissions/about-permissions) for more information or learn how to [assign a Project Admin here](/katalon-testops/administration-and-licensing/manage-administrators/assign-or-unassign-project-administrators).
- Connect [Jira to Katalon TestOps](/katalon-platform/integrations/jira-integration/enable-testops---jira-integration-for-test-management#task-3729).


---

The AI-assisted test case generator transforms your testing processes by addressing key challenges in traditional test design approaches. You can significantly reduce test case creation time as the system automatically generates comprehensive test scenarios from requirements, eliminating the manual effort previously required for analysis and planning.

By automating repetitive test design tasks, your testing team can focus on higher-value activities like exploratory testing and defect analysis, enabling earlier test planning that shifts quality assurance left in your development lifecycle.

## View the Requirement Detail Page

1. Go to **Plans**.

2. Click on any of the Iterations. The **Requirement List** appears. 

<br/>

<img src="https://tw-cdn.katalon.com/katalon-testops/Plans/Plans Page with Requirement List Drawer.png" alt="Your Account information in Katalon TestOps" width="1080"/>

<br/>

3. Click on the name of any of the requirements to go to its **Requirement Detail Page**. 

    This shows you an overview of all your requirements' relevant information. In the example below, the requirement and its information is taken from  Jira issue TO-7687. 

<br/>

<img src="https://tw-cdn.katalon.com/katalon-testops/Plans/Plans Requirement Detail Page.png" alt="Your Account information in Katalon TestOps" width="1080"/>

<br/>

:::tip  
You can click on the **outbound arrow [↗]** next to **+ Create a test case** to navigate directly to the Jira issue.
:::

## Generate Test Cases with AI

4. Click on the **Generate Test Cases** button in the upper right corner of the page.

    A list of generated test cases appears, highlighted in purple. The generated test cases are based on the given requirements.

    :::caution warning
    - Be careful when Accepting or Rejecting All; it's highly recommended you review each test case individually.
     - Make sure to review the test cases' contents before approving them. The AI can make mistakes.
    :::
  

<br/>

<img src="https://tw-cdn.katalon.com/katalon-testops/Plans/Plans Generated Test Cases From AI.png" alt="Your Account information in Katalon TestOps" width="1080"/>
<p align="center"><em>A list of AI-generated test cases highlighted in purple.</em></p>

<br/>

5. To review a test case, click on the test case name. A drawer will pop up on the right side of the screen detailing the test cases's generated content. Ensure that it aligns with the context of your general requirements before clicking **Accept**. 

    Otherwise, you can click **Generate test steps** to regenerate the content, edit it all manually, or click **Reject** to discard the content.

<br/>

<img src="https://tw-cdn.katalon.com/katalon-testops/Plans/Plans Test Case Details of AI Test Case.png" alt="Your Account information in Katalon TestOps" width="1080"/>

<br/>

6. Click **Accept** to approve the test case or **Reject** to discard it.

## Results

A notification confirms that you have successfully approved the test case(s). 

---

## Related topics

- You can also [create new test cases](/katalon-testops/create-and-organize-tests/create-and-manage-test-cases/create-new-test-cases) manually from within the Requirement Details page.
- You can also [link test cases to requirements](katalon-testops/create-and-organize-tests/create-and-manage-test-cases/edit-test-cases/about-linkages) to supplement the test coverage for your requirements.


