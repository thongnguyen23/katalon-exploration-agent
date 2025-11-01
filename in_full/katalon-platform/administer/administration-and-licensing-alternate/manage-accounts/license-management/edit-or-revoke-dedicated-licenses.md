---
title: Edit or Revoke Dedicated Licenses
---
import useBaseUrl from '@docusaurus/useBaseUrl';

This document shows you how to edit number of dedicated licenses given to organization or revoke them.

A dedicated license is a fixed number of licenses allocated to a specific Organization, limiting how many licenses that Organization can use and manage. Refer to this document to learn more about [Dedicated License](/katalon-platform/administer/administration-and-licensing-alternate/manage-accounts/license-management/assign-dedicated-licenses).

:::tip requirements
You must be assigned the **Account Admin** role to perform this action. Learn more about [roles](/katalon-platform/administer/administration-and-licensing-alternate/manage-systems/permissions/about-roles) and how to [assign Account Admins](/katalon-platform/administer/administration-and-licensing-alternate/manage-administrators/assign-or-unassign-account-administrators).
:::
## Edit Dedicated Licenses

1. Go to **Admin Settings**. You can find Admin Settings at the upper right corner of the page.
2. Click **Account > License Management**.
3. Hover over the Edit icon (pen icon) of the organization you want to edit the dedicated license for.
<br/>
    <img src="https://tw-cdn.katalon.com/katalon-platform/get-started/edit-license.png" alt="Edit dedicated license instructions" width="900"/> <br/>

4. You can increase or decrease the initial license amount:
    For example, if your account has 200 TestOps licenses and you've assigned 5 to an Organization (with 4 already in use):
    - Increasing adds more licenses to the Organization from the Account-level pool (e.g., from the remaining 195).
    - Decreasing reduces the Organization’s allocation:
        - You cannot reduce below the number currently in use.
        - Setting the value to 0 revokes all dedicated licenses from the Organization, including **those in use**.
5. Click **Save** to proceed.

## Revoke Dedicated Licenses

:::info notes
Any claimed or in-use licenses will now be taken from the **Account license pool**, if available.
:::

1. Go to **Admin Settings**. You can find Admin Settings at the upper right corner of the page
2. Click **Account > License Management**.
3. Hover over the Revoke icon (left-arrow icon) of the organization you want to revoke all dedicated licenses from.
    <br/>
    <img src="https://tw-cdn.katalon.com/katalon-platform/get-started/revoke-license.png" alt="Revoke dedicated licenses instructions" width="900"/> <br/>

4. A confirmation box will appear. Click **Revoke** to continue.
