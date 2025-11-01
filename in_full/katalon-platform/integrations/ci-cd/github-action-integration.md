---
title: "Github Action Integration"
---

This document shows you how to upload Katalon test reports to Katalon TestOps using Github Action.

## Prerequisites
- Katalon API key – If you haven’t set one up yet, follow this [guide](/katalon-platform/administer/profile/katalon-api-key-in-katalon-testops) to generate your API key.
- Project ID - You can find your Katalon project ID in the URL (typically after `/project/`, e.g., ".../project/1234567/..."), or refer to this [guide](/katalon-platform/administer/administration-and-licensing-alternate/manage-projects/view-project-ids) for more details.

## Upload test reports using Github Action

1. Get the path to the **Git repository folder** containing the test reports you want to upload.

2. Add the following code snippet to your GitHub Actions workflow file (e.g. `github/workflows/sample-name.yml`):

  :::note Warning
  You must replace the placeholder values with your actual information for the following fields:
    - `PASSWORD`: Enter your Katalon API Key value.
    - `PROJECT_ID`: Enter your Katalon Project ID.
    - `TYPE`: Select one of the following options:
      - katalon
      - junit
      - katalon_recorder
    - `REPORT_PATH`: Enter the local path to your test report.
  :::

    ```yml
    - name: Katalon Report Uploader
    uses: katalon-studio/report-uploader@v0.0.8
    env:
        PASSWORD: your_api_key_value
        PROJECT_ID: your_project_id
        TYPE: your_report_type
        REPORT_PATH: path/to/test/report
    ```

## Result

Once executed successfully, the command will upload your report to Katalon TestOps. Navigate to **Reports** to view all uploaded test reports. 

