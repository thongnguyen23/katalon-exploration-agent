---
hide_title: true
title: Understand waiting keywords in Katalon Studio
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="id" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Understand waiting keywords in <span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon Studio</span> 

<p xmlns="http://www.w3.org/1999/xhtml" className="p">When a condition is not met, Katalon Studio returns a result (either <em className="ph i">True</em> or <em className="ph i">False</em>) with a warning message regardless of what failure handling settings you specified.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">In other words, Katalon Studio continues running despite a test's failure. This behavior is similar to choosing the <em className="ph i">Optional</em> value for failure handling. See: <a className="xref" href="/katalon-studio/maintain-tests/configure-failure-handling-settings-in-katalon-studio">Failure Handling</a>.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">In case the waiting keyword fails due to such errors as a network problem, session timeout, or because the AUT didn't start, failure handling then applies your specified settings.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">For example, if you use the waiting keyword, <code className="ph codeph">WaitForElementPresent</code>, Katalon Studio only returns a <em className="ph i">True</em> or <em className="ph i">False</em> result in respect of the element's presence. If the element is not present on the current view, Katalon Studio returns a <em className="ph i">False</em> result and shows a warning message (Failure Handling = Optional).</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/understand-waiting-keywords/waiting-keyword.png")} alt="waiting keywords" /><br /><br /> </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">If you want to let the test case fail due to the element not being present, use the following script to make it an assertion:</p> 
<pre xmlns="http://www.w3.org/1999/xhtml" className="pre codeblock"><code>boolean present = Mobile.waitForElementPresent(findTestObject('...'), 10){"\n"}{"\n"}assert present{"\n"}</code></pre> 
