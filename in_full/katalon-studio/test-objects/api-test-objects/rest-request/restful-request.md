---
hide_title: true
title: RESTful Request
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="id" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>RESTful Request

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Katalon Studio supports sending RESTful requests with parameters, body data, and authorization details needed. When sending a request, you can receive a response from the API server for examination and troubleshooting.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">This page guides you on how to create and configure a RESTful request in <span className="ph">Katalon Studio</span>.</p> 

## <a id="task-3342" class="anchor_top_offset"/>Create a RESTful request

<ol xmlns="http://www.w3.org/1999/xhtml" className="ol steps"><li className="li step stepexpand"><span className="ph cmd">In the <span className="ph uicontrol">Tests Explorer</span> panel, select <span className="ph uicontrol">Object Repository</span> &gt; <span className="ph uicontrol">New</span> &gt; <span className="ph uicontrol">Web Service         Request</span>.</span></li><li className="li step stepexpand"><span className="ph cmd">In the <span className="ph uicontrol">New Web Service         Request</span> dialog, give the request a name, select <span className="ph uicontrol">RESTful</span> for the <span className="ph uicontrol">Request Type</span>; and set the request URL.</span><div className="itemgroup info"><img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/restful-web-services/KS-RESTFUL-Create-a-new-object.png")} width={500} alt="Create a new web service request" /><br /><br /></div></li><li className="li step stepexpand"><span className="ph cmd">Click OK.</span></li></ol> 
<section xmlns="http://www.w3.org/1999/xhtml" className="section result">You have a newly created RESTful request. Go to the next section to learn about the components of a RESTful request.</section> 

## <a id="id_2" class="anchor_top_offset"/>Configure RESTful request

<p xmlns="http://www.w3.org/1999/xhtml" className="p">After you have created a request, double-click on the request to open it in the editor view.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" width={600} src={useBaseUrl("/64c5cf6d-0056-4da7-82d3-b526c9b412f7/restful-request-editor.png")} /></p> 

### Request methods and URL

<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" width={600} src={useBaseUrl("/c1ee4c29-e02c-4480-bcbc-344fca5442a7/ks-request-method-url.png")} /></p> 
<div xmlns="http://www.w3.org/1999/xhtml" className="sectiondiv"><strong className="ph b">Request method</strong><p className="p">The request method indicates the expected action to be executed on the specified resource. Katalon Studio supports the following RESTful request methods: GET, POST, PUT, DELETE, PATCH, HEAD, CONNECT, OPTIONS, and TRACE. The method needs to match the API endpoint to be a valid request. You can refer to this guide for more details on each method: <a className="xref j-external-link" href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods" target="_blank">HTTP Methods</a>.</p><p className="p">By default, a newly created RESTful request uses the GET method. Click the drop-down menu next to GET to select a different method.</p><p className="p">For KSE users, you can add custom method to the project by clicking <span className="ph uicontrol">Customize API methods</span> to open the <span className="ph uicontrol">Project Settings</span> dialog, then click <span className="ph uicontrol">Add</span>.</p><p className="p"><img className="image" width={650} src={useBaseUrl("/4a91ec91-fd46-4e37-81c0-7165e61a4491/ks-custom-api-method.png")} /></p></div>
<div xmlns="http://www.w3.org/1999/xhtml" className="sectiondiv"><strong className="ph b">Request URL</strong><p className="p">You need to specify a URL indicating the service endpoint of each request. Request URL tells the web server which API is utilized under test. Any mismatch between method and URL leads to an invalid request exception at runtime or a wrong data response. For example, the URL <code className="ph codeph">https://petstore.swagger.io/v2/pet/findByStatus?status=${'{'}status{'}'}</code> is registered for the RESTful request we've created. In URLs, you can use variables to update the <span className="ph uicontrol">Query Parameters</span> table flexibly.</p></div>

### Query parameters

<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" width={650} src={useBaseUrl("/c46f5b57-eecd-41de-a7a1-0f3482a4013a/restful-request-query-param.png")} /></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Query parameters are parameters added to the end of the URL to tailor and filter the response output. When you input a URL, Katalon Studio detects the query parameters after the question mark <code className="ph codeph">?</code> and list them in the table. You can also manually <span className="ph uicontrol">+ Add</span> the parameters in the table and the URL is updated accordingly. </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Katalon Studio encodes special characters in query parameters before sending requests.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">To learn more about <span className="ph uicontrol">Query Parameters</span>, see: <a className="xref" href="/katalon-studio/test-objects/api-test-objects/rest-request/parameterize-a-web-service-object">Parameterize a Web Service Object</a>.</p> 

### Authorization tab

<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" width={650} src={useBaseUrl("/9131a938-fe20-43a0-a719-e5be2d46d461/ks-request-authorization.png")} /></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">By default, a newly created RESTful request is set with <span className="ph uicontrol">No Authorization</span>. You can select from the supported authorization types to verify if the client is permitted to send the request, and to perform the endpoint operation.</p> 
<div xmlns="http://www.w3.org/1999/xhtml" className="p">For more details on using each type of authorization, see:<ul className="ul"><li className="li"><a className="xref" href="/katalon-studio/test-objects/api-test-objects/authorization/bearer-authentication-in-katalon-studio#task-6669">Bearer</a></li><li className="li"><a className="xref" href="/katalon-studio/test-objects/api-test-objects/authorization/basic-authentication-in-katalon-studio">Basic</a></li><li className="li"><a className="xref" href="/katalon-studio/test-objects/api-test-objects/authorization/authorization-oauth-1.0-in-katalon-studio">OAuth 1.0</a></li><li className="li"><a className="xref" href="/katalon-studio/test-objects/api-test-objects/authorization/authorization-oauth-2.0-in-katalon-studio">OAuth 2.0</a></li><li className="li"><a className="xref" href="/katalon-studio/test-objects/api-test-objects/authorization/ntlm-authentication-in-katalon-studio">NTLM</a></li></ul></div>

### Request Header tab

<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" width={650} src={useBaseUrl("/4d95700d-06f1-4ab6-869d-f2ae93c98585/ks-request-header.png")} /></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">You can configure the header information needed for sending the RESTful request object. By default, the <span className="ph uicontrol">Content-Type</span> value is generated automatically based on the HTTP Body. You can also select headers from the list of suggested options (by double-clicking on the <span className="ph uicontrol">Name</span> cell) or enter another header. Refer to <a className="xref j-external-link" href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers" target="_blank">Supported HTTP Headers</a> for more details.</p> 

### Request Body tab

<p xmlns="http://www.w3.org/1999/xhtml" className="p">By default, Katalon Studio selects <span className="ph uicontrol">none</span> for HTTP body. If you need to send a body with your request, choose among these data types: text, x-www-form-urlencoded, form-data, file, and GraphQL.</p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p"><span className="ph uicontrol">Text</span>: With this type, the supported formats include Text, JSON, XML, HTML, and Javascript. You can check <span className="ph uicontrol">Auto update Content Type</span> to automatically generate a HTTP header.</p><p className="p"><img className="image" width={650} src={useBaseUrl("/5b02d212-c47b-4542-a5e6-41ded17a6c82/request-body-text.png")} /></p></li><li className="li"><p className="p"><span className="ph uicontrol">x-www-form-urlencoded</span>: Enter your key-value pairs accordingly to the <span className="ph uicontrol">Name</span> and <span className="ph uicontrol">Value</span> columns to encode with the request before sending.</p></li><li className="li"><p className="p"><span className="ph uicontrol">Form-data</span>: This data type allows you to send data to APIs as <code className="ph codeph">multipart/form-data</code>, and attach files to your request. You can specify the content type in the form-data body.<img className="image" width={650} src={useBaseUrl("/1459d610-d0df-4682-9e6b-99b534f46e94/request-body-form-data.png")} /></p></li><li className="li"><p className="p"><span className="ph uicontrol">file</span>: Select the file you want to send with the request.</p></li><li className="li"><p className="p"><span className="ph uicontrol">GraphQL</span>: Enter your code in the <span className="ph uicontrol">Query</span> pane and any variables in the <span className="ph uicontrol">Query Variables</span> pane.</p></li></ul> 

### Validation tab

<p xmlns="http://www.w3.org/1999/xhtml" className="p">You can validate against schemas to assert whether a request or a response follows the associated schema definition and make sure that APIs are working as expected. For more details, refer to <a className="xref" href="/katalon-studio/test-objects/api-test-objects/schema-compliance-testing-in-katalon-studio#id_2">Validate against a schema in the web service request</a>.</p> 

### Verifications tab

<p xmlns="http://www.w3.org/1999/xhtml" className="p">You can write verification scripts directly in the <span className="ph uicontrol">Verification</span> tab of the web service object. To learn more about the verification snippets, you can refer to this document: <a className="xref" href="/katalon-studio/test-objects/api-test-objects/verification-snippets-in-katalon-studio#id_1">Verification snippets</a>.</p> 

### Variables tab

<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" width={650} src={useBaseUrl("/37b87176-5ae9-4ae9-9f27-1894bccf8703/ks-restful-request-variables.png")} /></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">To use variables in a request, you define them in the <span className="ph uicontrol">Variables</span> tab or the <span className="ph uicontrol">Variables Editor</span> tab.</p> 

### Configuration tab

<p xmlns="http://www.w3.org/1999/xhtml" className="p">The <span className="ph uicontrol">Follow redirects</span> option allows you to automatically make a new request when the server responds with a 3xx status. You can disable this option to prevent automatically redirecting such requests that return a 3xx series response, you can examine and manage the redirection manually. </p> 

## <a id="id_9" class="anchor_top_offset"/>Response

<p xmlns="http://www.w3.org/1999/xhtml" className="p">After you send a request, Katalon Studio supports displaying its response in the <span className="ph uicontrol">Response</span> tab. A service response comprises Status, Elapsed time, and Size fields; Body section, Header, and Verification Log.</p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"> <span className="ph uicontrol">Status</span>: The status code of the response</li><li className="li"> <span className="ph uicontrol">Elapsed</span>: The total time that starts from the request is sent until Katalon Studio receives the last byte of the response</li><li className="li"> <span className="ph uicontrol">Size</span>: Size of the response package</li></ul> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" width="500" src="https://tw-cdn.katalon.com/katalon-studio/test-objects/api-test-objects/pretty_response_restful.png" alt="response tab in RESTful"/><br /><br /></p> 

### Response body

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Katalon can read a service response in JSON, XML, HTML, and JavaScript. The response body can be displayed in three formats: pretty, raw, and preview.</p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p"><span className="ph uicontrol">pretty</span>: Response is displayed in a pretty format which is easier to read <img className="image" width="500" src="https://tw-cdn.katalon.com/katalon-studio/test-objects/api-test-objects/pretty_response_restful.png" alt="pretty mode response in RESTful" /><br /><br /></p></li><li className="li"><p className="p"><span className="ph uicontrol">raw</span>: Response is displayed in the raw text without any format <img className="image" width="500" src="https://tw-cdn.katalon.com/katalon-studio/test-objects/api-test-objects/raw_response_restful.png" alt="raw mode  response in RESTful" /><br /><br /></p></li><li className="li"><p className="p"><span className="ph uicontrol">preview</span>: Response is displayed as visualized (for example, if a Response is from loading a specific webpage, it is displayed as the screenshot below) <img className="image" src="https://tw-cdn.katalon.com/katalon-studio/test-objects/api-test-objects/preview_response_body_restful.png" alt="Preview mode  response in RESTful" /><br /><br /></p></li></ul> 

### Response header

<p xmlns="http://www.w3.org/1999/xhtml" className="p">The response's header is displayed in the <span className="ph uicontrol">Header</span> tab and can be viewed in two formats: pretty and raw.</p>
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p"><span className="ph uicontrol">pretty</span>: The response is displayed in the Pretty format, which presents the data in an easy-to-read, table-like view. <img src="https://tw-cdn.katalon.com/katalon-studio/test-objects/api-test-objects/restful_pretty_response_header.png" alt="Pretty response header in API testing" width="500"/><br /><br /></p></li><li className="li"><p className="p"><span className="ph uicontrol">raw</span>: Response is displayed in the raw text without any format <img src="https://tw-cdn.katalon.com/katalon-studio/test-objects/api-test-objects/restful_raw_response_header.png" alt="raw response header in API testing" width="500"/><br /><br /></p></li></ul> 

### Verification log

<p xmlns="http://www.w3.org/1999/xhtml" className="p">This tab displays the verification results after the request is tested and verified.</p> 
