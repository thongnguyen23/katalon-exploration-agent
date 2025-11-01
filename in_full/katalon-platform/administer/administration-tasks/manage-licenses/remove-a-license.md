---
title: Remove a License (Legacy)
---
import Reusable from '@site/src/reusable/Reusable.mdx';

<Reusable />

:::tip tips
Contact us at license@katalon.com if you need further help with your licenses.
:::
## Requirements

You must be the Owner or Administrator of your organization to access the **License Management** page. For further details on roles and user management, see: [TestOps User Management](/katalon-platform/administer/administration-tasks/manage-users/manage-users).

---

On the **License Management** page, you can remove a Licensed User, a machine ID, or a license from a machine ID. To access the **License Management** page, do as follows:

1. Sign in to [TestOps Admin](https://my.katalon.com/) and select your Account.

2. From the Account admin page, select your Organization.

3. Select **License** on the sidebar to open the **License Management** page.

    <img src="https://docs.katalon.com/ba3f06a0-bfe6-11ee-ac6d-0242c7a41fd4/KT-_License_Management_page.png" alt="License Management page" />

## Remove Katalon Studio Enterprise (KSE) license from assigned user
You can remove a license to revoke a user's access to certain paid features. This step is only applicable to Katalon Studio Enterprise (KSE).

This action removes a license associated with a machine ID. The removed license is then available to be reassigned. The user who previously used the license is converted to a free user.

:::warning Notice
- The Owner or Admin of an Organization needs to ensure all of their users have a KSE license to avoid mixed free Katalon Studio and KSE licenses within an Organization. For further information, refer to the Free Offerings term in Terms of Use.
- By clicking Remove, you immediately terminate the current session that user is working on with their online licenses. Be cautious when exercising this step.
- Removing a Licensed User working with an offline license does not revoke the license.
:::

1. Go to the **License Management** page.
2. In the **Licenses Users** section, select the checkbox next to the user whose KSE license you want to remove, then click **Revoke License**.
You can select multiple or all users.
    <img src="https://docs.katalon.com/0a187e30-76f0-11ee-8403-0242c7a41fd4/KT-Revoke_KSE_licenses.png" alt="Revoke license in the license management page." />

3. A pop-up will ask you to confirm your action. Click **Remove**.

    <img src="https://docs.katalon.com/0a09d830-76f0-11ee-8403-0242c7a41fd4/KT-_Revoke_users_licenses.png" alt="Confirmation to remove a user from their associated license." />
#### Result
You have removed your user from using a KSE license. You can now reassign it to other users or save it for future use.

## Remove a license
This action removes a license associated with a machine ID. This license is then available to be attributed again. The User that was using the license can still use the free Katalon product.

Follow these steps:

1. Go to the **License Management** page.
2. In the **Online Licenses** section, click on the Trash bin icon of the machine ID for which you want to remove the license.

    The **Remove license** box pops up.

3. Click **Remove** to confirm your action.

    **Please note**: By clicking Remove, you immediately terminate the current session that machine ID is working on in Katalon Studio. You should remove a license from a machine ID with caution.

## Remove a registered machine ID
This action removes the license associated with a registered machine ID. This license is then available to be attributed again. The User who had their machine ID removed from the registered machine ID list can still use the free Katalon product.

Follow these steps:

1. Go to the **License Management** page.
2. Scroll down to the **Registered Machines** section.

3. Click on the *Trash bin* icon of the machine ID you want to remove.

    The **Deactivate Machine** box pops up.

4. Click **Remove** to confirm your action.

