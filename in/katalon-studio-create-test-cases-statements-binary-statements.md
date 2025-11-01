---
hide_title: true
title: Binary Statements
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="concept-8396" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Binary Statements

<p xmlns="http://www.w3.org/1999/xhtml" className="p">A Binary statement represents a dual expression consisting of two single&nbsp;<strong className="ph b">expressions</strong>&nbsp;(variables, strings, numbers, methods...) and an operator, for example: +, -, *, &lt;, &lt;=,&nbsp;!, etc.). For more details about using operators in Groovy, refer to&nbsp;this Groovy documentation:&nbsp;<a className="xref j-external-link" href="http://groovy-lang.org/operators.html" target="_blank">Operators</a>.</p> 
<div xmlns="http://www.w3.org/1999/xhtml" className="p"><div className="note note note_note"><span className="note__title">Note:</span> <ul className="ul"><li className="li"><p className="p">Once a test step is added as any of the control statements, it is not allowed to change into another keyword.</p></li></ul></div></div>

## <a id="task-9090" class="anchor_top_offset"/>In manual view

<ol xmlns="http://www.w3.org/1999/xhtml" className="ol steps"><li className="li step stepexpand"><span className="ph cmd">Open a test case in&nbsp;<span className="ph uicontrol">Manual</span>&nbsp;view. Click on the drop-down icon of the&nbsp;<span className="ph uicontrol">Add</span> button, then choose&nbsp;<span className="ph uicontrol">Binary Statements</span>.</span></li><li className="li step stepexpand"><span className="ph cmd">To add a keyword under a statement, select that statement, then click <span className="ph uicontrol">Add</span>. A test step is created under that statement.</span><div className="itemgroup info"><img className="image" width={300} src={useBaseUrl("/8fde7f80-22b2-11ed-9930-0242fe3e4a3f/set-binary-statement.png")} alt="binary statement" /></div><div className="itemgroup stepresult">A test step representing a binary statement is added to the test case.<p className="p"><img className="image" width={600} src={useBaseUrl("/8fe36180-22b2-11ed-9930-0242fe3e4a3f/830-binary-statements.png")} alt="add binary statement" /></p></div></li><li className="li step stepexpand"><span className="ph cmd">Double-click on the <span className="ph uicontrol">Input</span> cell to edit those required components. </span><div className="itemgroup info">Binary statements are normally used to assign either values to test objects<p className="p"><img className="image" width={600} src={useBaseUrl("/8fd64220-22b2-11ed-9930-0242fe3e4a3f/Binary-Statement.png")} alt="Binary statement" /></p><p className="p">or test objects to variables to take the next steps.</p><p className="p"><img className="image" width={600} src={useBaseUrl("/8fe5ab70-22b2-11ed-9930-0242fe3e4a3f/BS-2.png")} alt="Binary statement" /></p></div></li><li className="li step stepexpand"><span className="ph cmd">Save the test case when you're done.</span><div className="itemgroup info"><img className="image" width={600} src={useBaseUrl("/8fd77aa0-22b2-11ed-9930-0242fe3e4a3f/830-binary-statement-steps.png")} alt="Binary statements step" /></div></li></ol> 

## <a id="concept-7451" class="anchor_top_offset"/>In script view


### In Script view

                        
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> The <span className="ph uicontrol">Script</span> view of a test case allows you to programmatically define and handle binary statements using Groovy or Java languages. </p> 
            
<p xmlns="http://www.w3.org/1999/xhtml" className="p">For example : </p> 
            
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">     <p className="p">To assign a value to a test object</p>     <pre className="pre codeblock"><code>myText = 'Welcome to Katalon Studio'</code></pre>   </li><li className="li">     <p className="p">To assign a test object to a variable</p>     <pre className="pre codeblock"><code>myObject = findTestObject('my object') WebUI.setText(myObject, 'Welcome to Katalon Studio') WebUI.verifyTextPresent('Welcome to Katalon Studio', false)</code></pre>   </li></ul> 
        
