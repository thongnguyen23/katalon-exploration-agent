---
hide_title: true
title: '[Mobile] Find Image Elements'
---

# <a id="id_0" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>[Mobile] Find Image Elements

<div xmlns="http://www.w3.org/1999/xhtml" className="note important note_important"><span className="note__title">Important:</span> <ul className="ul"><li className="li"><p className="p">Katalon Studio Enterprise license.</p></li></ul></div>

## <a id="id_0__id" class="anchor_top_offset"/>Description

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Find all mobile elements that are recognized by the given image.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Keyword name: <code className="ph codeph">Mobile.findImageElements</code></p> 

## Parameters

<table xmlns="http://www.w3.org/1999/xhtml" className="table anchor_top_offset" id="id_0__f6118991-3928-40fd-a4e4-d35efc2e6f85"><caption /><colgroup><col style={{width: '20%'}} /><col style={{width: '20%'}} /><col style={{width: '20%'}} /><col style={{width: '40%'}} /></colgroup><thead className="thead"><tr className><th className="entry anchor_top_offset" id="id_0__f6118991-3928-40fd-a4e4-d35efc2e6f85__entry__1">Parameter</th><th className="entry anchor_top_offset" id="id_0__f6118991-3928-40fd-a4e4-d35efc2e6f85__entry__2">Parameter Type</th><th className="entry anchor_top_offset" id="id_0__f6118991-3928-40fd-a4e4-d35efc2e6f85__entry__3">Required</th><th className="entry anchor_top_offset" id="id_0__f6118991-3928-40fd-a4e4-d35efc2e6f85__entry__4">Description</th></tr></thead><tbody className="tbody"><tr className><td className="entry" headers="id_0__f6118991-3928-40fd-a4e4-d35efc2e6f85__entry__1 id_0__f6118991-3928-40fd-a4e4-d35efc2e6f85__entry__2 id_0__f6118991-3928-40fd-a4e4-d35efc2e6f85__entry__3 id_0__f6118991-3928-40fd-a4e4-d35efc2e6f85__entry__4 ">imageFilePath</td><td className="entry" headers="id_0__f6118991-3928-40fd-a4e4-d35efc2e6f85__entry__1 id_0__f6118991-3928-40fd-a4e4-d35efc2e6f85__entry__2 id_0__f6118991-3928-40fd-a4e4-d35efc2e6f85__entry__3 id_0__f6118991-3928-40fd-a4e4-d35efc2e6f85__entry__4 ">String</td><td className="entry" headers="id_0__f6118991-3928-40fd-a4e4-d35efc2e6f85__entry__1 id_0__f6118991-3928-40fd-a4e4-d35efc2e6f85__entry__2 id_0__f6118991-3928-40fd-a4e4-d35efc2e6f85__entry__3 id_0__f6118991-3928-40fd-a4e4-d35efc2e6f85__entry__4 ">Yes</td><td className="entry" headers="id_0__f6118991-3928-40fd-a4e4-d35efc2e6f85__entry__1 id_0__f6118991-3928-40fd-a4e4-d35efc2e6f85__entry__2 id_0__f6118991-3928-40fd-a4e4-d35efc2e6f85__entry__3 id_0__f6118991-3928-40fd-a4e4-d35efc2e6f85__entry__4 ">Absolute path of the image</td></tr><tr className><td className="entry" headers="id_0__f6118991-3928-40fd-a4e4-d35efc2e6f85__entry__1 id_0__f6118991-3928-40fd-a4e4-d35efc2e6f85__entry__2 id_0__f6118991-3928-40fd-a4e4-d35efc2e6f85__entry__3 id_0__f6118991-3928-40fd-a4e4-d35efc2e6f85__entry__4 ">flowControl</td><td className="entry" headers="id_0__f6118991-3928-40fd-a4e4-d35efc2e6f85__entry__1 id_0__f6118991-3928-40fd-a4e4-d35efc2e6f85__entry__2 id_0__f6118991-3928-40fd-a4e4-d35efc2e6f85__entry__3 id_0__f6118991-3928-40fd-a4e4-d35efc2e6f85__entry__4 ">FailureHandling</td><td className="entry" headers="id_0__f6118991-3928-40fd-a4e4-d35efc2e6f85__entry__1 id_0__f6118991-3928-40fd-a4e4-d35efc2e6f85__entry__2 id_0__f6118991-3928-40fd-a4e4-d35efc2e6f85__entry__3 id_0__f6118991-3928-40fd-a4e4-d35efc2e6f85__entry__4 ">Optional</td><td className="entry" headers="id_0__f6118991-3928-40fd-a4e4-d35efc2e6f85__entry__1 id_0__f6118991-3928-40fd-a4e4-d35efc2e6f85__entry__2 id_0__f6118991-3928-40fd-a4e4-d35efc2e6f85__entry__3 id_0__f6118991-3928-40fd-a4e4-d35efc2e6f85__entry__4 ">Specify <a className="xref" href="/katalon-studio/maintain-tests/configure-failure-handling-settings-in-katalon-studio">failure handling</a> schema to determine whether the execution should be allowed to continue or stop.</td></tr></tbody></table> 

## Returns

<p xmlns="http://www.w3.org/1999/xhtml" className="p">A list of Web elements that are recognized by the given image.</p> 

## Example

You want to find multiple UI elements on a mobile screen that match a given reference image:

<div xmlns="http://www.w3.org/1999/xhtml" className="p"><pre className="pre codeblock"><code>List&lt;WebElement&gt; elements = Mobile.findImageElements("/Users/myaccount/Desktop/image.png"){"\n"}println "Number of elements found: " + elements.size(){"\n"}</code></pre></div>
