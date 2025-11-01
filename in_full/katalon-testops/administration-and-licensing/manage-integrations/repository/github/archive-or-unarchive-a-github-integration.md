---
title: "Archive or Unarchive a Github integration"
---

This document shows you how to archive and unarchive a Github integration (project) within Katalon TestOps.

:::info Important
- You must possess the **Project Admin** role to perform this action. Go to [Roles](/katalon-testops/administration-and-licensing/manage-administrators/assign-or-unassign-project-administrators) or [Permissions](/katalon-testops/administration-and-licensing/manage-systems/permissions/about-permissions) for more information or learn how to [assign a Project Admin here.](/katalon-testops/administration-and-licensing/manage-administrators/assign-or-unassign-project-administrators)
:::

## Archive a Github integration

To unarchive a Github integration (project):

1. Go to **Admin > Project > Integrations**.

2. Hover over the right edge of your linked project and click the **Archive** icon.
    <img src="https://tw-cdn.katalon.com/katalon-testops/integration/github/archive-git.png" alt="Confirmed archive box" width="500"/>

3. A confirmation dialog will appear. Click **Archive** if you want to move forward.
    <img src="https://tw-cdn.katalon.com/katalon-testops/integration/github/archive-confirm-box.png" alt="Confirmed unarchive box" width="700"/>


When a project is archived:

- The status changes to **Archived**.
- The project no longer appears in the **Test Cases/Test Suites** module.
- Any scheduled test runs in the **Execution** module will be automatically canceled at runtime.


## Unarchive a Github integration

To unarchive a Github integration (project):

1. Go to **Admin > Project > Integrations**.

2. Hover over the right edge of your linked project and click the **Unarchive** icon.
    <img src="https://tw-cdn.katalon.com/katalon-testops/integration/github/unarchive-git.png" alt="Showing unarchive icon in System Integration list" width="700"/>

3. A confirmation dialog will appear. Click **Unarchive** if you want to move forward.
    <img src="https://tw-cdn.katalon.com/katalon-testops/integration/github/unarchive-confirm-box.png" alt="Confirmed unarchive box" width="700"/>


:::info Note
- After you archive an integration (project), the status might appear as **Inactive**, reload the page to update it to **Active**.
- If the status shows **Error**, verify all required configuration fields and make necessary corrections.
:::