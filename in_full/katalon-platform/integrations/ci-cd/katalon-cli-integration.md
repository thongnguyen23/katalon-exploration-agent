---
title: "Katalon CLI Integration"
---

import useBaseUrl from '@docusaurus/useBaseUrl';


This document shows you how to trigger test execution from existing test schedules on TestOps using Katalon CLI.

The Katalon Command-line Interface (CLI) Docker Image allows you to trigger test execution from existing test schedules on TestOps. You can use this image to integrate with your desired CI/CD pipeline and trigger execution upon code changes.

Katalon CLI is available on Docker Hub: [Katalon CLI](https://hub.docker.com/r/katalonstudio/katalon-cli).

## Prerequisites
- You have [Katalon CLI](https://hub.docker.com/r/katalonstudio/katalon-cli) installed and set up via Docker Hub.
- Katalon API key – If you haven’t set one up yet, follow this [guide](/katalon-platform/administer/profile/katalon-api-key-in-katalon-testops) to generate your API key.
- Project ID - You can find your Katalon project ID in the URL (typically after `/project/`, e.g., ".../project/1234567/..."), or refer to this [guide](/katalon-platform/administer/administration-and-licensing-alternate/manage-projects/view-project-ids) for more details.

## Usage
With Docker installed and running, you can start triggering a schedule.
```jsx
docker run katalonstudio/katalon-cli schedule <parameters>
```
**Parameters**
- `--api-key`: Your Katalon API key value

- `--username` and `--password`: The username and password of your TestOps account.

- `--project-id`: The ID of the project that contains your test schedule. 
<!-- This parameter is not required when using IDS_EXACT_MATCHES for operator. -->

- `--operator=<NAME_CONTAINS | NAME_STARTS_WITH | NAME_ENDS_WITH>`: The operator to filter the schedule, by id or by naming pattern.

- `--values`: The value that corresponds with the operator in use.

**Environment variables**: You can use environment variables instead of parameters.
- API_KEY
- USERNAME
- PASSWORD
- PROJECT_ID
- OPERATOR
- VALUES

<!-- To trigger an existing schedule on TestOps, you need to retrieve the schedule information, specifically the ID of your TestOps project and the ID of the test schedule. -->

<!-- In your TestOps project, go to Executions > Schedules, and select the desired test schedule. -->

<!-- You can find the project ID and schedule ID in the browser's address bar. For example, in the URL `https://testops.katalon.io/team/<team-id>/project/1366723/grid/plan/618831/job`, 
- `1366723` is the project ID.
- `618831` is the schedule ID. -->

<!-- The following is a sample command to trigger an execution from the schedule: -->

<!-- 1. Trigger an execution with **Katalon API key**  and **schedule ID**:
```jsx
docker run katalonstudio/katalon-cli schedule trigger
  --api-key=your_api_key_value
  --operator=IDS_EXACT_MATCHES
  --values="1366723"
``` -->
## Trigger command for TestOps schedules

1. Trigger an execution with **username / password** and **name pattern matching** (`--project-id` is **required**). This command triggers all schedules whose names contain the word "multiple".

```jsx
docker run katalonstudio/katalon-cli schedule trigger 
  --username=sample.email@katalon.com 
  --password=password 
  --project-id=123456 
  --operator=NAME_CONTAINS 
  --values="multiple"
```

## Result
Once executed successfully, the command will upload your report to Katalon TestOps. Navigate to **Reports** to view all uploaded test reports. 

<img src="https://tw-cdn.katalon.com/katalon-platform/integration/testing-framework/Katalon-CLI-uploaded.png" alt="Katalon CLI uploaded files successfully" width="700"/>
