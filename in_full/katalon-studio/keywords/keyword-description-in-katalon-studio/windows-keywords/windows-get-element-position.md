---
hide_title: true
title: '[Windows] Get Element Position'
---

# <a id="topic-6525" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>[Windows] Get Element Position


## Description

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Get the position of the <code className="ph codeph">WebElement</code> that is found by using locator value of the given <code className="ph codeph">windowsObject</code>.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Keyword name: <code className="ph codeph">getElementPosition</code></p> 

## Parameters

<table xmlns="http://www.w3.org/1999/xhtml" className="table anchor_top_offset" id="topic-6525__e960d30b-09fe-4ac3-a5a6-10755a8f7c59"><caption /><colgroup><col style={{width: '20%'}} /><col style={{width: '20%'}} /><col style={{width: '20%'}} /><col style={{width: '40%'}} /></colgroup><thead className="thead"><tr className><th className="entry anchor_top_offset" id="topic-6525__e960d30b-09fe-4ac3-a5a6-10755a8f7c59__entry__1">Parameter </th><th className="entry anchor_top_offset" id="topic-6525__e960d30b-09fe-4ac3-a5a6-10755a8f7c59__entry__2">Parameter Type</th><th className="entry anchor_top_offset" id="topic-6525__e960d30b-09fe-4ac3-a5a6-10755a8f7c59__entry__3">Required</th><th className="entry anchor_top_offset" id="topic-6525__e960d30b-09fe-4ac3-a5a6-10755a8f7c59__entry__4">Description</th></tr></thead><tbody className="tbody"><tr className><td className="entry" headers="topic-6525__e960d30b-09fe-4ac3-a5a6-10755a8f7c59__entry__1 topic-6525__e960d30b-09fe-4ac3-a5a6-10755a8f7c59__entry__2 topic-6525__e960d30b-09fe-4ac3-a5a6-10755a8f7c59__entry__3 topic-6525__e960d30b-09fe-4ac3-a5a6-10755a8f7c59__entry__4 " rowSpan={1} colSpan={1}><code className="ph codeph">windowsObject</code></td><td className="entry" headers="topic-6525__e960d30b-09fe-4ac3-a5a6-10755a8f7c59__entry__1 topic-6525__e960d30b-09fe-4ac3-a5a6-10755a8f7c59__entry__2 topic-6525__e960d30b-09fe-4ac3-a5a6-10755a8f7c59__entry__3 topic-6525__e960d30b-09fe-4ac3-a5a6-10755a8f7c59__entry__4 " rowSpan={1} colSpan={1}><code className="ph codeph">WindowsTestObject</code></td><td className="entry" headers="topic-6525__e960d30b-09fe-4ac3-a5a6-10755a8f7c59__entry__1 topic-6525__e960d30b-09fe-4ac3-a5a6-10755a8f7c59__entry__2 topic-6525__e960d30b-09fe-4ac3-a5a6-10755a8f7c59__entry__3 topic-6525__e960d30b-09fe-4ac3-a5a6-10755a8f7c59__entry__4 " rowSpan={1} colSpan={1}>Yes</td><td className="entry" headers="topic-6525__e960d30b-09fe-4ac3-a5a6-10755a8f7c59__entry__1 topic-6525__e960d30b-09fe-4ac3-a5a6-10755a8f7c59__entry__2 topic-6525__e960d30b-09fe-4ac3-a5a6-10755a8f7c59__entry__3 topic-6525__e960d30b-09fe-4ac3-a5a6-10755a8f7c59__entry__4 " rowSpan={1} colSpan={1}>An object that describes locator and locator strategy to find Windows Element.</td></tr></tbody></table> 

## Returns

<table xmlns="http://www.w3.org/1999/xhtml" className="table anchor_top_offset" id="topic-6525__1b1b0cbe-9c22-4c5f-96c3-46f1e73f0462"><caption /><colgroup><col style={{width: '33.33333333333333%'}} /><col style={{width: '66.66666666666666%'}} /></colgroup><thead className="thead"><tr className><th className="entry anchor_top_offset" id="topic-6525__1b1b0cbe-9c22-4c5f-96c3-46f1e73f0462__entry__1">Parameter Type</th><th className="entry anchor_top_offset" id="topic-6525__1b1b0cbe-9c22-4c5f-96c3-46f1e73f0462__entry__2">Description</th></tr></thead><tbody className="tbody"><tr className><td className="entry" headers="topic-6525__1b1b0cbe-9c22-4c5f-96c3-46f1e73f0462__entry__1 topic-6525__1b1b0cbe-9c22-4c5f-96c3-46f1e73f0462__entry__2 " rowSpan={1} colSpan={1}>Position of the element</td><td className="entry" headers="topic-6525__1b1b0cbe-9c22-4c5f-96c3-46f1e73f0462__entry__1 topic-6525__1b1b0cbe-9c22-4c5f-96c3-46f1e73f0462__entry__2 " rowSpan={1} colSpan={1}>Point indicating the element's position.</td></tr><tr className><td className="entry" headers="topic-6525__1b1b0cbe-9c22-4c5f-96c3-46f1e73f0462__entry__1 topic-6525__1b1b0cbe-9c22-4c5f-96c3-46f1e73f0462__entry__2 "><code className="ph codeph">StepFailedException</code></td><td className="entry" headers="topic-6525__1b1b0cbe-9c22-4c5f-96c3-46f1e73f0462__entry__1 topic-6525__1b1b0cbe-9c22-4c5f-96c3-46f1e73f0462__entry__2 ">Throws an error if Katalon Studio cannot find the specified element.</td></tr></tbody></table> 

## Example

<div xmlns="http://www.w3.org/1999/xhtml" className="p"><pre className="pre codeblock"><code>import org.openqa.selenium.Point as Point{"\n"}Point position = Windows.getElementPosition(findWindowsObject('Object Repository/Notepad/Edit')){"\n"}println String.format("{"{"} x: %d, y: %d {"}"}", position.getX(), position.getY())</code></pre></div>
