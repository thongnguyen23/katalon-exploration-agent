---
title: "Set up TrueTest in Salesforce CRM"
---

In Salesforce CRM Lightning, you cannot directly call TrueTest via the code snippet. Instead, you need to call TrueTest through a JavaScript file stored in **Static Resources**. The Lightning page acts as the AUT, where the code snippet tracks user actions for TrueTest to generate corresponding test artifacts.

This guide shows you how to configure TrueTest in Salesforce CRM and verify that it works.  

### Security configurations 

You need to configure security settings to allow the code snippet to run on the Lightning page. Go to the **Setup Menu** and select **Setup**.
<img src="https://tw-cdn.katalon.com/truetest/truetest-salesforce-integration/truetest-salesforce-go-to-step-up.png" alt="Go to Setup page" width="700"/>

- CORS (Cross-Origin Resource Sharing): In the **Setup** page, go to **Security** → **CORS** and add `https://*.katalon.com` to the **Allowed Origins List**. This will allow Katalon domains to communicate with your Salesforce page.
<img src="https://tw-cdn.katalon.com/truetest/truetest-salesforce-integration/truetest-add-new-cors.png" alt="Add Katalon to Allow Origins List" width="700"/>
<img src="https://tw-cdn.katalon.com/truetest/truetest-salesforce-integration/truetest-allow-an-origin.png" alt="Allow Katalon origin" width="700"/>

- CSP (Content Security Policy): In the **Setup** page, go to **Security** → **Trusted URLs** and add `https://*.katalon.com` as a **Trusted URL**.
<img src="https://tw-cdn.katalon.com/truetest/truetest-salesforce-integration/truetest-add-new-trusted-url.png" alt="Add Katalon as trusted URL" width="700"/>
<img src="https://tw-cdn.katalon.com/truetest/truetest-salesforce-integration/truetest-add-new-trusted-url-2.png" alt="Add Katalon as trusted URL" width="700"/>

### Create a JavaScript resource 

Write a JavaScript file to trigger the Agent and upload it to **Static Resources**.  

1. Create a JavaScript file `katalonAgent.js` with the content below, ensure to add your client code at `clientCode=<your client code>`:

```jsx 
console.log('[Katalon] Append Traffic Agent scripts, AI');
const katalonTrafficAgent = document.createElement('script');
katalonTrafficAgent.async = true;
katalonTrafficAgent.defer = true;
katalonTrafficAgent.src = 'https://static.katalon.com/libs/traffic-agent/v1/traffic-agent.min.js?clientCode=<your client code>';
katalonTrafficAgent.id = 'katalonTrafficAgent'
document.head.appendChild(katalonTrafficAgent);
```

1. Go to **Setup** → **Custom Code** → **Static Resources** and create **New**.
<img src="https://tw-cdn.katalon.com/truetest/truetest-salesforce-integration/truetest-static-resources.png" alt="Go to Static Resources" width="700" />

2. Upload your `katalonAgent.js` file as a new static resource.
<img src="https://tw-cdn.katalon.com/truetest/truetest-salesforce-integration/truetest-create-new-static-resources.png" alt=" " width="700" />

### Execute the JavaScript resource from Lightning components 

Call the uploaded JavaScript resource within your Lightning components. 

1. Go to **Setup** → **Developer Console**.
<img src="https://tw-cdn.katalon.com/truetest/truetest-salesforce-integration/truetest-developer-console.png" alt=" " width="400" />
   
2. Go to **File** > **Open Lightning Resources** and select TrueTest component.
<img src="https://tw-cdn.katalon.com/truetest/truetest-salesforce-integration/select-truetest-component.png" alt=" " width="700" />
   
3. Add the following line to your component’s markup:

```jsx
<ltng:require scripts="{!$Resource.TrueTest}" />
```
<img src="https://tw-cdn.katalon.com/truetest/truetest-salesforce-integration/truetest-add-script-to-component.png" alt="Add TrueTest script to the component" width="700" />

### Verify the integration

Go to the Lightning page and open the **Network** tab of the developer tool to ensure the data is sent to Katalon server.
<img src="https://tw-cdn.katalon.com/truetest/truetest-salesforce-integration/truetest-verify-the-integration.png" alt="Verify the integration works" width="700" />
<br/>

If no data is captured, check the **Console** tab for errors.
<img src="https://tw-cdn.katalon.com/truetest/truetest-salesforce-integration/truetest-salesforce-view-error.png" alt="View Console tab for errors" width="700" />
