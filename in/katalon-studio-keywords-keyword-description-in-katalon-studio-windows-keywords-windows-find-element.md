---
hide_title: true
title: '[Windows] Find Element'
---

# <a id="topic-8340" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>[Windows] Find Element


## Description

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Find an element by using the locator value of the given Windows object.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Keyword name: <code className="ph codeph">findElement</code></p> 

## Parameters

<table xmlns="http://www.w3.org/1999/xhtml" className="table anchor_top_offset" id="topic-8340__9c08b2ae-ea87-4197-90d5-5f11320a564d"><caption /><colgroup><col style={{width: '20%'}} /><col style={{width: '20%'}} /><col style={{width: '20%'}} /><col style={{width: '40%'}} /></colgroup><thead className="thead"><tr className><th className="entry anchor_top_offset" id="topic-8340__9c08b2ae-ea87-4197-90d5-5f11320a564d__entry__1">Parameter </th><th className="entry anchor_top_offset" id="topic-8340__9c08b2ae-ea87-4197-90d5-5f11320a564d__entry__2">Parameter Type</th><th className="entry anchor_top_offset" id="topic-8340__9c08b2ae-ea87-4197-90d5-5f11320a564d__entry__3">Required</th><th className="entry anchor_top_offset" id="topic-8340__9c08b2ae-ea87-4197-90d5-5f11320a564d__entry__4">Description</th></tr></thead><tbody className="tbody"><tr className><td className="entry" headers="topic-8340__9c08b2ae-ea87-4197-90d5-5f11320a564d__entry__1 topic-8340__9c08b2ae-ea87-4197-90d5-5f11320a564d__entry__2 topic-8340__9c08b2ae-ea87-4197-90d5-5f11320a564d__entry__3 topic-8340__9c08b2ae-ea87-4197-90d5-5f11320a564d__entry__4 " rowSpan={1} colSpan={1}><code className="ph codeph">windowsObject</code></td><td className="entry" headers="topic-8340__9c08b2ae-ea87-4197-90d5-5f11320a564d__entry__1 topic-8340__9c08b2ae-ea87-4197-90d5-5f11320a564d__entry__2 topic-8340__9c08b2ae-ea87-4197-90d5-5f11320a564d__entry__3 topic-8340__9c08b2ae-ea87-4197-90d5-5f11320a564d__entry__4 " rowSpan={1} colSpan={1}><code className="ph codeph">WindowsTestObject</code></td><td className="entry" headers="topic-8340__9c08b2ae-ea87-4197-90d5-5f11320a564d__entry__1 topic-8340__9c08b2ae-ea87-4197-90d5-5f11320a564d__entry__2 topic-8340__9c08b2ae-ea87-4197-90d5-5f11320a564d__entry__3 topic-8340__9c08b2ae-ea87-4197-90d5-5f11320a564d__entry__4 " rowSpan={1} colSpan={1}>Yes</td><td className="entry" headers="topic-8340__9c08b2ae-ea87-4197-90d5-5f11320a564d__entry__1 topic-8340__9c08b2ae-ea87-4197-90d5-5f11320a564d__entry__2 topic-8340__9c08b2ae-ea87-4197-90d5-5f11320a564d__entry__3 topic-8340__9c08b2ae-ea87-4197-90d5-5f11320a564d__entry__4 " rowSpan={1} colSpan={1}>An object describing the locator and locator strategy to find a Windows element.</td></tr></tbody></table> 

## Returns

<table xmlns="http://www.w3.org/1999/xhtml" className="table anchor_top_offset" id="topic-8340__1a21ab52-dff8-4320-a63b-4741866fb386"><caption /><colgroup><col style={{width: '33.33333333333333%'}} /><col style={{width: '66.66666666666666%'}} /></colgroup><thead className="thead"><tr className><th className="entry anchor_top_offset" id="topic-8340__1a21ab52-dff8-4320-a63b-4741866fb386__entry__1">Parameter Type</th><th className="entry anchor_top_offset" id="topic-8340__1a21ab52-dff8-4320-a63b-4741866fb386__entry__2">Description</th></tr></thead><tbody className="tbody"><tr className><td className="entry" headers="topic-8340__1a21ab52-dff8-4320-a63b-4741866fb386__entry__1 topic-8340__1a21ab52-dff8-4320-a63b-4741866fb386__entry__2 " rowSpan={1} colSpan={1}><code className="ph codeph">WebElement</code></td><td className="entry" headers="topic-8340__1a21ab52-dff8-4320-a63b-4741866fb386__entry__1 topic-8340__1a21ab52-dff8-4320-a63b-4741866fb386__entry__2 " rowSpan={1} colSpan={1}>The found element.</td></tr></tbody></table> 

## Example

<div xmlns="http://www.w3.org/1999/xhtml" className="p"><pre className="pre codeblock"><code>WebElement foundElement = Windows.findElement(findWindowsObject('Object Repository/Notepad/Edit'));{"\n"}println "The Found element said: " + foundElement.getText()</code></pre></div>
