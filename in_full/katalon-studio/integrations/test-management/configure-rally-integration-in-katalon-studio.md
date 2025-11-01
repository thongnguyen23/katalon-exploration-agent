---
hide_title: true
title: Configure Rally integration in Katalon Studio
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="id" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Configure Rally integration in <span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon Studio</span> 

<p xmlns="http://www.w3.org/1999/xhtml" className="p"><span className="ph">Katalon Studio</span> allows you to link <span className="ph">Katalon Studio</span> test cases and view test execution results in Rally.</p> 

## Requirements

<div xmlns="http://www.w3.org/1999/xhtml" className="p"><ul className="ul"><li className="li">An active <span className="ph">Katalon Studio Enterprise</span> license.</li></ul></div>

## <a id="task-4114" class="anchor_top_offset"/>Enable Rally integration in  <span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon Studio</span> 

<section xmlns="http://www.w3.org/1999/xhtml" className="section context">To enable Rally integration in <span className="ph">Katalon Studio</span>, do as follows:</section> 
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol steps"><li className="li step stepexpand"><span className="ph cmd">Install Rally integration plugin. To do so, follow these steps:</span><ol type="a" className="ol substeps"><li className="li substep"><span className="ph cmd">Download and install the <span className="ph uicontrol">Rally Integration</span>  plugin. You can go to the Katalon Store here: <a className="xref j-external-link" href="https://store.katalon.com/product/125/Rally-Integration" target="_blank">Rally Integration</a>.</span></li><li className="li substep"><span className="ph cmd">To activate the installed plugin, open Katalon Studio and navigate to Account Settings. Click <span className="ph uicontrol">Reload Plugin</span>.</span></li></ol></li><li className="li step stepexpand"><span className="ph cmd">Go to <span className="ph uicontrol">Project Settings</span> &gt; <span className="ph uicontrol">Plugins</span> &gt; <span className="ph uicontrol">Rally</span>. Input the following information:</span><div className="itemgroup info"><ul className="ul"><li className="li"><span className="ph uicontrol">Rally URL</span>: <code className="ph codeph">https://rally1.rallydev.com/</code>.</li><li className="li"><span className="ph uicontrol">API Key</span>: the API key in Rally. To generate an API key in Rally, you can refer to the Broadcom documentation: <a className="xref j-external-link" href="https://knowledge.broadcom.com/external/article/10814/rally-how-to-create-an-api-key.html" target="_blank">Create an API key</a>.</li></ul></div><div className="itemgroup stepxmp"><img className="image" src={useBaseUrl("/91cc6cd0-22b2-11ed-9930-0242fe3e4a3f/KS-Enable-Rally-integration-in-Studio.png")} alt="Enable Rally integration in Studio" /></div><div className="itemgroup stepresult">Once connected successfully, Katalon retrieves your available workspaces from Rally. Choose the Rally workspace you want to work on.</div></li><li className="li step stepexpand"><span className="ph cmd">Click <span className="ph uicontrol">Apply and Close</span>.</span></li></ol> 
<section xmlns="http://www.w3.org/1999/xhtml" className="section result">You have successfully enabled Rally integration in <span className="ph">Katalon Studio</span>.</section> 

## <a id="task-9908" class="anchor_top_offset"/>Map test cases between <span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon Studio</span>  and Rally

<section xmlns="http://www.w3.org/1999/xhtml" className="section context"><span className="ph">Katalon Studio</span> provides an easy way to map a Katalon test case to an existing Rally test case. Follow these steps:</section> 
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol steps"><li className="li step stepexpand"><span className="ph cmd">To retrieve the test case ID, open your project in Rally, then go to <span className="ph uicontrol">Quality</span> &gt; <span className="ph uicontrol">Test Cases</span>. Here you can see the list of test cases and their IDs.</span><div className="itemgroup stepxmp"><img className="image" src={useBaseUrl("/91ca22e0-22b2-11ed-9930-0242fe3e4a3f/KS-Test-case-ID-in-Rally.png")} alt="View Rally test cases" /></div></li><li className="li step stepexpand"><span className="ph cmd">In <span className="ph">Katalon Studio</span>, open the test case you wish to link to Rally. Switch to the  <span className="ph uicontrol">Integration</span> tab, and specify the respective test case ID in Rally. </span><div className="itemgroup stepxmp"><img className="image" src={useBaseUrl("/91c95f90-22b2-11ed-9930-0242fe3e4a3f/KS-Map-Studio-Rally-test-cases.png")} alt="Map Rally and Studio test cases" /></div></li></ol> 
<section xmlns="http://www.w3.org/1999/xhtml" className="section result">You have successfully mapped test cases between <span className="ph">Katalon Studio</span> and Rally.</section> 
