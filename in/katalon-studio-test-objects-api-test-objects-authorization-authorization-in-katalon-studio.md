---
hide_title: true
title: Authorization in Katalon Studio
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="id" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Authorization in <span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon Studio</span> 

<p xmlns="http://www.w3.org/1999/xhtml" className="p">APIs use authorization to make sure that client requests access data securely. Authorization involves authenticating and confirming that the sender of a request have the permission to access or manipulate the relevant data.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">You can add your authorization information the <span className="ph uicontrol">Authorization</span> tab of a <span className="ph uicontrol">Web Service Request</span>.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" width={700} src={useBaseUrl("/b5683067-c205-4ba4-aed1-d03e63713736/ks-970-authorization-type.png")} alt="Authorization tab" /></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">The following types of authorizations are supported in Katalon Studio:</p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><a className="xref" href="/katalon-studio/test-objects/api-test-objects/authorization/aws-signature-authentication-in-katalon-studio">AWS Signature</a></li><li className="li"><a className="xref" href="/katalon-studio/test-objects/api-test-objects/authorization/bearer-authentication-in-katalon-studio#task-6669">Bearer</a></li><li className="li"><a className="xref" href="/katalon-studio/test-objects/api-test-objects/authorization/basic-authentication-in-katalon-studio">Basic</a></li><li className="li"><a className="xref" href="/katalon-studio/test-objects/api-test-objects/authorization/digest-authentication-in-katalon-studio">Digest</a></li><li className="li"><a className="xref" href="/katalon-studio/test-objects/api-test-objects/authorization/authorization-oauth-1.0-in-katalon-studio">OAuth 1.0</a></li><li className="li"><a className="xref" href="/katalon-studio/test-objects/api-test-objects/authorization/authorization-oauth-2.0-in-katalon-studio">OAuth 2.0</a></li><li className="li"><p className="p"><a className="xref" href="/katalon-studio/test-objects/api-test-objects/authorization/ntlm-authentication-in-katalon-studio">NTLM</a></p></li></ul> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">To use current authentication information, make sure that you click on <span className="ph uicontrol">Update to HTTP Header</span>. Katalon Studio appends these information to the <span className="ph uicontrol">HTTP Header</span> of the web service request.</p> 
