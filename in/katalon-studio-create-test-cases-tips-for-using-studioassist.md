---
title: Tips for using StudioAssist
---

This article provides tips to optimize your experience when using StudioAssist and StudioAssist chat window in Katalon Studio.

## Tips for using StudioAssist

To generate desirable results with StudioAssist, you can provide prompt text in certain format and with specific context. The following are some tips to use StudioAssist effectively.

1. When you need to perform multiple actions, write each action in a bullet point.
   
  For example, instead of writing a prompt in one paragraph:

  ```jsx
   * Write me a test case that open a browser to a URL, log in to a website, click the login button, input the username and password, then close the browser *
  ```
  You can provide a list of actions:

  ``` jsx 
   * 1. Open a browser to a URL
   * 2. Log in to the website
   * 3. Click the login button
   * 4. Input username and password
   * 5. Clock the browser
  ```
2. Break complex tasks into smaller tasks and use StudioAssist on each small task.
3. To produce output in a specific format, you can provide the context in your comment. For example, to generate a custom keyword, you should provide details about the method template, data type, and possible exceptions:
   ```jsx
   * Write me a clickElement method that receives a test object id as a string and does as follows: 
   * 1. Find a web element
   * 2. Click the element 
   * 3. If cannot click the element, catch WebElementNotFoundException exception and use KeywordUtil.markFailed to say that you cannot find the element 
   * 4. If other errors, catch Exception saying that you failed to click the element with the KeywordUtil.markFailed 
   * 5. Otherwise, mark the keyword as succeed 
   *
   * The clickElement method should have the following format 
   * 
   * @Keyword 
   * def clickElement(<test object string>) {
   *    <content of the method>
   * }
   *
   ```


## Tips for using StudioAssist chat window

To get the best results when asking StudioAssist to generate a test case, provide clear and specific details. Here are some tips:

1. Provide your input in certain format. See [Tips to use StudioAssist](/katalon-studio/create-test-cases/studioassist-in-katalon-studio#tips-to-use-studioassist).
2. Specify the type of application under test (AUT): Indicate whether you're writing a mobile test, API test, or web test. For example:
    ```jsx
    Write me a mobile test case.
    ```
    ```jsx
    Generate an API test case.
    ```
3. Include details about the AUT: Mention specifics like the app ID for a mobile application or the URL for a web application.
4. Enable **Auto-include project context information** in **StudioAssist Preferences** to include available object IDs in your project when asking StudioAssist to generate test cases.
5. If you work with multiple files in a single conversation, we recommend clearing the conversation frequently to ensure more accurate responses. All files attached during a conversation are used as context until the conversation is cleared. The more files included, the higher the chance that StudioAssist may generate less relevant results.


## StudioAssist FAQs

This section answers some Frequent Asked Questions (FAQs) regarding the use cases and capabilities of StudioAssist.
1. **Can I use StudioAssist without inputting my own OpenAI key?** <br/>
   When first introduced in 9.0.0, StudioAssist required you to input your own OpenAI API key. With the change in 9.4.0, you can use StudioAssist with a KSE license directly without having to input your own key.
   
2. **Can I use hotkeys for easy access to StudioAssist?** <br/>
   You can highlight a piece of code or comment on the script editor and use these shortcuts for StudioAssist quicker:
    On macOS:
    - Generate code: `^` + `⌥` + `C`
    - Explain code: `^` + `⌥` + `E`
    On Windows:
    - Generate code: `Ctrl` + `Alt` + `C`
    - Explain code: `Ctrl` + `Alt` + `E`
   
3. **What should I do when the generated test scripts do not run?** <br/>
   If you are using StudioAssist to generate a script in a test case, make sure that you capture the test object in the Object Repository, define the variables, and list out the actions in steps with corresponding test objects and variables.
  
4. **Why can't I use StudioAssist?** <br/>
   If you cannot use StudioAssist, please check the following possible reasons:
   - Your company turned off AI features at the Account level of Katalon. You might see a warning message when trying to use StudioAssist in this case. You will need to contact the Account Owner and turn AI features on to use StudioAssist again.
   - You are not using an Enterprise license. StudioAssist has become an Enterprise feature since version 9.4.0. You need to upgrade your license to continue using it.
   - You are logging in via License Server. StudioAssist is not available when using License Server to log in. 
   - You might be behind a proxy. If setting proxy does not work for you, make sure that you are using StudioAssist on Studio version 9.4.0 onwards, where we fixed this issue.
   - If you encountered this error message: `The OpenAI secret key is missing. Please provide your key and try again.` You might need to: 
     - Input your own OpenAI key if you are using Studio in version prior to 9.4.0.
     - Or, upgrade to 9.4.0 onwards and make sure you have a KSE license.
   - If you encounter this error message: `{"error":"invalid _grant", "error _description": "Session not active"}`. You might log in from 2 machines at the same time, so you need to log out and log in again.
