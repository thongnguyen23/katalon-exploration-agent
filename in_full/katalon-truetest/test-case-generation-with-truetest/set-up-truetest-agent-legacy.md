---
title: Set up TrueTest Agent (Legacy)
---
import Reusable from '@site/src/reusable/Reusable.mdx';
import useBaseUrl from '@docusaurus/useBaseUrl';

<Reusable />

This document shows you how to set up TrueTest Agent for test case generation with TrueTest.

## Requirements
- You must be the Administrator of your Katalon Account. See: [Administrative Roles and Permissions](/katalon-platform/administer/administration-roles/administrative-roles-and-permissions).
- You must have a Git script repository configured in TestOps with the Write permission. See: [Configure a Git repository in TestOps](/katalon-platform/organize/configure-a-git-repository-in-testops).

## Add application under test
First you need to define an application under test (AUT). The AUT specifies the production environment where TrueTest can track all user interactions and leverage them in generating flows.

1. Log in to [TestOps Homepage](https://testops.katalon.io/).
2. On the top right corner, select **Settings > TrueTest**.
    
    <img src="https://docs.katalon.com/dd5b6490-d6ab-11ee-9719-0242c7a41fd4/TestOps_Settings_TrueTest.png" alt="TestOps Settings > TrueTest" width="1080"/> <br />
    
    The TrueTest Configuration menu displays as below.
    
    <img src="https://tw-cdn.katalon.com/truetest/truetest-configuration.png" width="1080" alt="TrueTest Configuration page" /> <br/>

3. Click **Add Application Under Test**. In the displayed dialog, provide the information of your AUT.
    <img src="https://tw-cdn.katalon.com/truetest/truetest-add-aut-dialog.png" alt="Add application under test dialog" width="500" /> 
    
    - **Name**: The displayed name of your application.
    - **Description**: The description for your application.

4. Click **Add**.

#### Result
Your application under test is successfully added.


### Configure the application under test
After the AUT is defined, you need to install the event tracking agent in your application, provide the development environment and link with the test project.

Select the AUT you want to configure. The configuration menu appears with four main components:
- Install TrueTest on your application. You can manually add the tracking snippet in the AUT source code or use Google Tag Manager.
- Add Data Tracking Environment.
- Add Test Environment(s).
- Link Project(s).

#### Result
After configuring the four components, navigate back to the **Application Under Test** list and check the **Activation Date, Last Data Received Date** data columns, and the **Active** status. These items signify that TrueTest Agent has successfully tracked data from the AUT.


### Install TrueTest snippet
A developer or someone with access to the codebase of the AUT must add the tracking code snippet provided by Katalon. The code snippet should be pasted into the `<HEAD>` element of the HTML code of the AUT. Once the code snippet is added, the AUT should be saved, built, and deployed to the production environment.

TrueTest also provides the option to install with Google Tag Manager.

Here are two options to install the code snippet:

- Install the code snippet manually. In the **Install your TrueTest** snippet section, copy the displayed code snippet and paste into the `<HEAD>` element of your application under test.
    <img src="https://docs.katalon.com/530a0040-5ce3-11ee-bc71-0242c7a41fd4/ATG_TrueTest_manual_snippet.png" alt="install true test snippet code" />

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
    
    a. Log in to [Google Tag Manager](https://tagmanager.google.com/).

    b. In the container that is connected to the application under test, create a new tag.
    
    c. Name and edit the tag. Here we define a custom HTML tag.
    <img src="https://docs.katalon.com/52e4c500-5ce3-11ee-bc71-0242c7a41fd4/ATG_Google_Tag_Manager_add_tag.png" alt="GTM - Add custom HTML tag" /> <br/>
    
    d. Paste the provided snippet into HTML block. Here, the `CLIENT-CODE` is the code displayed in the configuration UI.
    <img src="https://docs.katalon.com/5316f890-5ce3-11ee-bc71-0242c7a41fd4/ATG_Google_Tag_Manager_paste_code_snippet.png" alt="GTM - paste code snippet" /> <br/>
    
    e. Add a triggering event and select the **All pages** trigger to ensure that the TrueTest code snippet is enabled on all pages where the GTM is enabled.
    <img src="https://docs.katalon.com/5300ff90-5ce3-11ee-bc71-0242c7a41fd4/ATG_Google_Tag_Manager_add_trigger.png" alt="GTM - add trigger" /> 

#### Result
Once saved, the TrueTest tracking snippet will be added to the HTML header when a user accesses the application. To ensure that the Agent works properly, open the browser's **Developer Tools** > **Network** tab and filter for `KA-****`. Try clicking some buttons and links. If the network activity is being sent to our server, the Agent is working.
<img width="400" src="https://tw-cdn.katalon.com/truetest/truetest-verify-agent-function.png" alt="Verify TrueTest Agent functionality" />

### Add data tracking environment

TrueTest allows you to generate journey maps based on tracked data from specific environments. This setup enables you to analyze user behavior and generate tests independently across different deployment stages.

For each AUT, you can configure multiple data tracking environments. Data from each environment is kept separate and used to build environment-specific journey maps.

Click **Add data tracking environment** to open the dialog:
- **Environment name**: Provide a name to differentiate between environments, such as **Production**, **QA**, or **Staging**.
- **Environment domain(s)**: The name of your deployed website. For example, valid domains can be `*.katalon.com` or `katalon.com`.

<img src="https://tw-cdn.katalon.com/truetest/truetest-add-data-tracking-environment.png" width="500" alt="Add data tracking environment" />


### Add test environment
To generate test cases with traffic collected from the production site, TrueTest Agent requires a test environment, which functions similarly to a profile in Katalon Studio for managing configurations and scripts. Additionally, you will need to provide a login script within the test environment if the AUT requires login to complete any user flows. This will assist TrueTest in injecting authentication steps into generated test scripts.

To add a test environment, follow these steps:

Click on the **Add Test Environment** button. In the opened dialog, you need to provide the test environment for the test execution. Provide the name and the URL for the environment. You can also provide login credentials for accessing that environment if necessary.
<img src="https://docs.katalon.com/186d7c20-d8fc-11ed-ae00-0242cfbc79b5/ATG_add_test_environment.png" alt="Add test environment dialog" width="500" />

**Environment URL** should follow the correct pattern with the appropriate protocol and should not contain unnecessary trailing slashes. For example, a valid URL syntax will be `https://qe.your-app.com`.

For login method, there are two options: **No Authentication** or **Others** for custom login script.
<img src="https://docs.katalon.com/5ec57510-bfec-11ee-ac6d-0242c7a41fd4/TrueTest_login_method.png" alt="TrueTest - Login Method - others" width="600" />

:::info notes
Before generating TrueTest test cases, make sure that you've committed the changes you made, on login scripts and any other related test objects, to the Git repository: [Link project](/katalon-platform/create-tests/test-case-generation-with-truetest/set-up-truetest-agent#link-project).
:::
You can use the record and playback feature in Katalon Studio to record the login actions on your test environment. This will help generate a corresponding login script. See: [Record and playback in Katalon Studio](/katalon-studio/record-and-spy/webui-record-and-spy-utilities/create-test-cases-with-record-and-playback-in-katalon-studio).

<img src="https://docs.katalon.com/5ec10840-bfec-11ee-ac6d-0242c7a41fd4/TrueTest_Katalon_Studio_login_script.png" alt="add test env screen" /> <br />

There are three ways to use the custom script:

- Copy the entire login script and paste it into the script editor area.
- Use `thecallTestCase()` keyword.
    You can package the login script as a test case and call it with the keyword.
- Use a custom keyword.
    You can package your login script into a custom keyword and use it the script editor.

### Link project
:::info notes
The Git script repository must be configured with Write permission.
:::

Once test cases are generated, TrueTest needs to store the tests in a repository.

Click on the **Link Project** button to select the test project and script repository. You can select to commit and push the test artifacts to a script repository, which can then be executed as Katalon test scripts.
You can select multiple projects to link to an AUT. You must be a member of those projects to view and select them.
If you use a private network and cannot integrate with a Git repository, you can select Katalon Cloud to store the test artifacts.
<img src="https://docs.katalon.com/188f34f0-d8fc-11ed-ae00-0242cfbc79b5/ATG_link_project.png" alt="Link project dialog" width="600" />

### Data privacy configuration (optional)
TrueTest has a filtering mechanism to exclude sensitive information from user's application under test, see: [Protect user data privacy](/katalon-platform/create-tests/test-case-generation-with-truetest/protect-user-data-privacy).

Additionally, users have the option to manually specify which fields or elements should be excluded while TrueTest is collecting data. To do so, simply add CSS class `katalon-excluded` to the UI elements that you do not want their values to be captured.

<img src="https://docs.katalon.com/9a3df510-7300-11ee-9132-0242c7a41fd4/TrueTest_katalon_excluded_examples.png" alt="katalon-excluded examples" />

## Advanced settings
The advanced settings section allows you to further customize the behavior of TrueTest Agent while generating test cases for your AUT.

To access the settings, in the **Application Under Test** list, click on the desired AUT and switch to the **Advanced Settings** tab.

<img src="https://tw-cdn.katalon.com/truetest/truetest-advanced-settings.png" alt="truetest advanced settings tab" width="1080" />
<br/>

- **Default Selection Method**: You can specify the main selection method that Katalon Studio should use when running the generated test cases.
- **Common Functions**: When collecting data among multiple user flows, TrueTest can detect which group of steps are common across the flows and organize these steps into common functions. For example, in the checkout flow of an online shopping website, users may need to fill in billing addresses, shipping addresses, payment information, etc. These steps can be organized into a function. The **Minimum number steps** specify the minimum number of steps that TrueTest can include in a function.
- **Test Data**: This setting allows TrueTest to bind default values or values in data file in generated test cases. If you select the **Default** option, go to the **Variables** tab > **Default value** column to update the values. If the **Data Column** option is selected, go to **Data Files** > **AI-Generated** folder and import the data file to Excel. Each column is a variable's name and you can add data to each row.
- **Data Tracking**: Enabling more data tracking can enhance the accuracy of generated test cases.