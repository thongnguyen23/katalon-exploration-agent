---
hide_title: true
title: How to Handle File Uploads in Katalon Studio
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="id" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>How to Handle File Uploads in <span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon Studio</span> 

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Uploading a file is a common action for interacting with a web   app. You can handle the file upload action and verify the   downloaded files using Katalon Studio.</p> 

## <a id="id_1" class="anchor_top_offset"/>What is File Upload in testing?

<p xmlns="http://www.w3.org/1999/xhtml" className="p">The file upload widget is the input tag having the   <strong className="ph b">type</strong> attribute that is equal to   <strong className="ph b">file</strong>. It allows us to upload all file formats   (.jpg, .png, .txt…)</p> 
    
## <a id="id_2" class="anchor_top_offset"/>To upload a file you can use

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"> <a className="xref" href="/katalon-studio/keywords/keyword-description-in-katalon-studio/web-ui-keywords/webui-upload-file">[WebUI] Upload File</a>   </li><li className="li"> <a className="xref" href="/katalon-studio/keywords/keyword-description-in-katalon-studio/web-ui-keywords/webui-upload-file-by-drag-and-drop">[WebUI] Upload File by Drag-and-Drop</a>   </li></ul> 

## <a id="concept-7095" class="anchor_top_offset"/>Deprecated content

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Let's work on the case in which we need to upload a file and validate whether the file is uploaded.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><strong className="ph b">Steps</strong>:</p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">Launch the URL of the application</li><li className="li">Maximize the window</li><li className="li">Use the file upload widget to upload a file</li></ul> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Manual Mode</strong>:</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" width={750} src={useBaseUrl("/98899570-22b2-11ed-9930-0242fe3e4a3f/ks-840-file-upload.png")} alt="file upload" /></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">We can also use the script mode. Below script is the code to upload a file and validate the uploaded file.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><strong className="ph b">Script Mode:</strong></p> 

```jsx
'Open browser and navigate to given URL'
WebUI.openBrowser('C:\\Users\\User\\Desktop\\Katalon Articles\\File Upload\\UploadFile.html')

'Maximize the window'
WebUI.maximizeWindow()

'Passing the path of the file'
WebUI.uploadFile(findTestObject('Upload File'), 'C:\\Users\\Public\\Pictures\\Sample Pictures\\Desert.jpg')
 
'Capturing the file name after upload and storing it in a variable'
FilePath = WebUI.getAttribute(findTestObject('Upload File'), 'value')
 
'Verifying the Actual path and Expected path of file'
WebUI.verifyMatch(FilePath, 'C:\fakepath\Desert.jpg', false)
```

### <a id="concept-9572" class="anchor_top_offset"/>File upload using Send Keys

<p xmlns="http://www.w3.org/1999/xhtml" className="p">We can also upload files by using the <strong className="ph b">Send Keys</strong> method. <strong className="ph b">Send Keys</strong> works for the <strong className="ph b">input</strong> tag having <strong className="ph b">type</strong> equal to <strong className="ph b">file</strong>.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Steps:</p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">Launch the URL of the application</li><li className="li">Maximize the window</li><li className="li">Use the Send Keys method to upload a file.</li><li className="li">Send Keys accepts file URL as string.</li></ul> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><strong className="ph b">Manual Mode:</strong></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" width={750} src={useBaseUrl("/988835e0-22b2-11ed-9930-0242fe3e4a3f/ks-840-send-key.png")} alt="send key" /></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><strong className="ph b">Script Mode:</strong></p> 

```jsx
'Open browser and navigate to given URL'
 
WebUI.openBrowser('C:\\Users\\User\\Desktop\\Katalon Articles\\File Upload\\UploadFile.html')
 
'Maximize the window'
WebUI.maximizeWindow()
 
'Uploading the File using Send Keys method by passing the File path'
WebUI.sendKeys(findTestObject('Upload File'), 'C:\\Users\\Public\\Pictures\\Sample Pictures\\Desert.jpg')
 
'Capturing the file name after upload and storing it in a variable'
FilePath = WebUI.getAttribute(findTestObject('Upload File'), 'value')
 
'Verifying the Actual path and Expected path of file'
WebUI.verifyMatch(FilePath, 'C:\fakepath\Desert.jpg', false)
```

### <a id="concept-4815" class="anchor_top_offset"/>Verify a downloaded file

<p xmlns="http://www.w3.org/1999/xhtml" className="p">After downloading a file from the application, we need to verify whether the file is successfully downloaded and saved in a folder.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">For that, we need to set preferences for Firefox, as shown in the image below.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/handle_file_uploads/Verify-a-Downloaded-File.png")} alt="Verify a Downloaded file" /><br /><br /></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><strong className="ph b">Script Mode:</strong></p> 

```jsx
import org.openqa.selenium.By as By
import org.openqa.selenium.WebDriver as WebDriver
import org.testng.Assert as Assert
import com.kms.katalon.core.webui.driver.DriverFactory as DriverFactory
import com.kms.katalon.core.webui.keyword.WebUiBuiltInKeywords as WebUI
import internal.GlobalVariable as GlobalVariable
 
'Define Custom Path where file needs to be downloaded'
String downloadPath = 'D:\FileDownloadChecking'
 
'Launch a browser and Navigate to URL'
WebUI.openBrowser(GlobalVariable.FileDownloadCheckingURL)
 
WebDriver driver = DriverFactory.getWebDriver()
 
'Clicking on a Link text to download a file'
driver.findElement(By.linkText('smilechart.xls')).click()
'Wait for Some time so that file gets downloaded and Stored in user defined path'
WebUI.delay(10)
 
'Verifying the file is download in the User defined Path'
Assert.assertTrue(isFileDownloaded(downloadPath, 'smilechart.xls'), 'Failed to download Expected document')
 
boolean isFileDownloaded(String downloadPath, String fileName) {
    long timeout = 5 * 60 * 1000
    long start = new Date().getTime()
    boolean downloaded = false
    File file = new File(downloadPath, fileName)
    while (!downloaded) {
        KeywordUtil.logInfo("Checking file exists ${file.absolutePath}")
        downloaded = file.exists()
        if (downloaded) {
            file.delete() // remove this line if you want to keep the file
        } else {
            long now = new Date().getTime()
            if (now - start > timeout) {
                break
            }
            Thread.sleep(3000)
        }
    }
    return downloaded
}
```
<p xmlns="http://www.w3.org/1999/xhtml" className="p">We have just learned how to handle file uploads and verify downloaded files using Katalon Studio. You can download the source code from our GitHub repository: <a className="xref j-external-link" href="https://github.com/katalon-studio/katalon-web-automation" target="_blank">Katalon web automation sample project</a>.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">For further instructions, you can refer to this guideline: <a className="xref" href="/katalon-studio/keywords/keyword-description-in-katalon-studio/web-ui-keywords/webui-upload-file">[WebUI] Upload File</a>.</p> 
