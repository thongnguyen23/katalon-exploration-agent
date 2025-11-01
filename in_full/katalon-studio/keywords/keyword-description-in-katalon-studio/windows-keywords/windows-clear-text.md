---
hide_title: true
title: '[Windows] Clear Text'
---

# <a id="topic-2616" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>[Windows] Clear Text


## Description

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Clear the text content of the Web element found by using locator value of the given windows object.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Keyword name: <code className="ph codeph">clearText</code></p> 

## Parameters

<table xmlns="http://www.w3.org/1999/xhtml" className="table anchor_top_offset" id="topic-2616__e4eed75a-fc9a-4204-b8f4-9b73a748729e"><caption /><colgroup><col style={{width: '20%'}} /><col style={{width: '20%'}} /><col style={{width: '20%'}} /><col style={{width: '40%'}} /></colgroup><thead className="thead"><tr className><th className="entry anchor_top_offset" id="topic-2616__e4eed75a-fc9a-4204-b8f4-9b73a748729e__entry__1">Parameter </th><th className="entry anchor_top_offset" id="topic-2616__e4eed75a-fc9a-4204-b8f4-9b73a748729e__entry__2">Parameter Type</th><th className="entry anchor_top_offset" id="topic-2616__e4eed75a-fc9a-4204-b8f4-9b73a748729e__entry__3">Required</th><th className="entry anchor_top_offset" id="topic-2616__e4eed75a-fc9a-4204-b8f4-9b73a748729e__entry__4">Description</th></tr></thead><tbody className="tbody"><tr className><td className="entry" headers="topic-2616__e4eed75a-fc9a-4204-b8f4-9b73a748729e__entry__1 topic-2616__e4eed75a-fc9a-4204-b8f4-9b73a748729e__entry__2 topic-2616__e4eed75a-fc9a-4204-b8f4-9b73a748729e__entry__3 topic-2616__e4eed75a-fc9a-4204-b8f4-9b73a748729e__entry__4 " rowSpan={1} colSpan={1}><code className="ph codeph">windowsObject</code></td><td className="entry" headers="topic-2616__e4eed75a-fc9a-4204-b8f4-9b73a748729e__entry__1 topic-2616__e4eed75a-fc9a-4204-b8f4-9b73a748729e__entry__2 topic-2616__e4eed75a-fc9a-4204-b8f4-9b73a748729e__entry__3 topic-2616__e4eed75a-fc9a-4204-b8f4-9b73a748729e__entry__4 " rowSpan={1} colSpan={1}><code className="ph codeph">WindowsTestObject</code></td><td className="entry" headers="topic-2616__e4eed75a-fc9a-4204-b8f4-9b73a748729e__entry__1 topic-2616__e4eed75a-fc9a-4204-b8f4-9b73a748729e__entry__2 topic-2616__e4eed75a-fc9a-4204-b8f4-9b73a748729e__entry__3 topic-2616__e4eed75a-fc9a-4204-b8f4-9b73a748729e__entry__4 " rowSpan={1} colSpan={1}>Yes</td><td className="entry" headers="topic-2616__e4eed75a-fc9a-4204-b8f4-9b73a748729e__entry__1 topic-2616__e4eed75a-fc9a-4204-b8f4-9b73a748729e__entry__2 topic-2616__e4eed75a-fc9a-4204-b8f4-9b73a748729e__entry__3 topic-2616__e4eed75a-fc9a-4204-b8f4-9b73a748729e__entry__4 " rowSpan={1} colSpan={1}>An object describing the locator and locator strategy to find a Windows element.</td></tr></tbody></table> 

## Example

<div xmlns="http://www.w3.org/1999/xhtml" className="p"><pre className="pre codeblock"><code>"Set 'Welcome to Katalon Studio' on the edit panel"{"\n"}Windows.setText(findWindowsObject("Object Repository/Edit"), 'Welcome to Katalon Studio'){"\n"}{"\n"}"Get text of the edit panel and verify"{"\n"}def text = Windows.getText(findWindowsObject("Object Repository/Edit")){"\n"}{"\n"}assert text == 'Welcome to Katalon Studio'{"\n"}{"\n"}"Clear text of the edit panel"{"\n"}Windows.clearText(findWindowsObject("Object Repository/Edit")){"\n"}{"\n"}"Get text of the edit panel and verify the text is clear"{"\n"}text = Windows.getText(findWindowsObject("Object Repository/Edit")){"\n"}{"\n"}assert text == 'Welcome to Katalon Studio'</code></pre></div>
