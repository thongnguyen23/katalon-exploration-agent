---
hide_title: true
title: Mark test's status for a Custom Keyword in Katalon Studio
---

# <a id="id" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Mark test's status for a Custom Keyword in <span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon Studio</span> 

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Unlike built-in keywords, there will be no overall status for a Custom Keyword unless you define what your expected result is within the Custom Keyword. To generate a status for this one, Katalon Studio provides a couple of functions:</p> 

```jsx
import org.openqa.selenium.By
import org.openqa.selenium.WebElement
import com.kms.katalon.core.annotation.Keyword
import com.kms.katalon.core.testobject.TestObject
import com.kms.katalon.core.util.KeywordUtil
import com.kms.katalon.core.webui.keyword.WebUiBuiltInKeywords
 
/**
* Check if element present in timeout
* @param to Katalon test object
* @param timeout time to wait for element to show up 
* @return true if element present, otherwise false
*/
@Keyword
def isElementPresent(TestObject to, int timeout){
    //Use Katalon built-in function to find elements with time out 1 seconds
    List<WebElement> elements = WebUiBuiltInKeywords.findWebElements(to, timeout)
    if (elements.size() > 0) {
        //Mark Passed status after this step
        KeywordUtil.markPassed("Element is present")
    }
    else {
        //Mark Failed status after this step
        KeywordUtil.markFailed("Element is not present")
    }
}
```

<p xmlns="http://www.w3.org/1999/xhtml" className="p"><strong className="ph b">References:</strong></p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><a className="xref j-external-link" href="https://api-docs.katalon.com/com/kms/katalon/core/util/KeywordUtil.html" target="_blank">KeywordUtil</a></li></ul> 
