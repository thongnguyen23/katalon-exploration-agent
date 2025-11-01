---
title: "Appdome integration"
---
Appdome is an integration platform that enhances the security of your mobile apps. Once the app is uploaded to Appdome, you can download and add the app to Katalon for automated mobile testing. The Appdome and Katalon integration ensures that the mobile apps are both secure and thoroughly tested. Some of Appdome's security features include:

- Android Debug Bridge (ADB) Blocking
- Anti-tempering
- Detect VPN
- Runtime Bundle Validation
- URL Whitelisting

This document outlines the quick steps to test Appdome-fused apps with Katalon.

## Prerequisites

* An active TestCloud subscription or trial
* [An Appdome account](https://fusion.appdome.com/signup)
* Mobile app file in `.apk` or `.aab` format (for Android), or in `.ipa` format (for iOS)
* You have uploaded the app to Appdome. For how-to, see the Appdome guide: [Uploading a mobile app to Appdome](https://www.appdome.com/how-to/mobile-app-security/mobile-data-encryption/uploading-a-mobile-app-to-appdome/)
* You have downloaded the Appdome-fused app. For how-to, see: [Download secured mobile apps from Appdome](https://www.appdome.com/how-to/devsecops-automation-mobile-cicd/test-secured-mobile-apps/download-secured-mobile-apps-from-appdome/)

## Test Appdome-fused app with Katalon

To streamline your testing workflow, you can upload the fused app to TestOps application repository. From there, you can leverage Katalon TestCloud's wide range of cloud-based mobile devices, reducing the need to set up a complex mobile testing environment. This process enables you to run your tests from both Katalon Studio and Katalon TestOps.

### Upload app

To upload your Appdome-fused app to TestOps, refer to this guide: [Upload a mobile app to TestOps](/katalon-testcloud/mobile-native-app-testing/upload-your-application/upload-a-mobile-app-to-testops). 

### Create tests with Katalon Studio

1. Open Katalon Studio and create a new mobile testing project.
2. Follow the instruction in the [Use Mobile Recorder on TestCloud devices](/katalon-testcloud/mobile-native-app-testing/record--spy-on-testcloud-devices/use-mobile-recorder-on-testcloud-devices) guide to create your test case.
3. Select your Appdome-fused app in the **Application** section.
4. Click **Start** to create your test case using the Mobile Recorder.
![Use Mobile Recorder with TestCloud mobile device](https://tw-cdn.katalon.com/katalon-testcloud/Record-and-Spy-on-TestCloud-devices/start-record-TC-device.png)

### Execute tests with Katalon TestOps

1. Sign in to Katalon TestOps and go to your Project.
2. Go to **Test Execution** > **Schedule Test Run** to open the dialog.
3. Follow the steps in the [Run mobile native app tests on TestOps](/katalon-testcloud/mobile-native-app-testing/mobile-native-app-testing-with-testcloud#run-mobile-native-app-tests-on-testops) guide.
4. In the **Mobile Native App** tab, select your mobile environment and the fused app.
<img src="https://tw-cdn.katalon.com/katalon-testcloud/appdome-integration/configure-test-env-for-test-suites.png" alt="Configure TestCloud environment on TestOps" width="600"/>
