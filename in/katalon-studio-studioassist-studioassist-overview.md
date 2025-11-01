---
title: "StudioAssist Overview"
---
## Introduction 

StudioAssist is an AI-powered assistant integrated within Katalon Studio, designed to help testers efficiently create and understand automated tests.

Leveraging OpenAI’s GPT models, StudioAssist offers intelligent test code generation and insightful explanations directly within the Katalon Studio interface. The primary capabilities include:

- **Code generation**: StudioAssist automatically generates test automation scripts from structured user prompts.
- **Code explanation**: StudioAssist can help provide insight and clear explanation to selected code snippets.
- **Chat window**: StudioAssist offers a built-in interactive chat window for queries related to Katalon Studio functionalities. For more information, see: [StudioAssist chat window](/katalon-studio/create-test-cases/studioassist-chat-window).

## Requirements
- You have an active KSE license.
- AI features should be enabled at the Account level. If disabled, you can use a personal OpenAI key or Azure OpenAI API key. For detailed configuration steps, see [StudioAssist Preferences](/katalon-studio/get-started/workspace-settings/katalon-studio-preferences/studioassist-preferences).

## AI Model Information

- When using StudioAssist, the default model used is **GPT-4.1 mini**.
- When using a personal OpenAI key, the default model is set to **GPT-4o-mini**. However, you can choose your preferred model by clicking on the **Model** field (if applicable) in the KSE configuration window.

   ![Select AI model](https://tw-cdn.katalon.com/katalon-studio/create-test-cases/studio-assist/KS_StudioAssist_select_AI_model.png)

- When using a personal Azure OpenAI API key, you must specify the Deployment name via the KSE configuration window.

## Known limitations

As of Katalon Studio version 10.3.0, StudioAssist now includes fewer limitations compared to previous versions, thanks to ongoing improvements in AI capabilities and context handling. However, some constraints still apply:
- **Potential AI hallucinations**: StudioAssist may generate code with made-up built-in keywords. Always review and validate the generated code, and revise with the valid equivalent when applicable.
- **Programming language required**: Due to context limitations, generated code might require debugging and programming expertise.

## Best practices for using StudioAssist

For optimal results, follow these tips:

1. Break tasks into clearly defined bullet points rather than a single paragraph. Instead of:

  ```jsx
   Write me a test case that open a browser to a URL, log in to a website, click the login button, input the username and password, then close the browser *
  ```
  Write your prompt this way instead:

  ``` jsx 
   1. Open a browser to a URL
   2. Log in to the website
   3. Click the login button
   4. Input username and password
   5. Clock the browser
  ```
2. Divide complex actions into smaller tasks, generating code incrementally for each.
3. Include context in your prompt clearly specifying the desired method structure, data types, and exception handling. For example, here's a sample prompt for creating a custom keyword:
   ```jsx
   Write me a clickElement method that receives a test object id as a string and does as follows: 
   1. Find a web element
   2. Click the element 
   3. If cannot click the element, catch WebElementNotFoundException exception and use KeywordUtil.markFailed to say that you cannot find the element 
   4. If other errors, catch Exception saying that you failed to click the element with the KeywordUtil.markFailed 
   5. Otherwise, mark the keyword as succeed 
   
   The clickElement method should have the following format 
   
   @Keyword 
   def clickElement(<test object string>) {
       <content of the method>
    }
   ```

## StudioAssist FAQs

### Can I use StudioAssist without inputting my own OpenAI key?
When first introduced in 9.0.0, StudioAssist required you to input your own OpenAI API key. With the change in 9.4.0, you can use StudioAssist with a KSE license directly without having to input your own key.
   
### Can I use hotkeys for easy access to StudioAssist?
You can highlight a piece of code or comment on the script editor and use these shortcuts for StudioAssist quicker:

On macOS:
   - Generate code: `^` + `⌥` + `C`
   - Explain code: `^` + `⌥` + `E`

On Windows:
   - Generate code: `Ctrl` + `Alt` + `C`
   - Explain code: `Ctrl` + `Alt` + `E`
   
### What should I do when the generated test scripts do not run?
If you are using StudioAssist to generate a script in a test case, make sure that you capture the test object in the Object Repository, define the variables, and list out the actions in steps with corresponding test objects and variables.
  
### Why is StudioAssist not working for me?
Possible reasons include:

- AI features are disabled at the Account level. You might see a warning message when trying to use StudioAssist in this case. Contact the Account Owner to turn AI features so you can use StudioAssist again.
- You are not on an Enterprise license (required since version 9.4.0). Upgrade your license to continue using StudioAssist.
- You are logging in via a License Server (not supported).
- Proxy issues (update to version 9.4.0+).
- If you encounter this error message: `The OpenAI secret key is missing. Please provide your key and try again.`,you may need to:
   - Input your own OpenAI key if you are using Studio in version prior to 9.4.0.
   - Upgrade to 9.4.0 onwards and make sure you have a KSE license.
- If you encounter this error message: `{"error":"invalid _grant", "error _description": "Session not active"}`, you may have logged in using more than one machine at the same time. Log out from all devices and log in again.
- If you encounter this error message in the StudioAssist Chat window with the Katalon AI Service: `com.kms.katalon.ai.core.model.exception.StudioAssistLlmApiClientException: {“code”:8}`, it is usually caused by a large input size or hitting the current usage limits. To resolve this issue, try the following recommendations:
   - Clear the current conversation.
   - Disable **Auto-include project context information**.
   - Split your question into smaller parts.
