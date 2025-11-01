---
title: Camera image injection
---

This document provides details about the camera image injection feature of Katalon TestCloud.

:::caution Prerequisites
- You have installed the Katalon TestCloud Keywords plugin. If you have not, visit Katalon Store: [Katalon TestCloud keywords](https://store.katalon.com/product/397/Katalon-TestCloud-Keywords).
- This keyword is applicable for mobile native app testing.
:::

The Camera image injection function supports the following systems and interfaces:
  - iOS: 13 or higher.
    - The `didFinishPickingMediaWithInfo` class of `UIImagePickerController` iOS SDK class for capturing an image. See: [Apple documentation](https://developer.apple.com/documentation/uikit/uiimagepickercontrollerdelegate/1619126-imagepickercontroller).
    - The `AVCapturePhoto` iOS SDK class for receiving captured photos from `AVCapturePhotoOutput` class. See: [Apple Documentation](https://developer.apple.com/documentation/avfoundation/avcapturephoto).
  - Android: 9 or higher.
    - The `CameraX` API: [CameraX](https://developer.android.com/media/camera/camerax).
    - The `Camera` API: [Camera](https://developer.android.com/media/camera/camera-deprecated).
    - The `Camera2` API: [Camera2](https://developer.android.com/media/camera/camera2).
    - The `ACTION_IMAGE_CAPTURE` Intent action: [ACTION_IMAGE_CAPTURE](https://developer.android.com/reference/android/provider/MediaStore#ACTION_IMAGE_CAPTURE).

One limitation of testing with cloud-based mobile devices is the ability to capture images. Camera image injection tackles this issue by simulating the action of taking images through a mobile application.

Some common use cases of camera image injection are:
- Scanning a check for a banking application.
- Scanning a QR code.
- Taking a user profile picture.
- Taking a photo and store in a gallery app.

:::note
- Video capture and other media types are currently not supported.
- For iOS apps signed with Enterprise Certificates, app resigning (a prerequisite for using the Image Injection tool) is not available.
:::

To perform image injection, you need to specify the desired capability and prepare the images. Follow these steps:

1. In Katalon Studio, click the **Profile** drop-down and select **Reload Plugins** to check that the plugin is installed.
   <img width="600" src="/3a871180-56d3-4a86-aa06-9441c30937e4/KS_TestCloud_plugin.png" alt="Select Reload Plugin"/>
2. Go to **Project Settings** > **Desired Capabilities** > **TestCloud**.
3. In the TestCloud table, add a `katalon:options` property, set **Type** as `Dictionary`, then click the `...`.
   <img width="600" src="/3d76cb0e-d7e8-4c16-8323-869daa78a0ac/KS_TestCloud_desired_caps_menu.png" alt="Add a Katalon options property"/>
4. In the **Dictionary Property Builder** dialog, add the boolean property `enableImageInjection=true`. Then click **OK**.
   <img width="600" src="/606bcc95-d6b9-4fa7-a1b6-cad72add2cc1/KS_TestCloud_camera_injection.png" alt="Add the Boolean property enableImageInjection=true"/>
5. Save the images that are required for image injection in the **Data Files/TestCloud** folder of your project.
   The images must be in PNG, JPG, or JPEG formats, and does not exceed 4.5 MB.
   <img width="350" src="/18145fd0-88e9-11ee-b53b-0242c7a41fd4/KS_datafile_testcloud_folder.png" alt="Save images in Data Files/TestCloud"/> <br/>
6. Add the `CameraImageInjectionExecutor.injectImage` keyword to your test case.
   <img width="600" src="/417c9667-990d-4ce2-956c-7f873aebee6f/add-testcloud-custom-keyword.png" alt="Add the CameraImageInjectionExecutor.injectImage keyword"/> 
7. Configure your TestCloud environment and run the test.

