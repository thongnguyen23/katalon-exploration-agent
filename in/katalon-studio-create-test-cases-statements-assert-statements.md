---
hide_title: true
title: Assert Statements
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="concept-3702" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Assert Statements 

<p xmlns="http://www.w3.org/1999/xhtml" className="p">An assert statement contains a boolean expression where this&nbsp;condition must hold true for the test execution to continue. Thus, execution of the assertion causes evaluation of the boolean expression, and an error is reported if the expression evaluates as false.</p> 
<div xmlns="http://www.w3.org/1999/xhtml" className="p"><div className="note note note_note"><span className="note__title">Note:</span> <ul className="ul"><li className="li"><p className="p">Once a test step is added as any of the control statements, it is not allowed to change into another keyword.</p></li></ul></div></div>

## <a id="task-0" class="anchor_top_offset"/>In manual view

<ol xmlns="http://www.w3.org/1999/xhtml" className="ol steps"><li className="li step stepexpand"><span className="ph cmd">Open a test case in&nbsp;<span className="ph uicontrol">Manual</span>&nbsp;view. Click on the drop-down icon of the&nbsp;<span className="ph uicontrol">Add</span>&nbsp;button, then choose <span className="ph uicontrol">Assert Statements</span>.</span></li><li className="li step stepexpand"><span className="ph cmd">To add a keyword under a statement, select that statement, then click <span className="ph uicontrol">Add</span> . A test step is created under that statement.</span><div className="itemgroup info"><img className="image" width={300} src={useBaseUrl("/8fd86500-22b2-11ed-9930-0242fe3e4a3f/assert-statement.png")} alt="Assert statement" /></div><div className="itemgroup stepresult">A test step represents assert expression is added to the test case.<p className="p"><img className="image" width={600} src={useBaseUrl("/cf19ff10-5a59-11ed-a602-0242cfbc79b5/ks-assert-statement.png")} /></p></div></li><li className="li step stepexpand"><span className="ph cmd">Double-click on the <span className="ph uicontrol">Input</span> cell to edit the called method.</span><div className="itemgroup info"><img className="image" width={600} src={useBaseUrl("/8fd4e290-22b2-11ed-9930-0242fe3e4a3f/condition-input.png")} alt="Assert input" /></div></li></ol> 

## <a id="concept-8982" class="anchor_top_offset"/>In script view

<p xmlns="http://www.w3.org/1999/xhtml" className="p"> The <span className="ph uicontrol">Script</span> view of test cases allows you to programmatically define and handle assertions using either Groovy or Java language. For more details regarding assertions in Groovy, refer to this Groovy documentation: <a className="xref j-external-link" href="http://docs.groovy-lang.org/docs/latest/html/documentation/core-testing-guide.html" target="_blank">Core Testing Guide.html</a>. </p> 
<div xmlns="http://www.w3.org/1999/xhtml" className="p">For example:<pre className="pre codeblock"><code>WebUiBuiltInKeywords.openBrowser('', FailureHandling.STOP_ON_FAILURE){"\n"}WebUiBuiltInKeywords.navigateToUrl(GlobalVariable.global_Gmail_Url, FailureHandling.STOP_ON_FAILURE){"\n"}assert varA == true{"    "}{"\n"}{"            "}</code></pre></div>
