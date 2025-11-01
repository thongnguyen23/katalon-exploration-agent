---
hide_title: true
title: Basic Authentication in Katalon Studio
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="id_1" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/> Basic Authentication in <span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon Studio</span> 

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Basic authorization is the simplest authorization for a request, which involves sending a verified username and password with your request. With basic authentication, you need to input your credentials to authenticate the request. These credentials will be encoded into the authorization request headers.</p> 

## <a id="task-5613" class="anchor_top_offset"/>Use basic authentication in <span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon Studio</span> 

<section xmlns="http://www.w3.org/1999/xhtml" className="section context">To use basic authentication in <span className="ph">Katalon Studio</span>, do as follows:</section> 
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol steps"><li className="li step stepexpand"><span className="ph cmd">In the <span className="ph uicontrol">Authorization</span> tab of a web service request, set the <span className="ph uicontrol">Type</span> as <span className="ph uicontrol">Basic</span>.</span><div className="itemgroup info"><img className="image" src={useBaseUrl("/970873b0-22b2-11ed-9930-0242fe3e4a3f/ks-840-basic-authentication.png")} alt="basic authentication" /></div></li><li className="li step stepexpand"><span className="ph cmd">Pass in your username and password to authenticate the request, then click on <span className="ph uicontrol">Update to HTTP Header</span>. </span></li></ol> 
<section xmlns="http://www.w3.org/1999/xhtml" className="section result"><p className="p">The username and password are encoded to the <span className="ph uicontrol">Authorization</span> request of the <span className="ph uicontrol">HTTP Header</span> tab, as you can see below. </p><p className="p"><img className="image" src={useBaseUrl("/970629c0-22b2-11ed-9930-0242fe3e4a3f/ks-840-basic-authorization.png")} alt="basic authorization" /></p></section> 
