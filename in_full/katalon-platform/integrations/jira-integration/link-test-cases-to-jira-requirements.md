---
title: Link Test Cases to Jira Requirements (Legacy)
---
import useBaseUrl from '@docusaurus/useBaseUrl';
import Reusable from '@site/src/reusable/Reusable.mdx';

<Reusable />

<p xmlns="http://www.w3.org/1999/xhtml" className="p">You can link Test Cases to Jira Requirements and view them in   both Katalon TestOps and Jira.</p> 

## Requirements

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">In Jira, install this plugin from the Atlassian Marketplace website:   <a className="xref j-external-link" href="https://marketplace.atlassian.com/apps/1217501/katalon-bdd-test-automation-for-jira" target="_blank">Katalon Studio and TestOps integration.</a></p></li><li className="li"><p className="p">You have configured Jira integration. See: <a className="xref" href="/katalon-platform/integrations/jira-integration/enable-testops---jira-integration-for-test-management">Enable TestOps - Jira integration for test management</a>.</p></li></ul> 

## <a id="task-3348" class="anchor_top_offset"/>Link Test Cases to Jira Requirements

<section xmlns="http://www.w3.org/1999/xhtml" className="section context">To link test cases to Jira Requirements, follow these steps:</section> 
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol steps"><li className="li step stepexpand"><span className="ph cmd">Sign in to <a className="xref j-external-link" href="https://testops.katalon.io/login" target="_blank">Katalon         TestOps</a> and go to your Project.</span></li><li className="li step stepexpand"><span className="ph cmd">Go to <span className="ph uicontrol">Test Management</span> &gt; <span className="ph uicontrol">Test         Cases</span>. Click on a Test Case.</span><div className="itemgroup stepresult">The Test Case page appears.</div></li><li className="li step stepexpand"><span className="ph cmd">Enter the Jira issue in <span className="ph uicontrol">Jira Requirements</span>       (e.g., <span className="ph uicontrol">FLOW-13</span>), then click on the <em className="ph i">Link</em>       icon.</span><div className="itemgroup info"><img className="image" width={850} src={useBaseUrl("/43513bb0-5c11-11ed-a602-0242cfbc79b5/to-jira-requirements.png")} /></div></li></ol> 
<section xmlns="http://www.w3.org/1999/xhtml" className="section result"><p className="p">The Jira issue is  added to the <span className="ph uicontrol">Linked Issue</span>     section. You can click on the Jira issue to go to Jira and view the linked Test     Case.</p><p className="p"><img className="image" src={useBaseUrl("/43547000-5c11-11ed-a602-0242cfbc79b5/to-added-ticket.png")} /></p></section> 

## <a id="id_2" class="anchor_top_offset"/>View linked Test Cases in Jira

<p xmlns="http://www.w3.org/1999/xhtml" className="p">After linking a Test Case to Jira Requirements, you can click on   the Jira issue in Katalon TestOps, and it directs you to the Jira   issue in Jira.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" width={850} src={useBaseUrl("/434554d0-5c11-11ed-a602-0242cfbc79b5/ks-test-workflow.png")} /></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Click on the <span className="ph uicontrol">Linked Test Cases</span> section to see   the details of linked Test Cases.</p> 

## <a id="task-5705" class="anchor_top_offset"/>View Requirements in Katalon TestOps

<section xmlns="http://www.w3.org/1999/xhtml" className="section context">To view Requirements in Katalon TestOps, do as follows:</section> 
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol steps"><li className="li step stepexpand"><span className="ph cmd">Go to your <span className="ph uicontrol">Project</span> &gt; <span className="ph uicontrol">Planning</span> &gt;       <span className="ph uicontrol">Requirements</span>.</span><div className="itemgroup stepresult">The <span className="ph uicontrol">Requirements</span> page appears.</div></li><li className="li step stepexpand"><span className="ph cmd">Scroll down to the <span className="ph uicontrol">Requirements</span> section to view       all Jira issues with linked Test Cases.</span><div className="itemgroup info"><img className="image" width={850} src={useBaseUrl("/43404bc0-5c11-11ed-a602-0242cfbc79b5/to-requirements.png")} /><p className="p">See also: <a className="xref" href="/katalon-platform/integrations/jira-integration/link-test-runs-to-jira-defects-in-katalon-testops">Link           Test Runs to Jira Defects</a>.</p></div></li></ol> 
