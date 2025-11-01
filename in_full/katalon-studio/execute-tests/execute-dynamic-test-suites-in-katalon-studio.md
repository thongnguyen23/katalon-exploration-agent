---
hide_title: true
title: Execute dynamic test suites in Katalon Studio
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="concept-3696" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Execute dynamic test suites in <span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon Studio</span> 

<p xmlns="http://www.w3.org/1999/xhtml" className="p">This guide shows you how to execute a dynamic test suite in <span className="ph">Katalon Studio</span>.</p> 
<nav xmlns="http://www.w3.org/1999/xhtml" role="navigation" className="related-links"><div className="linklist"><strong>Previous step</strong><br /><br /><ul className="linklist"><li className="linklist"><a className="link" href="/katalon-studio/manage-test-artifacts/dynamic-test-suite/manage-dynamic-test-suites-in-katalon-studio">Manage dynamic test suites in Katalon Studio</a></li></ul></div></nav> 

## <a id="id_2" class="anchor_top_offset"/>Modify execution information

<p xmlns="http://www.w3.org/1999/xhtml" className="shortdesc">Before executing a test suite or a dynamic test suite, you might want to modify the execution information, including timeout, retry, and email recipient list for test execution reports.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">You can specify additional configurations for the test suite execution by expanding the <span className="ph uicontrol">Execution Information</span> section as below:</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" width={700} src={useBaseUrl("/be4e4860-64ab-11ed-a602-0242cfbc79b5/ks-execution-information.png")} /></p> 

### <a id="concept-8095" class="anchor_top_offset"/>Set implicit timeout in a test suite execution

<p xmlns="http://www.w3.org/1999/xhtml" className="p">In <span className="ph uicontrol">Implicit timeout</span>, you can decide the timeout period that Katalon Studio waits for a page to be loaded by choosing one of the following options:<img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/create-test-suite/implicit-timeout.png")} width={500} alt="implicit timeout" /><br /><br /></p> 
<div xmlns="http://www.w3.org/1999/xhtml" className="p"><ul className="ul"><li className="li"><span className="ph uicontrol">Use default</span>: Use the predefined default value in <span className="ph uicontrol">Project Settings</span> &gt; <span className="ph uicontrol">Execution</span> &gt; <span className="ph uicontrol">Default wait for element to timeout (in seconds)</span>.</li><li className="li"><span className="ph uicontrol">User define</span>: Set a custom waiting time. Input a value in seconds.</li></ul></div>

### <a id="concept-8352" class="anchor_top_offset"/>Retry after executing all

Katalon allows you to rerun test cases in a failed test suite execution to identify flaky tests.

To do so, in the **Retry after executing all** text field, set the desired number of retry times. By default, this is set to 0.

<img src="https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/dynamic-test-suite-ks/KS-DYNAMIC-Retry-options.png" alt="retry after executing all screen" /> <br/>

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

## <a id="task-1705" class="anchor_top_offset"/>Execute a test suite

<section xmlns="http://www.w3.org/1999/xhtml" className="section context">To execute a test suite or a dynamic test suite, follow these steps:</section> 
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol steps"><li className="li step stepexpand"><span className="ph cmd">In <span className="ph uicontrol">Tests Explorer</span>, open a test suite or a dynamic test suite.</span></li><li className="li step stepexpand"><span className="ph cmd">Click on the drop-down of <span className="ph uicontrol">Run</span> and select an environment to execute the test suite.</span><div className="itemgroup info"><p className="p"><img className="image" width={250} src={useBaseUrl("/138e0150-3241-11ed-9930-0242fe3e4a3f/ks-execute-test-suite.png")} /></p><p className="p">If you only click on <span className="ph uicontrol">Run</span>, Katalon Studio executes the test suite with the default execution environment defined in <span className="ph uicontrol">Project Settings</span> &gt; <span className="ph uicontrol">Execution</span> &gt; <span className="ph uicontrol">Default execution</span>. See <a className="xref" href="/katalon-studio/manage-projects/project-settings/execution-settings-in-katalon-studio">Execution settings in <span className="ph">Katalon Studio</span></a>.</p></div></li><li className="li step stepexpand"><span className="ph cmd">Click <span className="ph uicontrol">Run</span>.</span></li></ol> 
<section xmlns="http://www.w3.org/1999/xhtml" className="section result"><p className="p">The <span className="ph uicontrol">Job Progress</span> is triggered automatically to show the progress while your test suite is being executed.</p><img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/create-test-suite/job-progress.png")} width={600} alt="job progress" /><br /><br /><p className="p">You can also run  a test suite or a dynamic test suite in console mode. For detailed instructions on test execution in console mode, you can refer to this document: <a className="xref" href="/katalon-studio/execute-tests/katalon-runtime-engine/command-line-syntax-in-katalon-runtime-engine">Command-line syntax in Katalon Runtime Engine</a>.</p></section> 
