---
hide_title: true
title: Handling Alert Dialog in Mobile App in Katalon Studio
---
import useBaseUrl from '@docusaurus/useBaseUrl';

# <a id="id" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Handling Alert Dialog in Mobile App in <span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon Studio</span> 

<p xmlns="http://www.w3.org/1999/xhtml" className="p">An alert dialog box is used to send a message to the user. An   alert box displays a dialog with a specific message and allows user   to accept or reject the alert (OK/Cancel buttons).</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">The .apk file can be downloaded <a className="xref j-external-link" href="https://github.com/katalon-studio/katalon-mobile-automation/blob/master/Data%20Files/ApiDemos.apk" target="_blank">here</a>.   Start the app. Select <strong className="ph b">App</strong> &gt; <strong className="ph b">Alert     Dialogs</strong>.</p> 

## <a id="id_1" class="anchor_top_offset"/>Scenario

<p xmlns="http://www.w3.org/1999/xhtml" className="p">We want to test the alert dialog which usually appears on mobile   app when there are suspicious/potentially dangerous actions.</p> 
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/handle_alert_dialog_mobile_app/Handling-Alert-Dialog-in-Mobile-App.png")} alt="Handling Alert Dialog in Mobile App" /><br /><br /> </p> 
    
## <a id="id_2" class="anchor_top_offset"/>Manual Mode

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul">   <li className="li">Step 1<strong className="ph b">:</strong> Select <strong className="ph b">Start       Application</strong> from mobile keyword and click on     <strong className="ph b">Input</strong> to open a new dialogue. In     <strong className="ph b">appFile</strong>, select '<strong className="ph b">Value Type</strong>' as     <strong className="ph b">Variable</strong>. In <strong className="ph b">Value</strong>, pass the     variable name as '<strong className="ph b">path'</strong>.</li> </ul> 
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/handle_alert_dialog_mobile_app/Handling-Alert-Dialog-in-Mobile-App-1.png")} alt="Handling Alert Dialog in Mobile App" /><br /><br /> </p> 
      
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul">   <li className="li">Step 2: Add a <strong className="ph b">Wait For Element Present</strong>     item.</li>   <li className="li">Step 3: Call <strong className="ph b">Scroll To Text</strong> from mobile     keyword, pass <strong className="ph b">App</strong> to <strong className="ph b">Input</strong>.     <strong className="ph b">Scroll To Text</strong> accepts <strong className="ph b">String</strong>     type <strong className="ph b">parameter</strong> (Text of the element to scroll     to).</li> </ul> 
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/handle_alert_dialog_mobile_app/Handling-Alert-Dialog-in-Mobile-App-3.png")} alt="Handling Alert Dialog in Mobile App" /><br /><br /> </p> 
      
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul">   <li className="li">Step 4: Call <strong className="ph b">Tap</strong> method and pass the object of     <strong className="ph b">App</strong>.</li>   <li className="li">Step 5: Select <strong className="ph b">Scroll To Text</strong> method and pass     the <strong className="ph b">Alert Dialogs</strong> text.</li> </ul> 
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/handle_alert_dialog_mobile_app/Handling-Alert-Dialog-in-Mobile-App-5.png")} alt="Handling Alert Dialog in Mobile App" /><br /><br /> </p> 
      
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul">   <li className="li">Step 6: Tap on <strong className="ph b">Alert Dialogs</strong>.</li>   <li className="li">Step 7: Add another <strong className="ph b">Wait for Element Present</strong>     keyword for object <strong className="ph b">App</strong>/<strong className="ph b">Alert       Dialogs</strong>.</li>   <li className="li">Step 8: Call <strong className="ph b">Scroll To Text</strong> from mobile     keyword, pass the input as <strong className="ph b">OK Cancel dialog with       traditional theme</strong>.</li>   <li className="li">Step 9: Call <strong className="ph b">Tap</strong> method and pass the object of     <strong className="ph b">OK Cancel dialog with traditional theme</strong>.</li>   <li className="li">Step 10: Verify alert using <strong className="ph b">Verify Element       Visible</strong> keyword.</li>   <li className="li">Step 11: Capture the text of alert using <strong className="ph b">Get       Text</strong> command and store it in a variable     <strong className="ph b">actual_AlertText.</strong>   </li>   <li className="li">Step 12: Verify <strong className="ph b">Actual</strong> and     <strong className="ph b">Expected</strong> alert texts by <strong className="ph b">Verify       Match</strong> keyword.</li> </ul> 
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/handle_alert_dialog_mobile_app/Handling-Alert-Dialog-in-Mobile-App-13.png")} alt="Handling Alert Dialog in Mobile App" /></p> 
      
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul">   <li className="li">Step 13: <strong className="ph b">Tap</strong> on <strong className="ph b">OK</strong>     Button.</li> </ul> 
    
## <a id="id_3" class="anchor_top_offset"/>Script Mode

```jsx
import static com.kms.katalon.core.testobject.ObjectRepository.findTestObject
import com.kms.katalon.core.configuration.RunConfiguration as RunConfiguration
import com.kms.katalon.core.mobile.keyword.MobileBuiltInKeywords as Mobile
import com.kms.katalon.core.model.FailureHandling as FailureHandling
  
'Path of the Apk File Store in path variable'
def path = RunConfiguration.getProjectDir() + '/Data Files/ApiDemos.apk' 
 
'Start the application'
Mobile.startApplication(path, false)
 
'Wait for element Present of Heading API Demos'
Mobile.waitForElementPresent(findTestObject('API Demos Objects/Article_4/heading_API_Demos'), 45)
 
'Scroll to App text'
Mobile.scrollToText('App', FailureHandling.STOP_ON_FAILURE)
 
'Tap on App'
Mobile.tap(findTestObject('API Demos Objects/Handle Alert/text_App'), 20)
 
'Scroll to Alert Dialogs text'
Mobile.scrollToText('Alert Dialogs', FailureHandling.STOP_ON_FAILURE)
  
'Tap on Alert Dialogs'
Mobile.tap(findTestObject('API Demos Objects/Handle Alert/text_Alert Dialogs'), 30)
 
'Wait for Element Present of Header Alert'
Mobile.waitForElementPresent(findTestObject('API Demos Objects/Handle Alert/text_Header Alert'), 30)
 
'Verify Element Visible of Header Alert'
Mobile.verifyElementVisible(findTestObject('API Demos Objects/Handle Alert/text_Header Alert'), 30)
 
'Scroll to "OK Cancel dialog with traditional theme"'
Mobile.scrollToText('OK Cancel dialog with traditional theme', FailureHandling.STOP_ON_FAILURE)
 
'Tap On Button OK Cancel dialog with traditional theme'
Mobile.tap(findTestObject('API Demos Objects/Handle Alert/button_OK Cancel dialog with traditional theme'), 30)
 
'Wait for Element Visible of Alert Title'
Mobile.waitForElementPresent(findTestObject('API Demos Objects/Handle Alert/text_Alert Title'), 30) 
 
'Verify the Element Visible of Alert Title'
Mobile.verifyElementVisible(findTestObject('API Demos Objects/Handle Alert/text_Alert Title'), 30)
 
'Get the Alert Title text and Store in to "actual_AlertText" variable'
actual_AlertText = Mobile.getText(findTestObject('API Demos Objects/Handle Alert/text_Alert Title'), 30)
 
'Verify the actual and Expected Alert Texts'
Mobile.verifyMatch(actual_AlertText, "Lorem ipsum dolor sit aie consectetur adipiscing\nPlloaso mako nuto siwuf cakso dodtos anr koop.",false)

'Tap on OK Button on Alert'
Mobile.tap(findTestObject('API Demos Objects/Handle Alert/button_OK'), 30)
```

<p xmlns="http://www.w3.org/1999/xhtml" className="p">For further instructions and help, please refer to <a className="xref j-external-link" href="http://docs.katalon.com/x/oArR" target="_blank">Katalon User Guide</a> or <a className="xref j-external-link" href="https://forum.katalon.com/" target="_blank">Katalon Forum</a>.</p> 
