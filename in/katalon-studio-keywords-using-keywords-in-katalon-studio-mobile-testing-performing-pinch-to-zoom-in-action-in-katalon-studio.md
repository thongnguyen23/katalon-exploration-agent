---
hide_title: true
title: Performing Pinch to Zoom In Action in Katalon Studio
---
import useBaseUrl from '@docusaurus/useBaseUrl';

# <a id="id" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Performing Pinch to Zoom In Action in <span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon Studio</span> 

<p xmlns="http://www.w3.org/1999/xhtml" className="p">This tutorial is to test the <strong className="ph b">Pinch To Zoom In</strong>   action in the mobile app. The app used for this demonstration can   be downloaded here. We will be using Android O.S for this tutorial,   so please make sure that your Android device <strong className="ph b">API</strong>   is <strong className="ph b">greater</strong> than <strong className="ph b">18</strong>.</p> 

## <a id="id_1" class="anchor_top_offset"/>Scenario

<p xmlns="http://www.w3.org/1999/xhtml" className="p">In the screenshot below, we want to zoom into "Hello World" and   verify the zoom-in action.</p> 
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/pinch_zoom_action_mobile_app/Performing-Pinch-to-Zoom-In-in-automation-test.png")} alt="Performing Pinch to Zoom In in automation test" /><br /><br /> </p> 
    
## <a id="id_2" class="anchor_top_offset"/>Manual Mode

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">Step 1: Select <strong className="ph b">Start       Application</strong> from mobile keyword and click on     <strong className="ph b">Input</strong> it will open a window, where for appFile     select <strong className="ph b">Value Type</strong> as <strong className="ph b">Variable</strong> and     in <strong className="ph b">Value</strong>, pass the variable name as     <strong className="ph b">path</strong> and click <strong className="ph b">OK.</strong>   </li></ul> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/pinch_zoom_action_mobile_app/Performing-Pinch-to-Zoom-In-in-automation-test-1.png")} alt="Performing Pinch to Zoom In in automation test" /><br /><br /> </p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">Step 2: Add a <strong className="ph b">Wait For Element Present</strong> item     for API Demos to show up.</li><li className="li">Step 3: Call <strong className="ph b">Scroll To Text</strong> from mobile     keyword, pass <strong className="ph b">Views</strong> as Input. <strong className="ph b">Scroll To       Text</strong> accepts String type parameter (Text of the element to     scroll to)</li></ul> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/pinch_zoom_action_mobile_app/Performing-Pinch-to-Zoom-In-in-automation-test-3.png")} alt="Performing Pinch to Zoom In in automation test" /><br /><br /> </p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">Step 4: Call <strong className="ph b">Tap</strong> method and pass the object of     <strong className="ph b">Views.</strong>   </li><li className="li">Step 5: Select <strong className="ph b">Scroll To Text</strong> keyword and pass     the <strong className="ph b">Tabs</strong> text.</li></ul> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/pinch_zoom_action_mobile_app/Performing-Pinch-to-Zoom-In-in-automation-test-10.png")} alt="Performing Pinch to Zoom In in automation test" /><br /><br /> </p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">Step 6: Call <strong className="ph b">Tap</strong> method and pass the object of     <strong className="ph b">WebView</strong>   </li><li className="li">Step 7: Add <strong className="ph b">wait commands</strong> to wait for     '<strong className="ph b">Hello world</strong>' link to be visible.</li><li className="li">Step 8: Call '<strong className="ph b">Get Element Height</strong>' method and     capture the of "<strong className="ph b">Hello World</strong>" height to store it in     a variable named '<strong className="ph b">ele_Height</strong>'.</li><li className="li">Step 9: Call '<strong className="ph b">Get Element Width</strong>' method and     capture the of "<strong className="ph b">Hello World</strong>" element     <strong className="ph b">width</strong> to store it in '<strong className="ph b">ele_Width</strong>'.   </li><li className="li">Step 10: Add '<strong className="ph b">Pinch To Zoom In At Position</strong>'     method from mobile keyword list and pass the following values in:     <strong className="ph b">ele<em className="ph i">Height</em>,</strong> eleWidth,     <strong className="ph b">Offset</strong> value.</li></ul> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/pinch_zoom_action_mobile_app/Performing-Pinch-to-Zoom-In-in-automation-test-11.png")} alt="Performing Pinch to Zoom In in automation test" /><br /><br /> </p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">Step 11: After zooming in, we need to <strong className="ph b">verify</strong>     that element has been zoomed. Thus, we need to re-capture the     element Height and Width.</li><li className="li">Step 12: After zooming the element height and width     <strong className="ph b">should be greater</strong> than the existing height and     width in the test. By using '<strong className="ph b">Verify Greater Than</strong>'     method, we can validate the element height and width.</li></ul> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/pinch_zoom_action_mobile_app/Performing-Pinch-to-Zoom-In-in-automation-test-12.png")} alt="Performing Pinch to Zoom In in automation test" /><br /><br /> </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">As you can see from the step-by-step guide above, there are   repeated steps that will be easier to create in <strong className="ph b">Script     Mode</strong>. Thus, we suggest the users to utilize this feature   where one can quickly automate the test scenario and easily manage   test scripts.</p> 

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
Mobile.waitForElementPresent(findTestObject('API Demos Objects/Zoom_IN/heading_API_Demos'), 45)
 
'Checking the Element "Heading API Demos" is in Visible '
Mobile.verifyElementVisible(findTestObject('API Demos Objects/Zoom_IN/heading_API_Demos'), 30)
 
'Scroll to Views text'
Mobile.scrollToText('Views', FailureHandling.STOP_ON_FAILURE)
 
'Tap on Views'
Mobile.tap(findTestObject('API Demos Objects/Zoom_IN/text_Views'), 20)
 
'Scroll to WebView text'
Mobile.scrollToText('WebView', FailureHandling.STOP_ON_FAILURE)
 
'Checking the Element "WebView" is in Visible '
Mobile.verifyElementVisible(findTestObject('API Demos Objects/Zoom_IN/text_WebView'), 30)
 
'Tap on WebView'
Mobile.tap(findTestObject('API Demos Objects/Zoom_IN/text_WebView'), 30)
 
'Wait for Element Present "Hello World"'
Mobile.waitForElementPresent(findTestObject('API Demos Objects/Zoom_IN/link_Hello World'), 30)
 
'Checking the Element "Hello World" is in Visible '
Mobile.verifyElementVisible(findTestObject('API Demos Objects/Zoom_IN/link_Hello World'), 30)
 
'Get Element Height of "Hello World" Element'
ele_Height = Mobile.getElementHeight(findTestObject('API Demos Objects/Zoom_IN/link_Hello World'), 30)
 
'Get Element Width of "Hello World" Element'
ele_Width = Mobile.getElementWidth(findTestObject('API Demos Objects/Zoom_IN/link_Hello World'), 30)
 
'Pinch to Zoom In on "Hello World" Element up to 200 Offset'
Mobile.pinchToZoomInAtPosition(ele_Height, ele_Width, 200)
 
'Get Element Height of  Zoom In "Hello World" Element'
zoom_ele_Height = Mobile.getElementHeight(findTestObject('API Demos Objects/Zoom_IN/link_Hello World'), 30)
 
'Get Element Width of Zoom In "Hello World" Element'
zoom_ele_Width = Mobile.getElementWidth(findTestObject('API Demos Objects/Zoom_IN/link_Hello World'), 30)
 
'Verify the Element Height of Zoom In greater than normal Element height'
Mobile.verifyGreaterThan(zoom_ele_Height, ele_Height)
 
'Verify the Element Width of Zoom In greater than normal Element Width'
Mobile.verifyGreaterThan(zoom_ele_Width, ele_Width)
 
'Close the Application.'
Mobile.closeApplication()
```

<p xmlns="http://www.w3.org/1999/xhtml" className="p">The source code is available <a className="xref j-external-link" href="https://github.com/katalon-studio/katalon-mobile-automation" target="_blank">here</a>. For   further instructions and help, please refer to <a className="xref" href="/katalon-studio/keywords/keyword-description-in-katalon-studio/mobile-keywords/mobile-pinch-to-zoom-in-at-position">Pinch     To Zoom In At Position</a> guide and join us on <a className="xref j-external-link" href="http://forum.katalon.com/" target="_blank">Katalon Forum</a>.</p> 
