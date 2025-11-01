---
hide_title: true
title: Handling iFrame issue with Katalon Studio
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="id" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Handling iFrame issue with <span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon Studio</span> 

<p xmlns="http://www.w3.org/1999/xhtml" className="p">A prevalent type of control used in a website is the HTML   iframe. And this control needs to be handled in a specific manner   when testing. An iframe (Inline Frame) is an HTML document embedded   in another HTML document. The iframe HTML element is often used to   insert the content from another source, such as an advertisement,   into a Web page.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Verifying text and objects within iframes can be a challenge.   For example, even though you can see a text displayed in an iframe,   automation tools may not be able to detect the text. You have to   tell your script how to traverse through a website's iframes   structure and select the correct iframe where the text and its   object are present. This article shows you how to handle iframes   properly in Katalon Studio.</p> 

## <a id="id_1" class="anchor_top_offset"/>How to identify an iframe

<p xmlns="http://www.w3.org/1999/xhtml" className="p">We can identify iframes in two ways:</p> 
      
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol">   <li className="li">Right-click on an element, if there is     a <strong className="ph b">tag</strong> name available     with <strong className="ph b">iframe</strong>, the element is said to be in a     frame.</li>   <li className="li">Right-click on a page, if there is an option available with the     following options in the context menu, the element is available in     frames.</li> </ol> 
      
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul">   <li className="li">View frame source</li>   <li className="li">Reload frame</li>   <li className="li">This frame</li> </ul> 
    
### <a id="id_2" class="anchor_top_offset"/>Usage example 1

<ol xmlns="http://www.w3.org/1999/xhtml" className="ol">   <li className="li">     <p className="p">Given that you want to capture the Comment text field of a       certain question in Katalon Forum (this text field is an iframe),       you can use the Web Object Spy of Katalon and see that it can       detect the iframe in the red highlighted area.</p>     <p className="p">       <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/handling_iframe_issue/Web-Object-Spy.png")} alt="iframe issue" /><br /><br />     </p>   </li>   <li className="li">     <p className="p">Once the Comment iframe is captured, Katalon shows all of its       child elements, which you can see in the Object Spy dialog.</p>   </li>   <li className="li">     <p className="p">As you save the captured object to Katalon Studio, its iframe is       also included. This is illustrated in the following screenshot:</p>     <p className="p">       <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/handling_iframe_issue/captured-object.png")} alt="Captured object to Katalon Studio" /><br /><br />     </p>   </li>   <li className="li">     <p className="p">Then, you can proceed to set the text to the Comment field by       specifying the child element for the Set Text keyword as described       below:</p>     <p className="p">       <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/handling_iframe_issue/Comment-field-1024x238.png")} alt="Set the text to the Comment field" /><br /><br />     </p>   </li> </ol> 
      
    

### <a id="id_3" class="anchor_top_offset"/>Usage example 2

<ol xmlns="http://www.w3.org/1999/xhtml" className="ol"><li className="li">     <p className="p">Given that you want to capture the JQueryUI's Drag and Drop       example (this draggable control is an iframe), as shown in the       screenshot below, you can drag the 'Drag me around' object to other       areas of the iframe.</p>     <p className="p">       <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/handling_iframe_issue/JQueryUIs-Drag-and-Drop.png")} alt="capture the JQueryUI's Drag and Drop example" /><br /><br />     </p>   </li><li className="li">     <p className="p">Use the Object Spy to capture the iframe as usual. The Object       Spy can detect, capture the iframe, and show all of the iframe's       elements accordingly.</p>   </li><li className="li">     <p className="p">As you save the captured object to Katalon Studio, the iframe is       also included as the object's parent element. This is illustrated       in the following screenshot (Note that you can uncheck the option       to use parent iframe if needed):</p>     <p className="p">       <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/handling_iframe_issue/objects-parent-element..png")} alt="save the captured object to Katalon Studio" /><br /><br />     </p>   </li><li className="li">     <p className="p">Given the situation where you opt not to specify the iframe       parent for an element, in order to interact with the element, you       need to use the <a className="xref" href="/katalon-studio/keywords/keyword-description-in-katalon-studio/web-ui-keywords/webui-switch-to-frame">Switch To Frame</a>       keyword to have Katalon focus on the parent iframe before being       able to interact with the element.</p>   </li></ol> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">The sample code below shows how to switch to the parent frame   before using the drag and drop action on the elements within the   iframe:</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/handling_iframe_issue/sample-code_drag_n_drop.png")} alt="how to switch to the parent frame before using the drag and drop action" /><br /><br /> </p> 

```jsx
import com.kms.katalon.core.annotation.SetUp as SetUp
import com.kms.katalon.core.annotation.TearDown as TearDown
import com.kms.katalon.core.model.FailureHandling as FailureHandling
import com.kms.katalon.core.testobject.ObjectRepository as ObjectRepository
import com.kms.katalon.core.mobile.keyword.MobileBuiltInKeywords as Mobile
import com.kms.katalon.core.webservice.keyword.WSBuiltInKeywords as WS
import static com.kms.katalon.core.testobject.ObjectRepository.findTestObject
import static com.kms.katalon.core.testdata.TestDataFactory.findTestData
import static com.kms.katalon.core.testcase.TestCaseFactory.findTestCase
import com.kms.katalon.core.testcase.TestCase as TestCase
import com.kms.katalon.core.testdata.TestData as TestData
import com.kms.katalon.core.testobject.TestObject as TestObject
import com.kms.katalon.core.webui.keyword.WebUiBuiltInKeywords as WebUiBuiltInKeywords
import com.kms.katalon.core.webui.keyword.WebUiBuiltInKeywords as WebUI
import internal.GlobalVariable as GlobalVariable

'Open a browser and navigate to jQuery UI page'
WebUI.openBrowser('http://jqueryui.com/')

'Maximize current browser window'
WebUI.maximizeWindow()

'Click on 'Draggle' link'
WebUI.click(findTestObject('Page_jQuery_Homepage/lnk_Draggable'))

'Switch to iframe of Demo panel'
WebUI.switchToFrame(findTestObject('Page_jQuery_Drag and Drop Example/ifr_Demo Frame'),GlobalVariable.G_Timeout_Small, FailureHandling.STOP_ON_FAILURE)

'Drag and drop iframe into other position'
WebUI.dragAndDropByOffset(findTestObject('Page_jQuery_Drag and Drop Example/div_Frame_Draggable'),200, 38)

'Switch back to current window'
WebUI.switchToDefaultContent()

'Click on 'Droppable' link'
WebUI.click(findTestObject('Page_jQuery_Homepage/lnk_Droppable'))

'Switch to iframe of Demo panel'
WebUI.switchToFrame(findTestObject('Page_jQuery_Drag and Drop Example/ifr_Demo Frame'),GlobalVariable.G_Timeout_Small, FailureHandling.STOP_ON_FAILURE)

'Drag the left rectangle and Drop it the right-side one'
WebUI.dragAndDropToObject(findTestObject('Page_jQuery_Drag and Drop Example/div_Frame_Draggable'),findTestObject('Page_jQuery_Drag and Drop Example/div_Frame_Droppable'), FailureHandling.STOP_ON_FAILURE)
WebUI.closeBrowser()
```
### <a id="id_4" class="anchor_top_offset"/>Usage example 3: Switch To Frame

<p xmlns="http://www.w3.org/1999/xhtml" className="p">We can switch to frames using the   <strong className="ph b">switchTo()</strong> method then perform the action on   that element. If we want to get a text in the Text Area,   then we cannot get it directly by taking the XPath of the element.   As it is available in the iframe we need to switch to the   frame first, and then we can get the element's text.</p> 
        
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <strong className="ph b">Manual Mode</strong> </p> 
        
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/handling_iframe_issue/switch-to-frame.png")} alt="switch to frame" /><br /><br /> </p> 
        
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <strong className="ph b">Script Mode</strong> </p> 
                  
```jsx
import static com.kms.katalon.core.testobject.ObjectRepository.findTestObject
import com.kms.katalon.core.webui.keyword.WebUiBuiltInKeywords as WebUI
 
'Launching and Navigating to URL'
WebUI.openBrowser('http://the-internet.herokuapp.com/iframe')

'Maximize the window'
WebUI.maximizeWindow()
 
'Switching to text area which is situated in Iframe'
WebUI.switchToFrame(findTestObject('Frames/textArea_Iframe'), 60)
WebUI.scrollToElement(findTestObject('Frames/TextArea'), 60)
 
'Fecthing the text from Text area and storing it in a variable'
Text = WebUI.getText(findTestObject('Frames/TextArea'))
 
'Verifying the Actual text with Expected text from Text Area.'
WebUI.verifyEqual(Text, 'Your content goes here.')
```             
:::info notes
Please download the source code [here](https://github.com/katalon-studio/katalon-web-automation) and get the HTML [here](https://github.com/katalon-studio/katalon-web-automation/blob/master/Html%20Files/How%20to%20Handle%20Frames.html).
:::
      
### <a id="id_5" class="anchor_top_offset"/>Usage example 4: Switch to Default Content

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Whenever we switch to frames to handle certain features, we must   switch back to the parent node to access other features of the   application. If we <strong className="ph b">do not</strong> switch back to   the parent node, then your code looks for the next locators within   that same frame itself.</p> 
        
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Switch used to switch back to the main window or parent window   frame.</p> 
        
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <strong className="ph b">Manual Mode</strong> </p> 
        
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/handling_iframe_issue/Switch-to-Default-Content.png")} alt="Switch to Default Content" /><br /><br /> </p> 
        
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <strong className="ph b">Script Mode</strong> </p> 

```jsx
import static com.kms.katalon.core.testobject.ObjectRepository.findTestObject
import com.kms.katalon.core.webui.keyword.WebUiBuiltInKeywords as WebUI
 
'Launching and Navigating to URL'
WebUI.openBrowser('http://the-internet.herokuapp.com/iframe')

'Maximize the window'
WebUI.maximizeWindow()
 
'Switching to text area which is situated in Iframe'
WebUI.switchToFrame(findTestObject('Frames/textArea_Iframe'), 60)
 
'Fecthing the text from Text area and storing it in a variable'
Text = WebUI.getText(findTestObject('Frames/TextArea'))
 
'Switching back to the main window or parent window frame'
WebUI.switchToDefaultContent()
 
'Verifying the Actual text with Expected text from Text Area.'
WebUI.verifyEqual(Text, 'Your content goes here.')
 
'Getting the text of the web element and storing it in a variable'
Heading = WebUI.getText(findTestObject('Frames/Frame Heading'))
 
'Verifying the Actual text with Expected text from Text Area.'
WebUI.verifyEqual(Heading, 'An iframe containing the TinyMCE WYSIWYG Editor')
```                
:::info notes
Please download the source code [here](https://github.com/katalon-studio/katalon-web-automation) and get the HTML [here](https://github.com/katalon-studio/katalon-web-automation/blob/master/Html%20Files/How%20to%20Handle%20Frames.html).
:::
      
### <a id="id_6" class="anchor_top_offset"/>Common exceptions

<p xmlns="http://www.w3.org/1999/xhtml" className="p">The <strong className="ph b">NoSuchFrameException</strong> or   <strong className="ph b">InvalidSwitchToTargetException</strong> exceptions are   thrown when the target frame to be switched to doesn't exist.</p> 
      
    
