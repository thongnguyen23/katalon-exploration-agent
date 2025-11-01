---
hide_title: true
title: '[Windows] Get Element Rectangle'
---

# <a id="topic-2636" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>[Windows] Get Element Rectangle


## Description

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Get the bounding rectangle of the <code className="ph codeph">WebElement</code> that is found by using locator value of the given <code className="ph codeph">windowsObject</code>.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Keyword name: <code className="ph codeph">getElementRect</code></p> 

## Parameters

<table xmlns="http://www.w3.org/1999/xhtml" className="table anchor_top_offset" id="topic-2636__15e0563a-a835-4628-be4e-eedff8386fde"><caption /><colgroup><col style={{width: '20%'}} /><col style={{width: '20%'}} /><col style={{width: '20%'}} /><col style={{width: '40%'}} /></colgroup><thead className="thead"><tr className><th className="entry anchor_top_offset" id="topic-2636__15e0563a-a835-4628-be4e-eedff8386fde__entry__1">Parameter </th><th className="entry anchor_top_offset" id="topic-2636__15e0563a-a835-4628-be4e-eedff8386fde__entry__2">Parameter Type</th><th className="entry anchor_top_offset" id="topic-2636__15e0563a-a835-4628-be4e-eedff8386fde__entry__3">Required</th><th className="entry anchor_top_offset" id="topic-2636__15e0563a-a835-4628-be4e-eedff8386fde__entry__4">Description</th></tr></thead><tbody className="tbody"><tr className><td className="entry" headers="topic-2636__15e0563a-a835-4628-be4e-eedff8386fde__entry__1 topic-2636__15e0563a-a835-4628-be4e-eedff8386fde__entry__2 topic-2636__15e0563a-a835-4628-be4e-eedff8386fde__entry__3 topic-2636__15e0563a-a835-4628-be4e-eedff8386fde__entry__4 " rowSpan={1} colSpan={1}><code className="ph codeph">windowsObject</code></td><td className="entry" headers="topic-2636__15e0563a-a835-4628-be4e-eedff8386fde__entry__1 topic-2636__15e0563a-a835-4628-be4e-eedff8386fde__entry__2 topic-2636__15e0563a-a835-4628-be4e-eedff8386fde__entry__3 topic-2636__15e0563a-a835-4628-be4e-eedff8386fde__entry__4 " rowSpan={1} colSpan={1}><code className="ph codeph">WindowsTestObject</code></td><td className="entry" headers="topic-2636__15e0563a-a835-4628-be4e-eedff8386fde__entry__1 topic-2636__15e0563a-a835-4628-be4e-eedff8386fde__entry__2 topic-2636__15e0563a-a835-4628-be4e-eedff8386fde__entry__3 topic-2636__15e0563a-a835-4628-be4e-eedff8386fde__entry__4 " rowSpan={1} colSpan={1}>Yes</td><td className="entry" headers="topic-2636__15e0563a-a835-4628-be4e-eedff8386fde__entry__1 topic-2636__15e0563a-a835-4628-be4e-eedff8386fde__entry__2 topic-2636__15e0563a-a835-4628-be4e-eedff8386fde__entry__3 topic-2636__15e0563a-a835-4628-be4e-eedff8386fde__entry__4 " rowSpan={1} colSpan={1}>An object that describes locator and locator strategy to find Windows Element.</td></tr></tbody></table> 

## Returns

<table xmlns="http://www.w3.org/1999/xhtml" className="table anchor_top_offset" id="topic-2636__4c337364-2569-465a-9b6d-bae73f2339d2"><caption /><colgroup><col style={{width: '33.33333333333333%'}} /><col style={{width: '66.66666666666666%'}} /></colgroup><thead className="thead"><tr className><th className="entry anchor_top_offset" id="topic-2636__4c337364-2569-465a-9b6d-bae73f2339d2__entry__1">Parameter Type</th><th className="entry anchor_top_offset" id="topic-2636__4c337364-2569-465a-9b6d-bae73f2339d2__entry__2">Description</th></tr></thead><tbody className="tbody"><tr className><td className="entry" headers="topic-2636__4c337364-2569-465a-9b6d-bae73f2339d2__entry__1 topic-2636__4c337364-2569-465a-9b6d-bae73f2339d2__entry__2 " rowSpan={1} colSpan={1}><code className="ph codeph">Rectangle</code></td><td className="entry" headers="topic-2636__4c337364-2569-465a-9b6d-bae73f2339d2__entry__1 topic-2636__4c337364-2569-465a-9b6d-bae73f2339d2__entry__2 " rowSpan={1} colSpan={1}>Rectangle indicating the element's bounding rectangle.</td></tr><tr className><td className="entry" headers="topic-2636__4c337364-2569-465a-9b6d-bae73f2339d2__entry__1 topic-2636__4c337364-2569-465a-9b6d-bae73f2339d2__entry__2 "><code className="ph codeph">StepFailedException</code></td><td className="entry" headers="topic-2636__4c337364-2569-465a-9b6d-bae73f2339d2__entry__1 topic-2636__4c337364-2569-465a-9b6d-bae73f2339d2__entry__2 ">Throws an error if Katalon Studio cannot find the specified element.</td></tr></tbody></table> 

## Example

<div xmlns="http://www.w3.org/1999/xhtml" className="p"><pre className="pre codeblock"><code>import org.openqa.selenium.Rectangle as Rectangle{"\n"}Rectangle rect = Windows.getElementRect(findWindowsObject('Object Repository/Notepad/Edit')){"\n"}println String.format("{"{"} x: %d, y: %d, width: %d, height: %d {"}"}", rect.getX(), rect.getY(), rect.getWidth(), rect.getHeight())</code></pre></div>
