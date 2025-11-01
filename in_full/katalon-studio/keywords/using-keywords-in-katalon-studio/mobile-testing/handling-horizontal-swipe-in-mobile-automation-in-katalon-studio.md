---
hide_title: true
title: Handling Horizontal Swipe in Mobile Automation in Katalon Studio
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="id_horizontal_swipe_mobile_automation" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Handling Horizontal Swipe in Mobile Automation in <span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon Studio</span> 

## <a id="id_1" class="anchor_top_offset"/>Swipe Horizontally from Left to Right

<p xmlns="http://www.w3.org/1999/xhtml" className="p">This tutorial illustrates Horizontal Swiping actions in the   mobile app. This demonstration uses SwipeListView Demo, which you   can download it <a className="xref j-external-link" href="https://apkpure.com/swipelistview-demo/com.fortysevendeg.android.swipelistview" target="_blank">here</a>.   We will be using Android O.S for this tutorial, so please make sure   that your Android device API is greater than 18.</p> 

### <a id="id_2" class="anchor_top_offset"/>Scenario      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">The screenshot of the app contains a list of applications which   are installed in the mobile device. We want to swipe horizontally   from left to right on any application from this list.</p> 
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/horizontal_swipe_mobile_automation/Handling-Horizontal-Swipe-in-Mobile-Automation.png")} alt="Handling Horizontal Swipe in Mobile Automation" /><br /><br /> </p> 

### <a id="id_3" class="anchor_top_offset"/>Manual Mode

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">Step 1: Select <strong className="ph b">Start       Application</strong> from mobile keyword and click on     <strong className="ph b">Input</strong>, a new window will appear. In     <strong className="ph b">appFile</strong>     <em className="ph i">,</em> select Value Type as     <strong className="ph b">Variable</strong>. In <strong className="ph b">Value</strong>, pass the     variable name as <strong className="ph b">path</strong>.</li></ul> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/horizontal_swipe_mobile_automation/Handling-Horizontal-Swipe-in-Mobile-Automation-1.png")} alt="Handling Horizontal Swipe in Mobile Automation" /><br /><br /> </p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">Step 2: After launching the application, call a <strong className="ph b">Wait       For Element Present</strong> method. Capture the status of an Alert     presence in a variable '<strong className="ph b">alert_Status</strong>'. It returns     true when an alert is present and false when alert is not     present.</li><li className="li">Step 3: Adding an If statement, if     '<strong className="ph b">alert_Status</strong>' is true, tap on "Don't show this     message again" and tap OK<strong className="ph b">.</strong>   </li></ul> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/horizontal_swipe_mobile_automation/Handling-Horizontal-Swipe-in-Mobile-Automation-3.png")} alt="Handling Horizontal Swipe in Mobile Automation" /><br /><br /> </p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">Step 4: Add another <strong className="ph b">Wait For Element Present</strong>     item to verify whether the mobile element pops up.</li><li className="li">Step 5: Use <strong className="ph b">Get Device Height</strong> keyword to     capture the height of the device and store it in a     <strong className="ph b">device<em className="ph i">height</em> variable. Select</strong> Get Device     Width keyword to capture the width of the device and storing it in     a <strong className="ph b">device</strong>Width variable.</li><li className="li">Step 6: Add a <strong className="ph b">binary statement</strong> with the     'startY' divided by 2. Here, the y-coordinates are constant.</li><li className="li">Step 7: Add <strong className="ph b">binary statement</strong>, here 'endY' and     'startY' values are the same for horizontal swiping, so re-assign     'startY' value to 'endY'.</li><li className="li">Step 8: Add <strong className="ph b">binary statement</strong> and multiply     device width with 0.30 to store it in 'startX' variable.</li><li className="li">Step 9: Add <strong className="ph b">binary statement</strong> and multiply     device width with 0.70 to store it in 'endX' variable.</li><li className="li">Step 10: Call the <strong className="ph b">swipe method</strong> and select the     <strong className="ph b">Value Type</strong> as '<strong className="ph b">Variable</strong>'. Pass     the startX, startY, endX, endY values to that method</li></ul> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/horizontal_swipe_mobile_automation/Handling-Horizontal-Swipe-in-Mobile-Automation-10.png")} alt="Handling Horizontal Swipe in Mobile Automation" /><br /><br /> </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">The step-by-step guide above can be achieved through   <strong className="ph b">Script mode</strong> (switch to Script Mode by clicking on   Script tab).</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <em className="ph i">     <strong className="ph b">Note:</strong> Swiping horizontally from right to     left can also be implemented similarly.</em> </p> 

### <a id="id_4" class="anchor_top_offset"/>Script Mode

```jsx
import static com.kms.katalon.core.testobject.ObjectRepository.findTestObject
import com.kms.katalon.core.configuration.RunConfiguration as RunConfiguration
import com.kms.katalon.core.mobile.keyword.MobileBuiltInKeywords as Mobile

'Path of the Swipe List View Demo APK File Store in path variable' 
def path = RunConfiguration.getProjectDir() + '/Data Files/SwipeListView Demo.apk'

'Start the application' 
Mobile.startApplication(path, false)
 
'Wait for Element Present of checkbox Don't Show this message again.\r\nif element present return true otherwise false.'
alert_Status = Mobile.waitForElementPresent(findTestObject('Swipe ListView Demos/checkbox_Dont show this message again'), 20)
  
'Checking the if statement based on element present of alert check box'

if (alert_Status == true) {
    'Tap on check box'
    Mobile.tap(findTestObject('Swipe ListView Demos/checkbox_Dont show this message again'), 30)
    
    'Tap on Ok'
    Mobile.tap(findTestObject('Swipe ListView Demos/button_Ok'), 30)
}
 
'Wait for element Present of Heading API Demos'
Mobile.waitForElementPresent(findTestObject('Swipe ListView Demos/header_text SwipeListView Demo'), 45)

'Get Device Height and Store in device_height variable'
device_Height = Mobile.getDeviceHeight()

'Get Device Width and Store in device_Width variable'
device_Width = Mobile.getDeviceWidth()
 
'Storing the startX,endX values by dividing device height by 2 Because Y coordinates are constant'
int startY = device_Height / 2
 
'Here endY and startY values are equal for vertical Swiping for that assigning startY value to endY'
int endY = startY
 
'Storing the startX value'
int startX = device_Width * 0.30
 
'Storing the endX value'
int endX = device_Width * 0.70
 
'Here Y constant for Swipe Vertical Left to Right'
Mobile.swipe(startX, startY, endX, endY)
```

<p xmlns="http://www.w3.org/1999/xhtml" className="p">The source code is available <a className="xref j-external-link" href="https://github.com/katalon-studio/katalon-mobile-automation" target="_blank">here</a>. For   further instructions and help, please refer to <a className="xref" href="/katalon-studio/keywords/keyword-description-in-katalon-studio/mobile-keywords/mobile-swipe">Mobile     Swipe</a> guideline and join us on <a className="xref j-external-link" href="http://forum.katalon.com/" target="_blank">Katalon Forum</a>.</p> 
