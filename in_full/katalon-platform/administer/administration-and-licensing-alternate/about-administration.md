---
title: "Administration Overview"
---
This document outlines the organizational structure and user roles within Katalon TestOps, with a focus on the administrative (Admin) functions

Katalon TestOps uses a tiered administration system that groups all account management and platform settings under a single Admin section. It consists of two hierarchical levels:

- **Account Level**: Centralizes global settings across the organization (for Admins).
- **Project Level**: Manages settings within individual projects (for Testers/QA).

A typical organizational structure looks like this:

<img src="https://tw-cdn.katalon.com/katalon-platform/admin/example-structure.png" width="900" alt="Admin - Example Org Structure" /> <br/>
## About Roles

- When a user is added to an Account, they are assigned the **User** role by default.
- When a user is added to a Project, they are assigned the **Tester** role by default.
- A user can have **multiple roles** across projects or scopes. Their effective permissions will be the **union** **of all assigned roles**.
    
    *For example: If you belong to Organization 1, but you are granted a KSE license for Organization B, then you can access both resources from the two organizations.*
    

Roles determine what a user can see and do, whether at the Account level (for administrative tasks) or the Project level (for test-related work). Assigning the right roles ensures users have appropriate access based on their responsibilities.

## Account-Level Roles

| Role | Description |
| --- | --- |
| Account Admin | Manages account-level settings, subscriptions, and permission templates. |
| System Admin | Manages system settings and third-party integrations. |
| User | Base-level access. Required for any user joining an account. |

### Actions Available at the Account Level

|  	| **_Account Admin_** 	| **_System Admin_** 	| **_User_** 	|
|:---:	|:---:	|:---:	|:---:	|
| **User Management** 	| - Invite users<br/> - Revoke invitation<br/> - Resend invitation<br/> - Edit users role<br/> - Edit login options for users<br/> - Remove users from Account<br/> - Export User Management page 	| No access 	| No access 	|
| **Subscription Management** 	| - Purchase subscription<br/> - Upgrade subscription<br/> - Cancel subscription 	| No access 	| No access 	|
| **Project Management** 	| - View the Project list and details<br/> - Create a Project<br/> - Edit Project’s name<br/> - Delete a Project<br/> - Invite users to Project<br/> - Resend invitations to Project<br/> - Remove users from Project<br/> - Edit user's Project role 	| No access 	| No access 	|
| **Payment Method** 	| - View payment method<br/> - Edit payment method<br/> - Delete payment method 	| No access 	| No access 	|
| **License Management** 	| - View License Management page<br/> - Assign licenses to users<br/> - Revoke licenses from users 	| No access 	| No access 	|
| **Organization Management** 	| - Create Organizations<br/> - View Organization information<br/> - Update Organization information 	| No access 	| No access 	|
| **Account Settings** 	| - View Account information<br/> - Update Account information<br/> - Delete Account 	| No access 	| No access 	|
| **Security Settings** 	| - Configure Idle TimeOut<br/> - Configure Session Timeout<br/> - Configure IP Address Whitelist<br/> - Configure Single Sign-On 	| - Configure Idle TimeOut<br/> - Configure Session Timeout<br/> - Configure IP Address Whitelist<br/> - Configure Single Sign-On 	| No access 	|
| **Integration Settings** 	| - Create an Integration<br/> - Disconnect an Integration<br/> - Update an Integration 	| - Create an Integration<br/> - Disconnect an Integration<br/> - Update an Integration 	| No access 	|
| **AI Settings** 	| - Enable AI setting<br/> - Disable AI setting<br/> - Update AI setting<br/> - Add AI key<br/> - Delete AI key 	| Enable AI setting<br/> - Disable AI setting<br/> - Update AI setting<br/> - Add AI key<br/> - Delete AI key 	| No access 	|
| **Other Configurations** 	| - Add KRE Agents<br/> - Configure KRE Agents<br/> - Create Application under Test<br/> - View Application under Test list<br/> - Delete Application under Test 	| - Add KRE Agents<br/> - Configure KRE Agents<br/> - Create Application under Test<br/> - View Application under Test list<br/> - Delete Application under Test 	| No access 	|

## Project-Level Roles

| Role | Description |
| --- | --- |
| Project Admin | Manages project settings, roles, and integrations. |
| Test Lead | Approves test cases, manages key testing artifacts. |
| Tester | Creates and updates test cases, test runs, test suites, etc. |
| Member | Read-only or limited access, based on license and permission template. |

### Actions Available at the Project Level

|  	| **_Project Admin_** 	| **_Test Lead_** 	| **_Tester_** 	| **_Member_** 	|
|:---:	|:---:	|:---:	|:---:	|:---:	|
| **Project Management** 	| - View Project’s General Information <br/> -  Edit Project’s name<br/> - Invite users to Project<br/> - Resend invitations to Project<br/> - Remove users from Project<br/> - Edit user's Project role 	| No access 	| No access 	| No access 	|
| **Project Integrations** (Note: Integrations must first be set up at the Account-level) 	| - Configure integrations <br/> - Edit integrations <br/> - Archive/unarchive integrations <br/> - View integrations  	| No access 	| No access 	| No access 	|
| **Project Configurations** 	| - View KRE Agent Information<br/> - Connect/Disconnect KRE Agent <br/> - Link AUT (Application Under Test)<br/> - View linked AUT 	| No access 	| No access 	| No access 	|
| **Home (Reports and Analytics)** 	| - View dashboard<br/> - Add dashboard<br/> - Edit dashboard<br/> - Edit threshold for dashboard<br/> - Export/Share dashboard/test report 	| - View dashboard<br/> - Add dashboard<br/> - Edit dashboard<br/> - Edit threshold for dashboard<br/> - Export/Share dashboard/test report 	| - View dashboard<br/> - Export/Share dashboard/test report 	| - View dashboard<br/> - Export/Share dashboard/test report 	|
| **Planning** 	| - View Sprint Timelines<br/> - View Plans (Sprints & Releases)<br/> - Edit Items of a Sprint/Release 	| - View Sprint Timelines<br/> - View Plans (Sprints & Releases)<br/> - Edit Items of a Sprint/Release 	| - View Sprint Timelines<br/> - View Plans (Sprints & Releases)<br/> - Edit Items of a Sprint/Release 	| - View Sprint Timelines<br/> - View Plans (Sprints & Releases) 	|
| **Tests** 	| - Create test case/test suite<br/> - Import test case<br/> - Edit test case/test suite<br/> - Delete test case/test suite<br/> - View test case/test suite 	| - Create test case/test suite<br/> - Import test case<br/> - Edit test case/test suite<br/> - Delete test case/test suite<br/> - View test case/test suite 	| - Create test case/test suite<br/> - Import test case<br/> - Edit test case/test suite<br/> - Delete test case/test suite<br/> - View test case/test suite 	| View test case/test suite 	|
| **Executions** 	| - View Execution details and logs<br/> - Create Automated Test Run<br/> - Create Manual Test Run<br/> - Start/Run Execution<br/> - Edit/Delete Execution<br/> - View Visual Testing Info<br/> - Manage Recurring Test Run<br/> - Comment/Attach files in manual execution<br/> - Report defects  	| - View Execution details and logs<br/> - Create Automated Test Run<br/> - Create Manual Test Run<br/> - Start/Run Execution<br/> - Edit/Delete Execution<br/> - View Visual Testing Info<br/> - Manage Recurring Test Run<br/> - Comment/Attach files in manual execution<br/> - Report defects  	| - View Execution details and logs<br/> - Create Automated Test Run<br/> - Create Manual Test Run<br/> - Start/Run Execution<br/> - Edit/Delete Execution<br/> - View Visual Testing Info<br/> - Manage Recurring Test Run<br/> - Comment/Attach files in manual execution<br/> - Report defects  	| - View Execution details and logs<br/> - View Visual Testing Info 	|
| **TestCloud** 	| - Upload Applications (.apk/.ipa/.zip)<br/> - Live Testing: Mobile App, Mobile Browser, Desktop Browser<br/> - Delete Applications<br/> - View Application Info 	| - Upload Applications (.apk/.ipa/.zip)<br/> - Live Testing: Mobile App, Mobile Browser, Desktop Browser<br/> - Delete Applications<br/> - View Application Info 	| - Upload Applications (.apk/.ipa/.zip)<br/> - Live Testing: Mobile App, Mobile Browser, Desktop Browser<br/> - Delete Applications<br/> - View Application Info 	| View application Information 	|
