---
hide_title: true
title: Handling drag and drop testing for web applications with Katalon Studio
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="id" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Handling drag and drop testing for web applications with <span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon Studio</span> 

<div xmlns="http://www.w3.org/1999/xhtml" className="note important note_important"><span className="note__title">Important:</span> <ul className="ul"><li className="li">You need to install this <a className="xref j-external-link" href="https://store.katalon.com/product/70/DragAndDrop-Keywords" target="_blank">DragAndDrop Keywords</a> custom keyword plugin.</li></ul></div>
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Drag and drop is a fairly popular approach in modern websites to improve their overall UX. However, it could be very challenging to implement automation test for drag and drop components.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">In this tutorial, we will show how <span className="ph">Katalon Studio</span> is used to test the drag and drop feature in a web application.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">This tutorial assumes that you are familiar with the tool's basic features. To have a quick idea of how it works or to review the interface, refer to <a className="xref j-external-link" href="https://academy.katalon.com/courses/katalon-end-to-end-platform/" target="_blank">Kickstart your automation testing using Katalon Studio</a>.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">There are different common implementation methods for the drag and drop feature, which each needs to be addressed differently when testing, including:</p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">Using pure JavaScript to handle drag and drop with popular JavaScript frameworks like <a className="xref j-external-link" href="http://jqueryui.com/droppable/#default" target="_blank">jQuery</a>.</li><li className="li">Using HTML5 Drag and Drop, which is detailed in w3schools' HTML Drag and Drop tutorial.</li></ul> 

## <a id="id_1" class="anchor_top_offset"/>Create automation tests for JavaScript Drag and Drop

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Testing the pure JavaScript implemented drag and drop function   is quite straightforward with Katalon Studio as its built-in   keyword <a className="xref j-external-link" href="https://docs.katalon.com/katalon-studio/docs/webui-drag-and-drop-to-object.html" target="_blank"><strong className="ph b"><em className="ph i">dragAndDropObjectToObject</em></strong></a>   was designed to handle the JavaScript action natively.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">For this section, we will use the <a className="xref j-external-link" href="http://jqueryui.com/droppable/#default" target="_blank">jQuery Droppable     example page</a> as the application under test (AUT).</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/drag_drop_web_applications_katalon_studio/DragDrop1.png")} alt="Droppable Katalon Studio" /><br /><br /> </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">The example website provides a simple implementation of drag and   drop with a draggable object containing the text "Drag me to my   target" and a droppable object with the text "Drop here".</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">When the draggable object is dragged into the droppable object,   the target object's text will be changed to "Dropped!" like the   image below:</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/drag_drop_web_applications_katalon_studio/DragDrop2.png")} alt="Drag & Drop Katalon Studio 2" /><br /><br /> </p> 

We are going to test this behavior using Katalon Studio.

1. Create a Katalon project with the name ***DragAndDrop*** .
2. Open the [Object Spy](/katalon-studio/record-and-spy/webui-record-and-spy-utilities/spy-web-utility-in-katalon-studio) dialog, start a spy object session and navigate to the AUT website at http://jqueryui.com/droppable/#default.
3. Use the object spy utility to capture both the droppable object and the draggable object mentioned above and import them into the project's Object Repository. If you do it correctly, there will be 3 test objects as below in Object Repository and add navigation path:
    
    ![Highlight Object Repo folder](https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/drag_drop_web_applications_katalon_studio/DragDrop3.png)
    
    The name of each object is self-explanatory, except for the ***iframe*demo-frame_** object which is the parent iframe of both draggable and droppable objects. Now let's use those captured objects in a test script.
    
4. Create a test case named "jQuery Drag And Drop", open it, then change to Script mode and copy the following test scripts into it:

```jsx
import static com.kms.katalon.core.testobject.ObjectRepository.findTestObject
import com.kms.katalon.core.webui.keyword.WebUiBuiltInKeywords as WebUI

'Open the selected browser and navigate to our AUT website.'
WebUI.openBrowser('http://jqueryui.com/droppable/#default')

'Use the dragAndDropObjectToObject keyword to perform the drag and drop action.'
WebUI.dragAndDropToObject(findTestObject('Page_Droppable jQuery UI/div_draggable')findTestObject('Page_Droppable jQuery UI/div_droppable'))

'Get the text content of our droppable object.'
droppable_text = WebUI.getText(findTestObject('Page_Droppable jQuery UI/div_droppable'))

'Verify if it is actually changed to "Dropped!" because of the drag and drop action.'
WebUI.verifyEqual(droppable_text, 'Dropped!')

'Clean up the testing environment by closing the browser.'
WebUI.closeBrowser()
```
5. Run the test case and you will see that the executed test will pass effortlessly.

## <a id="id_2" class="anchor_top_offset"/>Create automation tests for HTML5 Drag and Drop

<p xmlns="http://www.w3.org/1999/xhtml" className="p">For this section, we will use the <a className="xref j-external-link" href="https://www.w3schools.com/html/html5_draganddrop.asp" target="_blank">w3school HTML5 Drag and Drop page</a> as the application under test (AUT):</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/drag_drop_web_applications_katalon_studio/w3school-HTML5-Drag-and-Drop-page.png")} /><br /><br /></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">This web page contains a simple implementation of drag and drop which allows you to simply drag the W3Schools.com image to change its container. After the W3Schools image is dragged and dropped to the right rectangle, it appears as below:</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/drag_drop_web_applications_katalon_studio/drag-and-drop-custom-keyword-for-HTML-Drag-and-Drop.png")} /><br /><br /></p> 

We will implement the drag and drop custom keyword for HTML Drag and Drop, then verify the inner HTML of the right rectangle when the drag and drop is completed.

Implementing an automation test for HTML5 Drag and Drop is a bit more complex than the JavaScript version. If you run the test case above to test this drag and drop feature, you will see that the draggable image does not move although the test passes.

This happens because as of the day of this article (May 22, 2017), Selenium still not provide official support for testing HTML5 Drag and Drop. You can follow the related Selenium issue [here](https://github.com/seleniumhq/selenium-google-code-issue-archive/issues/3604).

Therefore, as Katalon Studio utilizes Selenium for the automation execution, implementing the automated test for HTML5 Drag and Drop requires a little bit of workaround:

1. Capture the draggable and droppable objects into the project's repository like above. If done correctly we have 2 test objects as below:
    
    <img src="https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/drag_drop_web_applications_katalon_studio/DragDrop6.png" alt="Show Object Repo UI" />
    
    `img_drag1` is the identifier of the draggle image object, while `div_div2` identifies the destination rectangle element.
    
2. Create a package inside Keywords with the name ***dnd.***
3. Create a keyword class named ***DragAndDropHelper*** and open it. Copy the following scripts to create the custom keyword:

```jsx
package html5.dnd

import org.openqa.selenium.JavascriptExecutor
import org.openqa.selenium.WebDriver
import org.openqa.selenium.WebElement
import com.kms.katalon.core.annotation.Keyword
import com.kms.katalon.core.testobject.TestObject
import com.kms.katalon.core.webui.driver.DriverFactory
import com.kms.katalon.core.webui.keyword.WebUiBuiltInKeywords

public class DragAndDropHelper {

    private static String getJsDndHelper() {
        return '''
        function simulateDragDrop(sourceNode, destinationNode) {
            var EVENT_TYPES = {
                DRAG_END: 'dragend',
                DRAG_START: 'dragstart',
                DROP: 'drop'
            };

            function createCustomEvent(type) {
                var event = new CustomEvent("CustomEvent");
                event.initCustomEvent(type, true, true, null);
                event.dataTransfer = {
                    data: {},
                    setData: function(type, val) {
                        this.data[type] = val;
                    },
                    getData: function(type) {
                        return this.data[type];
                    }
                };
                return event;
            }

            function dispatchEvent(node, type, event) {
                if (node.dispatchEvent) {
                    return node.dispatchEvent(event);
                }
                if (node.fireEvent) {
                    return node.fireEvent("on" + type, event);
                }
            }

            var event = createCustomEvent(EVENT_TYPES.DRAG_START);
            dispatchEvent(sourceNode, EVENT_TYPES.DRAG_START, event);

            var dropEvent = createCustomEvent(EVENT_TYPES.DROP);
            dropEvent.dataTransfer = event.dataTransfer;
            dispatchEvent(destinationNode, EVENT_TYPES.DROP, dropEvent);

            var dragEndEvent = createCustomEvent(EVENT_TYPES.DRAG_END);
            dragEndEvent.dataTransfer = event.dataTransfer;
            dispatchEvent(sourceNode, EVENT_TYPES.DRAG_END, dragEndEvent);
        }
        ''';
    }

    @Keyword
    def dragAndDrop(TestObject sourceObject, TestObject destinationObject) {
        WebElement sourceElement = WebUiBuiltInKeywords.findWebElement(sourceObject);
        WebElement destinationElement = WebUiBuiltInKeywords.findWebElement(destinationObject);
        WebDriver webDriver = DriverFactory.getWebDriver();

        ((JavascriptExecutor) webDriver).executeScript(
            getJsDndHelper() + "simulateDragDrop(arguments[0], arguments[1]);",
            sourceElement, destinationElement
        );
    }
}
```
This keyword uses the JavaScript function from https://gist.github.com/druska/624501b7209a74040175 (thanks to [Druska](https://gist.github.com/druska)) to mimic HTML5 native events to simulate drag and drop for HTML5.

4. Use our newly created custom keyword. Create a test case with the name ***HTML5 Drag And Drop***, open it then changing to the Script mode and pasting the following Groovy code:
    
    ```jsx
    import static com.kms.katalon.core.testobject.ObjectRepository.findTestObject
    import com.kms.katalon.core.webui.keyword.WebUiBuiltInKeywords as WebUI
    
    'Open the selected browser and navigate to our AUT website'
    WebUI.openBrowser('https://www.w3schools.com/html/html5_draganddrop.asp')
    
    'Use the previous custom keywords to perform the drag and drop action.'
    CustomKeywords.'html5.dnd.DragAndDropHelper.dragAndDrop'(findTestObject('Page_HTML5 Drag and Drop/img_drag1'), findTestObject(
    'Page_HTML5 Drag and Drop/div_div2'))
    
    'Verify that the drag and drop action is performed successfully by checking the innerHTML of the destination element for the draggable image.'
    WebUI.verifyElementAttributeValue(findTestObject('Page_HTML5 Drag and Drop/div_div2'), 'innerHTML', '<img src="img_w3slogo.gif" draggable="true" ondragstart="drag(event)" id="drag1" alt="W3Schools">',
    0)
    
    'Close the browser to clean up the testing environment.'
    WebUI.closeBrowser();
    ```
    
    This sample project could be found [here](https://github.com/katalon-studio/DragAndDropExample).
    
5. Run the test case and you will notice that the W3Schools image is dragged and dropped in the right rectangle successfully.

We hope you enjoy the tutorial, please comment if you have any question or another solution to automate the drag & drop testing. For additional tip & tricks, access [Katalon Studio tutorial](https://forum.katalon.com/tags/c/community-discussion/katalon-studio/7/tips-tricks).
