---
hide_title: true
title: Import SOAP requests from WSDLs to Katalon Studio
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="id" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Import SOAP requests from WSDLs to Katalon Studio

<p xmlns="http://www.w3.org/1999/xhtml" className="p"><a className="xref j-external-link" href="https://www.w3.org/TR/wsdl/" target="_blank">WSDL</a> is used for specifying a SOAP web service's functionality. It is critical to SOAP web service testing when you can create web service requests based on a WSDL file. </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">This section shows you how to import a WSDL file into a Katalon Studio project and explore it. You can add the desired endpoint to your SOAP request, which takes precedence over the imported endpoint.</p> 

## <a id="id_1" class="anchor_top_offset"/>Import WSDLs into Katalon Studio

<p xmlns="http://www.w3.org/1999/xhtml" className="p">To import a WSDL file to your project, perform the following steps:</p> 
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol"><li className="li"><p className="p">Open an API/Web Service project.</p></li><li className="li"><p className="p">In the <strong className="ph b">Tests Explorer</strong> panel, right-click on <strong className="ph b">Object Repository</strong> &gt; <strong className="ph b">Import</strong> &gt; <strong className="ph b">From WSDL</strong>.</p><p className="p"><img className="image" width={500} src={useBaseUrl("/ce2de400-f255-11ee-a73e-0242c7a41fd4/ks-940-import-from-wsdl.png")} /></p></li><li className="li"><p className="p">In the <strong className="ph b">URL</strong> field of the <strong className="ph b">Import WSDL</strong> dialog, specify either a remote WSDL url or the path of a local WSDL file (E.g. <code className="ph codeph">http://www.dneonline.com/calculator.asmx?WSDL</code>).</p></li><li className="li"><p className="p">Click <strong className="ph b">OK</strong>. Katalon Studio loads the file and generates SOAP request objects.</p><div className="note note note_note"><span className="note__title">Note:</span> <ul className="ul"><li className="li"><p className="p">If you have created an <strong className="ph b">API/Web Service</strong> project, click the <strong className="ph b">Import WSDL</strong> icon on the main toolbar to display the <strong className="ph b">Import WSDL</strong> dialog in step 3.</p><p className="p"><img className="image" width={500} src={useBaseUrl("/6fa630d0-538d-11ed-a602-0242cfbc79b5/import-wsdl.png")} /></p></li></ul></div></li></ol> 

## <a id="id_2" class="anchor_top_offset"/>Work with imported WSDLs

<p xmlns="http://www.w3.org/1999/xhtml" className="p">A WSDL may contain multiple services. For each service, Katalon Studio:</p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">Creates a SOAP request with a specific service function.</p></li><li className="li"><p className="p">Parses its content from the specified WSDL, into their corresponding fields in the request object, such as Service Endpoint, SOAPAction, and Request message.</p></li></ul> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">For example, Katalon Studio creates multiple request objects with <code className="ph codeph">http://www.dneonline.com/calculator.asmx?WSDL</code>.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/import-soap-requests-from-wsdl/parsed-objects.png")} alt="parsed objects" /><br /><br /></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">You can manually change the content of these fields. When you override any fields of the imported request object with new values, you need to <em className="ph i">save</em> your modification(s) for it to take effect.</p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p"><strong className="ph b">Service Endpoint</strong>: This tab stores the service endpoint parsed from the WSDL file. You can specify another endpoint for the interface if you prefer. The request object receives any value given in this field.</p></li><li className="li"><p className="p"><strong className="ph b">SOAPAction</strong>: The SOAPAction is parsed in the HTTP Header of the request if the request method is SOAP.</p></li></ul> 

## <a id="id_3" class="anchor_top_offset"/>Troubleshooting

<p xmlns="http://www.w3.org/1999/xhtml" className="p">After sending the SOAP request, you might encounter a <em className="ph i">System.Web.Services.Protocols.SoapException: Server did not recognize the value of HTTP Header SOAPAction..</em> exception (1), in the response.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">This can happen if you check the <strong className="ph b">Use the endpoint and SOAPAction header parsed from WSDL</strong> (2) check box, and at the same time, specify the SOAPAction in the request header (3).</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <em className="ph i">(1),(2),(3): see the image below for more information.</em> </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/import-soap-requests-from-wsdl/exception.png")} alt="exception message" /><br /><br /></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><strong className="ph b">Proposed solution</strong> </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Remove <em className="ph i">SOAPAction</em> from the <em className="ph i">HTTP Header</em>, if you decide to use the endpoint and SOAPAction header parsed from WSDL.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">See also:</p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"> <a className="xref" href="/katalon-studio/test-objects/api-test-objects/soap-request-in-katalon-studio">SOAP Request</a>   </li></ul> 
