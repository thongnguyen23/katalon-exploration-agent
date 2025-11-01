---
hide_title: true
title: Mobile Recorder utility
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# Mobile Recorder utility

The Mobile Recorder utility in Katalon Studio allows you to create automated test cases for mobile applications. You perform actions on the application under test (AUT) as a user, and the recorder captures these actions to generate test cases.

## Device types

Katalon Studio provides three recording options for mobile test automation. Each option has distinct advantages, disadvantages, and prerequisites.

<div xmlns="http://www.w3.org/1999/xhtml" className="p"><table className="table anchor_top_offset" id="concept-6347__b2945b2c-dfc5-465c-8908-2040cc8c0ea2"><caption /><colgroup><col style={{width: '20%'}} /><col style={{width: '20%'}} /><col style={{width: '20%'}} /><col style={{width: '40%'}} /></colgroup><thead className="thead"><tr className><th className="entry anchor_top_offset" id="concept-6347__b2945b2c-dfc5-465c-8908-2040cc8c0ea2__entry__1">Device types</th><th className="entry anchor_top_offset" id="concept-6347__b2945b2c-dfc5-465c-8908-2040cc8c0ea2__entry__2">Pros</th><th className="entry anchor_top_offset" id="concept-6347__b2945b2c-dfc5-465c-8908-2040cc8c0ea2__entry__3">Cons</th><th className="entry anchor_top_offset" id="concept-6347__b2945b2c-dfc5-465c-8908-2040cc8c0ea2__entry__4">Prerequisites</th></tr></thead><tbody className="tbody"><tr className><td className="entry" headers="concept-6347__b2945b2c-dfc5-465c-8908-2040cc8c0ea2__entry__1 concept-6347__b2945b2c-dfc5-465c-8908-2040cc8c0ea2__entry__2 concept-6347__b2945b2c-dfc5-465c-8908-2040cc8c0ea2__entry__3 concept-6347__b2945b2c-dfc5-465c-8908-2040cc8c0ea2__entry__4 ">Local devices</td><td className="entry" headers="concept-6347__b2945b2c-dfc5-465c-8908-2040cc8c0ea2__entry__1 concept-6347__b2945b2c-dfc5-465c-8908-2040cc8c0ea2__entry__2 concept-6347__b2945b2c-dfc5-465c-8908-2040cc8c0ea2__entry__3 concept-6347__b2945b2c-dfc5-465c-8908-2040cc8c0ea2__entry__4 ">Direct control, no subscription needed.</td><td className="entry" headers="concept-6347__b2945b2c-dfc5-465c-8908-2040cc8c0ea2__entry__1 concept-6347__b2945b2c-dfc5-465c-8908-2040cc8c0ea2__entry__2 concept-6347__b2945b2c-dfc5-465c-8908-2040cc8c0ea2__entry__3 concept-6347__b2945b2c-dfc5-465c-8908-2040cc8c0ea2__entry__4 ">Complex mobile device setup process with occasional bugs.</td><td className="entry" headers="concept-6347__b2945b2c-dfc5-465c-8908-2040cc8c0ea2__entry__1 concept-6347__b2945b2c-dfc5-465c-8908-2040cc8c0ea2__entry__2 concept-6347__b2945b2c-dfc5-465c-8908-2040cc8c0ea2__entry__3 concept-6347__b2945b2c-dfc5-465c-8908-2040cc8c0ea2__entry__4 ">For Android:<ul className="ul"><li className="li"><p className="p"><a className="xref" href="/katalon-studio/manage-projects/set-up-projects/mobile-testing/android/mobile-configure-android-emulator">Android emulator</a></p></li><li className="li"><p className="p"><a className="xref" href="/katalon-studio/manage-projects/set-up-projects/mobile-testing/android/mobile-set-up-android-real-devices">Android real device</a></p></li></ul><div className="p">For iOS:<ul className="ul"><li className="li"><p className="p"><a className="xref" href="/katalon-studio/manage-projects/set-up-projects/mobile-testing/ios/mobile-ios-setup-simulators-in-katalon-studio">iOS simulator</a></p></li><li className="li"><p className="p"><a className="xref" href="/katalon-studio/manage-projects/set-up-projects/mobile-testing/ios/mobile-set-up-ios-real-devices">iOS real device</a></p></li></ul></div></td></tr><tr className><td className="entry" headers="concept-6347__b2945b2c-dfc5-465c-8908-2040cc8c0ea2__entry__1 concept-6347__b2945b2c-dfc5-465c-8908-2040cc8c0ea2__entry__2 concept-6347__b2945b2c-dfc5-465c-8908-2040cc8c0ea2__entry__3 concept-6347__b2945b2c-dfc5-465c-8908-2040cc8c0ea2__entry__4 ">Remote devices</td><td className="entry" headers="concept-6347__b2945b2c-dfc5-465c-8908-2040cc8c0ea2__entry__1 concept-6347__b2945b2c-dfc5-465c-8908-2040cc8c0ea2__entry__2 concept-6347__b2945b2c-dfc5-465c-8908-2040cc8c0ea2__entry__3 concept-6347__b2945b2c-dfc5-465c-8908-2040cc8c0ea2__entry__4 ">Access to a wide range of real devices for thorough testing, useful for cross-platform compatibility.</td><td className="entry" headers="concept-6347__b2945b2c-dfc5-465c-8908-2040cc8c0ea2__entry__1 concept-6347__b2945b2c-dfc5-465c-8908-2040cc8c0ea2__entry__2 concept-6347__b2945b2c-dfc5-465c-8908-2040cc8c0ea2__entry__3 concept-6347__b2945b2c-dfc5-465c-8908-2040cc8c0ea2__entry__4 ">Requirements of remote servers and management of network connections, potential latency issues</td><td className="entry" headers="concept-6347__b2945b2c-dfc5-465c-8908-2040cc8c0ea2__entry__1 concept-6347__b2945b2c-dfc5-465c-8908-2040cc8c0ea2__entry__2 concept-6347__b2945b2c-dfc5-465c-8908-2040cc8c0ea2__entry__3 concept-6347__b2945b2c-dfc5-465c-8908-2040cc8c0ea2__entry__4 ">See:<ul className="ul"><li className="li"><p className="p"><a className="xref" href="/katalon-studio/manage-projects/set-up-projects/mobile-testing/mobile-app-testing-with-remote-devices">Mobile app testing with remote devices</a>.</p></li><li className="li"><p className="p"><a className="xref" href="/katalon-studio/integrations/test-execution/kobiton-integration-with-katalon-studio">Kobiton integration with Katalon Studio</a>.</p></li></ul></td></tr><tr className><td className="entry" headers="concept-6347__b2945b2c-dfc5-465c-8908-2040cc8c0ea2__entry__1 concept-6347__b2945b2c-dfc5-465c-8908-2040cc8c0ea2__entry__2 concept-6347__b2945b2c-dfc5-465c-8908-2040cc8c0ea2__entry__3 concept-6347__b2945b2c-dfc5-465c-8908-2040cc8c0ea2__entry__4 ">TestCloud devices</td><td className="entry" headers="concept-6347__b2945b2c-dfc5-465c-8908-2040cc8c0ea2__entry__1 concept-6347__b2945b2c-dfc5-465c-8908-2040cc8c0ea2__entry__2 concept-6347__b2945b2c-dfc5-465c-8908-2040cc8c0ea2__entry__3 concept-6347__b2945b2c-dfc5-465c-8908-2040cc8c0ea2__entry__4 ">Access to multiple devices and configurations, no hardware needed, simple setup for users with minimal to no coding experience.</td><td className="entry" headers="concept-6347__b2945b2c-dfc5-465c-8908-2040cc8c0ea2__entry__1 concept-6347__b2945b2c-dfc5-465c-8908-2040cc8c0ea2__entry__2 concept-6347__b2945b2c-dfc5-465c-8908-2040cc8c0ea2__entry__3 concept-6347__b2945b2c-dfc5-465c-8908-2040cc8c0ea2__entry__4 ">Slower interaction and execution times compared to local devices.</td><td className="entry" headers="concept-6347__b2945b2c-dfc5-465c-8908-2040cc8c0ea2__entry__1 concept-6347__b2945b2c-dfc5-465c-8908-2040cc8c0ea2__entry__2 concept-6347__b2945b2c-dfc5-465c-8908-2040cc8c0ea2__entry__3 concept-6347__b2945b2c-dfc5-465c-8908-2040cc8c0ea2__entry__4 ">Subscription to TestCloud Mobile Native App testing. See TestCloud overview.</td></tr></tbody></table></div>

## Record a mobile application

Follow these steps to configure and execute your recording session effectively:

1. Click the **Record Mobile** icon on the main toolbar, and select your device type.

   <img src="https://tw-cdn.katalon.com/katalon-studio/record-and-spy/mobile-record-and-spy-utilities/KS_record_mobile.png" alt="Record Mobile" width="400"/>

2. In the displayed **Mobile Recorder** dialog, specify the device information in the **Configurations** section.

    <img className="image" width={300} src={useBaseUrl("/c257e3e2-652a-4d23-bc6e-851d56607538/ks-950-android-configurations.png")} />

    - **Device Name**: A mobile device where Katalon launches the application. All of your connected devices should be displayed in this list.
    - **Start with**: In the drop-down list, select either **Application File** or **Application ID**.
        - **Application File**: Browse your tested application (`.apk` file for Android; `.ipa` file for iOS).
        - **Application ID**: Specify the application ID of your tested application, which is either the package name of an Android app or the bundle identifier of an iOS app.

    For example, here we use the Android emulator for configuration setup.

3. Click **Start** on the action bar to begin recording.

    After starting the application, you can see the application display in **Device View** and the objects in **All Objects**:

    <img className="image" width={700} src={useBaseUrl("/1760ea0a-0df6-4734-9687-44ecffed96a6/ks-950-mobile-recorder-dialog.png")} />

    - **Device View** is a simulator of the device screen. You can interact with the AUT in this view.
    - **All Objects** captures and organizes all the displayed mobile objects of **Device View** in a tree.
    
    To make sure the **Device View** displays the current screen of the AUT on the device, click the **Capture Object** button on the action bar to reload **Device View** and refresh **All Objects**.

4. Perform actions on the AUT:

    1. Select any object either in the tree of **All Objects** or in **Device View**. Katalon highlights their counterpart accordingly for verification.

    <img className="image" width={600} src={useBaseUrl("/26ba5a10-8139-11ee-b53b-0242c7a41fd4/830-highlights.png")} />

    2. Choose a button in **Available Actions** to act on the selected object.

    To learn about available actions and UI elements, see [Available Actions](#available-actions) and [Validate UI elements](#validate-ui-elements).

    3. Repeat these two steps until all the actions you need to perform are completed.

5. Review the recorded actions.

    The **Recorded Actions** table shows all the recorded actions and related input/output you performed on the AUT. These items later become test steps in your test case.

    <img className="image" width={300} src={useBaseUrl("/ff52abd2-1f7a-45e3-967b-1ced393cd5d0/recorded-actions.png")} alt="recorded actions" />

    You can manually add new actions using keywords by clicking on **Add**, delete unwanted actions by clicking on **Remove**, or rearrange recorded actions by clicking on **Move Up** or **Move Down**.

6. Review properties of captured objects.

    **Captured Objects** displays all interacted objects during the recording session. For each object captured, you can find its detailed properties shown in the **Object Properties** table by clicking on it.

    The most important property of an object is its **Locator Strategy** and value. The default locator is a unique value in detecting that object.

    If you prefer another locator strategy, choose among the provided options and generate a new locator. Then click **Highlight** to confirm your newly updated locator can detect the target object correctly.

    <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/record-mobile-utility/830-selector-highlight.png")} alt="Verify new locators in captured objects section" />

    For more information about locator strategies, see [Locator strategies for Mobile objects](/katalon-studio/test-objects/mobile-test-objects/locator-strategies-for-mobile-objects).

7. When you finish a recording session, click **Stop**, then click **Save Script**.

    The **Add Element to Object Repository** dialog pops up asking you where to store recently captured objects. You can decide whether to merge, create duplicates or replace the existing objects:

    <img className="image" width={500} src={useBaseUrl("/33e0b090-8dbe-11ee-ab4f-0242c7a41fd4/KS_mobile_android_add_element_to_object_repository.png")} alt="Add Element to Object Repository dialog" />

    - **Merge changes into existing objects**: Add unique changes of the newly recorded object to the existing object, but still keep the existing object ID.
    - **Create duplicate objects**: Save the newly recorded object separately from the existing object.
    - **Replace existing objects**: The newly recorded object overrides the ID and attributes of the existing object.

8. After clicking **OK**, there are three (3) options to export the recorded actions to a test case:

    <img className="image" width={400} src={useBaseUrl("/335c34c4-5222-4f70-b810-acca851a49a5/KS-export-options.png")} alt="export options" />

    - **Export to new test case**: Creates a new test case with the recorded actions.
    - **Append to test case**: Adds the recorded actions to the end of an existing test case.
    - **Overwrite test case**: Replaces the existing actions in a test case with the recorded actions.

    After choosing your **Export Option**, click **OK**.

You have successfully set up and used the Mobile Recorder utility in Katalon Studio to create a mobile test case.

## Use Mobile Recorder on TestCloud devices

From Katalon Studio version 9.5.0 onwards, you can use TestCloud mobile devices for recording and playback. This feature removes the need for complex local setups and makes it easier for users with minimal coding experience to conduct mobile testing.

You need to upload your application file to TestOps and directly record objects on a TestCloud device.

Here's a demo video of using The Mobile Recorder on TestCloud devices:

<object data="https://fast.wistia.com/embed/medias/dcz81c669d" height={450} width={700}> </object>

### Requirements

- Katalon Studio Enterprise (KSE) version 9.5.0 onwards.
- A TestCloud Mobile Native App testing subscription.
- TestCloud integration enabled. See [Integrate TestCloud with Katalon Studio](/katalon-studio/get-started/workspace-settings/integrate-katalon-platform-with-katalon-studio).

### Upload a mobile app to TestOps

TestCloud allows you to perform automated tests on mobile native applications. You can upload a mobile application and local Katalon Studio tests to TestOps, then use TestCloud to orchestrate test executions without having to set up local emulators or simulators.

#### Requirements

- An active Katalon TestCloud subscription or trial.
- A mobile application file in .apk or .aab format (for Android), or in .ipa format (for iOS).
- A mobile test project configured in TestOps.
    - To set up a sample project for iOS application testing, see [Open the sample iOS test project](/katalon-studio/get-started/sample-projects/mobile/sample-ios-mobile-project-in-katalon-studio#open-the-sample-ios-test-project).
    - To set up a sample project for Android application testing, see [Open the sample Android test project](/katalon-studio/get-started/sample-projects/mobile/sample-android-mobile-project-in-katalon-studio).
- For Android hybrid mobile applications, follow the configurations in this document: Capture elements in hybrid Android apps.

Follow these steps to upload a mobile application to TestOps.

1. Sign in to Katalon TestOps and go to your project.

2. Go to **Test Execution > Application Repository**.

3. In the **Application Repository** page, click **Upload Application**.

    <img className="image" width={700} src={useBaseUrl("/321ce600-42b2-11ed-a602-0242cfbc79b5/Application_Repository_list.png")} alt="Application Repository list in Katalon TestOps" />

4. In the **Upload Application** dialog box, click **Choose Files** and select the application you want to upload.

    <img className="image" width={500} src={useBaseUrl("/359bfaa0-42b2-11ed-a602-0242cfbc79b5/Select_application_file.png")} alt="Choose application file to upload to Katalon TestOps." />

    :::note
    - **Application Repository** supports uploading application files in `.apk`, `.aab`, and `.ipa`.
    - The size limit for the uploaded application is 500MB.
    :::

Your mobile application file is successfully uploaded to TestOps.

### Record objects on a TestCloud device

To begin capturing objects on a TestCloud device, follow these steps:

1. From the main Toolbar, click the **Record Mobile** icon and select **TestCloud Devices**.

    <img className="image" width={400} src={useBaseUrl("/404f5b8a-1682-4a58-bd4a-5c93434da5e2/ks-950-mobile-recorder-select-testcloud.png")} />

    The Mobile Recorder dialog appears.

2. In the TestCloud Configurations section:

    <img className="image" width={400} src={useBaseUrl("/71c90365-7b4f-44dd-b261-6be4c13900fa/ks-972-testcloud-configurations.png")} />

    1. **Device Name**: Select the mobile operating system (OS), the version of the OS, and Studio will list out the available devices accordingly. 
    
    You can also select **Any Phone** or **Any Tablet** from the top of the list to let TestCloud automatically choose a suitable device that meets your requirements.

    2. **Show only high availability devices**: This option, enabled by default, filters the list to show devices with high availability status. You can then choose a device for testing without delays.

    - **When enabled**: Only devices with high availability status are shown.
    - **When disabled**: All devices are shown.

    3. **Application**: Select the application file you want to test from your TestOps uploads.

3. Click **Start** on the action bar to launch the AUT.

4. Follow from **Step 4** of [Record a mobile application](#record-a-mobile-application) to select objects.

## Available Actions

**Available Actions** contains multiple mobile action buttons that can be performed on the AUT.

<img src="https://tw-cdn.katalon.com/katalon-studio/record-and-spy/mobile-record-and-spy-utilities/KS_Mobile_Recorder_Utility_Available_Actions.png" alt="Mobile Available Actions" width="500"/>

There are two types of actions:

- **Object action**: Require selecting an object in Device View or All Objects. After selecting, you can see which actions are enabled for that object.
- **Application action**: Do not require selecting an object to perform.

| Available Actions     | Description     |
| ------------- | ------------- |
| [Tap](/katalon-studio/keywords/keyword-description-in-katalon-studio/mobile-keywords/mobile-tap) | Tap on a mobile element. |
| [Tap And Hold](/katalon-studio/keywords/keyword-description-in-katalon-studio/mobile-keywords/mobile-tap-and-hold) | Tap and hold on a mobile element for a duration. |
| [Swipe](/katalon-studio/keywords/keyword-description-in-katalon-studio/mobile-keywords/mobile-swipe) | Simulate swiping fingers on the mobile device. |
| [Get Text](/katalon-studio/keywords/keyword-description-in-katalon-studio/mobile-keywords/mobile-get-text)| Get the text of a mobile element. |
| [Set Text](/katalon-studio/keywords/keyword-description-in-katalon-studio/mobile-keywords/mobile-set-text) | Set the text on a mobile element. It also clears the previous value of the mobile element. |
| [Send Keys](/katalon-studio/keywords/keyword-description-in-katalon-studio/mobile-keywords/mobile-send-keys) | Simulates keystroke events on the specified element, as though you typed the value key-by-key. |
| [Set Encrypted Text](/katalon-studio/keywords/keyword-description-in-katalon-studio/mobile-keywords/mobile-set-encrypted-text) | Enter an encrypted text in an input field and clear the existing value of the input field. To encrypt a raw text, from the main menu, **Help > Encrypt Text**. |
| [Clear Text](/katalon-studio/keywords/keyword-description-in-katalon-studio/mobile-keywords/mobile-clear-text) | Clear text of a mobile element. |
| [Scroll To Text](/katalon-studio/keywords/keyword-description-in-katalon-studio/mobile-keywords/mobile-scroll-to-text) | Scroll to an element which contains the given text. |
| [Hide Keyboard](/katalon-studio/keywords/keyword-description-in-katalon-studio/mobile-keywords/mobile-hide-keyboard) | Hide the keyboard if it is showing. |
| [Press Back](/katalon-studio/keywords/keyword-description-in-katalon-studio/mobile-keywords/mobile-press-back) (Available on Android only) | Simulate pressing back button on a mobile device. |
| [Press Home](/katalon-studio/keywords/keyword-description-in-katalon-studio/mobile-keywords/mobile-press-home) | Simulate pressing the home button on a mobile device. |
| [Take Screenshot](/katalon-studio/keywords/keyword-description-in-katalon-studio/mobile-keywords/mobile-take-screenshot) | Take a screenshot of the current device screen.|
| [Switch To Web View](/katalon-studio/keywords/keyword-description-in-katalon-studio/mobile-keywords/mobile-switch-to-web-view) | Switch the current device to web view context. |
| [Switch To Native](/katalon-studio/keywords/keyword-description-in-katalon-studio/mobile-keywords/mobile-switch-to-native) | Switch the current device driver to native context. |
| [Switch To Landscape](/katalon-studio/keywords/keyword-description-in-katalon-studio/mobile-keywords/mobile-switch-to-landscape) | Switch the current mode of the device to landscape mode.|
| [Switch To Portrait](/katalon-studio/keywords/keyword-description-in-katalon-studio/mobile-keywords/mobile-switch-to-portrait) | Switch the current mode of the device to portrait mode. |

## Validate UI elements

Besides the available actions, you can right-click on any element in **Device View** or **All Objects** to access the context menu. Then, you can capture the selected object or add `Verify` and `Wait` keywords as test steps.

<img src="https://tw-cdn.katalon.com/katalon-studio/record-and-spy/mobile-record-and-spy-utilities/KS_Capture_Mobile_Object.png" alt="Capture Mobile Object" width="400"/>

The selected verification action is recorded in **Recorded Actions** table. Double-click on the **Input** field to add necessary values to some keywords.

<img src="https://tw-cdn.katalon.com/katalon-studio/record-and-spy/mobile-record-and-spy-utilities/KS_View_Recorded_Mobile_Actions.png" alt="View and edit Recorded Mobile Actions" width="400"/>

<img src="https://tw-cdn.katalon.com/katalon-studio/record-and-spy/mobile-record-and-spy-utilities/KS_View_Captured_Mobile_Objects.png" alt="View Captured Mobile Objects" width="400"/>

| Available Actions | Description | 
|----------|----------|
| Capture Object  | Used for capturing an object.  | 
| [Verify Element Exist](/katalon-studio/keywords/keyword-description-in-katalon-studio/mobile-keywords/mobile-verify-element-exist)   | Verify if a mobile element is present.  | 
| [Verify Element Not Exist](/katalon-studio/keywords/keyword-description-in-katalon-studio/mobile-keywords/mobile-verify-element-not-exist)    | Verify if a mobile element is NOT present.  | 
| [Verify Element Visible](/katalon-studio/keywords/keyword-description-in-katalon-studio/mobile-keywords/mobile-verify-element-visible)   | Verify if a mobile element is visible  | 
| [Verify Element Not Visible](/katalon-studio/keywords/keyword-description-in-katalon-studio/mobile-keywords/mobile-verify-element-not-visible)  | Verify if a mobile element is not visible.  | 
| [Verify Element Checked](/katalon-studio/keywords/keyword-description-in-katalon-studio/mobile-keywords/mobile-verify-element-checked)   | Verify if a mobile element is checked. Applicable to: <ul><li>Checkbox</li><li>Radio button</li></ul>  | 
| [Verify Element Not Checked](/katalon-studio/keywords/keyword-description-in-katalon-studio/mobile-keywords/mobile-verify-element-not-checked)    | Verify if a mobile element is not checked. Applicable to: <ul><li>Checkbox</li><li>Radio button</li></ul>  | 
| [Verify Element Text](/katalon-studio/keywords/keyword-description-in-katalon-studio/mobile-keywords/mobile-verify-element-text)   | Verify the text of an element. After adding this keyword, you need to get text and parse it in the **Input**.   | 
| [Wait for Element Present](/katalon-studio/keywords/keyword-description-in-katalon-studio/mobile-keywords/mobile-wait-for-element-present)   | Wait for the given mobile element to present within the given time (in seconds).  | 
| [Wait for Element Not Present](/katalon-studio/keywords/keyword-description-in-katalon-studio/mobile-keywords/mobile-wait-for-element-not-present)   | Wait for the given element to NOT be present within the given time (in seconds).  | 

## Use Mobile Recorder with Custom Desired Capabilities for Remote Appium Devices

Starting Version 10.2.0 and later, Katalon Studio now supports the use of custom desired capabilities with remote Appium type when using the Record Mobile and Spy Mobile features. This enhancement is especially useful when working with multiple remote device types.

Previously, users had to manually add custom desired capabilities under the **Remote** option each time, which added unnecessary setup time. With this enhancement, users can define their desired configurations under **Project > Settings > Desired Capabilities**, and simply select the appropriate device setup when initiating a recording or spying session. This eliminates the need to reconfigure the **Remote** settings each time, streamlining the workflow and saving time in mobile automation projects.

### Requirements

- You have added your custom mobile desired capabilities with remote Appium type in **Project > Settings > Desired Capabilities > Custom**. See [Add custom capabilities for mobile testing in Katalon Studio](/katalon-studio/manage-projects/project-settings/desired-capabilities/set-custom-desired-capabilities-in-katalon-studio).

    ![Select custom desired capabilities with remote Appium type](https://tw-cdn.katalon.com/katalon-studio/record-and-spy/mobile-record-and-spy-utilities/KS_add_custom_mobile_desired_capabilities.png)

### Record mobile objects using custom desired capabilities

To begin mobile objects using custom capabilities, follow these steps:

1. From the main Toolbar, click the **Record Mobile** icon and select **Custom Capabilities**.

    <img src="https://tw-cdn.katalon.com/katalon-studio/record-and-spy/mobile-record-and-spy-utilities/KS_select_mobile_custom_desired_capabilities.png" alt="Select Custom Mobile Capability" width="400"/>

2. Select the custom desired capability.

    :::note
    The new Custom option in the **Record**/**Spy** menu displays custom desired capabilities that are relevant to **mobile devices only**. Since desired capabilities are defined as key-value string pairs, Katalon Studio determines their relevance based on mobile-specific keys such as `automationName` and `platformName`. If these keys are not present in a desired capability object, it will not appear in the Custom menu — even if it is intended for a mobile device.
    :::

## Configure object tree display

You can configure the display of the object tree in **Project Settings > Test Design > Mobile**.

<img className="image" width={650} src={useBaseUrl("/dff1cfb0-a54f-11ee-b8c3-0242c7a41fd4/ks-920-object-tree-display.png")} />

<table xmlns="http://www.w3.org/1999/xhtml" className="table anchor_top_offset" id="concept-2427__83b2f148-0edf-4884-a647-379a794e6fa5"><caption /><colgroup><col style={{width: '33.33333333333333%'}} /><col style={{width: '66.66666666666666%'}} /></colgroup><thead className="thead"><tr className><th className="entry anchor_top_offset" id="concept-2427__83b2f148-0edf-4884-a647-379a794e6fa5__entry__1">Option</th><th className="entry anchor_top_offset" id="concept-2427__83b2f148-0edf-4884-a647-379a794e6fa5__entry__2">Description</th></tr></thead><tbody className="tbody"><tr className><td className="entry" headers="concept-2427__83b2f148-0edf-4884-a647-379a794e6fa5__entry__1 concept-2427__83b2f148-0edf-4884-a647-379a794e6fa5__entry__2 ">Minimal</td><td className="entry" headers="concept-2427__83b2f148-0edf-4884-a647-379a794e6fa5__entry__1 concept-2427__83b2f148-0edf-4884-a647-379a794e6fa5__entry__2 "><ul className="ul"><li className="li">Default option</li><li className="li">Uses the <code className="ph codeph">Driver.execute("mobile: source")</code> method and displays minimal elements in the object tree</li><li className="li">Better performance, but some elements might be missing</li></ul></td></tr><tr className><td className="entry" headers="concept-2427__83b2f148-0edf-4884-a647-379a794e6fa5__entry__1 concept-2427__83b2f148-0edf-4884-a647-379a794e6fa5__entry__2 ">Full</td><td className="entry" headers="concept-2427__83b2f148-0edf-4884-a647-379a794e6fa5__entry__1 concept-2427__83b2f148-0edf-4884-a647-379a794e6fa5__entry__2 "><ul className="ul"><li className="li">Uses the <code className="ph codeph">Driver.getPageSource()</code> and displays all elements in the object tree</li><li className="li">Might cause performance issue</li></ul></td></tr></tbody></table> 

## Related content

<div xmlns="http://www.w3.org/1999/xhtml" className="p"><ul className="ul"><li className="li"><a className="xref j-external-link" href="https://docs.katalon.com/katalon-studio/get-started/sample-projects/mobile/mobile-create-and-run-android-test-case" target="_blank">Create and run Android test case</a></li><li className="li"><a className="xref j-external-link" href="https://docs.katalon.com/katalon-studio/get-started/sample-projects/mobile/mobile-create-and-run-ios-test-case-in-katalon-studio" target="_blank">Create and run iOS test case</a></li><li className="li"><a className="xref j-external-link" href="https://docs.katalon.com/katalon-studio/manage-projects/set-up-projects/mobile-testing/mobile-image-based-testing-in-katalon-studio" target="_blank">Image-based testing in Katalon Studio</a></li></ul></div>
