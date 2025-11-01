---
hide_title: true
title: How to Handle Alerts in Katalon Studio
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="id_handle_alerts" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>How to Handle Alerts in <span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon Studio</span> 

    

## <a id="id_1" class="anchor_top_offset"/>What is an alert?

    
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">An alert is a Javascript function which is used to notify users   on a Web page. It displays a dialog with a specified message and   OK/Cancel buttons.</p> 
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">The alert is a modal dialog that takes the focus away from the   current window and forces the user to take action before performing   other actions. It also prevents the user from accessing other parts   of the page until the user performs the action presented in the   dialog. For example, when the user clicks on the "Delete" button,   an alert would be triggered asking user 'Are you sure, you want to   delete?' The user has to take action on this dialog.</p> 
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Such an alert can be handled using Katalon Studio built-in   keywords. This tutorial shows how to do so with HTML examples. You   can get the HTML by clicking <a className="xref j-external-link" href="https://github.com/katalon-studio/katalon-web-automation/blob/master/Html%20Files/How%20to%20Handle%20Alerts2.html" target="_blank">here</a>.</p> 

## <a id="id_2" class="anchor_top_offset"/>Handle Alerts using Katalon Studio
### <a id="id_3" class="anchor_top_offset"/>1. Handle Accept Alert

<p xmlns="http://www.w3.org/1999/xhtml" className="p">This alert method is used to confirm an action performed by the   user. You can handle this method either in the manual or script   modes.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <strong className="ph b">Manual Mode</strong> </p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">Step 1: Launching the browser navigating to Alert present page     by Open Browser method</li><li className="li">Step 2: Maximize the window of the browser with Maximize     window</li><li className="li">Step 3: Clicking on button</li><li className="li">Step 4: Call the Accept alert method</li></ul> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/handle_alerts/Handle-accept-alert.png")} alt="Handle Accept Alerts using Katalon Studio" /><br /><br /> </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <strong className="ph b">Script Mode</strong> </p> 

```jsx
import static com.kms.katalon.core.testobject.ObjectRepository.findTestObject
import com.kms.katalon.core.webui.keyword.WebUiBuiltInKeywords as WebUI
 
'Launching the browser navigating to Alert present page'
WebUI.openBrowser('C:\\Users\\User\\Desktop\\How to Handle Alerts.html')
 
'Maximize the window of the browser'
WebUI.maximizeWindow()
 
'Clicking on  button'
WebUI.click(findTestObject('Alerts/button_ClickHere'))
 
'Accepting the Alert'
WebUI.acceptAlert()
```

### <a id="id_4" class="anchor_top_offset"/>2. Handle Dismiss Alert

<p xmlns="http://www.w3.org/1999/xhtml" className="p">This alert method is used to ask the user to cancel   something.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <strong className="ph b">Manual Mode</strong> </p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">Step 1: Launching the browser navigating to Alert present page     by Open Browser method</li><li className="li">Step 2: Maximize the window of the browser with Maximize     window</li><li className="li">Step 3: Clicking on button</li><li className="li">Step 4: Call the Dismiss alert method</li></ul> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/handle_alerts/Handle-dismiss-alert.png")} alt="Handle dismiss alerts using Katalon Studio" /><br /><br /> </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <strong className="ph b">Script Mode</strong> </p> 

```jsx
import static com.kms.katalon.core.testobject.ObjectRepository.findTestObject
import com.kms.katalon.core.webui.keyword.WebUiBuiltInKeywords as WebUI
 
'Launching the browser navigating to Alert present page'
WebUI.openBrowser('C:\\Users\\User\\Desktop\Alerts\How to Handle Alerts2.html')
 
'Maximize the window of the browser'
WebUI.maximizeWindow()
 
'Clicking on  button'
WebUI.click(findTestObject('Alerts/button_ClickHere'))
 
'Dismiss the Alert '
WebUI.dismissAlert()
```

### <a id="id_5" class="anchor_top_offset"/>3. Send data to an alert dialog

<p xmlns="http://www.w3.org/1999/xhtml" className="p">We can pass text to an <strong className="ph b">Alert</strong> text message by   using the <strong className="ph b">sendKeys()</strong> method.</p> 
        
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <strong className="ph b">Manual Mode</strong> </p> 
        
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul">   <li className="li">Step 1: Launching the browser navigating to Alert present page     by Open Browser method</li>   <li className="li">Step 2: Maximize the window of the browser with Maximize     window</li>   <li className="li">Step 3: Clicking on button</li>   <li className="li">Step 4: By sendKeys method passing the Text to an Alert</li> </ul> 
        
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/handle_alerts/Send-data-to-an-alert-dialog.png")} alt="Send data to an alert dialog using Katalon Studio" /><br /><br /> </p> 
        
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <strong className="ph b">Script Mode</strong> </p> 
                  
```jsx
import static com.kms.katalon.core.testobject.ObjectRepository.findTestObject
import org.openqa.selenium.WebDriver as WebDriver
import com.kms.katalon.core.webui.driver.DriverFactory as DriverFactory
import com.kms.katalon.core.webui.keyword.WebUiBuiltInKeywords as WebUI
 
'Launching the browser navigating to Alert present page'
WebUI.openBrowser('C:\\Users\\User\\Desktop\Alerts\How to Handle Alerts2.html')
 
'Maximize the window of the browser'
WebUI.maximizeWindow()
 
'Clicking on  button'
WebUI.click(findTestObject('Alerts/button_ClickHere'))
WebDriver driver = DriverFactory.getWebDriver()

'Passing the text in the text box in the Alert'
driver.switchTo().alert().sendKeys('Testing')

'Dismiss the Alert'
WebUI.dismissAlert()
```
### <a id="id_6" class="anchor_top_offset"/>4. Capture the alert message

<p xmlns="http://www.w3.org/1999/xhtml" className="p">We can capture the message on Alert by using the getText()   method.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <strong className="ph b">Manual Mode</strong> </p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">Step 1: Launching the browser navigating to Alert present page     by Open Browser method</li><li className="li">Step 2: Maximize the window of the browser with Maximize     window</li><li className="li">Step 3: Clicking on button</li><li className="li">Step 4: Getting the text from the alert and storing it in     Variable</li><li className="li">Step 5: Verifying the Actual and Expected text from Alert</li></ul> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/handle_alerts/Capture-alert-message.png")} alt="Capture the alert message using Katalon Studio" /><br /><br /> </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <strong className="ph b">Script Mode</strong> </p> 

```jsx
import static com.kms.katalon.core.testobject.ObjectRepository.findTestObject
import org.openqa.selenium.WebDriver as WebDriver
import com.kms.katalon.core.webui.driver.DriverFactory as DriverFactory
import com.kms.katalon.core.webui.keyword.WebUiBuiltInKeywords as WebUI

'Launching the browser'
WebUI.openBrowser('C:\\Users\\User\\Desktop\Alerts\How to Handle Alerts2.html')

'Maximize the window of the browser'
WebUI.maximizeWindow()

'Clicking on the click here button'
WebUI.click(findTestObject('Alerts/button_ClickHere'))
WebDriver driver = DriverFactory.getWebDriver()

'Getting the text from the alert and storing it in Variable'
String AlertText = driver.switchTo().alert().getText()

'Verifying the Actual and Expected text from Alert'
WebUI.verifyEqual(AlertText, 'Please enter your name')
```
<p xmlns="http://www.w3.org/1999/xhtml" className="p">The source code is available to be downloaded <a className="xref j-external-link" href="https://github.com/katalon-studio/katalon-web-automation" target="_blank">here</a>.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">For further instructions and help, refer to <a className="xref" href="/katalon-studio/keywords/keyword-description-in-katalon-studio/web-ui-keywords/webui-accept-alert">WebUI Alert</a> and <a className="xref" href="/katalon-studio/keywords/using-keywords-in-katalon-studio/web-testing/solving-pop-up-dialog-issue-with-katalon-studio">Solving pop-up dialog issue with Katalon Studio</a>.</p> 
