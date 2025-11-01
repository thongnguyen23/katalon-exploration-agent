---
title: "Protractor Mocha Integration"
---

This document shows you how to integrate Protractor Mocha with Katalon TestOps to upload test reports.

## Prerequisites

- Node.js and npm installed on your machine.
- Katalon API key – If you haven’t set one up yet, follow this [guide](/katalon-platform/administer/profile/katalon-api-key-in-katalon-testops) to generate your API key.
- Project ID - You can find your Katalon project ID in the URL (typically after `/project/`, e.g., ".../project/1234567/..."), or refer to this [guide](/katalon-platform/administer/administration-and-licensing-alternate/manage-projects/view-project-ids) for more details.

## Upload Protractor Mocha test reports to Katalon TestOps

:::info
The step-by-step instructions below use a Katalon [sample project](https://github.com/katalon-studio/testops-report-js/tree/master/packages/testops-protractor) for illustration purposes.
:::

1. **Install dependencies**: Open your source code editor, navigate to your sample project, and run the following command in your terminal:

    ```
    npm i -s @katalon/testops-mocha @katalon/testops-protractor
    ```

2. **Configure TestOps credentials & project**: 

    a. Create a new file named ```testops-config.json``` in the root directory of your sample project and add the following content:

    ```jsx
    {
        "apiKey": "your_api_key_value",
        "projectId": "your_project_id_value",
        "reportFolder": "testops-report"
    }
    ```

    Replace the placeholder values with your actual details, for example:

    - ``apiKey``: Your Katalon API key (e.g., 1a11111a-1aa1-1a1a-1a1a-a1aaa111111).
    - ``projectId``: Your Katalon project ID (e.g., 1111111).
    - ``reportFolder``: The directory where Protractor Mocha will store test report JSON files (e.g., metadata, results, etc) after execution (default: `testops-report`).
    
    b. **Add reporter**: Create a file named ``protractor-mocha.config.js`` in your root directory and add the following content:

    ```jsx
    exports.config = {
        ...
        framework: "mocha",
        plugins: [
            {
                package: "@katalon/testops-protractor",
            }
        ],
        mochaOpts: {
            timeout: "20s",
            reporter: "@katalon/testops-mocha",
        },
    }
    ```
    <img src="https://tw-cdn.katalon.com/katalon-platform/integration/testing-framework/protractor-mocha-config.png" alt="Config Protractor Mocha file" width="700"/>

    
    c. Configure a proxy **(optional)**: Add the following to `testops-config.json` if a proxy is needed:

    ```jsx
    {
        ...
        "proxy": {
            "protocol": "http or https",
            "host": "your_proxy_host",
            "port": "your_proxy_port",
            "auth": {
                "username": "your_username",
                "password": "your_password"
            }
        }
    }
    ```
3. Run tests and upload reports: You can run your tests and upload reports to Katalon TestOps using either of the following commands:

    - If you have Protractor installed locally 
    ```jsx
    npx protractor
    ```

    -  If you have defined a test script in your package.json:
    ```jsx
    npm test
    ```
## Result

Once the reports are uploaded successfully, navigate to **Reports** to view all the uploaded test reports.

<img src="https://tw-cdn.katalon.com/katalon-platform/integration/testing-framework/pro-mocha-uploaded.png" alt="Uploaded Protractor Mocha file" width="700"/>

 

 