---
hide_title: true
title: '[Windows] Right-click'
---

# <a id="topic-4888" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>[Windows] Right-click


## Description

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Perform a right-clicking action on the Web element found by using the locator value of the given Windows object.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Keyword name: <code className="ph codeph">rightClick</code></p> 

## Parameters

<table xmlns="http://www.w3.org/1999/xhtml" className="table anchor_top_offset" id="topic-4888__6d1d5685-37e5-4ba1-a0ea-ae1bc610d2b4"><caption /><colgroup><col style={{width: '20%'}} /><col style={{width: '20%'}} /><col style={{width: '20%'}} /><col style={{width: '40%'}} /></colgroup><thead className="thead"><tr className><th className="entry anchor_top_offset" id="topic-4888__6d1d5685-37e5-4ba1-a0ea-ae1bc610d2b4__entry__1">Parameter </th><th className="entry anchor_top_offset" id="topic-4888__6d1d5685-37e5-4ba1-a0ea-ae1bc610d2b4__entry__2">Parameter Type</th><th className="entry anchor_top_offset" id="topic-4888__6d1d5685-37e5-4ba1-a0ea-ae1bc610d2b4__entry__3">Required</th><th className="entry anchor_top_offset" id="topic-4888__6d1d5685-37e5-4ba1-a0ea-ae1bc610d2b4__entry__4">Description</th></tr></thead><tbody className="tbody"><tr className><td className="entry" headers="topic-4888__6d1d5685-37e5-4ba1-a0ea-ae1bc610d2b4__entry__1 topic-4888__6d1d5685-37e5-4ba1-a0ea-ae1bc610d2b4__entry__2 topic-4888__6d1d5685-37e5-4ba1-a0ea-ae1bc610d2b4__entry__3 topic-4888__6d1d5685-37e5-4ba1-a0ea-ae1bc610d2b4__entry__4 " rowSpan={1} colSpan={1}><code className="ph codeph">windowsObject</code></td><td className="entry" headers="topic-4888__6d1d5685-37e5-4ba1-a0ea-ae1bc610d2b4__entry__1 topic-4888__6d1d5685-37e5-4ba1-a0ea-ae1bc610d2b4__entry__2 topic-4888__6d1d5685-37e5-4ba1-a0ea-ae1bc610d2b4__entry__3 topic-4888__6d1d5685-37e5-4ba1-a0ea-ae1bc610d2b4__entry__4 " rowSpan={1} colSpan={1}><code className="ph codeph">WindowsTestObject</code></td><td className="entry" headers="topic-4888__6d1d5685-37e5-4ba1-a0ea-ae1bc610d2b4__entry__1 topic-4888__6d1d5685-37e5-4ba1-a0ea-ae1bc610d2b4__entry__2 topic-4888__6d1d5685-37e5-4ba1-a0ea-ae1bc610d2b4__entry__3 topic-4888__6d1d5685-37e5-4ba1-a0ea-ae1bc610d2b4__entry__4 " rowSpan={1} colSpan={1}>Yes</td><td className="entry" headers="topic-4888__6d1d5685-37e5-4ba1-a0ea-ae1bc610d2b4__entry__1 topic-4888__6d1d5685-37e5-4ba1-a0ea-ae1bc610d2b4__entry__2 topic-4888__6d1d5685-37e5-4ba1-a0ea-ae1bc610d2b4__entry__3 topic-4888__6d1d5685-37e5-4ba1-a0ea-ae1bc610d2b4__entry__4 " rowSpan={1} colSpan={1}>An object describing the locator and locator strategy to find a Windows element.</td></tr></tbody></table> 

## Example

<div xmlns="http://www.w3.org/1999/xhtml" className="p"><pre className="pre codeblock"><code>"Right-click on the item element to view the context menu"{"\n"}Windows.rightClick(findWindowsObject("Object Repository/item"))</code></pre></div>
