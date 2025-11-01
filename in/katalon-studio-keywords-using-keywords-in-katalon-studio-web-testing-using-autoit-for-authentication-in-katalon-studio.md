---
hide_title: true
title: Using autoIT for authentication in Katalon Studio
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="id" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Using autoIT for authentication in <span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon Studio</span> 

<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <a className="xref j-external-link" href="http://docs.katalon.com/display/KD/%5BWebUI%5D+Authenticate" target="_blank">WebUI.authenticate</a> keyword in Katalon Studio would work well on Firefox browser, but the function might not work on other browsers due to unknown reasons. This guide will provide you a workaround solution for handling authentication on different browsers is using autoIT.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">This would be applicable for Chrome, Firefox and Edge.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><strong className="ph b">Requirements</strong></p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">Get the latest version of Katalon Studio: <a className="xref j-external-link" href="https://www.katalon.com/" target="_blank">https://www.katalon.com/</a> </p></li><li className="li"><p className="p">Install autoIT (Autoit Full Installation and AutoIt Script Editor) at <a className="xref j-external-link" href="https://www.autoitscript.com/site/autoit/downloads/" target="_blank">https://www.autoitscript.com/site/autoit/downloads/</a> </p></li></ul> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/using-autoit-for-authentication-in-katalon-studio/wpMJM58XL4bJUF-zmJZPMKebEtKP5jEyWJJpawmha20-V2RugS")} /><br /><br /></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">3. <strong className="ph b">Steps Details:</strong> </p> 
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol"><li className="li">Working with AutoIt file:</li></ol> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">Proceed to edit credential to your own account:</p><ul className="ul"><li className="li"><p className="p">Open autoIt Script Editor (SciTE)</p></li><li className="li"><p className="p">Open (or create new) autoit file with contents:</p></li></ul></li></ul> 
<div xmlns="http://www.w3.org/1999/xhtml" className="note note note_note"><span className="note__title">Note:</span> <p className="p">Change your own credential at "Username" and "Password" fields</p></div>

```jsx
WinWaitActive("","Authentication Required","10")
WinFlash("", "Authentication Required",4,500)
If WinExists("","Authentication Required") Then
  Send("Username{TAB}")
  Send("Password{Enter}")
ElseIf WinExists("","Chrome Legacy Window")Then
  Send("Username{TAB}")
  Send("Password{Enter}")
ElseIf WinExists("","Windows Security") Then
  Send("Username{TAB}")
  Send("Password{Enter}")
EndIf
```
- Save this file to your desired location. You would have a file with *au3 format. Right click on file and select "Compile Script" option to create .exe file.

```jsx
WebUI.openBrowser('') 
autoit_prj = '[your_autoit_file_path].exe' 
Runtime.getRuntime().exec(autoit_prj) 
Thread.sleep(3000);
WebUI.navigateToUrl('Your test site url')
```

<p xmlns="http://www.w3.org/1999/xhtml" className="p">For example:</p> 

```jsx
WebUI.openBrowser('')
 
//Sample path. Change it to your saved location of autoIT script
autoit_prj = 'D:\PS-Katalon\AutoIT\Authentication_Custom.exe'
Runtime.getRuntime().exec(autoit_prj)
Thread.sleep(3000);
 
//Sample URL. Please change it to your authentication URL
WebUI.navigateToUrl('http://the-internet.herokuapp.com/basic_auth')
```
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Now it's all done. You can run your test case to see how it works.</p> 
