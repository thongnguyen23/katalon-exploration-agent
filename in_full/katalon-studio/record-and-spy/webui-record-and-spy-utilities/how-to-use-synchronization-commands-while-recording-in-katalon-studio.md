---
hide_title: true
title: How to use synchronization commands while recording in Katalon Studio
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="id_synchronization_commands_recording" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>How to use synchronization commands while recording in <span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon Studio</span> 


## <a id="id_1" class="anchor_top_offset"/>What is Synchronization?

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Synchronization is a mechanism which allows multiple threads to work in parallel. In test automation, the application under test (AUT) and the automation tool we employ should collaborate to progress the test execution. In order to achieve this and avoid execution failures, we need to use synchronization commands. This tutorial shows you how to do just that.</p> 

### <a id="id_2" class="anchor_top_offset"/>Scenario: Login with valid credentials

<ol xmlns="http://www.w3.org/1999/xhtml" className="ol"><li className="li">Launch the application under test with this sample URL: <span className="ph">http://demoaut.katalon.com/</span></li><li className="li">Use <span className="ph uicontrol">Wait For Page Load</span> keyword</li><li className="li">Use <span className="ph uicontrol">Wait For Element Visible</span> keyword for Make Appointment button</li><li className="li">Click on Make Appointment</li><li className="li">Use <span className="ph uicontrol">Wait For Element Visible</span> for Login button</li><li className="li">Enter a valid username and password, then click on the Login button</li></ol> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">At runtime recording, we can add synchronization commands to wait for page load, wait for element present, wait for element visible, etc. </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><strong className="ph b">Step 1:</strong> Launch Katalon Studio and click on the <span className="ph uicontrol">Create New Test Case</span> button from the main toolbar. Provide a name for your test case and click <span className="ph uicontrol">OK</span>. An empty test case is created.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" width={500} src={useBaseUrl("/97b136d0-22b2-11ed-9930-0242fe3e4a3f/ks-create-a-new-test-case.png")} alt="create a new test case" /></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><strong className="ph b">Step 2:</strong> Click on <span className="ph uicontrol">Record Web</span> from the main toolbar.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" width={350} src={useBaseUrl("/97b0c1a0-22b2-11ed-9930-0242fe3e4a3f/ks-840-record-web.png")} alt="record web" /></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><strong className="ph b">Step 3:</strong> The <span className="ph uicontrol">Record</span> dialog displays, where recorded actions show.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> Provide the URL of the application under test.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" width={700} src={useBaseUrl("/d4eda8d0-6c72-11ed-a602-0242cfbc79b5/ks-855-recorder-dialog.png")} alt="record web" /></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><strong className="ph b">Step 4:</strong> Select a browser and click on the <span className="ph uicontrol">Record</span> button to start recording the test case</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" width={600} src={useBaseUrl("/d4e9d840-6c72-11ed-a602-0242cfbc79b5/ks-855-select-browser.png")} alt="select browser" /></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><strong className="ph b">Step 5:</strong> Once your application is launched, move the cursor to <span className="ph uicontrol">Make Appointment</span> and click on the button. You need to wait for the login page to load.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" width={700} src={useBaseUrl("https://tw-cdn.katalon.com/katalon-studio/ks-make-appointment.png")} alt="make appointment" /></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><strong className="ph b">Step 6:</strong> You can add synchronization commands in runtime recording in the <span className="ph uicontrol">Recorded Actions</span> pane. Select a step at which the synchronization commands will be added. Click on <span className="ph uicontrol">Add</span>.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" width={700} src={useBaseUrl("/cb23d060-750d-11ed-a602-0242cfbc79b5/ks-855-add-kw.png")} alt="add" /></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><strong className="ph b">Step 7:</strong> Double-click on the newly added keyword and type <span className="ph uicontrol">Wait For Page Load</span> keyword. Then, double click on the <span className="ph uicontrol">Input</span> cell and set the value to 45 seconds.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" width={700} src={useBaseUrl("/ca84f850-750d-11ed-a602-0242cfbc79b5/ks-855-wait-for-page-load-kw.png")} alt="add input" /></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> Now Katalon Studio will wait 45 seconds for the page to get fully loaded to execute the next command. These synchronization commands avoid execution failures.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" width={700} src={useBaseUrl("/cb207500-750d-11ed-a602-0242cfbc79b5/ks-855-wait-kw.png")} alt="wait for page load" /></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">You can pause and resume the recording whenever you need it. Let us continue with recording a few more actions. Switch to the browser in which you are recording, move to <span className="ph uicontrol">Make Appointment</span> button and click on <span className="ph uicontrol">Make Appointment</span> button.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><strong className="ph b">Step 8:</strong> Now to wait for a specific element to be loaded and to perform an action, we need to add the <span className="ph uicontrol">Wait for Element Present</span> command before clicking on the <span className="ph uicontrol">Make Appointment</span> button.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">To do so, right click on the element, then choose <span className="ph uicontrol">Katalon Studio</span> &gt; <span className="ph uicontrol">Wait For Element Present</span>.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" width={700} src={useBaseUrl("/97a21ba0-22b2-11ed-9930-0242fe3e4a3f/ks-wait-for-element-present.png")} alt="add wait keyword" /></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">So here, we have added two wait commands, one is to wait till the page gets loaded and other is to wait till the element gets displayed<strong className="ph b">.</strong> The reason behind adding these keywords is that, even though the page has been loaded, sometimes elements will not be present in the DOM (referring to Ajax-based applications mainly).</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><strong className="ph b">Step 9:</strong> We need to provide the expected time as an input for all the wait commands. Tap on the <span className="ph uicontrol">Wait For Element Present</span> step and provide 15 seconds as the expected time interval.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" width={600} src={useBaseUrl("/cae4cb90-750d-11ed-a602-0242cfbc79b5/ks-wait-15.png")} alt="add wait for element present" /></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><strong className="ph b">Step 10:</strong> You can also add the <span className="ph uicontrol">Wait For Element Visible</span> command on the <span className="ph uicontrol">Login</span> button. Once you are done, click on <span className="ph uicontrol">Stop</span> and save the recorded actions into Katalon Studio. You are prompted to save captured objects into the <span className="ph uicontrol">Object Repository</span>, which can be reused whenever needed<strong className="ph b">.</strong> You can also create a folder to maintain page objects in desired structure.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Your recorded test script should be as shown below.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" width={600} src={useBaseUrl("/cc00e9f0-750d-11ed-a602-0242cfbc79b5/ks-recorded-test-case.png")} alt="test case" /></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Click on <span className="ph uicontrol">Script</span> tab to view the generated code. You can also modify the script from the script mode. All the recorded actions can be modified in script mode.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><strong className="ph b">Script code:</strong></p> 

```jsx
WebUI.openBrowser('')
WebUI.navigateToUrl('http://demoaut.katalon.com/')
WebUI.waitForPageLoad(45)
 
WebUI.waitForElementPresent(findTestObject('Page_CURA Healthcare Service/a_Make Appointment'), 15)
 
WebUI.click(findTestObject('Page_CURA Healthcare Service/a_Make Appointment'))
 
WebUI.waitForElementVisible(findTestObject('Page_CURA Healthcare Service (1)/button_Login'), 45)
 
WebUI.click(findTestObject('Page_CURA Healthcare Service (1)/button_Login'))
 
WebUI.closeBrowser()
```

<p xmlns="http://www.w3.org/1999/xhtml" className="p">It is recommended to add synchronization while recording automation test cases in the <a className="xref" href="/katalon-studio/create-test-cases/generate-test-steps-in-katalon-studio-manual-view">manual mode</a> or <a className="xref" href="/katalon-studio/create-test-cases/generate-test-steps-in-katalon-studio-script-view">script mode</a>. It is also a good practice to use wait commands to avoid execution failures. Download source code <a className="xref j-external-link" href="https://github.com/katalon-studio/katalon-web-automation" target="_blank">here</a>.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">For further instructions and help, you can refer to <a className="xref" href="/katalon-studio/create-test-cases/create-test-case-overview">Recording WebUI Test</a> tutorial.</p> 
