---
hide_title: true
title: Manage Mobile Test Objects in Katalon Studio
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="id" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Manage Mobile Test Objects in <span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon Studio</span> 


## <a id="id_2" class="anchor_top_offset"/>Create a Mobile Object

<p xmlns="http://www.w3.org/1999/xhtml" className="p">We recommend creating a Mobile object by using <a className="xref" href="/katalon-studio/record-and-spy/mobile-record-and-spy-utilities/spy-mobile-utility#task-1724">Katalon Mobile Spy</a> since the object locators are captured automatically for detecting objects during test execution.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">You can also create an object in Object Repository by right-click on <span className="ph uicontrol">Object Repository</span> and selecting <span className="ph uicontrol">New</span> &gt; <span className="ph uicontrol">Mobile Object</span>.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/mobile-selector-strategies/create-new-mobile-object.png")} /><br /><br /></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">The most important property of an object is its locator strategy and value. The locator should be unique in detecting that object. Select a locator strategy among the provided option and enter a locator.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Katalon Studio fully supports Appium selector strategies except for Android Data Matcher. See <a className="xref" href="/katalon-studio/test-objects/mobile-test-objects/locator-strategies-for-mobile-objects">Locator strategies for Mobile objects</a>.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/manage-mobile-test-object./object.png")} width={500} /><br /><br /></p> 

## <a id="id_3" class="anchor_top_offset"/>Validate Test Object on AUT

<p xmlns="http://www.w3.org/1999/xhtml" className="p">You can add test objects to <span className="ph uicontrol">Mobile Object Spy</span> to verify if the object can be detected successfully in the application under test. Refer to <a className="xref" href="/katalon-studio/record-and-spy/mobile-record-and-spy-utilities/spy-mobile-utility#task-1724">Spy Mobile Utility</a> for more details regarding how to validate captured objects against the application under test.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">To add an object to <span className="ph uicontrol">Mobile Object Spy</span>, right-click on the item to open its context menu and select the option.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" height={614} src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/manage-mobile-test-object./add-mobile.png")} width={350} /><br /><br /></p> 

## <a id="id_4" class="anchor_top_offset"/>Add an object property

<p xmlns="http://www.w3.org/1999/xhtml" className="p">You can add multiple object properties to the <span className="ph uicontrol">Object's Properties</span> table. Please note that object properties cannot share the same name in an object.</p> 
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol"><li className="li">In the <span className="ph uicontrol">Object's Properties</span> panel, click <span className="ph uicontrol">Add</span>.</li><li className="li">In the displayed <span className="ph uicontrol">Add property</span> dialog, specify the required information:</li></ol> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"> <strong className="ph b">Name</strong>: The object property's name. You can select one of the provided options (class, css, id, name, title, xpath) or enter a name manually.</li><li className="li"> <strong className="ph b">Match condition</strong>: The condition is used for detecting the target object during execution.</li><li className="li"> <strong className="ph b">Value</strong>: The value that completes a match condition.</li></ul> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">The new property is added to the properties list as configured above. You can also change the properties' values here.</p> 

## <a id="id_5" class="anchor_top_offset"/>In Script View

<p xmlns="http://www.w3.org/1999/xhtml" className="p"><strong className="ph b">Script View</strong> allows defining and handling <strong className="ph b">Test Objects</strong> programmatically. The following is a usage example demonstrating how to do that:</p> 
<img xmlns="http://www.w3.org/1999/xhtml" className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/manage-mobile-test-object./script-ex.png")} /> 
<br xmlns="http://www.w3.org/1999/xhtml" /> 
<br xmlns="http://www.w3.org/1999/xhtml" /> 
<pre xmlns="http://www.w3.org/1999/xhtml" className="pre codeblock"><code>import static com.kms.katalon.core.testobject.ObjectRepository.findTestObject{"\n"}import com.kms.katalon.core.testobject.MobileTestObject{"\n"}import com.kms.katalon.core.testobject.MobileTestObject.MobileLocatorStrategy{"\n"}{"\n"}// Find an object which was defined already in Object Repository{"\n"}myPredefinedObject = findTestObject('android.widget.TextView - App'){"\n"}{"\n"}// Create a new mobile object programmatically{"\n"}MobileTestObject mobileTestObject = new MobileTestObject("TestObjectID"){"\n"}mobileTestObject.setMobileLocatorStrategy(MobileLocatorStrategy.XPATH){"\n"}mobileTestObject.setMobileLocator("//android.widget.TextView[(text() = 'App' or . = 'App')]"){"\n"}</code></pre> 
