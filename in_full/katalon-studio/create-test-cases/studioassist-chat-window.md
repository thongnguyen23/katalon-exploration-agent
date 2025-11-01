---
title: "StudioAssist chat window"
---

## Overview

StudioAssist Chat Window enables instant interaction with Katalon Studio’s AI assistant directly within your workspace. Use it for learning about Studio features, automating test script generation, and understanding testing concepts efficiently.

From the chat window, you can:

- Ask instructions for Katalon Studio features, automated test writing, and built-in keywords.
- Learn about testing concepts whenever you need help.
- Generate automation test code or explain a code snippet.
- Ask follow-up questions with a ChatGPT-like experience.

## Prerequisites

- Katalon Studio Enterprise version 10.1.0 onwards.
- The AI feature settings is enabled for the Account. If disabled, you can opt for either a personal OpenAI key, or Azure OpenAI key. For more details, see [StudioAssist Preferences](/katalon-studio/get-started/workspace-settings/katalon-studio-preferences/studioassist-preferences).

## Supported AI models

To choose your preferred AI model, click the dropdown in the Model field via the KSE configuration window, when applicable. 

<img width="600" src="https://tw-cdn.katalon.com/katalon-studio/get-started/workspace-settings/katalon-studio-preferences/studioassist-preferences/StudioAssist_Preferences_10_3_0.png" alt="Choose your AI model"/>
<br/>

Starting version 10.3.0, we have added more AI models. See [StudioAssist preferences](/katalon-studio/get-started/workspace-settings/katalon-studio-preferences/studioassist-preferences) for more information. 

For OpenAI compatibility information, refer to [OpenAI Supported Models](https://platform.openai.com/docs/models). 

## How to launch StudioAssist chat window

### Automatic launch
When opening a project for the first time, the StudioAssist chat window automatically appears on the right side of your workspace.

![Launch StudioAssist chat window automatically](https://tw-cdn.katalon.com/katalon-studio/create-test-cases/studio-assist/StudioAssist_chat_window_10_2.png)

### Manual launch

If StudioAssist chat window is not visible or if it's closed, click the **StudioAssist** icon on the main toolbar to open.

<img src="https://tw-cdn.katalon.com/katalon-studio/create-test-cases/studio-assist/ks-950-studioassist-click-icon.png" alt="StudioAssist icon in Katalon Studio" width="300" />

Alternatively, use the following shortcuts for quick access.
- macOS: `^ + ⌥ + N`
- Windows: `Ctrl + Alt + N` 

:::note Limitation
The hotkey on Windows generally works well; however, it may not function when you're focused on certain pages, such as the Start Page, Walkthrough, or other webview-based screens.
:::

### Resolving Missing AI Model Errors
If your account has no configured AI model, the following notification appears: `There is no AI model in your account`.

<img src="https://tw-cdn.katalon.com/katalon-studio/create-test-cases/studio-assist/StudioAssist_chat_window_small.jpg" alt="StudioAssist chat window in Katalon Studio" width="300" />

To resolve this, click:

- **Request access**: Contact your account owner to enable AI features.
- **Add your API key**: Configure your own OpenAI or Azure OpenAI key in [StudioAssist Preferences](/katalon-studio/get-started/workspace-settings/katalon-studio-preferences/studioassist-preferences).

After configuration, click Reload in the chat window to refresh settings.

## How to use StudioAssist chat window

StudioAssist supports:

- Answering queries about Katalon Studio features and testing concepts.
- Generating automation test scripts and custom keywords. For more information, see [Example use cases for StudioAssist](/katalon-studio/create-test-cases/studioassist-chat-window#example-use-cases-for-studioassist).
- Explaining code snippets clearly.

## Common use cases

Refer to the following common use cases and example prompts for guidance:

1. **Ask Testing Questions**: Get instant answers to your queries about automation testing concepts. For example:

```
How to create a test case in Katalon Studio?
```
2. **Generate Test Scripts**: Specify clearly your application type, test objects, and steps. 
```
Write me a web test script:
1. Open browser to URL: GlobalVariable.G_SiteURL
2. Click the Make Appointment button
3. Enter Username and Password
4. Click Login button
5. Close browser
```
3. **Explain Code Snippets**: Request concise explanations. 
```
Summarize this code in 3 sentences.
// Paste your code here
```
4. **Create Custom Keywords**: Provide detailed requirements.
```
Write a custom keyword for login handling:
- Method name: login
- Accept TestObjects for username, password fields, login button
- Accept Strings for username, password
```
5. **Explain a custom keyword**: If your team uses custom keywords in test scripts, StudioAssist can help you quickly understand what each keyword does.
```
Explain what this custom keyword does:
// Paste your custom keyword code here
```
6. **Reuse custom keywords**: If you've already generated custom keywords, you can reference them directly in your request to build new test scripts.
```
Use the clickElement custom keyword to tap on the login button.
```
7. **Troubleshoot issues**: Clearly mention errors and steps.
```
What should I do if my test case fails at step 3 due to timeout?
```
8. **Write manual test cases**: Include descriptive information.
```
Provide a manual test case outlining the steps to test a basic login process following a password reset. The test case should include a descriptive title, preconditions, test steps with expected outcomes, pass/fail criteria, and any relevant notes for handling errors or exceptions.
```
9. **Optimize code**: Clarify optimization intent.
```
Please optimize this code for better performance:
for (int i = 0; i < array.length; i++) {  
    if (array[i] % 2 == 0) {  
        System.out.println(array[i]);  
    }  
}
```

## Example use cases
Below are specific use cases and example prompts of how you can use StudioAssist chat window to support your work.

### (Mobile testing) Write a mobile test script

If you have captured mobile objects using **Mobile Object Spy** and want to write test cases for basic scenarios, you can provide the app ID and object list in a manual script.
```jsx
Write me a mobile test case with the following steps:
1. Start application, uninstalling the application automatically after run
2. Tab on the linear layout, timeout 0
3. Get text 'HorizontalNestedScrollView', timeout 0
4. Close the app
My app ID: 6261b88f-275b-4ae5-b0d1-b95fbf2560bd
Object list:
findTestObject('Object Repository/android.widget.LinearLayout')
findTestObject('Object Repository/android.widget.TextView - HorizontalNestedScrollView')
```
### (API testing) Verify status code

To generate an API test case, ensure you specify the API endpoint (for example, `https://reqres.in/api/users?page=2`) and the corresponding test object (`getAllUsers`) explicitly in your request.
```jsx
Write me an API test case with the following steps:
1. Send a GET request to the URL 'https://reqres.in/api/users?page=2'.
2. Verify that the response status code is 200.
Use the object ID: findTestObject('getAllUsers').
```

### (Web testing) Generate a Login test script using existing test objects

If you already have test objects prepared in your project, you can quickly generate a web test script using StudioAssist. Simply provide the necessary test object details, variables, and the steps you want to automate.

For an example of predefined test objects, refer to our sample project: [Sample WebUI project (Healthcare sample)](/katalon-studio/get-started/sample-projects/webui/sample-webui-project-healthcare-sample-in-katalon-studio).
```jsx
I have a list of test objects as below:
- Make appointment button: 'Page_CuraHomepage/btn_MakeAppointment'
- Username: 'Page_Login/txt_UserName'
- Password: 'Page_Login/txt_Password'
- Login button: 'Page_Login/btn_Login'
- Appointment div element: 'Page_CuraAppointment/div_Appointment'
 
I also have a URL: GlobalVariable.G_SiteURL, and two variables `Username` and `Password`
 
Write me a test case to perform the following steps:
1. Open browser to the URL stored in G_SiteURL
2. Click the make appointment button
3. Fill in the username and password fields based on the variables
4. Click the login button
5. Close the browser
```

## Attach files

:::info
This feature is available from version 10.2.0.
:::

You can now include files from your project or local machine directly in a conversation to give StudioAssist more context.

1. In the StudioAssist chat window, click the paperclip icon to attach files.

   <img width="300" src="https://tw-cdn.katalon.com/katalon-studio/create-test-cases/studio-assist/studioassist_attach_file_10_2.png" alt="Click paperclip icon to attach files"/>

2. Choose one of the following:
   - **Select from project**: Browse test cases, test suites, listeners, Groovy/Java files, feature files, etc.
   - **Select from computer**: Upload external files such as CSV data files.

:::note
  - You can send up to 10 files per question.
  - Each file must be text-based and under 10MB.
  - Invalid files are flagged and won't be sent.
  - Attachments appear above the input field and are also shown under each sent message.
:::

3. After you sent the file(s), StudioAssist will return the result according to your request.
   <img width="300" src="https://tw-cdn.katalon.com/katalon-studio/create-test-cases/studio-assist/studioassist_attached_file_response.png" alt="Display StudioAssist response from file prompt"/>

## Use current file as context

In addition to manual file attachment, StudioAssist automatically includes the content of the file you're actively working on as context. This removes the need to manually copy-paste file content into the chat. 

In the chat window, the **Current file** box is selected by default to include the file you're working on. When you switch between files, the context also automatically updates. If you want to turn this off, simply untick the box.

<img width="400" src="https://tw-cdn.katalon.com/katalon-studio/create-test-cases/studio-assist/studioassist_current_file.png" alt="Use current file as context"/>

:::tip Supported file types
This feature only applies for the following files: 
- test case
- test suite
- dynamic test suite
- test listener
- web service request
- custom keyword
- BDD feature file
- profile
- step definition (`.groovy` file)
- Java class (`.java` file).
:::

## Tips for getting better responses
To get the best results when asking StudioAssist to generate a test case, provide clear and specific details. Here are some tips:

1. Clearly specify your input in certain format. See [Tips to use StudioAssist](/katalon-studio/create-test-cases/studioassist-in-katalon-studio#tips-to-use-studioassist).
2. Clearly specify the type of application under test (Web. Mobile, API): Here are some example prompts:
    ```jsx
    Write me a mobile test case.
    ```
    ```jsx
    Generate an API test case.
    ```
3. IInclude details about the AUT: Mention specifics like the app ID for a mobile application or the URL for a web application.
4. Enable **Auto-include project context information** in StudioAssist Preferences to auto-populate object IDs.
5. Regularly clear conversations when context changes. All files attached during a conversation are used as context until the conversation is cleared. The more files included, the higher the chance that StudioAssist may generate less relevant results.
6. Set optimum complexion tokens to 16000 for optimal responses.

## Known limitations
While StudioAssist chat window offers valuable support, it currently has a few limitations:

- **Limited knowledge base**: StudioAssist does not yet pull information directly from Katalon Studio’s official documentation. For complex or uncommon queries, refer to Katalon documentation manually.
- **Project context limitations**: StudioAssist is not aware of global variables, custom keywords, other test cases, test data, etc. To make sure that the code is generated with proper variables and locators, we recommend specifying them in your question.
- **Single conversation mode**: StudioAssist supports only one active conversation at a time. Use the Clear conversation option regularly, especially when switching contexts, to reduce the chances of StudioAssist using incorrect context from previous questions. Your conversation is also automatically cleared when you close StudioAssist chat window.
- **AI response accuracy disclaimer**: Responses may be inaccurate or misleading. Always verify AI-generated output before implementation. You may rate responses as Good or Not Relevant to help improve StudioAssist. However, your feedback is not used to train the AI model or track your conversations.
- **Windows limitation**: On Windows, there is no functioning hotkey to open the StudioAssist chat window.
Performance: In projects with large number of test objects (more than 200 objects), StudioAssist tries to enumerate every object, which can cause timeouts and failed retrieval attempts.
