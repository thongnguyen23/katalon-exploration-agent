---
title: Create a test project in Katalon Studio
---

To create a test project in Katalon Studio, do as follows:

1. Go to **File** > **New** > **Project** from the main menu.
2. In the displayed **New Project** dialog, enter the name of your project.
    
    <img src="https://docs.katalon.com/46677cc0-2916-11ed-9930-0242fe3e4a3f/ks-850-new-project.png" alt="Create a new project in Katalon Studio" width="500"/>

    
3. Choose a desired project **Type**.
    - **Generic**, **Web**, **Mobile**, **Desktop**: All standard features for Web, Mobile, API, and Desktop testing are available.
    - **API/Web Service**: Exclusive features for API/Web Service Testing are enabled, including icons of importing test requests from [OpenAPI Specifications](https://docs.katalon.com/katalon-studio/test-objects/api-test-objects/import-web-service-objects/import-rest-request-from-openapi), [WADLs](https://docs.katalon.com/katalon-studio/test-objects/api-test-objects/import-web-service-objects/import-restful-requests-from-wadls-to-katalon-studio), [WSDLs](https://docs.katalon.com/katalon-studio/test-objects/api-test-objects/import-web-service-objects/import-soap-requests-from-wsdls-to-katalon-studio), and [Postman](https://docs.katalon.com/katalon-studio/test-objects/api-test-objects/import-web-service-objects/import-web-service-requests-from-soapui-to-katalon-studio); [Request History list](https://docs.katalon.com/katalon-studio/test-objects/api-test-objects/request-history-in-katalon-studio) and more.
4. In the **Project** field dropdown list, you can either choose to create a blank project or a sample project.
    
- If you choose to create a sample project, the Git repository URL of that sample project is retrieved in the **Repository URL** accordingly.
    
:::note

When you create a new project from the sample projects and open it for the first time, Katalon Studio displays a **Trust and open this project dialog**. For more details, see [Trust dialog on first open](https://docs.katalon.com/katalon-studio/manage-projects/manage-test-projects/open-a-test-project-in-katalon-studio#trust-dialog-on-first-open).

:::
    
    
 - If you choose to create a blank project, you can choose whether to generate .gitignore file or build.gradle file.
    
<img src="https://docs.katalon.com/a039c9d0-b5a0-11ed-825f-0242cfbc79b5/ks-855-gitnore.png" alt="Gitignore file option in Katalon Studio" width="500"/>
    
1. In the **Location** field, choose the location for your test where you have all Read & Write permission. Do not store your projects in the Katalon build folder.
2. Enter a brief **Description** for your new project, then click **OK**.

#### Result

Katalon generates a new project accordingly.

## Create API/Web Service project

Katalon Studio supports API/Web Service testing project, which allows separating the API/Web Service testing from Web UI and Mobile testing. You can also perform more API/Web Service automation tasks on Katalon Studio such as Quickstart wizard, import Swagger or WSDL definition File/URL directly, or retrieve the request history at any time.

The update comes with a interface, including a toolbar and a view that serve only for API/Web Service testing.

To create a new API/Web Service project, select **API/Web Service** type in the **New Project** dialog and specify all required project information.
<img src="https://docs.katalon.com/8f428da0-22b2-11ed-9930-0242fe3e4a3f/New-Project.png"alt="New Project dialog in Katalon Studio"width="500"/>
