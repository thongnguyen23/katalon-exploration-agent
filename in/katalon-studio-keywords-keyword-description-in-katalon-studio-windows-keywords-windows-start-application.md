---
hide_title: true
title: '[Windows] Start Application'
---

# <a id="topic-2364" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>[Windows] Start Application


## Description

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Start the Windows driver and the Windows application with the given absolute path.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Keyword name: <code className="ph codeph">startApplication</code></p> 

## Parameters

<table xmlns="http://www.w3.org/1999/xhtml" className="table anchor_top_offset" id="topic-2364__1313d459-6998-482a-a91f-696d9d02f90e"><caption /><colgroup><col style={{width: '20%'}} /><col style={{width: '20%'}} /><col style={{width: '20%'}} /><col style={{width: '40%'}} /></colgroup><thead className="thead"><tr className><th className="entry anchor_top_offset" id="topic-2364__1313d459-6998-482a-a91f-696d9d02f90e__entry__1">Parameter </th><th className="entry anchor_top_offset" id="topic-2364__1313d459-6998-482a-a91f-696d9d02f90e__entry__2">Parameter Type</th><th className="entry anchor_top_offset" id="topic-2364__1313d459-6998-482a-a91f-696d9d02f90e__entry__3">Required</th><th className="entry anchor_top_offset" id="topic-2364__1313d459-6998-482a-a91f-696d9d02f90e__entry__4">Description</th></tr></thead><tbody className="tbody"><tr className><td className="entry" headers="topic-2364__1313d459-6998-482a-a91f-696d9d02f90e__entry__1 topic-2364__1313d459-6998-482a-a91f-696d9d02f90e__entry__2 topic-2364__1313d459-6998-482a-a91f-696d9d02f90e__entry__3 topic-2364__1313d459-6998-482a-a91f-696d9d02f90e__entry__4 " rowSpan={1} colSpan={1}><code className="ph codeph">appFile</code></td><td className="entry" headers="topic-2364__1313d459-6998-482a-a91f-696d9d02f90e__entry__1 topic-2364__1313d459-6998-482a-a91f-696d9d02f90e__entry__2 topic-2364__1313d459-6998-482a-a91f-696d9d02f90e__entry__3 topic-2364__1313d459-6998-482a-a91f-696d9d02f90e__entry__4 " rowSpan={1} colSpan={1}>String</td><td className="entry" headers="topic-2364__1313d459-6998-482a-a91f-696d9d02f90e__entry__1 topic-2364__1313d459-6998-482a-a91f-696d9d02f90e__entry__2 topic-2364__1313d459-6998-482a-a91f-696d9d02f90e__entry__3 topic-2364__1313d459-6998-482a-a91f-696d9d02f90e__entry__4 " rowSpan={1} colSpan={1}>Yes</td><td className="entry" headers="topic-2364__1313d459-6998-482a-a91f-696d9d02f90e__entry__1 topic-2364__1313d459-6998-482a-a91f-696d9d02f90e__entry__2 topic-2364__1313d459-6998-482a-a91f-696d9d02f90e__entry__3 topic-2364__1313d459-6998-482a-a91f-696d9d02f90e__entry__4 " rowSpan={1} colSpan={1}>The absolute path to the Windows Executable File (*.exe) of the test machine.</td></tr></tbody></table> 

## Example

<div xmlns="http://www.w3.org/1999/xhtml" className="p"><pre className="pre codeblock"><code>"Start the note pad application"{"\n"}Windows.startApplication('C:\\Windows\\System32\\notepad.exe')</code></pre></div>
