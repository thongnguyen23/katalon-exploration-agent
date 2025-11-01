---
hide_title: true
title: How to Handle Textbox Checkbox and Radio Button in Katalon Studio
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="id" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>How to Handle Textbox Checkbox and Radio Button in <span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon Studio</span> 

<p xmlns="http://www.w3.org/1999/xhtml" className="p">This tutorial illustrates how to handle Textbox, Checkbox, Radio   buttons using Katalon Studio. The reference source code is provided   at the end of the tutorial.</p> 
    

## <a id="id_1" class="anchor_top_offset"/>How to Handle Textbox

    
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">A textbox is a field that allows users to enter text as an   input. Textbox and textarea are similar but the latter allows   multiple lines and more characters.</p> 
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Users can perform certain actions on textbox such as clear text,   type text and validate the provided text using Katalon Studio.</p> 
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <strong className="ph b">Scenario: Verifying the provided text in     textbox</strong> </p> 
      
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul">   <li className="li">Step 1: Launch Browser</li>   <li className="li">Step 2: Navigate to URL</li>   <li className="li">Step 3: Click on Make Appointment</li>   <li className="li">Step 4: Enter username as "Katalon"</li>   <li className="li">Step 5: Validate the Enter Username is correctly entered or     not</li> </ul> 
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <strong className="ph b">Script Mode</strong> </p> 
              
```jsx
import static com.kms.katalon.core.checkpoint.CheckpointFactory.findCheckpoint
import static com.kms.katalon.core.testcase.TestCaseFactory.findTestCase
import static com.kms.katalon.core.testdata.TestDataFactory.findTestData
import static com.kms.katalon.core.testobject.ObjectRepository.findTestObject
import com.kms.katalon.core.checkpoint.Checkpoint as Checkpoint
import com.kms.katalon.core.checkpoint.CheckpointFactory as CheckpointFactory
import com.kms.katalon.core.mobile.keyword.MobileBuiltInKeywords as MobileBuiltInKeywords
import com.kms.katalon.core.mobile.keyword.MobileBuiltInKeywords as Mobile
import com.kms.katalon.core.model.FailureHandling as FailureHandling
import com.kms.katalon.core.testcase.TestCase as TestCase
import com.kms.katalon.core.testcase.TestCaseFactory as TestCaseFactory
import com.kms.katalon.core.testdata.TestData as TestData
import com.kms.katalon.core.testdata.TestDataFactory as TestDataFactory
import com.kms.katalon.core.testobject.ObjectRepository as ObjectRepository
import com.kms.katalon.core.testobject.TestObject as TestObject
import com.kms.katalon.core.webservice.keyword.WSBuiltInKeywords as WSBuiltInKeywords
import com.kms.katalon.core.webservice.keyword.WSBuiltInKeywords as WS
import com.kms.katalon.core.webui.keyword.WebUiBuiltInKeywords as WebUiBuiltInKeywords
import com.kms.katalon.core.webui.keyword.WebUiBuiltInKeywords as WebUI
import internal.GlobalVariable as GlobalVariable
  
WebUI.openBrowser('')
 
'Passing the URL'
WebUI.navigateToUrl('http://demoaut.katalon.com/')

'Click on the make Appointment Button'
WebUI.click(findTestObject('Page_CURA Healthcare Service/a_Make Appointment'))
 
'Decalre username variable and assign the value'
 
def userName = 'katalon'
 
'Enter text to username field'
WebUI.setText(findTestObject('Page_CURA Healthcare Service (1)/input_username'), userName)
 
'Get the attribute value of username text field'
input_Value = WebUI.getAttribute(findTestObject('Page_CURA Healthcare Service (1)/input_username'), 'value')
 
'verify the entered text and attribute value'
WebUI.verifyMatch(userName, input_Value, false)
 
WebUI.closeBrowser()
```
            
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <strong className="ph b">Manual Mode</strong> </p> 
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/handle_textbox_checkbox_radio_button/Handle-text-box.png")} alt="Handle textbox using Katalon Studio Manual mode" /><br /><br /> </p> 
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">In the script mode above, <strong className="ph b">Def</strong> is a keyword in   Groovy used for declaration of variables. Username is a variable   name, here storing the value "Katalon" in the   <strong className="ph b">username</strong> variable.</p> 
    
  

## <a id="id_2" class="anchor_top_offset"/>How to Handle Button and Checkbox

<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <strong className="ph b">Scenario:</strong> To make an appointment</p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">Step 1: Launch the application under test (URL: <a className="xref j-external-link" href="http://demoaut.katalon.com/" target="_blank">http://demoaut.katalon.com/</a>).</li><li className="li">Step 2: Click on Make Appointment (verify the button and click     operation).</li><li className="li">Step 3: Enter the valid username, password and click on Login     button (verify the button and click operation).</li><li className="li">Step 4: Make an appointment (check, uncheck the     <strong className="ph b">checkbox</strong> and verify check, uncheck status).</li></ul> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <strong className="ph b">Script Mode</strong> </p> 

```jsx
import static com.kms.katalon.core.checkpoint.CheckpointFactory.findCheckpoint
import static com.kms.katalon.core.testcase.TestCaseFactory.findTestCase
import static com.kms.katalon.core.testdata.TestDataFactory.findTestData
import static com.kms.katalon.core.testobject.ObjectRepository.findTestObject
import com.kms.katalon.core.checkpoint.Checkpoint as Checkpoint
import com.kms.katalon.core.checkpoint.CheckpointFactory as CheckpointFactory
import com.kms.katalon.core.mobile.keyword.MobileBuiltInKeywords as MobileBuiltInKeywords
import com.kms.katalon.core.mobile.keyword.MobileBuiltInKeywords as Mobile
import com.kms.katalon.core.model.FailureHandling as FailureHandling
import com.kms.katalon.core.testcase.TestCase as TestCase
import com.kms.katalon.core.testcase.TestCaseFactory as TestCaseFactory
import com.kms.katalon.core.testdata.TestData as TestData
import com.kms.katalon.core.testdata.TestDataFactory as TestDataFactory
import com.kms.katalon.core.testobject.ObjectRepository as ObjectRepository
import com.kms.katalon.core.testobject.TestObject as TestObject
import com.kms.katalon.core.webservice.keyword.WSBuiltInKeywords as WSBuiltInKeywords
import com.kms.katalon.core.webservice.keyword.WSBuiltInKeywords as WS
import com.kms.katalon.core.webui.keyword.WebUiBuiltInKeywords as WebUiBuiltInKeywords
import com.kms.katalon.core.webui.keyword.WebUiBuiltInKeywords as WebUI
import internal.GlobalVariable as GlobalVariable 
 
WebUI.openBrowser('')
 
'Launch the url'
WebUI.navigateToUrl('http://demoaut.katalon.com/')

'Verify the element is clickable or not'
WebUI.verifyElementClickable(findTestObject('Page_CURA Healthcare Service/a_Make Appointment'))
 
'Click on Make Appointment Button'
WebUI.click(findTestObject('Page_CURA Healthcare Service/a_Make Appointment'))
 
'Click on Login Button'
WebUI.click(findTestObject('Page_CURA Healthcare Service (1)/button_Login'))
 
'Select the Hongkong CURA Healthcare Center from dropdown'
WebUI.selectOptionByValue(findTestObject('Page_CURA Healthcare Service (2)/select_facility'), 'Hongkong CURA Healthcare Center',true)
  
'Check Hospital readmission check box'
WebUI.check(findTestObject('Page_CURA Healthcare Service (2)/input_hospital_readmission'))
 
'Verify Hospital readmission check box is checked'
WebUI.verifyElementChecked(findTestObject('Page_CURA Healthcare Service (2)/input_hospital_readmission'), 30)
 
'Uncheck Hospital readmission check box'
WebUI.uncheck(findTestObject('Page_CURA Healthcare Service (2)/input_hospital_readmission'))
 
'Verify uncheck Hospital readmission check box'
WebUI.verifyElementNotChecked(findTestObject('Page_CURA Healthcare Service (2)/input_hospital_readmission'), 30)
 
'click on Medicadi radio button'
WebUI.click(findTestObject('Page_CURA Healthcare Service (2)/input_programs'))
 
'Click on calendar icon'
WebUI.click(findTestObject('Page_CURA Healthcare Service (2)/div_input-group-addon'))
 
'CLick on Calendar date'
WebUI.click(findTestObject('Page_CURA Healthcare Service (2)/td_3'))
 
'Enter katalon text in comments box'
WebUI.setText(findTestObject('Page_CURA Healthcare Service (2)/textarea_comment'), 'Katalon')
 
'Click on Book Appointment'
WebUI.click(findTestObject('Page_CURA Healthcare Service (2)/button_Book Appointment'))
 
'Close the Browser'
WebUI.closeBrowser()
```

<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <strong className="ph b">Manual Mode</strong> </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/handle_textbox_checkbox_radio_button/Handle-Button-and-Checkbox.png")} alt="Handle Button and Checkbox using Katalon Studio Manual mode" /><br /><br /> </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">In the script above, the keyword   <strong className="ph b">VerifyElementClickable</strong> is used to validate whether   the <strong className="ph b">Make Appointment Button</strong> is clickable.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">The keywords <strong className="ph b">VerifyElementChecked</strong> and   <strong className="ph b">VerifyElementNotChecked</strong> are used to validate   whether an element is checked or unchecked, respectively.</p> 

## <a id="id_3" class="anchor_top_offset"/>How to Handle Radio Button

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Radio Button is a toggle-button that allows you to check the   operations.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <strong className="ph b">Scenario:</strong> To make an appointment</p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">Step 1: Launch the application under test (URL: <a className="xref j-external-link" href="http://demoaut.katalon.com/" target="_blank">http://demoaut.katalon.com/</a>).</li><li className="li">Step 2: Click on Make Appointment (verify the button and click     operation).</li><li className="li">Step 3: Enter a valid username, password and click on Login     button (verify the button and click operation).</li><li className="li">Step 4: Make an appointment (check, uncheck the <strong className="ph b">Radio       Button</strong> and verify <strong className="ph b">radio button</strong> check,     uncheck status).</li></ul> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <strong className="ph b">Script Mode</strong> </p> 

```jsx
import static com.kms.katalon.core.checkpoint.CheckpointFactory.findCheckpoint
import static com.kms.katalon.core.testcase.TestCaseFactory.findTestCase
import static com.kms.katalon.core.testdata.TestDataFactory.findTestData
import static com.kms.katalon.core.testobject.ObjectRepository.findTestObject
import com.kms.katalon.core.checkpoint.Checkpoint as Checkpoint
import com.kms.katalon.core.checkpoint.CheckpointFactory as CheckpointFactory
import com.kms.katalon.core.mobile.keyword.MobileBuiltInKeywords as MobileBuiltInKeywords
import com.kms.katalon.core.mobile.keyword.MobileBuiltInKeywords as Mobile
import com.kms.katalon.core.model.FailureHandling as FailureHandling
import com.kms.katalon.core.testcase.TestCase as TestCase
import com.kms.katalon.core.testcase.TestCaseFactory as TestCaseFactory
import com.kms.katalon.core.testdata.TestData as TestData
import com.kms.katalon.core.testdata.TestDataFactory as TestDataFactory
import com.kms.katalon.core.testobject.ObjectRepository as ObjectRepository
import com.kms.katalon.core.testobject.TestObject as TestObject
import com.kms.katalon.core.webservice.keyword.WSBuiltInKeywords as WSBuiltInKeywords
import com.kms.katalon.core.webservice.keyword.WSBuiltInKeywords as WS
import com.kms.katalon.core.webui.keyword.WebUiBuiltInKeywords as WebUiBuiltInKeywords
import com.kms.katalon.core.webui.keyword.WebUiBuiltInKeywords as WebUI
import internal.GlobalVariable as GlobalVariable
  
WebUI.openBrowser('')
 
'Launch the url'
WebUI.navigateToUrl('http://demoaut.katalon.com/')

'Click on Make Appointment Button'
WebUI.click(findTestObject('Page_CURA Healthcare Service/a_Make Appointment'))
 
'Click on Login Button'
WebUI.click(findTestObject('Page_CURA Healthcare Service (1)/button_Login'))
 
'Select the Hongkong CURA Healthcare Center from dropdown'
WebUI.selectOptionByValue(findTestObject('Page_CURA Healthcare Service (2)/select_facility'), 'Hongkong CURA Healthcare Center', true)
  
'Check Hospital readmission check box'
WebUI.check(findTestObject('Page_CURA Healthcare Service (2)/input_hospital_readmission'))
 
'Check on Medicadi radio button'
WebUI.check(findTestObject('Page_CURA Healthcare Service (2)/input_Medicaid Radio'))
 
'Check the None Radio Button'
WebUI.verifyElementChecked(findTestObject('Page_CURA Healthcare Service (2)/input_Medicaid Radio'), 30)
 
'Check on Medicadi radio button'
WebUI.check(findTestObject('Page_CURA Healthcare Service (2)/input_None Radio'))
 
'Verify unchecked status of Medicaid Radio button'
WebUI.verifyElementNotChecked(findTestObject('Page_CURA Healthcare Service (2)/input_Medicaid Radio'), 30)
 
'Verify the checked status of the None Radio Button'
WebUI.verifyElementChecked(findTestObject('Page_CURA Healthcare Service (2)/input_None Radio'), 30)
 
'Click on calendar icon'
WebUI.click(findTestObject('Page_CURA Healthcare Service (2)/div_input-group-addon'))
 
'Click on Calendar date'
WebUI.click(findTestObject('Page_CURA Healthcare Service (2)/td_3'))
 
'Enter katalon text in comments box'
WebUI.setText(findTestObject('Page_CURA Healthcare Service (2)/textarea_comment'), 'Katalon')
 
'Click on Book Appointment'
WebUI.click(findTestObject('Page_CURA Healthcare Service (2)/button_Book Appointment'))
 
'Close the Browser' 
WebUI.closeBrowser()
```
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <strong className="ph b">Manual Mode</strong> </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/handle_textbox_checkbox_radio_button/Handle-Radio-Button.png")} alt="Handle Radio Button using Katalon Studio Manual Mode" /><br /><br /> </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">The source code is available to be downloaded <a className="xref j-external-link" href="https://github.com/katalon-studio/katalon-web-automation" target="_blank">here</a>.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">For further instructions and help, refer to <a className="xref" href="/katalon-studio/keywords/keyword-description-in-katalon-studio/web-ui-keywords/webui-set-text">[WebUI] Text</a> and <a className="xref" href="/katalon-studio/keywords/keyword-description-in-katalon-studio/web-ui-keywords/webui-check">[WebUI] Checkbox</a>.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">You can also refer to <a className="xref j-external-link" href="https://forum.katalon.com/" target="_blank">Katalon Forum</a> for more tutorials and discussions.</p> 
