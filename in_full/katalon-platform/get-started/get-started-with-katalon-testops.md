---
title: Get started with Katalon TestOps
---

import { TestOpsG2_TabNameValue, TestOpsG2_TabNameLabel, TestOpsG3_TabNameValue, TestOpsG3_TabNameLabel } from "../../../reusable-component";
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

This article shows you the different introductory components of Katalon TestOps.

<!-- Reusable component import -->
import Reusable from '@site/src/components/reusable-content/testops/note-testops-versions.mdx';

<Reusable />

<Tabs>
  <TabItem value={TestOpsG2_TabNameValue} label={TestOpsG2_TabNameLabel}>


## Get started with Katalon TestOps Legacy

In this section, learn about Katalon TestOps Legacy and its features.

Katalon TestOps is a test management platform that helps you manage your test data and collaborate with your team.

<br/>

<img src="https://tw-cdn.katalon.com/katalon-testops/Home/TestOps Gen 2 Home 2.png" alt="The Katalon TestOps Home page" width="1080"/>
<p align="center"><em>The Katalon TestOps Home page.</em></p>

<br/>


## Enrich the Katalon Studio experience

Katalon Studio is a powerful automation testing tool that can help you streamline your testing process and improve the quality of your software. However, testing authoring with Katalon Studio may not be enough. In an enterprise setting, you need to collaborate with several teammates and stakeholders. This is when you need to integrate with Katalon TestOps.

Katalon TestOps supports collaboration features, such as version control, shared test artifacts, and integration with other application lifecycle management tools (ALM). Take advantage of these features to collaborate effectively with your team and ensure that everyone is on the same page. See: [Upload test scripts from Git repository](/katalon-platform/organize/configure-a-git-repository-in-testops) and [View uploaded test scripts](/katalon-platform/organize/view-test-scripts-in-katalon-testops#task-179).

## Perform cross-browser testing with TestCloud

Katalon TestCloud is a test automation environment that allows you to execute tests on most standard browsers and operating systems on the cloud. With TestCloud, you can easily configure those test environments, reducing time and cost of creating physical infrastructure for test automation.

TestCloud addresses the following problems:

- Difficulty and inability to test across browsers and OS
- Scalability issues due to cost and time constraint in setting up physical labs
- Time-consuming configuration and integration for testing in different operating systems or scenarios
- Limited availability of test scenarios/devices/OS/browsers

**No setup and maintenance are required** to use TestCloud as your test environment. TestCloud is also ready to integrate with your CI/CD pipelines.

After setting up your test project and building test suites, follow these guides to execute with TestCloud:
- [Desktop browser testing with TestCloud](/katalon-testcloud/web-testing/desktop-browser-testing-with-testcloud)
- [Mobile browser testing with TestCloud](/katalon-testcloud/web-testing/mobile-browser-testing-with-testcloud)
- [Mobile native app testing with TestCloud](/katalon-testcloud/mobile-native-app-testing/mobile-native-app-testing-with-testcloud)

## Manage quality with analytics

In order to obtain relevant metrics on the progress of your tests as well as the completeness of your requirements, Katalon Platform provides test analysis features in both Katalon Studio and Katalon TestOps to make it easier for the entire project team to have a clear view of the overall readiness of the project.

Katalon Studio execution log and test suite / test suite collection reports give you an instant insight into how stable your test scripts are. It enables you to locate the root causes of any issues and troubleshoot them quickly. See: [View test reports in Katalon Studio](/katalon-studio/test-reports/view-test-reports/view-test-suite-and-test-suite-collection-reports-in-katalon-studio).

Katalon TestOps dashboards and reports allow you to centralize your test data in one place. As a QA manager, you can oversee your team productivity, and the status of product quality by looking at release readiness, requirement coverage, traceability matrix, and many more. See: [TestOps dashboards](/katalon-platform/analyze/reports/view-test-reports/view-testops-dashboard/testops-dashboard-overview).
  </TabItem>


  <TabItem value={TestOpsG3_TabNameValue} label={TestOpsG3_TabNameLabel} default>

  ## Get started with Katalon TestOps

In this section, learn about Katalon TestOps, its system requirements and log in options.

Katalon TestOps is a centralized platform for managing manual and automated testing with built-in analytics and AI capabilities. This solution helps you optimize testing processes, accelerate quality application delivery, and gain comprehensive visibility into quality metrics. 

You can track execution trends, identify bottlenecks, and make data-driven decisions through a streamlined interface that bridges the development-QA gap, supporting efficient workflows for organizations of any size.

This **all-new, updated version** introduces a modernized interface and enhanced capabilities to improve your test automation management experience.

<br/>

<img src="https://tw-cdn.katalon.com/katalon-testops/Home/TestOps Home Full.png" alt="The Katalon TestOps Home page" width="1080"/>
<p align="center"><em>The Katalon TestOps Home page.</em></p>

<br/>

  ### System requirements

:::note
- For use in conjunction with Katalon Studio, see [Supported environments for Katalon Studio and Katalon Runtime Engine (KRE)](/katalon-studio/supported-environments-for-katalon-studio-and-katalon-runtime-engine-kre)
:::

### Supported operating systems

* Windows
* Linux
* MacOS

### Supported browsers

Katalon TestOps supports the latest versions of the most common browsers such as: Firefox, Chrome, Edge Chromium, Internet Explorer, and Safari.

### IPs to whitelist

For users in controlled network environments, it is recommended that the following IPs be whitelisted to prevent network access errors. Go to our [Katalon domain and IP whitelist](/katalon-platform/troubleshooting/troubleshooting-common-administrative-issues/katalon-domain-and-ip-whitelist) page for a full list.

---

### Log in

Once you have created an account at Katalon, there are multiple ways with which you can log in to Katalon TestOps.

- Continue with Google
- Continue with GitHub 
- Continue with email
- Continue with SSO

<img src="https://tw-cdn.katalon.com/katalon-testops/Other/TestOps Login Options 2.png" alt="Log in to Katalon TestOps" width="1080"/>

### Login with SSO

When logging in with SSO, you’ll first be prompted to enter your Katalon domain. Depending on the login method configured by your administrator, you will either proceed with Single Sign-On (SSO) or log in using your username and password. 

<img src="https://tw-cdn.katalon.com/katalon-testops/Other/TestOps Custom Domain io.png" alt="Log in to Katalon TestOps" width="1080"/>

  </TabItem>
</Tabs>
