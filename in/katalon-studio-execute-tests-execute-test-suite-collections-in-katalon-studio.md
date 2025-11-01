---
hide_title: true
title: Execute test suite collections in Katalon Studio
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="concept-742" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Execute test suite collections in <span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon Studio</span> 

<p xmlns="http://www.w3.org/1999/xhtml" className="shortdesc">This guide shows you how to configure, perform, and schedule your test suite collections in <span className="ph">Katalon Studio</span>.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">You can execute a test suite collection in sequential or parallel mode. The behaviors of these two modes are described as follows.</p> 

## Sequential mode

<p xmlns="http://www.w3.org/1999/xhtml" className="p">The sequential mode allows you to execute the test suites one after another.</p> 

## Parallel mode

<div xmlns="http://www.w3.org/1999/xhtml" className="p">The parallel mode allows you to execute multiple test suites at the same time. With the parallel mode, you can  set: <ul className="ul"><li className="li"><p className="p"><span className="ph uicontrol">Max concurrent instances</span>: The maximum number of test suites executing at the same time. </p></li><li className="li"><p className="p"><span className="ph uicontrol">Delay between instances (in seconds)</span>: The delay time between each test suite execution from 0-999 seconds.</p></li></ul> This function reduces the risk of CPU spike issues when there are too many concurrent instances. When a test suite is ready to start, Katalon Studio  prints the following message in the <span className="ph uicontrol">Event Log</span> tab:<pre className="pre codeblock"><code>Test suite ${"{"}testSuiteID{"}"} is ready to start at ${"{"}currentTimeStamp{"}"}</code></pre><img className="image" width={700} src={useBaseUrl("/be51f1e0-64ab-11ed-a602-0242cfbc79b5/ks-delay-between.png")} /></div>

## <a id="task-1662" class="anchor_top_offset"/>Execute a test suite collection

<section xmlns="http://www.w3.org/1999/xhtml" className="section context">To execute a test suite collection, follow these steps: </section> 
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol steps"><li className="li step stepexpand"><span className="ph cmd">In a test suite collection, click <span className="ph uicontrol">Execution Information</span>.</span><div className="itemgroup stepxmp"><img className="image" src={useBaseUrl("/be5c0400-64ab-11ed-a602-0242cfbc79b5/ks-852-execution-information.png")} /></div></li><li className="li step stepexpand"><span className="ph cmd">Select <span className="ph uicontrol">Sequential</span> or <span className="ph uicontrol">Parallel</span> mode.</span><div className="itemgroup info">If you choose <span className="ph uicontrol">Parallel</span> mode, you need to set the <span className="ph uicontrol">Max concurrent instances</span> and the delay time between instances.</div></li><li className="li step stepexpand"><span className="ph cmd">For each test suite, click on <span className="ph uicontrol">Run with</span> to select execution environments.</span><div className="itemgroup info"><p className="p"><img className="image" width={700} src={useBaseUrl("/be0b7300-64ab-11ed-a602-0242cfbc79b5/ks-select-tsc-environment.png")} /></p></div><div className="itemgroup info">If you choose <span className="ph uicontrol">TestCloud</span> or <span className="ph uicontrol">Mobile</span>, you need to click on <span className="ph uicontrol">Run Configuration</span> for further set up.</div></li><li className="li step stepexpand"><span className="ph cmd">Choose a profile to run your test suite.</span></li><li className="li step stepexpand"><span className="ph cmd">In the <span className="ph uicontrol">Run</span> column, you can select which test suites to be run in this execution.</span></li><li className="li step stepexpand"><span className="ph cmd">Once you are done, save your test suite collection and  click <span className="ph uicontrol">Execute</span>.</span><div className="itemgroup stepxmp"><img className="image" width={700} src={useBaseUrl("/be27fbb0-64ab-11ed-a602-0242cfbc79b5/ks-test-suite-collection-execute.png")} /></div></li></ol> 
<section xmlns="http://www.w3.org/1999/xhtml" className="section result"><p className="p">The <span className="ph uicontrol">Job Progress</span> is triggered automatically to show the progress while your test suite collection  is being executed.</p><p className="p"><img className="image" width={700} src={useBaseUrl("/be389d80-64ab-11ed-a602-0242cfbc79b5/ks-job-progress-tsc.png")} /></p></section> 
