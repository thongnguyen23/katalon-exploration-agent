---
title: Set up CircleCI test environments for TestOps (Legacy)
---
import useBaseUrl from '@docusaurus/useBaseUrl';
import Reusable from '@site/src/reusable/Reusable.mdx';

<Reusable />


In Katalon TestOps, you can set up a CircleCI test environment to schedule and execute tests remotely.

:::tip requirements
- You have created a CircleCI account with a Github account.
- You have forked your Project to your Repository associated with your GitHub account. You can also fork this sample project, [TestOps CircleCI sample](https://github.com/katalon-studio-samples/testops-circleci-sample) for testing.
- You have followed your Project in CircleCI.
:::

## <a id="task-2431" class="anchor_top_offset"/>Set up a CircleCI Test Environment

<p xmlns="http://www.w3.org/1999/xhtml" className="shortdesc"> </p> 
<section xmlns="http://www.w3.org/1999/xhtml" className="section context">To set up a CircleCI Test Environment, follow these steps:</section> 
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol steps"><li className="li step stepexpand"><span className="ph cmd">Sign in to <a className="xref j-external-link" href="https://testops.katalon.io/login" target="_blank">Katalon TestOps</a> and go to <span className="ph menucascade"><span className="ph uicontrol">TestOps Settings</span><abbr title="and then"> &gt; </abbr><span className="ph uicontrol">Organization Setup</span></span>.</span><div className="itemgroup info"><img className="image" width={500} src={useBaseUrl("/cbcde300-9dea-11ee-b8c3-0242c7a41fd4/TO_December_20_2023_TestOps_Settings.png")} alt="Organization setup within the TestOps settings menu." /></div><div className="itemgroup stepresult">This shows the <span className="ph uicontrol">Test Environments</span> page. It also lists the agents you have. <img className="image" width={600} src={useBaseUrl("/cbd58420-9dea-11ee-b8c3-0242c7a41fd4/TO_Decemeber_20_2023_Test_Environments_page.png")} alt="Current Agents in Katalon TestOps." /></div></li><li className="li step stepexpand"><span className="ph cmd">Click on the <span className="ph uicontrol">CircleCI</span> tab.</span><div className="itemgroup info"><img className="image" width={500} src={useBaseUrl("/73124a10-9e1e-11ee-b8c3-0242c7a41fd4/TO_December_20_2023_CircleCI_Tab.png")} alt="The CircleCI tab within the Test Environments section." /></div><div className="itemgroup stepresult">This shows the <span className="ph uicontrol">CircleCI Test Environments</span> page. </div></li><li className="li step stepexpand"><span className="ph cmd">Click on the <span className="ph uicontrol">Create CircleCI Test Environment</span> button at the upper right corner.</span><div className="itemgroup info"><img className="image" src={useBaseUrl("/75357830-9e1e-11ee-b8c3-0242c7a41fd4/TO_Decemeber_20_2023_Create_CircleCI_Test_Environment_button.png")} alt="The Create CircleCI Test Environment button at the upper right corner." /></div></li><li className="li step stepexpand"><span className="ph cmd">In the <span className="ph uicontrol">Agent Name</span> section, create a name for the Agent (e.g., <span className="ph uicontrol">CircleCI Agent</span>).</span></li><li className="li step stepexpand"><span className="ph cmd">In the <span className="ph uicontrol">URL</span> and <span className="ph uicontrol">Personal API Token</span> sections, input your CircleCI information.</span><div className="itemgroup info"><img className="image" width={700} src={useBaseUrl("/74ab60a0-9e1e-11ee-b8c3-0242c7a41fd4/TO_Decemeber_20_2023_CircleCI_Test_Environment_Configuration.png")} alt="CircleCI Test Environment setup in Katalon TestOps" /></div></li><li className="li step stepexpand"><span className="ph cmd">Click <span className="ph uicontrol">Connect</span>.</span></li></ol> 
<section xmlns="http://www.w3.org/1999/xhtml" className="section result">You've set up your CircleCI Test Environment. The next step is to assign your agent to a project. To learn how, see: <a className="xref" href="/katalon-platform/execute/test-execution-with-testops/local-test-environments/create-a-local-test-environment-with-an-agent#task-4052">Manage the Agent status</a>. <p className="p">If you've already done both, then you can <a className="xref" href="/katalon-platform/execute/test-execution-with-testops/schedule-test-runs-in-testops#task-7544">Schedule test runs</a>. </p></section> 
