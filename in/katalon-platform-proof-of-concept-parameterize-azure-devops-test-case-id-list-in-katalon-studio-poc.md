---
hide_title: true
title: Parameterize Azure DevOps Test Case ID List in Katalon Studio (PoC)
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="id" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Parameterize Azure DevOps Test Case ID List in <span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon Studio</span>  (PoC)

:::tip requirements
This Proof of Concept (PoC) is not ready for production use. We recommend using this PoC for evaluation purposes only.
:::

You can natively integrate with Azure DevOps (ADO) to map ADO test cases to test cases in Katalon Studio, and automatically submit test runs with results to ADO.

In fact, running a test can generate lots of results when you use the data-driven testing method. In this PoC, we provide a solution to set custom test iteration IDs, so that test iterations in Katalon Studio are automatically mapped to the related ADO test cases.

:::info What is an iteration?
- An iteration is a test case executed with a test data row.
:::

## Requirements

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">An active Katalon Studio Enterprise license.</li><li className="li">Azure Test Plans is already configured.</li><li className="li">Azure DevOps integration is already enabled and configured. See     <a className="xref" href="/katalon-studio/integrations/test-management/configure-azure-devops-test-plans-integration-in-katalon-studio">Integration       with Azure DevOps Test Plans</a>.</li></ul> 

## <a id="id_1" class="anchor_top_offset"/>Set Parameter in Azure Test Plans and in <span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon Studio</span> 

<p xmlns="http://www.w3.org/1999/xhtml" className="p">In this step, we will guide you through adding and calling a test case variable in the <strong className="ph b">ADO test case ID list</strong>.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">In Azure Test Plans</strong> </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">You can view your test case IDs in Azure Test Plan.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/associated-ADO-TC-IDs/test-case-ids.png")} alt="ado ID" /><br /><br /> </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">In Katalon Studio</strong> </p> 
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol"><li className="li">     <p className="p">Add a test case variable:</p>     <p className="p">Open your desired test case and switch to the <strong className="ph b">Variables</strong> tab. To create a variable, click <strong className="ph b">Add</strong>. For example, we create a number variable named <code className="ph codeph">ado_id</code>. To learn more about variables, see <a className="xref" href="/katalon-studio/data-driven-testing/test-case-variables">Test Case Variables</a>.</p>     <p className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/associated-ADO-TC-IDs/number-ado_id.png")} /><br /><br />     </p>   </li><li className="li">     <p className="p">Call a variable in the ADO test case ID list:</p>     <p className="p">Switch to the <strong className="ph b">Integration</strong> tab and select the <strong className="ph b">Azure</strong> integration. In the <strong className="ph b">ADO Test Case ID list</strong>, call the variable with the syntax <code className="ph codeph">${'{'}Your_variable_name{'}'}</code>, for example: <code className="ph codeph">${'{'}ado_id{'}'}</code>.</p>     <p className="p">You can map one test case ID in Katalon Studio with many test case IDs on ADO, IDs are separated by commas. Duplicated test case IDs will be used one time only.</p>     <p className="p">To check if the test case ID is valid, click <strong className="ph b">Verify</strong>.</p>     <p className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/associated-ADO-TC-IDs/verified.png")} alt="verify" /><br /><br />     </p>   </li></ol> 

## <a id="id_2" class="anchor_top_offset"/>Execute a test suite containing associated test cases in <span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon Studio</span> 

<ol xmlns="http://www.w3.org/1999/xhtml" className="ol"><li className="li"><p className="p">Add the test case above to a test suite.</p></li><li className="li"><p className="p">To conduct <strong className="ph b">Data Binding</strong>, in the test suite editor, click <strong className="ph b">Show Data Binding</strong>.</p><p className="p">In the <strong className="ph b">Test Data</strong> table, you can add or check your test data files. The <strong className="ph b">Variable Binding</strong> table shows your variable list with related test data files and values.</p><p className="p"><img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/associated-ADO-TC-IDs/ks-ddt-ado-binding.png")} alt="conduct data binding" /><br /><br /></p></li><li className="li"><p className="p">When you are done with the configuration, click <strong className="ph b">Run</strong> to execute your test suite. After the test suite execution, you can view your test results in ADO. Each test iteration in Katalon Studio is automatically mapped to related ADO test cases. Invalid ADO test case IDs are showed in <span className="ph">Katalon Studio</span> <strong className="ph b">Event Log</strong>.</p><p className="p"><img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/associated-ADO-TC-IDs/event-log-ado.png")} alt="event log" /><br /><br /></p><p className="p">In Azure Test Plans, you can find a report with a list of test iterations.</p><p className="p"><img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/associated-ADO-TC-IDs/report%20in%20ADO.png")} alt="report in ADO" /><br /><br /></p></li></ol> 
