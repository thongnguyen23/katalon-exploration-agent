---
title: Generate and Explain code in script editors
---
## Generate code

StudioAssist can generate intelligent automation test code suggestion based on a prompt.

To generate code with StudioAssist, follow these steps:
1. Open a test case in **Script** mode.
2. Provide your code prompt in terms of code comments, single line or block comment. For example, the prompt can be:
   ```jsx
   * Write a Katalon Studio test case to perform the following steps. 
   * 1. Open browser to the URL stored in G_SiteURL
   * 2. Click the make appointment button
   * 3. Fill in the username and password fields based on the variables
   * 4. Click the login button
   * 5. Verify that the appointment div exists
   * 6. Close the browser
   ```
3. Select the prompt text. Right-click and select <span className="ph uicontrol">StudioAssist</span> &gt; <span className="ph uicontrol">Generate Code</span>.
   <img src= "/844dab10-0e4c-11ee-bd0e-0242c7a41fd4/StudioAssist_generate_code.png" alt="Generate Code button" width="500" />

#### Result 

StudioAssist then generates the test script below the prompt text:
<img src= "/841276d0-0e4c-11ee-bd0e-0242c7a41fd4/StudioAssist_generated_code.png" alt="StudioAssist Code generation results" width="600" />

## Explain code

You can select a code snippet and use StudioAssist to explain the code. 

To generate code explanation, follow these steps:
1. Open a test case with existing test steps in **Script** mode.
2. Select the the desired code snippet. Right-click and select **StudioAssist** > **Explain Code**. 
   <img src= "/84336c50-0e4c-11ee-bd0e-0242c7a41fd4/StudioAssist_explain_code.png" alt="Explain Code button" width="600" />

#### Result

StudioAssist then generates the code explanation below the selected script:
<img src= "/84559a50-0e4c-11ee-bd0e-0242c7a41fd4/StudioAssist_code_explanation.png" alt="StudioAssist code explanation results" width="600" /> 

