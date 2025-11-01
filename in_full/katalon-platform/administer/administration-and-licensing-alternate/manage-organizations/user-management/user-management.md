---
title: "User Management"
---

This document shows how to view user details, manage roles, change organizations, resend invitations, and deactivate users from the User Management page.

:::tip requirements
You must be assigned the **Account Admin** role to perform these actions. Learn more about [roles](/katalon-platform/administer/administration-and-licensing-alternate/manage-systems/permissions/about-roles) and [permissions](/katalon-platform/administer/administration-and-licensing-alternate/manage-systems/permissions/about-permissions) or how to [assign an Account Admin here](/katalon-platform/administer/administration-and-licensing-alternate/manage-administrators/assign-or-unassign-account-administrators).
:::

## View the User Detail Page

1. Go to **Admin Settings > Organization**. You can find **Admin Settings** in the upper-right corner of the page, indicated by a cog icon.
2. Click **Org > User Management**.
3. In the user directory, click on the name of the user whose details you want to view.

<img width="700" src="https://tw-cdn.katalon.com/katalon-platform/admin/user-management/user-management.png" alt="User Detail Page Screenshot"/>

The **User Detail** page displays the following information:

- **Full name**
- **Profile picture**
- **Contact details**
- **Employment start date**
- **Account-level role** – Determines if the user is an account-level admin
- **Affiliated Organization** – The organization the user belongs to
- **Licenses possessed** – Includes sources like:
    - TestOps - License Source
    - KSE License Source
    - TestOps Guest - License Source
- **Joined Projects List** – Projects the user is a member of

<img width="700" src="https://tw-cdn.katalon.com/katalon-platform/admin/user-management/user-info.png" alt="User Detail Page Screenshot"/>

## Change a User's Account Roles
To change a user's Account roles:
1. Go to **Admin Settings > Organization**. You can find **Admin Settings** in the upper-right corner of the page, indicated by a cog icon.
2. Click **Org > User Management**.
3. In the user directory, click on the name of the user whose details you want to view.

<img width="700" src="https://tw-cdn.katalon.com/katalon-platform/admin/user-management/user-management.png" alt="User Detail Page Screenshot"/>

4. Click on the **Change Role & Permission**  under the label Account Role
<img width="700" src="https://tw-cdn.katalon.com/katalon-platform/admin/user-management/change-user-roles.png" alt="Click change role and permissions account"/>

5. The **Change Role and Permission** dialog box appears. Click on the dropdown menu at the upper left corner and assign roles as needed.
<img src="https://docs.katalon.com/c44e07e2-ed8d-4d5d-86e0-922bde4b7b28/TO3B3_Change_Role_and_Permission_Dropdown.png" alt="Change roles and permission dropdown" width="700"/>

6. Click **Update**.

## Change a User's Project Roles

To change a user's Project roles:
1. Go to **Admin Settings > Organization**. You can find **Admin Settings** in the upper-right corner of the page, indicated by a cog icon.
2. Click **Org > User Management**.
3. In the user directory, click on the name of the user whose details you want to view.

<img width="700" src="https://tw-cdn.katalon.com/katalon-platform/admin/user-management/user-management.png" alt="User Detail Page Screenshot"/>

4.  Click on the **Change Role and Permission** button that corresponds to the same row of the Project you'd like to change the User's permissions in.

    <img width="700" src="https://tw-cdn.katalon.com/katalon-platform/admin/user-management/change-roles-project.png" alt="Click change role and permissions project"/>

5. The **Change Role and Permission** dialog box is displayed. In the dropdown labeled Project Role, select the Roles you'd like to add for the User.

    <img src="https://docs.katalon.com/055440df-13ae-4c30-8be6-7e9e37e04689/TO3G1_Project_Role_Selection.png" alt="Change roles and permissions dropdown" width="700" />

6. Click **Update**.

## Change a User's Organization

To change a user's Organization:
1.  Click on the **Change** button under the label Organization.
    <img width="700" src="https://tw-cdn.katalon.com/katalon-platform/admin/user-management/change-org.png" alt="Click change org"/>

2. The **Change Organization** dialog box appears. Select the new Organization from the dropdown menu.

    <img width="700" src="https://tw-cdn.katalon.com/katalon-platform/admin/user-management/change-org-dropdown.png" alt="Change org dropdown"/>

3. Click **Save**.

## Resend invitation to a user

If the invitation link expires and the user hasn't accepted it, you can resend the invitation.
1. Locate the user with the **Pending** status.
2. Hover at far right end of that user's row. Click **Resend invitation** or **Copy invitation link**.

    <img src="https://docs.katalon.com/eece300c-0e59-463e-8cea-c399d0296b30/testops-gen3-resend-invitation.png" alt="click resend invitation" width="700" />

## Deactivate a user
This document shows you how to remove/deactivate a user from your Account.

1. Navigate to your chosen user's User Detail page.
2. Click the three-dot menu button at the upper right corner of the information box, then select **Deactivate User**.
    <img width="700" src="https://tw-cdn.katalon.com/katalon-platform/admin/user-management/deactivate.png" alt="Deactivate a user"/>

3. The Deactivate User From Account dialog box appears. Continue by clicking **Deactivate**.
    <img width="500" src="https://tw-cdn.katalon.com/katalon-platform/admin/user-management/deactivate-confirm.png" alt="Deactivate a user confirmation"/>

4. Their Status is now **Inactive**. 

<img src="https://docs.katalon.com/10670ee9-d4bc-400e-a224-4206ae127298/TO3B3_User_Directory_Censored.png" alt="inactive status" width="500" />
