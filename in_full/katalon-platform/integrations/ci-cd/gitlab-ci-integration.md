---
title: "Gitlab CI Integration"
---

This document shows you how to upload Katalon test reports to Katalon TestOps using Gitlab CI.

## Prerequisites
- Katalon API key – If you haven’t set one up yet, follow this [guide](/katalon-platform/administer/profile/katalon-api-key-in-katalon-testops) to generate your API key.
- Project ID - You can find your Katalon project ID in the URL (typically after `/project/`, e.g., ".../project/1234567/..."), or refer to this [guide](/katalon-platform/administer/administration-and-licensing-alternate/manage-projects/view-project-ids) for more details.

## Upload test reports using Gitlab CI

1. Get the local path to your Katalon report folders, e.g. `C:\Users\alex\Katalon Studio\Web Sample\Reports\Test Suite\20190523_143946` that you want to upload.

2. Create an `Environment Variable` in your Gitlab CI configuration for:
```js
KATALON_TESTOPS_APIKEY=your-katalon-api-value
```

3. Copy the following .yml file to your repository that is already synced with Gitlab CI.

  :::note Warning
  You must replace the placeholder values with your actual information for the following fields:
    - `PROJECT_ID`: Enter your Katalon Project ID.
    - `TYPE`: Select one of the following options:
      - katalon
      - junit
      - katalon_recorder
    - `REPORT_PATH`: Enter the local path to your test report.
  :::

    ```yml
    stages:
    - test
    - upload-report

    test:
    stage: test
    image: node:10.15.3
    cache:
        paths:
        - node_modules/
    script:
        - npm install
        - npm test
    artifacts:
        paths:
        - report/
    only:
        - master

    upload-report:
    stage: upload-report
    image: katalonstudio/report-uploader:0.0.8
    script:
        - uploader.sh
    variables:
        PROJECT_ID: your_project_id
        TYPE: your_report_type
        REPORT_PATH: path/to/test/report
        PUSH_TO_XRAY: false
    dependencies:
        - test
    only:
        - master
    ```


## Result

Once executed successfully, the command will upload your report to Katalon TestOps. Navigate to **Reports** to view all uploaded test reports. 

