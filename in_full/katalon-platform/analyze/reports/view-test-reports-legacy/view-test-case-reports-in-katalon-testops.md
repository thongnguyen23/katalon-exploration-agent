---
title: View test case reports in Katalon TestOps (Legacy)
---
import useBaseUrl from '@docusaurus/useBaseUrl';

<p xmlns="http://www.w3.org/1999/xhtml" className="p">You can manage test cases in <span className="ph">Katalon TestOps</span> to evaluate test   case quality and visualize how the test case quality improves or   worsens over time.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">By doing so, your team can spot weak points in your software or   application deployment.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">With test management, you can also estimate the time it will   take to perform all your automated tests. This is useful in the   production stage, especially if you release critical updates.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">To help you manage test cases effectively, <span className="ph">Katalon TestOps</span>   categorizes test cases into the following types:</p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">Active test cases</li><li className="li">Stale test cases</li><li className="li">Slowest test cases</li><li className="li">Flaky test cases</li></ul> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">For a definition of each type of test cases, see <a className="xref" href="#">TestOps     Formulas.</a></p> 

## <a id="task-4799" class="anchor_top_offset"/>View active test cases reports

<section xmlns="http://www.w3.org/1999/xhtml" className="section context">To view active test cases reports, do as follow:</section> 
<div xmlns="http://www.w3.org/1999/xhtml" className="li step p"><span className="ph cmd">Go to <span className="ph uicontrol">Reports</span> &gt; <span className="ph uicontrol">Test Cases</span> &gt; <span className="ph uicontrol">Active</span>.</span><div className="itemgroup info"><img className="image" src={useBaseUrl("/8de6ce30-22b2-11ed-9930-0242fe3e4a3f/KT-JULY22-Active-test-case-reports.png")} alt="View active test cases reports" /></div></div>
<section xmlns="http://www.w3.org/1999/xhtml" className="section result">You can see all test cases with their most recently executed test runs here. You can click on an active test case to see its summary.</section> 

## <a id="task-1076" class="anchor_top_offset"/>View stale test cases reports

<section xmlns="http://www.w3.org/1999/xhtml" className="section context">To view stale test cases reports, do as follows:</section> 
<div xmlns="http://www.w3.org/1999/xhtml" className="li step p"><span className="ph cmd">Go to <span className="ph uicontrol">Reports</span> &gt; <span className="ph uicontrol">Test Cases</span> &gt; <span className="ph uicontrol">Stale</span>.</span><div className="itemgroup info"><img className="image" src={useBaseUrl("/8de9db70-22b2-11ed-9930-0242fe3e4a3f/KT-JULY22-stale-test-case-reports.png")} alt="View stale test cases reports" /></div></div>
<section xmlns="http://www.w3.org/1999/xhtml" className="section result">You can see the list of test cases which are outdated or no longer maintained. You can review these test cases to decide whether they need to be updated.</section> 

## <a id="task-8669" class="anchor_top_offset"/>View slowest test cases reports

<section xmlns="http://www.w3.org/1999/xhtml" className="section context">To view slowest test cases reports, do as follows:</section> 
<div xmlns="http://www.w3.org/1999/xhtml" className="li step p"><span className="ph cmd">Go to <span className="ph uicontrol">Reports</span> &gt; <span className="ph uicontrol">Test Cases</span> &gt; <span className="ph uicontrol">Slowest</span>.</span><div className="itemgroup info"><img className="image" src={useBaseUrl("/8de91820-22b2-11ed-9930-0242fe3e4a3f/KT-JULY22-slowest-test-case-reports.png")} alt="View slowest test cases reports" /></div></div>
<section xmlns="http://www.w3.org/1999/xhtml" className="section result">You can see the list of all Test Cases which have the longest average durations.</section> 

## <a id="task-6657" class="anchor_top_offset"/>View flaky test cases reports

<section xmlns="http://www.w3.org/1999/xhtml" className="section context">To view flaky test cases reports, do as follows:</section> 
<div xmlns="http://www.w3.org/1999/xhtml" className="li step p"><span className="ph cmd">Go to <span className="ph uicontrol">Reports</span> &gt; <span className="ph uicontrol">Test Cases</span> &gt; <span className="ph uicontrol">Flaky</span>.</span><div className="itemgroup info"><img className="image" src={useBaseUrl("/8de82dc0-22b2-11ed-9930-0242fe3e4a3f/KT-JULY22-flaky-test-case-reports.png")} alt="View flaky test cases reports" /></div></div>
<section xmlns="http://www.w3.org/1999/xhtml" className="section result">You can see the details of flaky test cases here. <span className="ph">Katalon TestOps</span> allows you to investigate deeper into the root causes of test flakiness, and assist with debugging.</section> 

## <a id="task-2411" class="anchor_top_offset"/>View test cases platform coverage

<div xmlns="http://www.w3.org/1999/xhtml" className="section prereq p"><ul className="ul"><li className="li"><p className="p">You need to subscribe to <span className="ph">Katalon TestOps Business</span> or    <span className="ph">Katalon TestOps Enterprise</span> plan. To request a trial, see <a className="xref" href="/katalon-platform/administer/katalon-platform-packages/katalon-trial-plan">TestOps Trial Plans</a>.</p></li></ul></div>
<section xmlns="http://www.w3.org/1999/xhtml" className="section context">To view test cases platform coverage, do as follows:</section> 
<div xmlns="http://www.w3.org/1999/xhtml" className="li step p"><span className="ph cmd">Go to <span className="ph uicontrol">Reports</span> &gt; <span className="ph uicontrol">Test Cases</span> &gt; <span className="ph uicontrol">Platform Coverage</span>.</span><div className="itemgroup info"><img className="image" src={useBaseUrl("/8de79180-22b2-11ed-9930-0242fe3e4a3f/KT-JULY22-platform-coverage-test-case-reports.png")} alt="Platform coverage in test cases" /></div></div>
<section xmlns="http://www.w3.org/1999/xhtml" className="section result">You can review test case quality based on operating systems and browsers. You can view quality changes on a weekly or monthly time scale.</section> 
