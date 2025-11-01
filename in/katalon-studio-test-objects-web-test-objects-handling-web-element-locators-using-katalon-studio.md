---
hide_title: true
title: Handling Web element locators using Katalon Studio
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="id" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Handling Web element locators using <span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon Studio</span> 

<ol xmlns="http://www.w3.org/1999/xhtml" className="ol"><li className="li">     <a className="xref" href="#id_1">Understanding Your Application Under       Test (AUT)</a>   </li><li className="li">     <a className="xref" href="#id_2">Understanding Application       Lifecycles</a>   </li><li className="li">     <a className="xref" href="#id_3">Using Static Locators</a>   </li><li className="li">     <a className="xref" href="#id_4">Using Uniquely Present Text</a>   </li><li className="li">     <a className="xref" href="#id_13">Summary</a>   </li></ol> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">In Web test automation, locator is the only way to identify an   element on a Web page when running test scripts. When it comes to   automated testing of Web applications, choosing a suitable strategy   is essential. Web element locators depend entirely on the   implementation process, so there is no one-size-fits-all approach   for every Web applications. The selection strategy can be   influenced by these factors: Web application frameworks,   development conventions, software life cycles, and the experience   of automation leaders.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Picking a suitable strategy is crucial not only to Selenium but   also to Katalon Studio. Katalon Studio provides features to   generate necessary locators (XPath, CSS, etc.); so that users only   need to choose the correct one to use. In other words, Katalon   Studio has done 80% of the task, and the remaining 20% will be   decided by users. Starting a project with a good strategy will make   test projects stable and scalable, as well as reduce effort at the   maintenance phase. This tutorial will help you fulfill this   expectation.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   There are many different types of Web element with the most common   including Label, Textbox, Button, Select, Hyperlink, Checkbox and   Radio button. Custom elements built from other basic elements are   Frame, Dialog, Dropdown, Calendar, and Form.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">To identify these elements, we can follow one of these   strategies.</p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">Simple     locators: id, name, class, tag, link     text, attribute</li><li className="li">Advanced locators by combining the simple locators above:      <ul className="ul"><li className="li">XPath</li><li className="li">CSS</li></ul>   </li><li className="li">Using functions in XPath:      <ul className="ul"><li className="li">contains</li><li className="li">sibling</li><li className="li">ancestor</li></ul>   </li></ul> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">This tutorial will help your team choose a good approach for Web   element locators.</p> 

## <a id="id_1" class="anchor_top_offset"/>Understanding Your Application Under Test (AUT)

<p xmlns="http://www.w3.org/1999/xhtml" className="p">This step contributes up to 80% of your success in choosing an   excellent approach to UI functional automation testing. Before   performing any automation testing, your team has to answer these   questions:</p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">Which web technologies are in use?</li><li className="li">Which conventions are applied by the development team?</li></ul> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">The answers to these questions will help you decide which   locator value is static or dynamic. Take ID, for example. ID is   generally suggested as the best locator in Web UI testing because   it is simple and unique on a web page. However, there is a problem   if it is generated dynamically at runtime. Different Web   technologies have different default settings when rendering   elements on a web page. For example, ExtJs or Angular frameworks   regularly create dynamic element IDs by default. Therefore, if your   AUT is developed using these technologies, you can expect that IDs   are dynamic and that they should not be used as the main selectors.   In this case, you should use Class, Name, or Text properties   instead.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">The development team's conventions should also be taken into   account. If the team has the conventions of using all elements with   static IDs, static names, for example, then these static properties   can be used as primary locators. Furthermore, it is unnecessary to   locate an element by its static locator if it has parents,   children, or siblings that can be located by static locators. You   instead locate the element using XPath functions. For example:</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/web_element_locators/Username.png")} alt="Username" /><br /><br /> </p> 
<pre xmlns="http://www.w3.org/1999/xhtml" className="pre codeblock"><code>&lt;div class="field-group"&gt;{"\n"}&lt;label accesskey="u" for="tl0156"&gt;Username&lt;/label&gt;{"\n"}&lt;input class="text medium-field" id="tl0156" type="text"&gt;{"\n"}&lt;/div&gt;{"\n"}</code></pre> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">Locate the <code className="ph codeph">        //label[.='Username']//ancestor::div[1]</code></li><li className="li">Locate the       <code className="ph codeph">//label[.='Username']/following-sibling::input</code>   </li></ul> 

## <a id="id_2" class="anchor_top_offset"/>Understanding Application Lifecycles

<p xmlns="http://www.w3.org/1999/xhtml" className="p">If the AUT life cycle is too short and the content is static,   the absolute XPath, which can be copied from the browser, is   sufficient. There is no need to find a better approach for this   type of project.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">However, if the AUT is large and its life cycle is long,   including the maintenance phase, you have to think about the   locator strategy seriously. A wrong approach may lead to wasting   tremendous time and effort to update and maintain test cases.</p> 

## <a id="id_3" class="anchor_top_offset"/>Using Static Locators

<p xmlns="http://www.w3.org/1999/xhtml" className="p">After studying the AUT and development conventions, if you are   certain that all locators for an element are static, then use them.   This is the simplest possible. See example below:</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/web_element_locators/Username.png")} alt="Username" /><br /><br /> </p> 
<pre xmlns="http://www.w3.org/1999/xhtml" className="pre codeblock"><code>&lt;div class="field-group"&gt;{"\n"}&lt;label accesskey="u" for="login-form-username"&gt;&lt;u&gt;U&lt;/u&gt;sername&lt;/label&gt;{"\n"}&lt;input class="text medium-field" id="login-form-username" name="os_username" type="text" value=""&gt;{"\n"}&lt;/div&gt;{"\n"}</code></pre> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">You can use one of the following XPath to locate the Username   textbox:</p> 

- Id: `//*[@id='login-form-username']`
- Name: `//*[@name='os_username']`
- Class: `//*[@class='text medium-field']`
- Tag: `//input[@class='text medium-field']`
- Attribute: `//input[@class='text medium-field'][@type='text']`

## <a id="id_4" class="anchor_top_offset"/>Using Uniquely Present Text

<p xmlns="http://www.w3.org/1999/xhtml" className="p">If an element does not have any static locator, you will have to   consider using combined locators. Below are a few suggestions:</p> 
    
### <a id="id_5" class="anchor_top_offset"/>Label

<p xmlns="http://www.w3.org/1999/xhtml" className="p">A label is usually used to describe a message (error message,   info message, hint message, etc.), a control (textbox, radio   button, text area, etc.), or a tooltip. As shown in the user   interface, a label is usually unique—otherwise it would be   confusing for users to differentiate UI elements. Therefore, the   label's text is considered a good candidate of the label's locator.   To make the locator more readable,    can be used to narrow the   scope of the locator.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">To locate a label, you should focus on: tag and text. For   example:</p> 

## <a id="id_6" class="anchor_top_offset"/>Welcome to Jira

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Xpath: //h2[text()='Welcome to Jira'] //div[.='Welcome to Jira'] | Priority Xpath: //label[text()='Priority'] //label[.='Priority'] | | --- | --- | </p> 

### <a id="id_7" class="anchor_top_offset"/>Textbox

`<input, type="text">`

A textbox is normally used to receive an input from users. If there is no single static locator, you need to look for references to unique elements to locate the textbox. Oftentimes when look at a webpage, what helps us recognize the functionality of a textbox is the text next to it. This is a good tactic of how to locate the textbox.

Here are several examples of textbox:

<ul>
  <li>
    A textbox has a label outside and next to it. Depending on the location of the label, you can select the most suitable XPath.
    <br />
    <img src="https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/web_element_locators/Username.png" alt="textbox input" />
    <pre><code>
&lt;div class="field-group"&gt;
  &lt;label accesskey="u" for="tl0156"&gt;Username&lt;/label&gt;
  &lt;input class="text medium-field" id="tl0156" type="text"&gt;
&lt;/div&gt;
</code></pre>
  </li>

  <li>
    There are some XPath expressions that can be used to locate the textbox:
    <ul>
      <li><code>//label[.='Username']/following-sibling::input</code></li>
      <li><code>//label[.='Username']//ancestor::div[1]//input</code></li>
      <li><code>//input[@id=//label[.='Username']/@for]</code></li>
    </ul>
  </li>

  <li>
    Sometimes you may see some textboxes that already have text (or a placeholder) inside them:
    <br />
    <img src="https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/web_element_locators/textboxes.png" alt="search box" />
    <pre><code>
&lt;input data-selenium="textInput" tabindex="-1" type="text" class="SearchBoxTextEditor SearchBoxTextEditor--autocomplete" placeholder="Enter a destination or property" value=""&gt;
</code></pre>
  </li>
</ul>

Use the 'placeholder' attribute in an XPath to locate the textbox as:

`//input[@placeholder='Enter a destination or property']`

Pay attention to the 'placeholder' attribute. It may be dynamic as well. The Search bar of Airbnb's website is an example:Search-bar-of-Airbnb's

<img src="https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/web_element_locators/Search-bar-of-Airbnbs.png" alt="placeholder search bar" /> <br/>

In this case, use Tag or texts next to the textbox.

### <a id="id_8" class="anchor_top_offset"/>Button

<p xmlns="http://www.w3.org/1999/xhtml" className="p">A button is normally used to receive an action from users   such as hover, click, and double click. Similar to a textbox, a   button is often recognized by its text. Here are some typical   examples of buttons in a web page:</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/web_element_locators/examples-of-buttons-in-a-web-page-300x60.png")} alt="examples-of-buttons-in-a-web-page" /><br /><br /> </p> 
<pre xmlns="http://www.w3.org/1999/xhtml" className="pre codeblock"><code>&lt;input accesskey="s" class="aui-button aui-button-primary" type="submit" value="Create"&gt;{"\n"}</code></pre> 
<div xmlns="http://www.w3.org/1999/xhtml" className="p">The text in this button is from the 'value' attribute. So
  the XPath should be:<pre className="pre codeblock"><code> //input[@value='Create']</code></pre></div>
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Sometimes, the text in the button is not from the 'value'   attribute. It is actually a text or label with the format that   makes it look like a button.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/web_element_locators/the-text-in-the-button-300x92.png")} alt="the-text-in-the-button" /><br /><br /> </p> 
<pre xmlns="http://www.w3.org/1999/xhtml" className="pre codeblock"><code>&lt;button type="submit" class="_1ptkf58d" aria-busy="false" data-veloute="book-it-footer-trigger"&gt;{"\n"}&lt;span class="_cgr7tc7"&gt;{"\n"}&lt;small class="_1pqj8ky3"&gt;{"\n"}&lt;div class="_1283fq"&gt;{"\n"}&lt;span&gt;Book{"\n"}&lt;/div&gt;{"\n"}&lt;/small&gt;{"\n"}&lt;/button&gt;{"\n"}</code></pre> 
<div xmlns="http://www.w3.org/1999/xhtml" className="p">The following XPaths will help to locate the button.
  You can use one of them.<pre className="pre codeblock"><code>//span[text()='Book']//ancestor::button[1] *{"\n"}{"            "}//button[.//span[text()='Book']] * //button[.='Book']</code></pre></div>

### <a id="id_9" class="anchor_top_offset"/>Select

<p xmlns="http://www.w3.org/1999/xhtml" className="p">A Select (or Drop-down list) allows you select an item from   a list of defined items. Normally, the locator of a select is   similar to that of a textbox—the difference is on the tag: it   uses 'select' tag instead of 'input'.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/web_element_locators/Drop-down-list.png")} alt="Drop-down-list" /><br /><br /> </p> 
<pre xmlns="http://www.w3.org/1999/xhtml" className="pre codeblock"><code>&lt;label for="tl0023"&gt;Priority&lt;/label&gt;{"\n"}&lt;select class="select aui-ss-select" id="tl0023" multiple="multiple"&gt;{"\n"}&lt;option class="imagebacked" value="10000"&gt;Blocker&lt;/option&gt;{"\n"}&lt;option class="imagebacked" value="1"&gt;Highest&lt;/option&gt;{"\n"}&lt;option class="imagebacked" value="2"&gt;High&lt;/option&gt;{"\n"}&lt;option class="imagebacked" value="3"&gt;Medium&lt;/option&gt;{"\n"}&lt;option class="imagebacked" value="4"&gt;Low&lt;/option&gt;{"\n"}&lt;/select&gt;{"\n"}{"\n"}</code></pre> 
<div xmlns="http://www.w3.org/1999/xhtml" className="p">The following XPaths can be used to locate the select
  element above:<ul className="ul"><li className="li"><p className="p"><code className="ph codeph">//Select[@id=//label[.="Priority"]/@for]</code> </p></li><li className="li"><p className="p"><code className="ph codeph">//Select[.//option[.="Highest"]]</code></p></li><li className="li"><p className="p"><code className="ph codeph">//option[.="Highest"]//ancestor::Select[1]</code></p></li></ul></div>

### <a id="id_10" class="anchor_top_offset"/>Hyperlink

<p xmlns="http://www.w3.org/1999/xhtml" className="p">A hyperlink is a link on a webpage that usually receives   the 'click' action. A hyperlink is displayed as a text with or   without an underline, in a different color. Hence, the a   hyperlink's locator is very similar to that of a text or   label—except that the 'a' tag is used. If a hyperlink does   not include text or its URL is more stable than its text, you   should use the 'href' attribute.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/web_element_locators/hyperlinks-locator.png")} alt="hyperlink's-locator" /><br /><br /> </p> 
<pre xmlns="http://www.w3.org/1999/xhtml" className="pre codeblock"><code>&lt;a accesskey="`" class="aui-button aui-button-link cancel" href="/secure/ForgotLoginDetails.jspa" title="Press Ctrl+Alt+` to cancel"&gt;Can't access your account?&lt;/a&gt;{"\n"}{"\n"}</code></pre> 
<div xmlns="http://www.w3.org/1999/xhtml" className="p">A hyperlink is normally located by 'href' or the text
  presenting it:<ul className="ul"><li className="li"><p className="p"> <code className="ph codeph">//a[@href="/secure/ForgotLoginDetails.jspa"]</code></p></li><li className="li"><p className="p"><code className="ph codeph">//a[.="Can't access your account?"]</code></p></li></ul></div>

### <a id="id_11" class="anchor_top_offset"/>Checkbox

<p xmlns="http://www.w3.org/1999/xhtml" className="p">With the tag 'input', a checkbox is used to receive the   "click" action. Normally, a checkbox locator is similar to that of   a textbox.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/web_element_locators/checkbox-locator.png")} alt="checkbox-locator" /><br /><br /> </p> 
<pre xmlns="http://www.w3.org/1999/xhtml" className="pre codeblock"><code>&lt;div class="input-list-item input-list-item-checkbox"&gt;{"\n"}&lt;input type="checkbox" class="sm-input sm-input--stretch" id="tl0056" name="remember_me"&gt;{"\n"}&lt;label class="sm-label" for="tl0056"&gt;Remember me&lt;/label&gt;{"\n"}&lt;/div&gt;{"\n"}</code></pre> 
<div xmlns="http://www.w3.org/1999/xhtml" className="p">A checkbox is often associated with a label. So we
  can use the label to locate the checkbox:<ul className="ul"><li className="li"><p className="p"><code className="ph codeph">//label[.='Remember
          me']//preceding-sibling::input[1]</code></p></li><li className="li"><p className="p"><code className="ph codeph">//label[.='Remember
          me']//ancestor::div[1]//input</code></p></li><li className="li"><p className="p"><code className="ph codeph">//input[@id=//label[.="Remember
          me"]/@for]</code></p></li><li className="li"><p className="p"><code className="ph codeph">//input[.//following-sibling::label[.='Remember
          me']]</code></p></li></ul></div>

### <a id="id_12" class="anchor_top_offset"/>Radio button

<p xmlns="http://www.w3.org/1999/xhtml" className="p">A radio button, like a checkbox, is designed to receive a   "click" action. Its locator is completely the same as the checkbox   locator.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/web_element_locators/radio-button.png")} alt="radio-button" /><br /><br /> </p> 
<pre xmlns="http://www.w3.org/1999/xhtml" className="pre codeblock"><code>&lt;form name="agreementFormjdk-8u181-oth-JPR" method="post" action="radio" class="lic_form"&gt;{"\n"}&lt;input type="radio" value="on" id="agreementjdk-8u181-oth-JPR-a" onclick=""&gt;{"\n"}&lt;label for="agreementjdk-8u181-oth-JPR-a"&gt;Accept License Agreement&lt;/label&gt;{"\n"}&lt;input type="radio" value="on" id="agreementjdk-8u181-oth-JPR-d" onclick=""&gt;{"\n"}&lt;label for="agreementjdk-8u181-oth-JPR-d"&gt;Decline License Agreement&lt;/label&gt;{"\n"}&lt;/form&gt;{"\n"}</code></pre> 
<div xmlns="http://www.w3.org/1999/xhtml" className="p">A radio is often presented with a label on the UI. We
  use labels to locate a radio button as follows:<ul className="ul"><li className="li"><p className="p"><code className="ph codeph">//label[.='Accept License
          Agreement']//preceding-sibling::input[1]</code></p></li><li className="li"><p className="p"><code className="ph codeph">//label[.='Accept
          License Agreement']//ancestor::div[1]//input</code></p></li><li className="li"><p className="p"> <code className="ph codeph">//input[@id=//label[.="Decline License Agreement"]/@for]</code></p></li><li className="li"><p className="p"><code className="ph codeph">//input[.//following-sibling::label[.='Decline License
          Agreement']]</code></p></li></ul></div>

## <a id="id_13" class="anchor_top_offset"/>Summary

<p xmlns="http://www.w3.org/1999/xhtml" className="p">This article presents some strategies for locating Web   elements on a webpage in different situations. These strategies   reflect the user's mindset when perform UI Automation tests: First,   think about simple static locators. Then when simple methods are no   longer working, gradually increase the complexity of the   solution.</p> 
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">It is important to mention that the following principle   must be held in deciding locators: the locator must be unique,   readable and maintainable. If the locator does not uniquely   represent the target element, technical problems will arise during   the maintenance phase as there is no way to know which locator   should be changed.</p> 
    
  
