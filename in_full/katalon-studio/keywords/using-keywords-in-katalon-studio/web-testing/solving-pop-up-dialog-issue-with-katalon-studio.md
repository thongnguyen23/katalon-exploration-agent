---
hide_title: true
title: Solving Pop-up dialog issue with Katalon Studio
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="id" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Solving Pop-up dialog issue with <span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon Studio</span> 

<p xmlns="http://www.w3.org/1999/xhtml" className="p">When performing automation testing, you may sometimes deal with   pop-up dialog issue that needs to be handled differently from   normal test objects. This tutorial shows you how to deal with   pop-up controls.</p> 
    

## <a id="id_1" class="anchor_top_offset"/>What is a pop-up?

    
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">A pop-up is a graphical display area, usually in a form of a   small window that appears ("pop-up") in the foreground of the   current interface.</p> 
    
  

## <a id="id_2" class="anchor_top_offset"/>What are issues with pop-up?

<p xmlns="http://www.w3.org/1999/xhtml" className="p">The problem with pop-ups is that they usually show up unexpectedly. There is no certain way to overcome this except that you need to understand the behavior of the application and insert scripts accordingly to handle the situation. Another issue with pop-ups is that they are not from the AUT so you need to handle them with dedicated keywords.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Below are a few commonly used pop-ups which might cause problems in your test web automation:</p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">New browser window.</li><li className="li">Alert: An alert box is often used to make sure that information comes through to the user.</li></ul> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/pop_up_dialog_issue/alert-box-300x94.png")} alt="Alert box Katalon Studio" /><br /><br /></p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">Custom modal dialog: A modal dialog is a dialog box/pop-up window that is displayed on top of the current page.</li></ul> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/pop_up_dialog_issue/sign-in.png")} alt="Custom modal dialog" /><br /><br /></p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">Native Window dialog. This dialog is common in case of testing uploading files</li></ul> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/pop_up_dialog_issue/Native-Window-dialog.png")} alt="Native Window dialog" /><br /><br /></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><strong className="ph b">A suggested solution for handling pop-ups using Katalon Studio:</strong></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">To handle such pop-ups as described, you need to capture them first using the Object Spy feature in Katalon Studio. After that, you use "<strong className="ph b">Switch To…</strong>" keywords of Katalon Studio to set focus to the specified pop-up as needed.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">The following screenshot shows simple scripts on how to handle a pop-up using the <a className="xref" href="/katalon-studio/keywords/keyword-description-in-katalon-studio/web-ui-keywords/webui-switch-to-window-title">Switch To Window Title</a> keyword.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/pop_up_dialog_issue/Switch-To-Window-Title-keyword..png")} alt="Solving Pop-up dialog issue" /><br /><br /></p> 

```jsx
'Open browser and navigate to elated site'
WebUI.openBrowser('http://www.elated.com/articles/javascript-tabs/')
'Maximize current browser window'
WebUI.maximizeWindow()
 
'Click on 'Tweet' button in iframe'
WebUI.click(findTestObject('Page_Elated/lnk_Tweet'))
 
'Switch to window that has title 'Share a link on Twitter''
WebUI.switchToWindowTitle('Share a link on Twitter')
 
'Enter email'
WebUI.setText(findTestObject('Page_Share a link on Twitter/txt_Twitter_Login_Email'), email)
 
'Enter password'
WebUI.setText(findTestObject('Page_Share a link on Twitter/txt_Twitter_Login_Password'), password)
 
'Verify Tweet message is displayed for successful login'
WebUI.verifyTextPresent("Share a link with your followers",false)
 
WebUI.closeBrowser()
```
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Where:</p> 
<table xmlns="http://www.w3.org/1999/xhtml" className="table anchor_top_offset" id="id_2__bafd7a85-6190-493c-84d2-e29908190df3"><caption /><thead className="thead"><tr className><th className="entry anchor_top_offset" id="id_2__bafd7a85-6190-493c-84d2-e29908190df3__entry__1">Keyword</th><th className="entry anchor_top_offset" id="id_2__bafd7a85-6190-493c-84d2-e29908190df3__entry__2">Description</th></tr></thead><tbody className="tbody"><tr className><td className="entry" headers="id_2__bafd7a85-6190-493c-84d2-e29908190df3__entry__1 id_2__bafd7a85-6190-493c-84d2-e29908190df3__entry__2 "><a className="xref" href="/katalon-studio/keywords/keyword-description-in-katalon-studio/web-ui-keywords/webui-switch-to-window-title">Switch To Window Title</a></td><td className="entry" headers="id_2__bafd7a85-6190-493c-84d2-e29908190df3__entry__1 id_2__bafd7a85-6190-493c-84d2-e29908190df3__entry__2 ">Switch to the window identified by a given title.</td></tr><tr className><td className="entry" headers="id_2__bafd7a85-6190-493c-84d2-e29908190df3__entry__1 id_2__bafd7a85-6190-493c-84d2-e29908190df3__entry__2 "><a className="xref" href="/katalon-studio/keywords/keyword-description-in-katalon-studio/web-ui-keywords/webui-switch-to-window-index">Switch To Window Index</a></td><td className="entry" headers="id_2__bafd7a85-6190-493c-84d2-e29908190df3__entry__1 id_2__bafd7a85-6190-493c-84d2-e29908190df3__entry__2 ">Switch to the window identified by a given index.</td></tr><tr className><td className="entry" headers="id_2__bafd7a85-6190-493c-84d2-e29908190df3__entry__1 id_2__bafd7a85-6190-493c-84d2-e29908190df3__entry__2 "><a className="xref" href="/katalon-studio/keywords/keyword-description-in-katalon-studio/web-ui-keywords/webui-switch-to-window-url">Switch To Window Url</a></td><td className="entry" headers="id_2__bafd7a85-6190-493c-84d2-e29908190df3__entry__1 id_2__bafd7a85-6190-493c-84d2-e29908190df3__entry__2 ">Switch to the window identified by a given URL.</td></tr></tbody></table> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">If you want to switch back to the default window (parent), use the <a className="xref" href="/katalon-studio/keywords/keyword-description-in-katalon-studio/web-ui-keywords/webui-switch-to-default-content">Switch To Default Content</a> keyword. For example<em className="ph i">:</em> </p> 

```jsx
'Open browser and navigate to a site that has an iframe'
WebUI.openBrowser(GlobalVariable.G_SiteURL)
 
'Switch to iframe'
WebUI.switchToWindowTitle('Share a link on Twitter')
 
'Switch back to default content'
WebUI.switchToDefaultContent()
 
'Close browser'
WebUI.closeBrowser()
```
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Where:</p> 
<table xmlns="http://www.w3.org/1999/xhtml" className="table anchor_top_offset" id="id_2__340e8069-0646-4014-8fcf-3c7375a75e49"><caption /><thead className="thead"><tr className><th className="entry anchor_top_offset" id="id_2__340e8069-0646-4014-8fcf-3c7375a75e49__entry__1">Keyword</th><th className="entry anchor_top_offset" id="id_2__340e8069-0646-4014-8fcf-3c7375a75e49__entry__2">Description</th></tr></thead><tbody className="tbody"><tr className><td className="entry" headers="id_2__340e8069-0646-4014-8fcf-3c7375a75e49__entry__1 id_2__340e8069-0646-4014-8fcf-3c7375a75e49__entry__2 "><a className="xref" href="/katalon-studio/keywords/keyword-description-in-katalon-studio/web-ui-keywords/webui-switch-to-default-content">Switch To Default Content</a></td><td className="entry" headers="id_2__340e8069-0646-4014-8fcf-3c7375a75e49__entry__1 id_2__340e8069-0646-4014-8fcf-3c7375a75e49__entry__2 ">Switch back to the default window, after working with iFrame windows.</td></tr></tbody></table> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">To deal with Windows' native dialogs such as uploading files, users use the <a className="xref" href="/katalon-studio/keywords/keyword-description-in-katalon-studio/web-ui-keywords/webui-switch-to-default-content">Upload File</a> keyword. For example:</p> 

```jsx
'Open browser and navigate to a site that has upload control'
WebUI.openBrowser('http://the-internet.herokuapp.com/upload')

'Use Upload File keyword to deal with the dialog. Noted that the keyword will proceed to click on the Choose File button as specified'
WebUI.uploadFile(findTestObject('choosefile_button'), 'D:\test-photo.png')
 
'Close browser'
WebUI.closeBrowser()
```
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Where:</p> 
<table xmlns="http://www.w3.org/1999/xhtml" className="table anchor_top_offset" id="id_2__56c9d039-2083-4775-86a1-fa35f816a8e6"><caption /><thead className="thead"><tr className><th className="entry anchor_top_offset" id="id_2__56c9d039-2083-4775-86a1-fa35f816a8e6__entry__1">Keyword</th><th className="entry anchor_top_offset" id="id_2__56c9d039-2083-4775-86a1-fa35f816a8e6__entry__2">Description</th></tr></thead><tbody className="tbody"><tr className><td className="entry" headers="id_2__56c9d039-2083-4775-86a1-fa35f816a8e6__entry__1 id_2__56c9d039-2083-4775-86a1-fa35f816a8e6__entry__2 "><a className="xref" href="/katalon-studio/keywords/keyword-description-in-katalon-studio/web-ui-keywords/webui-upload-file">Upload File</a></td><td className="entry" headers="id_2__56c9d039-2083-4775-86a1-fa35f816a8e6__entry__1 id_2__56c9d039-2083-4775-86a1-fa35f816a8e6__entry__2 ">Specify the file for the upload dialog<strong className="ph b">.</strong> </td></tr></tbody></table> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Regarding the browser's pop-ups as mentioned above, you can <a className="xref" href="/katalon-studio/manage-projects/project-settings/katalon-studio-project-settings-overview">modify Desired Capabilities</a> of the browser to prevent them from displaying. You can refer to <a className="xref j-external-link" href="https://forum.katalon.com/discussion/1417/disable-chrome-password-manager" target="_blank">this ticket</a> for an example on how to disable the Chrome password manager.</p> 

## <a id="id_3" class="anchor_top_offset"/>Example

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Here in this example, When I clicked a link, it will open a new window. So I want to switch to that window to perform actions on the newly opened window. We can handle it using Katalon Studio built-in keywords as shown below.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><strong className="ph b">Switch to Window Index:</strong></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">We need to use it when you want to switch to the second window (index 1).</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><strong className="ph b">Manual Mode:</strong></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/pop_up_dialog_issue/Switch-to-Window-Index.png")} alt="Switch To Window Index" /><br /><br /></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><strong className="ph b">Script Mode:</strong></p> 

```jsx
import static com.kms.katalon.core.testobject.ObjectRepository.findTestObject
import com.kms.katalon.core.webui.keyword.WebUiBuiltInKeywords as WebUI
 
'Open browser and navigate to website '
WebUI.openBrowser('http://the-internet.herokuapp.com/windows')

'Maximize the window' 
WebUI.maximizeWindow()
 
'Click on Click Here link'
WebUI.click(findTestObject('Windows/Link_Click Here'))

'Switch to New window by Switch to Window index method' 
WebUI.switchToWindowIndex(1)

'Capturing the Heading of the New Window text and Storing it in a variable'
Heading_NewWindow = WebUI.getText(findTestObject('Windows/Heading_New Window'))
 
'Validating the heading so that it is navigated to desired window by Switch To Window Url Method'
WebUI.verifyEqual(Heading_NewWindow, 'New Window')
```
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><strong className="ph b">Switch To Window Title :</strong></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Switch to the window with given title.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><strong className="ph b">Manual Mode:</strong></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/pop_up_dialog_issue/switch-to-window-title.png")} alt="Switch To Window Title" /><br /><br /></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><strong className="ph b">Script Mode:</strong></p> 

```jsx
import static com.kms.katalon.core.testobject.ObjectRepository.findTestObject
import com.kms.katalon.core.webui.keyword.WebUiBuiltInKeywords as WebUI
 
'Open browser and navigate to website ' 
WebUI.openBrowser('http://the-internet.herokuapp.com/windows')

'Maximize the window'
WebUI.maximizeWindow()
 
'Click on Click Here link'
WebUI.click(findTestObject('Windows/Link_Click Here'))
 
'Switch to New window by Switch to Window Title method'
WebUI.switchToWindowTitle('New Window')
 
'Capturing the Heading of the New Window text and Storing it in a variable'
Heading_NewWindow = WebUI.getText(findTestObject('Windows/Heading_New Window'))
 
'Validating the heading so that it is navigated to desired window by Switch To Window Title Method'
WebUI.verifyEqual(Heading_NewWindow, 'New Window')
```
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><strong className="ph b">Switch To Window Url :</strong></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Switch to the window with given URL.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><strong className="ph b">Manual Mode:</strong></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/pop_up_dialog_issue/switch-to-window-url.png")} alt="Switch To Window Url" /><br /><br /></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><strong className="ph b">Script Mode:</strong></p> 

```jsx
import static com.kms.katalon.core.testobject.ObjectRepository.findTestObject
import com.kms.katalon.core.webui.keyword.WebUiBuiltInKeywords as WebUI
 
'Open browser and navigate to website '
WebUI.openBrowser('http://the-internet.herokuapp.com/windows')

'Maximize the window'
WebUI.maximizeWindow()
 
'Click on Click Here link'
WebUI.click(findTestObject('Windows/Link_Click Here'))
 
'Switch to New window by Switch to Window URL method'
WebUI.switchToWindowUrl('http://the-internet.herokuapp.com/windows/new')

'Capturing the Heading of the New Window text and Storing it in a variable'
Heading_NewWindow = WebUI.getText(findTestObject('Windows/Heading_New Window'))
 
'Validating the heading so that it is navigated to desired window by Switch To Window Url Method'
WebUI.verifyEqual(Heading_NewWindow, 'New Window')
```
<p xmlns="http://www.w3.org/1999/xhtml" className="p">That is some examples of how we handle window using Katalon Studio. You can download the source code <a className="xref j-external-link" href="https://github.com/katalon-studio/katalon-web-automation" target="_blank">here</a>.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><em className="ph i"><strong className="ph b">Exception</strong></em></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><em className="ph i">Noted that <strong className="ph b">NoSuchWindowException</strong></em><em className="ph i">exception will be thrown when window target to be switched doesn't exist.</em></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">For further instructions and help, please refer to <a className="xref" href="/katalon-studio/record-and-spy/webui-record-and-spy-utilities/record-web-utility-in-katalon-studio">[WebUI] Window</a> and join us on <a className="xref j-external-link" href="https://forum.katalon.com/" target="_blank">Katalon Forum</a>.</p> 
