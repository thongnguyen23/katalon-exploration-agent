---
title: StudioAssist Preferences
---

:::info Prerequisites
- Katalon Studio Enterprise (KSE) 10.2.0.
:::

You can configure to use StudioAssist to further improve your experience.

In Katalon Studio, go to **Katalon Studio Enterprise > Settings > Katalon** and select **StudioAssist**. Depending on your Account configuration, you will see a slight difference in the dialog.

## AI service configuration

When [AI services and Katalon AI are enabled for your Account](/katalon-platform/administer/administration-and-licensing-alternate/manage-systems/configurations/configure-ai-services), you can freely choose between using:

| AI Provider   | Model used (default) | Configuration Details |
|------------|------------| ------------|
| Katalon AI Service| `gpt-4.1-mini`| Built-in; no configuration needed.|
| Personal OpenAI | `gpt-4o-mini`| Selectable via KSE configuration window.|
| Azure OpenAI | User-specified deployment | Requires specifying the deployment name in configuration.|
| Gemini | `gemini-2.5-flash`| URL points to the latest supported version of the Google Generative Language API.|
| OpenAI-Compatible Provider| `gpt-4.1-mini`| API key passed via the Authorization HTTP header.|

<img width="600" src="https://tw-cdn.katalon.com/katalon-studio/get-started/workspace-settings/katalon-studio-preferences/studioassist-preferences/StudioAssist_Preferences_10_3_0.png" alt="Choose between using Katalon AI Service, using your own OpenAI, Azure OpenAI API key, Gemini API key, or an OpenAI compatible provider."/> 

Click on the tab below to find more information about the AI service.

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

<Tabs>
  <TabItem value="Katalon AI" label="Katalon AI" default>

When selected, there is no need to to set up a key for **Katalon AI Service**.

You can, however, configure StudioAssist to auto-tag AI-generated test cases (e.g., API test cases or code generation) with default or custom tags, include project context such as the Object Repository and Custom Keywords, and enable follow-up question suggestions in the chat for a more guided AI experience.

<img width="600" src="https://tw-cdn.katalon.com/katalon-studio/get-started/workspace-settings/katalon-studio-preferences/studioassist-preferences/Katalon_AI_Service_10_3_0.png" alt="Choose between using Katalon AI Service or using your own OpenAI or Azure OpenAI API keys"/> 

  </TabItem>
  <TabItem value="Preset AI Service" label="Preset AI Service">

If your Admin has enabled the use of the organization’s AI key, the AI provider is shown at the top of the dialog as:
"**AI provider name** – managed by your organization". For example:

<img width="500" src="https://tw-cdn.katalon.com/katalon-studio/create-test-cases/studio-assist/studioassist_preset_AI_services.png" alt="Show AI provider name"/>

With this setting, you can configure the token limit and model for the AI service. You cannot switch between services (Katalon AI, OpenAI, Azure, Gemini, or OpenAI compatible provider).

  </TabItem>
  <TabItem value="Personal AI keys" label="Personal AI keys">

In the case of AI features are disabled, you can opt for your personal **OpenAI** key, **Azure** OpenAI API key, **Gemini** API key, or your personal OpenAPI key from a compatible provider.
  - Provide service provider configuration.
    - **Use personal OpenAI key**: Provide the following information before using:
    
      <img width="450" src="https://tw-cdn.katalon.com/katalon-studio/get-started/workspace-settings/katalon-studio-preferences/studioassist-preferences/Personal_OpenAPI_key_settings.png" alt="Use personal OpenAI key"/>

      - Secret key: To get your Secret key, refer to the provider's instruction: [Where do I find my secret key?](https://help.openai.com/en/articles/4936850-where-do-i-find-my-openai-api-key).
      - Max completion token: The default value that sets the maximum number of tokens the model can return in its response. The default value is 16000. To learn more about the token limits, refer to the OpenAI rate limits documentation: [OpenAI Token Limits](https://help.openai.com/en/articles/4936856-what-are-tokens-and-how-to-count-them#h_051eb08805).
      - Organization ID (optional): The organization ID on OpenAI is the unique identifier for your organization which can be used in API requests.
      - - Model: The OpenAI model you want to use. If not changed, the `gpt-4o-mini` model is used by default.
    
    - **Use personal Azure OpenAI API key**: Provide the following information before using:
      
      <img width="450" src="https://tw-cdn.katalon.com/katalon-studio/get-started/workspace-settings/katalon-studio-preferences/studioassist-preferences/Azure_OpenAPI_key_settings.png" alt="Use personal Azure OpenAI API key"/>

      - Base URL: The base URL for your Azure OpenAI resource in the following format: `https://{your-resource-name}.openai.azure.com`.
      - Deployment name: Azure OpenAI uses the deployment name to call the model. Enter the deployment name of your choosing, make sure that the model supports chat completion.
      - API key: To get your Azure OpenAI key, refer to this article: [How to get Azure OpenAI Keys and Endpoint](https://www.c-sharpcorner.com/article/how-to-get-azure-open-ai-keys-and-endpoint/)
      - Max completion token: The default value that sets the maximum number of tokens the model can return in its response. The default value is 16000.
      - API version: API version is selected for you by default.
    
    - **Use Gemini API key**: Provide the following information before using:

      <img width="450" src="https://tw-cdn.katalon.com/katalon-studio/get-started/workspace-settings/katalon-studio-preferences/studioassist-preferences/Gemini_API_key_settings.png" alt="Use personal Gemini API key"/>

      - Base URL: The base URL used to connect to the Gemini API service. This URL should point to the correct version of the Google Generative Language API.
      - API key: Your Gemini key. Create a key for free in [Google AI Studio](https://aistudio.google.com/app/apikey).
      - Model: The Gemini model you want to use. If not, StudioAssist will use the latest supported version of the Google Generative Language API by default.
      - Max completion token: The default value that sets the maximum number of tokens the model can return in its response.

    - **Open-AI compatible provider**: Provide the following information before using:

      <img width="450" src="https://tw-cdn.katalon.com/katalon-studio/get-started/workspace-settings/katalon-studio-preferences/studioassist-preferences/OpenAPI_compatible_provider_key_settings.png" alt="Use OpenAPI-compatible provider"/>

      - Base URL: The The API endpoint for your OpenAI-compatible service.
      - API key: Your API key.
      - API key header name: The name of the HTTP header where the API key is passed (commonly `Authorization`). This allows support for providers with different header naming conventions.
      - Model: The model you want to use. If not changed, the `gpt-4.1-mini` model is used by default.
      - Max completion token: The default value that sets the maximum number of tokens the model can return in its response.

  </TabItem>

</Tabs>

## StudioAssist Preferences options

Refer to the items below for the list and descriptions of StudioAssist Preferences options.

### Append tags for test cases used AI generated capabilities

- **API Test Case Generation** - Check this option to automatically tag AI-generated API test cases with a default tag (`API_Test_Generation`) or custom tag name of your choice. When enabled, StudioAssist adds an AI tag (default or custom) to each API test case it generates.

- **StudioAssist Code Generation** - Check this option to automatically tag AI-generated test automation scripts from structured user prompts with a default tag (`GenAI`) or custom tag name of your choice. 

Test cases with AI-generated tags are highlighted in purple.

### Auto-include project context information

To improve the scripts generated by StudioAssist, you can enable both the **Object repository** and your **Custom keywords**. StudioAssist will then automatically use the list of all test object IDs and available custom keywords in the project as context.

This helps StudioAssist deliver more tailored responses, reduces the effort of specifying exact object paths or test objects, and allows you to reuse your predefined actions through custom keywords directly in the generated scripts.

### Auto-suggest follow up questions in the chat

When enabled, StudioAssist automatically suggests follow-up questions after providing a successful answer. This gives users greater control over their chat experience, whether they prefer guided suggestions or a more minimal interface.

<img width="450" src="https://tw-cdn.katalon.com/katalon-studio/get-started/workspace-settings/katalon-studio-preferences/studioassist-preferences/kse_studio_10_3_0_StudioAssist_Chat_Enable_autosuggest.png" alt="Auto-suggest follow-up questions in the chat window"/>

## Customize engineering prompts with Prompt Library

Starting from version 10.2.3, you can customize your engineering prompts using Prompt Library to provide more context and improve the accuracy of StudioAssist responses.

1. Click **Katalon Studio Enterprise** on the main navigation and select **Settings** to open the **Preferences** dialog.
2. Select **Katalon > StudioAssist > Prompt Library**.
3. Configure your Prompt Library. Click on the prompt type you want to customize. Edit this text directly to include more context or specific instructions about how you want the AI to respond.

  <img src= "https://tw-cdn.katalon.com/katalon-studio/get-started/workspace-settings/katalon-studio-preferences/studioassist-preferences/Prompt_library_dialog.png" alt="StudioAssist Prompt Library" width="600" />

   - **Chat instruction**: Used in the [StudioAssist chat window](/katalon-studio/create-test-cases/studioassist-chat-window). This controls how StudioAssist responds to your general questions or guidance requests. Add more context about your application under test (AUT) or focus area, so you don’t have to repeat this every time you chat.
   - **Generate code**: Used in the [script editor](/katalon-studio/create-test-cases/studioassist-in-katalon-studio#generate-code), add style guide details or coding preferences to make the generated code better fit your project.
   - **Explain code**: Used in the [script editor](/katalon-studio/create-test-cases/studioassist-in-katalon-studio#explain-code), specify if you want detailed technical explanations or a high-level summary, depending on your needs.

    :::note Notes
    - Use `${userSelection}` for **Generate code** and **Explain code**. This variable represents the specific piece of text or code you have highlighted (selected) in the script editor. 
    - Customize prompt is not applied for Katalon AI service.
    :::

4. Click **Apply** or **Apply and Close** to save. 

You can now use StudioAssist with your customized prompts. 

If the generated output is not to your expectation, simply open the Prompt Library and select **Revert Original** to revert each prompt or click **Restore to Defaults** to restore all prompts.
