---
title: Create or manage test steps
---

Learn how you can create and manage test steps within a manual test case. 

## Prerequisites

- You have created a test case. See [Create new test cases](/katalon-testops/create-and-organize-tests/create-and-manage-test-cases/create-new-test-cases).

<!-- Reusable component import-->
import Reusable from '@site/src/components/reusable-content/testops/platform-permissions-project-admin.mdx';

<Reusable />

---

## Add or manage test steps

1. Go to **Tests** > **Test Cases** in the sidebar. The repository page appears.
2. Click on the name of the test case you would like to add steps to.
    
    The test case's details appear. It is automatically tagged as **Manual**.

    <img src="https://tw-cdn.katalon.com/katalon-testops/Tests/Test Cases/Test Case Detail Page.png" alt="Test case detail page in Katalon TestOps" width="1080"/>
    <p align="center"><em>Sample of a test case detail page.</em></p>

    <br/>

3. Optionally, input customization data into the following fields:
   - Select the working status. It is set to **Draft** by default.
   - Input a test case description.
   - Input pre-conditions or requirements that must be met before the test case is executed.
4. Scroll down to the **Steps** section and type or paste your steps in as follows:
   - **Description**: Detail the action that needs to be done.
   - **Expected results**: Define the success criteria based on the result of the action.
   - **Test Data**: Optionally input additional information about the step.

<br/> 

:::note 
- You can copy the test steps from a spreadsheet and paste directly to the section.
- CTRL+Z or CMD+Z to undo an action up to 20 times.
- A cell can fit multiple lines of wrapped text.
:::

<br/>

5. You can further edit your test steps directly by clicking on the test steps' numbers and selecting any of the following functions from the pop-up menu:

    <br/>

    <img src="https://tw-cdn.katalon.com/katalon-testops/Tests/Test Cases/Test Case Test Step Detail Popup.png" alt="Edit test case steps in Katalon TestOps" width="500"/>

    <br/>
    <br/>

   - **Duplicate**: Duplicate one or multiple steps.
   - **Insert above**: Inserts a step above.
   - **Insert below**: Inserts a step below.
   - **Delete**: Delete one or multiple steps.

## Result

You have created or edited a manual test case's steps. 
