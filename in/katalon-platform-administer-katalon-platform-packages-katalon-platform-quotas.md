---
title: Katalon Platform Quotas
---
import useBaseUrl from '@docusaurus/useBaseUrl';
import Reusable from '@site/src/reusable/Reusable.mdx';

<Reusable />

# Katalon Platform Quotas

Katalon TestOps comprises of different modules and services with their own individual quotas. These quotas represent how much of resources you can use according to your subscription plan.

This document lists out the quotas of Katalon TestOps and shows you how to view them.

## Quotas overview
The following are the quotas used throughout the platform.

### Test results
Katalon TestOps limits the number of test results, that is the results of test cases anywhere in the platform and reported in Katalon TestOps. A test result is counted under the following cases:
- The test result is of a test case executed via Katalon TestOps scheduler and other Katalon applications (Katalon Studio, Katalon TestCloud, Katalon Runtime Engine (KRE), Visual Testing), with Passed, Failed, Error, Incomplete status. Test cases with the Skipped status are not counted.

- The test result is imported from outside of Katalon applications, such as [JUnit](/katalon-platform/analyze/reports/upload-test-reports/upload-junit-and-katalon-studio-reports-to-testops-manually), [Mocha](/katalon-platform/analyze/reports/upload-test-reports/upload-reports-from-other-framework/upload-test-reports-from-mocha-to-katalon-testops), [Jest](/katalon-platform/analyze/reports/upload-test-reports/upload-reports-from-other-framework/upload-test-reports-from-jest-to-katalon-testops), [Jasmine](/katalon-platform/analyze/reports/upload-test-reports/upload-reports-from-other-framework/upload-test-reports-from-jasmine-to-katalon-testops), and [Pytest](/katalon-platform/analyze/reports/upload-test-reports/upload-reports-from-other-framework/upload-test-reports-from-pytest-to-katalon-testops).

- The test result is manually uploaded to TestOps using [TestOps interface](/katalon-platform/analyze/reports/upload-test-reports/upload-junit-and-katalon-studio-reports-to-testops-manually), [Command line using Report Uploader](/katalon-platform/analyze/reports/upload-test-reports/use-katalon-report-uploader), or from [Jenkins integration](/katalon-platform/integrations/cicd-integrations/jenkins-integration/use-katalon-plugins-for-jenkins-integration/integrate-jenkins-with-testops).
Test results that run under Debug mode in Katalon Studio are not counted (Katalon Studio does not allow uploading test results that run under Debug mode to TestOps).

### Active projects
An active project is a Katalon test project created in TestOps. Depending on your current Katalon TestOps subscription plan, there is a limit on the number of projects you can create.

Test projects created in Katalon Studio (not connected to the platform) are not counted into your active project quota.

### TestCloud sessions
The **TestCloud** per Session plan allows you to purchase a specific number of parallel sessions. One session enables you to run one sequence of tests, for as long as you need.

The number of TestCloud sessions that you purchase is the maximum number of parallel tests you can execute with TestCloud. If you schedule more parallel test runs than the purchased session quota, the additional test runs will be queued.

The maximum number of queued test runs is up to three times your session quota. For example, if your session quota is 5 sessions, you can queue 15 additional sessions.

### Visual testing checkpoint images
Visual Testing uses screenshots called checkpoint images to compare UI changes. These checkpoint images are taken via Visual Testing keywords (e.g., [[WebUI] Take Area Screenshot as a Checkpoint](/katalon-studio/keywords/keyword-description-in-katalon-studio/visual-based-web-testing-keywords/webui-take-area-screenshot-as-a-checkpoint) or [[WebUI] Take Area Screenshot)](/katalon-studio/keywords/keyword-description-in-katalon-studio/web-ui-keywords/webui-take-area-screenshot)).

## View your quotas
You can view quotas of different products in the **Usage Dashboard** section of the Katalon TestOps. Learn more about it here: [View Test Usage and Balance in the Usage Dashboard](/katalon-platform/administer/administration-tasks/manage-licenses/manage-license-usage/view-test-usage-and-balance-in-the-usage-dashboard).

To view your quotas, follow these steps:

1. Sign in to [TestOps Admin](https://my.katalon.com/) and select your Account.
2. From the Account admin page, select your Organization.
You are navigated to the Organization Admin page.
3. Under the **Dashboard** section, select the product with the associated quota that you want to view.
    For example, to view the test result quota of your Organization, select **Katalon Platform**.
    
    <img src="https://docs.katalon.com/e33b4750-c3f9-11ee-ac6d-0242c7a41fd4/KT-View_your_quota.png" alt="View your quota" width="700" />

#### Result
:::info notes 
Once 75% of your quota is reached, Account Owners or Account Billing Managers will receive a notification upon logging in to their Organization.
:::
It will look like this:
<img src="https://docs.katalon.com/f3ca8e60-2d17-11ee-bd4d-0242c7a41fd4/running_out_of_license_quota.png" alt="you are running our of license quota." width="500" /> <br/>

To avoid interruptions, please adjust your usage via the Usage Dashboard or buy more licenses accordingly.