---
title: Release Notes - Katalon TestOps
---

<!-- NOTE: Naming convention: G2 = Legacy, G3 = TestOps.
- 2025 Release Notes: https://katalon.atlassian.net/wiki/spaces/PM/pages/3566600257/2025+Releases -->

:::note
- This docset is not officially supported. It is only meant to be used as specific reference material. Please go to [Katalon TestOps' official documentation](https://docs.katalon.com/katalon-platform/get-started/get-started-with-katalon-testops) for the most accurate and up-to-date information.
:::

## May 15, 2025
<!---
Release notes:
- Core: https://katalon.atlassian.net/wiki/spaces/PM/pages/4159733761/TO-Core+Core.M.20250515
- Admin: https://katalon.atlassian.net/wiki/spaces/ADMIN/pages/4168450339/Release+Notes+-+TestOps+-+ADMIN+2025.05.14+-+May+14 
--->

## New features
<!--- Core --->
- Introduced AI-powered Visual Testing, allowing users to detect visual regressions in their application. Baseline collections can be managed and ignore zones can be set.

## Enhancements
<!--- Core --->
- Enhanced Test Suite management with Git Integration. This allows you to synchornize test suites between Katalon Studio and Katalon TestOps directly for a more seamless experience.

<!-- May 9, 2025 
- Admin: https://katalon.atlassian.net/wiki/spaces/ADMIN/pages/4155638094/Release+Notes+-+TestOps+-+ADMIN+2025.05.05
  - Minor release, enhancements only. Not added to this doc.
-->

<!-- May 7, 2025 
- MT: https://katalon.atlassian.net/wiki/spaces/SG/pages/4103209175/April-June+2025+Manual+Test+-+Release+Announcement#07-May-2025
- Core: https://katalon.atlassian.net/wiki/spaces/PM/pages/4159602689/TO-Core+Core.S.20250507 / https://katalon.atlassian.net/projects/TO/versions/11806/tab/release-report-all-issues
- Admin: https://katalon.atlassian.net/projects/TO/versions/11084/tab/release-report-all-issues 
  - Minor release, enhancements only. Not added to this doc.
-->

## April 23, 2025
<!---
Release notes:
- Admin: https://katalon.atlassian.net/wiki/spaces/ADMIN/pages/4116742258/Release+Notes+-+TestOps+-+ADMIN+2025.04.23+-+Apr+23+12+00
- Core: https://katalon.atlassian.net/wiki/spaces/PM/pages/4116938753/TO-Core+Core.S.20250423 
- RA: https://katalon.atlassian.net/wiki/spaces/PM/pages/4117495900/TO-RA+RA.M.20250423 
- MT: https://katalon.atlassian.net/wiki/spaces/SG/pages/4103209175/April-June+2025+Manual+Test+-+Release+Announcement#23-April-2025 
-->

### New features
<!--- Admin --->
- TestOps License Utilization provides tracking features that show how licenses are allocated and used across an organization and its users. This helps teams stay compliant and plan resources effectively.
- TestOps now supports TestCloud through a dedicated configuration area. TestCloud-related features can be managed directly within TestOps.
<!--- Manual Test --->
- Added an AI requirement analysis feature that analyzes requirements when generating test cases to clarify the scope of the test case.

### Enhancements
<!--- Admin --->
- Non-TestOps Account Admins now have restricted access to TestOps-specific settings. The user interface includes clearer prompts and streamlined permissions to prevent incorrect configurations and improve security.
<!--- Core --->
- The Create ALM Defect functionality now supports all data field types in the defect creation dialog. Users can now create defects directly from TestOps without needing to switch to another system.
<!--- Reports and Analytics --->
- The Home Dashboard now has customizable empty states and an improved widget layout. Users can now work with optimized default values and clearer data visualizations that improve both onboarding experience and data insights.
- Improved reporting with expanded test case distribution insights, clearer empty states, streamlined filters, and faster Test Run Detail page loading.
<!--- Manual Test --->
- Enhanced the new AI-assisted test case generation feature so users don't generate duplicated test cases from the same requirement and users can stop generating test cases should it take too long. 

### Bug Fixes
<!--- Core --->
- Fixed an issue where users could not add or remove test cases in Git-managed test suites despite the UI suggesting these actions were possible.
- Fixed an issue where a Personal Acccess Token (PAT) restriction message was displayed incorrectly when renaming a Test Suite in Katalon Cloud.
---

## April 16, 2025

*Katalon TestOps' TestPak has been updated with new minor features.*

### New features
- Added the ability to stop generating a test case should it take too long. 
- Added the ability to mark a test step result during a test run. 

---

## April 2, 2025

### *A new version of Katalon TestOps has been released!* 🎉

Katalon TestOps is a centralized platform for managing manual and automated testing with built-in analytics and AI capabilities. This solution helps you optimize testing processes, accelerate quality application delivery, and gain comprehensive visibility into quality metrics. 

You can track execution trends, identify bottlenecks, and make data-driven decisions through a streamlined interface that bridges the development-QA gap, supporting efficient workflows for organizations of any size.

This **all-new, updated version** introduces a modernized interface and enhanced capabilities to improve your test automation management experience.

### There are currently two versions of Katalon TestOps available:

### TestOps

<img src="https://tw-cdn.katalon.com/katalon-testops/Home/TestOps Home Full.png" alt="The Katalon TestOps new home page." width="1080"/>
<p align="center"><em>The Katalon TestOps' new home page within a Project.</em></p>

---

### TestOps Legacy
<img src="https://tw-cdn.katalon.com/katalon-testops/Home/TestOps Gen 2 Home 2.png" alt="The Katalon TestOps Legacy home page." width="1080"/>
<p align="center"><em>The Katalon TestOps Legacy home page within a Project.</em></p>

<br/>

You can still access your information from the previous version (TestOps Legacy) and continue using it as usual.

Documentation for both versions can be found in the [Katalon TestOps section](/katalon-platform/get-started/get-started-with-katalon-testops). 

:::note 
- Documentation for the new version of TestOps is temporarily marked as "alternate" in some sections. This will be removed. Then, TestOps Legacy will be referred to as such.
:::


<!-- Release notes 
- There were only bug fixes in this release and all were related to stability and performance fixes, so they were ommitted.
- Core: https://katalon.atlassian.net/wiki/spaces/PM/pages/4075913522/TO-Core+Core.S.20250402
- Admin: https://katalon.atlassian.net/wiki/spaces/ADMIN/pages/4076404763/Release+Notes+-+TestOps+-+ADMIN+2025.04.02+MAIN+RELEASE+-+Apr+02 
-->

---

## March 26, 2025
<!-- Release Notes:
- Admin: https://katalon.atlassian.net/wiki/spaces/ADMIN/pages/4044652816/Release+Notes+-+TestOps+-+ADMIN+2025.03.26
- Core: https://katalon.atlassian.net/wiki/spaces/PM/pages/4053992003/TO-Core+Core.L.20250326 
- Reports and Analytics: https://katalon.atlassian.net/wiki/spaces/PM/pages/4053992003/TO-RA+RA.L.20250326
- Manual Test: https://katalon.atlassian.net/wiki/spaces/SG/pages/3740633513/Jan-Mar+2025+Manual+Test+-+Release+Announcement#27-Mar-2025-RELEASED 
- Commerce Engine: https://katalon.atlassian.net/wiki/spaces/CE/pages/4054122785/Release+Notes+-+Commerce+Engine+-+CE+2025.03.26+-+Mar+26+13+31 
-->
*Katalon TestOps has been updated with new features and enhancements.*

### New features
<!-- Admin
- AI services PRD: https://katalon.atlassian.net/wiki/spaces/ADMIN/pages/3791683585/PRD+AI+Services+Configuration -->
- Introduced KSE release alerts. 
<!-- Core -->
- Introduced a seamless integration between TestOps and GitHub.
- Introduced the ability to link existing test cases to requirements.
- Introduced the ability to link specific releases or sprints to test runs. 
<!-- Reports and Analytics -->
- Added Iteration (Sprint/Release) filtering to key reports. 
<!-- Manual Test -->
- Introduced AI-assisted test case generation from a requirement. 
- Introduced in-app notifications for the executor of manual test schedule updates. 
- Introduced the ability to associate manual tets runs with a specific sprints.

### Enhancements
<!-- Admin -->
- Integrated the new configuration for AI services menu.
- Enhanced tracking for KRE and TestCloud License Utilization.
- Expanded the GitLab repostory Integration support at both system and project levels.
<!-- Reports and Analytics -->
- Customer-Driven UX Enhancements:
  - Chart/data table interaction improvements for Test Execution and Test Case Activity reports
  - Auto-apply local filters in Dashboards
  - Quick data preview with expandable widgets
  - New dashboard reset functionality
  - Enhanced report organization
  - Optimized query performance for release quality dashboard

---

## March 19, 2025
<!-- Release Notes: 
- Manual Test: https://katalon.atlassian.net/wiki/spaces/SG/pages/3740633513/Jan-Mar+2025+Manual+Test+-+Release+Announcement#19-Mar-2025-RELEASeD
-->

*Katalon TestOps' manual execution section has been updated with new features, enhancements, and general bug fixes.*

### New features
<!--- Executions --->
- Added executor notifications for test runs:
  - Instant notifications when assigned as a test run executor
  - Automated 15-minute reminders before scheduled test runs

---

## March 5, 2025
<!-- Release Notes: 
- Core: https://katalon.atlassian.net/wiki/spaces/PM/pages/3975545150/TO-Core+Core.S.20250305
- RA: https://katalon.atlassian.net/projects/TO/versions/11033/tab/release-report-all-issues
-->

*Katalon TestOps has been updated with new features and general bug fixes.*

### New features  

<!--- Core --->
- Added the ability to specify the KRE version during test run creation, allowing for better control over test execution environments.
- Upgraded Jira Plugin to Jira DC 10.3.x.
<!--- Reports and Analytics --->
- Added the ability to deep-dive from the Release Quality Dashboard into detailed reports.
- Added the ability to highlight relevant metrics that correspond to a certain quality crtieria in the Release Quality Dashboard.

### Bug fixes

<!--- Core --->
- Fixed errors with the Schedule Details interface.
- Resolved general UI issues. 

---

## Febrauary 19, 2025
<!-- Release notes: 
- Administration: https://katalon.atlassian.net/wiki/spaces/ADMIN/pages/edit-v2/3910336652? 
- Manual Test: https://katalon.atlassian.net/wiki/spaces/SG/pages/3740633513/Jan-Mar+2025+Manual+Test+-+Release+Announcement#19-Feb-2025-RELEASED
- Core: https://katalon.atlassian.net/wiki/spaces/PM/pages/3926230506/TO-Core+Core.M.20250219
- RA: https://katalon.atlassian.net/wiki/spaces/PM/pages/3926261792/TO-RA+RA.M.20250219 
-->

*Katalon TestOps has been updated with new features, enhancements, and general bug fixes.*

### New features

<!--- Administration --->
- Added the ability to manage a Github integration.
- Added the ability to manage KRE dedicated licenses for Organizations.
<!--- Dual Gen operation for G2-G3 ommitted as to not confuse users. -->
<!-- Executions --->
- Added the ability to edit manual test runs that have been scheduled. Users can modify anything from selected test suites, configurations, the assigned test executor, test run name, etc. (Note: test runs that are past its planned start time cannot be rescheduled.)
<!-- Core --->
- Added the feature for executors to receive notification upon being assigned to a test run.
- Added the feature for executors to receive reminders prior to scheduled test runs. 
<!-- Reports and Analytics --->
- Added the [Release Quality Dashboard](/katalon-testops/home/about-the-release-quality-dashboard): A new feature that provides a comprehensive view of release performance metrics, helping teams streamline their release management workflow.

### Enhancements
<!-- Executions -->
- Fixed accessibility issues for TestPak, the Create a Manual Test Run page, and the View Results page.
- Added internationalization to the Manual Editor. 
- Enhanced the Schedule Details interface with a new UI.

### Bug fixes
<!--- Administration --->
- Fixed errors related to the internal portal. 
- Fixed errors related to project integrations.
- Fixed errors related to license management.
- Fixed errors related to system integrations.
- Resolved various UI inconsistencies.
- Improved system stabilty and performance. 
- Fixed errors related to the Release Quality Dashboard and Home widgets.

---

## February 7, 2025
<!-- Release notes: 
- Manual Test: https://katalon.atlassian.net/wiki/spaces/SG/pages/3740633513/Jan-Mar+2025+Manual+Test+-+Release+Announcement#07-Feb-2025-RELEASED
-->

*Katalon TestOps' manual executions have been updated with new features and general bug fixes.*

### New features

<!--- Executions --->
- Added the ability to assign an executor for a manual test run. 
- Added the ability to select a release version for a manual test run.

### Bug fixes

<!--- Executions --->
- Fixed an error where the test case duration count continued even after a test run's end.
- Fixed an error where a user without the correct permissions could update test cases. 
- Fixed an error where switching manual tets cases while uploading attachments could cause errors. 
- Fixed general UI errors. 

---

## January 22, 2025
<!-- Release notes:
- RA: https://katalon.atlassian.net/wiki/spaces/PM/pages/3828842498/TO-RA+RA.S.20250122
-->

  *Katalon TestOps has been updated with new features for the Home Dashboard and bug fixes.*

### New features

<!--- Reports and Analytics --->
- Replaced statistics widget with pie charts for more intuitive data visualization. Impacted reports are:
  - Test execution during period by status
  - Total defect during period by status
  - Test case activity during period by status

- Implemented pie chart widgets for the Home Dashboard for the following statistics:
  - Execution Summary
  - Open Defects by Priority
  - Published Test Cases by Type

- Bar charts now support weekly Intevals, allowing for a clearer view of test execution trends.

### Bug fixes

<!--- Reports and Analytics --->
- Fixed an error where the Test Execution Result Report chart displayed incorrectly when there was no data. 
- Optimized the page loading time for the Requirement Coverage report.
- Fixed a bug with the Configuration Coverage Report imporperly showing data after filtering.
- Fixed general UI issues.

---


## January 15, 2025
<!-- Release notes:
- Admin:https://katalon.atlassian.net/wiki/spaces/ADMIN/pages/3791552550/Release+Notes+-+TestOps+-+ADMIN+2025.01.15+-+Jan+15
- MT: https://katalon.atlassian.net/wiki/spaces/SG/pages/3740633513/Jan-Mar+2025+Manual+Test+-+Release+Announcement#15-Jan-2025-RELEASED
- Core: https://katalon.atlassian.net/wiki/spaces/PM/pages/3799220225/TO-Core+Core.S.20250115
-->

*Katalon TestOps has been updated with new features, enhancements, and general bug fixes.*

### New features

- Added the ability to **schedule a manual test run**, allowing for planning and better test execution efficiency.
- Introduced multiple licensing report features designed to enhance visibility for license usage.
    - Introduced the **Seat-based: KSE License Usage** chart that displays license assignment and activity trends over time. 
    - Introduced the **Seat-based: KSE License Assignment and Activation History** chart that displays license allocation and usage trends.
    - Introduced the **Seat-based: KSE Assignment Details** table that displays actionable insights into individual license allocations and usage activity.
- Introduced API support for manual testing, allowing for the creation or cancellation of manual test schedules.

## Enhancements

- Automation Executions have been improved:
  - Scheduled test run times can now be edited.
  - Completed test runs can now be re-run to facilitate faster validation.


## Bug fixes

- Fixed general UI errors.
- Fixed general permission issues. 
- Fixed an error where scheduled test runs did not follow its automated start time.
- Fixed an error where the Jira integration could not be turned off in TestOps (original).
- Fixed an error where ALM projects wouldn't switch properly.
- Fixed an error where ADO requirements could not be linked to test case detail.

---

## January 8, 2025
<!--- Release notes:
- RA: https://katalon.atlassian.net/wiki/spaces/PM/pages/3771990019/TO-RA+RA.M.20250108
- Core: https://katalon.atlassian.net/wiki/spaces/PM/pages/3771859135/TO-Core+Core.M.20250108
- Admin: https://katalon.atlassian.net/wiki/spaces/ADMIN/pages/edit-v2/3758129296?
-->

*Katalon TestOps has been updated with new features, enhancements, and general bug fixes.*

### New features

<!--- Reports and Analytics --->
- Added the **Configuration Coverage Report** to provide users a detailed assessment of test coverage across various platforms within the Katalon software ecosystem. 
- New dashboard widgets have been added to the **Home Dashboard** to provide users with a more comprehensive overview of their test statuses and results:
    - **Test Execution Result Trend:** track daily test execution results with breakdown of passed, failed, error, incomplete, blocked, and skipped tests.

    - **Execution Summary:** view distribution of test results across all statuses with total execution count and percentages.

    - **Test Configuration Top Coverage:** monitor test execution coverage across operating systems and browsers with execution count.

    - **Open Defects by Priority:** view total defect count categorized by priority levels (High, Medium, Low).

    - **Defect Activity Trend:** track created, closed and accumulated open defects over time with daily breakdown.

    - **Published Test Cases by Type:** view published test cases categorized by type (Manual only, Automated only, Manual & Automated).

    - **Test Case Activity Progress:** monitor test case activity showing workflow progression from Draft to Published status.


<!--- TestOps --->
- Added the **Azure DevOps Integration** to allow users to sync their Azure DevOps projects with TestOps.
  - Added the ability to archive and unarchive ADO project configurations.
  - Added the ability to edit ADO project configurations for enhanced flexibility.
  - Added the ability to pull configurations from ADO.
  - Added the ability to create, edit, or disconnect an ADO integration.



## Enhancements

<!--- Reports and Analytics --->
- The Project Dashboard has been renamed to the **Home Dashboard**.
- The **Home Dashboard** filter has been changed:
    - Default time range is now the last 28 days
    - Users can select a sprint as a time range
    - Users can adjust time intervals for better data grouping
    - The filters for Profile and Release have been removed

<!--- TestOps --->
- Enhanced permissions for the Member role, allowing for better role-cased acccess control. 
- Simplified the **User Profile** by removing the phone number field. 

- **Automated Executions** have been improved:
  - Scheduled test runs can now be viewed in a full list with detailed insights.
  - Scheduled test runs can be run immedaitely using the **Run Now** option or cancelled if needed.
  - Scheduled test runs' configurations can be edited dynamically.
  - Added the ability to terminate a running test run, allowing for more granular control over execution processes.


## Bug fixes

<!--- Executions --->
- Fixed multiple erros when scheduling or interacting with scheduled test runs.

<!--- Reports and Analytics --->
- Fixed an error with the Requirement Coverage report showing incorrect data when filtering by release for the first time. 
- Fixed an error with the Requirement Coverage report not showing Jira IDs.
- Fixed an error with Configuration Coverage report where the local date range filter did not correctly update alongside the global date range filter.
- Fixed an error where reports were not generating properly.

<!--- TestOps --->
- Fixed general backend errors.
- Fixed general user permission errors. 
- Fixed general UI errors.
- Fixed general licensing errors. 
- Fixed an error where TestOps would not run with a local agent when choosing Visual Interface.

---

## January 6, 2025
<!-- Release notes:
- MT: https://katalon.atlassian.net/wiki/spaces/SG/pages/3740633513/Jan-Mar+2025+Manual+Test+-+Release+Announcement#06-Jan-2025-RELEASED
-->

*Katalon TestOps has been updated with new features, enhancements, and general bug fixes.*

### New features

<!--- Executions --->
- The **Create Manual Test Run** UI has been completely overhauled to streamline the user experience and match consistency with Automated test run workflows. 
- Users can now log defects directly wihtin TestPak for more seamless defect management. 

### Enhancements

<!--- Executions --->
- Added support for Comments and Attachments in **TestPak**.
- Added suuport for similar keyboard shortcuts with Excel to improve user experience.

### Bug fixes

<!--- Executions --->
- Fixed an error with TestPak where videos couldn't be downloaded in full.
- Fixed an error with user permissions regarding test case management.
- Fixed general UI errors.

---

## December 5, 2024

*Katalon TestOps has been updated with a new report type and general bug fixes.*

### New features

- **The Test Case Activity During Period by Status Report** has been introduced. This new report empowers users to better manage and analyze their test case workflows, ensuring improved organization and efficiency.
  - **Track Test Case Activity:** Monitor test cases created or updated within a specific time period or during a single sprint.
  - **Comprehensive Status Insights:** Gain visibility into test case statuses, including Draft, Ready for Review, In Review, and Published, for a clear understanding of the test case management process.
  - **Manual vs. Automated Classification:** Identify test cases as either manual or automated.

---

## November 27, 2024

*Katalon TestOps has been updated with two new features and general fixes.*

### New features

- **The Test Execution During Period by Status Report** has been introduced. This new feature enhances visibility into test progress and supports better-informed decision-making with:
  - **Visual Charts:** Gain insights with clear, visual representations of test execution results during a specified time period, categorized by status.
  - **Customizable Dashboard Integration:** [Add this report directly to your project's dashboard](/katalon-testops/manage-reports-and-analytics/edit-the-project-dashboard) for streamlined access and effortless monitoring of test execution trends.
- [TestPak](https://example.com) has been updated so users can view test results during an execution.
- [System integrations](/katalon-testops/administration-and-licensing/manage-systems/system-integrations/about-system-integrations) are now shown in a list.

---

## October 16, 2024

*The newest iteration of Katalon TestOps has been launched.*

### New features

- Users with a TestOps Guest license can access the **User Profile**, **User Settings**, **Dashboard**, and **Reports**.

### Enhancements

- Account Admins can resend or copy the invitation link for users with **Pending** status in **User Management**. See [Resend invitation to a user](/katalon-testops/administration-and-licensing/manage-organizations/user-management/resend-invitation-to-a-user).
- Minor UI enhancements in the **User Management** page.

---

## October 10, 2024

*The newest iteration of Katalon TestOps has been launched.*

### New features

This minor TestOps update includes new features aimed at enhancing general administrative functions, as well as minor enhancements and bug fixes.

- **Users can:**
  - View and [update their Account information](/katalon-testops/administration-and-licensing/manage-accounts/general/edit-account-information).
  - [Verify](https://example.com) or [remove Business Domains](/katalon-testops/administration-and-licensing/manage-systems/general/manage-business-domains/disown-or-reverify-a-business-domain) from their Account.
- **Account Admins can:**
  - Manage all Projects in their Account.

---

## October 2, 2024

*The newest iteration of Katalon TestOps has been launched.*

### Enhancements

This minor TestOps update includes features aimed at enhancing general functions to make them easier to work with.

- **Test case search improvement:** Users can now locate specific test cases via their IDs, simplifying the search process especially for large projects.
- **Test suite search improvement:** Users can now more easily locate test cases when building test suites.
- **Sprint/release timeline auto-sync:** Sprint, release, and requirement updates from Jira now automatically sync with TestOps, ensuring the latest information is always shown without manual intervention.
- **Bulk selection for test cases:** Users can now select all test cases in the test case table for quick bulk actions like move or delete.

---

## September 18, 2024 - GA

*The newest iteration of Katalon TestOps has been launched.*

### New features

- **View Jira releases or sprints in TestOps:**  
  TestOps now features a real-time release and sprint timeline within the Plans section. This seamless integration with Jira ensures you can easily stay up-to-date with the latest project schedules directly within TestOps.  
  For more information, see [About the sprint/release timeline](/katalon-testops/plan-and-collaborate/about-the-sprintrelease-timeline).

- **View requirements and assign testers:**  
  Within the timeline, users can click on sprints or releases to view linked requirements. QE leads can assign testers to these requirements for improved test coverage.  
  For more information, see [View requirement details](/katalon-testops/plan-and-collaborate/view-requirement-details) and [assign a tester to a requirement](/katalon-testops/plan-and-collaborate/about-the-sprintrelease-timeline#task-8424__assign-tester-to-requirement).

- **Create test cases from requirements and link them together:**  
  Test cases can be created directly from the requirement detail page, establishing an automatic, editable link between the test case and the requirement.  
  For more information, see [create test cases from requirements](/katalon-platform/plan/about-the-sprint-release-timeline#create-or-link-existing-test-cases-from-a-requirement) and [linkages](/katalon-testops/create-and-organize-tests/create-and-manage-test-cases/edit-test-cases/about-linkages).

- **Enter manual test case results:**  
  Users can easily input test case outcomes for manual test executions and then view the results in reports.  
  For more information, see [Add test results for manual executions](/katalon-testops/manage-executions/manual-executions/add-test-results-for-manual-executions) and [View a manual test run's report](/katalon-testops/manage-reports-and-analytics/report-types/view-a-manual-test-runs-report).

- **View the manual execution list:**  
  A consolidated list now houses all manual executions, providing a single location to view them.

---

## August 28, 2024 - Beta 3

*The Beta 3 iteration has been launched. This update introduces manual test step generation for test cases and a user detail page for enhanced administration, as well as improvements to the test run search bar and overall loading times.*

### New features

- **Generate test steps with AI:**  
  A test case's steps can now be automatically created using AI, speeding up test development.  
  For more information, see [Generate steps with AI](/katalon-testops/create-and-organize-tests/create-and-manage-test-cases/generate-steps-with-ai).

- **Administrate individual users:**  
  The new [User Detail page](/katalon-testops/administration-and-licensing/manage-organizations/user-management/view-the-user-detail-page) provides a complete overview of an individual user's information. It allows admins to change a user's Organization, edit their Account Roles, or add them to Projects.

### Enhancements

- **Test Run list search enhancement:**  
  Test runs can now be searched by their test run ID or name.
- **Performance fixes:**  
  Improved loading times for Reports and the Dashboard.

---

## July 24, 2024 - Beta 2

*The Beta 2 iteration has been launched. This update introduces sub-organizations, the User Management page, the Project Dashboard, and UI enhancements related to manual test case creation.*

### New features

This update includes features aimed at refining organizational functions, enhancing manual test case generation, and improving analytics monitoring via the Project Dashboard.

- **Organizational nesting:**  
  An organization can now contain sub-organizations, allowing flexible hierarchical structuring within accounts.  
  For more information, see [Create an Organization or sub-Organization](/katalon-testops/administration-and-licensing/manage-organizations/organization-management/create-an-organization-or-sub-organization).

- **User management:**  
  The new User Management page lists all users and their information, allowing admins to quickly locate users via search or filtering.  
  For more information, see [View User list](/katalon-testops/administration-and-licensing/manage-organizations/user-management/view-user-directory).

- **Project Dashboard:**  
  A customizable page with widgets that provides a bird's eye view of test statuses or results.  
  For more information, see [About the Project Dashboard](/katalon-testops/manage-reports-and-analytics/about-the-project-dashboard).

- **New manual test case editing features:**  
  The following functions have been added:
  - Wrap text for multiple lines within a cell.
  - Cut, copy, or paste content in steps.
  - Live hyperlinks in steps.
  - Undo and redo actions (up to 20).
  - Tab key navigation between rows.
  - A help menu explaining all supported shortcuts.

---

## June 26, 2024 - Beta 1

*The Beta 1 iteration of TestOps 3 has been launched. This update enables users to create, edit, and manage test cases, executions, and reports, as well as administer organizations and projects—all within a streamlined interface.*

### Introducing Katalon TestOps Gen 3

- This update introduces enhanced features aimed at refining test management processes, providing more granular user permission capabilities, and enhancing data visualization functions.
- Significant modifications to core testing workflows have been implemented to improve usability and efficiency.
- The user interface (UI) has been redesigned for more intuitive navigation and task execution.
- For more details on TestOps Gen 3, visit our [documentation page](/katalon-testops/get-started-with-katalon-testops/system-requirements).

---

*End of Release Notes*
