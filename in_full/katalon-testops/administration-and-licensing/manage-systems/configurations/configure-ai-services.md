---
title: Configure AI Services
---
<!-- PRD: https://katalon.atlassian.net/wiki/spaces/ADMIN/pages/3791683585/PRD+AI+Services+Configuration -->

Learn how you can configure AI services and features for Katalon TestOps.

## Prerequisites

- Make sure you are an Account Admin or possess the relevant permissions. Go to [roles](/katalon-testops/administration-and-licensing/manage-systems/permissions/about-roles) or [permissions](/katalon-testops/administration-and-licensing/manage-systems/permissions/about-permissions) for more information or learn how to [assign an Account Admin here](/katalon-testops/administration-and-licensing/manage-administrators/assign-or-unassign-account-administrators).

---
You can control how AI features operate across your systems through our comprehensive management tools. These allow you to enable or disable AI capabilities, configure various AI service providers, and manage API keys at both Account and Organization levels. These capabilities streamline AI service management for enterprise environments while maintaining compliance with your organizational policies.

:::caution
- AI features are disabled by default to ensure compliance with policy requirements.
:::

## Enable or disable AI features

1. Go to **Admin Settings > Organization**. You can find Admin Settings at the upper right corner of the page, indicated by a cog icon.

2. Toggle the **Enable AI Features** switch to enable or disable AI features.

3. Select the AI key you want to use:

    - **Default AI Key**: Use the default key provided by Katalon for AI-powered features. 
    - **Organization AI Key**: Use your own custom AI key. Choosing this requires you to create your own default key. 

<br/>

:::note Important notes about AI keys:
- Organization-specific AI keys take precedence over global keys.
- Katalon Studio-configured AI keys will take precedence over the default Katalon AI key.
- These settings will be retained in the event of deactivation (or later reactivation) of AI features.
:::

---

## Configure a Default or Organization-specific AI key

Admins can configure a Default AI key that applies across the entire account unless overridden by an Organization-specific AI key, allowing for different AI providers and model types. Only one default key can be active at any time.

Otherwise, an Organization-specific AI key that applies individually to each Organization can be used instead, ensuring policy compliance at the that level. This overrides any Default AI key and only one can be active per Organization.

To configure an Account AI key, click on the **Configure** button in the **Account AI Key** section.

<img src="https://tw-cdn.katalon.com/katalon-testops/Administration and Licensing/Manage Systems/Configurations/Configure Account AI Key Admin.png" alt="Your AI key configuration option in Katalon TestOps" width="1080"/>

<br/>

To configure an Organization-specific AI key, click on the **+ Add new** button in the **Organization-specific AI Key** section.

<img src="https://tw-cdn.katalon.com/katalon-testops/Administration and Licensing/Manage Systems/Configurations/Configure Organization Specific AI Key Admin.png" alt="Your AI key configuration option in Katalon TestOps" width="1080"/>

<br/>

Note that selecting the option **Require Organization AI API Key** will disable all other options in the AI configuration page: 


<img src="https://tw-cdn.katalon.com/katalon-testops/Administration and Licensing/Manage Systems/Configurations/Configure a Default AI Key.png" alt="Your Account information in Katalon TestOps" width="1080"/>
<p align="center"><em>The AI configuration page.</em></p>

<br/>

### Configure a System Reasoning Model

This AI type ensures structured, logic-driven decision making for automation and execution.

Toggling **Use Katalon Default** will use the default key provided by Katalon for AI-powered features. Otherwise, you can choose your own AI provider. 

1. Select your model from the dropdown menu. Currently, we support:
    - OpenAI 
    - Azure OpenAI

2. Enter your API key in the **API Key** field.

3. Enter your Organization (optional).

4. Click on **Validate Key** to check the validity of your connection.

:::note 
- You may need to enter additional information depending on the AI provider you choose, such as Base URL, API Version, Deployment Name, etc.
:::

5. Click **Update**.

### Results

A notification confirms that you have successfully configured your AI provider.

---

### Configure an LLM Model

This AI type generates human-like responses and interprets requirements to create structured test cases. 

Toggling **Use Katalon Default** will use the default key provided by Katalon for AI-powered features. Otherwise, you can choose your own AI provider.

1. Select your model from the dropdown menu. Currently, we support:
    - AWS Bedrock

2. Enter your AWS Access Key ID in the field of the same name. 

3. Enter your AWS Secret Access Key in the field of the same name.

4. Enter your AWS Region in the field of the same name.

5. Click on **Validate Key** to check the validity of your connection.

6. Click **Update**.

### Results

A notification confirms that you have successfully configured your AI provider.

---

## Manage an AI key

1. To edit an existing AI key, click on the **Edit** button in the rightmost column of the AI key you want to edit.

2. To delete an existing AI key, click on the **Delete** button in the rightmost column of the AI key you want to delete.

<img src="https://tw-cdn.katalon.com/katalon-testops/Administration and Licensing/Manage Systems/Configurations/Manage an AI Key.png" alt="Your AI key configuration option in Katalon TestOps" width="1080"/>
<p align="center"><em>Edit or delete an existing AI key by clicking on their respective buttons.</em></p>


