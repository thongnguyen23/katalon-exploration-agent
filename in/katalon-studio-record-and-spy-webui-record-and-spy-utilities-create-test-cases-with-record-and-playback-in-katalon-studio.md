---
hide_title: true
title: Create test cases with Record and Playback in Katalon Studio
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="concept-create-test-cases-record-playback" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Create test cases with Record and Playback in <span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon Studio</span> 

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Test recording is the easiest way for new automation testers to start learning test automation. Identifying objects on applications is time-consuming. The <a className="xref" href="/katalon-studio/record-and-spy/webui-record-and-spy-utilities/record-web-utility-in-katalon-studio">Web Recorder Utility</a> function captures your actions being performed on the application and converts them into executable code in the back-end.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">You can quickly automate a few functionalities of your app and save time by recording actions that have to be performed many times in iterative builds. This function supports recording and running the same tests on multiple browsers. This document shows you how to:</p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><a className="xref" href="#id_1">Record test with the Record Web function</a></li><li className="li"><a className="xref" href="#id_2">Rename Page Folders and Elements while runtime recording</a></li></ul> 

## <a id="id_1" class="anchor_top_offset"/>Record Test with the Record Web function

<p xmlns="http://www.w3.org/1999/xhtml" className="p"><strong className="ph b">Scenario:</strong> To make an appointment</p> 
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol"><li className="li">Launch the application under test (Example: <a className="xref j-external-link" href="http://demoaut.katalon.com/" target="_blank">http://demoaut.katalon.com/</a>)</li><li className="li">Click the <span className="ph uicontrol">Make Appointment</span> button</li><li className="li">Enter a valid username, password, and click <span className="ph uicontrol">Login</span> </li><li className="li">Make an appointment</li></ol> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Follow the below steps to get familiar with the Record &amp; Playback feature for Web UI tests</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><strong className="ph b">Step 1:</strong> Launch Katalon Studio and click <span className="ph uicontrol">New</span> &gt; <span className="ph uicontrol">Test Case</span> on the main toolbar. Provide a name for your test case and click <span className="ph uicontrol">OK</span>. An empty test case is created.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" width={500} src={useBaseUrl("/976efdb0-22b2-11ed-9930-0242fe3e4a3f/ks-840-new-test-case.png")} alt="Create a new test case in Katalon Studio." /></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><strong className="ph b">Step 2:</strong> Click <span className="ph uicontrol">Record Web</span> from the main toolbar.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" width={300} src={useBaseUrl("/976e6170-22b2-11ed-9930-0242fe3e4a3f/ks-840-record-web.png")} alt="The Record Web utility in Katalon Studio's main toolbar." /></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><strong className="ph b">Step 3:</strong> The <span className="ph uicontrol">Record</span> dialog displays.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" width={700} src={useBaseUrl("/d4eda8d0-6c72-11ed-a602-0242cfbc79b5/ks-855-recorder-dialog.png")} alt="The record web dialog in Katalon Studio." /></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><strong className="ph b">Step 4:</strong> Select a browser, then click <span className="ph uicontrol">Record</span> to start recording the test case.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" width={700} src={useBaseUrl("/d4e9d840-6c72-11ed-a602-0242cfbc79b5/ks-855-select-browser.png")} alt="Select your preferred browser in the web recorder menu." /></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><strong className="ph b">Step 5:</strong> Once your application has been launched, click on the <span className="ph uicontrol">Make Appointment</span> button. You are directed to the Login page.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" width={700} src={useBaseUrl("https://tw-cdn.katalon.com/katalon-studio/ks-make-appointment.png")} alt="Click on the make appointment button in the webpage." /></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><strong className="ph b">Step 6:</strong> Enter valid username and password (John Doe and ThisIsNotAPassword), then click <span className="ph uicontrol">Login</span>.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" width={600} src={useBaseUrl("/976bc960-22b2-11ed-9930-0242fe3e4a3f/ks-login.png")} alt="Enter the login credentials found at the top of the page." /></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><strong className="ph b">Step 7:</strong> Once the <span className="ph uicontrol">Make Appointment</span> page has been loaded, select the value <span className="ph uicontrol">Hongkong CURA Healthcare Center</span> from the Facility dropdown menu.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" width={500} src={useBaseUrl("/97725910-22b2-11ed-9930-0242fe3e4a3f/ks-set-facility.png")} alt="Select the value of the facility to Hongkong Cura Healthcare Center." /></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><strong className="ph b">Step 8:</strong> Select the <span className="ph uicontrol">Apply for hospital readmission</span> checkbox.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><strong className="ph b">Step 9:</strong> Then move the cursor to click on the <span className="ph uicontrol">Medicaid</span> checkbox.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><strong className="ph b">Step 10:</strong> Click the calendar icon next to <span className="ph uicontrol">Visit Date (Required)</span>. Select a date.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" width={600} src={useBaseUrl("/97742dd0-22b2-11ed-9930-0242fe3e4a3f/ks-set-date.png")} alt="Select a date for your appointment." /></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><strong className="ph b">Step 11:</strong> Enter text in the <span className="ph uicontrol">Comment</span> field.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><strong className="ph b">Step 12:</strong> Click <span className="ph uicontrol">Book Appointment</span>.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><strong className="ph b">Step 13:</strong> You can stop the recording anytime by clicking <span className="ph uicontrol">Stop</span>. You can select the <span className="ph uicontrol">Selection Method</span> for the captured objects. The <span className="ph uicontrol">Basic mode</span> is recommended to manual testers who have just started automated testing. With basic mode, Katalon Studio automatically generates robust and unique selectors for captured objects.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Advanced testers who want to manually input the selectors have the option to choose between <span className="ph uicontrol">CSS</span> and <span className="ph uicontrol">XPath</span> modes. For more details about <span className="ph uicontrol">Selection Method</span>, refer to <a className="xref" href="/katalon-studio/test-objects/web-test-objects/manage-web-test-objects">Manage Web Test Objects</a>.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" width={500} src={useBaseUrl("/976c65a0-22b2-11ed-9930-0242fe3e4a3f/ks-selection-method.png")} alt="Pick the selection method you want to use for your captured objects." /></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><strong className="ph b">Step 14:</strong> When you are done recording, click <span className="ph uicontrol">OK</span> to save the recorded actions into Katalon Studio.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">You are prompted to save captured objects to the <span className="ph uicontrol">Object Repository</span>, which can be reused whenever needed. You can also create a folder to maintain page objects in desired structure. Click <span className="ph uicontrol">OK</span> to continue.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" width={600} src={useBaseUrl("/97756650-22b2-11ed-9930-0242fe3e4a3f/ks-save-object.png")} alt="Add your element to the object repository." /></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Step 15:</strong> Recorded objects and actions are saved in the test case as shown below.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" width={700} src={useBaseUrl("/97731c60-22b2-11ed-9930-0242fe3e4a3f/ks-840-manual-script.png")} alt="Recorded objects and actions are saved in the test case." /></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Click <span className="ph uicontrol">Run</span> to execute recorded test cases in your desired browser.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><strong className="ph b">Script Code for Record and Playback</strong></p> 

```jsx
import static com.kms.katalon.core.testobject.ObjectRepository.findTestObject
import com.kms.katalon.core.webui.keyword.WebUiBuiltInKeywords as WebUI
 
WebUI.openBrowser('')
 
WebUI.navigateToUrl('http://demoaut.katalon.com/')
WebUI.click(findTestObject('Page_Home Page/button_Make Appointment'))
 
WebUI.click(findTestObject('Page_Login/button_Login'))
 
WebUI.closeBrowser()
```
## <a id="id_2" class="anchor_top_offset"/>Rename Page Folders and Elements while Recording

<p xmlns="http://www.w3.org/1999/xhtml" className="p">To organize your test scripts in page object pattern, you need to add test objects in the folder corresponding to the page. This action helps you reuse and maintain the objects.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><strong className="ph b">Scenario:</strong> Login with valid data</p> 
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol"><li className="li">Launch the application under test (Example: <a className="xref j-external-link" href="http://demoaut.katalon.com/" target="_blank">http://demoaut.katalon.com/</a>)</li><li className="li">Click the <span className="ph uicontrol">Make Appointment</span> button</li><li className="li">Enter a valid username, password, and click <span className="ph uicontrol">Login</span>   </li></ol> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><strong className="ph b">Step 1:</strong> Launch Katalon Studio and go to <span className="ph uicontrol">File</span> &gt; <span className="ph uicontrol">New</span> &gt; <span className="ph uicontrol">Test Case</span> on the main toolbar. Provide a name for your test case and click <span className="ph uicontrol">OK</span>. An empty test case is created.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" width={500} src={useBaseUrl("/9773b8a0-22b2-11ed-9930-0242fe3e4a3f/ks-840-change-element-name.png")} alt="Change element name in your test case." /></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Step 2:</strong> Click <span className="ph uicontrol">Record Web</span> on the main toolbar.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" width={300} src={useBaseUrl("/976e6170-22b2-11ed-9930-0242fe3e4a3f/ks-840-record-web.png")} alt="The record web toolbar in Katalon Studio." /></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><strong className="ph b">Step 3:</strong> The <span className="ph uicontrol">Record</span> dialog displays. Select a browser and click the <span className="ph uicontrol">Record</span> button to start recording the test case.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" width={700} src={useBaseUrl("/d4e9d840-6c72-11ed-a602-0242cfbc79b5/ks-855-select-browser.png")} alt="Select the browser you want to record in using the Web Recorder in Katalon Studio." /></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><strong className="ph b">Step 4:</strong> Once your application has been launched, click on the <span className="ph uicontrol">Make Appointment</span> button. You are directed to the <span className="ph uicontrol">Login</span> page.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><strong className="ph b">Step 5: </strong>Navigate back to the <span className="ph uicontrol">Web Recorder</span> window. Click <span className="ph uicontrol">expand.</span></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" src={useBaseUrl("/840deb50-9df0-11ed-998d-0242cfbc79b5/ks-expand-button-web-recorder.png")} alt="Expand the Web Recorder menu in Katalon Studio." /></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">By default, this will expand the menu downwards and show all recorded actions. </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><strong className="ph b">Step 6: </strong>Click on <span className="ph uicontrol">Show Captured Objects</span>. This will expand the <span className="ph uicontrol">Web Recorder</span> window again, this time to the right.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" src={useBaseUrl("/84036400-9df0-11ed-998d-0242cfbc79b5/ks_recorder_expanded_1.png")} alt="Click on Show Captured Objects to expand the Web Recorder window." /></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> If you cannot see the expanded window, drag the <span className="ph uicontrol">Web Recorder</span> window to the left until all elements are visible. It should look as below:</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" src={useBaseUrl("/84095770-9df0-11ed-998d-0242cfbc79b5/ks_recorder_expanded_2.png")} alt="The full Web Recorder window in Katalon Studio." /></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><strong className="ph b">Step 7: </strong>Go to the <span className="ph uicontrol">Captured Objects</span> window and click on "Page_CURA Healthcare Service". This will unfurl the toggle menu. It will go to "a_Make Appointment" by default.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" width={500} src={useBaseUrl("/976c65a0-22b2-11ed-9930-0242fe3e4a3f/ks-selection-method.png")} alt="Go to the Captured Objects window and unfurl the page." /></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Step 8:</strong> Rename the page name from "Page_CURA Healthcare Service" to "Page_Home Page."</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Step 9:</strong> In the <span className="ph uicontrol">Captured Objects</span> frame, select the <span className="ph uicontrol">a_Make Appointment</span> element.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Step 10:</strong> Rename the element name from "a_Make Appointment" to "button_Make Appointment."</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" width={500} src={useBaseUrl("/976b2d20-22b2-11ed-9930-0242fe3e4a3f/ks-840-captured-objects.png")} alt="Rename the a_Make Appointment button." /></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Step 11:</strong> Go back to the recording browser and continue to record. Click <span className="ph uicontrol">Login</span>.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" width={500} src={useBaseUrl("/976bc960-22b2-11ed-9930-0242fe3e4a3f/ks-login.png")} alt="Record logging in to the test website." /></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><strong className="ph b">Step 12:</strong> Repeat the same steps above to change the name of the object <strong className="ph b">Login</strong> and its folder.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><strong className="ph b">Step 13:</strong> You can stop recording by clicking <span className="ph uicontrol">Stop</span>. Click <span className="ph uicontrol">OK</span> to save recorded actions into Katalon Studio.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><strong className="ph b">Step 14:</strong> You are prompted to save the captured objects to <span className="ph uicontrol">Object Repository</span><strong className="ph b">,</strong> which can be reused whenever needed. You can also create a folder to maintain page objects in your desired structure. Click <span className="ph uicontrol">OK</span> to continue.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><strong className="ph b">Step 15:</strong> Recorded objects and actions are saved in the test case as shown below.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" width={600} src={useBaseUrl("/975de6b0-22b2-11ed-9930-0242fe3e4a3f/ks-840-test-case.png")} alt="Recorded objects and actions are saved in the test case as shown below." /></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Click <span className="ph uicontrol">Run</span> to execute the recorded test cases in your desired browser.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><strong className="ph b">Source Code:</strong></p> 

```jsx
import static com.kms.katalon.core.testobject.ObjectRepository.findTestObject
import com.kms.katalon.core.webui.keyword.WebUiBuiltInKeywords as WebUI
 
WebUI.openBrowser('')
 
WebUI.navigateToUrl('http://demoaut.katalon.com/')
WebUI.click(findTestObject('Page_Home Page/button_Make Appointment'))
 
WebUI.click(findTestObject('Page_Login/button_Login'))
 
WebUI.closeBrowser()
```

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Thus we can record the actions being performed using Katalon Studio. However, there are a few actions which cannot be recorded.</p> 

### <a id="id_3" class="anchor_top_offset"/>What cannot be recorded?

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Though recording your tests saves time, we cannot validate some   scenarios such as Web Table handling, switching to multiple frames,   switching to windows, handling captcha, image recognition, and   video playbacks.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">You can download the source code <a className="xref j-external-link" href="https://github.com/katalon-studio/katalon-web-automation" target="_blank">here</a>.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">For further instructions and help, you can refer to <a className="xref" href="/katalon-studio/record-and-spy/webui-record-and-spy-utilities/record-web-utility-in-katalon-studio">Recording WebUI Test</a>  tutorial.</p> 
