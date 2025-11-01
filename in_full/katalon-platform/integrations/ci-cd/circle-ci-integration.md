---
title: "Circle CI Integration"
---

This document shows you how to upload Katalon test reports to Katalon TestOps using Circle CI.

## Prerequisites
- Katalon API key – If you haven’t set one up yet, follow this [guide](/katalon-platform/administer/profile/katalon-api-key-in-katalon-testops) to generate your API key.
- Project ID - You can find your Katalon project ID in the URL (typically after `/project/`, e.g., ".../project/1234567/..."), or refer to this [guide](/katalon-platform/administer/administration-and-licensing-alternate/manage-projects/view-project-ids) for more details.

## Upload test reports using Circle CI

1. Get the local path to your Katalon report folders, e.g. `“C:\Users\alex\Katalon Studio\Web Sample\Reports\Test Suite\20190523_143946"` that you want to upload.

2. Create an `Environment Variable` in your Circle CI configuration for:
```js
KATALON_TESTOPS_APIKEY=your-katalon-api-value
```

3. Copy the following .yml file to your repository that is already synced with Circle CI.

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
    version: 2.1

    orbs:
    node: circleci/node@4.1.0

    jobs:

    test:
        executor:
        name: node/default
        tag: '10.15.3'
        working_directory: /root/project
        steps:
        - checkout
        - run: |
            set -ex
            npm install
            npm test
        - persist_to_workspace:
            root: /root/project
            paths:
                - report/*

    upload-report:
        docker:
        - image: katalonstudio/report-uploader:0.0.8
        environment:
        PROJECT_ID: your_project_id
        TYPE: your_report_type
        REPORT_PATH: path/to/test/report
        steps:
        - attach_workspace:
            at: /katalon
        - run: uploader.sh

    workflows:
    version: 2.1
    upload-report:
        jobs:
        - test
        - upload-report:
            requires:
                - test
    ```


## Result

Once executed successfully, the command will upload your report to Katalon TestOps. Navigate to **Reports** to view all uploaded test reports. 

