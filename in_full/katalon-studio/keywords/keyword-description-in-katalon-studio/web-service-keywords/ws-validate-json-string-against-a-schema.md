---
hide_title: true
title: '[WS] Validate JSON string against a schema'
---

# <a id="topic-3477" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>[WS] Validate JSON string against a schema

## Description

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Validate a JSON response body, request body, or string against a JSON schema. The JSON schema input can be a JSON string, URL, or file path.</p> 
            
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Keyword name: <code className="ph codeph">validateJsonAgainstSchema</code></p>   

## Parameters

Validate a **JSON Object** against a JSON Schema:

| **Parameter** | **Parameter Type** | **Required** | **Description** |
| --- | --- | --- | --- |
| jsonObject | String | Yes | Specify the JSON object that needs to be validated. |
| jsonSchema | String | Yes | Specify the JSON schema used to validate the JSON object. |
| flowControl | FailureHandling | Optional | Specify [failure handling](/katalon-studio/maintain-tests/configure-failure-handling-settings-in-katalon-studio) schema to determine whether the execution should be allowed to continue or stop. |

Validate a **Response** against a JSON Schema:

| **Parameter** | **Parameter Type** | **Required** | **Description** |
| --- | --- | --- | --- |
| response | ResponseObject | Yes | Specify the response object that needs to be validated. |
| jsonSchema | String | Yes | Specify the JSON schema used to validate the response object. |
| flowControl | FailureHandling | Optional | Specify [failure handling](/katalon-studio/maintain-tests/configure-failure-handling-settings-in-katalon-studio) schema to determine whether the execution should be allowed to continue or stop. |        

## Returns

                        
<table xmlns="http://www.w3.org/1999/xhtml" className="table anchor_top_offset" id="topic-3477__fbb40395-f1f3-495b-9fef-6bf9363ac0f9"><caption /><colgroup><col style={{width: '33.33333333333333%'}} /><col style={{width: '66.66666666666666%'}} /></colgroup><thead className="thead"><tr className><th className="entry anchor_top_offset" id="topic-3477__fbb40395-f1f3-495b-9fef-6bf9363ac0f9__entry__1">Parameter Type</th><th className="entry anchor_top_offset" id="topic-3477__fbb40395-f1f3-495b-9fef-6bf9363ac0f9__entry__2">Description</th></tr></thead><tbody className="tbody"><tr className><td className="entry" headers="topic-3477__fbb40395-f1f3-495b-9fef-6bf9363ac0f9__entry__1 topic-3477__fbb40395-f1f3-495b-9fef-6bf9363ac0f9__entry__2 ">Boolean</td><td className="entry" headers="topic-3477__fbb40395-f1f3-495b-9fef-6bf9363ac0f9__entry__1 topic-3477__fbb40395-f1f3-495b-9fef-6bf9363ac0f9__entry__2 ">         <ul className="ul"><li className="li"><code className="ph codeph">true</code>: If the response passes the validation.</li><li className="li">             <p className="p"><code className="ph codeph">false</code>: If the response does not pass the validation.</p>           </li></ul>       </td></tr></tbody></table> 

## Example

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">     <div className="p">Validate a JSON Object against a schema: <pre className="pre codeblock"><code>import com.kms.katalon.core.webservice.keyword.WSBuiltInKeywords as WS{"\n"}{"\n"}String jsonPass ={"\n"}"""{"\n"}{"{"}{"\n"}{"  "}"\$id": "https://example.com/person.schema.json",{"\n"}{"  "}"\$schema": "https://json-schema.org/draft/2020-12/schema",{"\n"}{"  "}"title": "Person",{"\n"}{"  "}"type": "object",{"\n"}{"  "}"properties": {"{"}{"\n"}{"    "}"firstName": {"{"}{"\n"}{"      "}"type": "string",{"\n"}{"      "}"description": "The person's first name."{"\n"}{"    "}{"}"},{"\n"}{"    "}"lastName": {"{"}{"\n"}{"      "}"type": "string",{"\n"}{"      "}"description": "The person's last name."{"\n"}{"    "}{"}"},{"\n"}{"    "}"age": {"{"}{"\n"}{"      "}"description": "Age in years which must be equal to or greater than zero.",{"\n"}{"      "}"type": "integer",{"\n"}{"      "}"minimum": 0{"\n"}{"    "}{"}"}{"\n"}{"  "}{"}"}{"\n"}{"}"}{"\n"}"""{"\n"}{"\n"}String jsonObject = {"\n"}"""{"\n"}{"{"}{"\n"}{"  "}"firstName": "White",{"\n"}{"  "}"lastName": "Walter",{"\n"}{"  "}"age": 52{"\n"}{"}"}{"\n"}{"\n"}"""{"\n"}{"\n"}boolean successful = WS.validateJsonAgainstSchema(jsonObject,jsonPass)</code></pre>     </div>   </li><li className="li">     <div className="p">Validate a Response against a schema: <pre className="pre codeblock"><code>import com.kms.katalon.core.testobject.ResponseObject{"\n"}import com.kms.katalon.core.webservice.keyword.WSBuiltInKeywords as WS{"\n"}import com.kms.katalon.core.webservice.verification.WSResponseManager{"\n"}{"\n"}ResponseObject response = WSResponseManager.getInstance().getCurrentResponse(){"\n"}{"\n"}String jsonPass ={"\n"}"""{"\n"}{"{"}{"\n"}{"  "}"\$id": "https://example.com/person.schema.json",{"\n"}{"  "}"\$schema": "https://json-schema.org/draft/2020-12/schema",{"\n"}{"  "}"title": "Person",{"\n"}{"  "}"type": "object",{"\n"}{"  "}"properties": {"{"}{"\n"}{"    "}"firstName": {"{"}{"\n"}{"      "}"type": "string",{"\n"}{"      "}"description": "The person's first name."{"\n"}{"    "}{"}"},{"\n"}{"    "}"lastName": {"{"}{"\n"}{"      "}"type": "string",{"\n"}{"      "}"description": "The person's last name."{"\n"}{"    "}{"}"},{"\n"}{"    "}"age": {"{"}{"\n"}{"      "}"description": "Age in years which must be equal to or greater than zero.",{"\n"}{"      "}"type": "integer",{"\n"}{"      "}"minimum": 0{"\n"}{"    "}{"}"}{"\n"}{"  "}{"}"}{"\n"}{"}"}{"\n"}"""{"\n"}{"\n"}boolean successful = WS.validateJsonAgainstSchema(response,jsonPass)</code></pre></div>   </li></ul> 
        
