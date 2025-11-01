---
hide_title: true
title: '[Mobile] Verify Image Present'
---

# <a id="id_0" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>[Mobile] Verify Image Present

<div xmlns="http://www.w3.org/1999/xhtml" className="note important note_important"><span className="note__title">Important:</span> <ul className="ul"><li className="li">Katalon Studio Enterprise license.</li></ul></div>

## <a id="id_0__id_1" class="anchor_top_offset"/>Description

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Verify the given image that presents on the device screen or not.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Keyword name: <code className="ph codeph">Mobile.verifyImagePresent</code></p> 

## Parameters

<table xmlns="http://www.w3.org/1999/xhtml" className="table anchor_top_offset" id="id_0__83aaccf5-8beb-46bb-a702-bfdc4514632a"><caption /><colgroup><col style={{width: '20%'}} /><col style={{width: '20%'}} /><col style={{width: '20%'}} /><col style={{width: '40%'}} /></colgroup><thead className="thead"><tr className><th className="entry anchor_top_offset" id="id_0__83aaccf5-8beb-46bb-a702-bfdc4514632a__entry__1">Parameters</th><th className="entry anchor_top_offset" id="id_0__83aaccf5-8beb-46bb-a702-bfdc4514632a__entry__2">Parameter Type</th><th className="entry anchor_top_offset" id="id_0__83aaccf5-8beb-46bb-a702-bfdc4514632a__entry__3">Required</th><th className="entry anchor_top_offset" id="id_0__83aaccf5-8beb-46bb-a702-bfdc4514632a__entry__4">Description</th></tr></thead><tbody className="tbody"><tr className><td className="entry" headers="id_0__83aaccf5-8beb-46bb-a702-bfdc4514632a__entry__1 id_0__83aaccf5-8beb-46bb-a702-bfdc4514632a__entry__2 id_0__83aaccf5-8beb-46bb-a702-bfdc4514632a__entry__3 id_0__83aaccf5-8beb-46bb-a702-bfdc4514632a__entry__4 ">imageFilePath</td><td className="entry" headers="id_0__83aaccf5-8beb-46bb-a702-bfdc4514632a__entry__1 id_0__83aaccf5-8beb-46bb-a702-bfdc4514632a__entry__2 id_0__83aaccf5-8beb-46bb-a702-bfdc4514632a__entry__3 id_0__83aaccf5-8beb-46bb-a702-bfdc4514632a__entry__4 ">String</td><td className="entry" headers="id_0__83aaccf5-8beb-46bb-a702-bfdc4514632a__entry__1 id_0__83aaccf5-8beb-46bb-a702-bfdc4514632a__entry__2 id_0__83aaccf5-8beb-46bb-a702-bfdc4514632a__entry__3 id_0__83aaccf5-8beb-46bb-a702-bfdc4514632a__entry__4 ">Yes</td><td className="entry" headers="id_0__83aaccf5-8beb-46bb-a702-bfdc4514632a__entry__1 id_0__83aaccf5-8beb-46bb-a702-bfdc4514632a__entry__2 id_0__83aaccf5-8beb-46bb-a702-bfdc4514632a__entry__3 id_0__83aaccf5-8beb-46bb-a702-bfdc4514632a__entry__4 ">Absolute path of the image</td></tr></tbody></table> 

## Returns

<p xmlns="http://www.w3.org/1999/xhtml" className="p"><strong className="ph b">true</strong> if the image presents. Otherwise, false.</p> 

## Example

You want to check whether the image specified below (`image.png`) is currently visible on the mobile screen:

<div xmlns="http://www.w3.org/1999/xhtml" className="p"><pre className="pre codeblock"><code>boolean isPresent = Mobile.verifyImagePresent("/Users/myaccount/Desktop/image.png"){"\n"}</code></pre></div>
