---
hide_title: true
title: '[WebUI] Upload File by Drag-and-Drop'
---

# <a id="id_0" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>[WebUI] Upload File by Drag-and-Drop


## <a id="id_0__id" class="anchor_top_offset"/>Description

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Upload files to a website by drag-and-drop.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Keyword name: <code className="ph codeph">uploadFileWithDragAndDrop</code></p> 
<div xmlns="http://www.w3.org/1999/xhtml" className="note note note_note"><span className="note__title">Note:</span> <p className="p">Your Katalon Studio version must be <strong className="ph b">7.5.0+</strong>.</p></div>
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Precondition</strong>: For the keyword to work, the drop zone must be visible before it is used.</p> 

## <a id="id_0__id_1" class="anchor_top_offset"/>Parameters

<table xmlns="http://www.w3.org/1999/xhtml" className="table anchor_top_offset" id="id_0__eb467905-7093-4b13-b826-bbbf866b82cd"><caption /><colgroup><col style={{width: '20%'}} /><col style={{width: '20%'}} /><col style={{width: '20%'}} /><col style={{width: '40%'}} /></colgroup><thead className="thead"><tr className><th className="entry anchor_top_offset" id="id_0__eb467905-7093-4b13-b826-bbbf866b82cd__entry__1">Parameter</th><th className="entry anchor_top_offset" id="id_0__eb467905-7093-4b13-b826-bbbf866b82cd__entry__2">Parameter Type</th><th className="entry anchor_top_offset" id="id_0__eb467905-7093-4b13-b826-bbbf866b82cd__entry__3">Required</th><th className="entry anchor_top_offset" id="id_0__eb467905-7093-4b13-b826-bbbf866b82cd__entry__4">Description</th></tr></thead><tbody className="tbody"><tr className><td className="entry" headers="id_0__eb467905-7093-4b13-b826-bbbf866b82cd__entry__1 id_0__eb467905-7093-4b13-b826-bbbf866b82cd__entry__2 id_0__eb467905-7093-4b13-b826-bbbf866b82cd__entry__3 id_0__eb467905-7093-4b13-b826-bbbf866b82cd__entry__4 ">to</td><td className="entry" headers="id_0__eb467905-7093-4b13-b826-bbbf866b82cd__entry__1 id_0__eb467905-7093-4b13-b826-bbbf866b82cd__entry__2 id_0__eb467905-7093-4b13-b826-bbbf866b82cd__entry__3 id_0__eb467905-7093-4b13-b826-bbbf866b82cd__entry__4 ">TestObject</td><td className="entry" headers="id_0__eb467905-7093-4b13-b826-bbbf866b82cd__entry__1 id_0__eb467905-7093-4b13-b826-bbbf866b82cd__entry__2 id_0__eb467905-7093-4b13-b826-bbbf866b82cd__entry__3 id_0__eb467905-7093-4b13-b826-bbbf866b82cd__entry__4 ">Optional</td><td className="entry" headers="id_0__eb467905-7093-4b13-b826-bbbf866b82cd__entry__1 id_0__eb467905-7093-4b13-b826-bbbf866b82cd__entry__2 id_0__eb467905-7093-4b13-b826-bbbf866b82cd__entry__3 id_0__eb467905-7093-4b13-b826-bbbf866b82cd__entry__4 ">An object representing the drop zone. If unspecified, the drop zone is the website's body element by default.</td></tr><tr className><td className="entry" headers="id_0__eb467905-7093-4b13-b826-bbbf866b82cd__entry__1 id_0__eb467905-7093-4b13-b826-bbbf866b82cd__entry__2 id_0__eb467905-7093-4b13-b826-bbbf866b82cd__entry__3 id_0__eb467905-7093-4b13-b826-bbbf866b82cd__entry__4 ">filePath</td><td className="entry" headers="id_0__eb467905-7093-4b13-b826-bbbf866b82cd__entry__1 id_0__eb467905-7093-4b13-b826-bbbf866b82cd__entry__2 id_0__eb467905-7093-4b13-b826-bbbf866b82cd__entry__3 id_0__eb467905-7093-4b13-b826-bbbf866b82cd__entry__4 ">String</td><td className="entry" headers="id_0__eb467905-7093-4b13-b826-bbbf866b82cd__entry__1 id_0__eb467905-7093-4b13-b826-bbbf866b82cd__entry__2 id_0__eb467905-7093-4b13-b826-bbbf866b82cd__entry__3 id_0__eb467905-7093-4b13-b826-bbbf866b82cd__entry__4 ">Yes</td><td className="entry" headers="id_0__eb467905-7093-4b13-b826-bbbf866b82cd__entry__1 id_0__eb467905-7093-4b13-b826-bbbf866b82cd__entry__2 id_0__eb467905-7093-4b13-b826-bbbf866b82cd__entry__3 id_0__eb467905-7093-4b13-b826-bbbf866b82cd__entry__4 ">The absolute path to the file to be uploaded.</td></tr><tr className><td className="entry" headers="id_0__eb467905-7093-4b13-b826-bbbf866b82cd__entry__1 id_0__eb467905-7093-4b13-b826-bbbf866b82cd__entry__2 id_0__eb467905-7093-4b13-b826-bbbf866b82cd__entry__3 id_0__eb467905-7093-4b13-b826-bbbf866b82cd__entry__4 ">flowControl</td><td className="entry" headers="id_0__eb467905-7093-4b13-b826-bbbf866b82cd__entry__1 id_0__eb467905-7093-4b13-b826-bbbf866b82cd__entry__2 id_0__eb467905-7093-4b13-b826-bbbf866b82cd__entry__3 id_0__eb467905-7093-4b13-b826-bbbf866b82cd__entry__4 ">FailureHandling</td><td className="entry" headers="id_0__eb467905-7093-4b13-b826-bbbf866b82cd__entry__1 id_0__eb467905-7093-4b13-b826-bbbf866b82cd__entry__2 id_0__eb467905-7093-4b13-b826-bbbf866b82cd__entry__3 id_0__eb467905-7093-4b13-b826-bbbf866b82cd__entry__4 ">Optional</td><td className="entry" headers="id_0__eb467905-7093-4b13-b826-bbbf866b82cd__entry__1 id_0__eb467905-7093-4b13-b826-bbbf866b82cd__entry__2 id_0__eb467905-7093-4b13-b826-bbbf866b82cd__entry__3 id_0__eb467905-7093-4b13-b826-bbbf866b82cd__entry__4 ">Specify <a className="xref" href="/katalon-studio/maintain-tests/configure-failure-handling-settings-in-katalon-studio">failure handling</a> schema to determine whether the execution should be allowed to continue or stop.</td></tr></tbody></table> 

## Example

Given there is a file named `yourImage.jpg` in our project folder that needs uploading on `https://imgur.com/upload?beta`, the snippet below uses `WebUI.uploadFileWithDragAndDrop` to perform the operation. Since the website supports drag and drop on the entire webpage, we don’t have to specify a drop zone:

```jsx
import com.kms.katalon.core.configuration.RunConfiguration as RunConfiguration
import com.kms.katalon.core.webui.keyword.WebUiBuiltInKeywords as WebUI
import static com.kms.katalon.core.testobject.ObjectRepository.findTestObject

WebUI.openBrowser('')
WebUI.navigateToUrl('https://imgur.com/upload?beta')
def filePath = RunConfiguration.getProjectDir() + '/yourImage.jpg'
WebUI.uploadFileWithDragAndDrop(filePath)
WebUI.delay(5)
WebUI.closeBrowser()
```

If uploading multiple files at once by drag-and-drop, for the value of the parameter named <code className="ph codeph">filePath</code>, please provide a string with the following format: <pre className="pre codeblock"><code>pathToFile 1 + "\n" + pathToFile2 + "\n" + pathToFile3</code></pre>For example:

```jsx
import com.kms.katalon.core.configuration.RunConfiguration as RunConfiguration
import com.kms.katalon.core.webui.keyword.WebUiBuiltInKeywords as WebUI
import static com.kms.katalon.core.testobject.ObjectRepository.findTestObject
WebUI.openBrowser('')
WebUI.navigateToUrl('https://imgur.com/upload?beta')
def filePath = RunConfiguration.getProjectDir() + '/Katalon-Devices.JPG'
def filePath1 = RunConfiguration.getProjectDir() + '/Katalon-Devices 1.JPG'
def filePath2 = RunConfiguration.getProjectDir() + '/Katalon-Devices 2.JPG'
def concatenatedFilePath = (((filePath + '\n') + filePath1) + '\n') + filePath2
WebUI.uploadFileWithDragAndDrop(concatenatedFilePath)
WebUI.verifyElementPresent(findTestObject('Object Repository/Imgur/Page_Imgur The magic of the Internet/span_3 images saved'), 10)
WebUI.delay(5)
WebUI.closeBrowser()
```

A sample project is available [here](https://github.com/katalon-studio/Upload-File-with-Drag-and-Drop-Sample-Project).

## <a id="id_0__id_2" class="anchor_top_offset"/>Variations of the keyword usage

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Some websites support uploading a file by drag-and-drop it anywhere on the page, while others only support that in a limited area. Hence, you can omit or keep the <code className="ph codeph">TestObject to</code> parameter in corresponding use cases.</p> 

## <a id="id_0__id_4" class="anchor_top_offset"/>Known limitation

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Some website (e.g., <a className="xref j-external-link" href="https://www.imageupload.net/" target="_blank">Mobile Photo Upload</a>) only shows the drop zone when users drag and drop a file, which means the drop zone is not visible before this keyword is used. In this case, the keyword will not work.</p> 
