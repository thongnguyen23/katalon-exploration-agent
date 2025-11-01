---
hide_title: true
title: Spy mobile utility
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# Spy mobile utility

The Mobile Object Spy utility allows you to capture available test objects of a mobile application. These captured objects are then applied directly in your mobile automation tests. Besides capturing, you can also modify the object properties directly with the utility, which helps save time and effort in managing test objects.

See the following table to learn about the device types you can use with Mobile Object Spy:

<table xmlns="http://www.w3.org/1999/xhtml" className="table anchor_top_offset" id="concept-6120__57e6693e-fa3d-45c1-a2d2-940a92bfffa2"><caption /><colgroup><col style={{width: '30%'}} /><col style={{width: '70%'}} /></colgroup><thead className="thead"><tr className><th className="entry anchor_top_offset" id="concept-6120__57e6693e-fa3d-45c1-a2d2-940a92bfffa2__entry__1">Device type</th><th className="entry anchor_top_offset" id="concept-6120__57e6693e-fa3d-45c1-a2d2-940a92bfffa2__entry__2">Description</th></tr></thead><tbody className="tbody"><tr className><td className="entry" headers="concept-6120__57e6693e-fa3d-45c1-a2d2-940a92bfffa2__entry__1 concept-6120__57e6693e-fa3d-45c1-a2d2-940a92bfffa2__entry__2 ">Local devices</td><td className="entry" headers="concept-6120__57e6693e-fa3d-45c1-a2d2-940a92bfffa2__entry__1 concept-6120__57e6693e-fa3d-45c1-a2d2-940a92bfffa2__entry__2 "><div className="p">With local devices, you need to set up the development environment before testing.<ul className="ul"><li className="li"><a className="xref" href="/katalon-studio/manage-projects/set-up-projects/mobile-testing/android/mobile-configure-android-emulator">Android Emulator</a></li><li className="li"><a className="xref" href="/katalon-studio/manage-projects/set-up-projects/mobile-testing/android/mobile-set-up-android-real-devices">Android real device</a></li></ul><ul className="ul"><li className="li"><a className="xref" href="/katalon-studio/manage-projects/set-up-projects/mobile-testing/ios/mobile-ios-setup-simulators-in-katalon-studio">iOS Simulator</a></li><li className="li"><a className="xref" href="/katalon-studio/manage-projects/set-up-projects/mobile-testing/ios/mobile-set-up-ios-real-devices">iOS real device</a></li></ul></div></td></tr><tr className><td className="entry" headers="concept-6120__57e6693e-fa3d-45c1-a2d2-940a92bfffa2__entry__1 concept-6120__57e6693e-fa3d-45c1-a2d2-940a92bfffa2__entry__2 ">Remote devices</td><td className="entry" headers="concept-6120__57e6693e-fa3d-45c1-a2d2-940a92bfffa2__entry__1 concept-6120__57e6693e-fa3d-45c1-a2d2-940a92bfffa2__entry__2 "><ul className="ul"><li className="li">Test mobile apps with your existing <a className="xref" href="/katalon-studio/manage-projects/set-up-projects/mobile-testing/mobile-app-testing-with-remote-devices">custom devices</a></li><li className="li">Install Kobiton plugin and access your <a className="xref" href="/katalon-studio/integrations/test-execution/kobiton-integration-with-katalon-studio">Kobiton devices</a></li></ul></td></tr><tr className><td className="entry" headers="concept-6120__57e6693e-fa3d-45c1-a2d2-940a92bfffa2__entry__1 concept-6120__57e6693e-fa3d-45c1-a2d2-940a92bfffa2__entry__2 ">TestCloud devices (available from 9.5.0+)</td><td className="entry" headers="concept-6120__57e6693e-fa3d-45c1-a2d2-940a92bfffa2__entry__1 concept-6120__57e6693e-fa3d-45c1-a2d2-940a92bfffa2__entry__2 ">You can test with Android and iOS mobile devices with no further setups. A TestCloud Mobile Native App Testing subscription is required. For more details, see <a className="xref" href="/katalon-testcloud/testcloud-overview">TestCloud overview</a>.</td></tr></tbody></table> 

## Capture objects with Mobile Object Spy

### Requirements

- You have configured the environment for mobile testing. For instance, see [[Mobile] Configure Android Emulator](/katalon-studio/manage-projects/set-up-projects/mobile-testing/android/mobile-configure-android-emulator).

### Capture Mobile objects of an application

Follow the steps on how to capture Mobile objects of an application using Spy Mobile Utility:

1. From the main Toolbar, click the **Spy Mobile** icon and select your device type, for instance, **Android Devices**.

    <img className="image" width={300} src={useBaseUrl("/e54e077d-c7f9-4d48-b790-73ddc4e26089/ks-950-mobile-spy.png")} />

2. In the displayed **Mobile Object Spy** dialog, specify the following information at the **Configurations** section:

    <img className="image" width={400} src={useBaseUrl("/a3e37ce0-c151-11ed-a4d3-0242cfbc79b5/ks-spy-config.png")} />

    - **Device Name**: A mobile device where Katalon Studio launches the application. All of your connected devices should be displayed in this list
    - **Start with**: In the drop-down list, you can select either Application File or Application ID
        - **Application File**: Browse your tested application (`.apk` file for Android, `.ipa` for iOS)
        - **Application ID**: Specify the application ID of your tested application, which is either the package name of an Android app or the bundle identifier of an iOS app

3. Click **Start** to begin spying the application under test (AUT). Wait until the AUT is launched, you can see the application display in **Device View** and the objects in **All Objects**.

    - **Device View** is a simulator of the device's screen.

    - **All Objects** captures and organizes all the displayed mobile objects of **Device View** in a tree.

    <img className="image" width={400} src={useBaseUrl("/a3e37ce0-c151-11ed-a4d3-0242cfbc79b5/ks-spy-config.png")} />

4. When you click any object either in **All Objects** or in **Device View**, Katalon Studio highlights their counterpart for verification.

    To make sure the **Device View** displays the current screen of the AUT on the device, you can click the **Capture Object** button to reload **Device View** and refresh **All Objects**.

5. Tick on any object checkbox in **All Objects**.
    
    Katalon Studio captures the selected objects and displays objects' properties in the **Object Properties** table.

    <img className="image" width={700} src={useBaseUrl("/a3ad8228-3d70-464f-b681-bcb7dc533597/ks-950-mobile-object-spy-dialog.png")} alt="Mobile Object Spy dialog" />

    The most important property of an object is its locator strategy and value. The default locator is a unique value in detecting that object. If you prefer another locator strategy, choose among the provided options and generate a new locator. Then click **Highlight** to confirm your newly updated locator can detect the target object on its screen correctly.

    <img className="image" width={400} src={useBaseUrl("/963a4cb6-6dbd-4f90-bbde-e6d854aa1948/ks-950-mobile-spy-locator-strategies.png")} />

6. Click **Add to Object Repository** to save the object you want to use in your tests.

    <img className="image" width={300} src={useBaseUrl("/a3f3d090-c151-11ed-a4d3-0242cfbc79b5/ks-spy-add-object.png")} />

7. In the displayed **Add Element to Object Repository** dialog, select where you want to save the objects, then click **OK**.

    <img className="image" width={500} src={useBaseUrl("/33e0b090-8dbe-11ee-ab4f-0242c7a41fd4/KS_mobile_android_add_element_to_object_repository.png")} alt="Add Element to Object Repository dialog" />

    You can select one of these options to save:

    - **Merge changes into existing objects**: Add unique changes of the newly recorded object to the existing object, but still keep the existing object ID.
    - **Create duplicate objects**: Save the newly recorded object separately from the existing object.
    - **Replace existing objects**: The newly recorded object overrides the ID and attributes of the existing object.

    The captured objects will be added to **Object Repository** accordingly.

8. You can continue with the current mobile screen or navigate to other interfaces as needed.

## Use Mobile Object Spy with Custom Desired Capabilities for Remote Appium Devices

Starting Version 10.2.0 and later, Katalon Studio now supports the use of custom desired capabilities with remote Appium type when using the Mobile Object Spy feature. This enhancement is especially useful when working with multiple remote device types.

### Requirements

- You have added your custom mobile desired capabilities with remote Appium type in **Project > Settings > Desired Capabilities > Custom**. See [Add custom capabilities for mobile testing in Katalon Studio](/katalon-studio/manage-projects/project-settings/desired-capabilities/set-custom-desired-capabilities-in-katalon-studio).

    ![Select custom desired capabilities with remote Appium type](https://tw-cdn.katalon.com/katalon-studio/record-and-spy/mobile-record-and-spy-utilities/KS_add_custom_mobile_desired_capabilities.png)

### Capture Objects using custom capabilities

1. From the main Toolbar, click the **Mobile Object Spy** icon and select **Custom Capabilities**.

    ![Select Custom Mobile Capability](https://tw-cdn.katalon.com/katalon-studio/record-and-spy/mobile-record-and-spy-utilities/KS_select_mobile_custom_desired_capabilities_object_spy.png)

2. Select the custom capability.

3. Click **Start** to launch the AUT and spy using the selected capabilities.

4. Select, review, and save the mobile objects you have captured to your **Object Repository**.

## Use Mobile Object Spy on TestCloud devices

TestCloud provides a wide range of mobile devices, supporting both Android and iOS, that are accessible from Katalon Studio. You just need to upload your application file to TestOps and directly capture the application objects.

### Requirements

- Katalon Studio Enterprise (KSE) version 9.5.0 onwards.
- A TestCloud Mobile Native App Testing subscription. You can check which type of TestCloud environment you can access in Platform integration settings.
- You have enabled TestCloud integration in **Project Settings**. See [Integrate Katalon TestCloud with Katalon Studio](/katalon-studio/get-started/workspace-settings/integrate-katalon-platform-with-katalon-studio).

### Upload a mobile app to TestOps

TestCloud allows you to perform automated tests on mobile native applications. You can upload a mobile application and local Katalon Studio tests to TestOps, then use TestCloud to orchestrate test executions without having to set up local emulators or simulators.

#### Requirements

- An active Katalon TestCloud subscription or trial.
- A mobile application file in `.apk` or `.aab` format (for Android), or in `.ipa` format (for iOS).
- A mobile test project configured in TestOps.
    - To set up a sample project for iOS application testing, see [Open the sample iOS test project](/katalon-studio/get-started/sample-projects/mobile/sample-ios-mobile-project-in-katalon-studio).
    - To set up a sample project for Android application testing, see [Open the sample Android test project](/katalon-studio/get-started/sample-projects/mobile/sample-android-mobile-project-in-katalon-studio).
- For Android hybrid mobile applications, follow the configurations in this document: [Capture elements in hybrid Android apps](/katalon-studio/record-and-spy/mobile-record-and-spy-utilities/hybrid-mobile-apps-testing/native-render-only-webview-render-capture-elements-in-hybrid-android-apps-in-katalon-studio).

Follow these steps to upload a mobile application to TestOps:

1. Sign in to [Katalon TestOps](https://testops.katalon.io/) and go to your project.

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

### Spy objects with a TestCloud device

You can capture objects on a TestCloud device. Follow these steps:

1. From the main toolbar, click the **Spy Mobile** icon and select **TestCloud devices**.

    <img className="image" src={useBaseUrl("/ea9f2d4c-86a1-41bd-a1ab-4d983e7a90ad/ks-950-mobile-spy-select-testcloud.png")} />

2. In the **TestCloud Configurations** section, do as follows:

    <img className="image" src={useBaseUrl("/71c90365-7b4f-44dd-b261-6be4c13900fa/ks-972-testcloud-configurations.png")} />

    1. **Device Name**: Select the mobile operating system (OS), the version of the OS, and Studio will list out the available devices accordingly.
        
    You can also select **Any Phone** or **Any Tablet** from the top of the list to let TestCloud automatically choose a suitable device that meets your requirements.

    2. **Show only high availability devices**: This option, enabled by default, filters the list to show devices with high availability status. You can then choose a device for testing without delays.
        - **When enabled**: Only devices with high availability status are shown.
        - **When disabled**: All devices are shown.

    3. **Application**: Select the application file you want to test from your TestOps uploads.

3. Click **Start** to launch the AUT.

4. Follow from **Step 3** of [Capture objects with Mobile Object Spy](#capture-objects-with-mobile-object-spy) to capture objects.

## Known limitations

- **Appium known limitation**: You may get incorrect object highlighting when rotating the device to landscape view. For workaround, after rotating, you need to click on the **Capture Object** button to refresh the **All Objects** tree, then the highlighting will work normally.

    <img className="image" width={400} src={useBaseUrl("/aab9bdb0-c14f-11ed-a4d3-0242cfbc79b5/ks-capture-object-button.png")} />

- **Mobile Object Spy** does not support capturing Android EditText message.
- Depending on the TestCloud devices, the default timeout is in the range of 60-120 seconds.
