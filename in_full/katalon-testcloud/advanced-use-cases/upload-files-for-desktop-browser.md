---
title: Upload files for desktop browser
---

To upload files to a TestCloud machine, you can use the `FileExecutor.uploadFileToWeb` keyword.

:::caution Requirements
- You have installed the Katalon TestCloud Keywords plugin from Katalon Store. If you have not, visit: [Katalon TestCloud Keywords](https://store.katalon.com/product/397/Katalon-TestCloud-Keywords).
:::

1. In Katalon Studio, click the **Profile** drop-down and select **Reload Plugins** to make sure the plugin is installed.
2. Add the `FileExecutor.uploadFileToWeb` keyword to your test case.
   1. In **Manual view**: Click **(+) Add Custom Keyword** and select `com.katalon.testcloud.FileExecutor.uploadFileToWeb`. Then select the test object and input the file path. 
   <br/><img width="700" alt="Add network throttling keyword to test case" src="https://tw-cdn.katalon.com/katalon-testcloud/advanced-use-cases/upload-file-to-web.gif" />
   <br/>

   2. In **Script view**, the keyword is added as follows:
   ```jsx
   CustomKeywords.'com.katalon.testcloud.FileExecutor.pushFiletoDevice'(findTestObject('Web App/Page_The Internet/a_File Upload'), 'Users/katalondemo/Documents/test.csv') 
   ```

**Example code**
```jsx
import static com.kms.katalon.core.testobject.ObjectRepository.findTestObject
import com.kms.katalon.core.webui.keyword.WebUiBuiltInKeywords as WebUI

'Go to the page'
WebUI.navigateToUrl('https://the-internet.herokuapp.com/')

'Navigate to the Upload file page'
WebUI.click(findTestObject('Object Repository/Web App/Page_The Internet/a_File Upload'))

'Upload the file'
String filePath = 'Users/katalondemo/Documents/puppy.png'
CustomKeywords.'com.katalon.testcloud.FileExecutor.uploadFileToWeb'(findTestObject('Object Repository/Web App/Page_The Internet/input_Upload file'), filePath)

'Click submit button'
WebUI.click(findTestObject('Object Repository/Web App/Page_The Internet/input_File Uploader_file-submit'))

'Verify the file is uploaded successfully'
WebUI.verifyElementPresent(findTestObject('Object Repository/Web App/Page_The Internet/h3_File Uploaded'), 3)
```

3. Configure your TestCloud mobile environment and run the test.