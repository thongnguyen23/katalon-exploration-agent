---
hide_title: true
title: Handling Spinner in Mobile Automation Testing in Katalon Studio
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="id" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Handling Spinner in Mobile Automation Testing in <span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon Studio</span> 

<p xmlns="http://www.w3.org/1999/xhtml" className="p">The source code can be downloaded <a className="xref j-external-link" href="https://github.com/katalon-studio/katalon-mobile-automation/blob/master/Data%20Files/ApiDemos.apk" target="_blank">here</a>.   This behavior is very common in mobile software development. An   example is choosing a location out of a list of US states and   territories.</p> 

## <a id="id_1" class="anchor_top_offset"/>Scenario

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Scroll down in Planet Spinner list and <strong className="ph b">select</strong>   "Pluto". <strong className="ph b">Verify</strong> selected value "Pluto".</p> 
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/handle_spinner_mobile_automation_testing/Handle-spinner-in-Mobile-automation-test.png")} alt="Handle Spinner in Mobile Automation Testing" /><br /><br /> </p> 

## <a id="id_2" class="anchor_top_offset"/>Manual Mode

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">Step 1: Select <strong className="ph b">Start       Application</strong> from mobile keyword and click on     <strong className="ph b">Input.</strong> A dialog will be displayed. In     <strong className="ph b">appFile</strong>, select <strong className="ph b">Value Type</strong> as     <strong className="ph b">Variable</strong>. In <strong className="ph b">Value</strong>, pass the     variable name as <strong className="ph b">path</strong>.</li></ul> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/handle_spinner_mobile_automation_testing/Handle-spinner-in-Mobile-automation-test-1.png")} alt="Handle Spinner in Mobile Automation Testing" /><br /><br /> </p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">Step 2: Add <strong className="ph b">Wait For Element Present</strong>     item.</li><li className="li">Step 3: Call <strong className="ph b">Scroll To Text</strong> from mobile     keyword, pass the input as <strong className="ph b">Views</strong>. <strong className="ph b">Scroll       To Text</strong> accepts String type parameter (Text of the element     to scroll to).</li></ul> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/handle_spinner_mobile_automation_testing/Handle-spinner-in-Mobile-automation-test-3.png")} alt="Handle Spinner in Mobile Automation Testing" /><br /><br /> </p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">Step 4: Call Tap method and pass the object of     <strong className="ph b">Views.</strong>   </li><li className="li">Step 5: Call <strong className="ph b">Scroll To Text</strong> from mobile     keyword, pass the input as <strong className="ph b">Spinner.</strong>   </li><li className="li">Step 6: Tap on <strong className="ph b">Spinner.</strong>   </li><li className="li">Step 7: Here in this step after tapping on 'Spinner' we need to     wait for Heading 'Views/Spinner' is visible on the screen.</li><li className="li">Step 8: Call <strong className="ph b">Tap</strong> method and pass the object of     'Planet Spinner' option.</li><li className="li">Step 9: Call <strong className="ph b">Scroll To Text</strong> from mobile     keyword, pass the input as <strong className="ph b">Pluto</strong>.</li><li className="li">Step 10: Call <strong className="ph b">Tap</strong> method and pass the object     of <strong className="ph b">Pluto</strong> option.</li><li className="li">Step 11: To verify that <strong className="ph b">Pluto</strong> option has been     selected, we are capturing the text of the selected object by     calling <strong className="ph b">Get Text</strong> keyword and storing it in a     variable.</li></ul> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/handle_spinner_mobile_automation_testing/Handle-spinner-in-Mobile-automation-test-11.png")} alt="Handle Spinner in Mobile Automation Testing" /><br /><br /> </p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">Step 12: Call <strong className="ph b">'Verify Match'</strong> keyword to     validate whether the value stored a variable is matched with the     expected result.</li></ul> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/handle_spinner_mobile_automation_testing/Handle-spinner-in-Mobile-automation-test-12.png")} alt="Handle Spinner in Mobile Automation Testing" /><br /><br /> </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">The step-by-step guide can also be achieved through   <strong className="ph b">Script Mode</strong>. We suggest using the Script feature   in Katalon to automate the process faster.</p> 

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
Mobile.waitForElementPresent(findTestObject('API Demos Objects/Spinner_Example/heading_API_Demos'), 45)

'Scroll to Views text'
Mobile.scrollToText('Views', FailureHandling.STOP_ON_FAILURE)

'Tap on Views'
Mobile.tap(findTestObject('API Demos Objects/Spinner_Example/text_Views'), 20)

'Scroll to Spinner text'
Mobile.scrollToText('Spinner', FailureHandling.STOP_ON_FAILURE)

'Tap on Spinner'
Mobile.tap(findTestObject('API Demos Objects/Spinner_Example/text_Spinner'), 20)

'wait for Element Present of text Header Spinner'
Mobile.waitForElementPresent(findTestObject('API Demos Objects/Spinner_Example/text_header Spinner'), 20)

'Verify Element Visible of text Header Spinner'
Mobile.verifyElementVisible(findTestObject('API Demos Objects/Spinner_Example/text_header Spinner'), 30)

'Tap on Spinner Planet'
Mobile.tap(findTestObject('API Demos Objects/Spinner_Example/spinner_Planet'), 30)

'Scroll to "Pluto" text'
Mobile.scrollToText('Pluto', FailureHandling.STOP_ON_FAILURE)

'Tap on Pluto'
Mobile.tap(findTestObject('API Demos Objects/Spinner_Example/text_Pluto'), 20)

'Get Selected Dropdown Value and Stored in to "actual_SelectedValue" variable'
actual_SelectedValue = Mobile.getText(findTestObject('API Demos Objects/Spinner_Example/validation_Selected Spinner value'),
    30)

'Verify Actual and Expected value of Selected Dropdown'
Mobile.verifyMatch(actual_SelectedValue, 'Pluto', false)

Mobile.closeApplication()
```

<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Note:</strong> This scenario can be also handled by capturing the values in a list and tapping on the desired value from spinner.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><em className="ph i">The source code is available at: <a className="xref j-external-link" href="https://github.com/katalon-studio/katalon-mobile-automation" target="_blank">katalon-studio-samples/katalon-mobile-automation</a>.</em></p> 
