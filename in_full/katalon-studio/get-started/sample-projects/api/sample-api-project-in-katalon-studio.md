---
title: Sample API project in Katalon Studio
---
This sample demonstrates fundamental API testing with RESTful requests. The sample uses the following base URL: [`https://sample-web-service-aut.herokuapp.com`](https://sample-web-service-aut.herokuapp.com/). To learn more about API testing, you can refer to this document: [Introduction to API testing](https://docs.katalon.com/katalon-studio/get-started/supported-applications-under-test-aut/introduction-to-api-testing-in-katalon-studio).

## Open the sample API test project

To open the API sample project, in Katalon Studio, go to **File** > **New Sample Project** > **Sample API Tests Project**.

<img src="https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/api-sample-prj/KS-API-Open-sample-project.png" alt="Open API sample in Studio" width="600" />

<br/>

Alternatively, you can download the sample API test project from our GitHub repository: [Web Service tests](https://github.com/katalon-studio-samples/web-service-tests).

### Trust dialog on first open

When you open a sample project for the first time, Katalon Studio will show a **"Trust and open this project"** dialog. This security prompt ensures you’re aware of the source before opening and potentially executing harmful scripts.

<img alt="Trust dialog when open api sample project" src="https://tw-cdn.katalon.com/katalon-studio/manage-projects/trust-dialog-pop-up/trust-dialog-API-test.png" width="500 " />

In this dialog, you can:

- Review the project path.
- Decide whether to trust this project or all projects inside the parent folder.
:::note Notes
- Trusting a parent folder also trusts all projects directly inside it, including the one you're opening.
- However, if this project contains subfolders with separate project files, those sub-projects won’t be trusted automatically. You'll still see the trust dialog when opening them.
:::

- Click **Trust Project** to continue, or **Don't Open** if you’re unsure.

## Sample API project components in Katalon Studio

### Profiles

To open the execution profile, go to **Profiles > default**.

<img src="https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/api-sample-prj/KS-API-Execution-profile.png" alt="Default profile in the API sample" width="300" />

<br/>

You can create and save all global variables in the execution profile. They can be used across test cases in your project. To learn more about execution profile, you can refer to this document: [Execution profile](https://docs.katalon.com/katalon-studio/data-driven-testing/global-variables-and-execution-profile).

Katalon creates three global variables in this sample project as follows:

| **Name** | **Value** |
| --- | --- |
| baseURL | [`https://sample-web-service-aut.herokuapp.com`](https://sample-web-service-aut.herokuapp.com/) |
| successCode | 200 |
| globalid | 0 |

### RESTful requests

We created two sample RESTful requests in this project: a POST request and a GET request. To access the sample RESTful requests, in the **Test Explorer** panel, go to the **Object Repository** folder.

<img src="https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/api-sample-prj/KS-API-Test-objects.png"  
alt="Test cases" width="400" />

1. The **POST a new user** object
    
    In this sample POST object, we specify the following information:
    
    <img src="https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/api-sample-prj/KS-API-POST-samples-POST-request.png"  alt="Sample POST request"  width="800" />

    
    - **Request method**:
        
        Katalon allows you to choose one of the following methods: GET, POST, PUT, DELETE, PATCH, HEAD, CONNECT, OPTIONS, TRACE. The method needs to match the API endpoint to be a valid request. Here, we create a POST request to send the user information to the server to create an account. The server will return us with a new userID as a response.
        
    - **Request URL**:
        
        Along with the request method, request URL is to tell the web server which API is utilized under test. Any mismatch between method and URL leads to an invalid request exception at runtime or a wrong data response. For the POST request, we specify the API endpoint as follows: `${GlobalVariable.baseUrl}/api/users/json`, where the base URL is listed as a global variable. See above: [Profiles](https://docs.katalon.com/katalon-studio/get-started/sample-projects/api/sample-api-project-in-katalon-studio).
        
        <img src="https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/api-sample-prj/KS-API-POST-Response-URL.png"  alt="Request URL in the sample POST request"  width="800" />


    - **Authorization**:
        
        Authorization is an essential part of an API. It is used to get the correct data under permission (unless the data is public). To learn more about authorization, you can refer to this document: [Authorization](https://docs.katalon.com/katalon-studio/test-objects/api-test-objects/authorization/authorization-in-katalon-studio).
        
        We don't specify any authorization for this POST request.
        
    - **HTTP Header**:
        
        You can configure the header information needed for sending the RESTful request object. By default, the **Content-Type** header is automatically generated from the input in the **HTTP Body** tab. Alternatively, you can select suggested headers from the dropdown list or manually input another header of your interest. To learn more about HTTP headers, you can refer to the Mozilla Developer website here: [HTTP headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers).
        
        Here, we want the HTTP header to be automatically generated by the HTTP body.

        <img src="https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/api-sample-prj/KS-API-POST-HTTP-header.png" alt="HTTP header in the sample POST request" width="600" />
        
    - **HTTP Body**:
    
    Katalon Studio supports the following body data types: text, x-www-form-urlencoded, form-data, and file. To learn more about the types of HTTP body, you can refer to this document: [Request body](https://docs.katalon.com/katalon-studio/test-objects/api-test-objects/rest-request/restful-request#id_2).
    
    Here, we want to send the user information with dynamic data, including username, password, age, gender, and avatar to the server to create new accounts. To do so, we call variables in the POST object, using the `${<variable_name>}` syntax as a placeholder in the HTTP body as follows:
    
    ```
    {
      "age": ${age},
      "avatar": null,
      "gender":"${gender}",
      "password": "${password}",
      "username": "${username}"
    }
    ```
    
    We also check the **Auto update Content Type** box to automatically generate a HTTP header.

    <img src="https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/api-sample-prj/KS-API-POST-HTTP-body.png" alt="HTTP body in the sample POST request" width="600" />

    
    To learn more about setting parameters in a web service object, see [Parameterize a web service object](https://docs.katalon.com/katalon-studio/test-objects/api-test-objects/rest-request/parameterize-a-web-service-object#id_1).
    
    - **Verification**:
    
    Katalon Studio allows you to write verification scripts directly in the **Verification** tab of the web service object. To learn more about the verification snippets, see [Verification snippets](https://docs.katalon.com/katalon-studio/test-objects/api-test-objects/verification-snippets-in-katalon-studio#id_1).

    <img src="https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/api-sample-prj/KS-API-POST-Verification.png" alt="Verification in the sample POST request" width="800" />

    <br/>

    - **Variables**:
    
    To pass the variables value to the POST request, we specify variables in the **Variables** tab. Here, we specify the user information, including `age`, `gender`, `username`, and `password` variables.
    

    <img src="https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/api-sample-prj/KS-API-POST-Variables.png" alt="Variables in the sample POST request" width="800" />

    <br/>

    - **Follow redirects**:
    
    The **Follow redirects** allows you to automatically make a new request when the server responds with a 3xx status. Conversely, you can disable this option to prevent automatically redirecting such requests that return a 3xx series response, you can examine and manage the redirection manually.
    
:::note 
- Starting from Katalon Studio version 9.7.0, the **Follow redirects** checkbox is located under the **Request method** dropdown
:::
    - The **Response** tab:
    
    The response is automatically displayed in a neat format: JSON, XML, HTML, and JavaScript. It is helpful for a quick view of the response status.

    <img src="https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/api-sample-prj/KS-API-Formatter.png" alt="Formatter in the sample POST request" width="800" />

    
1. The **GET user by id** object:
    
    In this sample GET object, we specify the following information:

    <img src="https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/api-sample-prj/KS-API-GET-Sample-GET-request.png" alt="Sample GET request" width="800" />

    <br/>
    
    - **Request method**:
    
    For the sample GET request, we are to retrieve the user information by the userID.
    
    - **Request URL**:
    
    To pass the `id` variable to the GET API, we add the `${<variable_name>}` placeholder at the end of the API endpoint. The API endpoint for the GET request is as follows: `${GlobalVariable.baseUrl}/api/users/${id}`, with the base URL is listed as a global variable.

    <img src="https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/api-sample-prj/KS-API-GET-Response-URL.png" alt="Request URL in the sample GET request" width="800" />

    <br/>
    
    - **Variables**:
    
    We specify the value for the `id` variable in the **Variables** tab.

    <img src="https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/api-sample-prj/KS-API-GET-Variables.png" alt="Variables in the sample GET request" width="800" />

    <br/>

    - **Follow redirects**:
    
    The **Follow redirects** option allows you to automatically make a new request when the server responds with a 3xx status. Conversely, you can disable this option to prevent automatically redirecting such requests that return a 3xx series response, you can examine and manage the redirection manually.
    
    - **Authorization** & **HTTP Header** & **HTTP Body**:
    
    We don't specify any authorization, HTTP header, or HTTP body for this sample GET request.
    

### Custom keywords

You can use custom keywords in the test case. To learn more about custom keywords, you can refer to this document: [Introduction to custom keywords](https://docs.katalon.com/katalon-studio/keywords/custom-keywords/introduction-to-custom-keywords-in-katalon-studio).

Katalon creates two custom keywords in this sample project. To see the custom keywords, in the **Test Explorer** panel, go to **Keywords** > **sample** > **Common.groovy**.

<img src="https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/api-sample-prj/KS-API-Custom-keyword.png" 
alt="Custom keywords in the API project" width="400" />


- **sample.Common.createNewUser**
    
    **Description**
    
    This keyword is to:
    
    - Send the POST request to the server to create an account, then return a userID as the response.
    - Execute verification snippets in the **Verification** tab of the POST request.
    - Extract the new user ID from the response.
    
    **Parameters**
    
    | **Parameter** | **Type** | **Mandatory** | **Description** |
    | --- | --- | --- | --- |
    | age | int | Yes | The age of the user |
    | username | String | Yes | The username for the user account |
    | password | String | Yes | The password for the user account |
    | gender | String | Yes | The gender of the user |
    | expectedStatus | int | Yes | The expected status code of the request |
- **sample.Common.findUserById**
    
    **Description**
    
    This keyword is to:
    
    - Send the GET request to retrieve user information by the userID.
    - Execute verification snippets in the **Verification** tab of the GET request.
    
    **Parameters**
    
    | **Parameter** | **Type** | **Mandatory** | **Description** |
    | --- | --- | --- | --- |
    | id | int | Yes | The id of the new user |
    | age | int | Yes | The age of the user |
    | username | String | Yes | The username for the user account |
    | password | String | Yes | The password for the user account |
    | gender | String | Yes | The gender of the user |
    | expectedStatus | int | Yes | The expected status code of the request |

### Test cases

To access the sample test cases in this project, in the **Test Explorer** panel, go to the **Test Cases** folder.

<img src="https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/api-sample-prj/KS-API-Test-case.png" alt="Test cases" width="400" />

<br/>

There are two test cases for different purposes:

1. The **Create a new user** test case is to create a new user. In the test case, we use the `sample.Common.createNewUser` keyword to:You can see the test script as follows:
    - Send the user information, including username, password, age, gender to the server to create an account. Here, we set the value type of **username**, **password**, **age**, **gender** as **Variable**. You can change the **username**, **password**, **age**, **gender** value in the **Variable** tab. To learn more about test case variables, you can refer to this document: [Test Case Variables](https://docs.katalon.com/katalon-studio/data-driven-testing/test-case-variables).

        <img src="https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/api-sample-prj/KS-830-API-User-info-in-variables.png" alt="User information in the variables tab" width="800" />

        
    - The POST will return a userID as the response.
    - Execute verification snippets in the **Verification** tab of the POST request.
    - Extract the new user ID from the response.
  :::note Notes
    - If you change the user information in the **Variables** tab of the test case, make sure to change the verification snippets in the **Verification** tab of the POST request accordingly for successful verification. For example, if you change the user's age to `10`, then make sure to change the verification of the `age` element to `10`.

        <img src="https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/api-sample-prj/KS-830-API-Matching-value-for-verification.png" alt="A successful verification" width="800" />

        
    :::
    You can see the test script as follows:

    ```
    import static com.kms.katalon.core.checkpoint.CheckpointFactory.findCheckpoint
    import static com.kms.katalon.core.testcase.TestCaseFactory.findTestCase
    import static com.kms.katalon.core.testdata.TestDataFactory.findTestData
    import static com.kms.katalon.core.testobject.ObjectRepository.findTestObject
    import com.kms.katalon.core.checkpoint.Checkpoint as Checkpoint
    import com.kms.katalon.core.cucumber.keyword.CucumberBuiltinKeywords as CucumberKW
    import com.kms.katalon.core.mobile.keyword.MobileBuiltInKeywords as Mobile
    import com.kms.katalon.core.model.FailureHandling as FailureHandling
    import com.kms.katalon.core.testcase.TestCase as TestCase
    import com.kms.katalon.core.testdata.TestData as TestData
    import com.kms.katalon.core.testobject.TestObject as TestObject
    import com.kms.katalon.core.webservice.keyword.WSBuiltInKeywords as WS
    import com.kms.katalon.core.webui.keyword.WebUiBuiltInKeywords as WebUI
    import internal.GlobalVariable as GlobalVariable
    
    CustomKeywords.'sample.Common.createNewUser'(age as Integer, username, password, gender, 200)
    ```
    
1. The **Find user by ID** test case retrieves user information via an **userID**. The flow is as follows:
    - First, we use the `sample.Common.createNewUser` keyword to:
        - Send the user information, including username, password, age, gender to the server to create a new account. Here, we set the value type of **username**, **password**, **age**, **gender** as **Variable**. You can change the **username**, **password**, **age**, **gender** value in the **Variable** tab.
        - The POST request returns a userID as the response.
        - Execute verification snippets in the **Verification** tab of the POST request.
        - Extract the new userID from the response.
    - Then, we use the `sample.Common.findUserById` keyword to:You can see the test script as follows:
        - Send the GET request to retrieve the user information via the newly created userID.
        - Execute verification snippets in the **Verification** tab of the GET request.
:::note Notes 
If you change the user information in the **Variables** tab of the test case, make sure to change the verification snippets in the **Verification** tab of the POST and GET requests accordingly for successful verification. For example, if you change the user's age to `10`, then make sure to change the verification of the `age` element to `10`.
            <img src="https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/api-sample-prj/KS-830-API-Matching-value-for-verification.png" alt="A successful verification"  width="800" />
:::
    You can see the test script as follows:
        ```
        import static com.kms.katalon.core.checkpoint.CheckpointFactory.findCheckpoint
        import static com.kms.katalon.core.testcase.TestCaseFactory.findTestCase
        import static com.kms.katalon.core.testdata.TestDataFactory.findTestData
        import static com.kms.katalon.core.testobject.ObjectRepository.findTestObject
        import com.kms.katalon.core.checkpoint.Checkpoint as Checkpoint
        import com.kms.katalon.core.cucumber.keyword.CucumberBuiltinKeywords as CucumberKW
        import com.kms.katalon.core.mobile.keyword.MobileBuiltInKeywords as Mobile
        import com.kms.katalon.core.model.FailureHandling as FailureHandling
        import com.kms.katalon.core.testcase.TestCase as TestCase
        import com.kms.katalon.core.testdata.TestData as TestData
        import com.kms.katalon.core.testobject.TestObject as TestObject
        import com.kms.katalon.core.webservice.keyword.WSBuiltInKeywords as WS
        import com.kms.katalon.core.webui.keyword.WebUiBuiltInKeywords as WebUI
        import internal.GlobalVariable as GlobalVariable
        import groovy.json.JsonSlurper as JsonSlurper
        import com.kms.katalon.core.testobject.RequestObject as RequestObject
        import static org.assertj.core.api.Assertions.*
        
        int id = CustomKeywords.'sample.Common.createNewUser'(age as Integer, username, password, gender, 200)
        
        CustomKeywords.'sample.Common.findUserById'(id, age as Integer, username, password, gender, 200)
        ```
        

### Data Files

To view the data files in this sample project, in the **Test Explorer** panel, go to **Data Files > ListUser**.

<img src="https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/api-sample-prj/KS-API-Data-files.png" 
alt="Data files in the API sample" width="400" />

<br/>

Alternatively, you can go to `<your-project-folder>\Data Files` and choose the file you want to open:

- `ListUser.dat` is the .dat file of the `ListUser.xlsx` file.
- `ListUser.xlsx` is an excel file that contains the user information.

### Test suites

The sample test suite demonstrates the web service testing with data-driven testing. To view sample test suite, in the **Test Explorer** panel, go to **Test Suite > web-service-tests - All Test Cases**.

This test suite includes the **Create a new user** and **Find user by ID** test case. We bind the **Create a new user** test case with the **ListUser** data file. To view the data binding section, select the **Create a new user** test case, then click **Show Data Binding**. To learn more about binding data, you can refer to the following document: [Data Binding](https://docs.katalon.com/katalon-studio/data-driven-testing/manage-data-binding).

<img src="https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/api-sample-prj/KS-830-API-Test-suite.png" alt="Sample test suites" width="800" />


## Execute selected test cases or test suites

To execute a test case or a test suite in the sample project:

1. Select the test case/test suite you want to execute.
2. Click **Run** or press Ctrl + Shift + A (macOS: Cmd+Shift+A).
    
    You can choose different browsers to execute your test in the dropdown list next to **Run**.

    <img src="https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/api-sample-prj/KS-API-Execution.png" alt="Run the test case" width="200" />

    
3. Observe the test result in the **Log Viewer** tab.**See also:**

    <img src="https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/api-sample-prj/KS-API-Log-viewer.png" alt="Oservice results in the log Viewer" width="800" />
:::note Notes
    - You can view test results of the test suite in the **Result** tab. The test results can be Passed, Failed, Error, or Incomplete.
    - After executing test suites or test suite collections, you can view your reports and details in `<your-project-folder>/Reports`. Katalon Studio also supports exporting test reports into different formats, such as HTML, CSV, PDF, and JUnit.
    - For real-time monitoring and better reporting capabilities, consider integrating your project with Katalon TestOps. Learn more about test result reports here: [Upload Test Results to Katalon TestOps from Katalon Studio](https://docs.katalon.com/katalon-studio/get-started/sample-projects/api/sample-api-project-in-katalon-studio#).
:::
**See also**
- [Create your first API test with Katalon Studio](https://docs.katalon.com/katalon-studio/create-test-cases/create-your-first-api-test-with-katalon-studio)
- [Data-driven testing with RESTful Web Service requests](https://docs.katalon.com/katalon-studio/data-driven-testing/data-driven-testing-with-restful-web-service-requests)