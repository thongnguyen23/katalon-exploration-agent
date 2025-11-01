---
title: Sample Android mobile project in Katalon Studio
---
This sample demonstrates Android testing fundamentals in Katalon Studio.

The application under test (AUT) is the `APIDemos.apk` application.

You can learn more about mobile testing in these guides:

- [Mobile Recorder utility](https://docs.katalon.com/katalon-studio/record-and-spy/mobile-record-and-spy-utilities/mobile-recorder-utility)
- [[Mobile] Create and Run Android Test Case in Katalon Studio](https://docs.katalon.com/katalon-studio/get-started/sample-projects/mobile/mobile-create-and-run-android-test-case-in-katalon-studio)

## Requirements

- Android setup. To learn more about setting up Android devices, you can refer to this document: [[Mobile] Android Setup](https://docs.katalon.com/katalon-studio/get-started/sample-projects/mobile/sample-android-mobile-project-in-katalon-studio#).
- If you are using Android Studio, you can refer to this document for the setup: [[Mobile] Configure Android Studio](https://docs.katalon.com/katalon-studio/manage-projects/set-up-projects/mobile-testing/android/mobile-configure-android-emulator).

## Open the sample Android test project

To open the Android sample project, in Katalon Studio, go to **File** > **New Sample Project** > **Sample Android Mobile Tests Project**. Katalon Studio will automatically detect and ask you to install Android SDK if your current machine does not have it or your Android SDK is not located at the default folder:`~/.katalon/tools/android_sdk`.

<img src="https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/android-sample-prj/KS-Android-Open-sample-Android.png" alt="Open Android sample project" width="800" />

<br/>

Alternatively, you can download the Android sample project from our GitHub repository: [Android sample](https://github.com/katalon-studio-samples/android-mobile-tests).

### Trust dialog on first open

When you open a sample project for the first time, Katalon Studio will show a **"Trust and open this project"** dialog. This security prompt ensures you’re aware of the source before opening and potentially executing harmful scripts.

<img alt="trust dialog android test " src="https://tw-cdn.katalon.com/katalon-studio/manage-projects/trust-dialog-pop-up/trust-dialog-android-test.png" width="500" />

In this dialog, you can:

- Review the project path.
- Decide whether to trust this project or all projects inside the parent folder.

:::note Notes
- Trusting a parent folder also trusts all projects directly inside it, including the one you're opening.
- However, if this project contains subfolders with separate project files, those sub-projects won’t be trusted automatically. You'll still see the trust dialog when opening them.
:::

- Click **Trust Project** to continue, or **Don't Open** if you’re unsure.

## Android sample project components

### Profiles

To open the execution profile, go to **Profiles** > **default**.

<img src="https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/android-sample-prj/KS-Android-Execution-profile.png" alt="Open execution profile in the sample Android project" width="700" />

<br/>

You can create and save all global variables in the execution profile. They can be used across test cases in your project. To learn more about execution profile, you can refer to this document: [Execution profile](https://docs.katalon.com/katalon-studio/data-driven-testing/global-variables-and-execution-profile).

Katalon creates four global variables in this sample project as follows:

| **Name** | **Value** |
| --- | --- |
| G_timeout | 10 |
| G_NotificationMessage | Your message has been sent. View message |
| G_AndroidApp | androidapp/APIDemos.apk |
| G_ShortTimeOut | 5 |

### Test cases

To access test cases in this project, go to the **Test Cases** folder in the **Test Explorer** panel.

<img src="https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/android-sample-prj/KS-ANDROID-Test-case.png" alt="Sample test cases in the Android project" width="400" />

<br/>

There are two test cases for different purposes:

1. The **Verify Correct Alarm Message** test case is to verify if we can get the correct displayed message.
    - Start the `APIDemos.apk` application. Here, the location of the AUT is under the `<sample-project-folder>/androidapp` folder. We use the following sample code to identify the absolute path to the application:
        
        ```
        /Get full directory's path of android application/
        def appPath = PathUtil.relativeToAbsolutePath(GlobalVariable.G_AndroidApp, RunConfiguration.getProjectDir())
        
        /Start the AUT/
        Mobile.startApplication(appPath, false)
        ```
        
    - Tap **App**. We set the timeout for 10 seconds.
    - Tap **Activity**. We set the timeout for 10 seconds.
    - Tap **Custom Dialog**. We set the timeout for 10 seconds.
    - Verify if the text displaying on the **App/Activity/Custom Dialog** dialog is correct.
        
    <img src="https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/android-sample-prj/KS-ANDROID-TC1.gif" alt="Verify Correct Alarm Message test case" width="800" />

        You can see the test script as follows:
        
        ```
        import static com.kms.katalon.core.testcase.TestCaseFactory.findTestCase
        import static com.kms.katalon.core.testdata.TestDataFactory.findTestData
        import static com.kms.katalon.core.testobject.ObjectRepository.findTestObject
        import internal.GlobalVariable as GlobalVariable
        import com.kms.katalon.core.configuration.RunConfiguration as RunConfiguration
        import com.kms.katalon.core.mobile.keyword.MobileBuiltInKeywords as Mobile
        import com.kms.katalon.core.util.internal.PathUtil as PathUtil
        import com.kms.katalon.core.webui.keyword.WebUiBuiltInKeywords as WebUI
        import com.kms.katalon.core.webservice.keyword.WSBuiltInKeywords as WS
        import static com.kms.katalon.core.checkpoint.CheckpointFactory.findCheckpoint
        import com.kms.katalon.core.model.FailureHandling as FailureHandling
        import com.kms.katalon.core.testcase.TestCase as TestCase
        import com.kms.katalon.core.testdata.TestData as TestData
        import com.kms.katalon.core.testobject.TestObject as TestObject
        import com.kms.katalon.core.checkpoint.Checkpoint as Checkpoint
        
        Mobile.comment('Story: Verify correct alarm message')
        
        Mobile.comment('Given that user has started an application')
        
        'Get full directory's path of android application'
        def appPath = PathUtil.relativeToAbsolutePath(GlobalVariable.G_AndroidApp, RunConfiguration.getProjectDir())
        
        Mobile.startApplication(appPath, false)
        
        Mobile.comment('And he navigates the application to Activity form')
        
        Mobile.tap(findTestObject('Alarm Message/android.widget.TextView - App'), 10)
        
        Mobile.tap(findTestObject('Alarm Message/android.widget.TextView - Activity'), 10)
        
        Mobile.comment('When he taps on the Custom Dialog button')
        
        Mobile.tap(findTestObject('Alarm Message/android.widget.TextView - Custom Dialog'), 10)
        
        'Get displayed message on the dialog'
        def message = Mobile.getText(findTestObject('Application/App/Activity/Custom Dialog/android.widget.TextViewCustomDialog'), 
          10)
        
        Mobile.comment('Then the correct dialog message should be displayed')
        
        Mobile.verifyEqual(message, 'Example of how you can use a custom Theme.Dialog theme to make an activity that looks like a customized dialog, here with an ugly frame.')
        
        Mobile.closeApplication()
        ```
        
2. The **Verify Last Items In List** test case is to verify whether we can identify the correct last item in the list.
    - Start the `APIDemos.apk` application. Here, the location of the AUT is under the `<sample-project-folder>/androidapp` folder. We use the following sample code to identify the absolute path to the application:
        
        ```
        /Get full directory path of the android application/
        def appPath = PathUtil.relativeToAbsolutePath(GlobalVariable.G_AndroidApp, RunConfiguration.getProjectDir())
        
        /Start the AUT/
        Mobile.startApplication(appPath, false)
        ```
        
    - Tap **Graphics**. We use the `G_Timeout` global variable as the timeout value.
    - Scroll to **Xfermodes** item.
    - Verify if the current screen should show Xfermodes text after scrolling

    <img src="https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/android-sample-prj/KS-ANDROID-TC2.gif" alt="Verify Last Items In List test case" width="800" />

    <br/>

        
        You can see the test script as follows:
        
        ```
        import static com.kms.katalon.core.testcase.TestCaseFactory.findTestCase
        import static com.kms.katalon.core.testdata.TestDataFactory.findTestData
        import static com.kms.katalon.core.testobject.ObjectRepository.findTestObject
        import internal.GlobalVariable as GlobalVariable
        import com.kms.katalon.core.configuration.RunConfiguration as RunConfiguration
        import com.kms.katalon.core.mobile.keyword.MobileBuiltInKeywords as Mobile
        import com.kms.katalon.core.util.internal.PathUtil as PathUtil
        
        Mobile.comment('Story: Verify correct alarm message')
        
        Mobile.comment('Given that user has started an application')
        
        'Get full directory's path of android application'
        def appPath = PathUtil.relativeToAbsolutePath(GlobalVariable.G_AndroidApp, RunConfiguration.getProjectDir())
        
        Mobile.startApplication(appPath, false)
        
        Mobile.comment('And he navigates the application to Graphics form')
        
        Mobile.tap(findTestObject('Last Items/android.widget.TextView - Graphics'), GlobalVariable.G_Timeout)
        
        Mobile.comment('When he scroll to Xfermodes text')
        
        Mobile.scrollToText('Xfermodes')
        
        Mobile.comment('Then the current screen should show Xfermodes text after scrolling')
        
        'Get item's label'
        def itemText = Mobile.getText(findTestObject('Last Items/android.widget.TextView - Xfermodes'), GlobalVariable.G_Timeout)
        
        Mobile.verifyEqual(itemText, 'Xfermodes')
        
        Mobile.closeApplication()
        ```
        

### Test suite

To access the test suite in this project, in the **Test Explorer** panel, go to the **Test Suites > Regression Tests** folder. This test suite combines the two test cases shown above.

<img src="https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/android-sample-prj/KS-ANDROID-Test-suites.png"alt="Test Suites"width="600" />


## Execute Android tests

To execute a test case or a test suite in the sample project, follow these steps:

1. Select the test case/test suite you want to execute.
2. On the main toolbar, click on the **Run** dropdown menu and select **Android** as the device type.

    <img src="https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/execute-mobile-testing-with-emulator/KS-TOOLBAR-Android.png"alt="Execute the selected test"width="200" />

    
3. Select your device from the **Android Devices** list. Click **OK**.
    
    <img src="https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/mobile-on-macos/device.png"  alt="Select the Android device"width="400" />

    
4. Observe the test result in the **Log Viewer** tab. To learn more about analyzing test execution logs, you can refer to this document: [[WebUI] Analyze Test Execution Logs and Debug the Test Case](https://docs.katalon.com/katalon-studio/get-started/sample-projects/webui/webui-analyze-test-execution-logs-and-debug-the-test-case-in-katalon-studio#concept-1867).
   
   <img src="https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/android-sample-prj/KS-ANDROID-Log-viewer.png" alt="View results" width="800" />
