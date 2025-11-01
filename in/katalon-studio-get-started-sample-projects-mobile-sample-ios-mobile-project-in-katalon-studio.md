---
title: Sample iOS mobile project in Katalon Studio
---
This sample demonstrates iOS testing fundamentals in Katalon Studio.

The application under test is the `Coffee Timer` application, which contains different timers for different coffee types.

You can learn more about mobile testing in these guides:

- [Mobile Recorder utility](https://docs.katalon.com/katalon-studio/record-and-spy/mobile-record-and-spy-utilities/mobile-recorder-utility)
- [[Mobile] Create and Run iOS Test Case](https://docs.katalon.com/katalon-studio/get-started/sample-projects/mobile/mobile-create-and-run-ios-test-case-in-katalon-studio)

## Requirements

- iOS setup. To set up Xcode simulators/ real iOS devices, you can refer to this document: [[Mobile] iOS Setup](https://docs.katalon.com/katalon-studio/manage-projects/set-up-projects/mobile-testing/ios/mobile-set-up-ios-real-devices).

## Open the sample iOS test project

To open the iOS sample project, in Katalon Studio, go to **File** > **New Sample Project** > **Sample iOS Mobile Tests Project**.

<img src="https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/iOS-sample-projects/KS-iOS-Open-the-iOS-sample.png" alt="Open iOS sample project" width="800" />

<br/>

Alternatively, you can download the iOS sample project from our GitHub repository: [iOS sample](https://github.com/katalon-studio-samples/ios-mobile-tests).

### Trust dialog on first open

When you open a sample project for the first time, Katalon Studio will show a **"Trust and open this project"** dialog. This security prompt ensures you’re aware of the source before opening and potentially executing harmful scripts.

<img alt="trust dialog ios " src="https://tw-cdn.katalon.com/katalon-studio/manage-projects/trust-dialog-pop-up/trust-dialog-mobile-ios.png" width="500"/>

In this dialog, you can:

- Review the project path.
- Decide whether to trust this project or all projects inside the parent folder.

:::note Notes
- Trusting a parent folder also trusts all projects directly inside it, including the one you're opening.
- However, if this project contains subfolders with separate project files, those sub-projects won’t be trusted automatically. You'll still see the trust dialog when opening them.
:::

- Click **Trust Project** to continue, or **Don't Open** if you’re unsure.

## Prepare the iOS application file

The `Coffee Timer` application located in the `App` folder of this sample project is pre-built and signed by the Katalon team to only run on Katalon devices.

<img src="https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/iOS-sample-projects/KS-iOS-Coffee-timer-app.png" alt="The sample coffee timer application" width="300" />

<br/>

As part of the iOS development procedure, to execute the sample test cases with your iOS devices, you need to build and sign the `Coffee Timer` application for your iOS devices.

### For iOS simulators

To execute the sample test cases with Xcode simulators, you need to prepare an `.app` file.

1. Open the `Coffee Timer.xcodeproj` project file with Xcode. To find the project save location, go to > **App** > **Your-First-iOS-App** > **Coffee Timer**. Double-click the `Coffee Timer.xcodeproj` file.

    <img src="https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/mobile-recorder-76/iOS/open-xcode-file.png" alt="KS - Coffee timer folder app" width="600" />

    
2. After opening the project in Xcode, choose one of the iOS simulators to launch the apps.

    <img src="https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/iOS-sample-projects/KS-iOS-Choose-simulator-1.png" alt="KS - choose 9th gen" width="400" />

    
3. To build the `.app` file, click **Product** > **Build**.
    
    When the build is finished, to find the `.app` file, go to `~/Library/Developer/Xcode/DerivedData/Coffee Timer/Build/Products/Debug-iphonesimulator/Coffee Timer.app`.
    
    :::note
    To quickly search for the `DerivedData` folder, copy and paste the following path `~/Library/Developer/Xcode/DerivedData` into the Spotlight Search.
    :::
    
4. Copy and paste the `Coffee Time.app` file into the `App` folder of the sample project. Katalon will use this file to start the `Coffee Time` application.

### For real iOS devices

To execute mobile testing with real iOS devices, you need to prepare an `.ipa` file.

1. Open the `Coffee Timer.xcodeproj` project file with Xcode. To find the project save location, go to **App** > **Your-First-iOS-App** > **Coffee Timer**. Double-click the `Coffee Timer.xcodeproj` file.
    
    <img src="https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/mobile-recorder-76/iOS/open-xcode-file.png" alt="Open Coffee Timer Xcode project" width="600" />

    
2. After opening the project in Xcode, select a registered iOS device to launch the apps.

    <img src="https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/mobile-recorder-76/iOS/select-device.png" alt="Choose the iOS device" width="400" />

    
3. In the **General** tab, set the deployment iOS version and select the device type in the **Deployment Info** section.
    
    <img src="https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/mobile-recorder-76/iOS/deployment.png" alt="Choose the iOS system" width="400" />

    
4. Switch to the **Signing & Capabilities** tab, check the **Automatically manage signing** box, then choose the team that has your device registered in the Apple Developer Portal.
5. To build the `.ipa` file, click **Product** > **Build**.
6. To archive the `.ipa` file, click **Product** > **Archive**. If the archive builds successfully, it appears in the Archives organizer.
7. To open the Archives organizer, choose **Window** > **Organizer** and click **Archives**.
8. Select the archive you want to export, then click **Distribute App** and follow the instructions to get the `.ipa` file. Here, we choose a development provisioning profile to export the `Coffee Timer.ipa` file.

    <img src="https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/mobile-recorder-76/iOS/export.gif" alt="Build the Coffee Timer.ipa" width="600" />

    
9. Verify the `.ipa` file.Once installed successfully, the application appears in the **Installed Apps**.
    1. Navigate to **Window** > **Devices** and **Simulators** in Xcode.
    2. Choose your device from the **Devices** list.
    3. Click **Add (+)** to browse the `.ipa` file.
    
    <img src="https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/mobile-on-macos/image2016-8-8-143A313A5.png" alt="Add the .ipa file to Xcode devices" width="600" />

    Once installed successfully, the application appears in the **Installed Apps**.

    <img src="https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/mobile-on-macos/image2016-8-8-143A313A14.png" alt="Add the .ipa file to Xcode devices" width="600" />

    
10. Put the `Coffee Time.ipa` file into the `App` folder of the sample project. Katalon will use this file to start the `Coffee Time` application.

## iOS sample project components

### Test cases


<img src="https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/iOS-sample-projects/KS-iOS-Test-cases.png" alt="Sample test cases" width="300" />

<br/>


There are two test cases for different purposes:

The **Mexican Coffee Timer** test case starts and stops the timer for making a Mexican coffee. In this example, we run the test case with a real iOS device.

- Start the `Coffee Timer.ipa` application. Here, we use the `sample.Common.startApplication` custom keyword to run the application.
- Tap **Mexican**. We set the timeout for 0 seconds.
- Tap **Start**. We set the timeout for 0 seconds.
- Tap **3:19**. We set the timeout for 0 seconds.
- Tap **Stop**. We set the timeout for 0 seconds.
- Tap **Back**. We set the timeout for 0 seconds.
- Close the application.

You can see the test script as follows:

```
import static com.kms.katalon.core.checkpoint.CheckpointFactory.findCheckpoint
import static com.kms.katalon.core.testcase.TestCaseFactory.findTestCase
import static com.kms.katalon.core.testdata.TestDataFactory.findTestData
import static com.kms.katalon.core.testobject.ObjectRepository.findTestObject
import com.kms.katalon.core.checkpoint.Checkpoint as Checkpoint
import com.kms.katalon.core.checkpoint.CheckpointFactory as CheckpointFactory
import com.kms.katalon.core.mobile.keyword.MobileBuiltInKeywords as MobileBuiltInKeywords
import com.kms.katalon.core.mobile.keyword.MobileBuiltInKeywords as Mobile
import com.kms.katalon.core.model.FailureHandling as FailureHandling
import com.kms.katalon.core.testcase.TestCase as TestCase
import com.kms.katalon.core.testcase.TestCaseFactory as TestCaseFactory
import com.kms.katalon.core.testdata.TestData as TestData
import com.kms.katalon.core.testdata.TestDataFactory as TestDataFactory
import com.kms.katalon.core.testobject.ObjectRepository as ObjectRepository
import com.kms.katalon.core.testobject.TestObject as TestObject
import com.kms.katalon.core.webservice.keyword.WSBuiltInKeywords as WSBuiltInKeywords
import com.kms.katalon.core.webservice.keyword.WSBuiltInKeywords as WS
import com.kms.katalon.core.webui.keyword.WebUiBuiltInKeywords as WebUiBuiltInKeywords
import com.kms.katalon.core.webui.keyword.WebUiBuiltInKeywords as WebUI
import internal.GlobalVariable as GlobalVariable

CustomKeywords.'sample.Common.startAppliucation'()

Mobile.verifyElementText(findTestObject('Spy/XCUIElementTypeStaticText - Mexican'), 'Mexican')

Mobile.tap(findTestObject('XCUIElementTypeStaticText - Mexican'), 0)

Mobile.tap(findTestObject('XCUIElementTypeButton - Start'), 0)

Mobile.tap(findTestObject('XCUIElementTypeStaticText - 319'), 0)

Mobile.tap(findTestObject('XCUIElementTypeButton - Stop'), 0)

Mobile.tap(findTestObject('XCUIElementTypeButton - Back'), 0)

Mobile.closeApplication()`

The **Verify the main list** test case verifies the list of the coffee name in the application. In this example, we run the test case with a real iOS device.

- Start the `Coffee Timer.ipa` application. Here, we use the `sample.Common.startApplication` custom keyword to run the application.
- Verify if the application is showing the **Mexican** item.
- Verify if the application is showing the **Colombian** item.
- Verify if the application is showing the **Coffees** item.
- Close the application.

```

You can see the test script as follows:

```
import static com.kms.katalon.core.checkpoint.CheckpointFactory.findCheckpoint
import static com.kms.katalon.core.testcase.TestCaseFactory.findTestCase
import static com.kms.katalon.core.testdata.TestDataFactory.findTestData
import static com.kms.katalon.core.testobject.ObjectRepository.findTestObject
import com.kms.katalon.core.checkpoint.Checkpoint as Checkpoint
import com.kms.katalon.core.checkpoint.CheckpointFactory as CheckpointFactory
import com.kms.katalon.core.mobile.keyword.MobileBuiltInKeywords as MobileBuiltInKeywords
import com.kms.katalon.core.mobile.keyword.MobileBuiltInKeywords as Mobile
import com.kms.katalon.core.model.FailureHandling as FailureHandling
import com.kms.katalon.core.testcase.TestCase as TestCase
import com.kms.katalon.core.testcase.TestCaseFactory as TestCaseFactory
import com.kms.katalon.core.testdata.TestData as TestData
import com.kms.katalon.core.testdata.TestDataFactory as TestDataFactory
import com.kms.katalon.core.testobject.ObjectRepository as ObjectRepository
import com.kms.katalon.core.testobject.TestObject as TestObject
import com.kms.katalon.core.webservice.keyword.WSBuiltInKeywords as WSBuiltInKeywords
import com.kms.katalon.core.webservice.keyword.WSBuiltInKeywords as WS
import com.kms.katalon.core.webui.keyword.WebUiBuiltInKeywords as WebUiBuiltInKeywords
import com.kms.katalon.core.webui.keyword.WebUiBuiltInKeywords as WebUI
import internal.GlobalVariable as GlobalVariable

CustomKeywords.'sample.Common.startAppliucation'()

Mobile.verifyElementText(findTestObject('Spy/XCUIElementTypeStaticText - Mexican'), 'Mexican')

MobileBuiltInKeywords.verifyElementText(findTestObject('Spy/XCUIElementTypeStaticText - Colombian'), 'Colombian')

MobileBuiltInKeywords.verifyElementText(findTestObject('Spy/XCUIElementTypeStaticText - Coffees'), 'Coffees')

Mobile.closeApplication()

```

### Test suites

To access the test suite in this project, in the **Test Explorer** panel, go to the **Test Suites** > **Smoke Tests** folder. This test suite combines the two test cases shown above.

<img src="https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/iOS-sample-projects/KS-iOS-Test-suite.png" alt="Test Suites" width="500" />


## Execute iOS tests

To execute a test case or a test suite in the sample project, follow these steps:

1. Select the test case/test suite you want to execute.
2. On the main toolbar, click on the **Run** dropdown menu and select **iOS** as the device type.

    <img src="https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/mobile-recorder-76/iOS/KS-TOOLBAR-iOS.png" alt="Execute iOS" width="200" />

    
3. In the displayed **iOS Devices** dialog, select an iOS device or Xcode simulator, then click **OK**.

    <img src="https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/mobile-recorder-76/iOS/ios-devices-list.png" alt="Choose iOS device" width="500" />

    
4. Observe the test result in the **Log Viewer** tab.

   <img src="https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/android-sample-prj/KS-ANDROID-Log-viewer.png" alt="View results" width="800" />
