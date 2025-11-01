---
hide_title: true
title: Extension Scripts for Custom Locator Builders and Actions in Katalon Recorder
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="id" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Extension Scripts for Custom Locator Builders and Actions in <span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon Recorder</span> 

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Starting from version 3.5.0 Katalon Recorder supports extension scripts (AKA user-extensions.js in the deprecated version of Selenium IDE on Firefox). At this moment this feature allows you to add custom locator builders (1) and your own actions (2) to Katalon Recorder. Please see a sample script at <a className="xref j-external-link" href="https://github.com/katalon-studio/katalon-recorder-samples" target="_blank">https://github.com/katalon-studio/katalon-recorder-samples</a>.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><strong className="ph b">After installing extension scripts, please restart Katalon Recorder and refresh the web page you want to work on.</strong></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-recorder/docs/extension-scripts-aka-user-extensionsjs-for-custom-locator-builders-and-actions/Screenshot-from-2018-04-23-11-21-42.png")} /><br /><br /></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">The following instructions were based on the original documentation (<a className="xref j-external-link" href="https://www.seleniumhq.org/docs/08_user_extensions.jsp" target="_blank">https://www.seleniumhq.org/docs/08_user_extensions.jsp</a>).</p> 
    

## <a id="id_1" class="anchor_top_offset"/>Locator builders
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">A locator in Selenium is a means of identifying an element for   the selenium command. A locator builder creates each of these   locators for you.</p> 
              
```jsx
LocatorBuilders.add('custom locator id goes here', function(e) {
    if (e.id) {
        return "css=" + e.tagName + '#' + e.id;
    }
    return null;
});
```          

## <a id="id_2" class="anchor_top_offset"/>Custom order for locator builders

<p xmlns="http://www.w3.org/1999/xhtml" className="p">The preferred order for locator builders can be customized.</p> 
              
```jsx
// built-in locators: "id", "link", "name", "dom:name", "xpath:link", "xpath:img", "xpath:attributes", "xpath:idRelative", "xpath:href", "dom:index", "xpath:position", "css"
LocatorBuilders._preferredOrder = ['xpath:position', 'my super locator'];
// Change the default order to preferredOrder
LocatorBuilders._orderChanged();
```
## <a id="id_3" class="anchor_top_offset"/>Actions
     
<p xmlns="http://www.w3.org/1999/xhtml" className="p">All methods on the Selenium prototype beginning with "do" are   added as actions. For each action "foo", there is also an action   "fooAndWait" registered. An action method can take up to two   parameters, which will be passed the second and third column values   in the test. Example: Add a "typeRepeated" action to Selenium,   which types the text twice into a text box.</p> 
              
```jsx
Selenium.prototype.doTypeRepeated = function(locator, text) {
    // All locator-strategies are automatically handled by "findElement"
    var element = this.page().findElement(locator);

    // Create the text to type
    var valueToType = text + text;

    // Replace the element text with the new text
    this.page().replaceText(element, valueToType);
};
```

## <a id="id_4" class="anchor_top_offset"/>Accessors/Assertions

    
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">All "getFoo" and "isFoo" methods on the Selenium prototype are   added as accessors ("storeFoo"). For each accessor there is an   "assertFoo", "verifyFoo" and "waitForFoo" registered. An assert   method can take up to two parameters, which will be passed the   second and third column values in the test. You can also define   your own assertions literally as simple "assert" methods, which   will also auto-generate "verify" and "waitFor" commands. Example:   Add a "valueRepeated" assertion, that makes sure that the element   value consists of the supplied text repeated. The two commands that   would be available in tests would be "assertValueRepeated" and   "verifyValueRepeated".</p> 
              
```jsx
Selenium.prototype.assertValueRepeated = function(locator, text) {
    // All locator-strategies are automatically handled by "findElement"
    var element = this.page().findElement(locator);

    // Create the text to verify
    var expectedValue = text + text;

    // Get the actual element value
    var actualValue = element.value;

    // Make sure the actual value matches the expected
    Assert.matches(expectedValue, actualValue);
};
```
### <a id="id_5" class="anchor_top_offset"/>Prototype generates additional commands

<p xmlns="http://www.w3.org/1999/xhtml" className="p">All "getFoo" and "isFoo" methods on the Selenium prototype   automatically result in the availability of "storeFoo",   "assertFoo", "assertNotFoo", "verifyFoo", "verifyNotFoo",   "waitForFoo", and "waitForNotFoo" commands. Example, if you add a   "getTextLength()" method, the following commands will automatically   be available: "storeTextLength", "assertTextLength",   "assertNotTextLength", "verifyTextLength", "verifyNotTextLength",   "waitForTextLength", and "waitForNotTextLength" commands.</p> 
                  
```jsx
Selenium.prototype.getTextLength = function(locator, text) {
    return this.getText(locator).length;
};
```
                
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Also note that the "assertValueRepeated" method described above   could have been implemented using "isValueRepeated", with the added   benefit of also automatically getting "assertNotValueRepeated",   "storeValueRepeated", "waitForValueRepeated" and   "waitForNotValueRepeated".</p> 
      
    
    

## <a id="id_6" class="anchor_top_offset"/>Adding extension scripts into Katalon Recorder

    
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">To add an extension script, click the "Extension Scripts" tab on   the bottom panel, and click the "Add Extension Script" button.   <strong className="ph b">Please remember to refresh the tabs you want to work on     because the new extension script only has effects on tabs     opened after being added.</strong> </p> 
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-recorder/docs/extension-scripts-aka-user-extensionsjs-for-custom-locator-builders-and-actions/Screenshot-from-2018-04-23-11-45-06.png")} /><br /><br /> </p> 
    
  
