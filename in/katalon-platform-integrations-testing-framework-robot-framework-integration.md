---
title: "Robot Framework (Python) Integration"
---

This document shows you how to integrate Robot Framework (Pytest) with Katalon TestOps to upload test reports.

## Prerequisites

- Python (pip3) installed on your machine.
- Katalon API key – If you haven’t set one up yet, follow this [guide](/katalon-platform/administer/profile/katalon-api-key-in-katalon-testops) to generate your API key.
- Project ID - You can find your Katalon project ID in the URL (typically after `/project/`, e.g., ".../project/1234567/..."), or refer to this [guide](/katalon-platform/administer/administration-and-licensing-alternate/manage-projects/view-project-ids) for more details.

## Upload Robot Framework test reports to Katalon TestOps

:::info
The step-by-step instructions below use a Katalon [sample project](https://github.com/katalon-studio-samples/katalon-testops-robot-sample) for illustration purposes.
:::

1. **Install dependencies**: Open your source code editor, navigate to your sample project, and run the following command in your terminal:

    ```
    pip3 install testops-robot
    pip3 install -r requirements.txt
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
    <img src="https://tw-cdn.katalon.com/katalon-platform/integration/testing-framework/robot-config.png" alt="Config robot file" width="700"/>

    Replace the placeholder values with your actual details, for example:

    - ``apiKey``: Your Katalon API key (e.g., 1a11111a-1aa1-1a1a-1a1a-a1aaa111111).
    - ``projectId``: Your Katalon project ID (e.g., 1111111).
    - ``reportFolder``: The directory where Pytest will store test report JSON files after execution (default: "testops-report").


3. Run tests and upload reports: In this setup, all test cases are located in the `test_sample` folder. You can choose to run all test cases at once or execute a specific one as needed:
    - All test cases:
    ```jsx
    robot --listener testops.Listener test_sample
    ```
    - Run a single test case (e.g., valid_login_with_AI.robot):
    ```jsx
    robot --listener testops.Listener test_sample/valid_login_with_AI.robot
    ```

## Result

Once the reports are uploaded successfully, navigate to **Reports** to view all the uploaded test reports.

<img src="https://tw-cdn.katalon.com/katalon-platform/integration/testing-framework/robot-uploaded.png" alt="Uploaded robot frameowork test cases" width="700"/>

 