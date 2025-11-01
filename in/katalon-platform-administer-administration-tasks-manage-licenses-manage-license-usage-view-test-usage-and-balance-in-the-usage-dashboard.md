---
title: View Test Usage and Balance in the Usage Dashboard (Legacy)
---
import useBaseUrl from '@docusaurus/useBaseUrl';
import Reusable from '@site/src/reusable/Reusable.mdx';

<Reusable />

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Organizations in <span className="ph">Katalon TestOps</span> are limited in how many tests can be run monthly, defined as your monthly <em className="ph i">quota</em>. This quota is defined by the license plan of your Account. You can view the current test execution quota, usage, and remaining balance in the <strong className="ph b">Usage Dashboard</strong>.</p> 
<div xmlns="http://www.w3.org/1999/xhtml" className="note important note_important"><span className="note__title">Important:</span> <ul className="ul"><li className="li"><span className="ph">Katalon TestOps</span> subscription.</li><li className="li">Owner or Admin role in an Organization.</li></ul><p className="p">Find out more about the licensing model and test execution quota here: <a className="xref" href="#">Katalon Platform Plans</a>.</p></div>

## <a id="task-9291" class="anchor_top_offset"/>Navigate to the Usage Dashboard

<section xmlns="http://www.w3.org/1999/xhtml" className="section context">To navigate to the <span className="ph uicontrol">Usage Dashboard</span>, follow these steps:</section> 
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol steps"><li className="li step stepexpand"><span className="ph cmd">Sign in to <a className="xref j-external-link" href="https://my.katalon.com/" target="_blank">TestOps Admin</a> and select your Account.</span></li><li className="li step stepexpand"><span className="ph cmd">From the Account admin page, select your Organization.</span><div className="itemgroup info"><img className="image" width={800} src={useBaseUrl("/10936890-bf7c-11ee-ac6d-0242c7a41fd4/KT-Acount-page.png")} alt="Account page" /></div><div className="itemgroup stepresult">The Organization admin page appears.</div></li><li className="li step stepexpand"><span className="ph cmd">Navigate to the <span className="ph uicontrol">Dashboard</span> section then select <span className="ph uicontrol">Katalon Platform</span>.</span><div className="itemgroup info"><p className="p">The <span className="ph uicontrol">Usage Dashboard</span> appears as below.</p><img className="image" width={700} src={useBaseUrl("/cf691050-3e48-11ed-9930-0242fe3e4a3f/TestOps-Katalon-Platform-Usage-dashboard.png")} alt="Katalon Platform usage dashboard" /></div></li></ol> 

## <a id="id_2" class="anchor_top_offset"/>Test Results Panel

<p xmlns="http://www.w3.org/1999/xhtml" className="p">The <span className="ph uicontrol">Test Results</span> panel displays a test result counter and your monthly quota. To view your remaining balance, hover your cursor over the panel.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" width={500} src={useBaseUrl("/ce4773b0-3e48-11ed-9930-0242fe3e4a3f/Katalon-Platform-Test-Result-panel.png")} alt="Katalon Platform Test Results panel" /></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">The <span className="ph uicontrol">Test Results</span> here refers to execution result of test runs scheduled and executed on <span className="ph">Katalon TestOps</span>. One test run usually encompasses multiple test cases and therefore, multiple test results. As illustrated in the screenshot below, test runs and test results are two different metrics. The difference in terminology can also be found in <a className="xref j-external-link" href="https://docs.katalon.com/docs/get-started/terminology-and-formulas#test-execution" target="_blank">Terminology and Formulas</a>. <img className="image" src={useBaseUrl("/44505f90-faeb-11ed-878a-0242c7a41fd4/TO-_project_dashboard.png")} alt="Project dashboard on TestOps" /></p> 
<div xmlns="http://www.w3.org/1999/xhtml" className="note note note_note"><span className="note__title">Note:</span> <ul className="ul"><li className="li">When you reach your monthly quota, you cannot run any more tests on TestOps, but you can still upload your test results from Katalon Studio.</li><li className="li">For the first 3 months of any billing plan, including the free plan, you can fill 130% of your maximum quota at no extra cost.</li><li className="li">Your test executions counter is reset to 0 every month, starting from the first day of your free plan, or from the last time you upgraded your subscription plan.</li><li className="li">Upgrading your subscription renews your balance and sets the new date as the first day of the first month of your new billing plan. You can once again use 130% of your maximum quota for 3 months.</li></ul></div>

## <a id="id_3" class="anchor_top_offset"/>Test Activities Panel

<p xmlns="http://www.w3.org/1999/xhtml" className="p">The <span className="ph uicontrol">Test Activities</span> panel displays your weekly testing activity as a bar chart. Data includes tests run on <span className="ph">Katalon TestOps</span> as well as uploaded test results.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" width={700} src={useBaseUrl("/d0aeafb0-3e48-11ed-9930-0242fe3e4a3f/Katalon-Platform-Test-Activities-panel.png")} alt="Test Activities panel" /></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Two numbers are displayed on the right side of the bar chart:</p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p"> <strong className="ph b">Test Results</strong> represents the total number of tests executed the preceding week.</p></li><li className="li"><p className="p"> <strong className="ph b">Test Duration</strong> represents the total time spent executing tests the preceding week.</p></li></ul> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Learn more about uploading test results to TestOps: <a className="xref" href="#">Upload Test Results to Katalon TestOps from Katalon Studio</a>.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">See also: <a className="xref" href="#">Upgrade Katalon Platform Subscription</a>.</p> 
