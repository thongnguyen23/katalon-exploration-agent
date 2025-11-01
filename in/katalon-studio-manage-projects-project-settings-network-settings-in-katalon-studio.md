---
hide_title: true
title: Network settings in Katalon Studio
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="concept-6905" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Network settings in <span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon Studio</span> 

<p xmlns="http://www.w3.org/1999/xhtml" className="p">In <span className="ph">Katalon Studio</span> network settings, you can configure: </p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p"> Certificate setting. See <a className="xref" href="#task-6600">Bypass certificate validation in <span className="ph">Katalon Studio</span></a>.</p></li><li className="li"><p className="p">Client certificate settings. See <a className="xref" href="/katalon-studio/manage-projects/set-up-projects/api-testing/use-client-certificate-for-requests-in-api-projects-in-katalon-studio">Use client certificate for  requests in API projects</a>.</p></li></ul> 

## <a id="task-6600" class="anchor_top_offset"/>Bypass certificate validation in <span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon Studio</span> 

<section xmlns="http://www.w3.org/1999/xhtml" className="section context"><div className="note note note_note"><span className="note__title">Note:</span> <ul className="ul"><li className="li">Available for Chrome and Firefox.</li></ul></div><span className="ph">Katalon Studio</span> supports the capability to bypass certificate validation so that users with protected network policy can work with <span className="ph">Katalon Studio</span> as usual. The configuration here applies for Web Service tests. <p className="p">To configure certificate settings, do as follows:</p></section> 
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol steps"><li className="li step stepexpand"><span className="ph cmd">Go to <span className="ph uicontrol">Project</span> &gt; <span className="ph uicontrol">Settings</span> &gt; <span className="ph uicontrol">Network</span>.</span><div className="itemgroup info"><img className="image" width={700} src={useBaseUrl("/8f9f53a0-22b2-11ed-9930-0242fe3e4a3f/ks-841-certificate-settings.png")} alt="network settings" /></div></li><li className="li step stepexpand"><span className="ph cmd">In the <span className="ph uicontrol">Certificate Settings</span> section, choose <span className="ph uicontrol">Bypass certificate validation</span>.</span></li><li className="li step stepexpand"><span className="ph cmd">Click <span className="ph uicontrol">Apply and Close</span>.</span></li></ol> 
