---
hide_title: true
title: Selenese (Selenium IDE) Commands Reference
---

# <a id="id" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Selenese (Selenium IDE) Commands Reference

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Katalon Automation Recorder provides various Selenium Commands (Selenese) to help automate web application testing. These commands stimulate actions on the application under test (AUT) and create automation test scripts.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">The below table is the list of all supported Selenese Commands.</p> 

## addLocationStrategy

<p xmlns="http://www.w3.org/1999/xhtml" className="p">addLocationStrategy(strategyName, functionDefinition)</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments:</strong>                          </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">strategyName - the name of the strategy to define; this should use only letters [a-zA-Z] with no spaces or other punctuation.</p> 
<div xmlns="http://www.w3.org/1999/xhtml" className="p"> functionDefinition - a string defining the body of a function in JavaScript. For example: <pre className="pre codeblock"><code>return inDocument.getElementById(locator);</code></pre>                          </div>
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> Defines a new function for Selenium to locate elements on the page. For example, if you define the strategy "foo", and someone runs click("foo=blah"), we'll run your function, passing you the string "blah", and click on the element that your function returns, or throw an "Element not found" error if your function returns null. We'll pass three arguments to your function:</p> 
<div xmlns="http://www.w3.org/1999/xhtml" className="p"><ul className="ul"><li className="li">locator: the string the user passed in</li><li className="li">inWindow: the currently selected window</li><li className="li">inDocument: the currently selected document</li></ul> The function must return null if the element can't be found.</div>
                    

## addLocationStrategyAndWait

<p xmlns="http://www.w3.org/1999/xhtml" className="p">addLocationStrategyAndWait(strategyName, functionDefinition)</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> Generated from addLocationStrategy(strategyName, functionDefinition)</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments:</strong>                          </p> 
<div xmlns="http://www.w3.org/1999/xhtml" className="p"><ul className="ul"><li className="li">strategyName - the name of the strategy to define; this should use only letters [a-zA-Z] with no spaces or other punctuation.</li><li className="li">functionDefinition - a string defining the body of a function in JavaScript. For example: <pre className="pre codeblock"><code>return inDocument.getElementById(locator);</code></pre>                              </li></ul> Defines a new function for Selenium to locate elements on the page. For example, if you define the strategy "foo", and someone runs click("foo=blah"), we'll run your function, passing you the string "blah", and click on the element that your function returns, or throw an "Element not found" error if your function returns null. We'll pass three arguments to your function: <ul className="ul"><li className="li">locator: the string the user passed in</li><li className="li">inWindow: the currently selected window</li><li className="li">inDocument: the currently selected document</li></ul> The function must return null if the element can't be found.</div>
                    

## addScript

                            
<p xmlns="http://www.w3.org/1999/xhtml" className="p">addScript(scriptContent, scriptTagId)</p> 
                            
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments:</strong>                          </p> 
                            
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> *scriptcontent - the Javascript content of the script to add</p> 
                            
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> *scriptTagId - (optional) the id of the new script tag. If specified, and an element with this id already exists, this operation will fail.</p> 
                            
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Loads script content into a new script tag in the Selenium document. This differs from the runScript command in that runScript adds the script tag to the document of the AUT, not the Selenium document. The following entities in the script content are replaced by the characters they represent: &lt; &gt; &amp; The corresponding remove command is removeScript.</p> 
                                            

## addScriptAndWait

<p xmlns="http://www.w3.org/1999/xhtml" className="p">addScriptAndWait(scriptContent, scriptTagId) Generated from addScript(scriptContent, scriptTagId</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*scriptContent - the Javascript content of the script to add *scriptTagId - (optional) the id of the new script tag. If specified, and an element with this id already exists, this operation will fail. Loads script content into a new script tag in the Selenium document. This differs from the runScript command in that runScript adds the script tag to the document of the AUT, not the Selenium document. The following entities in the script content are replaced by the characters they represent: &lt; &gt; &amp; The corresponding remove command is removeScript.</p> 
                    

## addSelection

<p xmlns="http://www.w3.org/1999/xhtml" className="p">addSelection(locator, optionLocator</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 *locator - an element locator identifying a multi-select box *optionLocator - an option locator (a label by default) 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Add a selection to the set of selected options in a multi-select element using an option locator. @see #doSelect for details of option locators</p> 
                                            

## addSelectionAndWait

<p xmlns="http://www.w3.org/1999/xhtml" className="p">addSelectionAndWait(locator, optionLocator)</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> Generated from addSelection(locator, optionLocator</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 *locator - an element locator identifying a multi-select box *optionLocator - an option locator (a label by default) 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Add a selection to the set of selected options in a multi-select element using an option locator. @see #doSelect for details of option locators</p> 
                                            

## ajaxWait

<p xmlns="http://www.w3.org/1999/xhtml" className="p">ajaxWait</p> 
                    

## ajaxWaitAndWait

<p xmlns="http://www.w3.org/1999/xhtml" className="p">ajaxWaitAndWait</p> 
                    

## allowNativeXpath

<p xmlns="http://www.w3.org/1999/xhtml" className="p">allowNativeXpath(allow</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 *allow - boolean, true means we'll prefer to use native XPath; false means we'll only use JS XPath 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Specifies whether Selenium should use the native in-browser implementation of XPath (if any native version is available); if you pass "false" to this function, we will always use our pure-JavaScript xpath library. Using the pure-JS xpath library can improve the consistency of xpath element locators between different browser vendors, but the pure-JS version is much slower than the native implementations.</p> 
                                            

## allowNativeXpathAndWait

<p xmlns="http://www.w3.org/1999/xhtml" className="p">allowNativeXpathAndWait(allow)</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> Generated from allowNativeXpath(allow</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 *allow - boolean, true means we'll prefer to use native XPath; false means we'll only use JS XPath 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Specifies whether Selenium should use the native in-browser implementation of XPath (if any native version is available); if you pass "false" to this function, we will always use our pure-JavaScript xpath library. Using the pure-JS xpath library can improve the consistency of xpath element locators between different browser vendors, but the pure-JS version is much slower than the native implementations.</p> 
                                            

## altKeyDown

                            
<p xmlns="http://www.w3.org/1999/xhtml" className="p">altKeyDown()</p> 
                            
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Press the alt key and hold it down until doAltUp() is called or a new page is loaded.</p> 
                                            

## altKeyDownAndWait

                            
<p xmlns="http://www.w3.org/1999/xhtml" className="p">altKeyDownAndWait() Generated from altKeyDown()</p> 
                            
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Press the alt key and hold it down until doAltUp() is called or a new page is loaded.</p> 
                                            

## altKeyUp

                            
<p xmlns="http://www.w3.org/1999/xhtml" className="p">altKeyUp()</p> 
                            
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Release the alt key.</p> 
                                            

## altKeyUpAndWait

                            
<p xmlns="http://www.w3.org/1999/xhtml" className="p">altKeyUpAndWait()</p> 
                            
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Generated from altKeyUp()</p> 
                            
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Release the alt key.</p> 
                                            

## answerOnNextPrompt

<p xmlns="http://www.w3.org/1999/xhtml" className="p">answerOnNextPrompt(answer</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*answer - the answer to give in response to the prompt pop-up Instructs Selenium to return the specified answer string in response to the next JavaScript prompt [window.prompt()].</p> 
                    

## assertAlert

                            
<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertAlert(pattern)</p> 
                            
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> Generated from getAlert().</p> 
                            
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> Returns: The message of the most recent JavaScript alert </p> 
                            
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Retrieves the message of a JavaScript alert generated during the previous action, or fail if there were no alerts.</p> 
                            
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Getting an alert has the same effect as manually clicking OK. If an alert is generated but you do not consume it with getAlert, the next Selenium action will fail.</p> 
                            
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Under Selenium, JavaScript alerts will NOT pop up a visible alert dialog.</p> 
                            
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Selenium does NOT support JavaScript alerts that are generated in a page's onload() event handler. In this case, a visible dialog WILL be generated and Selenium will hang until someone manually clicks OK.</p> 
                                            

## assertAlertAndWait

                            
<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertAlertAndWait(pattern)</p> 
                            
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> Generated from getAlert().</p> 
                            
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> Returns: The message of the most recent JavaScript alert </p> 
                            
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Retrieves the message of a JavaScript alert generated during the previous action, or fail if there were no alerts.</p> 
                            
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Getting an alert has the same effect as manually clicking OK. If an alert is generated but you do not consume it with getAlert, the next Selenium action will fail.</p> 
                            
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Under Selenium, JavaScript alerts will NOT pop up a visible alert dialog.</p> 
                            
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Selenium does NOT support JavaScript alerts that are generated in a page's onload() event handler. In this case a visible dialog WILL be generated and Selenium will hang until someone manually clicks OK.</p> 
                                            

## assertAlertNotPresent

                            
<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertAlertNotPresent()</p> 
                            
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> Generated from isAlertPresent().</p> 
                            
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> Returns: true if there is an alert </p> 
                            
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Has an alert occurred?</p> 
                            
<p xmlns="http://www.w3.org/1999/xhtml" className="p">This function never throws an exception</p> 
                                            

## assertAlertPresent

                            
<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertAlertPresent()</p> 
                            
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> Generated from isAlertPresent().</p> 
                            
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> Returns: true if there is an alert </p> 
                            
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Has an alert occurred?</p> 
                            
<p xmlns="http://www.w3.org/1999/xhtml" className="p">This function never throws an exception</p> 
                                            

## assertAllButtons

                            
<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertAllButtons(pattern)</p> 
                            
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> Generated from getAllButtons().</p> 
                            
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> Returns: the IDs of all buttons on the page</p> 
                            
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Returns the IDs of all buttons on the page.</p> 
                            
<p xmlns="http://www.w3.org/1999/xhtml" className="p">If a given button has no ID, it will appear as "" in this array.</p> 
                                            

## assertAllFields

<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertAllFields(pattern) Generated from getAllFields(). Returns: the IDs of all field on the page</p> 
                     

## assertAllLinks

<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertAllLinks(pattern) Generated from getAllLinks(). Returns: the IDs of all links on the page</p> 
                     

## assertAllWindowIds

<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertAllWindowIds(pattern) Generated from getAllWindowIds(). Returns: Array of identifiers of all windows that the browser knows about.</p> 
                     

## assertAllWindowNames

<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertAllWindowNames(pattern) Generated from getAllWindowNames(). Returns: Array of names of all windows that the browser knows about.</p> 
                     

## assertAllWindowTitles

<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertAllWindowTitles(pattern) Generated from getAllWindowTitles(). Returns: Array of titles of all windows that the browser knows about.</p> 
                     

## assertAttribute

<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertAttribute(attributeLocator, pattern) Generated from getAttribute(attributeLocator) Arguments: *attributeLocator - an element locator followed by an @ sign and then the name of the attribute, e.g. "foo@bar" . Returns: the value of the specified attr</p> 
                    

## assertAttributeFromAllWindows

<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertAttributeFromAllWindows(attributeName, pattern) Generated from getAttributeFromAllWindows(attributeName</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*attributeName - name of an attribute on the windows . Returns: the set of values of this attribute from all known windows.</p> 
                     

## assertBodyText

<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertBodyText(pattern) Generated from getBodyText(). Returns: the entire text of the page</p> 
                     

## assertChecked

<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertChecked(locator) Generated from isChecked(locator</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator pointing to a checkbox or radio button . Returns: true if the checkbox is checked, false otherwise</p> 
                     

## assertConfirmation

<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertConfirmation(pattern) Generated from getConfirmation(). Returns: the message of the most recent JavaScript confirmation dialog</p> 
                     

## assertConfirmationAndWait

<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertConfirmationAndWait(pattern) Generated from getConfirmation(). Returns: the message of the most recent JavaScript confirmation dialog</p> 
                     

## assertConfirmationNotPresent

<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertConfirmationNotPresent() Generated from isConfirmationPresent(). Returns: true if there is a pending confirmation</p> 
                     

## assertConfirmationPresent

<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertConfirmationPresent() Generated from isConfirmationPresent(). Returns: true if there is a pending confirmation</p> 
                     

## assertCookie

<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertCookie(pattern) Generated from getCookie(). Returns: all cookies of the current page under test</p> 
                     

## assertCookieByName

<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertCookieByName(name, pattern) Generated from getCookieByName(name</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*name - the name of the cookie. Returns: the value of the cookie</p> 
                     

## assertCookieNotPresent

<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertCookieNotPresent(name) Generated from isCookiePresent(name</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*name - the name of the cookie. Returns: true if a cookie with the specified name is present, or false otherwise.</p> 
                     

## assertCookiePresent

<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertCookiePresent(name) Generated from isCookiePresent(name</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*name - the name of the cookie . Returns: true if a cookie with the specified name is present, or false otherwise.</p> 
                     

## assertCssCount

<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertCssCount(css, pattern) Generated from getCssCount(css</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*css - the css selector to evaluate. do NOT wrap this expression in a 'count()' function; we will do that for you. Returns: the number of nodes that match the specified css select</p> 
                    

## assertCursorPosition

<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertCursorPosition(locator, pattern) Generated from getCursorPosition(locator</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator pointing to an input element or textarea. Returns: the numerical position of the cursor in the field</p> 
                     

## assertEditable

<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertEditable(locator) Generated from isEditable(locator</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator. Returns: true if the input element is editable, false otherwise</p> 
                     

## assertElementHeight

<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertElementHeight(locator, pattern) Generated from getElementHeight(locator</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator pointing to an element. Returns: height of an element in pixels</p> 
                     

## assertElementIndex

<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertElementIndex(locator, pattern) Generated from getElementIndex(locator</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator pointing to an element. Returns: of relative index of the element to its parent (starting from 0)</p> 
                     

## assertElementNotPresent

<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertElementNotPresent(locator) Generated from isElementPresent(locator</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator. Returns: true if the element is not present, false otherwise</p> 
                     

## assertElementPositionLeft

<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertElementPositionLeft(locator, pattern) Generated from getElementPositionLeft(locator</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator pointing to an element OR an element itself. Returns: of pixels from the edge of the frame.</p> 
                     

## assertElementPositionTop

<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertElementPositionTop(locator, pattern) Generated from getElementPositionTop(locator) <strong className="ph b"> <strong className="ph b">Arguments:</strong></strong>*locator - an element locator pointing to an element OR an element itself. Returns: of pixels from the edge of the frame.</p> 
                     

## assertElementPresent

<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertElementPresent(locator) Generated from isElementPresent(locator</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator. Returns: true if the element is present, false otherwise</p> 
                     

## assertElementWidth

<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertElementWidth(locator, pattern) Generated from getElementWidth(locator</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator pointing to an element . Returns: width of an element in pixels</p> 
                     

## assertEval

<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertEval(script, pattern) Generated from getEval(script</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*script - the JavaScript snippet to run. Returns: the results of evaluating the snippet</p> 
                     

## assertExpression

<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertExpression(expression, pattern) Generated from getExpression(expression</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*expression - the value to return. Returns: the value passed in</p> 
                     

## assertHtmlSource

<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertHtmlSource(pattern) Generated from getHtmlSource(). Returns: the entire HTML source</p> 
                     

## assertLocation

<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertLocation(pattern) Generated from getLocation(). Returns: the absolute URL of the current page</p> 
                     

## assertMouseSpeed

<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertMouseSpeed(pattern) Generated from getMouseSpeed(). Returns: the number of pixels between "mousemove" events during dragAndDrop commands (default=10)</p> 
                     

## assertNotAlert

<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertNotAlert(pattern) Generated from getAlert(). Returns: The message of the most recent JavaScript alert</p> 
                     

## assertNotAllButtons

<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertNotAllButtons(pattern) Generated from getAllButtons(). Returns: the IDs of all buttons on the page</p> 
                     

## assertNotAllFields

<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertNotAllFields(pattern) Generated from getAllFields(). Returns: the IDs of all field on the page</p> 
                     

## assertNotAllLinks

<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertNotAllLinks(pattern) Generated from getAllLinks(). Returns: the IDs of all links on the page</p> 
                     

## assertNotAllWindowIds

<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertNotAllWindowIds(pattern) Generated from getAllWindowIds(). Returns: Array of identifiers of all windows that the browser knows about.</p> 
                     

## assertNotAllWindowNames

<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertNotAllWindowNames(pattern) Generated from getAllWindowNames(). Returns: Array of names of all windows that the browser knows about.</p> 
                     

## assertNotAllWindowTitles

<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertNotAllWindowTitles(pattern) Generated from getAllWindowTitles(). Returns: Array of titles of all windows that the browser knows about.</p> 
                     

## assertNotAttribute

<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertNotAttribute(attributeLocator, pattern) Generated from getAttribute(attributeLocator</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*attributeLocator - an element locator followed by an @ sign and then the name of the attribute, e.g. "foo@bar" . Returns: the value of the specifie</p> 
                    

## assertNotAttributeFromAllWindows

<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertNotAttributeFromAllWindows(attributeName, pattern) Generated from getAttributeFromAllWindows(attributeName</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*attributeName - name of an attribute on the windows . Returns: the set of values of this attribute from all known windows.</p> 
                     

## assertNotBodyText

<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertNotBodyText(pattern) Generated from getBodyText(). Returns: the entire text of the page</p> 
                     

## assertNotChecked

<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertNotChecked(locator) Generated from isChecked(locator</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator pointing to a checkbox or radio button. Returns: true if the checkbox is checked, false otherwise</p> 
                     

## assertNotConfirmation

<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertNotConfirmation(pattern) Generated from getConfirmation(). Returns: the message of the most recent JavaScript confirmation dialog</p> 
                     

## assertNotCookie

<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertNotCookie(pattern) Generated from getCookie(). Returns: all cookies of the current page under test</p> 
                     

## assertNotCookieByName

<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertNotCookieByName(name, pattern) Generated from getCookieByName(name</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*name - the name of the cookie. Returns: the value of the cookie</p> 
                     

## assertNotCssCount

<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertNotCssCount(css, pattern) Generated from getCssCount(css)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*css - the css selector to evaluate. do NOT wrap this expression in a 'count()' function; we will do that for you. Returns: the number of nodes that match the specified css sel</p> 
                    

## assertNotCursorPosition

<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertNotCursorPosition(locator, pattern) Generated from getCursorPosition(locator</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator pointing to an input element or textarea . Returns: the numerical position of the cursor in the field</p> 
                     

## assertNotEditable

<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertNotEditable(locator) Generated from isEditable(locator) <strong className="ph b">Arguments:</strong> *locator - an element locator. Returns: true if the input element is editable, false otherwise</p> 
                     

## assertNotElementHeight

<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertNotElementHeight(locator, pattern) Generated from getElementHeight(locator) <strong className="ph b">Arguments:</strong> *locator - an element locator pointing to an element. Returns: height of an element in pixels</p> 
                     

## assertNotElementIndex

<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertNotElementIndex(locator, pattern) Generated from getElementIndex(locator</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator pointing to an element . Returns: of relative index of the element to its parent (starting from 0)</p> 
                     

## assertNotElementPositionLeft

<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertNotElementPositionLeft(locator, pattern) Generated from getElementPositionLeft(locator</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator pointing to an element OR an element itself . Returns: of pixels from the edge of the frame.</p> 
                     

## assertNotElementPositionTop

<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertNotElementPositionTop(locator, pattern) Generated from getElementPositionTop(locator</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator pointing to an element OR an element itself. Returns: of pixels from the edge of the frame.</p> 
                     

## assertNotElementWidth

<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertNotElementWidth(locator, pattern) Generated from getElementWidth(locator</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator pointing to an element. Returns: width of an element in pixels</p> 
                     

## assertNotEval

<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertNotEval(script, pattern) Generated from getEval(script</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*script - the JavaScript snippet to run . Returns: the results of evaluating the snippet</p> 
                     

## assertNotExpression

<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertNotExpression(expression, pattern) Generated from getExpression(expression</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*expression - the value to return. Returns: the value passed in</p> 
                     

## assertNotHtmlSource

<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertNotHtmlSource(pattern) Generated from getHtmlSource(). Returns: the entire HTML source</p> 
                     

## assertNotLocation

<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertNotLocation(pattern) Generated from getLocation(). Returns: the absolute URL of the current page</p> 
                     

## assertNotMouseSpeed

<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertNotMouseSpeed(pattern) Generated from getMouseSpeed(). Returns: the number of pixels between "mousemove" events during dragAndDrop commands (default=10)</p> 
                     

## assertNotOrdered

<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertNotOrdered(locator1, locator2) Generated from isOrdered(locator1, locator2</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator1 - an element locator pointing to the first element *locator2 - an element locator pointing to the second element . Returns: true if element1 is the</p> 
                    

## assertNotPrompt

<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertNotPrompt(pattern) Generated from getPrompt(). Returns: the message of the most recent JavaScript question prompt</p> 
                     

## assertNotSelectOptions

<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertNotSelectOptions(selectLocator, pattern) Generated from getSelectOptions(selectLocator</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*selectLocator - an element locator identifying a drop-down menu . Returns: an array of all option labels in the specified select drop-down</p> 
                     

## assertNotSelectedId

<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertNotSelectedId(selectLocator, pattern) Generated from getSelectedId(selectLocator</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*selectLocator - an element locator identifying a drop-down menu. Returns: the selected option ID in the specified select drop-down</p> 
                     

## assertNotSelectedIds

<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertNotSelectedIds(selectLocator, pattern) Generated from getSelectedIds(selectLocator</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*selectLocator - an element locator identifying a drop-down menu . Returns: an array of all selected option IDs in the specified select drop-down</p> 
                     

## assertNotSelectedIndex

<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertNotSelectedIndex(selectLocator, pattern) Generated from getSelectedIndex(selectLocator</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*selectLocator - an element locator identifying a drop-down menu. Returns: the selected option index in the specified select drop-down</p> 
                     

## assertNotSelectedIndexes

<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertNotSelectedIndexes(selectLocator, pattern) Generated from getSelectedIndexes(selectLocator) <strong className="ph b">Arguments:</strong> *selectLocator - an element locator identifying a drop-down menu . Returns: an array of all selected option indexes in the specified select dro</p> 
                    

## assertNotSelectedLabel

<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertNotSelectedLabel(selectLocator, pattern) Generated from getSelectedLabel(selectLocator</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*selectLocator - an element locator identifying a drop-down menu . Returns: the selected option label in the specified select drop-down</p> 
                     

## assertNotSelectedLabels

<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertNotSelectedLabels(selectLocator, pattern) Generated from getSelectedLabels(selectLocator</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*selectLocator - an element locator identifying a drop-down menu. Returns: an array of all selected option labels in the specified select drop-d</p> 
                    

## assertNotSelectedValue

<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertNotSelectedValue(selectLocator, pattern) Generated from getSelectedValue(selectLocator</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*selectLocator - an element locator identifying a drop-down menu . Returns: the selected option value in the specified select drop-down</p> 
                     

## assertNotSelectedValues

<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertNotSelectedValues(selectLocator, pattern) Generated from getSelectedValues(selectLocator</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*selectLocator - an element locator identifying a drop-down menu . Returns: an array of all selected option values in the specified select drop-</p> 
                    

## assertNotSomethingSelected

<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertNotSomethingSelected(selectLocator) Generated from isSomethingSelected(selectLocator</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*selectLocator - an element locator identifying a drop-down menu . Returns: true if some option has been selected, false otherwise</p> 
                     

## assertNotSpeed

<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertNotSpeed(pattern) Generated from getSpeed(). Returns: the execution speed in milliseconds.</p> 
                     

## assertNotTable

<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertNotTable(tableCellAddress, pattern) Generated from getTable(tableCellAddress</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*tableCellAddress - a cell address, e.g. "foo.1.4" . Returns: the text from the specified cell</p> 
                     

## assertNotText

<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertNotText(locator, pattern) Generated from getText(locator</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator Returns: the text of the element</p> 
                     

## assertNotTitle

<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertNotTitle(pattern) Generated from getTitle(). Returns: the title of the current page</p> 
                     

## assertNotValue

<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertNotValue(locator, pattern) Generated from getValue(locator</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator. Returns: the element value, or "on/off" for checkbox/radio elements</p> 
                     

## assertNotVisible

<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertNotVisible(locator) Generated from isVisible(locator</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator. Returns: true if the specified element is visible, false otherwise</p> 
                     

## assertNotWhetherThisFrameMatchFrameExpression

 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertNotWhetherThisFrameMatchFrameExpression(currentFrameString, target, pattern) Generated from getWhetherThisFrameMatchFrameExpression(currentFrameString, target</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*currentFrameString - starting frame *target - new frame (which might be r</p> 
                    

## assertNotWhetherThisWindowMatchWindowExpression

 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertNotWhetherThisWindowMatchWindowExpression(currentWindowString, target, pattern) Generated from getWhetherThisWindowMatchWindowExpression(currentWindowString, target</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*currentWindowString - starting window *target - new window (which m</p> 
                    

## assertNotXpathCount

<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertNotXpathCount(xpath, pattern) Generated from getXpathCount(xpath</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*xpath - the xpath expression to evaluate. do NOT wrap this expression in a 'count()' function; we will do that for you. Returns: the number of nodes that match the spe</p> 
                    

## assertOrdered

<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertOrdered(locator1, locator2) Generated from isOrdered(locator1, locator2</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator1 - an element locator pointing to the first element *locator2 - an element locator pointing to the second element. Returns: true if elemen</p> 
                    

## assertPrompt

<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertPrompt(pattern) Generated from getPrompt(). Returns: the message of the most recent JavaScript question prompt</p> 
                     

## assertPromptAndWait

<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertPromptAndWait(pattern) Generated from getPrompt(). Returns: the message of the most recent JavaScript question prompt</p> 
                     

## assertPromptNotPresent

<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertPromptNotPresent() Generated from isPromptPresent(). Returns: true if there is a pending prompt</p> 
                     

## assertPromptPresent

<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertPromptPresent() Generated from isPromptPresent(). Returns: true if there is a pending prompt</p> 
                     

## assertSelectOptions

<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertSelectOptions(selectLocator, pattern) Generated from getSelectOptions(selectLocator</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*selectLocator - an element locator identifying a drop-down menu. Returns: an array of all option labels in the specified select drop-down</p> 
                     

## assertSelectedId

<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertSelectedId(selectLocator, pattern) Generated from getSelectedId(selectLocator</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*selectLocator - an element locator identifying a drop-down menu . Returns: the selected option ID in the specified select drop-down</p> 
                     

## assertSelectedIds

<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertSelectedIds(selectLocator, pattern) Generated from getSelectedIds(selectLocator</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*selectLocator - an element locator identifying a drop-down menu . Returns: an array of all selected option IDs in the specified select drop-down</p> 
                     

## assertSelectedIndex

<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertSelectedIndex(selectLocator, pattern) Generated from getSelectedIndex(selectLocator</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*selectLocator - an element locator identifying a drop-down menu . Returns: the selected option index in the specified select drop-down</p> 
                     

## assertSelectedIndexes

<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertSelectedIndexes(selectLocator, pattern) Generated from getSelectedIndexes(selectLocator</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*selectLocator - an element locator identifying a drop-down menu . Returns: an array of all selected option indexes in the specified select drop-</p> 
                    

## assertSelectedLabel

<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertSelectedLabel(selectLocator, pattern) Generated from getSelectedLabel(selectLocator</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*selectLocator - an element locator identifying a drop-down menu . Returns: the selected option label in the specified select drop-down</p> 
                     

## assertSelectedLabels

<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertSelectedLabels(selectLocator, pattern) Generated from getSelectedLabels(selectLocator</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*selectLocator - an element locator identifying a drop-down menu . Returns: an array of all selected option labels in the specified select drop-dow</p> 
                    

## assertSelectedValue

<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertSelectedValue(selectLocator, pattern) Generated from getSelectedValue(selectLocator</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*selectLocator - an element locator identifying a drop-down menu . Returns: the selected option value in the specified select drop-down</p> 
                     

## assertSelectedValues

<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertSelectedValues(selectLocator, pattern) Generated from getSelectedValues(selectLocator</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*selectLocator - an element locator identifying a drop-down menu . Returns: an array of all selected option values in the specified select drop-dow</p> 
                    

## assertSomethingSelected

                            
<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertSomethingSelected(selectLocator)</p> 
                            
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> Generated from isSomethingSelected(selectLocator)</p> 
                            
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
                            
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*selectLocator - an element locator identifying a drop-down menu .</p> 
                            
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> Returns: true if some option has been selected, false otherwise </p> 
                                            

## assertSpeed

<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertSpeed(pattern) Generated from getSpeed(). Returns: the execution speed in milliseconds.</p> 
                     

## assertTable

<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertTable(tableCellAddress, pattern) Generated from getTable(tableCellAddress)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*tableCellAddress - a cell address, e.g. "foo.1.4" . Returns: the text from the specified cell</p> 
                     

## assertText

                            
<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertText(locator, pattern)</p> 
                            
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> Generated from getText(locator)</p> 
                            
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Arguments:</p> 
                            
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> *locator - an element locator .</p> 
                            
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> Returns: the text of the element </p> 
                                            

## assertTextAndWait

<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertTextAndWait(locator, pattern) Generated from getText(locator) Arguments: *locator - an element locator . Returns: the text of the element</p> 
                     

## assertTextNotPresent

<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertTextNotPresent(pattern) This command is deprecated. Use the assertNotText command with an element locator instead. Generated from isTextPresent(pattern) Arguments: *pattern - a pattern to match with the text of the page . Returns: true if the patt</p> 
                    

## assertTextPresent

<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertTextPresent(pattern) This command is deprecated. Use the assertText command with an element locator instead. Generated from isTextPresent(pattern) Arguments: *pattern - a pattern to match with the text of the page . Returns: true if the pattern m</p> 
                    

## assertTitle

<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertTitle(pattern) Generated from getTitle(). Returns: the title of the current page</p> 
                     

## assertTitleAndWait

<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertTitleAndWait(pattern) Generated from getTitle(). Returns: the title of the current page</p> 
                     

## assertValue

<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertValue(locator, pattern) Generated from getValue(locator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator. Returns: the element value, or "on/off" for checkbox/radio elements</p> 
                     

## assertVisible

<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertVisible(locator) Generated from isVisible(locator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator. Returns: true if the specified element is visible, false otherwise</p> 
                     

## assertWhetherThisFrameMatchFrameExpression

<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertWhetherThisFrameMatchFrameExpression(currentFrameString, target, pattern) Generated from getWhetherThisFrameMatchFrameExpression(currentFrameString, target)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*currentFrameString - starting frame *target - new frame (which might be rela</p> 
                    

## assertWhetherThisWindowMatchWindowExpression

 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertWhetherThisWindowMatchWindowExpression(currentWindowString, target, pattern) Generated from getWhetherThisWindowMatchWindowExpression(currentWindowString, target)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*currentWindowString - starting window *target - new window (which migh</p> 
                    

## assertXpathCount

<p xmlns="http://www.w3.org/1999/xhtml" className="p">assertXpathCount(xpath, pattern) Generated from getXpathCount(xpath)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*xpath - the xpath expression to evaluate. do NOT wrap this expression in a 'count()' function; we will do that for you. Returns: the number of nodes that match the specif</p> 
                    

## assignId

<p xmlns="http://www.w3.org/1999/xhtml" className="p">assignId(locator, identifier)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator pointing to an element *identifier - a string to be used as the ID of the specified element</p> 
                     

## assignIdAndWait

<p xmlns="http://www.w3.org/1999/xhtml" className="p">assignIdAndWait(locator, identifier) Generated from assignId(locator, identifier)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator pointing to an element *identifier - a string to be used as the ID of the specified element</p> 
                     

## break

<p xmlns="http://www.w3.org/1999/xhtml" className="p">break()</p> 
                    

## captureEntirePageScreenshot

<p xmlns="http://www.w3.org/1999/xhtml" className="p">captureEntirePageScreenshot(filename, kwargs) <strong className="ph b">Arguments</strong>: *filename - the path to the file to persist the screenshot as. No filename extension will be appended by default. Directories will not be created if they do not exist, and an ex</p> 
                    

## captureEntirePageScreenshotAndWait

<p xmlns="http://www.w3.org/1999/xhtml" className="p">captureEntirePageScreenshotAndWait(filename, kwargs) Generated from captureEntirePageScreenshot(filename, kwargs)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*filename - the path to the file to persist the screenshot as. No filename extension will be appended by default. Directories w</p> 
                    

## check

<p xmlns="http://www.w3.org/1999/xhtml" className="p">check(locator) <strong className="ph b">Arguments</strong>: *locator - an element locator</p> 
                    

## checkAndWait

<p xmlns="http://www.w3.org/1999/xhtml" className="p">checkAndWait(locator) Generated from check(locator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator</p> 
                    

## chooseCancelOnNextConfirmation

<p xmlns="http://www.w3.org/1999/xhtml" className="p">chooseCancelOnNextConfirmation()</p> 
                    

## chooseCancelOnNextPrompt

<p xmlns="http://www.w3.org/1999/xhtml" className="p">chooseCancelOnNextPrompt</p> 
                    

## chooseCancelOnNextPromptAndWait

<p xmlns="http://www.w3.org/1999/xhtml" className="p">chooseCancelOnNextPromptAndWait</p> 
                    

## chooseOkOnNextConfirmation

<p xmlns="http://www.w3.org/1999/xhtml" className="p">chooseOkOnNextConfirmation()</p> 
                    

## chooseOkOnNextConfirmationAndWait

<p xmlns="http://www.w3.org/1999/xhtml" className="p">chooseOkOnNextConfirmationAndWait() Generated from chooseOkOnNextConfirmation()</p> 
                    

## click

<p xmlns="http://www.w3.org/1999/xhtml" className="p">click(locator)</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 *locator - an element locator 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Clicks on a link, button, checkbox or radio button. If the click action causes a new page to load (like a link usually does), call waitForPageToLoad.</p> 
                                            

## clickAndWait

<p xmlns="http://www.w3.org/1999/xhtml" className="p">clickAndWait(locator)</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> Generated from click(locator)</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 *locator - an element locator 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Clicks on a link, button, checkbox or radio button. If the click action causes a new page to load (like a link usually does), call waitForPageToLoad.</p> 
                                            

## clickAt

<p xmlns="http://www.w3.org/1999/xhtml" className="p">clickAt(locator, coordString)</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 *locator - an element locator *coordString - specifies the x,y position (i.e. - 10,20) of the mouse event relative to the element returned by the locator. 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Clicks on a link, button, checkbox or radio button. If the click action causes a new page to load (like a link usually does), call waitForPageToLoad.</p> 
                                            

## clickAtAndWait

<p xmlns="http://www.w3.org/1999/xhtml" className="p">clickAtAndWait(locator, coordString)</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> Generated from clickAt(locator, coordString)</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 *locator - an element locator *coordString - specifies the x,y position (i.e. - 10,20) of the mouse event relative to the element returned by the locator. 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Clicks on a link, button, checkbox or radio button. If the click action causes a new page to load (like a link usually does), call waitForPageToLoad.</p> 
                                            

## close

<p xmlns="http://www.w3.org/1999/xhtml" className="p">close()</p> 
                    

## contextMenu

<p xmlns="http://www.w3.org/1999/xhtml" className="p">contextMenu(locator) <strong className="ph b">Arguments</strong>: *locator - an element locator</p> 
                     

## contextMenuAndWait

<p xmlns="http://www.w3.org/1999/xhtml" className="p">contextMenuAndWait(locator) Generated from contextMenu(locator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator</p> 
                     

## contextMenuAt

<p xmlns="http://www.w3.org/1999/xhtml" className="p">contextMenuAt(locator, coordString)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator *coordString - specifies the x,y position (i.e. - 10,20) of the mouse event relative to the element returned by the locator.</p> 
                     

## contextMenuAtAndWait

<p xmlns="http://www.w3.org/1999/xhtml" className="p">contextMenuAtAndWait(locator, coordString) Generated from contextMenuAt(locator, coordString)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator *coordString - specifies the x,y position (i.e. - 10,20) of the mouse event relative to the element returned by the</p> 
                     

## controlKeyDown

<p xmlns="http://www.w3.org/1999/xhtml" className="p">controlKeyDown()</p> 
                    

## controlKeyDownAndWait

<p xmlns="http://www.w3.org/1999/xhtml" className="p">controlKeyDownAndWait() Generated from controlKeyDown()</p> 
                    

## controlKeyUp

<p xmlns="http://www.w3.org/1999/xhtml" className="p">controlKeyUp()</p> 
                    

## controlKeyUpAndWait

<p xmlns="http://www.w3.org/1999/xhtml" className="p">controlKeyUpAndWait() Generated from controlKeyUp()</p> 
                    

## createCookie

<p xmlns="http://www.w3.org/1999/xhtml" className="p">createCookie(nameValuePair, optionsString)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*nameValuePair - name and value of the cookie in a format "name=value" *optionsString - options for the cookie. Currently supported options include 'path', 'max_age' and 'domain'. the optionsString'</p> 
                    

## createCookieAndWait

<p xmlns="http://www.w3.org/1999/xhtml" className="p">createCookieAndWait(nameValuePair, optionsString) Generated from createCookie(nameValuePair, optionsString)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*nameValuePair - name and value of the cookie in a format "name=value" *optionsString - options for the cookie. Currently supported</p> 
                     

## deleteAllVisibleCookies

<p xmlns="http://www.w3.org/1999/xhtml" className="p">deleteAllVisibleCookies()</p> 
                    

## deleteAllVisibleCookiesAndWait

<p xmlns="http://www.w3.org/1999/xhtml" className="p">deleteAllVisibleCookiesAndWait() Generated from deleteAllVisibleCookies()</p> 
                    

## deleteCookie

<p xmlns="http://www.w3.org/1999/xhtml" className="p">deleteCookie(name, optionsString)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*name - the name of the cookie to be deleted *optionsString - options for the cookie. Currently supported options include 'path', 'domain' and 'recurse.' The optionsString's format is "path=/path/, domain=.f</p> 
                    

## deleteCookieAndWait

<p xmlns="http://www.w3.org/1999/xhtml" className="p">deleteCookieAndWait(name, optionsString) Generated from deleteCookie(name, optionsString)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*name - the name of the cookie to be deleted *optionsString - options for the cookie. Currently supported options include 'path', 'domain' and 'recur</p> 
                    

## deselectPopUp

<p xmlns="http://www.w3.org/1999/xhtml" className="p">deselectPopUp()</p> 
                    

## deselectPopUpAndWait

<p xmlns="http://www.w3.org/1999/xhtml" className="p">deselectPopUpAndWait() Generated from deselectPopUp()</p> 
                    

## domWait

<p xmlns="http://www.w3.org/1999/xhtml" className="p">domWait</p> 
                    

## domWaitAndWait

<p xmlns="http://www.w3.org/1999/xhtml" className="p">domWaitAndWait</p> 
                    

## doubleClick

<p xmlns="http://www.w3.org/1999/xhtml" className="p">doubleClick(locator) <strong className="ph b">Arguments</strong>: *locator - an element locator</p> 
                     

## doubleClickAndWait

<p xmlns="http://www.w3.org/1999/xhtml" className="p">doubleClickAndWait(locator) Generated from doubleClick(locator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator</p> 
                     

## doubleClickAt

<p xmlns="http://www.w3.org/1999/xhtml" className="p">doubleClickAt(locator, coordString)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator *coordString - specifies the x,y position (i.e. - 10,20) of the mouse event relative to the element returned by the locator.</p> 
                     

## doubleClickAtAndWait

<p xmlns="http://www.w3.org/1999/xhtml" className="p">doubleClickAtAndWait(locator, coordString) Generated from doubleClickAt(locator, coordString)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator *coordString - specifies the x,y position (i.e. - 10,20) of the mouse event relative to the element returned by the</p> 
                     

## dragAndDrop

<p xmlns="http://www.w3.org/1999/xhtml" className="p">dragAndDrop(locator, movementsString)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator *movementsString - offset in pixels from the current location to which the element should be moved, e.g., "+70,-300"</p> 
                     

## dragAndDropAndWait

<p xmlns="http://www.w3.org/1999/xhtml" className="p">dragAndDropAndWait(locator, movementsString) Generated from dragAndDrop(locator, movementsString)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator *movementsString - offset in pixels from the current location to which the element should be moved, e.g., "+70,-</p> 
                    

## dragAndDropToObject

<p xmlns="http://www.w3.org/1999/xhtml" className="p">dragAndDropToObject(locatorOfObjectToBeDragged, locatorOfDragDestinationObject)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locatorOfObjectToBeDragged - an element to be dragged *locatorOfDragDestinationObject - an element whose location (i.e., whose center-most pixel) will be the po</p> 
                    

## dragAndDropToObjectAndWait

<p xmlns="http://www.w3.org/1999/xhtml" className="p">dragAndDropToObjectAndWait(locatorOfObjectToBeDragged, locatorOfDragDestinationObject) Generated from dragAndDropToObject(locatorOfObjectToBeDragged, locatorOfDragDestinationObject)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locatorOfObjectToBeDragged - an element to be dragged *lo</p> 
                    

## echo

<p xmlns="http://www.w3.org/1999/xhtml" className="p">echo(message) <strong className="ph b">Arguments</strong>: *message - the message to print</p> 
                     

## echoAndWait

<p xmlns="http://www.w3.org/1999/xhtml" className="p">echoAndWait(message) Generated from echo(message)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*message - the message to print</p> 
                     

## editContent

<p xmlns="http://www.w3.org/1999/xhtml" className="p">editContent</p> 
                    

## editContentAndWait

<p xmlns="http://www.w3.org/1999/xhtml" className="p">editContentAndWait</p> 
                    

## fireEvent

<p xmlns="http://www.w3.org/1999/xhtml" className="p">fireEvent(locator, eventName)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator *eventName - the event name, e.g. "focus" or "blur"</p> 
                     

## fireEventAndWait

<p xmlns="http://www.w3.org/1999/xhtml" className="p">fireEventAndWait(locator, eventName) Generated from fireEvent(locator, eventName)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator *eventName - the event name, e.g. "focus" or "blur"</p> 
                     

## focus

<p xmlns="http://www.w3.org/1999/xhtml" className="p">focus(locator) <strong className="ph b">Arguments</strong>: *locator - an element locator</p> 
                    

## focusAndWait

<p xmlns="http://www.w3.org/1999/xhtml" className="p">focusAndWait(locator) Generated from focus(locator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator</p> 
                    

## goBack

<p xmlns="http://www.w3.org/1999/xhtml" className="p">goBack()</p> 
                    

## goBackAndWait

<p xmlns="http://www.w3.org/1999/xhtml" className="p">goBackAndWait() Generated from goBack()</p> 
                    

## highlight

<p xmlns="http://www.w3.org/1999/xhtml" className="p">highlight(locator) Arguments: *locator - an element locator</p> 
                    

## highlightAndWait

<p xmlns="http://www.w3.org/1999/xhtml" className="p">highlightAndWait(locator) Generated from highlight(locator) Arguments: *locator - an element locator</p> 
                    

## ignoreAttributesWithoutValue

<p xmlns="http://www.w3.org/1999/xhtml" className="p">ignoreAttributesWithoutValue(ignore) <strong className="ph b">Arguments</strong>: *ignore - boolean, true means we'll ignore attributes without value at the expense of xpath "correctness"; false means we'll sacrifice speed for correctness.</p> 
                     

## ignoreAttributesWithoutValueAndWait

<p xmlns="http://www.w3.org/1999/xhtml" className="p">ignoreAttributesWithoutValueAndWait(ignore) Generated from ignoreAttributesWithoutValue(ignore)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*ignore - boolean, true means we'll ignore attributes without value at the expense of xpath "correctness"; false means we'll sacrifice speed for</p> 
                     

## keyDown

<p xmlns="http://www.w3.org/1999/xhtml" className="p">keyDown(locator, keySequence) This command is deprecated. Use the sendKeys command instead.</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator *keySequence - Either be a string("\" followed by the numeric keycode of the keytobe pressed, normally theASCIIvalu</p> 
                    

## keyDownAndWait

<p xmlns="http://www.w3.org/1999/xhtml" className="p">keyDownAndWait(locator, keySequence) This command is deprecated. Use the sendKeysAndWait command instead. Generated from keyDown(locator, keySequence)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator *keySequence - Either be a string("\" followed by the numeric</p> 
                    

## keyPress

<p xmlns="http://www.w3.org/1999/xhtml" className="p">keyPress(locator, keySequence) This command is deprecated. Use the sendKeys command instead.</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator *keySequence - Either be a string("\" followed by the numeric keycode of the keytobe pressed, normally the ASCIIval</p> 
                    

## keyPressAndWait

<p xmlns="http://www.w3.org/1999/xhtml" className="p">keyPressAndWait(locator, keySequence) This command is deprecated. Use the sendKeysAndWait command instead. Generated from keyPress(locator, keySequence)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator *keySequence - Either be a string("\" followed bythenumer</p> 
                    

## keyUp

<p xmlns="http://www.w3.org/1999/xhtml" className="p">keyUp(locator, keySequence) This command is deprecated. Use the sendKeys command instead.</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator *keySequence - Either be a string("\" followed by the numeric keycode of the key to be pressed, normally the ASCII value</p> 
                     

## keyUpAndWait

<p xmlns="http://www.w3.org/1999/xhtml" className="p">keyUpAndWait(locator, keySequence) This command is deprecated. Use the sendKeysAndWait command instead. Generated from keyUp(locator, keySequence)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator *keySequence - Either be a string("\" followed by the numeric ke</p> 
                    

## metaKeyDown

<p xmlns="http://www.w3.org/1999/xhtml" className="p">metaKeyDown()</p> 
                    

## metaKeyDownAndWait

<p xmlns="http://www.w3.org/1999/xhtml" className="p">metaKeyDownAndWait() Generated from metaKeyDown()</p> 
                    

## metaKeyUp

<p xmlns="http://www.w3.org/1999/xhtml" className="p">metaKeyUp()</p> 
                    

## metaKeyUpAndWait

<p xmlns="http://www.w3.org/1999/xhtml" className="p">metaKeyUpAndWait() Generated from metaKeyUp()</p> 
                    

## mouseDown

<p xmlns="http://www.w3.org/1999/xhtml" className="p">mouseDown(locator) <strong className="ph b">Arguments</strong>: *locator - an element locator</p> 
                    

## mouseDownAndWait

<p xmlns="http://www.w3.org/1999/xhtml" className="p">mouseDownAndWait(locator) Generated from mouseDown(locator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator</p> 
                    

## mouseDownAt

<p xmlns="http://www.w3.org/1999/xhtml" className="p">mouseDownAt(locator, coordString)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator *coordString - specifies the x,y position (i.e. - 10,20) of the mouse event relative to the element returned by the locator.</p> 
                     

## mouseDownAtAndWait

<p xmlns="http://www.w3.org/1999/xhtml" className="p">mouseDownAtAndWait(locator, coordString) Generated from mouseDownAt(locator, coordString)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator *coordString - specifies the x,y position (i.e. - 10,20) of the mouse event relative to the element returned by</p> 
                     

## mouseDownRight

<p xmlns="http://www.w3.org/1999/xhtml" className="p">mouseDownRight(locator) Arguments: *locator - an element locator</p> 
                     

## mouseDownRightAndWait

<p xmlns="http://www.w3.org/1999/xhtml" className="p">mouseDownRightAndWait(locator) Generated from mouseDownRight(locator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator</p> 
                    

## mouseDownRightAt

<p xmlns="http://www.w3.org/1999/xhtml" className="p">mouseDownRightAt(locator, coordString)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator *coordString - specifies the x,y position (i.e. - 10,20) of the mouse event relative to the element returned by the locator.</p> 
                     

## mouseDownRightAtAndWait

<p xmlns="http://www.w3.org/1999/xhtml" className="p">mouseDownRightAtAndWait(locator, coordString) Generated from mouseDownRightAt(locator, coordString)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator *coordString - specifies the x,y position (i.e. - 10,20) of the mouse event relative to the element re</p> 
                    

## mouseMove

<p xmlns="http://www.w3.org/1999/xhtml" className="p">mouseMove(locator) <strong className="ph b">Arguments</strong>: *locator - an element locator</p> 
                    

## mouseMoveAndWait

<p xmlns="http://www.w3.org/1999/xhtml" className="p">mouseMoveAndWait(locator) Generated from mouseMove(locator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator</p> 
                    

## mouseMoveAt

<p xmlns="http://www.w3.org/1999/xhtml" className="p">mouseMoveAt(locator, coordString)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator *coordString - specifies the x,y position (i.e. - 10,20) of the mouse event relative to the element returned by the locator.</p> 
                     

## mouseMoveAtAndWait

<p xmlns="http://www.w3.org/1999/xhtml" className="p">mouseMoveAtAndWait(locator, coordString) Generated from mouseMoveAt(locator, coordString)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator *coordString - specifies the x,y position (i.e. - 10,20) of the mouse event relative to the element returned by</p> 
                     

## mouseOut

<p xmlns="http://www.w3.org/1999/xhtml" className="p">mouseOut(locator) <strong className="ph b">Arguments</strong>: *locator - an element locator</p> 
                    

## mouseOutAndWait

<p xmlns="http://www.w3.org/1999/xhtml" className="p">mouseOutAndWait(locator) Generated from mouseOut(locator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator</p> 
                    

## mouseOver

<p xmlns="http://www.w3.org/1999/xhtml" className="p">mouseOver(locator) <strong className="ph b">Arguments</strong>: *locator - an element locator</p> 
                    

## mouseOverAndWait

<p xmlns="http://www.w3.org/1999/xhtml" className="p">mouseOverAndWait(locator) Generated from mouseOver(locator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator</p> 
                    

## mouseUp

<p xmlns="http://www.w3.org/1999/xhtml" className="p">mouseUp(locator) <strong className="ph b">Arguments</strong>: *locator - an element locator</p> 
                    

## mouseUpAndWait

<p xmlns="http://www.w3.org/1999/xhtml" className="p">mouseUpAndWait(locator) Generated from mouseUp(locator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator</p> 
                    

## mouseUpAt

<p xmlns="http://www.w3.org/1999/xhtml" className="p">mouseUpAt(locator, coordString)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator *coordString - specifies the x,y position (i.e. - 10,20) of the mouse event relative to the element returned by the locator.</p> 
                     

## mouseUpAtAndWait

<p xmlns="http://www.w3.org/1999/xhtml" className="p">mouseUpAtAndWait(locator, coordString) Generated from mouseUpAt(locator, coordString)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator *coordString - specifies the x,y position (i.e. - 10,20) of the mouse event relative to the element returned by the</p> 
                     

## mouseUpRight

<p xmlns="http://www.w3.org/1999/xhtml" className="p">mouseUpRight(locator) <strong className="ph b">Arguments</strong>: *locator - an element locator</p> 
                    

## mouseUpRightAndWait

<p xmlns="http://www.w3.org/1999/xhtml" className="p">mouseUpRightAndWait(locator) Generated from mouseUpRight(locator) Arguments: *locator - an element locator</p> 
                    

## mouseUpRightAt

<p xmlns="http://www.w3.org/1999/xhtml" className="p">mouseUpRightAt(locator, coordString)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator *coordString - specifies the x,y position (i.e. - 10,20) of the mouse event relative to the element returned by the locator.</p> 
                     

## mouseUpRightAtAndWait

<p xmlns="http://www.w3.org/1999/xhtml" className="p">mouseUpRightAtAndWait(locator, coordString) Generated from mouseUpRightAt(locator, coordString)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator *coordString - specifies the x,y position (i.e. - 10,20) of the mouse event relative to the element return</p> 
                    

## open

<p xmlns="http://www.w3.org/1999/xhtml" className="p">open(url) <strong className="ph b">Arguments</strong>: *url - the URL to open; may be relative or absolute</p> 
                     

## openWindow

<p xmlns="http://www.w3.org/1999/xhtml" className="p">openWindow(url, windowID)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*url - the URL to open, which can be blank *windowID - the JavaScript window ID of the window to select</p> 
                     

## openWindowAndWait

<p xmlns="http://www.w3.org/1999/xhtml" className="p">openWindowAndWait(url, windowID) Generated from openWindow(url, windowID)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*url - the URL to open, which can be blank *windowID - the JavaScript window ID of the window to select</p> 
                     

## pageWait

<p xmlns="http://www.w3.org/1999/xhtml" className="p">pageWait</p> 
                    

## pageWaitAndWait

<p xmlns="http://www.w3.org/1999/xhtml" className="p">pageWaitAndWait</p> 
                    

## pause

<p xmlns="http://www.w3.org/1999/xhtml" className="p">pause(waitTime) Arguments: *waitTime - the amount of time to sleep (in milliseconds)</p> 
                     

## prePageWait

<p xmlns="http://www.w3.org/1999/xhtml" className="p">prePageWait</p> 
                    

## prePageWaitAndWait

<p xmlns="http://www.w3.org/1999/xhtml" className="p">prePageWaitAndWait</p> 
                    

## refresh

<p xmlns="http://www.w3.org/1999/xhtml" className="p">refresh()</p> 
                    

## refreshAndWait

<p xmlns="http://www.w3.org/1999/xhtml" className="p">refreshAndWait() Generated from refresh()</p> 
                    

## removeAllSelections

<p xmlns="http://www.w3.org/1999/xhtml" className="p">removeAllSelections(locator) <strong className="ph b">Arguments</strong>: *locator - an element locator identifying a multi-select box</p> 
                     

## removeAllSelectionsAndWait

<p xmlns="http://www.w3.org/1999/xhtml" className="p">removeAllSelectionsAndWait(locator) Generated from removeAllSelections(locator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator identifying a multi-select box</p> 
                     

## removeScript

<p xmlns="http://www.w3.org/1999/xhtml" className="p">removeScript(scriptTagId) <strong className="ph b">Arguments</strong>: *scriptTagId - the id of the script element to remove.</p> 
                     

## removeScriptAndWait

<p xmlns="http://www.w3.org/1999/xhtml" className="p">removeScriptAndWait(scriptTagId) Generated from removeScript(scriptTagId)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*scriptTagId - the id of the script element to remove.</p> 
                     

## removeSelection

<p xmlns="http://www.w3.org/1999/xhtml" className="p">removeSelection(locator, optionLocator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator identifying a multi-select box *optionLocator - an option locator (a label by default)</p> 
                     

## removeSelectionAndWait

<p xmlns="http://www.w3.org/1999/xhtml" className="p">removeSelectionAndWait(locator, optionLocator) Generated from removeSelection(locator, optionLocator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator identifying a multi-select box *optionLocator - an option locator (a label by default)</p> 
                     

## rollup

<p xmlns="http://www.w3.org/1999/xhtml" className="p">rollup(rollupName, kwargs)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*rollupName - the name of the rollup command *kwargs - keyword arguments string that influences how the rollup expands into commands</p> 
                     

## rollupAndWait

<p xmlns="http://www.w3.org/1999/xhtml" className="p">rollupAndWait(rollupName, kwargs) Generated from rollup(rollupName, kwargs)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*rollupName - the name of the rollup command *kwargs - keyword arguments string that influences how the rollup expands into commands</p> 
                     

## runScript

<p xmlns="http://www.w3.org/1999/xhtml" className="p">runScript(script) <strong className="ph b">Arguments</strong>: *script - the JavaScript snippet to run</p> 
                     

## runScriptAndWait

<p xmlns="http://www.w3.org/1999/xhtml" className="p">runScriptAndWait(script) Generated from runScript(script)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*script - the JavaScript snippet to run</p> 
                     

## select

<p xmlns="http://www.w3.org/1999/xhtml" className="p">select(selectLocator, optionLocator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*selectLocator - an element locator identifying a drop-down menu *optionLocator - an option locator (a label by default)</p> 
                     

## selectAndWait

<p xmlns="http://www.w3.org/1999/xhtml" className="p">selectAndWait(selectLocator, optionLocator) Generated from select(selectLocator, optionLocator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*selectLocator - an element locator identifying a drop-down menu *optionLocator - an option locator (a label by default)</p> 
                     

## selectFrame

<p xmlns="http://www.w3.org/1999/xhtml" className="p">selectFrame(locator) <strong className="ph b">Arguments</strong>: *locator - an element locator identifying a frame or iframe</p> 
                     

## selectPopUp

<p xmlns="http://www.w3.org/1999/xhtml" className="p">selectPopUp(windowID) <strong className="ph b">Arguments</strong>: *windowID - an identifier for the popup window, which can take on a number of different meanings</p> 
                     

## selectPopUpAndWait

<p xmlns="http://www.w3.org/1999/xhtml" className="p">selectPopUpAndWait(windowID) Generated from selectPopUp(windowID)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*windowID - an identifier for the popup window, which can take on a number of different meanings</p> 
                     

## selectWindow

<p xmlns="http://www.w3.org/1999/xhtml" className="p">selectWindow(windowID) <strong className="ph b">Arguments</strong>: *windowID - the JavaScript window ID of the window to select</p> 
                     

## sendKeys

<p xmlns="http://www.w3.org/1999/xhtml" className="p">sendKeys(locator, value)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator *value - the value to type</p> 
                     

## sendKeysAndWait

<p xmlns="http://www.w3.org/1999/xhtml" className="p">sendKeysAndWait(locator, value) Generated from sendKeys(locator, value)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator *value - the value to type</p> 
                     

## setCursorPosition

<p xmlns="http://www.w3.org/1999/xhtml" className="p">setCursorPosition(locator, position)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator pointing to an input element or textarea *position - the numerical position of the cursor in the field; position should be 0 to move the position to the beginning of the</p> 
                     

## setCursorPositionAndWait

<p xmlns="http://www.w3.org/1999/xhtml" className="p">setCursorPositionAndWait(locator, position) Generated from setCursorPosition(locator, position)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator pointing to an input element or textarea *position - the numerical position of the cursor in the field; positio</p> 
                    

## setMouseSpeed

<p xmlns="http://www.w3.org/1999/xhtml" className="p">setMouseSpeed(pixels) <strong className="ph b">Arguments</strong>: *pixels - the number of pixels between "mousemove" events</p> 
                     

## setMouseSpeedAndWait

<p xmlns="http://www.w3.org/1999/xhtml" className="p">setMouseSpeedAndWait(pixels) Generated from setMouseSpeed(pixels)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*pixels - the number of pixels between "mousemove" events</p> 
                     

## setSpeed

<p xmlns="http://www.w3.org/1999/xhtml" className="p">setSpeed(value) <strong className="ph b">Arguments</strong>: *value - the number of milliseconds to pause after operation</p> 
                     

## setSpeedAndWait

<p xmlns="http://www.w3.org/1999/xhtml" className="p">setSpeedAndWait(value) Generated from setSpeed(value)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*value - the number of milliseconds to pause after operation</p> 
                     

## setTimeout

<p xmlns="http://www.w3.org/1999/xhtml" className="p">setTimeout(timeout) <strong className="ph b">Arguments</strong>: *timeout - a timeout in milliseconds, after which the action will return with an error</p> 
                     

## shiftKeyDown

<p xmlns="http://www.w3.org/1999/xhtml" className="p">shiftKeyDown()</p> 
                    

## shiftKeyDownAndWait

<p xmlns="http://www.w3.org/1999/xhtml" className="p">shiftKeyDownAndWait() Generated from shiftKeyDown()</p> 
                    

## shiftKeyUp

<p xmlns="http://www.w3.org/1999/xhtml" className="p">shiftKeyUp()</p> 
                    

## shiftKeyUpAndWait

<p xmlns="http://www.w3.org/1999/xhtml" className="p">shiftKeyUpAndWait() Generated from shiftKeyUp()</p> 
                    

## showElement

<p xmlns="http://www.w3.org/1999/xhtml" className="p">showElement</p> 
                    

## showElementAndWait

<p xmlns="http://www.w3.org/1999/xhtml" className="p">showElementAndWait</p> 
                    

## store

<p xmlns="http://www.w3.org/1999/xhtml" className="p">store(expression, variableName)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*expression - the value to store *variableName - the name of a variable in which the result is to be stored.</p> 
                     

## storeAlert

<p xmlns="http://www.w3.org/1999/xhtml" className="p">storeAlert(variableName) Generated from getAlert(). Returns: The message of the most recent JavaScript alert</p> 
                     

## storeAlertPresent

<p xmlns="http://www.w3.org/1999/xhtml" className="p">storeAlertPresent(variableName) Generated from isAlertPresent(). Returns: true if there is an alert</p> 
                     

## storeAllButtons

<p xmlns="http://www.w3.org/1999/xhtml" className="p">storeAllButtons(variableName) Generated from getAllButtons(). Returns: the IDs of all buttons on the page</p> 
                     

## storeAllFields

<p xmlns="http://www.w3.org/1999/xhtml" className="p">storeAllFields(variableName) Generated from getAllFields(). Returns: the IDs of all field on the page</p> 
                     

## storeAllLinks

<p xmlns="http://www.w3.org/1999/xhtml" className="p">storeAllLinks(variableName) Generated from getAllLinks(). Returns: the IDs of all links on the page</p> 
                     

## storeAllWindowIds

<p xmlns="http://www.w3.org/1999/xhtml" className="p">storeAllWindowIds(variableName) Generated from getAllWindowIds(). Returns: Array of identifiers of all windows that the browser knows about.</p> 
                     

## storeAllWindowNames

<p xmlns="http://www.w3.org/1999/xhtml" className="p">storeAllWindowNames(variableName) Generated from getAllWindowNames(). Returns: Array of names of all windows that the browser knows about.</p> 
                     

## storeAllWindowTitles

<p xmlns="http://www.w3.org/1999/xhtml" className="p">storeAllWindowTitles(variableName) Generated from getAllWindowTitles(). Returns: Array of titles of all windows that the browser knows about.</p> 
                     

## storeAndWait

<p xmlns="http://www.w3.org/1999/xhtml" className="p">storeAndWait(expression, variableName) Generated from store(expression, variableName)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*expression - the value to store *variableName - the name of a variable in which the result is to be stored.</p> 
                     

## storeAttribute

<p xmlns="http://www.w3.org/1999/xhtml" className="p">storeAttribute(attributeLocator, variableName) Generated from getAttribute(attributeLocator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*attributeLocator - an element locator followed by an @ sign and then the name of the attribute, e.g. "foo@bar" . Returns: the value of the specifie</p> 
                    

## storeAttributeFromAllWindows

<p xmlns="http://www.w3.org/1999/xhtml" className="p">storeAttributeFromAllWindows(attributeName, variableName) Generated from getAttributeFromAllWindows(attributeName)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*attributeName - name of an attribute on the windows . Returns: the set of values of this attribute from all known windows.</p> 
                     

## storeBodyText

<p xmlns="http://www.w3.org/1999/xhtml" className="p">storeBodyText(variableName) Generated from getBodyText(). Returns: the entire text of the page</p> 
                     

## storeChecked

<p xmlns="http://www.w3.org/1999/xhtml" className="p">storeChecked(locator, variableName) Generated from isChecked(locator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator pointing to a checkbox or radio button . Returns: true if the checkbox is checked, false otherwise</p> 
                     

## storeConfirmation

<p xmlns="http://www.w3.org/1999/xhtml" className="p">storeConfirmation(variableName) Generated from getConfirmation(). Returns: the message of the most recent JavaScript confirmation dialog</p> 
                     

## storeConfirmationPresent

<p xmlns="http://www.w3.org/1999/xhtml" className="p">storeConfirmationPresent(variableName) Generated from isConfirmationPresent(). Returns: true if there is a pending confirmation</p> 
                     

## storeCookie

<p xmlns="http://www.w3.org/1999/xhtml" className="p">storeCookie(variableName) Generated from getCookie(). Returns: all cookies of the current page under test</p> 
                     

## storeCookieByName

<p xmlns="http://www.w3.org/1999/xhtml" className="p">storeCookieByName(name, variableName) Generated from getCookieByName(name)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*name - the name of the cookie . Returns: the value of the cookie</p> 
                     

## storeCookiePresent

<p xmlns="http://www.w3.org/1999/xhtml" className="p">storeCookiePresent(name, variableName) Generated from isCookiePresent(name)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*name - the name of the cookie . Returns: true if a cookie with the specified name is present, or false otherwise.</p> 
                     

## storeCssCount

<p xmlns="http://www.w3.org/1999/xhtml" className="p">storeCssCount(css, variableName) Generated from getCssCount(css)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*css - the css selector to evaluate. do NOT wrap this expression in a 'count()' function; we will do that for you. Returns: the number of nodes that match the specified css sel</p> 
                    

## storeCursorPosition

<p xmlns="http://www.w3.org/1999/xhtml" className="p">storeCursorPosition(locator, variableName) Generated from getCursorPosition(locator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator pointing to an input element or textarea . Returns: the numerical position of the cursor in the field</p> 
                     

## storeEditable

<p xmlns="http://www.w3.org/1999/xhtml" className="p">storeEditable(locator, variableName) Generated from isEditable(locator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator . Returns: true if the input element is editable, false otherwise</p> 
                     

## storeElementHeight

<p xmlns="http://www.w3.org/1999/xhtml" className="p">storeElementHeight(locator, variableName) Generated from getElementHeight(locator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator pointing to an element . Returns: height of an element in pixels</p> 
                     

## storeElementIndex

<p xmlns="http://www.w3.org/1999/xhtml" className="p">storeElementIndex(locator, variableName) Generated from getElementIndex(locator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator pointing to an element . Returns: of relative index of the element to its parent (starting from 0)</p> 
                     

## storeElementPositionLeft

<p xmlns="http://www.w3.org/1999/xhtml" className="p">storeElementPositionLeft(locator, variableName) Generated from getElementPositionLeft(locator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator pointing to an element OR an element itself . Returns: of pixels from the edge of the frame.</p> 
                     

## storeElementPositionTop

<p xmlns="http://www.w3.org/1999/xhtml" className="p">storeElementPositionTop(locator, variableName) Generated from getElementPositionTop(locator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator pointing to an element OR an element itself . Returns: of pixels from the edge of the frame.</p> 
                     

## storeElementPresent

<p xmlns="http://www.w3.org/1999/xhtml" className="p">storeElementPresent(locator, variableName) Generated from isElementPresent(locator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator . Returns: true if the element is present, false otherwise</p> 
                     

## storeElementWidth

<p xmlns="http://www.w3.org/1999/xhtml" className="p">storeElementWidth(locator, variableName) Generated from getElementWidth(locator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator pointing to an element . Returns: width of an element in pixels</p> 
                     

## storeEval

<p xmlns="http://www.w3.org/1999/xhtml" className="p">storeEval(script, variableName) Generated from getEval(script)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*script - the JavaScript snippet to run . Returns: the results of evaluating the snippet</p> 
                     

## storeExpression

<p xmlns="http://www.w3.org/1999/xhtml" className="p">storeExpression(expression, variableName) Generated from getExpression(expression)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*expression - the value to return . Returns: the value passed in</p> 
                     

## storeHtmlSource

<p xmlns="http://www.w3.org/1999/xhtml" className="p">storeHtmlSource(variableName) Generated from getHtmlSource(). Returns: the entire HTML source</p> 
                     

## storeLocation

<p xmlns="http://www.w3.org/1999/xhtml" className="p">storeLocation(variableName) Generated from getLocation(). Returns: the absolute URL of the current page</p> 
                     

## storeMouseSpeed

<p xmlns="http://www.w3.org/1999/xhtml" className="p">storeMouseSpeed(variableName) Generated from getMouseSpeed(). Returns: the number of pixels between "mousemove" events during dragAndDrop commands (default=10)</p> 
                     

## storeOrdered

<p xmlns="http://www.w3.org/1999/xhtml" className="p">storeOrdered(locator1, locator2, variableName) Generated from isOrdered(locator1, locator2)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator1 - an element locator pointing to the first element *locator2 - an element locator pointing to the second element . Returns: true</p> 
                    

## storePrompt

<p xmlns="http://www.w3.org/1999/xhtml" className="p">storePrompt(variableName) Generated from getPrompt(). Returns: the message of the most recent JavaScript question prompt</p> 
                     

## storePromptPresent

<p xmlns="http://www.w3.org/1999/xhtml" className="p">storePromptPresent(variableName) Generated from isPromptPresent(). Returns: true if there is a pending prompt</p> 
                     

## storeSelectOptions

<p xmlns="http://www.w3.org/1999/xhtml" className="p">storeSelectOptions(selectLocator, variableName) Generated from getSelectOptions(selectLocator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*selectLocator - an element locator identifying a drop-down menu . Returns: an array of all option labels in the specified select drop-down</p> 
                     

## storeSelectedId

<p xmlns="http://www.w3.org/1999/xhtml" className="p">storeSelectedId(selectLocator, variableName) Generated from getSelectedId(selectLocator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*selectLocator - an element locator identifying a drop-down menu . Returns: the selected option ID in the specified select drop-down</p> 
                     

## storeSelectedIds

<p xmlns="http://www.w3.org/1999/xhtml" className="p">storeSelectedIds(selectLocator, variableName) Generated from getSelectedIds(selectLocator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*selectLocator - an element locator identifying a drop-down menu . Returns: an array of all selected option IDs in the specified select drop-down</p> 
                     

## storeSelectedIndex

<p xmlns="http://www.w3.org/1999/xhtml" className="p">storeSelectedIndex(selectLocator, variableName) Generated from getSelectedIndex(selectLocator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*selectLocator - an element locator identifying a drop-down menu . Returns: the selected option index in the specified select drop-down</p> 
                     

## storeSelectedIndexes

<p xmlns="http://www.w3.org/1999/xhtml" className="p">storeSelectedIndexes(selectLocator, variableName) Generated from getSelectedIndexes(selectLocator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*selectLocator - an element locator identifying a drop-down menu . Returns: an array of all selected option indexes in the specified selec</p> 
                    

## storeSelectedLabel

<p xmlns="http://www.w3.org/1999/xhtml" className="p">storeSelectedLabel(selectLocator, variableName) Generated from getSelectedLabel(selectLocator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*selectLocator - an element locator identifying a drop-down menu . Returns: the selected option label in the specified select drop-down</p> 
                     

## storeSelectedLabels

<p xmlns="http://www.w3.org/1999/xhtml" className="p">storeSelectedLabels(selectLocator, variableName) Generated from getSelectedLabels(selectLocator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*selectLocator - an element locator identifying a drop-down menu . Returns: an array of all selected option labels in the specified select d</p> 
                    

## storeSelectedValue

<p xmlns="http://www.w3.org/1999/xhtml" className="p">storeSelectedValue(selectLocator, variableName) Generated from getSelectedValue(selectLocator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*selectLocator - an element locator identifying a drop-down menu . Returns: the selected option value in the specified select drop-down</p> 
                     

## storeSelectedValues

<p xmlns="http://www.w3.org/1999/xhtml" className="p">storeSelectedValues(selectLocator, variableName) Generated from getSelectedValues(selectLocator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*selectLocator - an element locator identifying a drop-down menu . Returns: an array of all selected option values in the specified select d</p> 
                    

## storeSomethingSelected

<p xmlns="http://www.w3.org/1999/xhtml" className="p">storeSomethingSelected(selectLocator, variableName) Generated from isSomethingSelected(selectLocator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*selectLocator - an element locator identifying a drop-down menu . Returns: true if some option has been selected, false otherwise</p> 
                     

## storeSpeed

<p xmlns="http://www.w3.org/1999/xhtml" className="p">storeSpeed(variableName) Generated from getSpeed(). Returns: the execution speed in milliseconds.</p> 
                     

## storeTable

<p xmlns="http://www.w3.org/1999/xhtml" className="p">storeTable(tableCellAddress, variableName) Generated from getTable(tableCellAddress)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*tableCellAddress - a cell address, e.g. "foo.1.4" . Returns: the text from the specified cell</p> 
                     

## storeText

<p xmlns="http://www.w3.org/1999/xhtml" className="p">storeText(locator, variableName) Generated from getText(locator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator Returns: the text of the element</p> 
                     

## storeTextAndWait

<p xmlns="http://www.w3.org/1999/xhtml" className="p">storeTextAndWait(locator, variableName) Generated from getText(locator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator Returns: the text of the element</p> 
                     

## storeTextPresent

<p xmlns="http://www.w3.org/1999/xhtml" className="p">storeTextPresent(pattern, variableName) This command is deprecated. Use the storeText command with an element locator instead. Generated from isTextPresent(pattern)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*pattern - a pattern to match with the text of the page . Returns: true i</p> 
                    

## storeTitle

<p xmlns="http://www.w3.org/1999/xhtml" className="p">storeTitle(variableName) Generated from getTitle(). Returns: the title of the current page</p> 
                     

## storeTitleAndWait

<p xmlns="http://www.w3.org/1999/xhtml" className="p">storeTitleAndWait(variableName) Generated from getTitle(). Returns: the title of the current page</p> 
                     

## storeValue

<p xmlns="http://www.w3.org/1999/xhtml" className="p">storeValue(locator, variableName) Generated from getValue(locator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator Returns: the element value, or "on/off" for checkbox/radio elements</p> 
                     

## storeVisible

<p xmlns="http://www.w3.org/1999/xhtml" className="p">storeVisible(locator, variableName) Generated from isVisible(locator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator Returns: true if the specified element is visible, false otherwise</p> 
                     

## storeWhetherThisFrameMatchFrameExpression

<p xmlns="http://www.w3.org/1999/xhtml" className="p">storeWhetherThisFrameMatchFrameExpression(currentFrameString, target, variableName) Generated from getWhetherThisFrameMatchFrameExpression(currentFrameString, target)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*currentFrameString - starting frame *target - new frame (which might be</p> 
                     

## storeWhetherThisWindowMatchWindowExpression

 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">storeWhetherThisWindowMatchWindowExpression(currentWindowString, target, variableName) Generated from getWhetherThisWindowMatchWindowExpression(currentWindowString, target)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*currentWindowString - starting window *target - new window (which</p> 
                     

## storeXpathCount

<p xmlns="http://www.w3.org/1999/xhtml" className="p">storeXpathCount(xpath, variableName) Generated from getXpathCount(xpath)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*xpath - the xpath expression to evaluate. do NOT wrap this expression in a 'count()' function; we will do that for you. Returns: the number of nodes that match the spe</p> 
                    

## submit

<p xmlns="http://www.w3.org/1999/xhtml" className="p">submit(formLocator) <strong className="ph b">Arguments</strong>: *formLocator - an element locator for the form you want to submit</p> 
                     

## submitAndWait

<p xmlns="http://www.w3.org/1999/xhtml" className="p">submitAndWait(formLocator) Generated from submit(formLocator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*formLocator - an element locator for the form you want to submit</p> 
                     

## type

<p xmlns="http://www.w3.org/1999/xhtml" className="p">type(locator, value)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator *value - the value to type</p> 
                     

## typeAndWait

<p xmlns="http://www.w3.org/1999/xhtml" className="p">typeAndWait(locator, value) Generated from type(locator, value)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator *value - the value to type</p> 
                     

## typeKeys

<p xmlns="http://www.w3.org/1999/xhtml" className="p">typeKeys(locator, value) This command is deprecated. Use the sendKeys command instead.</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator *value - the value to type</p> 
                     

## typeKeysAndWait

<p xmlns="http://www.w3.org/1999/xhtml" className="p">typeKeysAndWait(locator, value) This command is deprecated. Use the sendKeysAndWait command instead. Generated from typeKeys(locator, value)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator *value - the value to type</p> 
                     

## uncheck

<p xmlns="http://www.w3.org/1999/xhtml" className="p">uncheck(locator) <strong className="ph b">Arguments</strong>: *locator - an element locator</p> 
                     

## uncheckAndWait

<p xmlns="http://www.w3.org/1999/xhtml" className="p">uncheckAndWait(locator) Generated from uncheck(locator) Arguments: *locator - an element locator</p> 
                    

## useXpathLibrary

<p xmlns="http://www.w3.org/1999/xhtml" className="p">useXpathLibrary(libraryName) <strong className="ph b">Arguments</strong>: *libraryName - name of the desired library Only the following three can be chosen: "ajaxslt" - Google's library, "javascript-xpath" - Cybozu Labs' faster library, "default" - The defau</p> 
                    

## useXpathLibraryAndWait

<p xmlns="http://www.w3.org/1999/xhtml" className="p">useXpathLibraryAndWait(libraryName) Generated from useXpathLibrary(libraryName)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*libraryName - name of the desired library Only the following three can be chosen: "ajaxslt" - Google's library, "javascript-xpath" - Cybozu La</p> 
                    

## verifyAlert

<p xmlns="http://www.w3.org/1999/xhtml" className="p">verifyAlert(pattern) Generated from getAlert(). Returns: The message of the most recent JavaScript alert</p> 
                     

## verifyAlertNotPresent

<p xmlns="http://www.w3.org/1999/xhtml" className="p">verifyAlertNotPresent() Generated from isAlertPresent(). Returns: true if there is an alert</p> 
                     

## verifyAlertPresent

<p xmlns="http://www.w3.org/1999/xhtml" className="p">verifyAlertPresent() Generated from isAlertPresent(). Returns: true if there is an alert</p> 
                     

## verifyAllButtons

<p xmlns="http://www.w3.org/1999/xhtml" className="p">verifyAllButtons(pattern) Generated from getAllButtons(). Returns: the IDs of all buttons on the page</p> 
                     

## verifyAllFields

<p xmlns="http://www.w3.org/1999/xhtml" className="p">verifyAllFields(pattern) Generated from getAllFields(). Returns: the IDs of all field on the page</p> 
                     

## verifyAllLinks

<p xmlns="http://www.w3.org/1999/xhtml" className="p">verifyAllLinks(pattern) Generated from getAllLinks(). Returns: the IDs of all links on the page</p> 
                     

## verifyAllWindowIds

<p xmlns="http://www.w3.org/1999/xhtml" className="p">verifyAllWindowIds(pattern) Generated from getAllWindowIds(). Returns: Array of identifiers of all windows that the browser knows about.</p> 
                     

## verifyAllWindowNames

<p xmlns="http://www.w3.org/1999/xhtml" className="p">verifyAllWindowNames(pattern) Generated from getAllWindowNames(). Returns: Array of names of all windows that the browser knows about.</p> 
                     

## verifyAllWindowTitles

<p xmlns="http://www.w3.org/1999/xhtml" className="p">verifyAllWindowTitles(pattern) Generated from getAllWindowTitles(). Returns: Array of titles of all windows that the browser knows about.</p> 
                     

## verifyAttribute

<p xmlns="http://www.w3.org/1999/xhtml" className="p">verifyAttribute(attributeLocator, pattern) Generated from getAttribute(attributeLocator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*attributeLocator - an element locator followed by an @ sign and then the name of the attribute, e.g. "foo@bar" . Returns: the value of the specified a</p> 
                    

## verifyAttributeFromAllWindows

<p xmlns="http://www.w3.org/1999/xhtml" className="p">verifyAttributeFromAllWindows(attributeName, pattern) Generated from getAttributeFromAllWindows(attributeName)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*attributeName - name of an attribute on the windows. Returns: the set of values of this attribute from all known windows.</p> 
                     

## verifyBodyText

<p xmlns="http://www.w3.org/1999/xhtml" className="p">verifyBodyText(pattern) Generated from getBodyText(). Returns: the entire text of the page</p> 
                     

## verifyChecked

<p xmlns="http://www.w3.org/1999/xhtml" className="p">verifyChecked(locator) Generated from isChecked(locator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator pointing to a checkbox or radio button . Returns: true if the checkbox is checked, false otherwise</p> 
                     

## verifyConfirmation

<p xmlns="http://www.w3.org/1999/xhtml" className="p">verifyConfirmation(pattern) Generated from getConfirmation(). Returns: the message of the most recent JavaScript confirmation dialog</p> 
                     

## verifyConfirmationNotPresent

<p xmlns="http://www.w3.org/1999/xhtml" className="p">verifyConfirmationNotPresent() Generated from isConfirmationPresent(). Returns: true if there is a pending confirmation</p> 
                     

## verifyConfirmationPresent

<p xmlns="http://www.w3.org/1999/xhtml" className="p">verifyConfirmationPresent() Generated from isConfirmationPresent(). Returns: true if there is a pending confirmation</p> 
                     

## verifyCookie

<p xmlns="http://www.w3.org/1999/xhtml" className="p">verifyCookie(pattern) Generated from getCookie(). Returns: all cookies of the current page under test</p> 
                     

## verifyCookieByName

<p xmlns="http://www.w3.org/1999/xhtml" className="p">verifyCookieByName(name, pattern) Generated from getCookieByName(name)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*name - the name of the cookie . Returns: the value of the cookie</p> 
                     

## verifyCookieNotPresent

<p xmlns="http://www.w3.org/1999/xhtml" className="p">verifyCookieNotPresent(name) Generated from isCookiePresent(name) Arguments: *name - the name of the cookie . Returns: true if a cookie with the specified name is present, or false otherwise.</p> 
                     

## verifyCookiePresent

<p xmlns="http://www.w3.org/1999/xhtml" className="p">verifyCookiePresent(name) Generated from isCookiePresent(name)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*name - the name of the cookie . Returns: true if a cookie with the specified name is present, or false otherwise.</p> 
                     

## verifyCssCount

<p xmlns="http://www.w3.org/1999/xhtml" className="p">verifyCssCount(css, pattern) Generated from getCssCount(css)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*css - the css selector to evaluate. do NOT wrap this expression in a 'count()' function; we will do that for you. Returns: the number of nodes that match the specified css select</p> 
                    

## verifyCursorPosition

<p xmlns="http://www.w3.org/1999/xhtml" className="p">verifyCursorPosition(locator, pattern) Generated from getCursorPosition(locator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator pointing to an input element or textarea . Returns: the numerical position of the cursor in the field</p> 
                     

## verifyEditable

<p xmlns="http://www.w3.org/1999/xhtml" className="p">verifyEditable(locator) Generated from isEditable(locator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator Returns: true if the input element is editable, false otherwise</p> 
                     

## verifyElementHeight

<p xmlns="http://www.w3.org/1999/xhtml" className="p">verifyElementHeight(locator, pattern) Generated from getElementHeight(locator) Arguments: *locator - an element locator pointing to an element . Returns: height of an element in pixels</p> 
                     

## verifyElementIndex

<p xmlns="http://www.w3.org/1999/xhtml" className="p">verifyElementIndex(locator, pattern) Generated from getElementIndex(locator) Arguments: *locator - an element locator pointing to an element . Returns: of relative index of the element to its parent (starting from 0)</p> 
                     

## verifyElementNotPresent

<p xmlns="http://www.w3.org/1999/xhtml" className="p">verifyElementNotPresent(locator) Generated from isElementPresent(locator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator Returns: true if the element is not present, false otherwise</p> 
                     

## verifyElementPositionLeft

<p xmlns="http://www.w3.org/1999/xhtml" className="p">verifyElementPositionLeft(locator, pattern) Generated from getElementPositionLeft(locator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator pointing to an element OR an element itself . Returns: of pixels from the edge of the frame.</p> 
                     

## verifyElementPositionTop

<p xmlns="http://www.w3.org/1999/xhtml" className="p">verifyElementPositionTop(locator, pattern) Generated from getElementPositionTop(locator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator pointing to an element OR an element itself . Returns: of pixels from the edge of the frame.</p> 
                     

## verifyElementPresent

<p xmlns="http://www.w3.org/1999/xhtml" className="p">verifyElementPresent(locator) Generated from isElementPresent(locator) Arguments: *locator - an element locator Returns: true if the element is present, false otherwise</p> 
                     

## verifyElementWidth

<p xmlns="http://www.w3.org/1999/xhtml" className="p">verifyElementWidth(locator, pattern) Generated from getElementWidth(locator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator pointing to an element . Returns: width of an element in pixels</p> 
                     

## verifyEval

<p xmlns="http://www.w3.org/1999/xhtml" className="p">verifyEval(script, pattern) Generated from getEval(script)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*script - the JavaScript snippet to run . Returns: the results of evaluating the snippet</p> 
                     

## verifyExpression

<p xmlns="http://www.w3.org/1999/xhtml" className="p">verifyExpression(expression, pattern) Generated from getExpression(expression)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*expression - the value to return . Returns: the value passed in</p> 
                     

## verifyHtmlSource

<p xmlns="http://www.w3.org/1999/xhtml" className="p">verifyHtmlSource(pattern) Generated from getHtmlSource(). Returns: the entire HTML source</p> 
                     

## verifyLocation

<p xmlns="http://www.w3.org/1999/xhtml" className="p">verifyLocation(pattern) Generated from getLocation(). Returns: the absolute URL of the current page</p> 
                     

## verifyMouseSpeed

<p xmlns="http://www.w3.org/1999/xhtml" className="p">verifyMouseSpeed(pattern) Generated from getMouseSpeed(). Returns: the number of pixels between "mousemove" events during dragAndDrop commands (default=10)</p> 
                     

## verifyNotAlert

<p xmlns="http://www.w3.org/1999/xhtml" className="p">verifyNotAlert(pattern) Generated from getAlert(). Returns: The message of the most recent JavaScript alert</p> 
                     

## verifyNotAllButtons

<p xmlns="http://www.w3.org/1999/xhtml" className="p">verifyNotAllButtons(pattern) Generated from getAllButtons(). Returns: the IDs of all buttons on the page</p> 
                     

## verifyNotAllFields

<p xmlns="http://www.w3.org/1999/xhtml" className="p">verifyNotAllFields(pattern) Generated from getAllFields(). Returns: the IDs of all field on the page</p> 
                     

## verifyNotAllLinks

<p xmlns="http://www.w3.org/1999/xhtml" className="p">verifyNotAllLinks(pattern) Generated from getAllLinks(). Returns: the IDs of all links on the page</p> 
                     

## verifyNotAllWindowIds

<p xmlns="http://www.w3.org/1999/xhtml" className="p">verifyNotAllWindowIds(pattern) Generated from getAllWindowIds(). Returns: Array of identifiers of all windows that the browser knows about.</p> 
                     

## verifyNotAllWindowNames

<p xmlns="http://www.w3.org/1999/xhtml" className="p">verifyNotAllWindowNames(pattern) Generated from getAllWindowNames(). Returns: Array of names of all windows that the browser knows about.</p> 
                     

## verifyNotAllWindowTitles

<p xmlns="http://www.w3.org/1999/xhtml" className="p">verifyNotAllWindowTitles(pattern) Generated from getAllWindowTitles(). Returns: Array of titles of all windows that the browser knows about.</p> 
                     

## verifyNotAttribute

<p xmlns="http://www.w3.org/1999/xhtml" className="p">verifyNotAttribute(attributeLocator, pattern) Generated from getAttribute(attributeLocator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*attributeLocator - an element locator followed by an @ sign and then the name of the attribute, e.g. "foo@bar" . Returns: the value of the specifie</p> 
                    

## verifyNotAttributeFromAllWindows

<p xmlns="http://www.w3.org/1999/xhtml" className="p">verifyNotAttributeFromAllWindows(attributeName, pattern) Generated from getAttributeFromAllWindows(attributeName)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*attributeName - name of an attribute on the windows . Returns: the set of values of this attribute from all known windows.</p> 
                     

## verifyNotBodyText

<p xmlns="http://www.w3.org/1999/xhtml" className="p">verifyNotBodyText(pattern) Generated from getBodyText(). Returns: the entire text of the page</p> 
                     

## verifyNotChecked

<p xmlns="http://www.w3.org/1999/xhtml" className="p">verifyNotChecked(locator) Generated from isChecked(locator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator pointing to a checkbox or radio button . Returns: true if the checkbox is checked, false otherwise</p> 
                     

## verifyNotConfirmation

<p xmlns="http://www.w3.org/1999/xhtml" className="p">verifyNotConfirmation(pattern) Generated from getConfirmation(). Returns: the message of the most recent JavaScript confirmation dialog</p> 
                     

## verifyNotCookie

<p xmlns="http://www.w3.org/1999/xhtml" className="p">verifyNotCookie(pattern) Generated from getCookie(). Returns: all cookies of the current page under test</p> 
                     

## verifyNotCookieByName

<p xmlns="http://www.w3.org/1999/xhtml" className="p">verifyNotCookieByName(name, pattern) Generated from getCookieByName(name)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*name - the name of the cookie . Returns: the value of the cookie</p> 
                     

## verifyNotCssCount

<p xmlns="http://www.w3.org/1999/xhtml" className="p">verifyNotCssCount(css, pattern) Generated from getCssCount(css)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*css - the css selector to evaluate. do NOT wrap this expression in a 'count()' function; we will do that for you. Returns: the number of nodes that match the specified css sel</p> 
                    

## verifyNotCursorPosition

<p xmlns="http://www.w3.org/1999/xhtml" className="p">verifyNotCursorPosition(locator, pattern) Generated from getCursorPosition(locator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator pointing to an input element or textarea . Returns: the numerical position of the cursor in the field</p> 
                     

## verifyNotEditable

<p xmlns="http://www.w3.org/1999/xhtml" className="p">verifyNotEditable(locator) Generated from isEditable(locator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator Returns: true if the input element is editable, false otherwise</p> 
                     

## verifyNotElementHeight

<p xmlns="http://www.w3.org/1999/xhtml" className="p">verifyNotElementHeight(locator, pattern) Generated from getElementHeight(locator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator pointing to an element . Returns: height of an element in pixels</p> 
                     

## verifyNotElementIndex

<p xmlns="http://www.w3.org/1999/xhtml" className="p">verifyNotElementIndex(locator, pattern) Generated from getElementIndex(locator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator pointing to an element . Returns: of relative index of the element to its parent (starting from 0)</p> 
                     

## verifyNotElementPositionLeft

<p xmlns="http://www.w3.org/1999/xhtml" className="p">verifyNotElementPositionLeft(locator, pattern) Generated from getElementPositionLeft(locator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator pointing to an element OR an element itself . Returns: of pixels from the edge of the frame.</p> 
                     

## verifyNotElementPositionTop

<p xmlns="http://www.w3.org/1999/xhtml" className="p">verifyNotElementPositionTop(locator, pattern) Generated from getElementPositionTop(locator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator pointing to an element OR an element itself . Returns: of pixels from the edge of the frame.</p> 
                     

## verifyNotElementWidth

<p xmlns="http://www.w3.org/1999/xhtml" className="p">verifyNotElementWidth(locator, pattern) Generated from getElementWidth(locator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator pointing to an element . Returns: width of an element in pixels</p> 
                     

## verifyNotEval

<p xmlns="http://www.w3.org/1999/xhtml" className="p">verifyNotEval(script, pattern) Generated from getEval(script)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*script - the JavaScript snippet to run . Returns: the results of evaluating the snippet</p> 
                     

## verifyNotExpression

<p xmlns="http://www.w3.org/1999/xhtml" className="p">verifyNotExpression(expression, pattern) Generated from getExpression(expression)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*expression - the value to return . Returns: the value passed in</p> 
                     

## verifyNotHtmlSource

<p xmlns="http://www.w3.org/1999/xhtml" className="p">verifyNotHtmlSource(pattern) Generated from getHtmlSource(). Returns: the entire HTML source</p> 
                     

## verifyNotLocation

<p xmlns="http://www.w3.org/1999/xhtml" className="p">verifyNotLocation(pattern) Generated from getLocation(). Returns: the absolute URL of the current page</p> 
                     

## verifyNotMouseSpeed

<p xmlns="http://www.w3.org/1999/xhtml" className="p">verifyNotMouseSpeed(pattern) Generated from getMouseSpeed(). Returns: the number of pixels between "mousemove" events during dragAndDrop commands (default=10)</p> 
                     

## verifyNotOrdered

<p xmlns="http://www.w3.org/1999/xhtml" className="p">verifyNotOrdered(locator1, locator2) Generated from isOrdered(locator1, locator2)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator1 - an element locator pointing to the first element *locator2 - an element locator pointing to the second element . Returns: true if elemen</p> 
                    

## verifyNotPrompt

<p xmlns="http://www.w3.org/1999/xhtml" className="p">verifyNotPrompt(pattern) Generated from getPrompt(). Returns: the message of the most recent JavaScript question prompt</p> 
                     

## verifyNotSelectOptions

<p xmlns="http://www.w3.org/1999/xhtml" className="p">verifyNotSelectOptions(selectLocator, pattern) Generated from getSelectOptions(selectLocator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*selectLocator - an element locator identifying a drop-down menu . Returns: an array of all option labels in the specified select drop-down</p> 
                     

## verifyNotSelectedId

<p xmlns="http://www.w3.org/1999/xhtml" className="p">verifyNotSelectedId(selectLocator, pattern) Generated from getSelectedId(selectLocator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*selectLocator - an element locator identifying a drop-down menu . Returns: the selected option ID in the specified select drop-down</p> 
                     

## verifyNotSelectedIds

<p xmlns="http://www.w3.org/1999/xhtml" className="p">verifyNotSelectedIds(selectLocator, pattern) Generated from getSelectedIds(selectLocator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*selectLocator - an element locator identifying a drop-down menu . Returns: an array of all selected option IDs in the specified select drop-down</p> 
                     

## verifyNotSelectedIndex

<p xmlns="http://www.w3.org/1999/xhtml" className="p">verifyNotSelectedIndex(selectLocator, pattern) Generated from getSelectedIndex(selectLocator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*selectLocator - an element locator identifying a drop-down menu . Returns: the selected option index in the specified select drop-down</p> 
                     

## verifyNotSelectedIndexes

<p xmlns="http://www.w3.org/1999/xhtml" className="p">verifyNotSelectedIndexes(selectLocator, pattern) Generated from getSelectedIndexes(selectLocator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*selectLocator - an element locator identifying a drop-down menu . Returns: an array of all selected option indexes in the specified select</p> 
                    

## verifyNotSelectedLabel

<p xmlns="http://www.w3.org/1999/xhtml" className="p">verifyNotSelectedLabel(selectLocator, pattern) Generated from getSelectedLabel(selectLocator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*selectLocator - an element locator identifying a drop-down menu . Returns: the selected option label in the specified select drop-down</p> 
                     

## verifyNotSelectedLabels

<p xmlns="http://www.w3.org/1999/xhtml" className="p">verifyNotSelectedLabels(selectLocator, pattern) Generated from getSelectedLabels(selectLocator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*selectLocator - an element locator identifying a drop-down menu . Returns: an array of all selected option labels in the specified select dr</p> 
                    

## verifyNotSelectedValue

<p xmlns="http://www.w3.org/1999/xhtml" className="p">verifyNotSelectedValue(selectLocator, pattern) Generated from getSelectedValue(selectLocator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*selectLocator - an element locator identifying a drop-down menu . Returns: the selected option value in the specified select drop-down</p> 
                     

## verifyNotSelectedValues

<p xmlns="http://www.w3.org/1999/xhtml" className="p">verifyNotSelectedValues(selectLocator, pattern) Generated from getSelectedValues(selectLocator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*selectLocator - an element locator identifying a drop-down menu . Returns: an array of all selected option values in the specified select dr</p> 
                    

## verifyNotSomethingSelected

<p xmlns="http://www.w3.org/1999/xhtml" className="p">verifyNotSomethingSelected(selectLocator) Generated from isSomethingSelected(selectLocator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*selectLocator - an element locator identifying a drop-down menu . Returns: true if some option has been selected, false otherwise</p> 
                     

## verifyNotSpeed

<p xmlns="http://www.w3.org/1999/xhtml" className="p">verifyNotSpeed(pattern) Generated from getSpeed(). Returns: the execution speed in milliseconds.</p> 
                     

## verifyNotTable

<p xmlns="http://www.w3.org/1999/xhtml" className="p">verifyNotTable(tableCellAddress, pattern) Generated from getTable(tableCellAddress)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*tableCellAddress - a cell address, e.g. "foo.1.4" . Returns: the text from the specified cell</p> 
                     

## verifyNotText

<p xmlns="http://www.w3.org/1999/xhtml" className="p">verifyNotText(locator, pattern) Generated from getText(locator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator . Returns: the text of the element</p> 
                     

## verifyNotTitle

<p xmlns="http://www.w3.org/1999/xhtml" className="p">verifyNotTitle(pattern) Generated from getTitle(). Returns: the title of the current page</p> 
                     

## verifyNotValue

<p xmlns="http://www.w3.org/1999/xhtml" className="p">verifyNotValue(locator, pattern) Generated from getValue(locator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator . Returns: the element value, or "on/off" for checkbox/radio elements</p> 
                     

## verifyNotVisible

<p xmlns="http://www.w3.org/1999/xhtml" className="p">verifyNotVisible(locator) Generated from isVisible(locator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator . Returns: true if the specified element is visible, false otherwise</p> 
                     

## verifyNotWhetherThisFrameMatchFrameExpression

 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">verifyNotWhetherThisFrameMatchFrameExpression(currentFrameString, target, pattern) Generated from getWhetherThisFrameMatchFrameExpression(currentFrameString, target)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*currentFrameString - starting frame *target - new frame (which might be r</p> 
                    

## verifyNotWhetherThisWindowMatchWindowExpression

 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">verifyNotWhetherThisWindowMatchWindowExpression(currentWindowString, target, pattern) Generated from getWhetherThisWindowMatchWindowExpression(currentWindowString, target)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*currentWindowString - starting window *target - new window (which m</p> 
                    

## verifyNotXpathCount

<p xmlns="http://www.w3.org/1999/xhtml" className="p">verifyNotXpathCount(xpath, pattern) Generated from getXpathCount(xpath)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*xpath - the xpath expression to evaluate. do NOT wrap this expression in a 'count()' function; we will do that for you. Returns: the number of nodes that match the spe</p> 
                    

## verifyOrdered

<p xmlns="http://www.w3.org/1999/xhtml" className="p">verifyOrdered(locator1, locator2) Generated from isOrdered(locator1, locator2)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator1 - an element locator pointing to the first element *locator2 - an element locator pointing to the second element . Returns: true if element1</p> 
                     

## verifyPrompt

<p xmlns="http://www.w3.org/1999/xhtml" className="p">verifyPrompt(pattern) Generated from getPrompt(). Returns: the message of the most recent JavaScript question prompt</p> 
                     

## verifyPromptNotPresent

<p xmlns="http://www.w3.org/1999/xhtml" className="p">verifyPromptNotPresent() Generated from isPromptPresent(). Returns: true if there is a pending prompt</p> 
                     

## verifyPromptPresent

<p xmlns="http://www.w3.org/1999/xhtml" className="p">verifyPromptPresent() Generated from isPromptPresent(). Returns: true if there is a pending prompt</p> 
                     

## verifySelectOptions

<p xmlns="http://www.w3.org/1999/xhtml" className="p">verifySelectOptions(selectLocator, pattern) Generated from getSelectOptions(selectLocator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*selectLocator - an element locator identifying a drop-down menu . Returns: an array of all option labels in the specified select drop-down</p> 
                     

## verifySelectedId

<p xmlns="http://www.w3.org/1999/xhtml" className="p">verifySelectedId(selectLocator, pattern) Generated from getSelectedId(selectLocator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*selectLocator - an element locator identifying a drop-down menu . Returns: the selected option ID in the specified select drop-down</p> 
                     

## verifySelectedIds

<p xmlns="http://www.w3.org/1999/xhtml" className="p">verifySelectedIds(selectLocator, pattern) Generated from getSelectedIds(selectLocator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*selectLocator - an element locator identifying a drop-down menu . Returns: an array of all selected option IDs in the specified select drop-down</p> 
                     

## verifySelectedIndex

<p xmlns="http://www.w3.org/1999/xhtml" className="p">verifySelectedIndex(selectLocator, pattern) Generated from getSelectedIndex(selectLocator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*selectLocator - an element locator identifying a drop-down menu . Returns: the selected option index in the specified select drop-down</p> 
                     

## verifySelectedIndexes

<p xmlns="http://www.w3.org/1999/xhtml" className="p">verifySelectedIndexes(selectLocator, pattern) Generated from getSelectedIndexes(selectLocator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*selectLocator - an element locator identifying a drop-down menu . Returns: an array of all selected option indexes in the specified select dr</p> 
                    

## verifySelectedLabel

<p xmlns="http://www.w3.org/1999/xhtml" className="p">verifySelectedLabel(selectLocator, pattern) Generated from getSelectedLabel(selectLocator) Arguments: *selectLocator - an element locator identifying a drop-down menu . Returns: the selected option label in the specified select drop-down</p> 
                     

## verifySelectedLabels

<p xmlns="http://www.w3.org/1999/xhtml" className="p">verifySelectedLabels(selectLocator, pattern) Generated from getSelectedLabels(selectLocator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*selectLocator - an element locator identifying a drop-down menu . Returns: an array of all selected option labels in the specified select drop-</p> 
                    

## verifySelectedValue

<p xmlns="http://www.w3.org/1999/xhtml" className="p">verifySelectedValue(selectLocator, pattern) Generated from getSelectedValue(selectLocator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*selectLocator - an element locator identifying a drop-down menu . Returns: the selected option value in the specified select drop-down</p> 
                     

## verifySelectedValues

<p xmlns="http://www.w3.org/1999/xhtml" className="p">verifySelectedValues(selectLocator, pattern) Generated from getSelectedValues(selectLocator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*selectLocator - an element locator identifying a drop-down menu . Returns: an array of all selected option values in the specified select drop-</p> 
                    

## verifySomethingSelected

<p xmlns="http://www.w3.org/1999/xhtml" className="p">verifySomethingSelected(selectLocator) Generated from isSomethingSelected(selectLocator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*selectLocator - an element locator identifying a drop-down menu . Returns: true if some option has been selected, false otherwise</p> 
                     

## verifySpeed

<p xmlns="http://www.w3.org/1999/xhtml" className="p">verifySpeed(pattern) Generated from getSpeed(). Returns: the execution speed in milliseconds.</p> 
                     

## verifyTable

<p xmlns="http://www.w3.org/1999/xhtml" className="p">verifyTable(tableCellAddress, pattern) Generated from getTable(tableCellAddress)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*tableCellAddress - a cell address, e.g. "foo.1.4" . Returns: the text from the specified cell</p> 
                     

## verifyText

<p xmlns="http://www.w3.org/1999/xhtml" className="p">verifyText(locator, pattern) Generated from getText(locator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator Returns: the text of the element</p> 
                     

## verifyTextAndWait

<p xmlns="http://www.w3.org/1999/xhtml" className="p">verifyTextAndWait(locator, pattern) Generated from getText(locator) Arguments: *locator - an element locator Returns: the text of the element</p> 
                     

## verifyTextNotPresent

<p xmlns="http://www.w3.org/1999/xhtml" className="p">verifyTextNotPresent(pattern) This command is deprecated. Use the verifyNotText command with an element locator instead. Generated from isTextPresent(pattern)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*pattern - a pattern to match with the text of the page . Returns: true if the</p> 
                     

## verifyTextPresent

<p xmlns="http://www.w3.org/1999/xhtml" className="p">verifyTextPresent(pattern) This command is deprecated. Use the verifyText command with an element locator instead. Generated from isTextPresent(pattern)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*pattern - a pattern to match with the text of the page . Returns: true if the patter</p> 
                    

## verifyTitle

<p xmlns="http://www.w3.org/1999/xhtml" className="p"> </p> 
                    

## verifyTitleAndWait

<p xmlns="http://www.w3.org/1999/xhtml" className="p">verifyTitleAndWait(pattern) Generated from getTitle(). Returns: the title of the current page</p> 
                     

## verifyValue

<p xmlns="http://www.w3.org/1999/xhtml" className="p">verifyValue(locator, pattern) Generated from getValue(locator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator Returns: the element value, or "on/off" for checkbox/radio elements</p> 
                     

## verifyVisible

<p xmlns="http://www.w3.org/1999/xhtml" className="p">verifyVisible(locator) Generated from isVisible(locator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator Returns: true if the specified element is visible, false otherwise</p> 
                     

## verifyWhetherThisFrameMatchFrameExpression

<p xmlns="http://www.w3.org/1999/xhtml" className="p">verifyWhetherThisFrameMatchFrameExpression(currentFrameString, target, pattern) Generated from getWhetherThisFrameMatchFrameExpression(currentFrameString, target)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*currentFrameString - starting frame *target - new frame (which might be rela</p> 
                    

## verifyWhetherThisWindowMatchWindowExpression

 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">verifyWhetherThisWindowMatchWindowExpression(currentWindowString, target, pattern) Generated from getWhetherThisWindowMatchWindowExpression(currentWindowString, target)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*currentWindowString - starting window *target - new window (which migh</p> 
                    

## verifyXpathCount

<p xmlns="http://www.w3.org/1999/xhtml" className="p">verifyXpathCount(xpath, pattern) Generated from getXpathCount(xpath)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*xpath - the xpath expression to evaluate. do NOT wrap this expression in a 'count()' function; we will do that for you. Returns: the number of nodes that match the specif</p> 
                    

## waitForAlert

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForAlert(pattern) Generated from getAlert(). Returns: The message of the most recent JavaScript alert</p> 
                     

## waitForAlertNotPresent

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForAlertNotPresent() Generated from isAlertPresent(). Returns: true if there is an alert</p> 
                     

## waitForAlertPresent

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForAlertPresent() Generated from isAlertPresent(). Returns: true if there is an alert</p> 
                     

## waitForAllButtons

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForAllButtons(pattern) Generated from getAllButtons(). Returns: the IDs of all buttons on the page</p> 
                     

## waitForAllFields

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForAllFields(pattern) Generated from getAllFields(). Returns: the IDs of all field on the page</p> 
                     

## waitForAllLinks

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForAllLinks(pattern) Generated from getAllLinks(). Returns: the IDs of all links on the page</p> 
                     

## waitForAllWindowIds

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForAllWindowIds(pattern) Generated from getAllWindowIds(). Returns: Array of identifiers of all windows that the browser knows about.</p> 
                     

## waitForAllWindowNames

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForAllWindowNames(pattern) Generated from getAllWindowNames(). Returns: Array of names of all windows that the browser knows about.</p> 
                     

## waitForAllWindowTitles

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForAllWindowTitles(pattern) Generated from getAllWindowTitles(). Returns: Array of titles of all windows that the browser knows about.</p> 
                     

## waitForAttribute

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForAttribute(attributeLocator, pattern) Generated from getAttribute(attributeLocator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*attributeLocator - an element locator followed by an @ sign and then the name of the attribute, e.g. "foo@bar" . Returns: the value of the specified</p> 
                     

## waitForAttributeFromAllWindows

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForAttributeFromAllWindows(attributeName, pattern) Generated from getAttributeFromAllWindows(attributeName)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*attributeName - name of an attribute on the windows . Returns: the set of values of this attribute from all known windows.</p> 
                     

## waitForBodyText

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForBodyText(pattern) Generated from getBodyText(). Returns: the entire text of the page</p> 
                     

## waitForChecked

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForChecked(locator) Generated from isChecked(locator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator pointing to a checkbox or radio button . Returns: true if the checkbox is checked, false otherwise</p> 
                     

## waitForCondition

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForCondition(script, timeout)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*script - the JavaScript snippet to run *timeout - a timeout in milliseconds, after which this command will return with an error</p> 
                     

## waitForConfirmation

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForConfirmation(pattern) Generated from getConfirmation(). Returns: the message of the most recent JavaScript confirmation dialog</p> 
                     

## waitForConfirmationNotPresent

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForConfirmationNotPresent() Generated from isConfirmationPresent(). Returns: true if there is a pending confirmation</p> 
                     

## waitForConfirmationPresent

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForConfirmationPresent() Generated from isConfirmationPresent(). Returns: true if there is a pending confirmation</p> 
                     

## waitForCookie

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForCookie(pattern) Generated from getCookie(). Returns: all cookies of the current page under test</p> 
                     

## waitForCookieByName

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForCookieByName(name, pattern) Generated from getCookieByName(name) Arguments: *name - the name of the cookie . Returns: the value of the cookie</p> 
                     

## waitForCookieNotPresent

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForCookieNotPresent(name) Generated from isCookiePresent(name) Arguments: *name - the name of the cookie . Returns: true if a cookie with the specified name is present, or false otherwise.</p> 
                     

## waitForCookiePresent

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForCookiePresent(name) Generated from isCookiePresent(name) Arguments: *name - the name of the cookie . Returns: true if a cookie with the specified name is present, or false otherwise.</p> 
                     

## waitForCssCount

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForCssCount(css, pattern) Generated from getCssCount(css) Arguments: *css - the css selector to evaluate. do NOT wrap this expression in a 'count()' function; we will do that for you. . Returns: the number of nodes that match the specified css selecto</p> 
                    

## waitForCursorPosition

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForCursorPosition(locator, pattern) Generated from getCursorPosition(locator) Arguments: *locator - an element locator pointing to an input element or textarea . Returns: the numerical position of the cursor in the field</p> 
                     

## waitForEditable

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForEditable(locator) Generated from isEditable(locator) Arguments: *locator - an element locator . Returns: true if the input element is editable, false otherwise</p> 
                     

## waitForElementHeight

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForElementHeight(locator, pattern) Generated from getElementHeight(locator) Arguments: *locator - an element locator pointing to an element . Returns: height of an element in pixels</p> 
                     

## waitForElementIndex

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForElementIndex(locator, pattern) Generated from getElementIndex(locator) Arguments: *locator - an element locator pointing to an element . Returns: of relative index of the element to its parent (starting from 0)</p> 
                     

## waitForElementNotPresent

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForElementNotPresent(locator) Generated from isElementPresent(locator) Arguments: *locator - an element locator . Returns: true if the element is not present, false otherwise</p> 
                     

## waitForElementPositionLeft

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForElementPositionLeft(locator, pattern) Generated from getElementPositionLeft(locator) Arguments: *locator - an element locator pointing to an element OR an element itself . Returns: of pixels from the edge of the frame.</p> 
                     

## waitForElementPositionTop

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForElementPositionTop(locator, pattern) Generated from getElementPositionTop(locator) Arguments: *locator - an element locator pointing to an element OR an element itself . Returns: of pixels from the edge of the frame.</p> 
                     

## waitForElementPresent

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForElementPresent(locator) Generated from isElementPresent(locator) Arguments: *locator - an element locator . Returns: true if the element is present, false otherwise</p> 
                     

## waitForElementWidth

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForElementWidth(locator, pattern) Generated from getElementWidth(locator) Arguments: *locator - an element locator pointing to an element . Returns: width of an element in pixels</p> 
                     

## waitForEval

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForEval(script, pattern) Generated from getEval(script)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*script - the JavaScript snippet to run . Returns: the results of evaluating the snippet</p> 
                     

## waitForExpression

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForExpression(expression, pattern) Generated from getExpression(expression) Arguments: *expression - the value to return . Returns: the value passed in</p> 
                     

## waitForFrameToLoad

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForFrameToLoad(frameAddress, timeout)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*frameAddress - FrameAddress from the server side *timeout - a timeout in milliseconds, after which this command will return with an error</p> 
                     

## waitForHtmlSource

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForHtmlSource(pattern) Generated from getHtmlSource(). Returns: the entire HTML source</p> 
                     

## waitForLocation

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForLocation(pattern) Generated from getLocation(). Returns: the absolute URL of the current page</p> 
                     

## waitForMouseSpeed

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForMouseSpeed(pattern) Generated from getMouseSpeed(). Returns: the number of pixels between "mousemove" events during dragAndDrop commands (default=10)</p> 
                     

## waitForNotAlert

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForNotAlert(pattern) Generated from getAlert(). Returns: The message of the most recent JavaScript alert</p> 
                     

## waitForNotAllButtons

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForNotAllButtons(pattern) Generated from getAllButtons(). Returns: the IDs of all buttons on the page</p> 
                     

## waitForNotAllFields

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForNotAllFields(pattern) Generated from getAllFields(). Returns: the IDs of all field on the page</p> 
                     

## waitForNotAllLinks

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForNotAllLinks(pattern) Generated from getAllLinks(). Returns: the IDs of all links on the page</p> 
                     

## waitForNotAllWindowIds

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForNotAllWindowIds(pattern) Generated from getAllWindowIds(). Returns: Array of identifiers of all windows that the browser knows about.</p> 
                     

## waitForNotAllWindowNames

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForNotAllWindowNames(pattern) Generated from getAllWindowNames(). Returns: Array of names of all windows that the browser knows about.</p> 
                     

## waitForNotAllWindowTitles

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForNotAllWindowTitles(pattern) Generated from getAllWindowTitles(). Returns: Array of titles of all windows that the browser knows about.</p> 
                     

## waitForNotAttribute

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForNotAttribute(attributeLocator, pattern) Generated from getAttribute(attributeLocator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*attributeLocator - an element locator followed by an @ sign and then the name of the attribute, e.g. "foo@bar" . Returns: the value of the specifi</p> 
                    

## waitForNotAttributeFromAllWindows

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForNotAttributeFromAllWindows(attributeName, pattern) Generated from getAttributeFromAllWindows(attributeName)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*attributeName - name of an attribute on the windows . Returns: the set of values of this attribute from all known windows.</p> 
                     

## waitForNotBodyText

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForNotBodyText(pattern) Generated from getBodyText(). Returns: the entire text of the page</p> 
                     

## waitForNotChecked

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForNotChecked(locator) Generated from isChecked(locator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator pointing to a checkbox or radio button . Returns: true if the checkbox is checked, false otherwise</p> 
                     

## waitForNotConfirmation

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForNotConfirmation(pattern) Generated from getConfirmation(). Returns: the message of the most recent JavaScript confirmation dialog</p> 
                     

## waitForNotCookie

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForNotCookie(pattern) Generated from getCookie(). Returns: all cookies of the current page under test</p> 
                     

## waitForNotCookieByName

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForNotCookieByName(name, pattern) Generated from getCookieByName(name)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*name - the name of the cookie . Returns: the value of the cookie</p> 
                     

## waitForNotCssCount

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForNotCssCount(css, pattern) Generated from getCssCount(css)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*css - the css selector to evaluate. do NOT wrap this expression in a 'count()' function; we will do that for you. Returns: the number of nodes that match the specified css se</p> 
                    

## waitForNotCursorPosition

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForNotCursorPosition(locator, pattern) Generated from getCursorPosition(locator) Arguments: *locator - an element locator pointing to an input element or textarea. Returns: the numerical position of the cursor in the field</p> 
                     

## waitForNotEditable

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForNotEditable(locator) Generated from isEditable(locator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator. Returns: true if the input element is editable, false otherwise</p> 
                     

## waitForNotElementHeight

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForNotElementHeight(locator, pattern) Generated from getElementHeight(locator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator pointing to an element . Returns: height of an element in pixels</p> 
                     

## waitForNotElementIndex

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForNotElementIndex(locator, pattern) Generated from getElementIndex(locator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator pointing to an element . Returns: of relative index of the element to its parent (starting from 0)</p> 
                     

## waitForNotElementPositionLeft

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForNotElementPositionLeft(locator, pattern) Generated from getElementPositionLeft(locator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator pointing to an element OR an element itself. Returns: of pixels from the edge of the frame.</p> 
                     

## waitForNotElementPositionTop

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForNotElementPositionTop(locator, pattern) Generated from getElementPositionTop(locator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator pointing to an element OR an element itself. Returns: of pixels from the edge of the frame.</p> 
                     

## waitForNotElementWidth

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForNotElementWidth(locator, pattern) Generated from getElementWidth(locator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator pointing to an element. Returns: width of an element in pixels</p> 
                     

## waitForNotEval

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForNotEval(script, pattern) Generated from getEval(script)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*script - the JavaScript snippet to run. Returns: the results of evaluating the snippet</p> 
                     

## waitForNotExpression

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForNotExpression(expression, pattern) Generated from getExpression(expression)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*expression - the value to return. Returns: the value passed in</p> 
                     

## waitForNotHtmlSource

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForNotHtmlSource(pattern) Generated from getHtmlSource(). Returns: the entire HTML source</p> 
                     

## waitForNotLocation

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForNotLocation(pattern) Generated from getLocation(). Returns: the absolute URL of the current page</p> 
                     

## waitForNotMouseSpeed

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForNotMouseSpeed(pattern) Generated from getMouseSpeed(). Returns: the number of pixels between "mousemove" events during dragAndDrop commands (default=10)</p> 
                     

## waitForNotOrdered

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForNotOrdered(locator1, locator2) Generated from isOrdered(locator1, locator2)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator1 - an element locator pointing to the first element *locator2 - an element locator pointing to the second element. Returns: true if element1 is the</p> 
                    

## waitForNotPrompt

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForNotPrompt(pattern) Generated from getPrompt(). Returns: the message of the most recent JavaScript question prompt</p> 
                     

## waitForNotSelectOptions

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForNotSelectOptions(selectLocator, pattern) Generated from getSelectOptions(selectLocator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*selectLocator - an element locator identifying a drop-down menu . Returns: an array of all option labels in the specified select drop-down</p> 
                     

## waitForNotSelectedId

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForNotSelectedId(selectLocator, pattern) Generated from getSelectedId(selectLocator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*selectLocator - an element locator identifying a drop-down menu. Returns: the selected option ID in the specified select drop-down</p> 
                     

## waitForNotSelectedIds

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForNotSelectedIds(selectLocator, pattern) Generated from getSelectedIds(selectLocator) Arguments: *selectLocator - an element locator identifying a drop-down menu. Returns: an array of all selected option IDs in the specified select drop-down</p> 
                     

## waitForNotSelectedIndex

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForNotSelectedIndex(selectLocator, pattern) Generated from getSelectedIndex(selectLocator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*selectLocator - an element locator identifying a drop-down menu. Returns: the selected option index in the specified select drop-down</p> 
                     

## waitForNotSelectedIndexes

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForNotSelectedIndexes(selectLocator, pattern) Generated from getSelectedIndexes(selectLocator) Arguments: *selectLocator - an element locator identifying a drop-down menu. Returns: an array of all selected option indexes in the specified select drop</p> 
                    

## waitForNotSelectedLabel

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForNotSelectedLabel(selectLocator, pattern) Generated from getSelectedLabel(selectLocator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*selectLocator - an element locator identifying a drop-down menu. Returns: the selected option label in the specified select drop-down</p> 
                     

## waitForNotSelectedLabels

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForNotSelectedLabels(selectLocator, pattern) Generated from getSelectedLabels(selectLocator) Arguments: *selectLocator - an element locator identifying a drop-down menu. Returns: an array of all selected option labels in the specified select drop-d</p> 
                    

## waitForNotSelectedValue

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForNotSelectedValue(selectLocator, pattern) Generated from getSelectedValue(selectLocator) Arguments: *selectLocator - an element locator identifying a drop-down menu. Returns: the selected option value in the specified select drop-down</p> 
                     

## waitForNotSelectedValues

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForNotSelectedValues(selectLocator, pattern) Generated from getSelectedValues(selectLocator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*selectLocator - an element locator identifying a drop-down menu. Returns: an array of all selected option values in the specified select drop-</p> 
                    

## waitForNotSomethingSelected

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForNotSomethingSelected(selectLocator) Generated from isSomethingSelected(selectLocator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*selectLocator - an element locator identifying a drop-down menu. Returns: true if some option has been selected, false otherwise</p> 
                     

## waitForNotSpeed

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForNotSpeed(pattern) Generated from getSpeed(). Returns: the execution speed in milliseconds.</p> 
                     

## waitForNotTable

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForNotTable(tableCellAddress, pattern) Generated from getTable(tableCellAddress)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*tableCellAddress - a cell address, e.g. "foo.1.4" . Returns: the text from the specified cell</p> 
                     

## waitForNotText

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForNotText(locator, pattern) Generated from getText(locator) Arguments: *locator - an element locator. Returns: the text of the element</p> 
                     

## waitForNotTitle

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForNotTitle(pattern) Generated from getTitle(). Returns: the title of the current page</p> 
                     

## waitForNotValue

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForNotValue(locator, pattern) Generated from getValue(locator) Arguments: *locator - an element locator. Returns: the element value, or "on/off" for checkbox/radio elements</p> 
                     

## waitForNotVisible

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForNotVisible(locator) Generated from isVisible(locator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator. Returns: true if the specified element is visible, false otherwise</p> 
                     

## waitForNotWhetherThisFrameMatchFrameExpression

 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForNotWhetherThisFrameMatchFrameExpression(currentFrameString, target, pattern) Generated from getWhetherThisFrameMatchFrameExpression(currentFrameString, target)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*currentFrameString - starting frame *target - new frame (which might be</p> 
                     

## waitForNotWhetherThisWindowMatchWindowExpression

 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForNotWhetherThisWindowMatchWindowExpression(currentWindowString, target, pattern) Generated from getWhetherThisWindowMatchWindowExpression(currentWindowString, target)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*currentWindowString - starting window *target - new window (which</p> 
                     

## waitForNotXpathCount

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForNotXpathCount(xpath, pattern) Generated from getXpathCount(xpath)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*xpath - the xpath expression to evaluate. do NOT wrap this expression in a 'count()' function; we will do that for you. Returns: the number of nodes that match the sp</p> 
                    

## waitForOrdered

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForOrdered(locator1, locator2) Generated from isOrdered(locator1, locator2)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator1 - an element locator pointing to the first element *locator2 - an element locator pointing to the second element . Returns: true if element1 is the p</p> 
                    

## waitForPageToLoad

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForPageToLoad(timeout) <strong className="ph b">Arguments</strong>: *timeout - a timeout in milliseconds, after which this command will return with an error</p> 
                     

## waitForPopUp

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForPopUp(windowID, timeout) <strong className="ph b">Arguments</strong>: *windowID - the JavaScript window "name" of the window that will appear (not the text of the title bar) If unspecified, or specified as "null", this command will wait for the first non-top window to appear (don</p> 
                    

## waitForPrompt

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForPrompt(pattern) Generated from getPrompt(). Returns: the message of the most recent JavaScript question prompt</p> 
                     

## waitForPromptNotPresent

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForPromptNotPresent() Generated from isPromptPresent(). Returns: true if there is a pending prompt</p> 
                     

## waitForPromptPresent

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForPromptPresent() Generated from isPromptPresent(). Returns: true if there is a pending prompt</p> 
                     

## waitForSelectOptions

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForSelectOptions(selectLocator, pattern) Generated from getSelectOptions(selectLocator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*selectLocator - an element locator identifying a drop-down menu . Returns: an array of all option labels in the specified select drop-down</p> 
                     

## waitForSelectedId

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForSelectedId(selectLocator, pattern) Generated from getSelectedId(selectLocator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*selectLocator - an element locator identifying a drop-down menu. Returns: the selected option ID in the specified select drop-down</p> 
                     

## waitForSelectedIds

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForSelectedIds(selectLocator, pattern) Generated from getSelectedIds(selectLocator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*selectLocator - an element locator identifying a drop-down menu. Returns: an array of all selected option IDs in the specified select drop-down</p> 
                     

## waitForSelectedIndex

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForSelectedIndex(selectLocator, pattern) Generated from getSelectedIndex(selectLocator) Arguments: *selectLocator - an element locator identifying a drop-down menu. Returns: the selected option index in the specified select drop-down</p> 
                     

## waitForSelectedIndexes

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForSelectedIndexes(selectLocator, pattern) Generated from getSelectedIndexes(selectLocator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*selectLocator - an element locator identifying a drop-down menu . Returns: an array of all selected option indexes in the specified select drop</p> 
                    

## waitForSelectedLabel

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForSelectedLabel(selectLocator, pattern) Generated from getSelectedLabel(selectLocator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*selectLocator - an element locator identifying a drop-down menu . Returns: the selected option label in the specified select drop-down</p> 
                     

## waitForSelectedLabels

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForSelectedLabels(selectLocator, pattern) Generated from getSelectedLabels(selectLocator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*selectLocator - an element locator identifying a drop-down menu . Returns: an array of all selected option labels in the specified select drop-do</p> 
                    

## waitForSelectedValue

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForSelectedValue(selectLocator, pattern) Generated from getSelectedValue(selectLocator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*selectLocator - an element locator identifying a drop-down menu . Returns: the selected option value in the specified select drop-down</p> 
                     

## waitForSelectedValues

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForSelectedValues(selectLocator, pattern) Generated from getSelectedValues(selectLocator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*selectLocator - an element locator identifying a drop-down menu . Returns: an array of all selected option values in the specified select drop-do</p> 
                    

## waitForSomethingSelected

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForSomethingSelected(selectLocator) Generated from isSomethingSelected(selectLocator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*selectLocator - an element locator identifying a drop-down menu . Returns: true if some option has been selected, false otherwise</p> 
                     

## waitForSpeed

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForSpeed(pattern) Generated from getSpeed(). Returns: the execution speed in milliseconds.</p> 
                     

## waitForTable

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForTable(tableCellAddress, pattern) Generated from getTable(tableCellAddress)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*tableCellAddress - a cell address, e.g. "foo.1.4" . Returns: the text from the specified cell</p> 
                     

## waitForText

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForText(locator, pattern) Generated from getText(locator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator. Returns: the text of the element</p> 
                     

## waitForTextNotPresent

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForTextNotPresent(pattern) This command is deprecated. Use the waitForNotText command with an element locator instead. Generated from isTextPresent(pattern)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*pattern - a pattern to match with the text of the page . Returns: true if the</p> 
                     

## waitForTextPresent

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForTextPresent(pattern) This command is deprecated. Use the waitForText command with an element locator instead. Generated from isTextPresent(pattern)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*pattern - a pattern to match with the text of the page . Returns: true if the patter</p> 
                    

## waitForTitle

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForTitle(pattern) Generated from getTitle(). Returns: the title of the current page</p> 
                     

## waitForValue

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForValue(locator, pattern) Generated from getValue(locator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator. Returns: the element value, or "on/off" for checkbox/radio elements</p> 
                     

## waitForVisible

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForVisible(locator) Generated from isVisible(locator)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*locator - an element locator. Returns: true if the specified element is visible, false otherwise</p> 
                     

## waitForWhetherThisFrameMatchFrameExpression

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForWhetherThisFrameMatchFrameExpression(currentFrameString, target, pattern) Generated from getWhetherThisFrameMatchFrameExpression(currentFrameString, target)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*currentFrameString - starting frame *target - new frame (which might be rel</p> 
                    

## waitForWhetherThisWindowMatchWindowExpression

 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForWhetherThisWindowMatchWindowExpression(currentWindowString, target, pattern) Generated from getWhetherThisWindowMatchWindowExpression(currentWindowString, target)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*currentWindowString - starting window *target - new window (which mig</p> 
                    

## waitForXpathCount

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitForXpathCount(xpath, pattern) Generated from getXpathCount(xpath)</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Arguments</strong>:</p> 
 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">*xpath - the xpath expression to evaluate. do NOT wrap this expression in a 'count()' function; we will do that for you. Returns: the number of nodes that match the speci</p> 
                    

## waitPreparation

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitPreparation</p> 
                    

## waitPreparationAndWait

<p xmlns="http://www.w3.org/1999/xhtml" className="p">waitPreparationAndWait</p> 
                    

## windowFocus

<p xmlns="http://www.w3.org/1999/xhtml" className="p">windowFocus()</p> 
                    

## windowFocusAndWait

<p xmlns="http://www.w3.org/1999/xhtml" className="p">windowFocusAndWait() Generated from windowFocus()</p> 
                    

## windowMaximize

<p xmlns="http://www.w3.org/1999/xhtml" className="p">windowMaximize()</p> 
                    

## windowMaximizeAndWait

<p xmlns="http://www.w3.org/1999/xhtml" className="p">windowMaximizeAndWait() Generated from windowMaximize()</p> 
                    
