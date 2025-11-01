---
hide_title: true
title: Kobiton integration with TestOps
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="id-eo7qstml" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Kobiton integration with TestOps

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Kobiton is a mobile device testing platform that accelerates mobile testing and delivery of mobile applications on real devices. By integrating Kobiton with Katalon TestOps, you can plan and execute tests using Kobiton's devices to improve your mobile testing efforts.</p> 
<div xmlns="http://www.w3.org/1999/xhtml" className="note important note_important"><span className="note__title">Important:</span> 
  <ul className="ul"><li className="li">You have already registered a <a className="xref j-external-link" href="https://kobiton.com/" target="_blank">Kobiton</a> account.</li></ul></div>

## <a id="task-8126" class="anchor_top_offset"/>Integrate Kobiton with Katalon TestOps

<section xmlns="http://www.w3.org/1999/xhtml" className="section context">To set up Kobiton integration in Katalon TestOps, follow these steps:</section> 
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol steps"><li className="li step stepexpand"><span className="ph cmd">Sign in to <a className="xref j-external-link" href="https://testops.katalon.io/login" target="_blank">Katalon TestOps</a> and go to your Project.</span></li><li className="li step stepexpand"><span className="ph cmd">Go to <span className="ph uicontrol">Configurations</span> &gt; <span className="ph uicontrol">Integrations</span>.</span></li><li className="li step stepexpand"><span className="ph cmd">Select <span className="ph uicontrol">Kobiton</span> from the dropdown list.</span></li><li className="li step stepexpand"><span className="ph cmd">Fill in the required information.</span><div className="itemgroup info"><img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-analytics/docs/testops-revamp-oct-kobiton-integration/kobiton-integration-page-fillin-2.png")} alt="kobiton integration page" /><br /><br /></div><div className="itemgroup info"><ul className="ul"><li className="li"><span className="ph uicontrol">Kobiton Device URL</span>: enter your Kobiton Device URL.</li><li className="li"><span className="ph uicontrol">Username</span>: enter your Kobiton username.</li><li className="li"><span className="ph uicontrol">Kobiton's API Key</span>: enter your Kobiton's API key.</li></ul></div></li><li className="li step stepexpand"><span className="ph cmd">Click <span className="ph uicontrol">Test Connection</span>, then click <span className="ph uicontrol">Save</span>.</span></li></ol> 
<section xmlns="http://www.w3.org/1999/xhtml" className="section result">You have enabled Kobiton integration. Now you can run tests with a Kobiton device in Katalon TestOps.</section> 

## <a id="id_2-c226jr5a" class="anchor_top_offset"/>Run tests with a Kobiton device

:::tip requirements
You have created a Script Repository on Katalon TestOps. See [Configure a Git repository in TestOps](/katalon-platform/integrations/cloud-device-integrations/kobiton-integration-with-testops).
:::
<p xmlns="http://www.w3.org/1999/xhtml" className="p">After creating a Script Repository, you can schedule test runs with a Kobiton device by configuring the advanced settings in the <span className="ph uicontrol">Schedule Test Run</span> dialog. You can also execute test runs manually. See <a className="xref" href="#">Schedule test runs</a>.</p> 
