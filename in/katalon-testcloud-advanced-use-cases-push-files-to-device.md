---
title: Push files to device
---

To upload files to a TestCloud device, you can use the `pushFiletoDevice` keyword.

- This keyword is applicable for Android devices only.
- You have installed the Katalon TestCloud Keywords plugin from Katalon Store. If you have not, visit: [Katalon TestCloud Keywords](https://store.katalon.com/product/397/Katalon-TestCloud-Keywords).

On Android, you can push files to these folders:

- `/sdcard/Download/`
- `/sdcard/Pictures`
- `/sdcard/Android/data/<app_package>`

Follow these steps:

1. In Katalon Studio, click the **Profile** drop-down and select **Reload Plugins** to make sure the plugin is installed.
   <img width="600" alt="Reload plugins" src="https://docs.katalon.com/3a871180-56d3-4a86-aa06-9441c30937e4/KS_TestCloud_plugin.png" />

2. Add the `FileExecutor.pushFiletoDevice` keyword to your test case.
   1. In **Manual view**: Click **(+) Add Custom Keyword** and select `com.katalon.testcloud.FileExecutor.pushFiletoDevice`. In the **Input** field, provide the values for `destinationPath` and `localFilePath`. 
   <br/><img width="700" alt="Add network throttling keyword to test case" src="https://tw-cdn.katalon.com/katalon-testcloud/advanced-use-cases/push-files-to-device.gif" />
   <br/>

   2. In **Script view**, the keyword is added as follows:
   ```jsx
   CustomKeywords.'com.katalon.testcloud.FileExecutor.pushFiletoDevice'("/sdcard/Pictures/puppy.png", "/Users/demouser/Pictures/puppy.png") 
   ```

**Example code**
```jsx
import static com.kms.katalon.core.testobject.ObjectRepository.findTestObject

import com.kms.katalon.core.configuration.RunConfiguration
import com.kms.katalon.core.mobile.keyword.MobileBuiltInKeywords as Mobile
import com.kms.katalon.core.model.FailureHandling

'Push file to the device'
String localPath = '/Users/demouser/Pictures/puppy.png'
CustomKeywords.'com.katalon.testcloud.FileExecutor.pushFileToDevice'('/sdcard/Pictures/puppy.png', localPath)

'Login to the app'
Mobile.setText(findTestObject('Object Repository/Native App/MyDemoApp/android.widget.EditText - Username'), 'mydemouser', 0)
Mobile.setEncryptedText(findTestObject('Object Repository/Native App/MyDemoApp/android.widget.EditText - Password'), 'tTkSizDjdvtHYxURT8SvuQ==', 0)
Mobile.hideKeyboard(FailureHandling.OPTIONAL)
Mobile.tap(findTestObject('Object Repository/Native App/MyDemoApp/android.widget.Button - Login'), 0)

'Open the Gallery'
Mobile.tap(findTestObject('Object Repository/Native App/MyDemoApp/android.widget.Button - Camera'), 0)
Mobile.tap(findTestObject('Object Repository/Native App/MyDemoApp/android.widget.Button - Open Gallery'), 0)

'Take screenshot to verify the file is pushed to the device'
Mobile.takeScreenshot(FailureHandling.CONTINUE_ON_FAILURE)
```

3. Configure your TestCloud mobile environment and run the test.