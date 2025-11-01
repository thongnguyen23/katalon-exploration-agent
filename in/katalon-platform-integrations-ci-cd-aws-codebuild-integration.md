---
title: "AWS Codebuild Integration"
---

This document shows you how to upload Katalon test reports to Katalon TestOps using AWS Codebuilder.

## Prerequisites
- Katalon API key – If you haven’t set one up yet, follow this [guide](/katalon-platform/administer/profile/katalon-api-key-in-katalon-testops) to generate your API key.
- Project ID - You can find your Katalon project ID in the URL (typically after `/project/`, e.g., ".../project/1234567/..."), or refer to this [guide](/katalon-platform/administer/administration-and-licensing-alternate/manage-projects/view-project-ids) for more details.

## Upload test reports using AWS Codebuilder

1. Get the local path to your Katalon report folders, e.g. `“C:\Users\alex\Katalon Studio\Web Sample\Reports\Test Suite\20190523_143946"` that you want to upload.

2. Copy the following .yml file to your repository that is already synced with AWS CodeBuild.

  :::note Warning
  You must replace the placeholder values with your actual information for the following fields:
    - `PASSWORD`: Enter your actual Katalon API Key.
    - `PROJECT_ID`: Enter your Katalon Project ID.
    - `TYPE`: Select one of the following options:
      - katalon
      - junit
      - katalon_recorder
    - `REPORT_PATH`: Enter the local path to your test report.
  :::

  ```yml
  version: 0.2

  phases:
    install:
      runtime-versions:
        docker: 18
        nodejs: 10

      commands:
        - node -v

    build:
      commands:
        - npm install && npm test

    post_build:
      commands:
        - |
          set -ex
          export REPORT_PATH=$(pwd)/report
          docker run -t --rm -v \
            $REPORT_PATH: \
            -e PASSWORD=your_api_key_value
            -e PROJECT_ID=your-project-id-value
            -e TYPE=your_report_type
            -e REPORT_PATH=path/to/test/report
            katalonstudio/report-uploader:0.0.8
  cache:
    paths:
      - 'node_modules/**/*'
  ```
## Result

Once executed successfully, the command will upload your report to Katalon TestOps. Navigate to **Reports** to view all uploaded test reports. 

