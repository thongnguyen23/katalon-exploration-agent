---
title: Configure TrueTest Agent
---

This document shows you how to set up TrueTest Agent for test case generation with TrueTest.

### Prerequisites

- You have an active TrueTest license or trial.
- You have enabled AI features for your Organization. See [Configure AI services](/katalon-platform/administer/administration-and-licensing-alternate/manage-systems/configurations/configure-ai-services).
- You have configured Github integration at the **Account level** and **Project level**. For detail instructions, refer to [Github integration](/katalon-platform/integrations/repository/github-integration).

## Configure TrueTest Agent to track data

:::caution Prerequisites
- You must be the Account Admin or System Admin of your Account.
:::

### Add application under test

First, you need to define an application under test (AUT). The AUT specifies the production environment where TrueTest can track all user interactions and leverage them in generating flows.
1. Go to **Admin Settings** > **System Configurations**.
2. Switch to the **Application Under Test** tab.
    <img width="800" src="https://tw-cdn.katalon.com/truetest/configure-truetest-gen3/create-an-aut.png" alt="Create an AUT" />
3. Click the **+ Create AUT button** to open the below page. Provide the information of your AUT following the instruction.
    <img width="800" src="https://tw-cdn.katalon.com/truetest/configure-truetest-gen3/create-new-aut-page.png" alt="Create new AUT page" />
4. When you’re done, click **Create**.
5. From the AUT list, select the (🖊️) of the newly created AUT to configure. 
6. In the **TrueTest AUT Detail** page, check the **Enable for TrueTest** checkbox and **Save** your settings.
    <img width="800" src="https://tw-cdn.katalon.com/truetest/configure-truetest-gen3/truetest-aut-detail-page.png" alt="TrueTest AUT Detail page" />
#### Result
After enabling the AUT for TrueTest, additional fields will appear to configure both the data tracking and test execution environments.

### Configure environment(s)

<img width="1080" src="https://tw-cdn.katalon.com/truetest/configure-truetest-gen3/add-truetest-environment.png" alt="TrueTest AUT Detail page" /> <br/>

#### Add Data Tracking Environment

TrueTest generates journey maps based on tracked data from specific environments. This setup enables you to analyze user behavior and generate test cases that reflect real-world usage patterns. <br/>
For each AUT, you can configure multiple data tracking environments. Data from each environment is kept separate and used to build environment-specific journey maps.

1. Click **+ Add Environment** to create a new one.
2. In the **Create Environment** dialog, provide a name and URL. A valid URL syntax will be `https://qe.your-app.com`.
    <img width="400" src="https://tw-cdn.katalon.com/truetest/configure-truetest-gen3/create-DTE.png" alt="Create data tracking environment" />
3. Check the **Data Tracking Environment** checkbox. 
    1. **(Optional)** If you want to define additional domain patterns, input them into the **Additional Domains**  field. For example, valid domains can be `*.katalon.com` or `katalon.com`.
4. Select an **Environment Label** (e.g., Production, QA, Staging).
5. Click **Create** to save your configuration.

---
#### Add Test Execution Environment

To execute generated test cases using traffic collected from the production site, the TrueTest Agent requires a **Test Execution Environment** - where a generated test case will execute. Additionally, you will need to provide a login script within the test environment if the AUT requires login when executing a test case. This will assist TrueTest in injecting authentication steps into generated test scripts.

1. Click **+** **Add Environment** again to open a new **Create Environment** dialog.
2. Enter the **name** and the **URL** for the environment. You can only enter one URL.
3. Check the **Test Execution Environment** checkbox.
    <img width="500" src="https://tw-cdn.katalon.com/truetest/configure-truetest-gen3/add-TEE.png" alt="Add execution environment" />
    :::note
    The **first test execution environment** created is automatically set as the **default test execution environment** (this cannot be changed).
    :::
4. Select an **Environment Label** (e.g., Production, QA, Staging).
5. Choose a **login method** between **No Authentication** and **Others** (for custom login script).
6. Click **Create** to save your setup.

### Install TrueTest snippet
A developer or someone with access to the codebase of the AUT must add the tracking code snippet provided by Katalon. The code snippet should be pasted into the `<HEAD>` element of the HTML code of the AUT. Once the code snippet is added, the AUT should be saved, built, and deployed to the production environment.

TrueTest also provides the option to install with Google Tag Manager.

Here are two options to install the code snippet:

- Install the code snippet manually. In the **Install your TrueTest** snippet section, copy the displayed code snippet and paste into the `<HEAD>` element of your application under test.
    <img src="https://tw-cdn.katalon.com/truetest/configure-truetest-gen3/install-truetest-snippet-g3.png" alt="install true test snippet code" />

    ```jsx
    <!DOCTYPE html>
    <html>
    <head>
        <!-- Paste the TrueTest code snippet here -->
    </head>
    <body></body>
    </html>
    ```
    
- If you've already implemented Google Tag Manager as the tag management system, you can dynamically set up code snippet.
    1. Log in to [Google Tag Manager](https://tagmanager.google.com/).
    2. In the container that is connected to the application under test, create a new tag.
    3. Name and edit the tag. Here we define a custom HTML tag.
    <img src="https://docs.katalon.com/52e4c500-5ce3-11ee-bc71-0242c7a41fd4/ATG_Google_Tag_Manager_add_tag.png" alt="GTM - Add custom HTML tag" /> <br/>
    4. Paste the provided snippet into HTML block. Here, the `CLIENT-CODE` is the code displayed in the configuration UI.
    <img src="https://docs.katalon.com/5316f890-5ce3-11ee-bc71-0242c7a41fd4/ATG_Google_Tag_Manager_paste_code_snippet.png" alt="GTM - paste code snippet" /> <br/>
    5. Add a triggering event and select the **All pages** trigger to ensure that the TrueTest code snippet is enabled on all pages where the GTM is enabled.
    <img src="https://docs.katalon.com/5300ff90-5ce3-11ee-bc71-0242c7a41fd4/ATG_Google_Tag_Manager_add_trigger.png" alt="GTM - add trigger" /> 

#### Result
Once saved, the TrueTest tracking snippet will be added to the HTML header when a user accesses the application. To ensure that the Agent works properly, open the browser's **Developer Tools** > **Network** tab and filter for `KA-****`. Try clicking some buttons and links. If the network activity is being sent to our server, the Agent is working.
<img width="400" src="https://tw-cdn.katalon.com/truetest/truetest-verify-agent-function.png" alt="Verify TrueTest Agent functionality" />


### Assign TrueTest license to a TrueTest AUT

:::caution Prerequisites
- You must be the Account Admin of your Account.
:::

In order to use TrueTest with your AUT, you need to assign the TrueTest license to the targeted AUT.

1. Go to **Admin Settings** at the upper right corner of the page.
2. Click **Account > License Management**.
3. Switch to the **TrueTest** tab.
4. Click the **+ Assign TrueTest AUT** button.
    <img width="1080" src="https://tw-cdn.katalon.com/truetest/configure-truetest-gen3/truetest-assign-aut-license.png" alt="Assign AUT license" />

5. In the dialog, select the checkbox of the AUT you want to assign the license to. Then, check the acknowledge checkbox and click **Assign**.
    <img width="500" src="https://tw-cdn.katalon.com/truetest/configure-truetest-gen3/assign-truetest-aut-dialog.png" alt="Assign AUT license dialog" />

#### Result
You have assigned a TrueTest license to an AUT.
Once all configurations above are complete, the TrueTest Agent can begin tracking data. When data is successfully received, the status of the AUT will automatically change from `INACTIVE` to `ACTIVE`.


### Associate the AUT to a project

:::caution Prerequisites
- You must be the Project Admin of your Project.
- You have completed all the configuration steps before this one.
- You have granted the Write permission for the Git repository integrated with TestOps. See the following documents: 
  - GitHub personal access token: you need to provide the `repo:status` scope. See: [GitHub available scope](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/scopes-for-oauth-apps#available-scopes).
  - GitLab personal access token: you need to assign the `write_repository` scope. See: [GitLab personal access token scopes](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html#personal-access-token-scopes).
  - Atlassian Bitbucket Repository Access Token: you need to provide the `repository:write` permission. See: [Bitbucket Repository Access Token permissions](https://support.atlassian.com/bitbucket-cloud/docs/repository-access-token-permissions/).
  - Azure DevOps access token: you need to provide the `vso.code_write` scope. See: [Azure DevOps access token scopes](https://learn.microsoft.com/en-us/azure/devops/integrate/get-started/authentication/oauth?view=azure-devops#scopes).
  - AWS CodeCommit Git credentials: you need to create an IAM policy with write access to repository. See: [AWS managed policies for CodeCommit](https://docs.aws.amazon.com/codecommit/latest/userguide/security-iam-awsmanpol.html).
:::

Once test cases are generated, TrueTest needs to store the tests in a repository.
> You can associate an AUT to only one project. Should you want to change the AUT, please contact TrueTest support team for assistance.

1. Integrate your preferred Git repository with TestOps following these guides:
   - [Github](/katalon-platform/integrations/repository/github-integration)
   - [GitLab](/katalon-platform/integrations/repository/gitlab-integration)
   - [Bitbucket](/katalon-platform/integrations/repository/bitbucket-integration)
   - [Azure DevOps](/katalon-platform/integrations/repository/azure-repos-integration)
2. In your project, navigate to **Settings** > **Configurations** > **Application Under Test**. 
3. Click **+ Associate AUT** to open the **Associate AUT** dialog.

<img src="https://tw-cdn.katalon.com/truetest/configure-truetest-gen3/associate-aut-with-project.png" width="1080" alt="Select Associate AUT" />

3. Select the recently created AUT from the AUT list and click **Associate**.

<img src="https://tw-cdn.katalon.com/truetest/configure-truetest-gen3/associate-aut-dialog.png" width="500" alt="Associate AUT dialog" />

4. Click the (🖊️) of the recently associated AUT.
5. Scroll to the **TrueTest Settings** section. In the **Repository** dropdown, select the integrated Git repo or Katalon Cloud. <br/>
    You can select to commit and push the test artifacts to a script repository, which can then be executed as Katalon test scripts. You can associate the same AUT with multiple projects individually as long as you are a member of those projects. If you use a private network and cannot integrate with a Git repository, you can select Katalon Cloud to store the test artifacts.

<img src="https://tw-cdn.katalon.com/truetest/configure-truetest-gen3/select-repository-for-aut.png" width="600" alt="Select repository for AUT" />

<details>

 <summary>**Advanced settings**</summary>
    
The advanced settings allow you to further customize the behavior of TrueTest Agent while generating test cases for your AUT.
- **Default Selection Method**: You can specify the main selection method that Katalon Studio should use when running the generated test cases.
- **Test Data**: This setting allows TrueTest to bind default values or values in data file in generated test cases. If you select the **Default** option, go to the **Variables** tab > **Default value** column to update the values. If the **Data Column** option is selected, go to **Data Files** > **AI-Generated** folder and import the data file to Excel. Each column is a variable's name and you can add data to each row.
- **Minimum Number Steps**: When collecting data among multiple user flows, TrueTest can detect which group of steps are common across the flows and organize these steps into common functions. For example, in the checkout flow of an online shopping website, users may need to fill in billing addresses, shipping addresses, payment information, etc. These steps can be organized into a function. Specify the minimum number of steps that TrueTest can include in a function.

</details>

#### Result
Once this configuration is complete, Journey Map features will become available for the project.

### Data privacy configuration (optional)
TrueTest has a filtering mechanism to exclude sensitive information from user's application under test, see: [Protect user data privacy](/katalon-platform/create-tests/test-case-generation-with-truetest/protect-user-data-privacy).

Additionally, users have the option to manually specify which fields or elements should be excluded while TrueTest is collecting data. To do so, simply add CSS class `katalon-excluded` to the UI elements that you do not want their values to be captured.

<img src="https://docs.katalon.com/9a3df510-7300-11ee-9132-0242c7a41fd4/TrueTest_katalon_excluded_examples.png" alt="katalon-excluded examples" />

## Known limitations
- AUTs with TrueTest enabled cannot be deleted. This helps prevent users from deleting the AUT and being unable to recover the purchased license. Should you need to delete an AUT with TrueTest enabled, please contact TrueTest team for support.
- For migrated projects from TestOps (Legacy):
    - The name of the data tracking environment cannot be changed.
    - The URL of the test execution environment cannot be changed.
    - Data tracking environment or test execution environment cannot be deleted.
    - Cannot unlink a project from an associated AUT with TrueTest enabled.
    - Cannot change the selected Git repository in an AUT with TrueTest enabled.