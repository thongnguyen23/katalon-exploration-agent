---
hide_title: true
title: Parameterize Mobile Test Object Properties in Katalon Studio
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="id" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Parameterize Mobile Test Object Properties in <span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon Studio</span> 

:::info notes
Parameterizing Mobile Test Object Properties is only available with the **Attributes** Selection Method.
:::
<p xmlns="http://www.w3.org/1999/xhtml" className="p">The benefits of parameterizing mobile test objects are similar to those of parameterizing web test objects. Refer to <a className="xref" href="/katalon-studio/test-objects/web-test-objects/use-variables-in-web-test-objects">this document</a> for further details.</p> 

## <a id="id_1" class="anchor_top_offset"/>Usage Example

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Below is an example of how to parameterize test objects in   Mobile testing. Open a sample project of Mobile testing on Android   devices by accessing <strong className="ph b">File&gt; New Sample Project&gt; Sample     Android Mobile Tests Project</strong>.</p> 
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Navigate to <strong className="ph b">Object     Repository/Application/android.widget.TextView - App</strong> in   Tests Explorer, open the test object view of   <code className="ph codeph">android.widget.TextView - App</code> whose property will be   parameterized.</p> 
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">In this example, we want to find a test object that has   <code className="ph codeph">//*[(text() = 'demokatalon' or . = 'demokatalon')]</code> as   its selector. Here are the steps to apply this feature:</p> 
    
### <a id="id_2" class="anchor_top_offset"/>Step 1: Parameterize the test object's dynamic property

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Create a property with its value as a variable having this syntax: <code className="ph codeph">${'{'}Variable_name{'}'}</code>. For this example, in the <span className="ph uicontrol">Object's Properties</span> panel, add an object's property with:</p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">Name: <code className="ph codeph">text</code>   </li><li className="li">Value: <code className="ph codeph">${'{'}text{'}'}</code>   </li></ul> 
<div xmlns="http://www.w3.org/1999/xhtml" className="p">Its selected locator is generated as <pre className="pre codeblock"><code>//*[(text() ={"\n"}{"            "}'${"{"}text{"}"}' or . = '${"{"}text{"}"}')]</code></pre> and identified at runtime with passing data.</div>
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/param-mobile-object/selector.png")} /><br /><br /> </p> 

### <a id="id_3" class="anchor_top_offset"/>Step 2: Use the parameterized test object in a test case

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">     <p className="p"> <strong className="ph b">In Manual View</strong>     </p>     <p className="p">In the <code className="ph codeph">Verify Correct Alarm Message</code> test case, double-click the test object that contains the parameterized property, which is <code className="ph codeph">android.widget.TextView - App</code>. The <span className="ph uicontrol">Test Object Input</span> dialog is displayed.</p>     <p className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/param-mobile-object/test-case.png")} /><br /><br />     </p>     <p className="p">In the <span className="ph uicontrol">Variables</span> panel, add a new variable with the following properties:</p>     <ul className="ul"><li className="li">Param Type: the variable type (The default type is String).</li><li className="li">Param: the variable name of the property created in step 1.</li><li className="li">Value Type: the type of the variable's value.</li><li className="li">Value: a specific value of that variable.</li></ul>     <p className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/param-mobile-object/test-object-input.png")} /><br /><br />     </p>   </li><li className="li">     <p className="p"> <strong className="ph b">In Script View</strong>     </p>     <p className="p">You can also switch to the <strong className="ph b">Scripting Mode</strong> of the current Test Case to adjust the property's value at any time. The predefined variable is automatically mapped when you select a mobile object from manual mode, so you don't need to define them again manually.</p>   </li></ul> 
      

### <a id="id_4" class="anchor_top_offset"/>Step 3: Call the findTestObject method within a keyword

<p xmlns="http://www.w3.org/1999/xhtml" className="p">In this example, the <code className="ph codeph">tap</code> keyword is performed on   the object with the text value that we have just specified.</p> 
        
<div xmlns="http://www.w3.org/1999/xhtml" className="p">
  <pre className="pre codeblock"><code>groovy{"\n"}{"            "}Mobile.tap(findTestObject('Application/android.widget.TextView -{"\n"}{"            "}App', [('text') : 'demokatalon']), 10)</code></pre>
</div>
      
## <a id="id_5" class="anchor_top_offset"/>Escaping special characters

To use a special character like `$` or `\` as a regular one in any place that uses parameterized test objects, prepend it with a backslash: `\` (the so-called escape character).

<pre xmlns="http://www.w3.org/1999/xhtml" className="pre codeblock"><code>{"{"}{"\n"}{"    "}"productName": ${"{"}GlobalVariable.productName{"}"},{"\n"}{"    "}"unit": "\\bottle\",{"\n"}{"    "}"quantity": 50,{"\n"}{"    "}"discount": ${"{"} if (productName == "wine") {"{"} return 30 {"}"} else {"{"} return 0{"}"}{"}"}{"\n"}{"    "}"note": "Currency unit of ${"{"}GlobalVariable.productName{"}"} is \$."{"\n"}{"\n"}{"}"}{"\n"}</code></pre> 
            

- Without `\`: note: Currency unit of `${GlobalVariable.productName}` is `$`.
- With `\`: note: Currency unit of wine is `$`.

