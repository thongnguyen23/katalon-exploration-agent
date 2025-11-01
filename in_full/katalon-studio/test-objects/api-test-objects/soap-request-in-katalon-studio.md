---
hide_title: true
title: SOAP Request in Katalon Studio
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="id_soap" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>SOAP Request in <span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon Studio</span> 

<p xmlns="http://www.w3.org/1999/xhtml" className="p">When sending a SOAP Request in <span className="ph">Katalon Studio</span>, you can receive a   response from the API server for examination and troubleshooting.   This section includes a tutorial of how to create a SOAP request   object and an introduction to each field of a request service in   its opened editor.</p> 

## <a id="id_1" class="anchor_top_offset"/>Creating a SOAP-based Request

<ol xmlns="http://www.w3.org/1999/xhtml" className="ol"><li className="li">From the main menu, select <strong className="ph b">File &gt; New &gt; Web Service Request</strong>.</li><li className="li"><p className="p">In the <strong className="ph b">New Web Service Request</strong> dialog, select <strong className="ph b">SOAP</strong> in the <strong className="ph b">Request Type</strong> list and click <strong className="ph b">OK</strong> to create a new SOAP object.</p><p className="p"><img className="image" width={500} src={useBaseUrl("/96fab810-22b2-11ed-9930-0242fe3e4a3f/ks-840-new-soap-request.png")} alt="new SOAP request" /></p></li><li className="li"><p className="p">A <strong className="ph b">New</strong> request object is created under the <strong className="ph b">Object Repository</strong> of Katalon Studio.</p></li></ol> 

## <a id="id_2" class="anchor_top_offset"/>Adding SOAP Request Details

<p xmlns="http://www.w3.org/1999/xhtml" className="p">After you've created a request successfully, double-click on the request to open its editor for adding details. In the opened editor of the <strong className="ph b">New Request</strong> object, you can see all the required information of a request object.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" width={700} src={useBaseUrl("/96f97f90-22b2-11ed-9930-0242fe3e4a3f/ks-840-ws-editor.png")} alt="web service object editor" /></p> 
      

### <a id="id_3" class="anchor_top_offset"/>Request Method

      
        
<p xmlns="http://www.w3.org/1999/xhtml" className="p">The request method indicates the expected action to be executed   on the specified resource. Katalon Studio supports the following   SOAP methods: SOAP, SOAP 1.2, POST, GET. By default, Katalon   selects SOAP as a method for a new SOAP request.</p> 
        
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/soap-request/method-list.png")} /><br /><br /> </p> 
      
    
      

### <a id="id_4" class="anchor_top_offset"/>WSDL URL

      
        
<p xmlns="http://www.w3.org/1999/xhtml" className="p">This field is for a WSDL path from which Katalon Studio imports   the content to this SOAP request.</p> 
        
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/soap-request/wsdl-url.png")} /><br /><br /> </p> 
      
    
      

### <a id="id_5" class="anchor_top_offset"/>Service Function

      
        
<p xmlns="http://www.w3.org/1999/xhtml" className="p">The function that you want to use in this SOAP request. When   clicking <strong className="ph b">Load Service Function</strong>, you can retrieve a   list of service functions available from the WSDL file.</p> 
        
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/soap-request/method.png")} /><br /><br /> </p> 
        
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Each Service Function carries its own content, including Service   Endpoint, SOAPAction Header and Request message.</p> 
        
<p xmlns="http://www.w3.org/1999/xhtml" className="p">In <strong className="ph b">Service Endpoint</strong>, You can specify another   URL indicating the desired service endpoint of this request.</p> 
        
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/soap-request/service-endpoint.png")} /><br /><br /> </p> 
      
    

### <a id="id_6" class="anchor_top_offset"/>Request Authentication

<p xmlns="http://www.w3.org/1999/xhtml" className="p">This part is used for authenticating and authorizing the request, which means to verify if the client is permitted to send the request and to perform the endpoint operation.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">For more details on using each type of auth, please see:</p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><a className="xref" href="/katalon-studio/test-objects/api-test-objects/authorization/aws-signature-authentication-in-katalon-studio">AWS Signature</a></li><li className="li"><a className="xref" href="/katalon-studio/test-objects/api-test-objects/authorization/bearer-authentication-in-katalon-studio">Bearer</a></li><li className="li"><a className="xref" href="/katalon-studio/test-objects/api-test-objects/authorization/basic-authentication-in-katalon-studio">Basic</a></li><li className="li"><p className="p"><a className="xref" href="/katalon-studio/test-objects/api-test-objects/authorization/digest-authentication-in-katalon-studio">Digest</a></p></li><li className="li"><a className="xref" href="/katalon-studio/test-objects/api-test-objects/authorization/authorization-oauth-1.0-in-katalon-studio">OAuth 1.0</a></li><li className="li"><a className="xref" href="/katalon-studio/test-objects/api-test-objects/authorization/authorization-oauth-2.0-in-katalon-studio">OAuth 2.0</a></li><li className="li"><a className="xref" href="/katalon-studio/test-objects/api-test-objects/authorization/ntlm-authentication-in-katalon-studio">NTLM</a></li></ul> 

### <a id="id_7" class="anchor_top_offset"/>Request Headers

<p xmlns="http://www.w3.org/1999/xhtml" className="p">The header information needs sending along with this SOAP   request. You can select headers from the list of suggested options   (by double-clicking on the <strong className="ph b">Name</strong> cell) or enter   another header of your interest. For more details, refer to Mozilla documentation: <a className="xref j-external-link" href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers" target="_blank">Supported     HTTP Headers</a>.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/soap-request/header.png")} /><br /><br /> </p> 
      

### <a id="id_8" class="anchor_top_offset"/>Request Message

      
        
<p xmlns="http://www.w3.org/1999/xhtml" className="p">The information that you want to transmit in this SOAP request.   You can get it after clicking <strong className="ph b">Load New Content</strong> of   the selected service function.</p> 
        
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/soap-request/request-message.png")} /><br /><br /> </p> 
      
    
    

## <a id="id_9" class="anchor_top_offset"/>Response

    
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">After sending the service request, Katalon Studio retrieves a   message from the server and displays it in the   <strong className="ph b">Response</strong> view of the request. A service response   comprises Status, Elapsed time, and Size fields; Body section,   Header, and Verification Log.</p> 
      
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul">   <li className="li">     <strong className="ph b">Status</strong>: The status code of the response</li>   <li className="li">     <strong className="ph b">Elapsed</strong>: The total time that starts from the     request is sent until Katalon Studio receives the last byte of the     response</li>   <li className="li">     <strong className="ph b">Size</strong>: Size of the response package</li> </ul> 
    
              

### <a id="id_10" class="anchor_top_offset"/>Response Body

<p xmlns="http://www.w3.org/1999/xhtml" className="p">There are 2 viewing formats: <strong className="ph b">pretty</strong> and   <strong className="ph b">raw</strong>. For example, the SOAP's response to   <code className="ph codeph">http://www.dneonline.com/calculator.asmx?WSDL</code> is shown   below.</p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">     <p className="p">Pretty format</p>     <p className="p">       <img className="image" src={useBaseUrl("https://tw-cdn.katalon.com/katalon-studio/test-objects/api-test-objects/pretty_response_body.png")} width={500} /><br /><br />     </p>   </li><li className="li">     <p className="p">Raw Format</p>     <p className="p">       <img className="image" src={useBaseUrl("https://tw-cdn.katalon.com/katalon-studio/test-objects/api-test-objects/raw_response_body_soap_request.png")} width={500} /><br /><br />     </p>   </li></ul> 
      

### <a id="id_11" class="anchor_top_offset"/>Response Header

      
        
<p xmlns="http://www.w3.org/1999/xhtml" className="p">The response's header is displayed in   the <strong className="ph b">Header</strong> tab and can be viewed in three formats: <strong className="ph b">pretty</strong>, <strong className="ph b">raw</strong>. For example, the SOAP's response to   <code className="ph codeph">http://www.dneonline.com/calculator.asmx?WSDL</code> is shown   below.</p>
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">     <p className="p">Pretty format</p>     <p className="p">       <img src="https://tw-cdn.katalon.com/katalon-studio/test-objects/api-test-objects/soap_pretty_response_header.png" alt="Pretty response in SOAP" width="500"/><br /><br />     </p>   </li><li className="li">     <p className="p">Raw Format</p>     <p className="p">       <img src="https://tw-cdn.katalon.com/katalon-studio/test-objects/api-test-objects/soap_raw_response_header.png" alt="Raw response header in SOAP" width="500"/><br /><br />     </p>   </li></ul> 
    

### <a id="id_12" class="anchor_top_offset"/>Verification Log

<p xmlns="http://www.w3.org/1999/xhtml" className="p">This tab displays the verification results after the request is   tested and verified.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <strong className="ph b">See also:</strong> </p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">     <a className="xref" href="/katalon-studio/test-objects/api-test-objects/rest-request/parameterize-a-web-service-object">Parameterize a       Web Service Object</a>   </li><li className="li">     <a className="xref" href="/katalon-studio/test-objects/api-test-objects/verification-snippets-in-katalon-studio">Verification       Snippets</a>   </li><li className="li">     <a className="xref" href="/katalon-studio/create-test-cases/using-web-services-in-a-test-case-in-katalon-studio">Using       Web Services in a Test Case</a>   </li></ul> 
