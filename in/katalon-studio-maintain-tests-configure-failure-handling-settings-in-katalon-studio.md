---
hide_title: true
title: Configure failure handling settings in Katalon Studio
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="id" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Configure failure handling settings in <span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon Studio</span> 

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Failure handling settings allow users to decide whether Katalon   Studio will continue running or not when errors occur during   execution.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Currently, Katalon Studio supports the following failure   handling options:</p> 
<table xmlns="http://www.w3.org/1999/xhtml" className="table anchor_top_offset" id="id__f4af672f-08b8-4168-a0dc-2d37cb6fd554"><caption /><thead className="thead"><tr className><th className="entry anchor_top_offset" id="id__f4af672f-08b8-4168-a0dc-2d37cb6fd554__entry__1">Option</th><th className="entry anchor_top_offset" id="id__f4af672f-08b8-4168-a0dc-2d37cb6fd554__entry__2">Description</th></tr></thead><tbody className="tbody"><tr className><td className="entry" headers="id__f4af672f-08b8-4168-a0dc-2d37cb6fd554__entry__1 id__f4af672f-08b8-4168-a0dc-2d37cb6fd554__entry__2 ">Stop on Failure</td><td className="entry" headers="id__f4af672f-08b8-4168-a0dc-2d37cb6fd554__entry__1 id__f4af672f-08b8-4168-a0dc-2d37cb6fd554__entry__2 ">         <p className="p">Katalon Studio will stop execution should there be any error           occurs.</p>         <p className="p">The step with errors will have <strong className="ph b">Failed</strong>           status.</p>       </td></tr><tr className><td className="entry" headers="id__f4af672f-08b8-4168-a0dc-2d37cb6fd554__entry__1 id__f4af672f-08b8-4168-a0dc-2d37cb6fd554__entry__2 ">Continue on Failure</td><td className="entry" headers="id__f4af672f-08b8-4168-a0dc-2d37cb6fd554__entry__1 id__f4af672f-08b8-4168-a0dc-2d37cb6fd554__entry__2 ">         <p className="p">Katalon Studio will continue in spite of any error during its           execution.</p>         <p className="p">The step with errors will have <strong className="ph b">Failed</strong>           status.</p>       </td></tr><tr className><td className="entry" headers="id__f4af672f-08b8-4168-a0dc-2d37cb6fd554__entry__1 id__f4af672f-08b8-4168-a0dc-2d37cb6fd554__entry__2 ">Optional</td><td className="entry" headers="id__f4af672f-08b8-4168-a0dc-2d37cb6fd554__entry__1 id__f4af672f-08b8-4168-a0dc-2d37cb6fd554__entry__2 ">         <p className="p">Katalon Studio will continue in spite of any error during its           execution.</p>         <p className="p"> The step with errors will have <strong className="ph b">Warning</strong>           status.</p>       </td></tr></tbody></table> 

## <a id="id_1" class="anchor_top_offset"/>Default failure handling behavior

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Follow these steps to define the default behavior for failure   handling to be applied across your project:</p> 
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol"><li className="li">From Katalon Studio menu, access <strong className="ph b">Project &gt;       Settings &gt; Test Design &gt; Test Case</strong>. <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/failure-handling/image2017-6-30-203A363A43.png")} /><br /><br />   </li><li className="li">     <p className="p">Select the preferred option for the default behavior of       <strong className="ph b">Failure Handling</strong>. Click <strong className="ph b">OK</strong> when       you're done.</p>     <div className="note note note_note"><span className="note__title">Note:</span>        <p className="p">The selected option will be applied to new test steps only. For         the steps already existed in your test cases, their failure         handling option will not be affected by this change. Thus, you may         need to <a className="xref" href="/katalon-studio/maintain-tests/configure-failure-handling-settings-in-katalon-studio#id_2">update           them manually</a>.</p>     </div>   </li></ol> 
    

## <a id="id_2" class="anchor_top_offset"/>Override failure handling behavior

    
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">You can override the default failure handling behavior for each   test step manually in either <strong className="ph b">Manual view</strong> or   <strong className="ph b">Scripting view</strong> of test case. </p> 
    
          
      

### <a id="id_3" class="anchor_top_offset"/>In Manual View

      
        
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol">   <li className="li">     <p className="p">Right click on the step that you want to change the failure       handling behavior to trigger its context menu</p>     <p className="p">       <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/failure-handling/image2017-8-18-153A133A36.png")} /><br /><br />     </p>   </li>   <li className="li">     <p className="p">Select the preferred failure handling option and save your test       case.</p>   </li> </ol> 
      
    

### <a id="id_4" class="anchor_top_offset"/>In Scripting View

<p xmlns="http://www.w3.org/1999/xhtml" className="p">For all built-in keywords in Katalon Studio, you can add   <em className="ph i">FailureHandling</em> as the last parameter.When editing a   keyword in Scripting mode, use any of these option to specify its   behavior.</p> 
<pre xmlns="http://www.w3.org/1999/xhtml" className="pre codeblock"><code>FailureHandling.STOP_ON_FAILURE{"\n"}FailureHandling.CONTINUE_ON_FAILURE{"\n"}FailureHandling.OPTIONAL{"\n"}</code></pre> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">For example:</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/failure-handling/23.png")} /><br /><br /> </p> 
<div xmlns="http://www.w3.org/1999/xhtml" className="p">Tips and tricks: <ul className="ul"><li className="li"><p className="p"> Why waiting keywords didn't fail? See: <a className="xref" href="/katalon-studio/keywords/using-keywords-in-katalon-studio/web-testing/understand-waiting-keywords-in-katalon-studio">Understand
          waiting keywords</a>.</p></li></ul></div>
