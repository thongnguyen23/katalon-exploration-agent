---
title: Generate test cases with AI
---
<!-- PRD: https://katalon.atlassian.net/wiki/spaces/SG/pages/3878388438/PRD+-+AI+Test+Case+Generator+From+Requirement -->

Learn how you can turn your requirements into editable test cases with steps automatically. 

## Prerequisites

<!-- Reusable component import-->
import Reusable from '@site/src/components/reusable-content/testops/testlead-tester.mdx';

<Reusable />

- Make sure [AI features are enabled in your System Configuration](/katalon-platform/administer/administration-and-licensing-alternate/manage-systems/configurations/configure-ai-services#enable-or-disable-ai-features).

---

The AI-assisted test case generator transforms your testing processes by addressing key challenges in traditional test design approaches. You can significantly reduce test case creation time as the system automatically generates comprehensive test scenarios from requirements, eliminating the manual effort previously required for analysis and planning.

By automating repetitive test design tasks, your testing team can focus on higher-value activities like exploratory testing and defect analysis, enabling earlier test planning that shifts quality assurance left in your development lifecycle.

## View the Requirement Detail Page

1. Go to **Plans**.

2. Click on any of the Iterations. The **Requirement List** appears. 

<br/>

<img src="https://tw-cdn.katalon.com/katalon-testops/Execution/OrangeHRM Plans.png" alt="Plans page in Katalon TestOps" width="1080"/>

<br/>

3. Click on the name of any of the requirements to go to its **Requirement Detail Page**. 

    This shows you an overview of all your requirements' relevant information. In the example below, the requirement and its information is taken from  Jira issue RNGHRM-6. 

<br/>

<img src="https://tw-cdn.katalon.com/katalon-testops/Execution/OrangeHRM Requirement Details.png" alt="Requirement details page in Katalon TestOps" width="1080"/>

<br/>

:::tip  
You can click the **outbound arrow [↗]** to the left of **+ Create a test case** to navigate directly to the Jira/ADO work item, based on the project integration configured by your Project Administrator.
:::

## Generate Test Cases with AI

4. Click on the **Generate Test Cases** button in the upper right corner of the page.

    <br/>

    <img src="https://tw-cdn.katalon.com/katalon-testops/Execution/OrangeHRM Generate Test Cases Button.png" alt="Generate test cases button in Katalon TestOps" width="1080"/>

    <br/>

5. If TestOps finds your requirements need clarification, the **Additional Context Refinement** feature may ask you to provide additional context to make the test cases it generates more accurate. You can add custom prompts to focus on specific aspects of the test cases.

    <br/>

    <img src="https://tw-cdn.katalon.com/katalon-testops/Execution/OrangeHRM Additional Context Refinement.png" alt="Additional context refinement in Katalon TestOps" width="1080"/>
    
    <br/>

    Click on **Start Generating** after you have provided the additional context.

6. The system displays a list of AI-generated test cases highlighted in purple. These test cases are created based on your specified requirements.

    :::caution warning
     - Make sure to review the test cases' contents individually before approving them. The AI can make mistakes.
    :::
  
<br/>

<img src="https://tw-cdn.katalon.com/katalon-testops/Execution/Staging Generated Test Case Location Annotated.png" alt="Your Account information in Katalon TestOps" width="1080"/>
<p align="center"><em>A list of AI-generated test cases highlighted in purple while showing possible locations to save to.</em></p>

<br/>

7. You can choose the location to save the test case to as highlighted above. Click **Save All** to confirm the location or **Discard All** to discard the test cases.


8. To review a test case's content, click on the test case name. A drawer will pop up on the right side of the screen displaying test case details. Ensure that it aligns with the context of your general requirements before clicking **Save**. 

    Otherwise, you can click **Generate test steps** to regenerate the content, edit it all manually, or click **Discard** to discard the content.

<br/>

<img src="https://tw-cdn.katalon.com/katalon-testops/Execution/OrangeHM Generated Test Case Details.png" alt="Generated test case details in Katalon TestOps" width="1080"/>

<br/>

9. Click **Save** to approve the test case or **Discard** to discard it.



