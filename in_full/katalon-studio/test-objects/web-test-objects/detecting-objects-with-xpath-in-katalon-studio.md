---
hide_title: true
title: Detecting objects with XPath in Katalon Studio
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="id" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Detecting objects with XPath in <span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon Studio</span> 

<p xmlns="http://www.w3.org/1999/xhtml" className="p">With any application under test (AUT), the detection of UI elements is crucial to automated testing. However, identifying them manually requires much time and experience in HTML.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">This task becomes even more challenging for elements that could not be identified by their common attributes, elements that change dynamically, or elements that are located deep within another element (nested elements).</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">This article shows you how to use XPath in Katalon Studio to deal with nested elements and dynamic elements.</p> 
    

## <a id="id_1" class="anchor_top_offset"/>What is XPath?

    
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">XPath stands for XML Path Language. In an XML document, XPath   uses path expressions to navigate through elements, attributes, and   select nodes or node-sets.</p> 
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">On a webpage using the HTML DOM (Document Object Model)   structure, you can also use XPath to find the location of any   element. To learn more about HTML DOM, you can refer to the   W3schools documentation: <a className="xref j-external-link" href="https://www.w3schools.com/whatis/whatis_htmldom.asp" target="_blank">What is     the HTML DOM?</a> </p> 
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">There are two types of XPath: absolute XPath and relative XPath   (smart XPath).</p> 
    
          
      

### <a id="id_2" class="anchor_top_offset"/>Absolute XPath

      
        
<p xmlns="http://www.w3.org/1999/xhtml" className="p">XML documents are treated as trees of nodes, in which the   topmost element of the tree is the root element.</p> 
        
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Absolute XPath is the path starting from the root. An absolute   XPath starts with HTML and forward-slash (/).</p> 
        
<p xmlns="http://www.w3.org/1999/xhtml" className="p">For example:   <code className="ph codeph">/html/body/div[1]/div[1]/div/div[3]/div[2]/div</code> </p> 
        
<p xmlns="http://www.w3.org/1999/xhtml" className="p">In Katalon Studio, the XPath capture strategy for absolute XPath   is <code className="ph codeph">xpath:position</code>. Using absolute XPath is a simple   way to solve the problem when dealing with dynamic elements.   However, if something changes in the structure of your web page,   this XPath might fail. Therefore, absolute XPath is not recommended   for detecting dynamic elements.</p> 
      
    
      

### <a id="id_3" class="anchor_top_offset"/>Relative XPath

      
        
<p xmlns="http://www.w3.org/1999/xhtml" className="p">You might want to use the relative XPath method to observe a   pattern in the attribute values like ID or Class of the web   element. Relative XPath (smart XPath) is the path that starts from   the middle of the HTML DOM structure. Unlike the absolute XPath   that starts from the root, relative XPath starts with the double   forward-slash (//), which means it can search for the element   anywhere on the webpage. Therefore, you can start from the middle   of the HTML DOM structure without writing a long XPath. For   example: <code className="ph codeph">//a[contains(text(), 'Katalon Studio')]</code>.</p> 
        
<p xmlns="http://www.w3.org/1999/xhtml" className="p">You can find a list of XPath capture strategies in Katalon   Studio using relative XPath in this document: <a className="xref" href="/katalon-studio/test-objects/web-test-objects/selection-methods-for-web-objects#id_2">Configure     XPath</a>.</p> 
      
    
    

## <a id="id_4" class="anchor_top_offset"/>How to identify nested elements?

    
          
      

### <a id="id_5" class="anchor_top_offset"/>What is a nested element?

      
        
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Elements can contain other elements. Nested elements are   children of their parent container.</p> 
        
<p xmlns="http://www.w3.org/1999/xhtml" className="p">For example, the download link in the script below is an element   nested in another.</p> 
                  
<pre xmlns="http://www.w3.org/1999/xhtml" className="pre codeblock"><code>&lt;div class="container"&gt;{"\n"}{"    "}&lt;div class="navbar-collapse navbar-right"&gt;{"\n"}{"        "}&lt;div class="nav-bar-decorated"&gt;{"\n"}{"            "}&lt;ul&gt;{"\n"}{"                "}&lt;li&gt;&lt;a class="pbtn-download" href="#katalon-download"&gt;Download&lt;/a&gt; &lt;!-- Deeply nested element{"  "}--&gt;&lt;/li&gt;{"\n"}{"            "}&lt;/ul&gt;{"\n"}{"        "}&lt;/div&gt;{"\n"}{"    "}&lt;/div&gt;{"\n"}&lt;/div&gt;{"\n"}</code></pre> 
                
<p xmlns="http://www.w3.org/1999/xhtml" className="p">It is difficult to identify a nested element, such as the   <code className="ph codeph">&lt;a&gt;</code> element in the script above. To define the   XPath manually, we need to have solid knowledge about the DOM   structure of the webpage.</p> 
      
    

### <a id="id_6" class="anchor_top_offset"/>Identify nested elements using XPath

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Identifying XPath is an effective way to find nested elements that cannot be identified by common properties such as ID, name, or class. Katalon Studio can generate and optimize XPath for HTML elements, regardless of how deeply nested they are. You can use these XPaths to identify elements without searching through the DOM tree.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">The example below illustrates how Katalon Studio generates and optimizes XPath automatically when you spy on the <strong className="ph b">Make Appointment</strong> object (a nested element).</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" width={850} src={useBaseUrl("https://tw-cdn.katalon.com/katalon-studio/ks-855-capture-object-btn.png")} alt="detecting elements with XPath by Katalon Studio" /></p> 
    

## <a id="id_7" class="anchor_top_offset"/>Deal with dynamically changing elements

    
          
      

### <a id="id_8" class="anchor_top_offset"/>What is a dynamic element?

      
        
<p xmlns="http://www.w3.org/1999/xhtml" className="p">One of the challenging and time-consuming tasks in test   automation is to modify test scripts when the AUT is changed,   especially in the early stages of software development. Developers   may change identifiers and elements quite often from one build to   another. In addition, during the execution, the AUT elements may   change dynamically.</p> 
        
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Dynamic web elements are elements whose IDs and any other   attributes like class names or values keep changing when you   refresh the page. Dynamic elements are database-driven or   session-driven. For example, when you edit an element in a   database, it changes a number of areas of the application under   test.</p> 
      
    

### <a id="id_9" class="anchor_top_offset"/>Deal with dynamic elements using XPath

<p xmlns="http://www.w3.org/1999/xhtml" className="p">To deal with dynamic elements, you might not want to use absolute XPaths for these elements in test cases. Instead, you might want to use relative XPaths based on specific patterns.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">XPath axes are used to search for the multiple nodes in the XML document from the current node context. Katalon Studio supports all XPath axes. The table below shows some common methods you can use to detect dynamic elements:</p> 

| **Method** | **Description** | **Example** |
| --- | --- | --- |
| Checking Multiple Attributes | Add more than one condition to search element using XPath. | `//*[@id='btn-login'][@type='submit']` |
| Index | Specify a given tag name in terms of the index value you wish to locate. Use this when more than one element is present in the DOM with similar attributes, and it becomes difficult to search for them. | `//div[@class='form-group']//select[1]` |
| Chained XPath | Use multiple XPath expressions and chain them. | `//section[@id='appointment']//span[@class='glyphiconglyphicon-calendar']` |
| Contains() | Use the Contains() method to detect dynamic elements that contain static values. | `//button[contains(@id, 'btn-login')]` |
| Last() | Last() is a method used in an XPath expression. It is used to get the very last node. | `//ul[@class='list-inline']/li[last()]` |
| Start-with() | The Start-with method finds the element using the starting text of an attribute. This method is useful when the first part of the attribute value is fixed (static), and the rest is dynamic. | `//h3[starts-with(text(),'We Care About')]` |
| Preceding | Select all nodes that come before the current node. | `//*[@id='btn-login']//preceding::input` |
| Following | Select all elements in the document following the current node( ). | `.//*[@id='txt-username']//following::input` |
| Following-sibling | Select the following siblings of the context node. | `.//*[@id='txt-username']//following::input` |
| Ancestor | Select all ancestors (parent, grandparent, etc.) of the current node. | `//ul[@class='list-inline']/ancestor::div` |
| Child | Select all children of the current node. | `//ul[@class='list-inline']/child::li` |
| Descendant | Select all descendant (child node, grandchild node, etc.) of the current node. | `//ul[@class='list-inline']/descendant::li` |

For more information on XPath axes, refer to the W3school documentation: [XPath Axes](https://www.w3schools.com/xml/xpath_axes.asp).

- To learn how to find object locators in Katalon Studio, see [Spy Web Utility](/katalon-studio/record-and-spy/webui-record-and-spy-utilities/spy-web-utility-in-katalon-studio).

**Next step**:

Learn how to input and edit XPath or CSS objects to identify objects on Web UI via Spy Web Utility: [Generating reliable object selector using Spy Web utility](/katalon-studio/test-objects/web-test-objects/detecting-objects-with-xpath-in-katalon-studio#).