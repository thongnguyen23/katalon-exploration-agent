---
hide_title: true
title: Create REST API requests manually in Katalon Studio
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="id" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Create REST API requests manually in <span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon Studio</span> 

<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <strong className="ph b">About the author</strong> </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Marek Melocik is currently working as Test Automation Engineer   in Brno, Czech Republic. He has been working in QA industry since   2014.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Meet Marek at  <a className="xref j-external-link" href="https://www.linkedin.com/in/marek-melocik/" target="_blank">www.linkedin.com/in/marek-melocik</a> </p> 
    

## <a id="id_1" class="anchor_top_offset"/>Introduction

    
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Katalon offers a great UI support for creating REST API   requests. But if you are the advanced Katalon user, you can do it   manually and benefit from a large library of Katalon support   methods for API requests. This tutorial will be about how to create   REST API requests from manual and handle responses to make your   code robust and effective.</p> 
    
      
      

### <a id="id_2" class="anchor_top_offset"/>Requirements

      
        
<p xmlns="http://www.w3.org/1999/xhtml" className="p">You should be familiar with Katalon Studio and know the basics   of Java/Groovy.</p> 
      
    
    

## <a id="id_3" class="anchor_top_offset"/>RequestObject and ResponseObject

    
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">These are two main classes for handling API requests. I am sure   you have already figured out that the RequestObject class   represents an API request and the WSBuiltInKeywords.sendRequest   method returns ResponseObject.</p> 
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Now let's create a REST API request as an example (of course,   you can do the same with SOAP API requests). You first need to have   information for a request, including</p> 
      
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul">   <li className="li">URL</li>   <li className="li">Request method (GET, POST, PUT, DELETE, …)</li>   <li className="li">Request headers (Authorization, Content-Type, …)</li>   <li className="li">Request body (for POST request)</li>   <li className="li">REST request parameters</li> </ul> 
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Next, you create an object from RequestObject using either one   of the following ways:</p> 
      
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul">   <li className="li">New a RequestObject instance directly and set its information     using setter methods such as <em className="ph i">setRestUrl()</em> and     <em className="ph i">setRestRequestMethod()</em>.</li>   <li className="li">Use RestRequestObjectBuilder, a useful helper class offered by     Katalon Studio version 5.4 and later.</li> </ul> 
              
<pre xmlns="http://www.w3.org/1999/xhtml" className="pre codeblock"><code>import com.kms.katalon.core.testobject.ConditionType{"\n"}import com.kms.katalon.core.testobject.RequestObject{"\n"}import com.kms.katalon.core.testobject.ResponseObject{"\n"}import com.kms.katalon.core.testobject.RestRequestObjectBuilder{"\n"}import com.kms.katalon.core.testobject.TestObjectProperty{"\n"}import com.kms.katalon.core.testobject.impl.HttpTextBodyContent{"\n"}import com.kms.katalon.core.webservice.keyword.WSBuiltInKeywords as WS{"\n"} {"\n"}public class SampleRequestObject {"{"}{"\n"} {"\n"}String endpoint = "https://www.katalon.com"{"\n"}String requestMethod = "GET"{"\n"}String authHeader = "whateverYouNeedForAuthentication"{"\n"} {"\n"}TestObjectProperty header1 = new TestObjectProperty("Authorization", ConditionType.EQUALS, authHeader){"\n"}TestObjectProperty header2 = new TestObjectProperty("Content-Type", ConditionType.EQUALS, "application/json"){"\n"}TestObjectProperty header3 = new TestObjectProperty("Accept", ConditionType.EQUALS, "application/json"){"\n"}ArrayList defaultHeaders = Arrays.asList(header1, header2, header3){"\n"} {"\n"}/**{"\n"}* GET requests{"\n"}* @return{"\n"}*/{"\n"}public ResponseObject buildApiRequest1() {"{"}{"\n"}RequestObject ro = new RequestObject("objectId"){"\n"}ro.setRestUrl(endpoint){"\n"}ro.setHttpHeaderProperties(defaultHeaders){"\n"}ro.setRestRequestMethod(requestMethod){"\n"} {"\n"}ResponseObject respObj = WS.sendRequest(ro){"\n"}return respObj{"\n"}{"}"}{"\n"} {"\n"}public ResponseObject buildApiRequest2() {"{"}{"\n"}RequestObject ro = new RestRequestObjectBuilder(){"\n"}.withRestUrl(endpoint){"\n"}.withHttpHeaders(defaultHeaders){"\n"}.withRestRequestMethod(requestMethod){"\n"}.build(){"\n"} {"\n"}ResponseObject respObj = WS.sendRequest(ro){"\n"}return respObj{"\n"}{"}"}{"\n"}{"}"}{"\n"}{"\n"}</code></pre> 
            
<p xmlns="http://www.w3.org/1999/xhtml" className="p">As you can see, the source code includes two different ways to   create a request. Both of them return a ResponseObject object. When   using RestRequestObjectBuilder to create a RequestObject instance,   you call <em className="ph i">withXXX()</em> and <em className="ph i">build()</em> methods.</p> 
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">One benefit of RestRequestObjectBuilder is that it has   additional methods to allow directly setting different body types   for POST requests such as <em className="ph i">FileBodyContent</em> and   <em className="ph i">MultipartFormBodyContent</em>. It is possible also using   RequestObject, but it is more straightforward with   RestRequestObjectBuilder.</p> 
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">For further details on the methods of these classes, please   visit <a className="xref j-external-link" href="https://api-docs.katalon.com/com/kms/katalon/core/testobject/RequestObject.html" target="_blank">RequestObject</a>   and <a className="xref j-external-link" href="https://api-docs.katalon.com/com/kms/katalon/core/testobject/RestRequestObjectBuilder.html" target="_blank">RestRequestObjectBuilder</a>   on Katalon API Documentation website.</p> 
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">As a note, if you want to use HTTP headers, you can create new   TestObjectProperty instances as shown in the code snippet.</p> 
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Creating a POST request is basically the same as a GET request,   but you must specify the request body using either   <em className="ph i">setBodyContent</em> from RequestObject or   <em className="ph i">withTextBodyContent</em> from RestRequestObjectBuilder.</p> 
              
<pre xmlns="http://www.w3.org/1999/xhtml" className="pre codeblock"><code>import com.kms.katalon.core.testobject.ConditionType{"\n"}import com.kms.katalon.core.testobject.RequestObject{"\n"}import com.kms.katalon.core.testobject.ResponseObject{"\n"}import com.kms.katalon.core.testobject.RestRequestObjectBuilder{"\n"}import com.kms.katalon.core.testobject.TestObjectProperty{"\n"}import com.kms.katalon.core.testobject.impl.HttpTextBodyContent{"\n"}import com.kms.katalon.core.webservice.keyword.WSBuiltInKeywords as WS{"\n"} {"\n"}public class SampleRequestObject {"{"}{"\n"} {"\n"}String endpoint = "https://www.katalon.com"{"\n"}String requestMethod = "POST"{"\n"}String authHeader = "whateverYouNeedForAuthentication"{"\n"} {"\n"}TestObjectProperty header1 = new TestObjectProperty("Authorization", ConditionType.EQUALS, authHeader){"\n"}TestObjectProperty header2 = new TestObjectProperty("Content-Type", ConditionType.EQUALS, "application/json"){"\n"}TestObjectProperty header3 = new TestObjectProperty("Accept", ConditionType.EQUALS, "application/json"){"\n"}ArrayList defaultHeaders = Arrays.asList(header1, header2, header3){"\n"} {"\n"}String body = '{"{"}"dummyRequest":"yes"{"}"}'{"\n"} {"\n"}/**{"\n"}* POST requests{"\n"}* @return{"\n"}*/{"\n"}public ResponseObject buildPostApiRequest1() {"{"}{"\n"}RequestObject ro = new RequestObject("objectId"){"\n"}ro.setRestUrl(endpoint){"\n"}ro.setHttpHeaderProperties(defaultHeaders){"\n"}ro.setRestRequestMethod("POST"){"\n"}ro.setBodyContent(new HttpTextBodyContent(body)){"\n"} {"\n"}ResponseObject respObj = WS.sendRequest(ro){"\n"}return respObj{"\n"}{"}"}{"\n"} {"\n"}public ResponseObject buildPostApiRequest2() {"{"}{"\n"}RequestObject ro = new RestRequestObjectBuilder(){"\n"}.withRestUrl(endpoint){"\n"}.withHttpHeaders(defaultHeaders){"\n"}.withRestRequestMethod("POST"){"\n"}.withTextBodyContent(body){"\n"}.build(){"\n"} {"\n"}ResponseObject respObj = WS.sendRequest(ro){"\n"}return respObj{"\n"}{"}"}{"\n"}{"}"}{"\n"}{"\n"}</code></pre> 
            
<p xmlns="http://www.w3.org/1999/xhtml" className="p">There are many different types of request body such as file and   form data body content. Please refer to <a className="xref j-external-link" href="https://api-docs.katalon.com/com/kms/katalon/core/testobject/RestRequestObjectBuilder.html" target="_blank">RestRequestObjectBuilder     API documentation</a> to get a full list of its methods.</p> 
    
  
    

## <a id="id_4" class="anchor_top_offset"/>ResponseObject

    
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">As you can see above, we get a ResponseObject instance when   sending an API request. This object contains all information needed   for a response, including status code, response body, response   headers, waiting time and many others. Methods for handling   response objects may look like this:</p> 
              
<pre xmlns="http://www.w3.org/1999/xhtml" className="pre codeblock"><code>import com.kms.katalon.core.testobject.ResponseObject{"\n"} {"\n"}public class SampleResponseObject {"{"}{"\n"} {"\n"}public static int getStatusCode(ResponseObject resp) {"{"}{"\n"}return resp.getStatusCode(){"\n"}{"}"}{"\n"}public static String getResponseText(ResponseObject resp) {"{"}{"\n"}return resp.getResponseText(){"\n"}{"}"}{"\n"}public static long getResponseBodySize(ResponseObject resp) {"{"}{"\n"}return resp.getResponseBodySize(){"\n"}{"}"}{"\n"}public static long getResponseHeaderSize(ResponseObject resp) {"{"}{"\n"}return resp.getResponseHeaderSize(){"\n"}{"}"}{"\n"}public static long getWaitingTime(ResponseObject resp) {"{"}{"\n"}return resp.getWaitingTime(){"\n"}{"}"}{"\n"}{"}"}{"\n"}{"\n"}</code></pre> 
            
<p xmlns="http://www.w3.org/1999/xhtml" className="p">And sample usage in your test case:</p> 
              
<pre xmlns="http://www.w3.org/1999/xhtml" className="pre codeblock"><code>import com.kms.katalon.core.testobject.ResponseObject{"\n"}import com.kms.katalon.core.util.KeywordUtil{"\n"} {"\n"}import mypackage.SampleRequestObject{"\n"}import mypackage.SampleResponseObject as SampleResponseObject{"\n"} {"\n"}SampleRequestObject req = new SampleRequestObject(){"\n"} {"\n"}ResponseObject resp = req.buildApiRequest1(){"\n"} {"\n"}if(SampleResponseObject.getStatusCode(resp) != 200) {"{"}{"\n"}KeywordUtil.markFailed("Status code is not 200 as expected. It is "{"\n"}+ SampleResponseObject.getStatusCode(resp)){"\n"}{"}"}{"\n"} {"\n"}if(SampleResponseObject.getWaitingTime(resp) &gt; 5000) {"{"}{"\n"}KeywordUtil.markFailed("Your request takes more than 5000ms. Actual time is "{"\n"}+ SampleResponseObject.getWaitingTime(resp)){"\n"}{"}"}{"\n"}{"\n"}</code></pre> 
            
<p xmlns="http://www.w3.org/1999/xhtml" className="p">You may wonder why the SampleResponseObject class is needed as I   can get all information directly by calling the methods from the   response object. This wrapper may be helpful for your future   enhancements as your code is less dependent on the ResponseObject   class. If there are changes to this class, you only need to update   the wrapper class. It is up to you which approach you follow, but   both of them are correct.</p> 
    
      

### <a id="id_5" class="anchor_top_offset"/>Conclusion

<p xmlns="http://www.w3.org/1999/xhtml" className="p">This tutorial was focused on advanced usage of REST API requests   in Katalon. As I prefer writing code instead of clicking in Manual   mode, this tutorial may be helpful to similar automation engineers   as I am.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">RequestObject and ResponseObject are powerful classes, which may   help you to customize your API tests in details.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <a className="xref j-external-link" href="https://www.katalon.com/download" target="_blank">     <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/create_rest_api_requests_manually/api-testing-interview-question-1024x101.png")} alt="Rest API Request Katalon Studio" /><br /><br /></a> </p> 
