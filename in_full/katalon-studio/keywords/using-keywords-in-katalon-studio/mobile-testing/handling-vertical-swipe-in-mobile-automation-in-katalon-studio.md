---
hide_title: true
title: Handling Vertical Swipe in Mobile Automation in Katalon Studio
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="id_vertical_swipe_in_mobile_automation" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Handling Vertical Swipe in Mobile Automation in <span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon Studio</span> 

  

## <a id="id_1" class="anchor_top_offset"/>Swipe Vertically from Top to Bottom

  
    
<p xmlns="http://www.w3.org/1999/xhtml" className="p">This tutorial illustrates <strong className="ph b">Vertical</strong>   <strong className="ph b">Swiping from Top to Bottom</strong> action in the mobile   app.This demonstration uses <strong className="ph b">API Demos,</strong> which you   can download from <a className="xref j-external-link" href="https://github.com/katalon-studio/katalon-mobile-automation/blob/master/Data%20Files/ApiDemos.apk" target="_blank">here</a>.   We will be using <strong className="ph b">Android O.S</strong> for this tutorial,   please make sure that your Android device <strong className="ph b">API</strong> is   greater than <strong className="ph b">18</strong>.</p> 
  
    
    

### <a id="id_2" class="anchor_top_offset"/>Scenario

    
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">The screenshot of the app below has a listview containing 'n'   number of rows. Our goal is to swipe vertically from top to bottom   of the screen.</p> 
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/vertical_swipe_in_mobile_automation/Vertical-swipe-in-Mobile-automation.png")} alt="Vertical Swipe in Mobile Automation" /><br /><br /> </p> 
    
  

### <a id="id_3" class="anchor_top_offset"/>Manual Mode

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">Step 1: Select <strong className="ph b">Start       Application</strong> from mobile keyword and click on     <strong className="ph b">Input</strong>, a new window will open. In     <strong className="ph b">appFile</strong>, select <strong className="ph b">Value Type</strong> as     <strong className="ph b">Variable</strong>. In value, pass the variable name as     <strong className="ph b">path</strong>.</li></ul> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/vertical_swipe_in_mobile_automation/Vertical-swipe-in-Mobile-automation-1.png")} alt="Vertical Swipe in Mobile Automation" /><br /><br /> </p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">Step 2: Add a <strong className="ph b">Wait For Element Present</strong>     item.</li><li className="li">Step 3: Call <strong className="ph b">Scroll To Text</strong> from mobile     keyword and pass input as '<strong className="ph b">Views'</strong>. <strong className="ph b">Scroll       To Text</strong> accepts String type parameter (Text of the element     to scroll to)</li></ul> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/vertical_swipe_in_mobile_automation/Vertical-swipe-in-Mobile-automation-3.png")} alt="Vertical Swipe in Mobile Automation" /><br /><br /> </p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">Step 4: Tap on <strong className="ph b">Views</strong>.</li><li className="li">Step 5: Use <strong className="ph b">Get Device Height</strong> keyword to     capture the height of the device and store it in a     <strong className="ph b">device<em className="ph i">height</em> variable. Select</strong> Get Device     Width keyword to capture the width of the device and storing it in     a <strong className="ph b">device</strong>Width variable.</li><li className="li">Step 6: Add a <strong className="ph b">binary statement</strong>, and in the     'startX' value, store the device width divided by 2. In this     illustration, the X-coordinates will stay constant.</li><li className="li">Step 7: Add a <strong className="ph b">binary statement</strong>, assign 'endX'     value to startX'.</li><li className="li">Step 8: Add a <strong className="ph b">binary statement</strong>, in which the     'startY' variable is the device height multiplied by 0.30.</li><li className="li">Step 9: Add a <strong className="ph b">binary statement</strong>, in which the     'endY' variable is the device height multiplied by 0.70.</li><li className="li">Step 10: Call the <strong className="ph b">swipe method</strong> and select the     <strong className="ph b">Value Type</strong> as '<strong className="ph b">Variable</strong>'. Pass     the startX, startY, endX, endY values to that method.</li></ul> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/vertical_swipe_in_mobile_automation/Vertical-swipe-in-Mobile-automation-10.png")} alt="Vertical Swipe in Mobile Automation" /><br /><br /> </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">The same thing can be achieved from the Script mode (switch to   Script Mode by clicking on Script tab).</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <strong className="ph b">Script Mode:</strong> </p> 

```jsx
import static com.kms.katalon.core.testobject.ObjectRepository.findTestObject 
import com.kms.katalon.core.configuration.RunConfiguration as RunConfiguration
import com.kms.katalon.core.mobile.keyword.MobileBuiltInKeywords as Mobile
import com.kms.katalon.core.model.FailureHandling as FailureHandling
 
'Path of the Apk File Store in path variable'
def path = RunConfiguration.getProjectDir() + '/Data Files/ApiDemos.apk'

'Start the application'
Mobile.startApplication(path, false)
 
'Wait for element Present'
Mobile.waitForElementPresent(findTestObject('API Demos Objects/heading_API_Demos'), 45)
 
''Scroll to Text Views''
Mobile.scrollToText('Views', FailureHandling.STOP_ON_FAILURE)
 
''Tap on Views''
Mobile.tap(findTestObject('API Demos Objects/text_Views'), 20)
 
'Get Device Height and Store in device_height variable'
device_Height = Mobile.getDeviceHeight()
 
'Get Width Height and Store in device_Width variable'
device_Width = Mobile.getDeviceWidth()
 
'Storing the startX value by dividing device width by 2. Because x coordinates are constant for Vertical Swiping'
int startX = device_Width / 2

'Here startX and endX values are equal for vertical Swiping for that assigning startX value to endX'
int endX = startX 
'Storing the startY value'
int startY = device_Height * 0.30
 
'Storing the endY value'
int endY = device_Height * 0.70
 
'Swipe Vertical from top to bottom'
Mobile.swipe(startX, endY, endX, startY)
 
'Swipe Vertical from bottom to top'
Mobile.swipe(startX, startY, endX, endY)
```

<p xmlns="http://www.w3.org/1999/xhtml" className="p">The source code is available <a className="xref j-external-link" href="https://github.com/katalon-studio/katalon-mobile-automation" target="_blank">here</a>. For   further instructions and help, please refer to <a className="xref" href="/katalon-studio/keywords/keyword-description-in-katalon-studio/mobile-keywords/mobile-swipe">Mobile     Swipe</a> guideline and join us on <a className="xref j-external-link" href="http://forum.katalon.com/" target="_blank">Katalon Forum</a>.</p> 
