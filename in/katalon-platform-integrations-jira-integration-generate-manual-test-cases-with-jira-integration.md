---
title: Generate manual test cases with Jira integration (Legacy)
---
import Reusable from '@site/src/reusable/Reusable.mdx';

<Reusable />

Generate manual test cases in Jira using the Katalon Manual Test Cases Generator.

## Requirements
1. **Install Katalon - Test Automation for Jira plugin** from the Atlassian Marketplace to enable test case generation in Jira.

2. **Enable Jira Integration in TestOps**: 
- This activates the Save to Katalon button and enables syncing between Jira and Katalon TestOps.
- Test cases generated and saved to TestOps are automatically linked to their corresponding Jira requirements.
---- 
Katalon Manual Test Cases Generator uses GPT technology to automatically generate structured, detailed test cases from natural language input. This streamlines the process, improves efficiency, and reduces manual effort.
1.  Create a Jira Ticket
- Enter test case name, description, and relevant details.
- Make sure the title and description clearly explain the test’s purpose and steps. This helps GPT generate accurate and structured test steps.

2. Click **Katalon manual test cases** from the actions menu:
<img src="https://docs.katalon.com/43eeb790-faeb-11ed-878a-0242c7a41fd4/TO_Jira_NLP_Manual_Test_Case_Generator_app.png" width="700" alt="Click Katalon manual test cases"/>

3. Then click **Generate manual test cases**. This will process your input and automatically generate the test steps based on the provided instructions (may take 3–5 minutes to process).

<img src="https://docs.katalon.com/43fe6f00-faeb-11ed-878a-0242c7a41fd4/TO_Jira_click_generate_manual_test_cases.png" width="500" alt="Click Generate manual test cases"/>

4. Review the generated test steps.

- If unsatisfied, click **Clear**, update the Jira ticket, and click the **Generate Manual Test Cases** button again.
- Once satisfied, click **Save to Katalon** to store the test case in TestOps.

<img src="https://docs.katalon.com/447573c0-faeb-11ed-878a-0242c7a41fd4/TO_JIra_save_NLP_generated_test_cases_to_Katalon.png" width="500"  alt="Review the generated test steps"/>

#### Result
Your GPT-generated manual test cases are saved to Jira and Katalon TestOps: 

<img src="https://docs.katalon.com/43cb02f0-faeb-11ed-878a-0242c7a41fd4/TO_Jira_saved_NLP_test_cases.png" width="500" alt="GPT-generated manual test cases are saved to Jira and Katalon TestOps" />


## View linked generated manual test cases in Jira
After you save your generated manual test cases to the Katalon TestOps, your generated manual test cases are automatically linked to your Jira issue, to view:

1. Navigate to the Katalon TestOps section in the bottom-right of your Jira issue.
2. You'll see the number of linked test cases. Click it to open a modal showing:
- Linked Test Cases
- Katalon Platform Test Results
- Katalon Studio Test Results

<img src="https://docs.katalon.com/43b09d20-faeb-11ed-878a-0242c7a41fd4/TO_Jira_Katalon_integration_linked_manual_test_cases.png" alt="View linked test cases of your Jira issue." width="700" />

3. To view the detail of a specific test case in TestOps, hover over it and click **View detail**.

<img src="https://docs.katalon.com/4456a120-faeb-11ed-878a-0242c7a41fd4/TO_Jira_Katalon_view_linked_test_cases.png" alt="View Linked Test Cases" width="700" />

## View saved NLP-generated manual test cases in the Katalon TestOps
After you save your NLP-generated manual test case in Jira, the manual test case is also saved in the Katalon Platform. 
Go to **Test Explorer**, under `Uploaded Data/test-cases/manual`.

<img src="https://docs.katalon.com/d6933820-f54e-11ed-878a-0242c7a41fd4/TO_Jira_NLP_generated_test_case_location.png" width="700" alt="View saved NLP-generated manual test cases"/>

Each test case is organized by:
- Jira Issue ID
- Save Date

Example folder structure: `Uploaded Data/test-cases/manual/<Jira-issue-ID>/<Saved-date>`

## View linked Jira requirements
To view the linked Jira requirements of an NLP-generated manual test case in Katalon TestOps:

1. Open the GPT-generated test case in Katalon TestOps.
2. Scroll down to the Linked issue section.

<img src="https://docs.katalon.com/d6955b00-f54e-11ed-878a-0242c7a41fd4/TO_Jira_NLP_generated_test_case_details.png" width="700" alt="View linked Jira requirements"/>

## Edit the test steps of your NLP-generated test case
To prevent duplication or unnecessary regeneration in Jira, we recommend editing test cases directly in Katalon TestOps.

1. Go to test case you want to edit in Katalon TestOps.
2. Hover over the test case field and click to open it
3. Update the test steps as needed.
4. Click **Save** to apply your changes.

<img src="https://tw-cdn.katalon.com/katalon-platform/integration/edit-test-case_to.gif" width="600" alt="Edit the test steps of your NLP-generated test case"/>

<!-- Edit NLP-generated test case. -->

