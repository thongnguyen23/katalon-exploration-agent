---
hide_title: true
title: '[Windows] Get Driver'
---

# <a id="topic-7684" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>[Windows] Get Driver


## Description

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Get the current Windows Driver.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Keyword name: <code className="ph codeph">getDriver</code></p> 

## Returns

<table xmlns="http://www.w3.org/1999/xhtml" className="table anchor_top_offset" id="topic-7684__110306a3-b3c5-4eff-bbdf-b5daa9e603ab"><caption /><colgroup><col style={{width: '33.33333333333333%'}} /><col style={{width: '66.66666666666666%'}} /></colgroup><thead className="thead"><tr className><th className="entry anchor_top_offset" id="topic-7684__110306a3-b3c5-4eff-bbdf-b5daa9e603ab__entry__1">Parameter Type</th><th className="entry anchor_top_offset" id="topic-7684__110306a3-b3c5-4eff-bbdf-b5daa9e603ab__entry__2">Description</th></tr></thead><tbody className="tbody"><tr className><td className="entry" headers="topic-7684__110306a3-b3c5-4eff-bbdf-b5daa9e603ab__entry__1 topic-7684__110306a3-b3c5-4eff-bbdf-b5daa9e603ab__entry__2 " rowSpan={1} colSpan={1}><code className="ph codeph">WindowsDriver</code></td><td className="entry" headers="topic-7684__110306a3-b3c5-4eff-bbdf-b5daa9e603ab__entry__1 topic-7684__110306a3-b3c5-4eff-bbdf-b5daa9e603ab__entry__2 " rowSpan={1} colSpan={1}>The current Windows Driver.</td></tr></tbody></table> 

## Example

<div xmlns="http://www.w3.org/1999/xhtml" className="p"><pre className="pre codeblock"><code>"Start the note pad application"{"\n"}Windows.startApplication('C:\\Windows\\System32\\notepad.exe'){"\n"}{"\n"}"Get the application title"{"\n"}Windows.getDriver().getTitle()</code></pre></div>
