---
hide_title: true
title: Handling Drag and Drop in Mobile App in Katalon Studio
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="id" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Handling Drag and Drop in Mobile App in <span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon Studio</span> 

<p xmlns="http://www.w3.org/1999/xhtml" className="p">In this tutorial, we will see how to handle drag and drop action   in a mobile application using Katalon Studio. The source code can   be downloaded <a className="xref j-external-link" href="https://github.com/katalon-studio/katalon-mobile-automation/blob/master/Data%20Files/Drag%20and%20Drop.apk" target="_blank">here</a>.</p> 

## <a id="id_1" class="anchor_top_offset"/>Scenario
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">The scenario is to <strong className="ph b">drag and drop</strong> a draggable   object containing the text "<strong className="ph b">Brad Mehldau</strong>" and a   droppable object containing the text "<strong className="ph b">Kurt     Rosenwinkel</strong>".</p> 
      
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul">   <li className="li">Step 1: Start the Application (<strong className="ph b">Drag and       Drop.apk</strong>)</li>   <li className="li">Step 2: Tap on <strong className="ph b">Basic Usage playground</strong>     text</li>   <li className="li">Step 3: Drag <strong className="ph b">Brad Mehldau</strong> text to drop at     <strong className="ph b">Kurt Rosenwinkel</strong> text</li> </ul> 

## <a id="id_2" class="anchor_top_offset"/>Manual Mode

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">Step 1: Select <strong className="ph b">Start       Application</strong> from mobile keyword and click on     <strong className="ph b">Input</strong> to open a new dialogue. In     <strong className="ph b">appFile</strong>, select '<strong className="ph b">Value Type</strong>' as     <strong className="ph b">Variable</strong>. In <strong className="ph b">Value</strong>, pass the     variable name as '<strong className="ph b">path'</strong>.</li></ul> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/handle_drag_drop_mobile_app/Handling-Drag-and-Drop-in-Mobile-App.png")} alt="Handling Drag and Drop in Mobile App" /><br /><br /> </p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">Step 2: Add a <strong className="ph b">Wait For Element Present</strong> item to     wait for Basic Usage playground to pop up.</li><li className="li">Step 3: Select <strong className="ph b">Tap</strong> from mobile keyword and     pass the object of Basic Usage playground.</li><li className="li">Step 4: Similarly, add a <strong className="ph b">Wait For Element       Present</strong> item to wait for the 'Brad Mehldau' text.</li><li className="li">Step 5: Select the <strong className="ph b">DragAndDrop</strong>     <strong className="ph b">keyword</strong> to perform the drag and drop action.</li><li className="li">Step 6: The draggable object will be dragged into the droppable     object.</li></ul> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/handle_drag_drop_mobile_app/Handling-Drag-and-Drop-in-Mobile-App-6.png")} alt="Handling Drag and Drop in Mobile App" /><br /><br /> </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">You can utilize our <strong className="ph b">Script</strong> feature to automate   the test.</p> 

## <a id="id_3" class="anchor_top_offset"/>Script Mode

```jsx
import static com.kms.katalon.core.testobject.ObjectRepository.findTestObject
import com.kms.katalon.core.configuration.RunConfiguration as RunConfiguration
import com.kms.katalon.core.mobile.keyword.MobileBuiltInKeywords as Mobile
import com.kms.katalon.core.model.FailureHandling as FailureHandling
 
'Path of the Apk File Store in path variable'
def path = RunConfiguration.getProjectDir() + '/Data Files/Drag and Drop.apk'
 
'Start the Application'
Mobile.startApplication(path, false)
  
'Wait for Element Present of text "Basic Usage playground"'
Mobile.waitForElementPresent(findTestObject('Drag Sort Demos/Handle Drag and Drop/text_Basic Usage playground'), 30)
 
'Verify Element visible of "Basic Usage playground"'
Mobile.verifyElementVisible(findTestObject('Drag Sort Demos/Handle Drag and Drop/text_Basic Usage playground'), 30)
 
'Tap on "Basic Usage playground"'
Mobile.tap(findTestObject('Drag Sort Demos/Handle Drag and Drop/text_Basic Usage playground'), 30)
  
'Wait for Element Present of "Brad Mehldau"'
Mobile.waitForElementPresent(findTestObject('Drag Sort Demos/Handle Drag and Drop/text_Brad Mehldau'), 30)
 
'Verify Element visible of "Brad Mehldau"'
Mobile.verifyElementVisible(findTestObject('Drag Sort Demos/Handle Drag and Drop/text_Brad Mehldau'), 30)
 
'Use the dragAndDrop keyword to perform the drag and drop action.'
Mobile.dragAndDrop(findTestObject('Drag Sort Demos/Handle Drag and Drop/text_Brad Mehldau'), findTestObject('Drag Sort Demos/Handle Drag and Drop/text_Kurt Rosenwinkel'), 30)

Mobile.delay(50, FailureHandling.STOP_ON_FAILURE)
Mobile.closeApplication()
```