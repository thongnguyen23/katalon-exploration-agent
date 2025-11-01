---
title: Create or manage test cases
---
import Reusable from '@site/src/components/reusable-content/testops/platform-permissions-project-admin.mdx';

Learn how to create an empty test case or how you can add more.

:::tip requirements
<Reusable />
:::

Learn how to create test cases and manage them.

## Create test case

1. Navigate to your **specific project's UI > Tests > Test Cases**.
2. Click on the **+ Create** button. Select **Test Case**.

<img src="https://tw-cdn.katalon.com/katalon-platform/create-tests/create-test-case1.png" alt="Create test case" width="500" />

3. Fill out the following information:
    1. Name (required): Input the label for your test case.
    2. Automation Status (required): Select the current stage of the test case in the automation lifecycle.
    3. Priority (required): Set the priority level (e.g., High, Medium, Low).
    4. Assignee (required): Select the person responsible for the test case.
    5. Feature areas (optional): Parts of the application this test covers.
    6. Test types (optional): Kind of testing (e.g., Functional, Regression).
    7. Description (optional): Input details about your test case.
    8. Precondition (optional): List the prerequisites for your test case.
    9. Location (required): Select where you want to save your test case.
4. Click **Create**.

<img src="https://tw-cdn.katalon.com/katalon-platform/create-tests/fields.png" alt="Creat test fields dialog" width="500" />

- Alternatively, click on **"Save & Create Another"** to immediately input information for an additional test case without navigating away from the current screen.

### Manage test cases

To manage an individual test case:

1. Click on its name to open the **Test Case Detail** page.
2. Use the action buttons in the upper right:
    1. Move – Move the test case to a different location.
    2. Duplicate – Create a copy in the same location.
    3. Delete – Remove the test case from your repository (its result history is retained).

<img src="https://tw-cdn.katalon.com/katalon-testops/Tests/Test%20Cases/Test%20Case%20Detail%20Page%20Manage%20Annotated.png" alt="Manage test cases" />

### Manage test steps

Within a test case, you can define and manage individual test steps using the following fields:

- **Description**: Specify the action to perform.
- **Expected Results**: Define the criteria for success based on the action's outcome.
- **Test Data**: Provide any data needed for the step.

To add or edit test steps:

1. Click **+ New Step** to create a test step and fill in the required details.
2. To modify an existing step, click the step number and choose an option from the pop-up menu to:
    - **Duplicate** the test step
    - **Insert above**
    - **Insert below**
    - **Delete** the test step
3. All changes are saved automatically.

    <video width="800" controls>
    <source src="https://tw-cdn.katalon.com/katalon-platform/create-tests/edit-test-steps.mov" type="video/mp4" />
    </video>

## Import test cases

:::info Things to Know Before Importing Test Cases:
- **Names and paths must start with:**
    Lowercase letters (a–z), numbers (1–9), or an underscore (_)
- **Allowed characters within names and paths:**
    Parentheses (), commas ,, periods ., hyphens -, and underscores _
- **Please avoid the following:**
    - Using .. (double periods) anywhere in the name or path
    - Ending a test case name with a period (.)
- We also recommend splitting your import file into **smaller batches** (around 500 test cases per file).
:::

You can import test cases from a CSV file into Katalon TestOps. During import, all CSV values are automatically mapped to their corresponding TestOps fields, including any **requirements linkages** from your configured ALM integrations (e.g., Jira or Azure DevOps).

1. Navigate to your **specific project's UI > Tests > Test Cases**.
2. Click the **+ Create** button, then choose **Import Test Cases**.

<img src="https://tw-cdn.katalon.com/katalon-platform/create-tests/create-test-case1.png" alt="Create test case" width="500"/>

3. Upload your CSV file from your device and click **Next**.
4. TestOps will automatically map each field in your CSV file to a corresponding TestOps field. You can adjust these mappings if needed.
5. Review the mapped fields in the preview. When you're ready, click **Import**.

    <video width="800" controls>
    <source src="https://tw-cdn.katalon.com/katalon-platform/create-tests/import-test.mov" type="video/mp4" />
    </video>
## Linkages

In TestOps, **Linkages** let you associate a test case with requirements from your ALM tools (like Jira or Azure DevOps), or with other test cases. This ensures clear traceability between requirements and what’s being tested—visible directly within each test case.

Currently, you can link a test case to:

- **Requirements**
- Other **Test Cases**
- **Defects**
- **ADO Test Cases**

<img src="https://tw-cdn.katalon.com/katalon-platform/create-tests/linkages1.png" alt="Linkages UI"/>

### Import linkages
:::info
To link **Requirements**, **Defects**, **ADO Test Cases**, make sure you’ve configured an ALM integration, such as, [Jira](katalon-platform/integrations/alm-and-test-management/jira-integration) or [Azure DevOps (ADO)](/katalon-platform/create-tests/katalon-platform/integrations/alm-and-test-management/azure-devops-integration).
:::
When importing test cases from a CSV file, you can include a column that links each test case to a requirement in your ALM tool. If a cell is left blank, that test case won’t be linked to any requirement.

For example, if your ALM has an issue called DEF-60, and your imported CSV file includes a column that lists DEF-60 for a test case:

<img src="https://tw-cdn.katalon.com/katalon-platform/create-tests/import-highlight1.png" alt="Example Excel sheet" width="700" />

**Result**

TestOps will automatically link the imported test case to the corresponding issue.

In this case, the Verify Resources Page test case will be automatically linked to the issue **DEF-60**.

    <video width="800" controls>
    <source src="https://tw-cdn.katalon.com/katalon-platform/create-tests/view-linked-issue.mov" type="video/mp4" />
    </video>
### Manage linkages

After importing or creating test cases, you can update their requirement linkages at any time to reflect changes or correct mappings.

1. Open the test case you want to update.
2. In the test case detail view, go to the **Linkages** panel.
3. You can do the following:
    - To add a linkage, click Click to link .... Then search for and select the requirement(s) from your connected ALM tool.
    - To remove a linkage, click the Unlink icon next to the linked issue. Changes are applied automatically.
4. Click **Link** to apply your changes.

    <video width="800" controls>
    <source src="https://tw-cdn.katalon.com/katalon-platform/create-tests/edit-linkages1.mov" type="video/mp4" />
    </video>