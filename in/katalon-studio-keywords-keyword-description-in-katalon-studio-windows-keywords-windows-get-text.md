---
hide_title: true
title: '[Windows] Get Text'
---

# <a id="topic-1982" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>[Windows] Get Text


## Description

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Get the text content of the Web element found by using the locator value of the given Windows object. This action appends the given text on the element without clearing its current text.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Keyword name: <code className="ph codeph">getText</code></p> 

## Parameters

<table xmlns="http://www.w3.org/1999/xhtml" className="table anchor_top_offset" id="topic-1982__1e8b4af1-662f-49b6-9458-0d29610af0ef"><caption /><colgroup><col style={{width: '20%'}} /><col style={{width: '20%'}} /><col style={{width: '20%'}} /><col style={{width: '40%'}} /></colgroup><thead className="thead"><tr className><th className="entry anchor_top_offset" id="topic-1982__1e8b4af1-662f-49b6-9458-0d29610af0ef__entry__1">Parameter </th><th className="entry anchor_top_offset" id="topic-1982__1e8b4af1-662f-49b6-9458-0d29610af0ef__entry__2">Parameter Type</th><th className="entry anchor_top_offset" id="topic-1982__1e8b4af1-662f-49b6-9458-0d29610af0ef__entry__3">Required</th><th className="entry anchor_top_offset" id="topic-1982__1e8b4af1-662f-49b6-9458-0d29610af0ef__entry__4">Description</th></tr></thead><tbody className="tbody"><tr className><td className="entry" headers="topic-1982__1e8b4af1-662f-49b6-9458-0d29610af0ef__entry__1 topic-1982__1e8b4af1-662f-49b6-9458-0d29610af0ef__entry__2 topic-1982__1e8b4af1-662f-49b6-9458-0d29610af0ef__entry__3 topic-1982__1e8b4af1-662f-49b6-9458-0d29610af0ef__entry__4 " rowSpan={1} colSpan={1}><code className="ph codeph">windowsObject</code></td><td className="entry" headers="topic-1982__1e8b4af1-662f-49b6-9458-0d29610af0ef__entry__1 topic-1982__1e8b4af1-662f-49b6-9458-0d29610af0ef__entry__2 topic-1982__1e8b4af1-662f-49b6-9458-0d29610af0ef__entry__3 topic-1982__1e8b4af1-662f-49b6-9458-0d29610af0ef__entry__4 " rowSpan={1} colSpan={1}><code className="ph codeph">WindowsTestObject</code></td><td className="entry" headers="topic-1982__1e8b4af1-662f-49b6-9458-0d29610af0ef__entry__1 topic-1982__1e8b4af1-662f-49b6-9458-0d29610af0ef__entry__2 topic-1982__1e8b4af1-662f-49b6-9458-0d29610af0ef__entry__3 topic-1982__1e8b4af1-662f-49b6-9458-0d29610af0ef__entry__4 " rowSpan={1} colSpan={1}>Yes</td><td className="entry" headers="topic-1982__1e8b4af1-662f-49b6-9458-0d29610af0ef__entry__1 topic-1982__1e8b4af1-662f-49b6-9458-0d29610af0ef__entry__2 topic-1982__1e8b4af1-662f-49b6-9458-0d29610af0ef__entry__3 topic-1982__1e8b4af1-662f-49b6-9458-0d29610af0ef__entry__4 " rowSpan={1} colSpan={1}>An object describing the locator and locator strategy to find a Windows element.</td></tr></tbody></table> 

## Returns

<table xmlns="http://www.w3.org/1999/xhtml" className="table anchor_top_offset" id="topic-1982__86f1edc8-ea2c-42d7-8d3d-df2998352622"><caption /><colgroup><col style={{width: '33.33333333333333%'}} /><col style={{width: '66.66666666666666%'}} /></colgroup><thead className="thead"><tr className><th className="entry anchor_top_offset" id="topic-1982__86f1edc8-ea2c-42d7-8d3d-df2998352622__entry__1">Parameter Type</th><th className="entry anchor_top_offset" id="topic-1982__86f1edc8-ea2c-42d7-8d3d-df2998352622__entry__2">Description</th></tr></thead><tbody className="tbody"><tr className><td className="entry" headers="topic-1982__86f1edc8-ea2c-42d7-8d3d-df2998352622__entry__1 topic-1982__86f1edc8-ea2c-42d7-8d3d-df2998352622__entry__2 " rowSpan={1} colSpan={1}>String</td><td className="entry" headers="topic-1982__86f1edc8-ea2c-42d7-8d3d-df2998352622__entry__1 topic-1982__86f1edc8-ea2c-42d7-8d3d-df2998352622__entry__2 " rowSpan={1} colSpan={1}>The text content of the found Windows element.</td></tr></tbody></table> 

## Example

<div xmlns="http://www.w3.org/1999/xhtml" className="p"><pre className="pre codeblock"><code>"Set 'Welcome to Katalon Studio' on the edit panel"{"\n"}Windows.setText(findWindowsObject("Object Repository/Edit"), 'Welcome to Katalon Studio'){"\n"}{"\n"}"Get text of the edit panel and verify"{"\n"}def text = Windows.getText(findWindowsObject("Object Repository/Edit")){"\n"}{"\n"}assert text == 'Welcome to Katalon Studio'</code></pre></div>
