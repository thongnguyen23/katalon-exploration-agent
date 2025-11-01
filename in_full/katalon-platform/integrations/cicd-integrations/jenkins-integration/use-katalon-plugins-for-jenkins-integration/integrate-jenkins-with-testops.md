---
hide_title: true
title: Integrate Jenkins with TestOps
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="id" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Integrate Jenkins with TestOps

:::tip requirements
- You have downloaded and installed [Jenkins](https://jenkins.io/download/).
- You have downloaded and installed [Katalon Runtime Engine](/katalon-studio/execute-tests/katalon-runtime-engine/get-started-with-katalon-runtime-engine).
:::

## <a id="task-3099" class="anchor_top_offset"/>Install the Katalon plugin on Jenkins

<section xmlns="http://www.w3.org/1999/xhtml" className="section context">To run Katalon tests on Jenkins, you need to install the Katalon plugin on Jenkins. Do as follows:</section> 
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol steps"><li className="li step stepexpand"><span className="ph cmd">Sign in to Jenkins and go to <span className="ph uicontrol">Manage Jenkins</span> &gt;   <span className="ph uicontrol">Manage Plugins</span>. </span><div className="itemgroup stepresult">The <span className="ph uicontrol">Plugin Manager</span> page appears.</div></li><li className="li step stepexpand"><span className="ph cmd">Click on the <span className="ph uicontrol">Available</span> tab and search for the Katalon plugin.</span><div className="itemgroup info"><img className="image" width={850} src={useBaseUrl("/c1d37300-6af7-11ed-a602-0242cfbc79b5/jenkins-install-plugin.png")} alt="plugin-manager" /></div></li><li className="li step stepexpand"><span className="ph cmd">Select the plugin and choose  <span className="ph uicontrol">Install without restart</span>.</span></li></ol> 

## <a id="id_2" class="anchor_top_offset"/>Configure Test Runs in Katalon TestOps

You must schedule test runs in Katalon TestOps before assigning this schedule to Jenkins for test executions. See: [Schedule Test Runs](/katalon-platform/execute/test-execution-with-testops/schedule-test-runs-in-testops).

:::info notes
Choose the **Save Configurations** option in the **Schedule Test Run** dialog to schedule Test Runs for Jenkins.
:::

## <a id="task-222" class="anchor_top_offset"/>Execute Katalon TestOps plan on Jenkins

<section xmlns="http://www.w3.org/1999/xhtml" className="section context">To execute the test run scheduled from Katalon TestOps on Jenkins, do as follows:</section> 
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol steps"><li className="li step stepexpand"><span className="ph cmd">On Jenkins, create a new <span className="ph uicontrol">Freestyle</span> project.</span></li><li className="li step stepexpand"><span className="ph cmd">In <span className="ph uicontrol">Build Steps</span>, add <span className="ph uicontrol">Execute Katalon TestOps Plan</span>.</span><div className="itemgroup info"><img className="image" width={500} src={useBaseUrl("/c1acb120-6af7-11ed-a602-0242cfbc79b5/jenkins-execute-kt-plan.png")} alt="execute Katalon TestOps plan" /></div><div className="itemgroup stepresult"><p className="p">The <span className="ph uicontrol">Execute Katalon TestOps Plan</span> is added as a build step.</p><p className="p"><img className="image" width={850} src={useBaseUrl("/c19bc130-6af7-11ed-a602-0242cfbc79b5/jenkins-build-step.png")} alt="execute Katalon TestOps plan" /></p></div></li><li className="li step stepexpand"><span className="ph cmd">In <span className="ph uicontrol">Server URL</span>, enter your TestOps server URL: <code className="ph codeph">https://testops.katalon.io</code>.</span></li><li className="li step stepexpand"><span className="ph cmd">In <span className="ph uicontrol">Credentials</span>, add a secret text with the secret value is your Katalon API key.</span><div className="itemgroup info"><img className="image" width={600} src={useBaseUrl("/c172dc70-6af7-11ed-a602-0242cfbc79b5/jenkins-add-credentials.png")} alt="add credentials" /></div></li><li className="li step stepexpand"><span className="ph cmd">After you added your Katalon API key, select it and click on <span className="ph uicontrol">Test Connection</span>. If you are successfully connected, you can retrieve your projects and test plan.</span><div className="itemgroup info"><img className="image" width={600} src={useBaseUrl("/c1cc4710-6af7-11ed-a602-0242cfbc79b5/jenkins-test-connection.png")} /></div></li><li className="li step stepexpand"><span className="ph cmd">Choose your project, then choose the test plan that you want to execute.</span></li><li className="li step stepexpand"><span className="ph cmd">Save your project, then click <span className="ph uicontrol">Build Now</span>.</span></li></ol> 
<section xmlns="http://www.w3.org/1999/xhtml" className="section result">Your test run is executed. You can view the execution log in <span className="ph uicontrol">Console Output</span>.<p className="p">After the test is completed, you can go back to Katalon TestOps to view and analyze your report.</p></section> 
