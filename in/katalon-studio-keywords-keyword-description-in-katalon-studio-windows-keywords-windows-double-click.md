---
hide_title: true
title: '[Windows] Double-click'
---

# <a id="topic-8241" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>[Windows] Double-click


## Description

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Perform a double-clicking action on the Web element found by using the locator value of the given Windows object.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Keyword name: <code className="ph codeph">doubleClick</code></p> 

## Parameters

<table xmlns="http://www.w3.org/1999/xhtml" className="table anchor_top_offset" id="topic-8241__63b8f447-ccc4-4f48-b9b5-f6dd62f331d9"><caption /><colgroup><col style={{width: '20%'}} /><col style={{width: '20%'}} /><col style={{width: '20%'}} /><col style={{width: '40%'}} /></colgroup><thead className="thead"><tr className><th className="entry anchor_top_offset" id="topic-8241__63b8f447-ccc4-4f48-b9b5-f6dd62f331d9__entry__1">Parameter </th><th className="entry anchor_top_offset" id="topic-8241__63b8f447-ccc4-4f48-b9b5-f6dd62f331d9__entry__2">Parameter Type</th><th className="entry anchor_top_offset" id="topic-8241__63b8f447-ccc4-4f48-b9b5-f6dd62f331d9__entry__3">Required</th><th className="entry anchor_top_offset" id="topic-8241__63b8f447-ccc4-4f48-b9b5-f6dd62f331d9__entry__4">Description</th></tr></thead><tbody className="tbody"><tr className><td className="entry" headers="topic-8241__63b8f447-ccc4-4f48-b9b5-f6dd62f331d9__entry__1 topic-8241__63b8f447-ccc4-4f48-b9b5-f6dd62f331d9__entry__2 topic-8241__63b8f447-ccc4-4f48-b9b5-f6dd62f331d9__entry__3 topic-8241__63b8f447-ccc4-4f48-b9b5-f6dd62f331d9__entry__4 " rowSpan={1} colSpan={1}><code className="ph codeph">windowsObject</code></td><td className="entry" headers="topic-8241__63b8f447-ccc4-4f48-b9b5-f6dd62f331d9__entry__1 topic-8241__63b8f447-ccc4-4f48-b9b5-f6dd62f331d9__entry__2 topic-8241__63b8f447-ccc4-4f48-b9b5-f6dd62f331d9__entry__3 topic-8241__63b8f447-ccc4-4f48-b9b5-f6dd62f331d9__entry__4 " rowSpan={1} colSpan={1}><code className="ph codeph">WindowsTestObject</code></td><td className="entry" headers="topic-8241__63b8f447-ccc4-4f48-b9b5-f6dd62f331d9__entry__1 topic-8241__63b8f447-ccc4-4f48-b9b5-f6dd62f331d9__entry__2 topic-8241__63b8f447-ccc4-4f48-b9b5-f6dd62f331d9__entry__3 topic-8241__63b8f447-ccc4-4f48-b9b5-f6dd62f331d9__entry__4 " rowSpan={1} colSpan={1}>Optional</td><td className="entry" headers="topic-8241__63b8f447-ccc4-4f48-b9b5-f6dd62f331d9__entry__1 topic-8241__63b8f447-ccc4-4f48-b9b5-f6dd62f331d9__entry__2 topic-8241__63b8f447-ccc4-4f48-b9b5-f6dd62f331d9__entry__3 topic-8241__63b8f447-ccc4-4f48-b9b5-f6dd62f331d9__entry__4 " rowSpan={1} colSpan={1}>An object describing the locator and locator strategy to find a Windows element.</td></tr></tbody></table> 

## Example

<div xmlns="http://www.w3.org/1999/xhtml" className="p"><pre className="pre codeblock"><code>"Double-click on the item element to open the editor"{"\n"}Windows.doubleClick(findWindowsObject("Object Repository/item"))</code></pre></div>
