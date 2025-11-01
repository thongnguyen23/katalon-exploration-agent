---
hide_title: true
title: '[Mobile] Image-based testing in Katalon Studio'
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# Image-based testing for Mobile  

Katalon Studio provides an image locator method that allows you to associate test objects with images. This method enables image-based testing, which is useful when the elements of the mobile application under test (AUT) retain their visual appearance but their underlying structure has changed.

Image-based testing for Mobile in Katalon Studio is built on Appium’s image element detection feature. Katalon Studio automatically encodes your reference images to Base64 and uses them during test execution to find matching areas on the screen. The accuracy of image-based testing depends heavily on capturing high-quality reference images.

This guide shows you how to configure image-based object recognition for mobile testing, capture reference screenshots, and reduce the chance of failures when using image locators in Katalon Studio.

 ## Requirements

- An active **Katalon Studio Enterprise** license.
- **Appium 2** must be installed and properly configured on your machine. Install Appium 2. If you haven't installed Appium 2, follow the guide at [Appium 2 Quickstart Guide](https://appium.io/docs/en/2.0/quickstart/install/).
- If you previously installed Appium 1, older setup instructions, including those for custom acceptance thresholds, no longer apply. To switch to Appium 2, follow this guide: [Uninstall and Reinstall Appium](/katalon-studio/troubleshooting/troubleshoot-mobile-automated-testing/how-to-uninstall-and-re-install-appium).
- You no longer need to install `opencv4nodejs`, CMake, or Windows Build Tools. The new image plugin architecture introduced in Appium 2 simplifies setup and removes the need for native OpenCV bindings.

## Setup: Install Appium Image Plugin
To install the Image Plugin, run the following command in your terminal:

    ```jsx
    appium plugin install images
    ```
You have successfully installed the **Appium Image Plugin**. After running the installation command, you should see the following confirmation message in your terminal:

<img src= "https://tw-cdn.katalon.com/katalon-studio/maintain-tests/Success_Image_Plugin_install.png" alt="You have successfully installed the Appium Image Plugin" width="500" />

## Capture Images

:::note
Image-based locators are not auto-captured. You must initiate the screenshot manually using the **Add Screenshot** button.
:::

Follow the steps on how to capture an image of the desired Mobile elements for interaction during test recording. You can use either the Mobile Recorder or Mobile Spy to complete this process:

1. Start the Mobile Recorder. Launch the recorder as you normally would.

2. Select the element. In the device view, choose the element you want to capture.

3. Capture the object. Right-click on the element and select **Capture Object**. 

    <img src= "https://tw-cdn.katalon.com/katalon-studio/maintain-tests/Capture_mobile_object_with_image_plugin.png" alt="Right-click on the element and select Capture Object" width="400" />
    
    The element will appear under the **Captured Objects** section.

4. Highlight to verify. Click **Highlight** to verify the captured element. Katalon Studio will search for the element on the device.

    :::note
    Currently, if Katalon Studio finds more than one match for the captured image, the **Add Screenshot** button will be disabled.
    :::

    <img src= "https://tw-cdn.katalon.com/katalon-studio/maintain-tests/Highlight_mobile_object_to_verify.png" alt="Right-click on the element and select Capture Object" width="400" />

5. Add screenshot. Click **Add Screenshot** to attach the image to the object. A confirmation message (`Screenshot taken!`) will appear once the image is successfully saved to the object’s Image property.

    <img src= "https://tw-cdn.katalon.com/katalon-studio/maintain-tests/Add_screenshot_of_mobile_object.png" alt="Right-click on the element and select Capture Object" width="400" />

You have successfully captured a screenshot of your mobile object. The image locator is now added to your mobile test object.

<img src= "https://tw-cdn.katalon.com/katalon-studio/manage-projects/set-up-projects/mobile-testing/Captured_image_locator.png" alt="The image locator is now added to your mobile test object" width="600" />