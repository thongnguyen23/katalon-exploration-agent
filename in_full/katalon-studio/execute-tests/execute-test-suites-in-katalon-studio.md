---
hide_title: true
title: Execute test suites in Katalon Studio
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="concept-5022" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Execute test suites in <span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon Studio</span> 

<p xmlns="http://www.w3.org/1999/xhtml" className="p">This guide shows you how to configure  and perform test suite execution in <span className="ph">Katalon Studio</span>.</p> 
<nav xmlns="http://www.w3.org/1999/xhtml" role="navigation" className="related-links"><div className="linklist"><strong>Previous step</strong><br /><br /><ul className="linklist"><li className="linklist"><a className="link" href="/katalon-studio/manage-test-artifacts/manage-test-suites-in-katalon-studio">Manage test suites in Katalon Studio</a></li></ul></div></nav> 

## <a id="id_2" class="anchor_top_offset"/>Modify execution information

<p xmlns="http://www.w3.org/1999/xhtml" className="shortdesc">Before executing a test suite or a dynamic test suite, you might want to modify the execution information, including timeout, retry, and email recipient list for test execution reports.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">You can specify additional configurations for the test suite execution by expanding the <span className="ph uicontrol">Execution Information</span> section as below:</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" width={700} src={useBaseUrl("/be4e4860-64ab-11ed-a602-0242cfbc79b5/ks-execution-information.png")} /></p> 

### <a id="concept-8095" class="anchor_top_offset"/>Set implicit timeout in a test suite execution

<p xmlns="http://www.w3.org/1999/xhtml" className="p">In <span className="ph uicontrol">Implicit timeout</span>, you can decide the timeout period that Katalon Studio waits for a page to be loaded by choosing one of the following options:<img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/create-test-suite/implicit-timeout.png")} width={500} alt="implicit timeout" /><br /><br /></p> 
<div xmlns="http://www.w3.org/1999/xhtml" className="p"><ul className="ul"><li className="li"><span className="ph uicontrol">Use default</span>: Use the predefined default value in <span className="ph uicontrol">Project Settings</span> &gt; <span className="ph uicontrol">Execution</span> &gt; <span className="ph uicontrol">Default wait for element to timeout (in seconds)</span>.</li><li className="li"><span className="ph uicontrol">User define</span>: Set a custom waiting time. Input a value in seconds.</li></ul></div>

### <a id="concept-8352" class="anchor_top_offset"/>Retry after executing all

Katalon allows you to rerun test cases in a failed test suite execution to identify flaky tests.

To do so, in the **Retry after executing all** text field, set the desired number of retry times. By default, this is set to `0`.

<img src="https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/dynamic-test-suite-ks/KS-DYNAMIC-Retry-options.png" alt="retry after executing all" />


Choose one of the following options:
- **Retry all executions**: Retry all test cases when the test suite fails.
- **Retry failed executions only**: Retry only failed test cases when the test suite fails.

  For example, when a test suite execution fails, we want to rerun failed test cases in that test suite twice.

  In the **Retry after executing all** checkbox, we input 2 in the text field, then we choose the **Retry failed executions only** option.

  <img src="https://docs.katalon.com/be3bd1d0-64ab-11ed-a602-0242cfbc79b5/ks-retry-failed-executions-only.png" alt="retry after executing all screen" /> <br/>

<p xmlns="http://www.w3.org/1999/xhtml" className="p">In this case, the test suite is executed three times in total. The first one is the main execution, while the latter two are the retried executions when the first execution fails.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" width={600} src={useBaseUrl("/be184440-64ab-11ed-a602-0242cfbc79b5/ks-retry-progress.png")} /></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Katalon Studio automatically generates reports after each test execution.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" width={500} src={useBaseUrl("/bdfe0580-64ab-11ed-a602-0242cfbc79b5/ks-report-retry.png")} /></p> 

### <a id="concept-6469" class="anchor_top_offset"/>Retry failed execution immediately

:::tip requirements
An active Katalon Studio Enterprise license.
:::
<p xmlns="http://www.w3.org/1999/xhtml" className="p">By default, each test case is run only one time in a test suite execution. Suppose you want to rerun failed test cases several times to identify flaky tests before executing the next ones. You can set the desired number of retry times in <span className="ph uicontrol">Retry Failed Execution Immediately</span>. The failed test case will be rerun immediately until they pass or all retries are used up. If all rerun attempts fail, Katalon Studio marks that test case as <span className="ph uicontrol">Failed</span> and proceeds with the rest in the test suite.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><strong className="ph b">Consolidate Reports</strong></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Katalon Studio automatically consolidates reports in JUnit, HTML, PDF, and CSV format with one final test result for a test case. Browser-based or window-based videos are recorded for runs and reruns of a test case.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><strong className="ph b">Usage example</strong></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">In this example, we have a test suite with five test cases. We set <span className="ph uicontrol">Retry Failed Execution Immediately</span> for one and two times. When we run the test suite and a test fails, Katalon Studio immediately reruns the problematic test case until it passes or the maximum number of retries is reached.</p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">     <p className="p"> <strong className="ph b">Example 1</strong>: Execute the test suite with a Retry limit of 1:</p>     <p className="p"><img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/create-test-suite/ts-with-5-tc-and-retry-fail-1.png")} width={500} /><br /><br /></p>     <p className="p">You can see the test suite status once the test suite finishes executing. Because test case 3 is marked as <strong className="ph b">Failed</strong>, we open the <span className="ph uicontrol">Result</span> tab and expand test case 3 to investigate.</p>     <p className="p">test case 3 failed twice, once during the main run and once as a retried run. Only one retried run was allowed.</p>     <p className="p">At this point, <span className="ph">Katalon Studio</span> logged its final result as <strong className="ph b">Failed</strong> and continued to execute test case 4 and 5 with the same logic.</p>     <p className="p">You can view how many test cases in the test suite were executed and their final status in the <span className="ph uicontrol">Summary</span> tab. In this use case, the test suite has five total test cases; test cases 1, 2, and 4 pass while 3 and 5 fail.</p>     <p className="p"><img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/create-test-suite/retry-usage-example-result.png")} width={600} /><br /><br /></p>   </li><li className="li">     <p className="p"><strong className="ph b">Example 2</strong>: Execute the test suite with a Retry limit of 2:</p>     <p className="p">When we set the retry limit to 2, five test cases passed. Test cases 3 and 5 failed at the main run and first rerun but passed at the second try.</p>     <p className="p">Since test cases 3 and 5 did not succeed on the first try but still succeed after two tries, their result pattern is intermittent. This is a clear sign of test flakiness and can be further investigated.</p>     <p className="p"><img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/create-test-suite/retry-2-times-result.png")} width={600} alt="Retry failed execution immediately" /><br /><br /></p>   </li></ul> 

### <a id="task-2165" class="anchor_top_offset"/>Add mail recipients in <span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon Studio</span>  test suites

<div xmlns="http://www.w3.org/1999/xhtml" className="section prereq p"><ul className="ul"><li className="li"><p className="p">You have  set up a mail server, an email template, and a default recipient list in <span className="ph">Katalon Studio</span>. See: <a className="xref" href="/katalon-studio/test-reports/share-test-reports-via-email-in-katalon-studio">Share test reports via email in <span className="ph">Katalon Studio</span></a>.</p></li></ul></div>
<section xmlns="http://www.w3.org/1999/xhtml" className="section context">You can add an additional email list of recipients for a specific test suite reports. You can do this in a test suite or dynamic test suite user interface. Follow these steps:</section> 
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol steps"><li className="li step"><span className="ph cmd">Open a test suite or a dynamic test suite.</span></li><li className="li step"><span className="ph cmd">Expand the <span className="ph uicontrol">Execution Information</span> section. In the <span className="ph uicontrol">Mail Recipients</span> box, click <span className="ph uicontrol">Add</span>.</span></li><li className="li step"><span className="ph cmd">An <span className="ph uicontrol">Add recipient's email</span> dialog opens. Type in the email you want to send the reports to.</span></li></ol> 
<section xmlns="http://www.w3.org/1999/xhtml" className="section result">You have successfully added an additional email list to receive a specific test suite report. After the test execution, the default recipient list configured in <span className="ph uicontrol">Email settings</span> and the additional list in a test suite can receive the same test report. Duplicated emails only receive one test report.</section> 

## <a id="task-1705" class="anchor_top_offset"/>Execute a test suite

<section xmlns="http://www.w3.org/1999/xhtml" className="section context">To execute a test suite or a dynamic test suite, follow these steps:</section> 
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol steps"><li className="li step stepexpand"><span className="ph cmd">In <span className="ph uicontrol">Tests Explorer</span>, open a test suite or a dynamic test suite.</span></li><li className="li step stepexpand"><span className="ph cmd">Click on the drop-down of <span className="ph uicontrol">Run</span> and select an environment to execute the test suite.</span><div className="itemgroup info"><p className="p"><img className="image" width={250} src={useBaseUrl("/138e0150-3241-11ed-9930-0242fe3e4a3f/ks-execute-test-suite.png")} /></p><p className="p">If you only click on <span className="ph uicontrol">Run</span>, Katalon Studio executes the test suite with the default execution environment defined in <span className="ph uicontrol">Project Settings</span> &gt; <span className="ph uicontrol">Execution</span> &gt; <span className="ph uicontrol">Default execution</span>. See <a className="xref" href="/katalon-studio/manage-projects/project-settings/execution-settings-in-katalon-studio">Execution settings in <span className="ph">Katalon Studio</span></a>.</p></div></li><li className="li step stepexpand"><span className="ph cmd">Click <span className="ph uicontrol">Run</span>.</span></li></ol> 
<section xmlns="http://www.w3.org/1999/xhtml" className="section result"><p className="p">The <span className="ph uicontrol">Job Progress</span> is triggered automatically to show the progress while your test suite is being executed.</p><img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/create-test-suite/job-progress.png")} width={600} alt="job progress" /><br /><br /><p className="p">You can also run  a test suite or a dynamic test suite in console mode. For detailed instructions on test execution in console mode, you can refer to this document: <a className="xref" href="/katalon-studio/execute-tests/katalon-runtime-engine/command-line-syntax-in-katalon-runtime-engine">Command-line syntax in Katalon Runtime Engine</a>.</p></section> 
