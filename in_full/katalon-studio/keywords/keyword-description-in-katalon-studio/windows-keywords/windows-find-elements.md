---
hide_title: true
title: '[Windows] Find Elements'
---

# <a id="topic-3896" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>[Windows] Find Elements


## Description

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Find elements by using the locator value of the given Windows object.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Keyword name: <code className="ph codeph">findElements</code></p> 

## Parameters

<table xmlns="http://www.w3.org/1999/xhtml" className="table anchor_top_offset" id="topic-3896__2f76e056-c130-4433-b6df-aeeab958766a"><caption /><colgroup><col style={{width: '20%'}} /><col style={{width: '20%'}} /><col style={{width: '20%'}} /><col style={{width: '40%'}} /></colgroup><thead className="thead"><tr className><th className="entry anchor_top_offset" id="topic-3896__2f76e056-c130-4433-b6df-aeeab958766a__entry__1">Parameter </th><th className="entry anchor_top_offset" id="topic-3896__2f76e056-c130-4433-b6df-aeeab958766a__entry__2">Parameter Type</th><th className="entry anchor_top_offset" id="topic-3896__2f76e056-c130-4433-b6df-aeeab958766a__entry__3">Required</th><th className="entry anchor_top_offset" id="topic-3896__2f76e056-c130-4433-b6df-aeeab958766a__entry__4">Description</th></tr></thead><tbody className="tbody"><tr className><td className="entry" headers="topic-3896__2f76e056-c130-4433-b6df-aeeab958766a__entry__1 topic-3896__2f76e056-c130-4433-b6df-aeeab958766a__entry__2 topic-3896__2f76e056-c130-4433-b6df-aeeab958766a__entry__3 topic-3896__2f76e056-c130-4433-b6df-aeeab958766a__entry__4 " rowSpan={1} colSpan={1}><code className="ph codeph">windowsObject</code></td><td className="entry" headers="topic-3896__2f76e056-c130-4433-b6df-aeeab958766a__entry__1 topic-3896__2f76e056-c130-4433-b6df-aeeab958766a__entry__2 topic-3896__2f76e056-c130-4433-b6df-aeeab958766a__entry__3 topic-3896__2f76e056-c130-4433-b6df-aeeab958766a__entry__4 " rowSpan={1} colSpan={1}><code className="ph codeph">WindowsTestObject</code></td><td className="entry" headers="topic-3896__2f76e056-c130-4433-b6df-aeeab958766a__entry__1 topic-3896__2f76e056-c130-4433-b6df-aeeab958766a__entry__2 topic-3896__2f76e056-c130-4433-b6df-aeeab958766a__entry__3 topic-3896__2f76e056-c130-4433-b6df-aeeab958766a__entry__4 " rowSpan={1} colSpan={1}>Yes</td><td className="entry" headers="topic-3896__2f76e056-c130-4433-b6df-aeeab958766a__entry__1 topic-3896__2f76e056-c130-4433-b6df-aeeab958766a__entry__2 topic-3896__2f76e056-c130-4433-b6df-aeeab958766a__entry__3 topic-3896__2f76e056-c130-4433-b6df-aeeab958766a__entry__4 " rowSpan={1} colSpan={1}>An object describing the locator and locator strategy to find a Windows element.</td></tr></tbody></table> 

## Returns

<table xmlns="http://www.w3.org/1999/xhtml" className="table anchor_top_offset" id="topic-3896__f65442c2-225e-4b0f-a606-03c5c536e4e8"><caption /><colgroup><col style={{width: '33.33333333333333%'}} /><col style={{width: '66.66666666666666%'}} /></colgroup><thead className="thead"><tr className><th className="entry anchor_top_offset" id="topic-3896__f65442c2-225e-4b0f-a606-03c5c536e4e8__entry__1">Parameter Type</th><th className="entry anchor_top_offset" id="topic-3896__f65442c2-225e-4b0f-a606-03c5c536e4e8__entry__2">Description</th></tr></thead><tbody className="tbody"><tr className><td className="entry" headers="topic-3896__f65442c2-225e-4b0f-a606-03c5c536e4e8__entry__1 topic-3896__f65442c2-225e-4b0f-a606-03c5c536e4e8__entry__2 " rowSpan={1} colSpan={1}>(List) <code className="ph codeph">WebElement</code></td><td className="entry" headers="topic-3896__f65442c2-225e-4b0f-a606-03c5c536e4e8__entry__1 topic-3896__f65442c2-225e-4b0f-a606-03c5c536e4e8__entry__2 " rowSpan={1} colSpan={1}>The found elements in list form.</td></tr></tbody></table> 

## Example

<div xmlns="http://www.w3.org/1999/xhtml" className="p"><pre className="pre codeblock"><code>List&lt;WebElement&gt; foundElements = Windows.findElements(findWindowsObject('Object Repository/Notepad/Edit')){"\n"}println "Found " + foundElements.size() + " element(s)"{"\n"}println "The First found element said: " + foundElements.get(0).getText()</code></pre></div>
