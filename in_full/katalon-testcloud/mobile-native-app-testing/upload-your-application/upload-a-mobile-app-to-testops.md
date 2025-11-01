---
title: Upload a mobile app to TestOps
---

TestCloud allows you to perform automated tests on mobile native applications. You can upload a mobile application and local Katalon Studio tests to TestOps, then use TestCloud to orchestrate test executions without having to set up local emulators or simulators.

:::caution Requirements
- An active Katalon TestCloud subscription or trial.
- A mobile application file in `.apk` or `.aab` format (for Android), or in `.ipa` format (for iOS).
- A mobile test project configured in TestOps.
    - To set up a sample project for iOS application testing, see [Open the sample iOS test project](/katalon-studio/get-started/sample-projects/mobile/sample-ios-mobile-project-in-katalon-studio).
    - To set up a sample project for Android application testing, see [Open the sample Android test project](/katalon-studio/get-started/sample-projects/mobile/sample-android-mobile-project-in-katalon-studio).
- For Android hybrid mobile applications, follow the configurations in this document: [Capture elements in hybrid Android apps](/katalon-studio/record-and-spy/mobile-record-and-spy-utilities/hybrid-mobile-apps-testing/native-render-only-webview-render-capture-elements-in-hybrid-android-apps-in-katalon-studio).
:::

Alternatively, you can log in to [TestCloud Web App](https://tcm.katalon.com/) and navigate to **Application** to upload app. This guide shows you how to upload a mobile application to TestOps using TestOps interface.

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

<Tabs>
  <TabItem value="testops-gen3" label="TestOps" default>
    
1. In [TestOps](https://platform.katalon.io/) home page, select **TestCloud** from the left sidebar.
2. Switch to the **Applications** tab, then click **Upload Application**.
   <img src="https://tw-cdn.katalon.com/katalon-testcloud/testcloud-gen3-upload-mobile-app.png" width="800" alt="Upload application screen" />
  </TabItem>
  <TabItem value="testcloud-web-app" label="TestCloud Web App">

1. Sign in to [TestCloud Web App](https://cloud.katalon.com/) site.
2. Select **Application** from the sidebar, then click **Upload Application**.
    <img src="https://tw-cdn.katalon.com/katalon-testcloud/testcloud-web-app-upload-mobile-app.png" width="800" alt="Upload application screen" />
  </TabItem>
  <TabItem value="testops-gen2" label="TestOps Legacy">
   
1. Sign in to [Katalon TestOps](https://testops.katalon.io/) and go to your project.
2. Go to **Test Execution** > **Application Repository**, then click **Upload Application**.
    <img src="https://tw-cdn.katalon.com/katalon-testcloud/Application_Repository_list.png" width="800" alt="Application repository list" />
  </TabItem>
</Tabs>
    
3. In the **Upload Application** dialog, click **Choose Files** and select the application you want to upload.
    <img alt="Choose application file to upload to Katalon TestOps" src="https://tw-cdn.katalon.com/katalon-testcloud/Select_application_file.png" width="500" />
    
    :::note
    - **Application Repository** supports uploading application files in `.apk`, `.aab`, and `.ipa`.
    - The size limit for the uploaded application is 500MB.
    :::

#### Result
Your mobile application file is successfully uploaded to TestOps. The metadata of each uploaded application will be displayed in the list.

- **Version**: The app version number shown to users (`CFBundleShortVersionString` in iOS, or `versionName` in Android).
- **Build**: The internal build number of the app (`CFBundleVersion` on iOS and `versionCode` on Android).
- **Status**: `READY` when the app is uploaded successfully, `PROCESSING` when the file is being uploaded and processed, `ERROR` when the upload failed.
- **Identifier**: A unique string assigned to an app to distinguish it from all other apps on a platform.
- **App ID**: A unique key assigned by TestCloud to represent your app in the system.