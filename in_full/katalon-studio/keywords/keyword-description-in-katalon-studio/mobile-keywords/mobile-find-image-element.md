---
hide_title: true
title: '[Mobile] Find Image Element'
---

# <a id="id_0" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>[Mobile] Find Image Element

<div xmlns="http://www.w3.org/1999/xhtml" className="p"><div className="note important note_important"><span className="note__title">Important:</span> <ul className="ul"><li className="li"><p className="p">Katalon Studio Enterprise license.</p></li></ul></div></div>

## Description

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Find the mobile element that is recognized by the given image.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Keyword name: <code className="ph codeph">Mobile.findImageElement</code></p> 

## Parameters

<table xmlns="http://www.w3.org/1999/xhtml" className="table anchor_top_offset" id="id_0__4b4f2e18-e108-4264-a35c-ce736e71cf9a"><caption /><colgroup><col style={{width: '20%'}} /><col style={{width: '20%'}} /><col style={{width: '20%'}} /><col style={{width: '40%'}} /></colgroup><thead className="thead"><tr className><th className="entry anchor_top_offset" id="id_0__4b4f2e18-e108-4264-a35c-ce736e71cf9a__entry__1">Parameter</th><th className="entry anchor_top_offset" id="id_0__4b4f2e18-e108-4264-a35c-ce736e71cf9a__entry__2">Parameter Type</th><th className="entry anchor_top_offset" id="id_0__4b4f2e18-e108-4264-a35c-ce736e71cf9a__entry__3">Required</th><th className="entry anchor_top_offset" id="id_0__4b4f2e18-e108-4264-a35c-ce736e71cf9a__entry__4">Description</th></tr></thead><tbody className="tbody"><tr className><td className="entry" headers="id_0__4b4f2e18-e108-4264-a35c-ce736e71cf9a__entry__1 id_0__4b4f2e18-e108-4264-a35c-ce736e71cf9a__entry__2 id_0__4b4f2e18-e108-4264-a35c-ce736e71cf9a__entry__3 id_0__4b4f2e18-e108-4264-a35c-ce736e71cf9a__entry__4 ">imageFilePath</td><td className="entry" headers="id_0__4b4f2e18-e108-4264-a35c-ce736e71cf9a__entry__1 id_0__4b4f2e18-e108-4264-a35c-ce736e71cf9a__entry__2 id_0__4b4f2e18-e108-4264-a35c-ce736e71cf9a__entry__3 id_0__4b4f2e18-e108-4264-a35c-ce736e71cf9a__entry__4 ">String</td><td className="entry" headers="id_0__4b4f2e18-e108-4264-a35c-ce736e71cf9a__entry__1 id_0__4b4f2e18-e108-4264-a35c-ce736e71cf9a__entry__2 id_0__4b4f2e18-e108-4264-a35c-ce736e71cf9a__entry__3 id_0__4b4f2e18-e108-4264-a35c-ce736e71cf9a__entry__4 ">Yes</td><td className="entry" headers="id_0__4b4f2e18-e108-4264-a35c-ce736e71cf9a__entry__1 id_0__4b4f2e18-e108-4264-a35c-ce736e71cf9a__entry__2 id_0__4b4f2e18-e108-4264-a35c-ce736e71cf9a__entry__3 id_0__4b4f2e18-e108-4264-a35c-ce736e71cf9a__entry__4 ">Absolute path of the image</td></tr><tr className><td className="entry" headers="id_0__4b4f2e18-e108-4264-a35c-ce736e71cf9a__entry__1 id_0__4b4f2e18-e108-4264-a35c-ce736e71cf9a__entry__2 id_0__4b4f2e18-e108-4264-a35c-ce736e71cf9a__entry__3 id_0__4b4f2e18-e108-4264-a35c-ce736e71cf9a__entry__4 ">flowControl</td><td className="entry" headers="id_0__4b4f2e18-e108-4264-a35c-ce736e71cf9a__entry__1 id_0__4b4f2e18-e108-4264-a35c-ce736e71cf9a__entry__2 id_0__4b4f2e18-e108-4264-a35c-ce736e71cf9a__entry__3 id_0__4b4f2e18-e108-4264-a35c-ce736e71cf9a__entry__4 ">FailureHandling</td><td className="entry" headers="id_0__4b4f2e18-e108-4264-a35c-ce736e71cf9a__entry__1 id_0__4b4f2e18-e108-4264-a35c-ce736e71cf9a__entry__2 id_0__4b4f2e18-e108-4264-a35c-ce736e71cf9a__entry__3 id_0__4b4f2e18-e108-4264-a35c-ce736e71cf9a__entry__4 ">Optional</td><td className="entry" headers="id_0__4b4f2e18-e108-4264-a35c-ce736e71cf9a__entry__1 id_0__4b4f2e18-e108-4264-a35c-ce736e71cf9a__entry__2 id_0__4b4f2e18-e108-4264-a35c-ce736e71cf9a__entry__3 id_0__4b4f2e18-e108-4264-a35c-ce736e71cf9a__entry__4 ">Specify <a className="xref" href="/katalon-studio/maintain-tests/configure-failure-handling-settings-in-katalon-studio">failure handling</a> schema to determine whether the execution should be allowed to continue or stop.</td></tr></tbody></table> 

## Returns

<p xmlns="http://www.w3.org/1999/xhtml" className="p">The first found WebElement that is recognized by the given image.</p> 

## Example

You want to locate a UI element on a mobile device screen using a reference image:

<div xmlns="http://www.w3.org/1999/xhtml" className="p"><pre className="pre codeblock"><code>WebElement element = Mobile.findImageElement("/Users/myaccount/Desktop/image.png"){"\n"}println "Element found at: (" + element.getPosition().x + ", " + element.getPosition().y + ")"{"\n"}</code></pre></div>
