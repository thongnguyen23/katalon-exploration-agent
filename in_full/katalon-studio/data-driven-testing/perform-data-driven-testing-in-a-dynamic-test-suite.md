---
hide_title: true
title: Perform data-driven testing in a dynamic test suite
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="id_11" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Perform data-driven testing in a dynamic test suite

You can perform data-driven testing by running a dynamic test suite with multiple data points.

:::tip requirements
An active Katalon Studio Enterprise license.
:::
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Follow these steps:</p> 
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol"><li className="li">     <p className="p">Configure data binding for the test cases. See: <a className="xref" href="/katalon-studio/data-driven-testing/data-driven-testing-at-test-case-level">Data-driven testing at the test case level</a>.</p>   </li><li className="li">     <p className="p">Add the associated test cases to a dynamic test suite via a search query. See above: <a className="xref" href="/katalon-studio/manage-test-artifacts/dynamic-test-suite/manage-dynamic-test-suites-in-katalon-studio#task-e8973c4f">Add test cases to a dynamic test suite</a>.</p>     <p className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/ddt-test-case-level/KS-DDT-Dynamic-Test-suite.png")} alt="Test cases added by query" /><br /><br /></p>   </li><li className="li">     <p className="p">Hit <strong className="ph b">Run</strong> to execute the dynamic test suite. Test cases in the dynamic test suite are then executed with the configured test data.</p>   </li><li className="li">     <p className="p">Verify the data binding and test execution results in <strong className="ph b">Log Viewer</strong>.</p>     <p className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/dynamic-test-suite-ks/KS-DYNAMIC-DDT-Log-Viewer.png")} alt="Test cases added by query" /><br /><br />     </p>   </li></ol> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">See also</strong> </p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"> <a className="xref" href="/katalon-studio/test-reports/view-test-reports/view-and-customize-execution-log-in-katalon-studio#id_1">View and Customize Execution Log</a>   </li><li className="li"> <a className="xref" href="/katalon-studio/integrations/test-management/configure-testrail-integration-in-katalon-studio#task-6760">Query Test Cases linked to TestRail in Dynamic Test Suite</a>   </li></ul> 
