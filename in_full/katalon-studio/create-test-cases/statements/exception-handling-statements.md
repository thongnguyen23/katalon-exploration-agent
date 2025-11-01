---
hide_title: true
title: Exception Handling Statements
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="id_10" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Exception Handling Statements

:::info notes
Once a test step is added as any of the control statements, it is not allowed to change into another keyword.
:::

## <a id="task-9820" class="anchor_top_offset"/>In Manual view 

<ol xmlns="http://www.w3.org/1999/xhtml" className="ol steps"><li className="li step stepexpand"><span className="ph cmd">Open a test case in <span className="ph uicontrol">Manual</span> view.</span></li><li className="li step stepexpand"><span className="ph cmd">Click on the drop-down icon of the <span className="ph uicontrol">Add</span> button, then choose <span className="ph uicontrol">Exception Handling Statements</span>.</span><div className="itemgroup stepxmp"><img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/statements/exception-handling-statements.png")} width={500} alt="exception handling statement" /><br /><br /></div></li><li className="li step stepexpand"><span className="ph cmd">To add a keyword under a statement, select that statement, then click <span className="ph uicontrol">Add</span>. A test step is created under that statement.</span><div className="itemgroup stepxmp"><img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/statements/exception-handling.png")} alt="exception handling statements in manual view" /><br /><br /></div><div className="itemgroup info">Refer to the following table for the usage of each statement:<table className="table anchor_top_offset" id="task-9820__33ca7663-c00a-4678-a8fe-09e57348f8ee"><caption /><thead className="thead"><tr className><th className="entry anchor_top_offset" id="task-9820__33ca7663-c00a-4678-a8fe-09e57348f8ee__entry__1">Statement</th><th className="entry anchor_top_offset" id="task-9820__33ca7663-c00a-4678-a8fe-09e57348f8ee__entry__2">Description</th></tr></thead><tbody className="tbody"><tr className><td className="entry" headers="task-9820__33ca7663-c00a-4678-a8fe-09e57348f8ee__entry__1 task-9820__33ca7663-c00a-4678-a8fe-09e57348f8ee__entry__2 ">Try</td><td className="entry" headers="task-9820__33ca7663-c00a-4678-a8fe-09e57348f8ee__entry__1 task-9820__33ca7663-c00a-4678-a8fe-09e57348f8ee__entry__2 ">This statement indicates that all steps within is monitored by exception handlers.</td></tr><tr className><td className="entry" headers="task-9820__33ca7663-c00a-4678-a8fe-09e57348f8ee__entry__1 task-9820__33ca7663-c00a-4678-a8fe-09e57348f8ee__entry__2 ">Throw</td><td className="entry" headers="task-9820__33ca7663-c00a-4678-a8fe-09e57348f8ee__entry__1 task-9820__33ca7663-c00a-4678-a8fe-09e57348f8ee__entry__2 ">Some code must throw an exception before you can <strong className="ph b">Catch</strong> an exception. Regardless of what code throws the exception, it always involves the <strong className="ph b">Throw</strong> statement.</td></tr><tr className><td className="entry" headers="task-9820__33ca7663-c00a-4678-a8fe-09e57348f8ee__entry__1 task-9820__33ca7663-c00a-4678-a8fe-09e57348f8ee__entry__2 ">Catch</td><td className="entry" headers="task-9820__33ca7663-c00a-4678-a8fe-09e57348f8ee__entry__1 task-9820__33ca7663-c00a-4678-a8fe-09e57348f8ee__entry__2 ">When there is any issue occurred during the execution of the <strong className="ph b">Try</strong> block, Katalon Studio executes all steps within.</td></tr><tr className><td className="entry" headers="task-9820__33ca7663-c00a-4678-a8fe-09e57348f8ee__entry__1 task-9820__33ca7663-c00a-4678-a8fe-09e57348f8ee__entry__2 ">Finally</td><td className="entry" headers="task-9820__33ca7663-c00a-4678-a8fe-09e57348f8ee__entry__1 task-9820__33ca7663-c00a-4678-a8fe-09e57348f8ee__entry__2 ">This is the last part of the <strong className="ph b">Try-Catch-Finally</strong></td></tr></tbody></table></div></li></ol> 
      

## <a id="id_12" class="anchor_top_offset"/>In Script view

      
        
<p xmlns="http://www.w3.org/1999/xhtml" className="p">The <strong className="ph b">Script</strong> view of test cases allows you   to programmatically define and handle exceptions using Groovy or   Java language. For more details about exception handling in Groovy,   refer to this Groovy documentation: <a className="xref j-external-link" href="http://groovy-lang.org/semantics.html#_try_catch_finally" target="_blank">Try     - Catch - Finally</a>.</p> 
        
<p xmlns="http://www.w3.org/1999/xhtml" className="p">For example:</p> 
                  
<pre xmlns="http://www.w3.org/1999/xhtml" className="pre codeblock"><code>{"   "}try {"{"}{"\n"}{"        "}WebUI.openBrowser(''){"\n"}{"\n"}{"        "}WebUI.navigateToUrl('katalon.com'){"\n"}{"\n"}{"        "}if (WebUI.getText(findTestObject('Object Repository/txt_singin')).length() &lt; 0) {"{"}{"\n"}{"            "}throw new com.kms.katalon.core.exception.StepFailedException('Value required'){"\n"}{"        "}{"}"}{"\n"}{"    "}{"}"}{"\n"}{"    "}catch (StepErrorException e) {"{"}{"\n"}{"        "}this.println(e){"\n"}{"    "}{"}"} {"\n"}{"    "}catch (Exception e) {"{"}{"\n"}{"        "}this.println("General issue occurs."){"\n"}{"    "}{"}"} {"\n"}{"    "}finally {"{"} {"\n"}{"        "}this.println("Navigate to a page."){"\n"}{"    "}{"}"}{"\n"}</code></pre> 
              
    
