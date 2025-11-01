---
hide_title: true
title: Windows Test Objects in Katalon Studio
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="id_windows-test-objects" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Windows Test Objects in <span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon Studio</span> 

## <a id="id_1" class="anchor_top_offset"/>Manage Windows Test Objects

### <a id="id_2" class="anchor_top_offset"/>Create a Windows test object

<ol xmlns="http://www.w3.org/1999/xhtml" className="ol">   <li className="li">     <p className="p">Select <strong className="ph b">File &gt; New &gt; Windows         Object</strong> from the main menu. The <strong className="ph b">New         Windows Object</strong> dialog is displayed.</p>     <p className="p">       <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/windows-test-objects/create-new-object.png")} /><br /><br />     </p>   </li>   <li className="li">     <p className="p">Provide a name for the new test object, then       click <strong className="ph b">OK</strong> button to create a new object       under the <strong className="ph b">Object Repository</strong> of Katalon       Studio.</p>   </li> </ol> 
      
### <a id="id_3" class="anchor_top_offset"/>Locator strategy for detecting an object

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Built upon Windows Application Driver, Katalon Studio supports 6   locator strategies to identify UI elements of a Desktop   application. You can choose different ways to locate a Windows test   object.</p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">     <p className="p">       <strong className="ph b">Accessibility ID</strong>: The AutomationId of an       object</p>     <ul className="ul"><li className="li">E.x.: <code className="ph codeph">AppNameTitle</code>         <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/windows-test-objects/accessibility-id.png")} /><br /><br />       </li></ul>   </li><li className="li">     <p className="p">       <strong className="ph b">Class Name</strong>: The ClassName property of an       object</p>     <ul className="ul"><li className="li">E.x.: TextBlock <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/windows-test-objects/class-name.png")} /><br /><br />       </li></ul>   </li><li className="li">     <p className="p">       <strong className="ph b">ID</strong>: The unique runtime ID of an object</p>     <ul className="ul"><li className="li">E.x.: 42.333896.3.1 <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/windows-test-objects/runtime-id.png")} /><br /><br />       </li></ul>   </li><li className="li">     <p className="p">       <strong className="ph b">Name</strong>: The name of an object</p>     <ul className="ul"><li className="li">E.x.: Calculator <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/windows-test-objects/name.png")} /><br /><br />       </li></ul>   </li><li className="li">     <p className="p">       <strong className="ph b">Tag Name</strong>: The tag name (aka the element type)       of an object</p>     <ul className="ul"><li className="li">E.x.: <code className="ph codeph">Text</code>       </li></ul>   </li><li className="li">     <p className="p">       <strong className="ph b">XPath</strong>     </p>     <ul className="ul"><li className="li">E.x.: <code className="ph codeph">//Button[0]</code>       </li></ul>   </li></ul> 

### <a id="id_4" class="anchor_top_offset"/>Test Objects in Script View

<p xmlns="http://www.w3.org/1999/xhtml" className="p">The Script View of a test script allows you to define Windows   objects programmatically. Below are the code snippets of an object   with different locator strategies.</p> 
        
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <strong className="ph b">ACCESSIBILITY_ID</strong> </p> 
                  
<pre xmlns="http://www.w3.org/1999/xhtml" className="pre codeblock"><code>WindowsTestObject wo = new WindowsTestObject(''){"\n"}wo.setLocatorStrategy(LocatorStrategy.ACCESSIBILITY_ID){"\n"}wo.setLocator("accessibility id value here"){"\n"}</code></pre> 
                
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <strong className="ph b">CLASS_NAME</strong> </p> 
                  
<pre xmlns="http://www.w3.org/1999/xhtml" className="pre codeblock"><code>WindowsTestObject wo = new WindowsTestObject(''){"\n"}wo.setLocatorStrategy(LocatorStrategy.CLASS_NAME){"\n"}wo.setLocator("classname value here"){"\n"}</code></pre> 
                
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <strong className="ph b">ID</strong> </p> 
                  
<pre xmlns="http://www.w3.org/1999/xhtml" className="pre codeblock"><code>WindowsTestObject wo = new WindowsTestObject(''){"\n"}wo.setLocatorStrategy(LocatorStrategy.ID){"\n"}wo.setLocator("id here"){"\n"}</code></pre> 
                
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <strong className="ph b">NAME</strong> </p> 
                  
<pre xmlns="http://www.w3.org/1999/xhtml" className="pre codeblock"><code>WindowsTestObject wo = new WindowsTestObject(''){"\n"}wo.setLocatorStrategy(LocatorStrategy.NAME){"\n"}wo.setLocator("name here"){"\n"}</code></pre> 
                
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <strong className="ph b">TAG_NAME</strong> </p> 
                  
<pre xmlns="http://www.w3.org/1999/xhtml" className="pre codeblock"><code>WindowsTestObject wo = new WindowsTestObject(''){"\n"}wo.setLocatorStrategy(LocatorStrategy.TAG_NAME){"\n"}wo.setLocator("tag name here"){"\n"}</code></pre> 
                
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <strong className="ph b">XPATH</strong> </p> 
                  
<pre xmlns="http://www.w3.org/1999/xhtml" className="pre codeblock"><code>WindowsTestObject wo = new WindowsTestObject(''){"\n"}wo.setLocatorStrategy(LocatorStrategy.XPATH){"\n"}wo.setLocator("XPATH here"){"\n"}</code></pre> 
              
### <a id="id_5" class="anchor_top_offset"/>Verify and Highlight

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Katalon Studio Windows Object Spy and Recorder have a built-in   <strong className="ph b">Highlight</strong> feature that allows double-checking if   the Windows objects are able to be located.</p> 
        
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Katalon Studio displays a message on how many elements are found   or NOT found with the selected locator strategy and locator. If the   object is found, it will be highlighted with the   <strong className="ph b">green</strong> border.</p> 
        
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/windows-test-objects/name-highlight.png")} /><br /><br /> </p> 
      
## <a id="id_6" class="anchor_top_offset"/>Parameterize Windows Test Objects

:::info notes
Parameterizing Windows test objects is available in version 7.3.0+.
:::
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">The benefit of parameterizing test objects in general is to   handle object with dynamic properties (<a className="xref" href="/katalon-studio/test-objects/web-test-objects/manage-web-test-objects">Read     more</a>). With this feature, you can update test objects' locators   dynamically by using either local or global variables.</p> 
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Here are the steps demonstrating how to use this feature:</p> 
      
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol">   <li className="li">Select a Windows object you want to parameterize</li>   <li className="li">     <p className="p">Capture its locator with Katalon Studio Windows Object Spy or       Recorder and create a variable with this syntax       <code className="ph codeph">${'{'}variable_name{'}'}</code> as a place holder for its dynamic       locator. For example, we create the <code className="ph codeph">${'{'}xpath{'}'}</code> variable       for the XPATH locator strategy. You can parameterize test objects       with other locator strategies as well.</p>     <p className="p">       <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/windows-test-objects/step2.png")} /><br /><br />     </p>   </li>   <li className="li">     <p className="p">Use the parameterized test object.</p>   </li> </ol> 
    
### <a id="id_7" class="anchor_top_offset"/>In Manual View

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Open your Test Case in the <strong className="ph b">Manual</strong> View and   double-click on the object that you want to parameterize its   locator.</p> 
        
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/windows-test-objects/img_manual.png")} /><br /><br /> </p> 
        
<p xmlns="http://www.w3.org/1999/xhtml" className="p">In the displayed <strong className="ph b">Test Object Input</strong> dialog,   declare the expected dynamic locator as a variable in the   <strong className="ph b">Variables</strong> panel.</p> 
        
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul">   <li className="li">     <strong className="ph b">Param Type</strong>: the variable type (The default     type is String).</li>   <li className="li">     <strong className="ph b">Param</strong>: the variable name.</li>   <li className="li">     <strong className="ph b">Value Type</strong>: the type of the variable's     value.</li>   <li className="li">     <strong className="ph b">Value</strong>: a specific value of that variable.</li> </ul> 
        
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/windows-test-objects/img_test_object_input.png")} /><br /><br /> </p> 
        
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/windows-test-objects/img_variables.png")} /><br /><br /> </p> 
        
<p xmlns="http://www.w3.org/1999/xhtml" className="p">For instance, Katalon Studio uses the <code className="ph codeph">xpath</code>   variable created in step 2, with its specific value as   <code className="ph codeph">//Button[0]</code> to find the <strong className="ph b">btn_Login</strong>   object.</p> 

### <a id="id_8" class="anchor_top_offset"/>In Script View

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Once the locator is declared, you can switch to the   <strong className="ph b">Script</strong> View and modify the perceived value of the   locator. Typically, users want to pass the locator value as a   variable or refer to data files.</p> 
        
<p xmlns="http://www.w3.org/1999/xhtml" className="p">The general syntax to find a Windows test object using a dynamic   locator is as follows:</p> 
                  
<pre xmlns="http://www.w3.org/1999/xhtml" className="pre codeblock"><code>findWindowsObject('{"{"}your test object{"}"}', [('{"{"}variable{"}"}') : '{"{"}value of variable{"}"}']){"\n"}</code></pre> 
                
<p xmlns="http://www.w3.org/1999/xhtml" className="p">For example:</p> 
                  
<pre xmlns="http://www.w3.org/1999/xhtml" className="pre codeblock"><code>findWindowsObject('Object Repository/btn_Login', [('xpath') : '//Button[0]']){"\n"}</code></pre> 
                
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/windows-test-objects/img_script_view.png")} /><br /><br /> </p> 
      
    
