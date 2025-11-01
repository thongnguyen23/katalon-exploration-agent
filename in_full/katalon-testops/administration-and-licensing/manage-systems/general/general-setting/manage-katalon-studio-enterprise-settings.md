---
title: Manage Katalon Studio Enterprise settings
---

Learn how you can manage Katalon Studio Enterprise (KSE) settings directly within TestOps, such as configuring idle time out or KSE notifications.

## Prerequisites

- You must be an Account or System Administrator or possess the relevant permissions. Go to [Roles](/katalon-platform/administer/administration-and-licensing-alternate/manage-systems/general/permissions/about-roles) or [Permissions](/katalon-platform/administer/administration-and-licensing-alternate/manage-systems/general/permissions/about-permissions) for more information or learn how to [assign an Account Admin here.](/katalon-platform/administer/administration-and-licensing-alternate/manage-administrators/assign-or-unassign-account-administrators)

---

## Configure idle time out

After a set period of inactivity, Katalon Studio Enterprise (KSE) automatically logs a user out. This feature helps protect your Katalon Studio Enterprise account from unauthorized access.

You can set a custom idle timeout period.

1. Go to **Admin Settings** > **System** > **General**. You can find Admin Settings at the upper right corner of the page, indicated by a cog icon.

    The General Settings page displays.

2. Within the **Katalon Studio Enterprise** section, toggle the **Idle Timeout** button to enable this feature. The button is highlighted in blue when it is enabled.

<br/>

<img src="https://tw-cdn.katalon.com/katalon-testops/Administration and Licensing/Manage Systems/General/Admin System General Katalon Studio Enterprise.png" alt="The General Settings page with the Idle Timeout feature highlighted." width="1080"/>
<p align="center"><em>The Katalon Studio Enterprise section in the System General page.</em></p>

<br/>

3. Set the idle timeout limit from the dropdown menu. This determines how much time needs to elapse before a user is logged out. You can select from the following options:

- 1 hour
- 3 hours
- 6 hours
- 12 hours
- 24 hours
- Custom (in minutes)

4. Optional: Toggle the **Allow user to continue after the timeout** setting to permit users to resume their session a specified number of times after reaching the idle timeout threshold.

5. Select **Save Changes** to apply your modifications and confirm your changes.

### Result

A notification confirms that your settings have been saved.

---

## Enable or disable Katalon Studio Enterprise notifications

<!-- Feature ticket: https://katalon.atlassian.net/browse/TO-7378-->

You can manage Katalon Studio update notifications through this setting. When enabled, users receive alerts about new Katalon Studio versions with download options. When disabled, all update notifications are suppressed, keeping users on their current version. This feature helps organizations standardize software versions across teams, ensuring all users operate on the same approved version, which simplifies troubleshooting by eliminating version inconsistencies. 

1. Go to **Admin Settings** > **System** > **General**. You can find Admin Settings at the upper right corner of the page, indicated by a cog icon.

2. Within the **Katalon Studio Enterprise** section, toggle the **Notifications** button to enable this feature. The button is highlighted in blue when it is enabled.

<br/>

<img src="https://tw-cdn.katalon.com/katalon-testops/Administration and Licensing/Manage Systems/General/Admin System General KSE Notifications 2.png" alt="The General Settings page with the Notifications feature highlighted." width="500"/>

<br/>

3. Select **Save Changes** to apply your modifications and confirm your changes.

### Result

A notification confirms that your settings have been saved.



