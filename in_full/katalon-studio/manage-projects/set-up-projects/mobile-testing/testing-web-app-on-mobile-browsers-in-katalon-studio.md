---
hide_title: true
title: Testing Web App on Mobile Browsers in Katalon Studio
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="id" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Testing Web App on Mobile Browsers in <span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon Studio</span> 

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Katalon Studio supports executing the same test cases on both desktop browsers and mobile browsers. A test case created via recording, either in manual mode or script mode, on a desktop browser with Katalon Studio can be executed on a mobile browser as well. This tutorial guides you step by step how to do that.</p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">Understand your web application under test (AUT)</li><li className="li">Create a test case with Katalon Studio</li><li className="li">Execute the test case with mobile browsers</li></ul> 

## Requirements

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">Katalon Studio: running on both Windows and macOS with a beta Linux support. Visit the <a className="xref j-external-link" href="https://www.katalon.com/download" target="_blank">Katalon Studio website</a> to get the latest version.</p></li><li className="li"><p className="p">Verify if your computer meets the <a className="xref j-external-link" href="https://docs.katalon.com/docs/general-information/supported-environments/supported-environments-for-katalon-studio-and-katalon-runtime-engine" target="_blank">System Requirements</a> of Katalon Studio.</p></li><li className="li"><p className="p">A Katalon account to activate this automation tool. If you don't have one, provide your desired username and password to sign up after launching the app.</p></li><li className="li"><p className="p">Check out <a className="xref j-external-link" href="https://docs.katalon.com/docs/get-started/onboarding-katalon-platform/quick-guide-for-testers" target="_blank">Quick Start</a> to familiarize yourself with Katalon Studio.</p></li></ul> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Web application testing can be directly executed on a mobile device. To do so, you need to connect your testing devices/emulators to a machine and run test scripts. Make sure Chrome and Safari applications are installed so that test steps can execute properly.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">It requires some knowledge of working with OS, Appium, and devices in use. Please refer to our Mobile Setup guide for <a className="xref" href="/katalon-studio/manage-projects/set-up-projects/mobile-testing/android/mobile-set-up-android-real-devices">Android</a> and <a className="xref" href="/katalon-studio/manage-projects/set-up-projects/mobile-testing/ios/mobile-set-up-ios-real-devices">iOS</a> for detailed instructions.</p> 

## <a id="id_2" class="anchor_top_offset"/>Understand your web application under test (AUT)

<p xmlns="http://www.w3.org/1999/xhtml" className="p">When a smartphone is a must-have for everyone, it is required for a web application to accommodate both desktop browsers and mobile browsers.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">​ ​Often, a desktop UI and a mobile web UI will vary for the same web application since the screen of a desktop is different from that of a phone (in resolution, size, and ratio, for example). Thus, a web application with responsive implementation can adapt to various devices, which might cause a problem during the quality assurance period. The same element on desktop implementation may have different locators on mobile, preventing test cases from executing correctly on mobile browsers.​ ​</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Do not stress out when your test cases cannot run properly on mobile browsers like desktop browsers. Automation testing is about understanding the AUT (Application Under Test) clearly to find a suitable approach. This practice should be a top priority before we want to continue testing our web application.</p> 
    

## <a id="id_3" class="anchor_top_offset"/>Create a test case with Katalon Studio

    
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">After understanding your AUT, and you have decided to perform   automation testing, let's create a test case with Katalon Studio.   Below is the test scenario and how to create the test case in   manual mode.</p> 
    
              
      

### <a id="id_4" class="anchor_top_offset"/>Scenario: Login

      
        
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Step 1: Launch Chrome browser on mobile.</p> 
        
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Step 2: Enter valid username and password.</p> 
        
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Step 3: Click on the login button.</p> 
        
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Step 4: Verify login is successful.</p> 
      
    

### <a id="id_5" class="anchor_top_offset"/>Manual Mode

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Step 1: Click on Add from Toolbar and select Web UI Keyword.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/running_application_mobile_browsers/web-ui-keyword.png")} width={250} alt="web UI keyword" /><br /><br /> </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Step 2: Select <em className="ph i">Open Browser</em> and pass the URL in the   input field. Call <em className="ph i">Wait for Page to Load</em> and provide a   timeout value in the input field.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Step 3: Add <em className="ph i">Wait for Element Visible</em> keyword for button   object "Make Appointment."</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Step 4: Before performing the click action, Verify whether the   element is clickable using <em className="ph i">Verify Element Clickable</em>   keyword, pass the object button "Make Appointment."</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Step 5: Call <em className="ph i">Click</em> action to be performed on the "Make   Appointment" button.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Step 6: <em className="ph i">Wait for Element Visible</em> "Login."</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Step 7: Add <em className="ph i">Verify Element Clickable</em> and pass the   object as the "Login" button.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Step 8: <em className="ph i">Set Text</em> for the username as "John Doe".</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Step 9:  <em className="ph i">Set Text</em> in the password as   "ThisIsNotAPassword".</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Step 10: Add <em className="ph i">Click</em> action to be performed on the Login   button.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Step 11: <em className="ph i">Wait for Element</em> present of text "Make   Appointment".</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Step12: Add <em className="ph i">Get Text</em> keyword to capture the Header   "Make Appointment" and store it in a variable called   "actual_Header".</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Step 13: Use the <em className="ph i">Verify Match</em> Keyword to verify the   actual and expected texts.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Step 14: Close the browser.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/running_application_mobile_browsers/830-test-steps.png")} width={850} alt="test steps" /><br /><br /> </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">You can also achieve the desired test case by using   <strong className="ph b">Script Mode</strong>.</p> 
      

### <a id="id_6" class="anchor_top_offset"/>Script Mode

      
                  
<pre xmlns="http://www.w3.org/1999/xhtml" className="pre codeblock"><code>import static com.kms.katalon.core.testobject.ObjectRepository.findTestObject{"\n"}import com.kms.katalon.core.model.FailureHandling as FailureHandling{"\n"}import com.kms.katalon.core.webui.keyword.WebUiBuiltInKeywords as WebUI{"\n"}{"\n"}'Launch Browser'{"\n"}WebUI.openBrowser('http://demoaut.katalon.com/'){"\n"}{"\n"}'Wait for Page Load'{"\n"}WebUI.waitForPageLoad(30){"\n"}{"\n"}'Wait for Element Visible of Button Make Appointment'{"\n"}WebUI.waitForElementVisible(findTestObject('Browser Application/button_Make Appointment'), 30){"\n"}{"\n"}'Verify Button Make Appointment is clickable or not'{"\n"}WebUI.verifyElementClickable(findTestObject('Browser Application/button_Make Appointment'), FailureHandling.STOP_ON_FAILURE){"\n"}{"\n"}'Click on Button Make Appointment'{"\n"}WebUI.click(findTestObject('Browser Application/button_Make Appointment')){"\n"}{"\n"}'Wait for text login Header '{"\n"}WebUI.waitForElementVisible(findTestObject('Browser Application/text_Login Header'), 30){"\n"}{"\n"}'Verify text login Header is in visible '{"\n"}WebUI.verifyElementVisible(findTestObject('Browser Application/text_Login Header')){"\n"}{"\n"}'Enter username as "John Doe"'{"\n"}WebUI.setText(findTestObject('Browser Application/txt_UserName'), 'John Doe'){"\n"}{"\n"}'Enter password as "ThisIsNotAPassword"'{"\n"}WebUI.setText(findTestObject('Browser Application/txt_Password'), 'ThisIsNotAPassword'){"\n"}{"\n"}'Click on Login Button'{"\n"}WebUI.click(findTestObject('Browser Application/button_Login')){"\n"}{"\n"}'Wait for Element Present of "Header Make Appointment"'{"\n"}WebUI.waitForElementPresent(findTestObject('Browser Application/text_Header Make Appointment'), 30){"\n"}{"\n"}'Get the Header text of Make Appointment and store in "actual_Header" variable'{"\n"}actual_Header = WebUI.getText(findTestObject('Browser Application/text_Header Make Appointment')){"\n"}{"\n"}'Verify the actual and Expected text'{"\n"}WebUI.verifyMatch(actual_Header, 'Make Appointment', false){"\n"}{"\n"}'Close the Browser'{"\n"}WebUI.closeBrowser(){"\n"}{"\n"}</code></pre> 
                
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Do not forget to execute the test case in Katalon Studio again   to ensure that it works properly.</p> 
      
    

## <a id="id_7" class="anchor_top_offset"/>Execute the test case with a mobile browser

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Double-check to ensure that the real device is connected, the   virtual device loaded, or cloud device connected successfully. From   Katalon Studio, select the test case and choose to execute with   Android/iOS as follows:</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/running_application_mobile_browsers/830-execution.png")} width={850} alt="execution" /><br /><br /> </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">It may take a while before the browser can be loaded into the   device.</p> 

## <a id="id_8" class="anchor_top_offset"/>Troubleshoot common errors

<p xmlns="http://www.w3.org/1999/xhtml" className="p">ChromeDriver related error:</p> 
<pre xmlns="http://www.w3.org/1999/xhtml" className="pre codeblock"><code>error: No Chromedriver found that can automate Chrome '&lt;chrome_version&gt;'{"\n"}</code></pre> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">To fix this issue, refer to: <a className="xref" href="/katalon-studio/troubleshooting/troubleshoot-mobile-automated-testing/no-chromedriver-found-that-can-automate-chrome-chrome_version">No Chromedriver found that can automate Chrome '&lt;chrome_version&gt;'</a></p> 
