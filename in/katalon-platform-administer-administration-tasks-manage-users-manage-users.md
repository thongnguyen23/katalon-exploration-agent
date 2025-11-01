---
title: Manage users (Legacy)
---
import Reusable from '@site/src/reusable/Reusable.mdx';

<Reusable />
The following article shows you how to invite new users and manage your users within your Organization.

---
## Requirements
You must be the Owner or Admin of your Organization.

---
## Invite users to join an Organization
To work with your team on a project, start by adding them to your Organization.

Follow these steps to add users to your Organization:

1. Sign in to [TestOps Admin](https://my.katalon.com/) and select your desired Account.
2. In your Account admin page, select your Organization.
<img src="https://docs.katalon.com/5062d860-bf78-11ee-ac6d-0242c7a41fd4/KT-Acount-page.png" width="700" alt="View user management settings in Katalon TestOps."/> <br/>

3. Select **Users** to open the **User Management** page. Click the **Invite Users** button at the top right corner.
<img src="https://docs.katalon.com/507dda70-bf78-11ee-ac6d-0242c7a41fd4/KT-_Users_page.png" alt="View the user management menu in Katalon TestOps" width="700" /> <br/>

4. Before you perform this step, we highly suggest that you plan which group of users you want to assign specific licenses and teams to.

    On the **Invite Users to Organization** window, enter your user's email address. Then, click **Next**.
    You can enter multiple email addresses to invite multiple users at once (separate by commas).

<img src="https://docs.katalon.com/508f4ed0-6650-11ee-bc04-0242c7a41fd4/KT-Oct09-Invite_users_to_Organization.png" alt="Invite users to your Katalon TestOps organization." width="700" />

5. On the **Team and Licenses**  window, assign teams and licenses to your users.
<img src="https://docs.katalon.com/5086c350-6650-11ee-bc04-0242c7a41fd4/KT-Oct09-Team_and_License-01.png" width="700" alt="Add users to Teams and Licenses" /> <br />        a. In **Add users to teams** section, select one or multiple teams you wish to assign to your users.
            
            In case your Organization have no team, you can create a new team by clicking Create a team. Refer to the following topic for the next steps: [Create a Team](/katalon-platform/administer/administration-tasks/manage-projects-and-teams/set-up-teams#task-9332).
            
            <img src="https://docs.katalon.com/505be2c0-6650-11ee-bc04-0242c7a41fd4/KT-Oct09-Invite_to_Team.png.png" alt="Add users to 1 or multiple team" width="600" />
    
        b. In **Select licenses** section, select the type of licenses you wish to award to your users. You can change these settings later in the **License Management** section.

6. When you're done, click **Confirm**.
#### Result
- If the email domain of the invited users is not a public one (e.g., `@gmail.com`) and matches the email domain of either the Account/Organization Owner or the inviter, the invited users will promptly become active users of your Organization.

- In contrast, other users will receive an invitation email to join your organization. Once these users accept your invitation, they then become users of your Organization.

    You can track their pending invitations in **Pending Invitation** section. You can also refer these users to view this topic for more information: [Join a TestOps Organization](/katalon-platform/administer/administration-tasks/join-an-organization).

**Note**: In case your invited users have not received the email, make sure that they check their spam inbox or ensure that the Katalon Platform email address is whitelisted.

## Manage users
After inviting new users to your Organization successfully, the Owner or Admin can manage their users on the **User Management** page. The following guide shows you how to manage users and pending invitations.
:::tip Requirements
You must be the Owner or Admin of your Organization.
:::
### View the active users list
Go to the **User Management** page, the **Active Users** tab displays.

<img src="https://docs.katalon.com/57cdac80-bf80-11ee-ac6d-0242c7a41fd4/KT-_Users_page1.png" width="700" alt="View active user list" /> <br/>
You then can view the list of all existing users.

Once your team members have accepted the invitations to join your Organization, you will see their full names, emails, roles, the dates they joined your organization, their license access, and their most recent access to the organization in the **Active Users** section.

You can update their permissions by changing their roles.

### Change user role
In an organization, different roles have different permissions. Learn how to change roles and permissions for a user.

----
#### Requirements
- You must have [invited users to join an organization](/katalon-platform/administer/administration-tasks/manage-users#invite-users-to-join-an-organization) first. To learn more about roles and permissions, see: [Administrative Roles and Permissions](/katalon-platform/administer/administration-roles/administrative-roles-and-permissions).

- The Owner has the highest level of permissions. This is the default role for the first member of any Organization.
----
Change the role of an existing user by following these steps:
1. Go to the **User Management** page.
2. Select the checkbox next to the user's name then click on the **Change Role** button.

    You can select multiple checkboxes if you want to update the same role for multiple users.

    <img src="https://docs.katalon.com/507500d0-bf78-11ee-ac6d-0242c7a41fd4/KT-Change_role.png" alt="Change your user's roles." width="700" />

3. The **Change User Role** dialog pops up. Double-check the email addresses then select a new role in the dropdown list.
    <img src="https://docs.katalon.com/50471300-bf78-11ee-ac6d-0242c7a41fd4/KT-Change_user_role_dialog.png" alt="Change user role dialog" width="400" />

4. Click **Change Role** to confirm your action.

#### Result 
You have now changed you users' roles.

### Remove existing users

:::info notes
- When you remove a user from your Organization, that user can no longer log in to your Organization.
- After being removed, users' assigned licenses are revoked and their associated machine IDs are removed from the Registered Machine list.
- The data that was used by removed users is retained and remains accessible within your Organization.
- In case removed users are the Owner of any Projects, this role will be transferred to the Organization Owner.
- Removed users can be invited back any time, but they will have to go through the invitation process again.
:::
To remove existing users, do as follows:

1. Go to the **User Management** page.
2. Select the checkbox next to the user's full name that you want, then click the **Remove Users** button.

    You can remove multiple users by selecting multiple checkboxes.
    <img src="https://docs.katalon.com/57ae64b0-bf80-11ee-ac6d-0242c7a41fd4/KT-Revoke.png" alt="Remove users button" width="500" />

3. The **Remove Users** dialog pops up. Double-check the email addresses and click Remove to confirm your action.

    <img src="https://docs.katalon.com/57f22470-bf80-11ee-ac6d-0242c7a41fd4/KT-Remove_users_dialog.png" alt="Remove users dialog" width="400" />

#### Result 
You have removed the users.

### Export user list
To export your user list, do as follows:
1. Go to the **User Management** page then click **Export Users** at the top right corner.
<img src="https://docs.katalon.com/57df5fc0-bf80-11ee-ac6d-0242c7a41fd4/KT-_Export_users.png" alt="Export user list" width="700" />

2. The user list is exported in .csv format. The exported file contains **Active Users** list and **Removed Users** list.
### View pending invitations
:::info notes
If the email domain of the invited users is a public one (e.g., `@gmail.com`) or does not match the email domain of either the Account/Organization Owner or the inviter, the invited users will receive an invitation email to join an Organization. The pending invitations will be recorded for tracking.
:::

Go to the **User Management** page and switch to the **Pending Invitation** tab. You can check all pending invitations here.

<img src="https://docs.katalon.com/57d63800-bf80-11ee-ac6d-0242c7a41fd4/KT-Pending_invitation.png" alt="Pending invitation" width="700" />

### Revoke invitations
Follow these steps to revoke pending invitations.
1. Click on the **Pending Invitation** tab on the **User Management** page.
2. Select the checkbox next to the user's full name that you want, then click the **Revoke** button.
    You can revoke multiple invitations by selecting multiple checkboxes.

    <img src="https://docs.katalon.com/57c3c170-bf80-11ee-ac6d-0242c7a41fd4/KT-Revoke_invitations.png" alt="To revoke the invitation" width="500" />
3. The **Revoke Invitation** dialog pops up. Double-check the email addresses, then click **Revoke**.
    <img src="https://docs.katalon.com/57fa13b0-bf80-11ee-ac6d-0242c7a41fd4/KT-Revoke_invitations_dialog.png" alt="Revoke invitation dialog" width="500" />

#### Result
You have revoked the invitations. The invitation links your team members have received now become invalid.
### View the removed user list
Go to the **User Management** page and click on the **Removed Users** tab. By default, the list is sorted by **JOIN DATE**.

You can view a full list of users you have removed from your Organization.

<img src="https://docs.katalon.com/58031460-bf80-11ee-ac6d-0242c7a41fd4/KT-Removed_users_list.png" alt="Removed users tab" width="700" />
