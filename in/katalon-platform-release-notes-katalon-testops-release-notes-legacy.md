---
hide_title: true
title: Release Notes - Katalon TestOps Legacy
---
import Reusable from '@site/src/reusable/Reusable.mdx';

<Reusable />

# <a id="concept-5391" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Release Notes - Katalon TestOps Legacy


## <a id="concept-dbf8qeyw" class="anchor_top_offset"/>March 27th 2024


### New features

            
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">Introduced the Katalon Report Uploader, which allows the automatic pushing of test results to XRAY. This makes syncing Gitlab runs easier. </p></li><li className="li"><p className="p">Introduced the ability to choose a subdirectory when <a className="xref" href="/katalon-platform/organize/configure-a-git-repository-in-testops#task-7534">configuring a Git Repository</a>. </p></li></ul> 
                    

## <a id="concept-5za3lpwj" class="anchor_top_offset"/>March 13th 2024


### New features

<div xmlns="http://www.w3.org/1999/xhtml" className="p"><ul className="ul"><li className="li"><p className="p">Introduced the ability to link any custom Xray issue type with user-defined test artifacts on Katalon. Learn more here: <a className="xref" href="/katalon-platform/integrations/xray-integration/configure-xray-integration-in-katalon-testops#task-4126">How to enable the  Xray integration</a>.</p></li></ul></div>

### Enhancements

<div xmlns="http://www.w3.org/1999/xhtml" className="p"><ul className="ul"><li className="li"><p className="p">Improved executions by ensuring TestOps Local Agent's compatibility with the latest version of KRE (9.3). </p></li><li className="li"><p className="p"> Upgraded the Jira Plugin for compatibility with Jira Data Center 9.12.x.</p></li></ul></div>

## <a id="concept-34th6nxn" class="anchor_top_offset"/>March 6th 2024


### New features

<div xmlns="http://www.w3.org/1999/xhtml" className="p"><ul className="ul"><li className="li"><p className="p">Introduced a new feature called User Group. The Organization Owner/Admin can now create a group of users and invite their group to any Project at once without having to invite every single user.</p></li></ul></div>

## <a id="concept-coermj4n" class="anchor_top_offset"/>March 5th 2024


### New features

<div xmlns="http://www.w3.org/1999/xhtml" className="p"><ul className="ul"><li className="li"><p className="p">Introduced a new feature called Daily Summary Email, which provides users with email reports of their execution results. </p></li></ul></div>

### Enhancements

<div xmlns="http://www.w3.org/1999/xhtml" className="p"><ul className="ul"><li className="li"><p className="p">Now displaying the total number for Failed Test Results and Linked Defects in the navigation tab of Test Run Reports.</p></li></ul></div>

## <a id="concept-7702" class="anchor_top_offset"/>February 20th 2024


### New features

<div xmlns="http://www.w3.org/1999/xhtml" className="p"><ul className="ul"><li className="li"><p className="p">Introduced Bank Transfer as a new payment method. This payment method is applicable to US customers with a business domain and an annual subscription. For more details, you can refer to: <a className="xref" href="/katalon-platform/administer/administration-tasks/payment-and-subscription/payment-method#concept-4010">Bank transfer payment</a>.</p></li></ul></div>

## <a id="concept-9amcjfy1" class="anchor_top_offset"/>January 31st 2024


### New Features

<div xmlns="http://www.w3.org/1999/xhtml" className="p"><ul className="ul"><li className="li"><p className="p">Added the ability to preview Jira issue information when hovering over linked defects in Test Results lists, as well as a button to go directly to its corresponding Jira issue. </p></li><li className="li"><p className="p">Introduced AI Control feature. The Account Owner can now disable all AI-powered features of Katalon within an Account. For more details, you can refer to: <a className="xref" href="/katalon-platform/administer/administration-tasks/enabledisable-ai-features-in-an-account">Enable/disable AI features in an Account</a>.</p></li><li className="li"><p className="p">Introduced a new Organization section on the Account admin page which shows your organization's general information. This page also replaces the Account Homepage displayed when users log in to TestOps.</p></li></ul></div>

### Enhancements

<div xmlns="http://www.w3.org/1999/xhtml" className="p"><ul className="ul"><li className="li"><p className="p">Enhanced UI for Test Results lists to show more information.</p></li><li className="li"><p className="p">Enhanced the Failed Test Results page to display all exceptions from all Test Results, as well as providing more filter options. </p></li><li className="li"><p className="p">Disabled Virtual Data Analyst from generating insights if disallowed based on configurations from Account Settings. </p></li><li className="li"><p className="p">The TestOps admin page is now divided into 2 separate pages - one for the Account level and the other for the Organization level.</p></li><li className="li"><p className="p">The Owner and Admin can now check who invited new users to the Organization in the User Management.</p></li></ul></div>

### Bug fixes

<div xmlns="http://www.w3.org/1999/xhtml" className="p"><ul className="ul"><li className="li"><p className="p">Deployed a fix within the test run level logic of TestOps that now prevents the following scenarios from causing executions to get stuck at the incomplete status:</p><ul className="ul"><li className="li"><p className="p">Failed test results based on a browser error.</p></li><li className="li"><p className="p">Running a test suite collection with a universal configuration. </p></li></ul></li></ul></div>

## <a id="concept-bew19xf7" class="anchor_top_offset"/>January 17th 2024


### New features

<div xmlns="http://www.w3.org/1999/xhtml" className="p"><ul className="ul"><li className="li"><p className="p">Re-introduced the ability for users to upload ZIP files in order to import their tests into TestOps, optimizing their workflows by not limiting them to only uploading via Git repositories. See: <a className="xref" href="/katalon-platform/organize/upload-a-script-repository-to-testops">Upload a Script Repository to TestOps</a>.</p></li><li className="li"><p className="p">Pushing TestOps reports and test runs to Xray will automatically push a corresponding PDF and a ZIP file too. This ZIP file contains all artifacts of the reports, unlike before when we only pushed the PDF reports. See: <a className="xref" href="/katalon-platform/integrations/xray-integration/manually-push-katalon-test-result-to-xray">Manually push Katalon test result to Xray</a>.</p></li><li className="li"><p className="p">Introduced the Project Detail page in the Project Management section for project information and membership management.</p></li></ul></div>

### Enhancements

<div xmlns="http://www.w3.org/1999/xhtml" className="p"><ul className="ul"><li className="li"><p className="p">Allowed all Project roles to invite multiple users to the project. This includes users who haven't joined the Organization yet, provided that users' emails have the same business domain as the Organization Owner.</p></li></ul></div>

### Changes

<div xmlns="http://www.w3.org/1999/xhtml" className="p"><ul className="ul"><li className="li"><p className="p">Offline license generation is no longer supported. Active offline licenses are still working until their expiry dates. When an offline license expires, you can switch to using an online license.</p></li></ul></div>

## <a id="concept-3439" class="anchor_top_offset"/>January 10th 2024


### Enhancements

<div xmlns="http://www.w3.org/1999/xhtml" className="p"><ul className="ul"><li className="li"><p className="p">Added a list containing suggested defects that show when linking test results within the Report Defect feature.</p></li><li className="li"><p className="p">Enhanced automation rules where new matched test results will not auto-link if the defect is already marked as resolved.</p></li><li className="li"><p className="p">Enhanced UI to make it easier for users to view more information regarding linked defects for a particular test run or test result. </p></li><li className="li"><p className="p">Enhanced the <span className="ph uicontrol">Refresh</span> button's responsiveness in the Dashboard, Defect, and Requirements pages.</p></li></ul></div>

## <a id="concept-o9n8u8d1" class="anchor_top_offset"/>December 20th 2023


### New features

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">Introduced Katalon Platform's new structure which applies to Organizations created from December 20th, 2023 onward. Katalon now has 3 management levels: Account level is the highest, followed by the Organization level, then Project levels. To learn more about the new structure, you can refer to <a className="xref" href="/katalon-platform/administer/administration-roles/administrative-roles-and-permissions">Administrative Roles and Permissions</a>.</p></li><li className="li"><div className="p">At the Project level:<ul className="ul"><li className="li">Allowed the Owner or Admin of an Organization to invite multiple users to multiple projects even if they have not joined the Organization.</li><li className="li">Allowed the Owner or Admin of an Organization to view details of all Projects under their Organization.</li><li className="li"><p className="p">Allowed to auto transfer ownership to the Organization Owner if the Owner of any Project is removed from an Organization.</p></li></ul></div></li><li className="li"><p className="p">Introduced a new page on TestOps called "Organization Setup". This page consolidates features like test environments, TrueTest configurations, and more. It provides users with a streamlined method to configure their organization's properties directly within TestOps.</p></li><li className="li"><p className="p">Test environments have now been relocated to the Organization Level, granting users the ability to establish test environments and assign them to the relevant projects independent of Team Level limitations. </p></li></ul> 

### Enhancements

<div xmlns="http://www.w3.org/1999/xhtml" className="p"><ul className="ul"><li className="li"><p className="p">The Project Management section is now on the TestOps Admin page.</p></li><li className="li"><p className="p">Once an Organization configures Custom Domain and SSO, the login settings for all users is set to enable login with SSO and disable login with username/password by default .</p></li></ul></div>

## <a id="concept-1452" class="anchor_top_offset"/>December 12th 2023


### New features

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">Introduced new functions for the Slack integration. You can now configure it to send you notifications in a Slack channel based on defects updates. </p></li><li className="li"><p className="p">Introduced a new toggle feature that only shows Failed/Error/Incomplete test results that haven't been linked to a defect yet.</p></li></ul> 

### Enhancements

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">Revamped the Jira add-on button behavior and its banner.</p></li></ul> 

## <a id="concept-470" class="anchor_top_offset"/>December 6th 2023


### New features

<div xmlns="http://www.w3.org/1999/xhtml" className="p"><ul className="ul"><li className="li"><p className="p">Introduced automatically attached PDF reports for pushed Xray Test Executions' matching TestOps reports. </p></li></ul></div>

## <a id="concept-phv1wqmc" class="anchor_top_offset"/>November 29th 2023


### New features

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">Introduced Automation Rules for test defects which allows you to automatically link specific defects to to matching test results to help minimize manual linking. Learn more about it here: <a className="xref" href="/katalon-platform/analyze/analytics/defects-report/defects-report-automations">Defects Report automations</a>.</li></ul> 

## <a id="concept-nxd4t2p6" class="anchor_top_offset"/>November 22nd 2023


### New features

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">To enhance user productivity and streamline workflows on TestOps, we now allow bulk operations with test suites. You can: </p>     <ul className="ul"><li className="li"><p className="p">Move multiple test suites</p></li><li className="li"><p className="p">Duplicate multiple test suites</p></li><li className="li"><p className="p">Delete multiple test suites</p></li></ul></li></ul> 

### Bug fixes

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">Report Defect dialog automatically closed  itself. </p></li></ul> 

## <a id="concept-7671" class="anchor_top_offset"/>November 15th 2023

<p xmlns="http://www.w3.org/1999/xhtml" className="shortdesc"> </p> 

### Enhancements

<div xmlns="http://www.w3.org/1999/xhtml" className="p"><ul className="ul"><li className="li"><p className="p">Removed the invitation accept step. When an Account Owner invites a user who shares the same non-public email domain, the user can immediately join the organization without having to accept the invitation email.</p></li></ul></div>

## <a id="concept-489" class="anchor_top_offset"/>November 8th 2023


### New features

<div xmlns="http://www.w3.org/1999/xhtml" className="p"><ul className="ul"><li className="li"><p className="p">To enhance user productivity and streamline workflows on TestOps, we now allow bulk operations with test cases. You can: </p><ul className="ul"><li className="li"><p className="p">Add multiple test cases to a test suite</p></li><li className="li"><p className="p">Move multiple test cases</p></li><li className="li"><p className="p">Duplicate multiple test cases</p></li><li className="li"><p className="p">Delete multiple test cases</p></li></ul></li></ul></div>

### Enhancements

<div xmlns="http://www.w3.org/1999/xhtml" className="p"><ul className="ul"><li className="li"><p className="p">Users who connect Xray Tests to TestOps test cases now have their linked test cases displayed in the Katalon Platform section of the Jira plugin.</p></li><li className="li"><p className="p">You can now enable or disable the Jira plugin for specific Jira projects. </p></li><li className="li"><p className="p">The automatic linking of an undeletable Release to a Schedule was reportedly a challenge for some users. This has been modified; users can now link a Release to their Schedule instead of it being linked automatically.</p></li></ul></div>

## <a id="concept-5269" class="anchor_top_offset"/>October 31, 2023


### New features

<div xmlns="http://www.w3.org/1999/xhtml" className="p"><ul className="ul"><li className="li">Users can now seamlessly create new Jira issues from TestOps after investigating a failed test result. Linking issues to a Jira ticket with current test results can be done without leaving TestOps.</li></ul></div>

### Enhancements

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">TestOps' Jira integration has been revamped when it comes to: setting up configurations, choosing a project, and creating a Webhook.</p></li><li className="li"><p className="p">Added Refresh button to fetch latest Jira tickets &amp; fields configuration.</p></li><li className="li"><p className="p">Defect reporting behavior related to linking tparticular test results to existing issues on Jira has been revamped. </p></li><li className="li"><p className="p">Enhanced the notification mechanism for sending messages via Slack and Email. </p></li></ul> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> </p> 

## <a id="concept-4503" class="anchor_top_offset"/>October 30th 2023


### New Features

<div xmlns="http://www.w3.org/1999/xhtml" className="p"><ul className="ul"><li className="li">You can now sign in to <span className="ph">Katalon TestOps</span> with your Google account.</li><li className="li">Added a banner to notify Account Owner and Admins to purchase more licenses, arrange the account membership, or assign licenses to the members. If no action is taken within 90 days, users will be blocked from using free  <span className="ph">Katalon Studio</span>. For further information, refer to <strong className="ph b">Free Offerings</strong> term in <a className="xref j-external-link" href="https://katalon.com/terms#customer-terms-of-use" target="_blank">Terms of Use</a>.</li></ul></div>

### Enhancements

* [Cloud Studio] You now can  create and execute test cases with Cloud Studio without being counted towards the quota in Product Utilization of Katalon TestOps.
* [License Management] You now can select multiple users at a time to revoke users' licenses.
* Redirected all Administration login pages to a centralized sign-in page: <a href="https://testops.katalon.io/" target="_blank">Katalon login page</a>. 

## <a id="concept-4591" class="anchor_top_offset"/>October 25th 2023

<p xmlns="http://www.w3.org/1999/xhtml" className="shortdesc"> </p> 

### New features

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p"> Introduced a new feature called Instant Run. This allows users to quickly execute test cases in Cloud Storage directly from the Test Explorer view. This allows users to rapidly produce their Cloud Studio test case reports and derive insights from them with one click.</p></li></ul> 

### Bug fixes

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">Fixed a failure to add additional licenses for an existing product. </p></li></ul> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> </p> 

## <a id="concept-3137" class="anchor_top_offset"/>October 11th 2023

<p xmlns="http://www.w3.org/1999/xhtml" className="shortdesc"> </p> 

### New features

<div xmlns="http://www.w3.org/1999/xhtml" className="p"><ul className="ul"><li className="li"><p className="p">Users can now add test cases to test suites directly from the Test Case table or Test Case details page, allowing for easier test case organization. </p></li></ul></div>

### Enhancements

<div xmlns="http://www.w3.org/1999/xhtml" className="p"><ul className="ul"><li className="li"><p className="p">The delete function in TestOps' test suite screen has been relocated to the triple dot menu at the upper right corner. </p></li><li className="li"><p className="p">The pop-up dialog for the delete confirmation dialog has been updated. </p></li><li className="li"><p className="p">Redirected the download link for Katalon Studio. It now leads <a className="xref j-external-link" href="https://katalon.com/download" target="_blank">here</a>. </p></li></ul></div>

## <a id="concept-5561" class="anchor_top_offset"/>October 9th 2023

<p xmlns="http://www.w3.org/1999/xhtml" className="shortdesc"> </p> 

### New features

<div xmlns="http://www.w3.org/1999/xhtml" className="p"><ul className="ul"><li className="li"><p className="p">Allowed Organization Owners and Organization Admins to seamlessly add new users to a team right after sending invitations for them to join the organization. For more details, refer to: <a className="xref" href="/katalon-platform/administer/administration-tasks/manage-users#invite-users-to-join-an-organization">Invite users to join an Organization</a>.</p></li></ul></div>

## <a id="concept-7176" class="anchor_top_offset"/>October 5th 2023

<p xmlns="http://www.w3.org/1999/xhtml" className="shortdesc"> </p> 

### New features

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">Users can now view the value of Severity fields on the Defects page.</p></li></ul> 

### Enhancements

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">Migrated the database for the Severity field to the Defects page.</p></li><li className="li"><p className="p">Enhanced the Jira field fetching mechanism to get the Severity field. </p></li><li className="li"><p className="p">Updated the display Priority with the format "icon - value" in a Defects page. </p></li><li className="li"><p className="p">Reduced the number of searches when a user changes the time filter on the Test Run page.</p></li></ul> 

## <a id="concept-5162" class="anchor_top_offset"/>September 6th 2023

<p xmlns="http://www.w3.org/1999/xhtml" className="shortdesc"> </p> 

### New features

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">Introduced enhanced starter packages: Upgrade options for starter users, including those who already purchased a starter package and those joining this phase, can now seamlessly ascend to a higher-tier package within the subscription cycle of the initial package. Users can enjoy aligned pricing and simplified renewals for additional products within a seamless subscription cycle.</li></ul> 

### Enhancements

<div xmlns="http://www.w3.org/1999/xhtml" className="p"><ul className="ul"><li className="li"><p className="p">[UI/UX] The <span className="ph uicontrol">Your current subscriptions</span> section will transform into a collapse/expand panel. By default, it will be collapsed whenever users visit the <span className="ph uicontrol">Subscription Management</span> page.</p></li><li className="li"><p className="p">[UI/UX] The <span className="ph uicontrol">Get more single products</span> section will be converted into a collapse/expand panel. For starter users, it will stay collapsed by default when they land on the <span className="ph uicontrol">Subscription Management</span> page.</p></li></ul></div>

## <a id="concept-4322" class="anchor_top_offset"/>August 30th 2023

<p xmlns="http://www.w3.org/1999/xhtml" className="shortdesc"> </p> 

### New features

<div xmlns="http://www.w3.org/1999/xhtml" className="p"><ul className="ul"><li className="li"><p className="p">[TrueTest] Now displays the "data tracking" status of AUTs. They can be either Inactive, Active, or Paused.</p></li><li className="li"><p className="p">[TrueTest] Associates a specific error when generating a map with corresponding error documentation.</p></li><li className="li"><p className="p">[TrueTest] Review test cases of archived maps in the script repository. </p></li><li className="li">[Test Management] Users can now perform quick actions directly on test cases or test suites such as renaming, editing, duplicating, and moving. </li><li className="li"><p className="p">[Test Management] Users can now schedule test runs directly from both test suite list view and the test suite detail page. Note that this is not available for test cases/test suites stored in Git repositories. </p></li></ul></div>

### Enhancements

<div xmlns="http://www.w3.org/1999/xhtml" className="p"><ul className="ul"><li className="li"><p className="p">[TrueTest] Improved the quality of AI-generated test cases. </p></li><li className="li"><p className="p">[Platform Settings] Project Settings has been removed and consolidated with Project Configurations within settings. </p></li><li className="li"><p className="p">[Virtual Data Analyst] Enhanced the AI-blocks so users can refresh and add tracking events. </p></li></ul></div>

## <a id="concept-752" class="anchor_top_offset"/>August 15th 2023

<p xmlns="http://www.w3.org/1999/xhtml" className="shortdesc"> </p> 

### New features 

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">Released the beta for Virtual Data Analyst. It's a new feature that uses the capabilities of generative AI to analyze TestOps data and subsequently create actionable insights. Read more about it here: <a className="xref" href="/katalon-platform/proof-of-concept/virtual-data-analyst">Virtual Data Analyst</a>.</p></li></ul> 

## <a id="concept-9278" class="anchor_top_offset"/>August 2nd 2023


### New features

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">Added Katalon Cloud. It's the new default bucket for all new projects. It's designed to enhance the user experience by providing a seamless and convenient way for users to publish, manage, execute, and report tests directly on the Katalon Platform. See: <a className="xref" href="#">January 19th 2021</a>.</p></li><li className="li"><p className="p">Users can execute tests with Cloud Studio (Beta) from Katalon Cloud, as well as view results or reports similar to how it works when using a Git repository. </p></li></ul> 

### Enhancements

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">The <span className="ph uicontrol">Repeat</span> toggle in the <span className="ph uicontrol">Schedule Test Run</span> dialog in TestOps is now toggled off by default. </p></li><li className="li"><p className="p">Changed the notification text when running the Mobile Native App testing feature. </p></li></ul> 

### Bug fixes

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">TestCloud will update its Local Engine automatically instead of using a fixed version. </p></li></ul> 

## <a id="concept-9452" class="anchor_top_offset"/>July 27th 2023


### Enhancements

<div xmlns="http://www.w3.org/1999/xhtml" className="p"><ul className="ul"><li className="li"><p className="p">Created a notification banner for Account Owners or Billing managers to receive to remind them should their Test Results usage reach 75%. It links to subscription management to help them adjust their quotas accordingly. </p></li><li className="li"><p className="p">Fixed how user support slots work in the event that a selected member is removed from the Organization. </p></li></ul></div>

## <a id="concept-5586" class="anchor_top_offset"/>June 7th 2023


### New features

<div xmlns="http://www.w3.org/1999/xhtml" className="p"><ul className="ul"><li className="li"><p className="p">Introduced the free use of <span className="ph">Visual Testing Professional (VTP)</span> for <span className="ph">TestOps</span>. Any current and future users can create as many checkpoint images and subsequent test results until they hit their test result quota for their subscription tier. </p></li></ul></div>

### Enhancements

<div xmlns="http://www.w3.org/1999/xhtml" className="p"><ul className="ul"><li className="li"><p className="p">The onboarding flow for users newly invited to an organization has been improved. They will now go straight to the <span className="ph">TestOps</span> homepage for a quicker start. </p></li></ul></div>

### Fixes

<div xmlns="http://www.w3.org/1999/xhtml" className="p"><ul className="ul"><li className="li"><p className="p">Fixed a bug regarding support management slots not properly reflecting allowed quota. </p></li><li className="li"><p className="p">Fixed another bug in support management where all members could be removed from assigned support slots. This is no longer possible. </p></li><li className="li"><p className="p">Fixed an error in On-premises' license server regarding data migration. </p></li></ul></div>

## <a id="concept-1385" class="anchor_top_offset"/>May 18th 2023


### Enhancements

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Added a notification banner to remind users to verify their email addresses if they have not completed the email verification process.</p> 

## <a id="concept-3875" class="anchor_top_offset"/>May 11th 2023


### New features

<div xmlns="http://www.w3.org/1999/xhtml" className="p"><ul className="ul"><li className="li"><p className="p">Introduced the tree view for script repository which allows choosing multiple test cases for a test suite.</p></li><li className="li"><p className="p">Introduced ability to run test cases with configured data binding.</p></li><li className="li"><p className="p">Now on project pages, <span className="ph">Katalon TestOps</span> interacts with  you by dynamically rewriting  on the  displaying page instead of loading entire new pages.</p></li></ul></div>

## <a id="concept-1623" class="anchor_top_offset"/>April 12th 2023


### Enhancements

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Visual Testing: Hide the "Visual Testing" drop-down list in the Schedule Test Run dialog (Advanced Settings) when scheduling with Katalon Command and Generic Command. Users now specify the baseline collection ID in the command argument.</p> 

## <a id="concept-3234" class="anchor_top_offset"/>March 28th 2023


### Enhancements

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">Introduced the ability to create Jira Webhook integration with Katalon Platform.</p></li><li className="li"><p className="p">Introduced Defects Report with trendline graph and useful insights to the defects in Katalon test runs.</p></li></ul> 

## <a id="concept-3305" class="anchor_top_offset"/>March 20th 2023


### New features

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">Introduced a new feature to the current On-Premises package: Katalon Platform On-Premises, a new solution designed for enterprise users with strict security and privacy policies. Users have access to TestOps features similar to the current Katalon Platform offerings such as managing users and projects through the administration module, scheduling execution, and visual testing of projects in the isolated On-Premises deployment. </p></li></ul> 

### Enhancements

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">From now on, Katalon On-Premises only supports Linux distros that are Debian-based and CentOS-based. Windows and MacOS are no longer supported.</p></li></ul> 

## <a id="concept-5101" class="anchor_top_offset"/>March 1st 2023


### Enhancements

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">Enhanced Xray Katalon integration experience by linking Katalon test result URL under Xray test run and show linked Katalon defects as Xray Defects under Xray test run. </p></li></ul> 

## <a id="concept-8142" class="anchor_top_offset"/>February 22nd 2023


### Enhancements

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">Introduced the ability to share filtered test runs report via URL. Now users within an organization can copy the URL of a report chart and send to each other, with filters such as time range, profile, release/build retained in the chart view. </p></li></ul> 

### Bug fixes

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">The Failed/Passed run ratio was not calculated correctly due to the implicit inclusion of Incomplete test run. The Incomplete test run was removed from the Failed/Passed ratio and test run statistics bar.</p></li></ul> 

## <a id="concept-4181" class="anchor_top_offset"/>February 1st 2023


### Enhancements

<div xmlns="http://www.w3.org/1999/xhtml" className="p"><ul className="ul"><li className="li"><p className="p">[Custom Fields &amp; Tags] Improved the inheriting mechanism so that incomplete and in-progress test executions also have custom fields and tags assigned. </p></li><li className="li"><p className="p">[Custom Fields &amp; Tags] Allowed overwriting custom fields and tags if they were assigned both through <span className="ph">Katalon Studio</span> with <span className="ph">Katalon Runtime Engine (KRE)</span> and through <span className="ph">TestOps</span> interface. </p></li><li className="li"><p className="p">[Xray integration] Showed on Xray/Jira interface the <span className="ph">TestOps</span> test environments. This enhancement allowed the ability to search for test executions on Jira based on test environments. </p></li><li className="li"><p className="p">[Xray integration] Showed on <span className="ph">TestOps</span> interface the Xray test executions that were linked with TestOps test run.</p></li><li className="li"><p className="p">[UI/UX] Polished the wording and center-aligned the elements within the header <span className="ph">TestOps</span> navigation bar. </p></li><li className="li"><p className="p">[UI/UX] Added the external icon to <span className="ph uicontrol">View Profile</span> button under the user profile section. Also within the user profile section, <span className="ph uicontrol">Notification settings</span> has been renamed to <span className="ph uicontrol">User settings</span>.</p></li><li className="li"><p className="p">[UI/UX] Displayed the count of test cases being executed, grouped by their status in the test execution status progress bar.</p></li><li className="li"><div className="p">[UI/UX] Improved test execution report chart behavior: <ul className="ul"><li className="li"><p className="p">Dynamically adjusting bar length and labels based on window size.</p></li><li className="li"><p className="p">Expanding Daily Group filter limit to 90 days.</p></li><li className="li"><p className="p">Hiding the report header when scrolling down.</p></li><li className="li"><p className="p">Eliminating vacant spaces among chart columns.</p></li></ul></div></li></ul></div>

## <a id="concept-5837" class="anchor_top_offset"/>January 5th 2023


### Enhancements

<p xmlns="http://www.w3.org/1999/xhtml" className="p">[Custom fields and tags] Allowed users to assign custom fields and tags to test runs in <span className="ph">Katalon Runtime Engine (KRE)</span> commands. See: <a className="xref" href="/katalon-studio/execute-tests/katalon-runtime-engine/command-line-syntax-in-katalon-runtime-engine#concept-9115__dl-544">TestOps integration arguments</a>.</p> 

## <a id="concept-5164" class="anchor_top_offset"/>December 7th 2022


### New features

<div xmlns="http://www.w3.org/1999/xhtml" className="p"><ul className="ul"><li className="li"><p className="p">[Custom fields &amp; tags] Allows users to organize their test artifacts. See: <a className="xref" href="/katalon-platform/organize/custom-fields-and-tags">Custom Fields and Tags</a>.</p><ul className="ul"><li className="li"><p className="p">Assign custom fields or tags to test case, test schedule, and test run</p></li><li className="li"><p className="p">Assign custom fields or tags to test entities when uploading reports from external sources</p></li><li className="li"><p className="p">Filter test entities on <span className="ph">TestOps</span></p></li><li className="li"><p className="p">Limited analytical filtering with custom fields and tags</p></li></ul></li><li className="li"><p className="p">[Xray integration] Allows users to link their manual &amp; automation test from TestOps to Xray. See: <a className="xref" href="/katalon-platform/integrations/xray-integration/configure-xray-integration-in-katalon-testops">Configure Xray Integration in <span className="ph">Katalon TestOps</span></a>.</p><ul className="ul"><li className="li"><p className="p">Link TestOps test case with Xray test on Jira</p></li><li className="li"><p className="p">Link TestOps test schedule with Xray test plan on Jira</p></li><li className="li"><p className="p">Automatically/manually push TestOps test run to Jira as Xray test execution</p></li><li className="li"><p className="p">Manage Xray test execution with release versions and evidences from TestOps</p></li><li className="li"><p className="p">Synchronize TestOps test results to Xray test run</p></li></ul></li><li className="li"><p className="p">Users who adopt Robot framework can now orchestrate testing activities by integrating with <span className="ph">TestOps</span>: the status of visual test cases developed by Robot framework can be promptly driven by <span className="ph">Visual Testing</span> results.</p></li><li className="li"><p className="p">Supported the multi-year subscription plan.</p></li></ul></div>

### Enhancements

<div xmlns="http://www.w3.org/1999/xhtml" className="p"><ul className="ul"><li className="li"><p className="p">Changed a UI text: The button "Submit a Ticket" is now "Submit a Support Case" to maintain consistency with the header on the Katalon Platform portal.</p></li><li className="li"><p className="p">Implemented an API for project creation in Reports and Analytics.</p></li><li className="li">Test Run Report enhancements:<ul className="ul"><li className="li"><p className="p">Synchronize test run list and test result by status chart</p></li><li className="li"><p className="p">Customizable filter</p></li><li className="li"><p className="p">Interactive search bar</p></li><li className="li"><p className="p">Advance Time range filter</p></li></ul></li></ul></div>

### Fixes

<div xmlns="http://www.w3.org/1999/xhtml" className="p"><ul className="ul"><li className="li"><p className="p">Allowed the Account Owner/ Account Admin to assign a Visual Testing Professional product to a member's license before they accept the invitation.</p></li><li className="li">Fixed the issue where users cannot assign KRE-Nodelock after clicking the Back button.</li><li className="li"><p className="p">Added a notice message for users who exceed 50 accounts limit. </p></li><li className="li"><p className="p">Fixed the issue where creating a default project after signing up on Katalon Platform did not generate default custom fields.</p></li><li className="li"><p className="p">Fixed the mismatched test run results in some user cases of purchasing or canceling subscription plan. </p></li></ul></div>

## <a id="concept-4091" class="anchor_top_offset"/>November 29th 2022


### New features

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"> <span className="ph">Visual Testing Professional (VTP)</span>:<ul className="ul"><li className="li">Introduced the <span className="ph uicontrol">Pixel Sensitivity</span> adjustment feature. See: <a className="xref" href="/katalon-platform/analyze/analytics/visual-testing/adjust-the-pixel-sensitivity-level">Adjust the pixel sensitivity level</a>.</li><li className="li">Introduced the <span className="ph uicontrol">Default Comparison Method</span> feature in a baseline collection. See: Default Comparison Method.</li><li className="li">Introduced the <span className="ph uicontrol">Upload Images</span> and <span className="ph uicontrol">Create Baseline Collection</span> features. See: <a className="xref" href="/katalon-platform/analyze/analytics/visual-testing/baseline-collection#task-9029">Upload baseline images/collection</a>.</li></ul></li></ul> 

## <a id="concept-6671" class="anchor_top_offset"/>November 9th 2022


### New features

<div xmlns="http://www.w3.org/1999/xhtml" className="p"><ul className="ul"><li className="li"><p className="p"> Displayed the number of Organizations and Users per plan on the <span className="ph uicontrol">Subscription Management</span> page. </p></li><li className="li"><p className="p">Introduced one more sub-tier for the Ultimate plan - 20000 Test results.</p></li><li className="li"><p className="p">Allowed Team Owner and Team Admin to edit Project Name in <span className="ph uicontrol">Project Management</span>.</p></li><li className="li"><p className="p">Allowed Account Owner and Account Admin to assign KSE/KRE licenses right after sending invitations to new member users.</p></li><li className="li"><p className="p">Users can go to <span className="ph uicontrol">Welcome Page</span> from their Profile Page, which simplifies user navigation. </p></li></ul></div>

### Enhancements

<div xmlns="http://www.w3.org/1999/xhtml" className="p"><ul className="ul"><li className="li"><p className="p">Added a sample project called <strong className="ph b">First Project</strong> in every newly created organization. Users can interact with the data in this project to learn about <span className="ph">TestOps</span> features.</p></li><li className="li"><p className="p">Removed the redundant pop-up where users must select standalone apps before processing the checkout. </p></li><li className="li"><p className="p">Provided Guidelines for users who reach the limit of the Katalon Platform quota so they can adjust their subscription plan accordingly. </p></li><li className="li"><p className="p">Allowed users to delete their Account if they do not have any subscriptions or cancel auto-renewal. </p></li><li className="li"><p className="p">[UI/UX] Removed the <span className="ph uicontrol">View Demo Site</span> button on the navigation bar. </p></li><li className="li"><p className="p">[UI/UX] Removed the <span className="ph uicontrol">Schedule Sample Test Run</span> button on the Test Execution page. </p></li><li className="li"><p className="p">[UI/UX] Removed the <span className="ph uicontrol">Quick Guide</span> button on the Profile menu. </p></li></ul></div>

### Fixes

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">Removed the incorrect name and incorrect quota of Katalon Platform for the Free tier when users are in the trial plan.</p></li><li className="li"><p className="p">Fixed bugs that are relevant to Assign Licenses and Inviting User flows. </p></li><li className="li"><p className="p">Fixed HTML injection issues.</p></li></ul> 

## <a id="concept-9450" class="anchor_top_offset"/>October 26th 2022


### Enhancements

<div xmlns="http://www.w3.org/1999/xhtml" className="p"><ul className="ul"><li className="li"><p className="p">Added a user survey to help new users start to use <span className="ph">Katalon TestOps</span> with the right edition of <span className="ph">Katalon Studio</span>.</p></li><li className="li"><p className="p">Improved the Smart Scheduler to set proper date for test execution.</p></li><li className="li"><p className="p">Added the <em className="ph i">Skipped</em> category for test result status.</p></li></ul></div>

## <a id="concept-1287" class="anchor_top_offset"/>October 12th 2022


### New features

<div xmlns="http://www.w3.org/1999/xhtml" className="p"><ul className="ul"><li className="li"><p className="p">Introduced root cause analysis for each failed test result. Failed test results are now automatically associated with failure reasons. See: <a className="xref" href="/katalon-platform/analyze/reports/view-test-reports/view-test-run-results/view-test-run-result-details">Failure reason</a>.</p></li><li className="li"><p className="p">Introduced the <span className="ph uicontrol">Failed Test Results</span> tab that shows statistics of failed test results.</p></li></ul></div>

### Enhancements

<div xmlns="http://www.w3.org/1999/xhtml" className="p"><ul className="ul"><li className="li"><p className="p">Added the option to download <span className="ph">Katalon Studio - Standalone Edition</span> directly in <span className="ph">TestOps</span>.</p></li><li className="li"><p className="p">Removed the requirement for typing in the test run ID when users want to terminate a test run.</p></li><li className="li"><p className="p">Updated the Test Scheduler UI with more accurate wording and tooltips.</p></li></ul></div>

### Fixes

<div xmlns="http://www.w3.org/1999/xhtml" className="p"><ul className="ul"><li className="li"><p className="p">Fixed the Katalon integration extension issue (on Chrome).</p></li></ul></div>

## <a id="concept-8490" class="anchor_top_offset"/>September 21st 2022


### New features

<div xmlns="http://www.w3.org/1999/xhtml" className="p"><ul className="ul"><li className="li"><p className="p"> Implemented the <span className="ph">Katalon TestOps</span> onboarding tours for testers and QA managers.</p></li><li className="li"><p className="p">Introduced the Account level to handle billing management. One organization belongs to only one Account. The Billing Manager role is now moved to the Account level. See: <a className="xref" href="/katalon-platform/administer/administration-roles/administrative-roles-and-permissions">Administrative Roles and Permissions</a>.</p></li></ul></div>

### Enhancements

<div xmlns="http://www.w3.org/1999/xhtml" className="p"><ul className="ul"><li className="li"><p className="p">Added the option to download <span className="ph">Katalon Studio</span> and <span className="ph">Katalon Runtime Engine</span> in the navigation bar.</p></li></ul></div>

## <a id="concept-2280" class="anchor_top_offset"/>August 2nd 2022


### Enhancements

<div xmlns="http://www.w3.org/1999/xhtml" className="p"><ul className="ul"><li className="li"><p className="p">[Jira integration] Fetched the <span className="ph uicontrol">Start Date</span> and <span className="ph uicontrol">Release Date</span> for populated Jira releases. See <a className="xref" href="/katalon-platform/integrations/jira-integration/populate-jira-releases">Populate Jira releases</a>.</p></li><li className="li"><p className="p">[UX/UI]:</p><ul className="ul"><li className="li"><p className="p">In the <em className="ph i">Profile</em> dropdown list:</p><ul className="ul"><li className="li"><p className="p"> Added the option to view release notes.</p></li><li className="li"><p className="p">Added the option to download <span className="ph">Katalon Studio</span>.</p></li><li className="li"><p className="p">Changed UI text from <span className="ph uicontrol">Community</span> to <span className="ph uicontrol">Community Portal</span>.</p></li><li className="li"><p className="p">Changed UI text from <span className="ph uicontrol">Submit a Ticket</span> to <span className="ph uicontrol">Submit a Support Case</span>.</p></li><li className="li"><p className="p">Removed <span className="ph uicontrol">Feature Requests</span> and <span className="ph uicontrol">Bug Reports</span> buttons. You can now submit feature requests and report bugs via the <a className="xref j-external-link" href="https://forum.katalon.com/" target="_blank">Forum</a>.</p></li></ul></li><li className="li"><p className="p">In the <span className="ph uicontrol">Test Execution</span> tab: </p><ul className="ul"><li className="li"><p className="p">Changed UI text from <span className="ph uicontrol">Pre-Installed Katalon Studio Location</span> to <span className="ph uicontrol">Pre-Installed Katalon Runtime Engine Location</span> in the <span className="ph uicontrol">Schedule Test Run</span> dialog.</p></li><li className="li"><p className="p">Changed UI text from <span className="ph uicontrol">Katalon Studio version</span> to <span className="ph uicontrol">Katalon Runtime Engine version</span> in the session details.</p></li></ul></li><li className="li"><p className="p">In the <span className="ph uicontrol">Settings</span> panel:</p><ul className="ul"><li className="li"><p className="p">Added the <span className="ph uicontrol">Support Management</span> button in the <span className="ph uicontrol">TestOps Admin</span> settings. This option allows an organization owner or administrator to assign supported slots to members for ticket submission.</p></li></ul></li></ul></li><li className="li"><p className="p">[Visual Testing]:</p><ul className="ul"><li className="li"><p className="p">Enabled the ability to move and edit applied-all ignored zones. See <a className="xref" href="/katalon-platform/analyze/analytics/visual-testing/use-testops-visual-testing#task-8096">Apply an ignored zone to all baseline images</a>.</p></li><li className="li"><p className="p">Added the <span className="ph uicontrol">Analyzing</span> status to the comparison methods when the process is being run.</p></li></ul></li></ul></div>

## <a id="concept-3027" class="anchor_top_offset"/>July 5th 2022


### New features

<div xmlns="http://www.w3.org/1999/xhtml" className="p"><ul className="ul"><li className="li"><p className="p">[Reports] Introduced the <span className="ph uicontrol">Incomplete</span> status for test runs.</p></li></ul></div>

### Enhancements

<div xmlns="http://www.w3.org/1999/xhtml" className="p"><ul className="ul"><li className="li"><p className="p">Upgraded dependencies to version 1.3.3-AC for the Jira cloud add-on.</p></li><li className="li"><p className="p">Optimized data fetching from Git repositories.</p></li><li className="li"><div className="p">[Visual Testing]:<ul className="ul"><li className="li"><p className="p">Allowed an ignored zone to be applied to all baseline images in a baseline collection.</p></li><li className="li"><p className="p">Allowed an ignored zone to be deleted in all baseline images in a baseline collection.</p></li><li className="li"><p className="p">Enabled navigation back to the baseline collection details from the baseline collection history.</p></li><li className="li"><p className="p">Combined the <span className="ph uicontrol">Results</span> and <span className="ph uicontrol">Checkpoints</span> tabs into one <span className="ph uicontrol">Results</span> tab in the <span className="ph uicontrol">Visual Test Run</span> section.</p></li></ul></div></li></ul></div>

### Fixes

<div xmlns="http://www.w3.org/1999/xhtml" className="p"><ul className="ul"><li className="li"><div className="p">Bug: Could not clone Bitbucket repository from a branch containing <code className="ph codeph">/</code> (e.g., <code className="ph codeph">test/develop</code>).<div className="note note note_note"><span className="note__title">Note:</span> <ul className="ul"><li className="li"><p className="p">Users need to upgrade the agent to the latest version 1.7.4. </p></li></ul></div></div></li></ul></div>

## <a id="concept-6822" class="anchor_top_offset"/>June 7th 2022


### New features

<div xmlns="http://www.w3.org/1999/xhtml" className="p"><ul className="ul"><li className="li"><div className="p">Visual testing:<ul className="ul"><li className="li"><p className="p">Introduced the <strong className="ph b">Configure Ignored Zones </strong>feature. See: <a className="xref" href="/katalon-platform/analyze/analytics/visual-testing/use-testops-visual-testing#task-44">Add an ignored zone to a baseline image</a>. </p></li><li className="li"><p className="p">Introduced the <strong className="ph b">Visual Baseline Collection </strong> feature. See: <a className="xref" href="/katalon-platform/analyze/analytics/visual-testing/baseline-collection">Baseline collection</a>. </p></li><li className="li"><p className="p">Added <strong className="ph b">Visual Testing</strong> option in the <strong className="ph b">Schedule Test Runs</strong> dialog to associate test runs with a baseline collection.</p></li></ul></div></li></ul></div>

### Enhancements

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">[Visual Testing] Enabled marking multiple checkpoints as passed or failed. </p></li><li className="li"><p className="p">[Test Case Management] Added <strong className="ph b">Flakiness</strong>,<strong className="ph b"> Last Updated</strong>, <strong className="ph b">Average Duration</strong>, <strong className="ph b">Last Executed</strong> in the Test Case filter search. </p></li><li className="li"><p className="p">[Test Case Management] Added the status for each test case, the <strong className="ph b">No. of execution </strong>column and enabled all linked requirements to be displayed in the <strong className="ph b">Requirements</strong> column.</p></li></ul> 

## <a id="concept-7781" class="anchor_top_offset"/>May 9th 2022


### New features

<div xmlns="http://www.w3.org/1999/xhtml" className="p"><ul className="ul"><li className="li">Implemented the new design for Project Dashboard, adding new dashboards (Productivity and Quality). See: <a className="xref" href="/katalon-platform/analyze/reports/view-test-reports/view-testops-dashboard/testops-dashboard-overview">Introduction to TestOps Dashboard</a>.</li><li className="li">Introduced two AI-powered features for visual testing (two additional comparison methods supported by AI engine). See: <a className="xref" href="/katalon-platform/analyze/analytics/visual-testing/visual-testing-overview">Visual Testing Overview</a>.</li></ul></div>

### Enhancements

<div xmlns="http://www.w3.org/1999/xhtml" className="p"><ul className="ul"><li className="li">[Integration] Enabled compatibility for Jira version 8.19.1 with Katalon TestOps adds-on.</li><li className="li">[UI/UX] Separated Visual Testing from Reports module. Visual Testing has now become an independent module on TestOps.</li><li className="li">[UI/UX] In the <strong className="ph b">Test Runs</strong> page, added filters for operating system and browser with their corresponding columns in the <strong className="ph b">All Test Runs</strong> grid.</li></ul></div>

## <a id="concept-8164" class="anchor_top_offset"/>March 29th 2022


### New features

<div xmlns="http://www.w3.org/1999/xhtml" className="p"><ul className="ul"><li className="li"><p className="p">Introduced the Test Runs Overview module. See: <a className="xref" href="/katalon-platform/analyze/reports/view-test-reports/test-runs-reports-overview">Test Runs Overview</a>.</p></li><li className="li"><p className="p">Allowed access to a demo site from the organization's dashboard.</p></li><li className="li"><p className="p">Introduced onboarding tours for key TestOps functionalities.</p></li></ul></div>

### Enhancements

<div xmlns="http://www.w3.org/1999/xhtml" className="p"><ul className="ul"><li className="li"><p className="p">[UI/UX] Disabled the Survey Monkey in the <strong className="ph b">Test Run Details</strong> page.</p></li><li className="li"><p className="p">[Script Repository] Required username and PAT input when creating a new Git script repository.</p></li><li className="li"><p className="p">[UI/UX] Retained the state of previous page in the <strong className="ph b">Test Suite Details</strong> page.</p></li><li className="li"><p className="p">[UI/UX] In the <strong className="ph b">Schedule Test Run</strong> dialog, when choosing <strong className="ph b">Test Suite</strong> for type:</p><ul className="ul"><li className="li">Added <strong className="ph b">Chrome (headless)</strong> and <strong className="ph b">Firefox (headless)</strong> options in the <strong className="ph b">Run with</strong> dropdown list.</li><li className="li">Removed the currently-selected TestCloud platforms if choosing a different browser from the <strong className="ph b">Run with</strong> dropdown list.</li></ul></li><li className="li"><p className="p">[UI/UX] Allowed automatic navigation to the <strong className="ph b">TestOps</strong> folder in which the new Test Suite has just been created.</p></li><li className="li"><p className="p">[Administration] Introduced the new license types. See: <a className="xref" href="/katalon-studio/katalon-studio-enterprise-and-katalon-runtime-engine-license/deprecation-of-node-locked-and-floating-license-models#id_1">Sunsetting plan for node-locked and floating licenses</a>.</p></li></ul></div>

## <a id="concept-5517" class="anchor_top_offset"/>February 28th 2022


### New features

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Introduced AWS CodeCommit for test scheduling and test management. Read more: <a className="xref" href="/katalon-platform/organize/configure-a-git-repository-in-testops">Upload Test Scripts from a Git Repository</a>.</p> 

### Enhancements

<div xmlns="http://www.w3.org/1999/xhtml" className="p"><ul className="ul"><li className="li">[Test Suite Management] Enabled test suite deletion.</li><li className="li">[UX/UI] [Test Suite] Allowed script repository to be indicated under loading.</li><li className="li">Disabled .zip script repository uploads for unused projects.</li><li className="li">[UX/UI] [Schedule Test Run] Appended path to test suite name when scheduling test run with Test Suite type.</li><li className="li">[UX/UI] [Schedule Test Run] Made TestCloud as default option in environment selection.</li></ul></div>

### Fixes

<div xmlns="http://www.w3.org/1999/xhtml" className="p"><ul className="ul"><li className="li">Bug: Resolved security bugs.</li></ul></div>

## <a id="concept-9809" class="anchor_top_offset"/>January 20th 2022


### New features

<div xmlns="http://www.w3.org/1999/xhtml" className="p"><ul className="ul"><li className="li">Introduced test suite functionalities for TestOps. Users can create, execute and manage test suites. Read more: <a className="xref" href="/katalon-platform/organize/manage-tests-in-testops/manage-test-suites-in-katalon-testops">Manage Test Suites</a>.</li><li className="li">Introduced the design for test suite management. Read more: <a className="xref" href="/katalon-platform/organize/manage-tests-in-testops/manage-test-suites-in-katalon-testops">Manage Test Suites</a>.</li><li className="li">Introduced GitLab and Azure Repos integration for test scheduling and test management. Read more: <a className="xref" href="/katalon-platform/organize/configure-a-git-repository-in-testops">Upload Test Scripts from a Git Repository</a>.</li><li className="li">Introduce TestCloud Trial Period as a new multi-browser testing environment. Read more: <a className="xref" href="/katalon-testcloud/testcloud-overview">TestCloud Overview</a>.</li></ul></div>

### Enhancements

<div xmlns="http://www.w3.org/1999/xhtml" className="p"><ul className="ul"><li className="li">[Integration] Enabled users to merge existing test results when configuring a new script repository integration.</li><li className="li">[Test Case Management] Enabled the script repository folder refresh in the directory view.</li><li className="li">[UX/UI] Enabled users to resize the test management directory view.</li><li className="li">[UX/UI] Indicated that the script repository is loading.</li><li className="li">[TestCloud] Displayed <em className="ph i">Trial</em> tag for TestCloud environment option when scheduling test runs.</li></ul></div>

## <a id="id_1" class="anchor_top_offset"/>December 13th, 2021


### New features

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">Introduced a new design for test case management. Read more: <a className="xref" href="/katalon-platform/organize/view-test-scripts-in-katalon-testops">Manage Test Cases</a>.</p></li></ul> 

### Enhancements

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">[UI] Updated the navigation bar.</p></li><li className="li"><p className="p">[UI] Added breadcrumbs of Test Case paths in the Test Case's detailed page.</p></li></ul> 

### Fixes

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">[Bug] Cannot schedule test runs from Katalon Studio when moving refreshed Test Suite Collection to the queue.</p></li></ul> 

## <a id="id_5" class="anchor_top_offset"/>November 2nd 2021


### New features

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">Introduced further capabilities to current Mark as Passed/Failed feature. Read more: <a className="xref" href="/katalon-platform/analyze/reports/manage-reports/override-test-results-status-in-katalon-testops">Override Test Result status</a>.</p></li><li className="li">Improved Test Run report with new stacked bar chart</li><li className="li"><p className="p">Introduced TestCloud as a test environment to schedule a Test Run (for beta users only). Read more: <a className="xref" href="#">Integrate TestCloud with TestOps</a></p></li></ul> 

### Enhancements

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">[UI] Updated Organization and Project navigation menu</li><li className="li"><p className="p">[UI] Updated Settings menu</p></li><li className="li"><p className="p">[UI] Automatically remove machine ID when user is removed - Activate License validation</p></li><li className="li"><p className="p">[UI] View original &amp; latest status in test result</p></li><li className="li"><p className="p">[Reports] Added confirmation dialog before sharing reports via email</p></li></ul> 

### Fixes

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">[Jira Integration] Can not refresh Jira status if user has deleted Jira release</p></li><li className="li"><p className="p">[Access Log] Access Log records do not have IP Address values</p></li></ul> 

## <a id="id_9" class="anchor_top_offset"/>September 29th 2021


### New features

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">Introduced Test Orchestration for Bitbucket repositories (sequential and parallel mode). Read more: <a className="xref" href="/katalon-platform/organize/configure-a-git-repository-in-testops">Upload Test Scripts from a Git Repository</a>.</p></li><li className="li"><p className="p">Introduced a new flow to schedule test runs. Read more: <a className="xref" href="/katalon-platform/execute/test-execution-with-testops/schedule-test-runs-in-testops">Schedule Test Runs</a>.</p></li></ul> 

### Enhancements

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">[Subscription] Enabled subscribing to TestOps Business via a "Get Quote" email.</p></li><li className="li"><p className="p">[License Management] Added max session timeout in Idle TimeOut.</p></li><li className="li"><p className="p">[UI] Updated invitation UI in User Management.</p></li><li className="li"><p className="p">[UI] Allowed to select Test Environment in Schedule Test Run dialog.</p></li><li className="li"><p className="p">[UI] Allowed to create Test Run Type without running or scheduling.</p></li><li className="li"><p className="p">[UI] Updated information in Script Repositories view (Create &amp; Edit).</p></li><li className="li"><p className="p">[UI] Consolidated Schedule Test Run button colors.</p></li><li className="li"><p className="p">[Access log] Added email address to access log files.</p></li><li className="li"><p className="p">[Test Run Type] Added sorting value by time.</p></li><li className="li"><p className="p">[Test Run Type] Removed data in Last Run column.</p></li><li className="li"><p className="p">[Reports] New confirmation dialog when exporting test run reports.</p></li><li className="li"><p className="p">[Reports] Allowed viewing re-run test results via email.</p></li><li className="li"><p className="p">[Jira integration] Synced Release status from Jira.</p></li><li className="li"><p className="p">[Jira integration] Enabled refreshing Jira release status in TestOps.</p></li></ul> 

### Fixes

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">[Agent] Local Agent status (online/offline) failed to show up when scheduling test runs.</p></li><li className="li"><p className="p">[Jira integration] Katalon Studio and TestOps integration (com.katalon.katalon-jira-plugin) failed HSTS Validation from Connect Security Requirements Tester.</p></li><li className="li"><p className="p">[Maintenance mode] Chart did not display and show error message after navigating to the Summary by Test Result page.</p></li></ul> 

## <a id="id_13" class="anchor_top_offset"/>July 26th 2021


### New features

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">Introduced Auto-distributed execution. Users can automatically distribute tasks to active and available Agents. Learn more: <a className="xref" href="/katalon-platform/execute/test-execution-with-testops/local-test-environments/auto-distributed-executions">Auto-Distributed Execution</a>.</p></li><li className="li"><p className="p">Introduced Test Usage Validation. Users can view how many test runs remain until their subscription quota is capped.</p></li><li className="li">Introduced Similar Error Suggestion. Users can view all common errors of their failed test results in the centralized view.</li></ul> 

### Enhancements

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">Enhanced filters for Reports &amp; Analytics.</p></li><li className="li">Enhanced component release summary.</li><li className="li">Enabled component to show test percentage in release readiness.</li><li className="li"><p className="p">Enhanced wizard for framework integration.</p></li><li className="li"><p className="p">Build visible under Configuration section for each Test Run.</p></li></ul> 

### Fixes

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">Could not filter API log by timestamp.</li><li className="li">testRuns (Number of test runs) field could be manipulated into invalid values.</li><li className="li">Long pending messages in Retry function.</li><li className="li">Path Injection, Zip Slip vulnerabilities.</li><li className="li">Occurrences where the app would break because of a missing LD config file.</li><li className="li">Uncommon error when creating thumbnail.</li><li className="li">User could fetch other organization's invoices from Payment Success screen.</li><li className="li">Week/day view of calendar would show wrong test runs when updating time zone.</li><li className="li">Manually uploading Katalon Reports in TestOps sometimes failed.</li><li className="li"><p className="p">Agent could not override Execution Mode of Test Suite Collection when executing with KRE 8.0/ 8.0.5 versions.</p></li><li className="li"><p className="p">Removed: polling message prompts for certain errors.</p></li></ul> 

## <a id="id_17" class="anchor_top_offset"/>June 22nd 2021


### New features

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">Added Re-run Test Results to the Test Results summary. See: <a className="xref" href="/katalon-platform/analyze/reports/view-test-reports/view-re-run-test-results-in-katalon-testops">View Re-run Test Results in TestOps</a>.</p></li></ul> 

### Enhancements

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">Updated maintainer column in Flaky Test list. </p></li><li className="li"><p className="p">Updated UI for Integration function. </p></li><li className="li"><p className="p">Enhanced security when updating Git test projects.</p></li></ul> 

### Fixes

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">Fixed a bug where users could not:</p><ul className="ul"><li className="li">migrate subscriptions.</li><li className="li">send an invitation email.</li><li className="li">calculate statistics for empty Test Runs.</li><li className="li">download a large Test Run as .xsls file.</li><li className="li">delete the execution.</li></ul></li><li className="li"><p className="p">Fixed the missing profile name on the execution page.</p></li><li className="li">Fixed search field for execution that doesn't re-run.</li><li className="li">Clarified the message for adding Users to Teams successfully.</li></ul> 

## <a id="id_21" class="anchor_top_offset"/>May 26th 2021


### Enhancements

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">Filter test runs by Build Name. <a className="xref" href="/katalon-platform/analyze/reports/manage-reports/filter-test-run-list-by-build-name-in-katalon-testops">Learn more</a>.</p></li><li className="li"><p className="p">View Release Readiness in TestOps Dashboard. <a className="xref" href="/katalon-platform/analyze/reports/view-test-reports/view-testops-dashboard/testops-dashboard-overview">Learn more</a>.</p></li></ul> 

## <a id="id_30" class="anchor_top_offset"/>April 26th 2021


### New features

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">Integration with Pytest. <a className="xref" href="/katalon-platform/analyze/reports/upload-test-reports/upload-reports-from-other-framework/upload-test-reports-from-pytest-to-katalon-testops">Learn more</a></p></li><li className="li"><p className="p">Integration with Kobiton. <a className="xref" href="#">Learn more</a></p></li><li className="li"><p className="p">Test Suite-based parallel execution. <a className="xref" href="/katalon-platform/execute/test-execution-with-testops/local-test-environments/run-multiple-test-suites-in-parallel-with-agents">Learn more</a></p></li></ul> 

### Enhancements

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">New release of Katalon agent version 1.7.</p></li><li className="li"><p className="p">Improve performance for Test Planning calendar view.</p></li></ul> 

## <a id="id_33" class="anchor_top_offset"/>March 8th 2021


### New features

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">Introduce a new term — Build — that is used in Katalon TestOps. <a className="xref" href="#">Learn more</a>.</p></li><li className="li"><p className="p">Create and manage Builds in Test Planning. <a className="xref" href="/katalon-platform/plan/create-and-manage-builds-in-katalon-testops">Learn more</a>.</p></li><li className="li"><p className="p">The "Task" feature has been removed.</p></li></ul> 

### Enhancements

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">Introduce a new and improved Katalon TestOps User Interface.</li></ul> 

## <a id="id_36" class="anchor_top_offset"/>January 19th 2021


### New features

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">Monitor Test Runs in a calendar view. <a className="xref" href="/katalon-platform/execute/test-execution-with-testops/schedule-test-runs-in-testops">Learn more</a></p></li><li className="li"><p className="p">Manage Test Runs with similar configurations with Test Run Types. <a className="xref" href="/katalon-platform/execute/test-execution-with-testops/schedule-test-runs-in-testops#task-7544">Learn more</a></p></li><li className="li"><p className="p">View Release Readiness by Test Case status &amp; Test Run history. <a className="xref" href="/katalon-platform/plan/create-and-edit-releases-in-testops">Learn more</a></p></li><li className="li"><p className="p">Manage <strong className="ph b">Katalon Studio</strong> Test Results (BDD and non-BDD). <a className="xref" href="/katalon-platform/analyze/reports/view-test-reports/view-bdd-test-results-in-testops">Learn more</a></p></li><li className="li"><p className="p">Automatically detect assertions in each Test Case for better quality evaluation &amp; failure investigation. </p></li><li className="li"><p className="p">Balance loads between multiple Test Environments. <a className="xref" href="/katalon-platform/execute/test-execution-with-testops/local-test-environments/load-balancing-for-local-test-environments">Learn more</a></p></li><li className="li"><p className="p">Support reports for Visual Testing. <a className="xref j-external-link" href="https://forum.katalon.com/t/visual-testing-image-comparison-with-katalon-studio-7-8-0-and-katalon-testops/45557" target="_blank">Learn more</a></p></li><li className="li"><p className="p">Create an Agent for Docker Environment. <a className="xref" href="/katalon-platform/execute/test-execution-with-testops/local-test-environments/create-a-local-test-environment-with-an-agent">Learn more</a></p></li><li className="li"><p className="p">Create a Kubernetes Environment. Learn more</p></li><li className="li"><p className="p">View reports of Web Services &amp; Test Objects.</p></li><li className="li"><p className="p">View abnormal Web Services for faster failure detection. <a className="xref" href="/katalon-platform/analyze/reports/view-test-reports/detect-abnormal-web-services-in-katalon-testops">Learn more</a></p></li><li className="li"><p className="p">View Requirement coverage heat map. <a className="xref" href="#">Learn more</a></p></li><li className="li"><p className="p">Detect the flakiness of Test Cases. <a className="xref" href="/katalon-platform/analyze/reports/view-test-reports/view-test-case-reports-in-katalon-testops">Learn more</a></p></li></ul> 

### Enhancements

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">Simplify the Local Test Environment setup process.</p></li><li className="li"><p className="p">Enhance CI integrations.</p></li><li className="li"><p className="p">Enhance UI/UX</p></li><li className="li"><p className="p">Simplify the Local Test Environment setup process.</p></li><li className="li"><p className="p">Enhance navigation to recent projects and on-going Test Runs.</p></li><li className="li"><p className="p">Enhance Jira issue lists.</p></li><li className="li"><p className="p">Centralize Test Run data for better collaboration.</p></li><li className="li"><p className="p">[Visual Testing] Incorporate reports into Test Run results.</p></li><li className="li"><p className="p">[Visual Testing] Provide execution comparisons with visualization.</p></li><li className="li"><p className="p">View Test Sessions with logs submitted from Test Environments.</p></li><li className="li"><p className="p">Support sharing Test Run report via email.</p></li><li className="li"><p className="p">Provide shortcuts to access reports.</p></li></ul> 
