---
title: "Report Uploader Integration"
---

This document shows you how to upload Katalon test reports to Katalon TestOps using Report Uploader.

Report Uploader is a utility to upload reports to Katalon TestOps. The utility supports JUnit, Katalon Studio, and Katalon Recorder report format. It can be used with CLI, Docker, GitHub Action, and other CIs.

## Prerequisites
- Katalon API key – If you haven’t set one up yet, follow this [guide](/katalon-platform/administer/profile/katalon-api-key-in-katalon-testops) to generate your API key.
- Project ID - You can find your Katalon project ID in the URL (typically after `/project/`, e.g., ".../project/1234567/..."), or refer to this [guide](/katalon-platform/administer/administration-and-licensing-alternate/manage-projects/view-project-ids) for more details.

## Upload test reports using Report Uploader in CLI
1. Download [Report Uploader](https://github.com/katalon-studio/report-uploader/releases) and install [Java JRE](https://www.java.com/en/download/manual.jsp) and [Java JDK](https://www.oracle.com/java/technologies/downloads/?er=221886).

2. Get the local path to your Katalon report folders, e.g. `“C:\Users\alex\Katalon Studio\Web Sample\Reports\Test Suite\20190523_143946"` that you want to upload.

3. Run the following command to upload test reports:

    :::note Warning
    You must replace the placeholder values with your actual information for the following fields:
    - `projectId`: Your project ID in Katalon TestOps.
    - `path`: The local path of Katalon Studio Reports folder identified in step 2.
    - `email`: The email registered for your Katalon account. However, this field is **not required** if an API key is used as `password`
    - `password`: The password used for signing in Katalon TestOps or an API Key of that account. Using API key is *recommended* as it will not expose your password.
    - `type`: Select one of the following options:
      - katalon
      - junit
      - katalon_recorder
    - `server`: (Optional) The Katalon TestOps server endpoint, by default it is `https://platform.katalon.com`.
    - `--push-to-xray=true` (Optional): If your TestOps project is integrated with Xray test management, this option enables pushing the test results to Xray.
    :::

    ```jsx
    java -jar katalon-report-uploader-0.0.8.jar
    --projectId=your_project_id
    --path=path/to/test/report
    --password=your_api_key_value
    --type=your_report_type
    ```
## Result
Once executed successfully, the command will upload your report to Katalon TestOps. Navigate to **Reports** to view all uploaded test reports. 