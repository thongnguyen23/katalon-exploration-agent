---
hide_title: true
title: Test Case Preferences in Katalon Studio
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="id" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Test Case Preferences in <span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon Studio</span> 

<p xmlns="http://www.w3.org/1999/xhtml" className="p">With Test Case preferences, you can define the default behaviors   related to your test case design. This includes:</p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">Test Case Calling</li><li className="li">Default Open View</li><li className="li">Default Keyword Type</li><li className="li">Line-wrapping settings</li></ul> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">To configure your Test Case preferences, go to <span className="ph">Katalon Studio</span>   &gt; <span className="ph uicontrol">Preferences</span> &gt; <span className="ph uicontrol">Katalon</span> &gt; <span className="ph uicontrol">Test Case</span>.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/test-case-preferences/test-case-preferences.png")} width={700} alt="Test Case Preferences" /><br /><br /> </p> 

## <a id="id_1" class="anchor_top_offset"/>Test Case Calling

<p xmlns="http://www.w3.org/1999/xhtml" className="p">The <span className="ph uicontrol">Test Case Calling</span> option allows you to specify how Katalon Studio should behave when you call another test case as a test step. To learn more about this function, see <a className="xref" href="/katalon-studio/create-test-cases/call-test-case-in-katalon-studio">Call Test Case</a>.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">For example, we call the "TC1_Verify Successful/Login test case", with two variables named <code className="ph codeph">Username</code> and <code className="ph codeph">Password</code>. Their variables are displayed in the image below:</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/test-case-preferences/830-calling-example.png")} width={700} alt="example" /><br /><br /></p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p"><span className="ph uicontrol">Generate variable with default value</span>: The called test case uses the default value of its variables.</p><pre className="pre codeblock"><code>WebUI.callTestCase(findTestCase('Main Test Cases/TC1_Verify Successful Login'), [('Username') : 'John Doe', ('Password') : 'ThisIsNotAPassword'], FailureHandling.STOP_ON_FAILURE){"\n"}</code></pre></li><li className="li"><p className="p"><span className="ph uicontrol">Generate variable with the same name as the exposed variable of the called test case</span>: The called test case uses its variable names as variable values.</p><pre className="pre codeblock"><code>WebUI.callTestCase(findTestCase('Main Test Cases/TC1_Verify Successful Login'), [('Username') : Username, ('Password') : Password], FailureHandling.STOP_ON_FAILURE){"\n"}</code></pre><ul className="ul"><li className="li"><span className="ph uicontrol">Expose variables automatically after choosing the called test case</span>: At the <span className="ph uicontrol">Variables</span> tab, all variables of the called test case are also added to the current test case.</li></ul></li></ul> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">To learn more about supported types of variables in Katalon Studio, refer to this document: <a className="xref" href="/katalon-studio/data-driven-testing/data-driven-testing-with-katalon-studio#id__section-ddt-variables">Variable Types</a>.</p> 
    

## <a id="id_2" class="anchor_top_offset"/>Default Open View

    
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">By default, Katalon Studio opens your test case in the manual   view. You can choose to always open your test case in the manual   view or the script view.</p> 
    
  

## <a id="id_3" class="anchor_top_offset"/>Default Keyword Type

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><span className="ph uicontrol">Default Keyword</span>: Based on your frequently used     types of testing, you can set the <span className="ph uicontrol">Default Keyword       Type</span> as WebUI, Mobile, Cucumber, Web Service, Windows, or     TestNG. For example, you set the default keyword type as     <code className="ph codeph">WebUI</code>. In the test case editor, whenever you click     <span className="ph uicontrol">Add</span>, a new WebUI keyword is added as a new test     step.</li></ul> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">In each keyword type, you can also set a default keyword. For   example, you set <span className="ph uicontrol">Accept Alert</span> as the default   keyword for the <span className="ph uicontrol">WebUI</span> keyword type. In the test   case editor, whenever you click <span className="ph uicontrol">Add</span>, the   <span className="ph uicontrol">Accept Alert</span> is added as a new test step by   default.</p> 

## <a id="id_4" class="anchor_top_offset"/>Line-wrapping Settings

<p xmlns="http://www.w3.org/1999/xhtml" className="p">When you edit in script view, depending on how you want to view your scripts, you can enable/disable the line-wrapping to wrap up the code lines in customized maximum line width.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">When switching from the manual mode to the script mode, you can also wrap the code lines by pressing a keyboard combination of <kbd className="ph userinput">⌘</kbd>+<kbd className="ph userinput">Shift</kbd>+<kbd className="ph userinput">F</kbd> for macOS or <kbd className="ph userinput">Ctrl</kbd>+<kbd className="ph userinput">Shift</kbd>+<kbd className="ph userinput">F</kbd> for Windows and Linux.</p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">     <p className="p">Line-wrapping disabled:</p>     <p className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/test-case-preferences/wrap.png")} alt="Before the line-wrapping enabled" /><br /><br />     </p>   </li><li className="li">     <p className="p">Line-wrapping enabled:</p>     <p className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/test-case-preferences/wrapped.png")} alt="After the line-wrapping enabled" /><br /><br />     </p>   </li></ul> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">See also</strong>:</p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"> <a className="xref" href="/katalon-studio/get-started/workspace-settings/katalon-studio-preferences/preferences-in-katalon-studio">Katalon Preferences</a>   </li><li className="li"> <a className="xref" href="/katalon-studio/get-started/workspace-settings/katalon-studio-preferences/import-preferences-to-katalon-studio">Import Preferences</a>   </li><li className="li"> <a className="xref" href="/katalon-studio/get-started/workspace-settings/katalon-studio-preferences/configure-proxy-preferences-in-katalon-studio">Proxy Preferences</a>   </li><li className="li"> <a className="xref" href="/katalon-studio/get-started/workspace-settings/katalon-studio-preferences/object-spy-preferences-in-katalon-studio">Object Spy Preferences</a>   </li></ul> 
