---
hide_title: true
title: Branching Statements
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="concept-5160" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Branching Statements

<div xmlns="http://www.w3.org/1999/xhtml" className="p"><div className="note note note_note"><span className="note__title">Note:</span> <ul className="ul"><li className="li"><p className="p">Once a test step is added as any of the control statements, it is not allowed to change into another keyword.</p></li></ul></div></div>

## <a id="task-9176" class="anchor_top_offset"/>In manual view

<ol xmlns="http://www.w3.org/1999/xhtml" className="ol steps"><li className="li step stepexpand"><span className="ph cmd">Open a test case in&nbsp; <span className="ph uicontrol">Manual</span> &nbsp;view. Click on the drop-down icon of the <span className="ph uicontrol">Add</span> button, then choose <span className="ph uicontrol">Branching Statements</span>.</span><div className="itemgroup info"><img className="image" width={500} src={useBaseUrl("/8fdb9950-22b2-11ed-9930-0242fe3e4a3f/branching-statement.png")} alt="Branching statements" /></div></li><li className="li step stepexpand"><span className="ph cmd">To add a keyword under a statement, select that statement, then click <span className="ph uicontrol">Add</span> . A test step is created under that statement. </span><div className="itemgroup info"><img className="image" width={600} src={useBaseUrl("/8fdd6e10-22b2-11ed-9930-0242fe3e4a3f/break-continue-return.png")} alt="branching statement in manual view" /><p className="p">Refer to the following table for the usage of each statement:</p></div><div className="itemgroup info"><table className="table anchor_top_offset" id="task-9176__54a57d81-566f-475e-b03a-62468c2ae71f"><caption /><colgroup><col /><col /></colgroup><thead className="thead"><tr className><th className="entry anchor_top_offset" id="task-9176__54a57d81-566f-475e-b03a-62468c2ae71f__entry__1">Statement</th><th className="entry anchor_top_offset" id="task-9176__54a57d81-566f-475e-b03a-62468c2ae71f__entry__2">Description</th></tr></thead><tbody className="tbody"><tr className><td className="entry" headers="task-9176__54a57d81-566f-475e-b03a-62468c2ae71f__entry__1 task-9176__54a57d81-566f-475e-b03a-62468c2ae71f__entry__2 ">Break</td><td className="entry" headers="task-9176__54a57d81-566f-475e-b03a-62468c2ae71f__entry__1 task-9176__54a57d81-566f-475e-b03a-62468c2ae71f__entry__2 "><span className="ph">Katalon Studio</span> exits the current code block and continues to the next code block/test step.</td></tr><tr className><td className="entry" headers="task-9176__54a57d81-566f-475e-b03a-62468c2ae71f__entry__1 task-9176__54a57d81-566f-475e-b03a-62468c2ae71f__entry__2 ">Continue</td><td className="entry" headers="task-9176__54a57d81-566f-475e-b03a-62468c2ae71f__entry__1 task-9176__54a57d81-566f-475e-b03a-62468c2ae71f__entry__2 "><span className="ph">Katalon Studio</span> skips the remainder of the current loop and continues with the next iteration of the loop.</td></tr><tr className><td className="entry" headers="task-9176__54a57d81-566f-475e-b03a-62468c2ae71f__entry__1 task-9176__54a57d81-566f-475e-b03a-62468c2ae71f__entry__2 ">Return</td><td className="entry" headers="task-9176__54a57d81-566f-475e-b03a-62468c2ae71f__entry__1 task-9176__54a57d81-566f-475e-b03a-62468c2ae71f__entry__2 ">Katalon exits from the current method/step, and the flow control is returned to where the method/step was invoked.</td></tr></tbody></table></div></li></ol> 

## <a id="concept-801" class="anchor_top_offset"/>In script view

            
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> The <span className="ph uicontrol">Script</span> &nbsp;view of test cases allows you to programmatically define and handle <strong className="ph b">Break</strong> , <strong className="ph b">Continue</strong> and <strong className="ph b">Return</strong> , using either Groovy or Java language.&nbsp; </p> 
            
<p xmlns="http://www.w3.org/1999/xhtml" className="p">For example:</p> 
            
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><strong className="ph b">Break</strong> : </li></ul> 
            
<pre xmlns="http://www.w3.org/1999/xhtml" className="pre codeblock"><code>for (int i = 0; i &lt; max; i++) {"{"} // interested only in p's if (searchMe.charAt(i) != 'p') {"{"} break; {"}"} // process p's numPs++; {"}"}{"\n"}{"            "}</code></pre> 
            
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><strong className="ph b">Continue</strong> : </li></ul> 
            
<pre xmlns="http://www.w3.org/1999/xhtml" className="pre codeblock"><code>for (int i = 0; i &lt; max; i++) {"{"} // interested only in p's if (searchMe.charAt(i) != 'p') {"{"} continue; {"}"} // process p's numPs++; {"}"}{"\n"}{"            "}</code></pre> 
            
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><strong className="ph b">Return</strong> : </li></ul> 
            
<pre xmlns="http://www.w3.org/1999/xhtml" className="pre codeblock"><code>for (int i = 0; i &lt; max; i++) {"{"} // interested only in p's if (searchMe.charAt(i) != 'p') {"{"} return true; {"}"} // process p's numPs++; {"}"}{"\n"}{"            "}</code></pre> 
