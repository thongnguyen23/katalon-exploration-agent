---
hide_title: true
title: How to check element status in conditional statement in Katalon Studio
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="id" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>How to check element status in conditional statement in <span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon Studio</span> 

<p xmlns="http://www.w3.org/1999/xhtml" className="p">In Web UI functional testing, you may want to ensure that an   element is clickable, present, or visible before performing further   actions on the element. The function used in such a case is   <strong className="ph b">verifyElementClickable</strong> with this   specification:</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/how_to_check_element_status_in_conditional_statement/verifyElementClickable_1.png")} alt="verifyElementClickable" /><br /><br /> </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">The following code block demonstrates how to check the element   status in a conditional statement. You may assume that the function   WebUI.verifyElementClickable will return <strong className="ph b">true</strong> if   the element is clickable, and <strong className="ph b">false</strong> if the element   is not.</p> 

```jsx
if (WebUI.verifyElementClickable(findTestObject('Test Objects/Pages/Login Page/elContinue - Wrong'))) {
    WebUI.click(findTestObject('Test Objects/Pages/Login Page/elContinue - Wrong'))
} else {
    WebUI.click(findTestObject('Test Objects/Pages/Login Page/elContinue'))
}
```
<p xmlns="http://www.w3.org/1999/xhtml" className="p">However, in practice, if the element is not found after timeout,   the function does not return false. Instead, the exception below is   returned:</p> 
<pre xmlns="http://www.w3.org/1999/xhtml" className="pre codeblock"><code>Stack trace: com.kms.katalon.core.exception.StepFailedException: {"\n"}Unable to verify object 'Object Repository/Test Objects/Pages/Login Page/elContinue - Wrong' to be clickable (Root cause: Web element with id: 'Object Repository/Test Objects/Pages/Login Page/elContinue - Wrong' located by 'By.xpath: //button[.='Continue - Wrong']' not found){"\n"}</code></pre> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">You may find it confusing since the function has been used with   the proper syntax and purpose as specified in the API   documentation. Here’s why: In Katalon Studio, there are two   overloading functions named   <strong className="ph b">verifyElementClickable</strong>.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Function 1 with default FailureHandling: <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/how_to_check_element_status_in_conditional_statement/verifyElementClickable_1.png")} alt="Function 1 with default FailureHandling" /><br /><br /> </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Function 2 wich custom FailureHandling: <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/how_to_check_element_status_in_conditional_statement/verifyElementClickable_2.png")} alt="Function 2 wich custom FailureHandling" /><br /><br /> </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">The first function has a default   <strong className="ph b">FailureHandling</strong> parameter; while the second allows   you to customize the parameter. This will determine the   function’s behavior in some specific situations.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">If you expect the function to return <strong className="ph b">false</strong> if   the element is not found, you will have to use the second function   with the <strong className="ph b">FailureHandling.OPTIONAL</strong> parameter. The   following script will work with your expectation:</p> 

```jsx
if (WebUI.verifyElementClickable(findTestObject('Test Objects/Pages/Login Page/elContinue - Wrong'), FailureHandling.OPTIONAL)) {
    WebUI.click(findTestObject('Test Objects/Pages/Login Page/elContinue - Wrong'))
} else {
    WebUI.click(findTestObject('Test Objects/Pages/Login Page/elContinue'))
}
```
<p xmlns="http://www.w3.org/1999/xhtml" className="p">We hope this tip will help resolve your problem when checking an   element status before performing actions on it.</p> 
