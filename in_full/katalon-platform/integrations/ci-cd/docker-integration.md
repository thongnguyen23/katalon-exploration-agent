---
title: "Docker Integration"
---

This document shows you how to upload Katalon test reports to Katalon TestOps using Docker.

## Prerequisites
- You have [Docker](https://www.docker.com/) installed and set up.
- Katalon API key – If you haven’t set one up yet, follow this [guide](/katalon-platform/administer/profile/katalon-api-key-in-katalon-testops) to generate your API key.
- Project ID - You can find your Katalon project ID in the URL (typically after `/project/`, e.g., ".../project/1234567/..."), or refer to this [guide](/katalon-platform/administer/administration-and-licensing-alternate/manage-projects/view-project-ids) for more details.

## Upload test reports using Docker

1. Get the local path to your Katalon report folders, e.g. `“C:\Users\alex\Katalon Studio\Web Sample\Reports\Test Suite\20190523_143946"` that you want to upload.

2. Run the following command to upload test reports:

  :::note Warning
  You must replace the placeholder values with your actual information for the following fields:
    - `Report Path (-v path/to/report/)`: Enter the local path to your test report before `:/katalon/report`.
    - `EMAIL`: The email registered for your Katalon account.
    - `PASSWORD`: The password used for signing in Katalon TestOps or an API Key.
    - `PROJECT_ID`: Enter your Katalon Project ID.
    - `TYPE`: Select one of the following options:
      - katalon
      - junit
      - katalon_recorder
  :::
  ```jsx
  docker run -t --rm
    -v path/to/test/report/:/katalon/report
    -e PASSWORD=your_api_key_value
    -e PROJECT_ID=your_project_id
    -e TYPE=your_report_type
    -e REPORT_PATH=/katalon/report //no need to change this
    katalonstudio/report-uploader:0.0.8
  ```

## Result

Once executed successfully, the command will upload your report to Katalon TestOps. Navigate to **Reports** to view all uploaded test reports. 

