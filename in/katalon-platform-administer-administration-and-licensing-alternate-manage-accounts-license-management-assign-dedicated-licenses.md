---
title: Assign Dedicated Licenses to Organization
---
import useBaseUrl from '@docusaurus/useBaseUrl';


This document shows you what is dedicated license and how to assign them to organization(s).

:::tip requirements
You must be assigned the **Account Admin** role to perform this action. Learn more about [roles](/katalon-platform/administer/administration-and-licensing-alternate/manage-systems/permissions/about-roles) and how to [assign Account Admins](/katalon-platform/administer/administration-and-licensing-alternate/manage-administrators/assign-or-unassign-account-administrators).
:::

## What is a Dedicated License?

A dedicated license is a fixed number of licenses allocated to a specific Organization, limiting how many licenses that Organization/sub-Organization can use and manage. 

When you purchase Katalon licenses, they are added to your Account-level license pool by default. This pool is shared across all users in the account, making licenses accessible to everyone. To streamline license management, we recommend grouping users into Organizations or sub-Organizations. Once organizations are in place, you can:

1. Assign dedicated licenses to each Organization or sub-Organization.
2. Define limits on how many licenses each group can access and manage.
---
### Examples
The following examples illustrate how dedicated licensing functions across Accounts, Organizations, and Sub-Organizations:

First example: This account has 200 TestOps licenses. They assign 20, 10, 1, and 5 licenses to four Organizations, respectively. These numbers represent the dedicated licenses each Organization can use and they cannot exceed that amount.

<img src="https://tw-cdn.katalon.com/katalon-platform/admin/license-pool-account.png" alt="License management page" width="900"/> <br/>

- **Dedicated**: The total number of licenses explicitly assigned to an Account, Organization, or Sub-Organization.
- **Pool**: The number of licenses still available after allocation to sub-levels (e.g., from Account to Organization, or Organization to Sub-Organization).
- **Assigned User**: The number of users who have actively claimed a license in that specific level.
- **Available**: The number of unclaimed licenses remaining at that level, ready to be assigned to users.
---
Second example: This Organization receives 10 dedicated licenses. It then assigns 5 licenses to a sub-Organization, reducing its remaining pool to 5 licenses.

<img src="https://tw-cdn.katalon.com/katalon-platform/admin/suborg-pool.png" alt="Sub org license pool UI" width="900"/> <br/>

If they later create a second sub-Organization, they can assign it up to 5 licenses, depending on what's left in the parent Organization’s pool.

---

## Assign Dedicated Licenses

To assign licenses to an Organization that **has not** received any dedicated licenses yet:

1. Click **Assign Dedicated Licenses**.
<img src="https://tw-cdn.katalon.com/katalon-platform/get-started/dedicated-license.png" alt="License management page" width="900"/> <br/>

2. Select an Organization from the dropdown, enter the amount, and click **Assign**.

<img src="https://tw-cdn.katalon.com/katalon-platform/get-started/assign-dedicated.png" alt="Assign license to organization box" width="900"/> <br/>
