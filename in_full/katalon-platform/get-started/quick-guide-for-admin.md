---
title: Quick guide for administrators
---
:::info note
For the legacy version of this guide, refer to this [document](/katalon-platform/get-started/quick-guide-for-administrators).
:::
This quick guide helps administrators set up and manage Katalon accounts, organizations, projects, licenses, and users effectively.

**Recommended Setup Flow** after initial purchase:

1. Set Up General Account – Define account details for alignment with your organization’s identity.
2. Configure Security Settings – Set up a custom domain and complete other mandatory security configurations.
3. Create an Organization or sub-Organization (or a Project) – Projects must always reside within an Organization or sub-Organization.
4. Assign Dedicated Licenses – Assign dedicated licenses to specific organizations or sub-Organizations.
5. Invite Users – Add users to organizations or projects.
6. Assign Licenses to Users – Grant users licenses from the organization’s pool.

## Requirements
- You have created a Katalon account. [Register for a Katalon account](https://www.katalon.com/sign-up/) if you don't have one.
- You must be assigned the **Account Admin** role to perform this action.

## Set up Account's General Information
Start by defining your account details and ensuring the system aligns with your organization’s identity.
1. Go to **Admin Settings > Organization**. You can find **Admin Settings** in the upper-right corner of the page, indicated by a cog icon.
2. Click **Account > General**.
3. Click on the **Edit Account Information** button located at the upper right corner of your account's information box.
    <img src="https://tw-cdn.katalon.com/katalon-platform/admin/user-management/edit-account-info.png" alt="Click edit account info button" width="700"/>

4. The **Edit Account Information** dialog box pops up. Input or edit your information as required.
    <img src="https://tw-cdn.katalon.com/katalon-testops/Administration and Licensing/Manage Accounts/General/Admin Account General Edit.png" alt="The account information box in Katalon TestOps" width="700"/>
5. Click **Save**.

## Create Organizations, sub-Organizations, or Projects
Organizations and sub-Organizations represent your company’s structure (departments, teams). Projects must always reside within an Organization or sub-Organization.

1. Go to **Admin Settings**. You can find Admin Settings at the upper right corner of the page
2. Click **Org > Organization Management**

3. Click on `+ Create`. Select **Organization** from the dropdown.
    <img src="https://tw-cdn.katalon.com/katalon-platform/get-started/create-org.png" alt="Create org instructions" width="700"/> <br/>
4. Input the name you want.
5. Under **Parent Organization**, select your Account to create a new Organization, or choose an existing Organization to create a sub-Organization.
6. Click **Create** to finish.
    <img src="https://tw-cdn.katalon.com/katalon-platform/get-started/create-org-box.png" alt="Create org box pop up" width="700"/> <br/>

To create a Project
1. Go to **Admin Settings**. You can find Admin Settings at the upper right corner of the page
2. Click **Org > Organization Management**

3. Click on `+ Create`. Select **Project** from the dropdown.
    <img src="https://tw-cdn.katalon.com/katalon-platform/get-started/create-org.png" alt="Create org instructions" width="700"/> <br/>
The Create Project dialog box appears. Input the requested information:
- Name
- Description
- Admin: The users you would like to assign as Project Admins.
- Parent organization: The Organization to which you would like to add this project to.
4. Click **Create**.
---
## License Management
Licenses are provisioned at the **Account-level** by default. You may either:

- Use the default setting (licenses consumed at **Account-level**), or
- Assign dedicated licenses to Organizations/sub-Organizations and consume from there for tighter governance (**recommended**).
### Dedicated Licenses Explained

A dedicated license is a fixed number of licenses allocated to a specific Organization, limiting how many licenses that Organization/sub-Organization can use and manage. 

When you purchase Katalon licenses, they are added to your **Account-level license pool** by default. This pool is shared across all users in the account, making licenses accessible to everyone. To improve license governance, you can assign dedicated licenses to Organizations and sub-Organizations.

Once Organizations are set up, you can:

1. Assign dedicated licenses to each Organization or sub-Organization.
2. Define limits on how many licenses each group can access and manage.

#### Examples 1
The following examples illustrate how dedicated licensing functions across Accounts, Organizations, and Sub-Organizations:

First example: This account has 200 TestOps licenses. They assign 20, 10, 1, and 5 licenses to four Organizations, respectively. These numbers represent the dedicated licenses each Organization can use and they cannot exceed that amount.

<img src="https://tw-cdn.katalon.com/katalon-platform/admin/license-pool-account.png" alt="License management page" width="900"/> <br/>

- **Dedicated**: The total number of licenses explicitly assigned to an Account, Organization, or Sub-Organization.
- **Pool**: The number of licenses still available after allocation to sub-levels (e.g., from Account to Organization, or Organization to Sub-Organization).
- **Assigned User**: The number of users who have actively claimed a license in that specific level.
- **Available**: The number of unclaimed licenses remaining at that level, ready to be assigned to users.

#### Examples 2
This Organization receives 10 dedicated licenses. It then assigns 5 licenses to a sub-Organization, reducing its remaining pool to 5 licenses.

<img src="https://tw-cdn.katalon.com/katalon-platform/admin/suborg-pool.png" alt="Sub org license pool UI" width="900"/> <br/>

If they later create a second sub-Organization, they can assign it up to 5 licenses, depending on what's left in the parent Organization’s pool.

---

### Assign Dedicated Licenses to Organization

To assign licenses to Organization that **has not** received any dedicated licenses yet:

1. Click **Assign Dedicated Licenses**.
    <img src="https://tw-cdn.katalon.com/katalon-platform/get-started/dedicated-license.png" alt="License management page" width="900"/> <br/>
2. Select an Organization from the dropdown, enter the amount, and click **Assign**.
    <img src="https://tw-cdn.katalon.com/katalon-platform/get-started/assign-dedicated.png" alt="Assign license to organization box" width="900"/> <br/>

### Edit Dedicated Licenses given to Organization

This section shows you how to edit number of dedicated licenses given to organization.
1. Go to **Admin Settings**. You can find Admin Settings at the upper right corner of the page.
2. Click **Account > License Management**.
3. Hover over the Edit icon (pen icon) of the organization you want to edit the dedicated license for.
    <img src="https://tw-cdn.katalon.com/katalon-platform/get-started/edit-license.png" alt="Edit dedicated license instructions" width="900"/>
4. You can increase or decrease the initial license amount:
    For example, if your account has 200 TestOps licenses and you've assigned 5 to an Organization (with 4 already in use):
    - Increasing adds more licenses to the Organization from the Account-level pool (e.g., from the remaining 195).
    - Decreasing reduces the Organization’s allocation:
        - You cannot reduce below the number currently in use.
        - Setting the value to 0 revokes all dedicated licenses from the Organization, including **those in use**.
5. Click **Save** to proceed.

### Revoke Dedicated Licenses from Organization
If needed, you can revoke all dedicated licenses from an Organization:
:::info notes
Any claimed or in-use licenses will now be taken from the **Account license pool**, if available.
:::

1. Go to **Admin Settings**. You can find Admin Settings at the upper right corner of the page
2. Click **Account > License Management**.
3. Hover over the Revoke icon (left-arrow icon) of the organization you want to revoke all dedicated licenses from.
    <img src="https://tw-cdn.katalon.com/katalon-platform/get-started/revoke-license.png" alt="Revoke dedicated licenses instructions" width="900"/> <br/>
4. A confirmation box will appear. Click **Revoke** to continue.
## User Management

### Invite users to join an Organization
As an administrator, you can invite new users to join your organization and immediately assign them licenses (Given if you have already assigned dedicated licenses to your Organization)

1. Go to **Admin Settings**. (You can find Admin Settings at the upper right corner of the page).
2. Click **Org > User Management** tab. The user directory appears with all users in a list.
3. Click **+ Add user**. The Add Users dialog box appears.
   <img src="https://tw-cdn.katalon.com/katalon-platform/get-started/add-user.png" alt="Add users to Katalon TestOps." width="800"/>
4. Input the email addresses of the Users you would like to invite.
   - Separate entries by pressing space or enter.
   - You can copy-paste email entries.

### Assign licenses during user invitation
5. Select the licenses you want to assign by checking the boxes.

   The license source in the dropdown indicates where the licenses are available within the Account.<br/>    
<img src="https://tw-cdn.katalon.com/katalon-testops/Administration and Licensing/Manage Organizations/User Management/Add Users Dialog Box.png" alt="Add users to Katalon TestOps and assign licenses to them instantly. Choose the source of the licenses through the dropdown." width="600"/>

<br/>

6. (Optional) Select the Organization you would like these Users to belong to.
7. (Optional) Select the Project you would like these Users to work on.
8. Click **Add** to proceed.

### Assign licenses after invitation

If the user is already existing in your account:

1. Go to **Admin Settings**. (You can find Admin Settings at the upper right corner of the page).
2. Click **Org > User Management** tab. The user directory appears with all users in a list.
   <img src="https://tw-cdn.katalon.com/katalon-platform/admin/user-management/user-management-ui.png" width="900" alt="Navigate to user management UI" /> <br/>
3. Locate the user you want to assign a license to and open their detail page.
4. Click **Change** next to the license type.
5. Select a license source from the available pools in your Account.

<img src="https://tw-cdn.katalon.com/katalon-platform/get-started/assign-license-profile.png" alt="Assign licenses from user profile" width="900"/>

### View the User Detail Page

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

### Change a User's Account Roles
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

### Change a User's Project Roles

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

### Change a User's Organization

To change a user's Organization:
1.  Click on the **Change** button under the label Organization.
    <img width="700" src="https://tw-cdn.katalon.com/katalon-platform/admin/user-management/change-org.png" alt="Click change org"/>

2. The **Change Organization** dialog box appears. Select the new Organization from the dropdown menu.

    <img width="700" src="https://tw-cdn.katalon.com/katalon-platform/admin/user-management/change-org-dropdown.png" alt="Change org dropdown"/>

3. Click **Save**.

### Resend invitation to a user

If the invitation link expires and the user hasn't accepted it, you can resend the invitation.
1. Locate the user with the **Pending** status.
2. Hover at far right end of that user's row. Click **Resend invitation** or **Copy invitation link**.

    <img src="https://docs.katalon.com/eece300c-0e59-463e-8cea-c399d0296b30/testops-gen3-resend-invitation.png" alt="click resend invitation" width="700" />

### Deactivate a user
This document shows you how to remove/deactivate a user from your Account.

1. Navigate to your chosen user's User Detail page.
2. Click the three-dot menu button at the upper right corner of the information box, then select **Deactivate User**.
    <img width="700" src="https://tw-cdn.katalon.com/katalon-platform/admin/user-management/deactivate.png" alt="Deactivate a user"/>

3. The Deactivate User From Account dialog box appears. Continue by clicking **Deactivate**.
    <img width="500" src="https://tw-cdn.katalon.com/katalon-platform/admin/user-management/deactivate-confirm.png" alt="Deactivate a user confirmation"/>

4. Their Status is now **Inactive**. 

<img src="https://docs.katalon.com/10670ee9-d4bc-400e-a224-4206ae127298/TO3B3_User_Directory_Censored.png" alt="inactive status" width="500" />
