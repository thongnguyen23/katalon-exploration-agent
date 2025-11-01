---
hide_title: true
title: '[WebUI] Analyze test execution logs and debug the test case in Katalon Studio'
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="id" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>[WebUI] Analyze test execution logs and debug the test case in <span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon Studio</span> 

After executing a test case, Katalon Studio provides you with comprehensive execution logs in the **Log Viewer**. You can quickly investigate the logs to pinpoint the root causes of any issue and correct the test execution with Debug utilities.

This tutorial shows you how to analyze execution logs of a failed test case in the **Log Viewer** and debug the test case.

Here we reuse the test case ("Sign in the shopping page to purchase a tank top") from the tutorial [[WebUI] Create and Run Web UI Test Case using Record and Playback](/katalon-studio/get-started/sample-projects/webui/webui-create-and-run-web-ui-test-case-using-record-and-playback-in-katalon-studio).

You can download the sample project here: [Shopping Cart Tests](https://github.com/katalon-studio-samples/shopping-cart-tests).

In our example, the test case fails to find a Web element due to an unexpected change in the application under test (AUT). We look for the failed steps in the execution logs, find the root cause, correct the step, and resume execution using the **Run from here** Debug utility.

To use the Debug utility, you need to configure Katalon Studio to not terminate browser session when execution finishes. For detailed instructions, refer to this guide: [Execute and Debug a Test Case](/katalon-studio/debug-a-test-case/debug-a-test-case-in-katalon-studio#id_6).

## <a id="concept-1867" class="anchor_top_offset"/>Analyze test execution logs in Log Viewer

<p xmlns="http://www.w3.org/1999/xhtml" className="p">After executing the test case, <span className="ph">Katalon Studio</span> displays the results in the <strong className="ph b">Log Viewer</strong> as follows:</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/webui-analyze-execution-logs-and-debug/KS-Execution-Results.png")} width={750} alt="Test Execution overview" /><br /><br /> </p> 

Here we use the **Tree View** mode of the **Log Viewer** to analyze the logs. This mode displays execution logs in a structural way that helps you trace the Test execution and locate failed steps quickly.

Follow these steps to analyze the logs:

1. Switch to the **Tree View**. Toggle on the **Tree View** button on the top-right corner of the **Log Viewer**.
    
    <img src="https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/webui-analyze-execution-logs-and-debug/KS-Tree-View-Button.png" alt="KS tree view" />
    
    The **Tree View** displays the execution logs in a tree-like structure on the left pane. Each node in the tree corresponds to a step in the test case, and failed steps are marked in red.
    
    <img src="https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/webui-analyze-execution-logs-and-debug/KS-Log-Viewer-Tree-View.png" alt="KS bug logger" />
    
    On the right panel, the view displays detailed log messages of each step.
    
    <img src="https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/webui-analyze-execution-logs-and-debug/KS-Log-Viewer-Log-Message-Overview.png" alt="KS log reviewer right panel" width="600" />
    
2. To view warning messages of the failed step, click on the *expand* icon on the left of the step.
    
    Here the warnings indicate that Katalon Studio fails to find a test object with a specific XPath.
    
    <img src="https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/webui-analyze-execution-logs-and-debug/KS-Log-Viewer-Warnings.png" alt="KS Log reviewer" width="600" />
    
3. To view the detailed log message, click on the step. The log message is displayed on the right pane.
    
    <img src="https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/webui-analyze-execution-logs-and-debug/KS-Log-Viewer-Click-on-step.png" alt="KS log reviewer" width="600" />
    
    In the root cause section, the message shows an exception: `com.kms.katalon.core.webui.exception.WebElementNotFoundException: Web element with id ... not found.`
    
    <img src="https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/webui-analyze-execution-logs-and-debug/KS-Log-Viewer-Root-cause-section.png" alt="KS log reviewer" />
    
    To learn how to troubleshoot common exceptions in Web tests, you can refer to this document: [Troubleshoot common exceptions when executing web tests](/katalon-studio/troubleshooting/troubleshoot-web-automated-testing/troubleshoot-web-test-execution-exceptions-overview).
    
    Below the root cause section, the message displays the failed step in the form of test script.
    
    <img src="https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/webui-analyze-execution-logs-and-debug/KS-Log-Viewer-Error-Script.png" alt="KS log reviewer" />
    
    From the details provided, we know that Katalon Studio cannot locate the sign-in button with the id `'Object Repository/Page_Zack Market/input_Password_button_btn__2lzmo'` and the Object Locator `//*[@value = 'Signing_in']`.

:::info notes
- Execution logs of test cases are preserved only in the running session of Katalon Studio. Once you reload Katalon Studio, the logs will disappear.
:::
## <a id="id_2" class="anchor_top_offset"/>Debug the test case

<p xmlns="http://www.w3.org/1999/xhtml" className="p">After finding the root cause, we update the test object with a   new XPath, and use the <strong className="ph b">Run from here</strong> Debug utility   to resume the test execution.</p> 

### <a id="id_3" class="anchor_top_offset"/>Update the Object Locator

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Because a deprecated Object Locator causes the error, we can find the new Object Locator using the browser's <strong className="ph b">Inspector</strong> tool.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">In our example, we use the <strong className="ph b">Inspector</strong> tool to get the XPath of the corresponding Web element.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Follow these steps:</p> 
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol"><li className="li">     <p className="p">To get the new XPath, in the running browser instance, right-click on the target web element, and select <strong className="ph b">Inspect</strong>.</p>     <p className="p">Here we right-click on the Sign-in button that causes the error.</p>     <p className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/webui-analyze-execution-logs-and-debug/KS-Browser-right-click-on-element.png")} width={750} alt="Error Script" /><br /><br />     </p>   </li><li className="li">     <p className="p">In the inspector window, the selected element is highlighted, indicating the target element's location in the HTML DOM. Right-click on the highlighted line and select <strong className="ph b">Copy &gt; Copy XPath</strong>.</p>     <p className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/webui-analyze-execution-logs-and-debug/KS-Copy-XPath.png")} width={750} alt="Error Script" /><br /><br />     </p>   </li><li className="li">     <p className="p">Add the new XPath to the test object. Open the test object, in the test object view, specify <strong className="ph b">XPath</strong> as the <strong className="ph b">Selection Method</strong> and paste the copied XPath from step 2 in the <strong className="ph b">Selected Locator</strong> editor.</p>     <p className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/webui-analyze-execution-logs-and-debug/KS-Add-new-XPath.png")} width={750} alt="Error Script" /><br /><br />     </p>   </li></ol> 

### <a id="concept-3960" class="anchor_top_offset"/>Resume the test execution

<p xmlns="http://www.w3.org/1999/xhtml" className="p">After adding the new XPath to the test object, we use the <strong className="ph b">Run from here</strong> Debug utility to resume test execution without re-executing the entire test case.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Follow these steps to resume the test execution:</p> 
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol"><li className="li">     <p className="p">Resume executing from the failed step. Open the test case, right-click on the failed step, and select <strong className="ph b">Run from here</strong> &gt; <em className="ph i">The running browser session</em>.</p>     <p className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/webui-analyze-execution-logs-and-debug/KS-Run-from-here.png")} width={750} alt="Error Script" /><br /><br />     </p>   </li><li className="li">     <p className="p">After the test execution is completed, verify the results in the Log Viewer.</p>     <p className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/webui-analyze-execution-logs-and-debug/KS-Successful-Test-Execution.png")} width={750} alt="Error Script" /><br /><br />     </p>   </li></ol> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><strong className="ph b">See also</strong>: <a className="xref" href="/katalon-studio/test-reports/view-test-reports/view-and-customize-execution-log-in-katalon-studio">View and Customize Execution Log.</a></p> 
