---
hide_title: true
title: How to Perform Multi-touch Actions in Mobile App in Katalon Studio
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="id" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>How to Perform Multi-touch Actions in Mobile App in <span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon Studio</span> 

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Multi-touch action often appears in gaming applications. This   tutorial shows you how to perform a multi-touch action at four   different points simultaneously. We will use the <strong className="ph b">MultiTouch     Tester</strong> app to demonstrate automation testing on this   typical behavior. Please download:</p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">     <a className="xref j-external-link" href="https://play.google.com/store/apps/details?id=com.the511plus.MultiTouchTester" target="_blank">The       app</a>; or</li><li className="li">     <p className="p">       <a className="xref j-external-link" href="https://www.appsapk.com/multitouch-tester/" target="_blank">The direct         apk file</a>     </p>     <p className="p">       <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/handle_multi_touch_action/Handling-Multi-touch-Action.png")} alt="Handling Multi-touch Action in automation testing" /><br /><br />     </p>   </li></ul> 
    

## <a id="id_1" class="anchor_top_offset"/>In Manual Mode

    
      
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol">   <li className="li">Select <strong className="ph b">Start Application</strong> from mobile keyword     and click on <strong className="ph b">Input.</strong>   </li>   <li className="li">In the displayed dialogue, in <strong className="ph b">appFile</strong>, select     <strong className="ph b">Value Type</strong> as <strong className="ph b">Variable</strong> and in     <strong className="ph b">Value</strong> passing the variable name as     <strong className="ph b">path</strong>. <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/handle_multi_touch_action/Handling-Multi-touch-Action-1.png")} alt="Handling Multi-touch Action in automation testing" /><br /><br />   </li>   <li className="li">Add <strong className="ph b">Wait For Element Present</strong> item.</li>   <li className="li">Initialize Katalon Mobile Driver to Appium Driver</li>   <li className="li">Call the '<strong className="ph b">Get Device Height</strong>' method and     capture the height. Then store it in a variable     '<strong className="ph b">device_Height</strong>'.</li>   <li className="li">Call the '<strong className="ph b">Get Device Width</strong>' method and capture     the width. Then store it in a variable     '<strong className="ph b">device_Width</strong>'.</li>   <li className="li">Add <strong className="ph b">binary statement</strong> and get X, Y Coordinates     for touch action 1 (<strong className="ph b">top left</strong> side).</li>   <li className="li">Repeat step 6 for touch action 2 (<strong className="ph b">top right</strong>     side), touch action 3 (<strong className="ph b">bottom left</strong> side), and     touch action 4 (<strong className="ph b">bottom right</strong> side).</li>   <li className="li">Create an object of <strong className="ph b">MultiTouchAction</strong>     class.</li>   <li className="li">Set all four touch actions on given X, Y Coordinates of the     screen.</li>   <li className="li">Add a method call statement and press <strong className="ph b">first       action</strong> with X, Y coordinates and wait for 5 seconds then     release. Repeat for the three other actions.</li>   <li className="li">The final step is to add a method call statement and generate a     multi-touch action chain. <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/handle_multi_touch_action/Handling-Multi-touch-Action-2.png")} alt="Handling Multi-touch Action in automation testing" /><br /><br />   </li> </ol> 
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">As you can see from the step-by-step guide above, there are   repeated steps that would be easier to create in <strong className="ph b">Script     Mode</strong>. Thus, we suggest the users utilize this feature   where one can quickly automate the test scenario and easily manage   test scripts.</p> 
    
  
    

## <a id="id_2" class="anchor_top_offset"/>In Script Mode

```jsx
import static com.kms.katalon.core.testobject.ObjectRepository.findTestObject

import java.time.Duration
import com.kms.katalon.core.configuration.RunConfiguration as RunConfiguration
import com.kms.katalon.core.mobile.keyword.MobileBuiltInKeywords as Mobile
import com.kms.katalon.core.mobile.keyword.internal.MobileDriverFactory as MobileDriverFactory
import io.appium.java_client.AppiumDriver as AppiumDriver
import io.appium.java_client.MultiTouchAction as MultiTouchAction
import io.appium.java_client.TouchAction as TouchAction
import io.appium.java_client.touch.WaitOptions
import io.appium.java_client.touch.offset.PointOption

'Path of the Apk File Store in path variable'
def path = RunConfiguration.getProjectDir() + '/Data Files/MultiTouchTester.apk'

'Start the application'
Mobile.startApplication(path, false)

'Wait for Element Visible "Touch Me"'
Mobile.waitForElementPresent(findTestObject('MultiTouchTester/text_Touch Me'), 30)

'Verify Element Visible "Touch Me"'
Mobile.verifyElementVisible(findTestObject('MultiTouchTester/text_Touch Me'), 30)

'Initializing Katalon Mobile Driver to Appium Driver'
AppiumDriver<?> driver = MobileDriverFactory.getDriver()

'Get Device Height and store to "device_Height" variable'
device_Height = Mobile.getDeviceHeight()

'Get Device Width and store to "device_Width" variable'
device_Width = Mobile.getDeviceWidth()

'Get X1 coordinate of touchpoint 1 (Top Left Side)'
int X1 = device_Width * 0.20

'Get Y1 coordinate of touch action 1 (Top Left Side)'
int Y1 = device_Height * 0.20

'Get X2 coordinate of touchpoint 2 (Top Right Side)'
int X2 = device_Width * 0.80

'Get Y2 coordinate of touchpoint 2 (Top Right Side)'
int Y2 = device_Height * 0.20

'Get X3 coordinate of touchpoint 3 (Bottom Left Side)'
int X3 = device_Width * 0.20

'Get Y3 coordinate of touchpoint 3 (Bottom Left Side)'
int Y3 = device_Height * 0.80

'Get X4 coordinate of touchpoint 4 (Bottom Right Side)'
int X4 = device_Width * 0.80

'Get Y4 coordinate of touchpoint 4 (Bottom Right Side)'
int Y4 = device_Height * 0.80

'Create object to "MultiTouchAction" class '
MultiTouchAction multiTouch = new MultiTouchAction(driver)

'Create First action Object to "TouchAction" class'
TouchAction action1 = new TouchAction(driver)

'Create Second action Object to "TouchAction" class'
TouchAction action2 = new TouchAction(driver)

'Create Third action Object to "TouchAction" class'
TouchAction action3 = new TouchAction(driver)

'Create Fourth action Object to "TouchAction" class'
TouchAction action4 = new TouchAction(driver)

'Press First action with x y coordinates wait 5 Seconds then release'
action1.press(PointOption.point(X1, Y1)).waitAction(WaitOptions.waitOptions(Duration.ofMillis(5000))).release()

'Press Second action with x y coordinates wait 5 Seconds then release'
action2.press(PointOption.point(X2, Y2)).waitAction(WaitOptions.waitOptions(Duration.ofMillis(5000))).release()

'Press Third action with x y coordinates wait 5 Seconds then release'
action3.press(PointOption.point(X3, Y3)).waitAction(WaitOptions.waitOptions(Duration.ofMillis(5000))).release()

'Press Fourth action with x y coordinates wait 5 Seconds then release'
action4.press(PointOption.point(X4, Y4)).waitAction(WaitOptions.waitOptions(Duration.ofMillis(5000))).release()

'Multi Touch Object to add Multiple touch actions as per you need'
multiTouch.add(action1).add(action2).add(action3).add(action4).perform()
```          
  
