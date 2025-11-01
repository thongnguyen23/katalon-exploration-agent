---
hide_title: true
title: '[Windows] Click'
---

# <a id="topic-6988" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>[Windows] Click


## Description

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Perform a left-clicking action on the Web element found by using the locator value of the given Windows object.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Keyword name: <code className="ph codeph">click</code></p> 

## Parameters

<table xmlns="http://www.w3.org/1999/xhtml" className="table anchor_top_offset" id="topic-6988__0304a765-3175-4a0a-8f17-4060b2cf50b4"><caption /><colgroup><col style={{width: '20%'}} /><col style={{width: '20%'}} /><col style={{width: '20%'}} /><col style={{width: '40%'}} /></colgroup><thead className="thead"><tr className><th className="entry anchor_top_offset" id="topic-6988__0304a765-3175-4a0a-8f17-4060b2cf50b4__entry__1">Parameter </th><th className="entry anchor_top_offset" id="topic-6988__0304a765-3175-4a0a-8f17-4060b2cf50b4__entry__2">Parameter Type</th><th className="entry anchor_top_offset" id="topic-6988__0304a765-3175-4a0a-8f17-4060b2cf50b4__entry__3">Required</th><th className="entry anchor_top_offset" id="topic-6988__0304a765-3175-4a0a-8f17-4060b2cf50b4__entry__4">Description</th></tr></thead><tbody className="tbody"><tr className><td className="entry" headers="topic-6988__0304a765-3175-4a0a-8f17-4060b2cf50b4__entry__1 topic-6988__0304a765-3175-4a0a-8f17-4060b2cf50b4__entry__2 topic-6988__0304a765-3175-4a0a-8f17-4060b2cf50b4__entry__3 topic-6988__0304a765-3175-4a0a-8f17-4060b2cf50b4__entry__4 " rowSpan={1} colSpan={1}><code className="ph codeph">windowsObject</code></td><td className="entry" headers="topic-6988__0304a765-3175-4a0a-8f17-4060b2cf50b4__entry__1 topic-6988__0304a765-3175-4a0a-8f17-4060b2cf50b4__entry__2 topic-6988__0304a765-3175-4a0a-8f17-4060b2cf50b4__entry__3 topic-6988__0304a765-3175-4a0a-8f17-4060b2cf50b4__entry__4 " rowSpan={1} colSpan={1}><code className="ph codeph">WindowsTestObject</code></td><td className="entry" headers="topic-6988__0304a765-3175-4a0a-8f17-4060b2cf50b4__entry__1 topic-6988__0304a765-3175-4a0a-8f17-4060b2cf50b4__entry__2 topic-6988__0304a765-3175-4a0a-8f17-4060b2cf50b4__entry__3 topic-6988__0304a765-3175-4a0a-8f17-4060b2cf50b4__entry__4 " rowSpan={1} colSpan={1}>Yes</td><td className="entry" headers="topic-6988__0304a765-3175-4a0a-8f17-4060b2cf50b4__entry__1 topic-6988__0304a765-3175-4a0a-8f17-4060b2cf50b4__entry__2 topic-6988__0304a765-3175-4a0a-8f17-4060b2cf50b4__entry__3 topic-6988__0304a765-3175-4a0a-8f17-4060b2cf50b4__entry__4 " rowSpan={1} colSpan={1}>An object describing the locator and locator strategy to find a Windows element.</td></tr></tbody></table> 

## Example

<div xmlns="http://www.w3.org/1999/xhtml" className="p"><pre className="pre codeblock"><code>"Click on the Close button"{"\n"} Windows.click(findWindowsObject("Object Repository/CloseButton"))</code></pre></div>
