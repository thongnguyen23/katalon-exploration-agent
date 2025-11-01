---
hide_title: true
title: Parameterize a Web Service Object
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="id_parameterize-a-web-service-object" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Parameterize a Web Service Object

## <a id="id_1" class="anchor_top_offset"/>Query Parameters

:::info notes
Only available for **RESTful** Web Service requests
:::
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Query parameters can be added to a REST request's URL to tailor and filter the response output. When you input a URL, Katalon Studio detects the query parameters (after the question mark <code className="ph codeph">?</code>) and list them in the table for better management.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/updated-parameterize-a-web-service-object/Screen-Shot-2018-09-18-at-5.04.18-PM.png")} /><br /><br /> </p> 

## <a id="id_2" class="anchor_top_offset"/>Variables and Parameterizing Request Objects

:::info notes
Available for both **RESTful** and **SOAP** Web Service requests
:::
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Katalon Studio provides the <strong className="ph b">Variables</strong> section with both manual and scripting editors. By using variables in a request object, you can handle the dynamic values of an object's properties and have more control over them. You can add a new variable and declare its properties in the <strong className="ph b">Variables</strong> tab. To call a variable in a Web Service object, use the <strong className="ph b">${'{'}variable_name{'}'}</strong> syntax as a place holder in any of the supported locations. The values of the pre-defined variables are passed to their place holders, respectively, during runtime. It is called parameterization, and the approach is the same as <a className="xref" href="/katalon-studio/test-objects/web-test-objects/manage-web-test-objects">parameterizing a WebUI object</a>.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">In the manual view of a test case, when you add a request object, the pre-defined variables are added <strong className="ph b">automatically</strong>; hence, you don't need to define them again.</p> 
      

### <a id="id_3" class="anchor_top_offset"/>For RESTful request

      
        
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Katalon Studio supports calling the declared variables in the   following places of a RESTful Web Service object.</p> 
        
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul">   <li className="li">URL</li>   <li className="li">Query Parameters</li>   <li className="li">HTTP Header</li>   <li className="li">HTTP Body</li>   <li className="li">Verification</li> </ul> 
        
<p xmlns="http://www.w3.org/1999/xhtml" className="p">The screenshot below illustrates an example of using the   '<strong className="ph b">status</strong>' variable in a URL.</p> 
        
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/updated-parameterize-a-web-service-object/Screen-Shot-2018-09-18-at-5.10.01-PM.png")} /><br /><br /> </p> 
      
    

### <a id="id_4" class="anchor_top_offset"/>For SOAP-based request

<p xmlns="http://www.w3.org/1999/xhtml" className="p">The following locations are where you can use the pre-defined variables:</p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">WSDL URL</li><li className="li">Service Endpoint</li><li className="li">HTTP Header</li><li className="li">Request Message</li><li className="li">Verification</li></ul> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Below is an example of parameterizing the domain URL in a SOAP request's service endpoint.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/parameterize-a-web-service-object/soap-endpoint.png")} /><br /><br /></p> 

## <a id="id_5" class="anchor_top_offset"/>Add test requests to a test case

<p xmlns="http://www.w3.org/1999/xhtml" className="p">There are multiple ways to add a test request object to a test   case Katalon Studio. You can call the web service requests in the   Manual View (keywords test) or Script View (test scripts) of a test   case, and verify the responses. <a className="xref" href="/katalon-studio/create-test-cases/using-web-services-in-a-test-case-in-katalon-studio">Learn     more</a>.    </p> 
