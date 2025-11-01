---
title: About Administration
---

This document discusses the different levels of administration in Katalon TestOps.

Katalon TestOps's administration framework is structured as a tiered system, consolidating all Account management functions and TestOps settings into a single section labeled **Admin**. Its hierarchy consists of two levels. They are:

*The Account level is at the top of the hierarchy, followed by the Project level.*

<!-- Internal doc on Admin system configuration: https://katalon.atlassian.net/wiki/spaces/ADMIN/pages/3032515037/Permission+Ready+to+be+Reviewed -->

## Account Level

At the top of the hierarchy is the **Account**. It serves as a control center for all universal settings and acts as a repository for Projects and Users.

Within this level, you can access the following functions:

- [General Account information](/katalon-testops/administration-and-licensing/manage-accounts/manage-account-information)
- License Management
- License Utilization
- System Configurations

**Account Admins** govern this level and have all permissions needed to administrate functions outside of direct testing, like managing account information, subscriptions, license reports, and user permissions.

Learn how you can [turn a user into an Account Admin here](/katalon-testops/administration-and-licensing/manage-administrators/assign-or-unassign-account-administrators).

Each Account has its own unique ID. Within the UI, an account number is identified by looking for a prefix of **AC**.

<br/>

<img src="https://tw-cdn.katalon.com/katalon-testops/Administration and Licensing/Manage Accounts/General/Feb192025 Account Number.png" alt="Account Admin Permissions" width="1080"/>

*In the image above you can see the Account number below the Account's name, depicted as **AC-164XX**.*

---

## Project Level

At the bottom of the hierarchy is the **Project** level. Its main function is to manage Users in detail and define their project configurations.

Within this level, you can access the following functions:
- General Project Information
- Project Members and their roles
- Project Configurations

Learn how you can [turn a user into a Project Admin here](/katalon-testops/administration-and-licensing/manage-administrators/assign-or-unassign-project-administrators).

Each Project has its own unique ID. Within the UI, a project number is identified by looking for a prefix of **PJ**.

<br/>

<img src="https://tw-cdn.katalon.com/katalon-testops/Administration and Licensing/Feb192025 Project ID 2.png" alt="Account Admin Permissions" width="1080"/>

*In the image above you can see the Project numbers beside the Projects' names.*

---

## About new Users

When a person is first invited to join an Account, they are automatically assigned the **User** role and become affiliated with a single Organization.

<br/>

<img src="https://tw-cdn.katalon.com/katalon-testops/Administration and Licensing/Manage Accounts/General/Feb192025 User Organzation Relationship.png" alt="Account Admin Permissions" width="100"/>

<br/>

:::note
- If there is no Organization chosen during the invitation phase, then the user will be affiliated directly with the Account instead.
:::

While they possess the default User role, they do not have access to most of TestOps' features, so it's generally recommended that they be reassigned to a more appropriate role immediately. There are [premade roles](/katalon-testops/administration-and-licensing/manage-systems/permissions/about-roles) that an Account Admin can leverage to grant access quickly. You can:

* [Assign a User Account Roles](/katalon-testops/administration-and-licensing/manage-organizations/user-management/edit-a-users-account-roles): These roles are best for operational administrators who need access to features related to Account management, licensing management, User and permission management, or system configurations.

* [Assign a User Project Roles](/katalon-testops/administration-and-licensing/manage-organizations/user-management/edit-a-users-project-roles): These roles are best for testers who have to set up general Project settings, configurations, or integrations, or have to use features in TestOps that have to do with the actual testing process.

Upon reassignment, they are free to work between Projects or Organizations within the Account as needed.

To track a specific user's attributes and work spaces within Katalon TestOps, visit their [User Detail](/katalon-testops/administration-and-licensing/manage-organizations/user-management/view-the-user-detail-page) page.
