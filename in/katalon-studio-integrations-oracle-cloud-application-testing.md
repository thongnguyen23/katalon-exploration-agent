---
hide_title: true
title: Oracle Cloud application testing
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="concept-895" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Oracle Cloud application testing

<p xmlns="http://www.w3.org/1999/xhtml" className="p">This article guidelines how <span className="ph">Katalon Studio</span> helps you automate Oracle Web platform. We will demonstrate a test case for create and delete a new Cadence. </p> 

## <a id="task-3191" class="anchor_top_offset"/>How to automate Oracle Cloud application testing

<div xmlns="http://www.w3.org/1999/xhtml" className="section prereq p">
  <ul className="ul"><li className="li">
      <p className="p">Clone our sample project <a className="xref j-external-link" href="https://github.com/katalon-studio-samples/katalon-oracle-sample" target="_blank">Github repository.</a></p>
    </li><li className="li">
      <p className="p">Katalon Studio</p>
    </li><li className="li">
      <p className="p">Oracle account </p>
    </li></ul>
</div>
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol steps"><li className="li step stepexpand"><span className="ph cmd">In <span className="ph">Katalon Studio</span>, go to <span className="ph menucascade"><span className="ph uicontrol">Project</span><abbr title="and then"> &gt; </abbr><span className="ph uicontrol">Settings</span><abbr title="and then"> &gt; </abbr><span className="ph uicontrol">Test Design</span><abbr title="and then"> &gt; </abbr><span className="ph uicontrol">WebUI</span></span> and change the priority of Xpath Locators.<img className="image" src={useBaseUrl("/769b9cb0-f54d-11ed-878a-0242c7a41fd4/KS-_change_priority_of_xpath_locators.png")} alt="change priority of Xpath locators" /></span></li><li className="li step stepexpand"><span className="ph cmd">Record test script via Katalon Recorder and save test objects and test cases. You can refer to <a className="xref" href="/katalon-studio/record-and-spy/webui-record-and-spy-utilities/record-web-utility-in-katalon-studio">Record Web utility in Katalon Studio</a>.</span><div className="itemgroup info">You can also use the test in our sample project, by updating the application URL, Username, and Password inside the Default Profile. Refer to <a className="xref" href="/katalon-studio/data-driven-testing/global-variables-and-execution-profile">Global variables and Execution profile</a>.  <img className="image" src={useBaseUrl("/74b30690-f54d-11ed-878a-0242c7a41fd4/KS-execute_oracle_sample_test.png")} alt="execute Oracle sample test" /></div></li><li className="li step stepexpand"><span className="ph cmd">Run the test execution. You can refer to <a className="xref" href="/katalon-studio/execute-tests/execute-tests-with-katalon-studio-overview">Execute tests with Katalon Studio overview</a>.</span></li><li className="li step stepexpand"><span className="ph cmd">Verify the test execution result. You can refer to <a className="xref" href="/katalon-platform/analyze/reports/view-test-reports/view-test-run-results/view-a-test-run-summary">View test runs and execution logs</a>.</span></li></ol> 
