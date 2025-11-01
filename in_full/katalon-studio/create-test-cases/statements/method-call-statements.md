---
hide_title: true
title: Method Call Statements
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="concept-3836" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Method Call Statements

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Method Call statement allows you to call other methods provided by the built-in libraries of <span className="ph">Katalon Studio</span>.</p> 
<div xmlns="http://www.w3.org/1999/xhtml" className="p"><div className="note note note_note"><span className="note__title">Note:</span> <ul className="ul"><li className="li"><p className="p">Once a test step is added as any of the control statements, it is not allowed to change into another keyword.</p></li></ul></div></div>

## <a id="task-5575" class="anchor_top_offset"/>In manual view

<ol xmlns="http://www.w3.org/1999/xhtml" className="ol steps"><li className="li step stepexpand"><span className="ph cmd">Open a test case in&nbsp;<span className="ph uicontrol">Manual</span>&nbsp;view. Click on the drop-down icon of the&nbsp;<span className="ph uicontrol">Add</span> button, then choose <span className="ph uicontrol">Method Call Statements</span>.</span></li><li className="li step stepexpand"><span className="ph cmd">To add a keyword under a statement, select that statement, then click <span className="ph uicontrol">Add</span> . A test step is created under that statement.</span><div className="itemgroup info"><img className="image" width={300} src={useBaseUrl("/8fda60d0-22b2-11ed-9930-0242fe3e4a3f/method-call.png")} alt="Method call statement" /></div><div className="itemgroup stepresult">A test step representing a method call  is added to the test case.<p className="p"><img className="image" width={600} src={useBaseUrl("/8fd94f60-22b2-11ed-9930-0242fe3e4a3f/830-method-call-statement.png")} alt="add binary statement" /></p></div></li><li className="li step stepexpand"><span className="ph cmd">Double-click on the <span className="ph uicontrol">Input</span> cell to edit the called method.</span><div className="itemgroup info"><img className="image" width={600} src={useBaseUrl("/8fd38300-22b2-11ed-9930-0242fe3e4a3f/method-call-input.png")} alt="Method call input" /></div></li><li className="li step stepexpand"><span className="ph cmd">Save the test case when you're done. </span></li></ol> 

## <a id="concept-4098" class="anchor_top_offset"/>In script view

                        
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> The <span className="ph uicontrol">Script</span> view of a test case allows you to programmatically define and handle method calls using Groovy or Java language. </p> 
            
<p xmlns="http://www.w3.org/1999/xhtml" className="p">For example:</p> 
            
<pre xmlns="http://www.w3.org/1999/xhtml" className="pre codeblock"><code>WebUiBuiltInKeywords.openBrowser('', FailureHandling.STOP_ON_FAILURE) WebUiBuiltInKeywords.navigateToUrl(GlobalVariable.global_Gmail_Url, FailureHandling.STOP_ON_FAILURE) WebUiBuiltInKeywords.setText(ObjectRepository.findTestObject(null), 'varA'.toString(), FailureHandling.STOP_ON_FAILURE) Integer.notifyAll(){"\n"}{"            "}</code></pre> 
        
