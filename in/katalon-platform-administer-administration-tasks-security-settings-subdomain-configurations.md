---
title: Custom Domain Configurations (Legacy)
---
import useBaseUrl from '@docusaurus/useBaseUrl';
import Reusable from '@site/src/reusable/Reusable.mdx';

<Reusable />

# Custom Domain Configurations

<div xmlns="http://www.w3.org/1999/xhtml" className="note important note_important"><span className="note__title">Important:</span> <ul className="ul"><li className="li"><p className="p">You need to subscribe to <span className="ph">Katalon TestOps</span> <span className="ph">Ultimate</span> plan.</p></li><li className="li"><p className="p">You must be an <strong className="ph b">Owner</strong> or <strong className="ph b">Admin</strong> of your Account.</p></li></ul></div>

## <a id="task-6203" class="anchor_top_offset"/>Create a Custom Domain

<p xmlns="http://www.w3.org/1999/xhtml" className="shortdesc"> </p> 
<section xmlns="http://www.w3.org/1999/xhtml" className="section context">Follow these steps to create a Subdomain.</section> 
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol steps"><li className="li step stepexpand"><span className="ph cmd">Sign in to <a className="xref j-external-link" href="https://my.katalon.com/" target="_blank">TestOps Admin</a>.</span></li><li className="li step stepexpand"><span className="ph cmd">On the Account admin menu, select the <span className="ph uicontrol">Security</span> section on the left bar.</span><div className="itemgroup info">The <span className="ph uicontrol">Security Settings</span> page appears.<img className="image" width={850} src={useBaseUrl("/f79a8eb0-bf7e-11ee-ac6d-0242c7a41fd4/KT-Security_Settings1.png")} alt="Custom Domain" /></div></li><li className="li step stepexpand"><span className="ph cmd">Scroll down to the <span className="ph uicontrol">Custom Domain and SSO (Single Sign-On)</span> section then toggled on <span className="ph uicontrol">Enable Custom Domain</span>.</span><div className="itemgroup stepresult"><p className="p">Domain Name box appears.<img className="image" width={700} src={useBaseUrl("/f7fe0b70-bf7e-11ee-ac6d-0242c7a41fd4/KT-Enable-custom-domain.png")} alt="SSO - Enable Custom Domain" /></p></div></li><li className="li step stepexpand"><span className="ph cmd">Enter your desired Domain Name in the <span className="ph uicontrol">Custom Domain Name</span> section.</span><div className="itemgroup info"><div className="note note note_note"><span className="note__title">Note:</span> <ul className="ul"><li className="li"><p className="p">It can only contain the letters (A-Z) and numbers (0-9).</p></li></ul></div></div></li><li className="li step stepexpand"><span className="ph cmd">Click <span className="ph uicontrol">Update</span>.</span></li></ol> 
<section xmlns="http://www.w3.org/1999/xhtml" className="section result"><p className="p">After completing the configuration, you must access TestOps using your designated custom URL in the format:
`https://{yourcustomdomain}.katalon.io`. <br/> <br/> Access through the default URL `https://testops.katalon.io` will no longer be available.</p></section> 
