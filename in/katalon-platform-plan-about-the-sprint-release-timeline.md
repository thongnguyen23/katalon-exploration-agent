---
title: About the sprint/release timeline
---

This document explains how to use the Sprint/Release Timeline in TestOps to plan and manage resources connected to your ALM tools (such as Jira or Azure DevOps) directly within TestOps.

:::tip requirements
Make sure you have connected your ALM tool to TestOps. Sprints must have a start and end date to appear in the timeline. If this information is missing, the sprint may not show up.
- For Jira, refer to this [document](/katalon-platform/integrations/alm-and-test-management/jira-integration).
- For Azure DevOps, refer to this [document](/katalon-platform/integrations/alm-and-test-management/azure-devops-integration).
:::

In the Plans section of TestOps, you can:
- Track release and sprint schedules from your **connected ALM**.
- View upcoming or ongoing sprints in a visual timeline.
- Assign testers to requirements directly within TestOps.

## Use the Sprint/Release Timeline

1. If you have multiple ALM tools connected, select the appropriate integration from the **Integration dropdown** at the top-right of the screen.
2. Click on any sprint or release to open a drawer displaying all linked requirements.
From here, you can:
    - Assign testers: Click the Tester dropdown to assign a user to a requirement.
    - Filter by tester: Use the Filter Tester feature to view only requirements assigned to you or others.

    <video width="600" controls>
        <source src="https://tw-cdn.katalon.com/katalon-platform/create-tests/explore-plans.mov" type="video/mp4" />
    </video>

### View Requirement details
To view a requirement in more detail:

1. Click on the sprint or release that contains the requirement.

2. In the list of requirements, click the name of the one you want to explore. This opens the requirement details page.
    <video width="600" controls>
    <source src="https://tw-cdn.katalon.com/katalon-platform/create-tests/click-linked-plan.mov" type="video/mp4" />
    </video>

### Create or Link existing Test Cases from a Requirement
You can create new test cases or link existing ones directly from a requirement in the **Plans** module:

1. Click on the sprint or release that contains the requirement.
2. In the list of requirements, click the name of the one you want to open. This will take you to the Requirement Details page.

3. To create a new test case, click `+ Create Test Case` and fill in the required fields. The test case will be created automatically.
    <video width="600" controls>
    <source src="https://tw-cdn.katalon.com/katalon-platform/create-tests/create-test-case-from-requirement.mov" type="video/mp4" />
    </video>
4. To link existing test cases, click `Link Test Case`, then select one or more from the list.

    <video width="600" controls>
    <source src="https://tw-cdn.katalon.com/katalon-platform/create-tests/link-test-case-from-requirement.mov" type="video/mp4" />
    </video>

## Keep Your ALM Data in Sync

TestOps syncs with your connected ALM tool in real time to keep your sprint and release data up to date.
If you don’t see recent changes (like a newly created sprint or updated requirement), click the **Sync** button at the top right of the timeline to manually sync the data.

<img src="https://tw-cdn.katalon.com/katalon-platform/create-tests/sync-button.png" alt="Navigate to sync button - Plan module" width="400"/>
