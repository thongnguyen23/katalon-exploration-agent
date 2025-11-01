---
hide_title: true
title: '[Mobile] Tap on Image'
---

# <a id="id_0" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>[Mobile] Tap on Image

<div xmlns="http://www.w3.org/1999/xhtml" className="note note note_note"><span className="note__title">Note:</span> <ul className="ul"><li className="li"><p className="p">Katalon Studio Enterprise license.</p></li><li className="li"><p className="p">The <code className="ph codeph">tapOnImage</code> keyword is not supported in headless browser mode.</p></li></ul></div>

## Description

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Simulate toggling airplane mode on mobile devices. Support iOS real devices and Android emulators.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Keyword name: <code className="ph codeph">Mobile.tapOnImage</code></p> 

## <a id="id_0__id_2" class="anchor_top_offset"/> Parameters

<table xmlns="http://www.w3.org/1999/xhtml" className="table anchor_top_offset" id="id_0__f06a3eea-320e-4f62-923e-2a1be50a1fdb"><caption /><colgroup><col style={{width: '20%'}} /><col style={{width: '20%'}} /><col style={{width: '20%'}} /><col style={{width: '40%'}} /></colgroup><thead className="thead"><tr className><th className="entry anchor_top_offset" id="id_0__f06a3eea-320e-4f62-923e-2a1be50a1fdb__entry__1">Param</th><th className="entry anchor_top_offset" id="id_0__f06a3eea-320e-4f62-923e-2a1be50a1fdb__entry__2">Param Type</th><th className="entry anchor_top_offset" id="id_0__f06a3eea-320e-4f62-923e-2a1be50a1fdb__entry__3">Required</th><th className="entry anchor_top_offset" id="id_0__f06a3eea-320e-4f62-923e-2a1be50a1fdb__entry__4">Description</th></tr></thead><tbody className="tbody"><tr className><td className="entry" headers="id_0__f06a3eea-320e-4f62-923e-2a1be50a1fdb__entry__1 id_0__f06a3eea-320e-4f62-923e-2a1be50a1fdb__entry__2 id_0__f06a3eea-320e-4f62-923e-2a1be50a1fdb__entry__3 id_0__f06a3eea-320e-4f62-923e-2a1be50a1fdb__entry__4 ">imageFilePath</td><td className="entry" headers="id_0__f06a3eea-320e-4f62-923e-2a1be50a1fdb__entry__1 id_0__f06a3eea-320e-4f62-923e-2a1be50a1fdb__entry__2 id_0__f06a3eea-320e-4f62-923e-2a1be50a1fdb__entry__3 id_0__f06a3eea-320e-4f62-923e-2a1be50a1fdb__entry__4 ">String</td><td className="entry" headers="id_0__f06a3eea-320e-4f62-923e-2a1be50a1fdb__entry__1 id_0__f06a3eea-320e-4f62-923e-2a1be50a1fdb__entry__2 id_0__f06a3eea-320e-4f62-923e-2a1be50a1fdb__entry__3 id_0__f06a3eea-320e-4f62-923e-2a1be50a1fdb__entry__4 ">Yes</td><td className="entry" headers="id_0__f06a3eea-320e-4f62-923e-2a1be50a1fdb__entry__1 id_0__f06a3eea-320e-4f62-923e-2a1be50a1fdb__entry__2 id_0__f06a3eea-320e-4f62-923e-2a1be50a1fdb__entry__3 id_0__f06a3eea-320e-4f62-923e-2a1be50a1fdb__entry__4 ">Absolute path of the image</td></tr><tr className><td className="entry" headers="id_0__f06a3eea-320e-4f62-923e-2a1be50a1fdb__entry__1 id_0__f06a3eea-320e-4f62-923e-2a1be50a1fdb__entry__2 id_0__f06a3eea-320e-4f62-923e-2a1be50a1fdb__entry__3 id_0__f06a3eea-320e-4f62-923e-2a1be50a1fdb__entry__4 ">flowControl</td><td className="entry" headers="id_0__f06a3eea-320e-4f62-923e-2a1be50a1fdb__entry__1 id_0__f06a3eea-320e-4f62-923e-2a1be50a1fdb__entry__2 id_0__f06a3eea-320e-4f62-923e-2a1be50a1fdb__entry__3 id_0__f06a3eea-320e-4f62-923e-2a1be50a1fdb__entry__4 ">FailureHandling</td><td className="entry" headers="id_0__f06a3eea-320e-4f62-923e-2a1be50a1fdb__entry__1 id_0__f06a3eea-320e-4f62-923e-2a1be50a1fdb__entry__2 id_0__f06a3eea-320e-4f62-923e-2a1be50a1fdb__entry__3 id_0__f06a3eea-320e-4f62-923e-2a1be50a1fdb__entry__4 ">Optional</td><td className="entry" headers="id_0__f06a3eea-320e-4f62-923e-2a1be50a1fdb__entry__1 id_0__f06a3eea-320e-4f62-923e-2a1be50a1fdb__entry__2 id_0__f06a3eea-320e-4f62-923e-2a1be50a1fdb__entry__3 id_0__f06a3eea-320e-4f62-923e-2a1be50a1fdb__entry__4 ">Specify <a className="xref" href="/katalon-studio/maintain-tests/configure-failure-handling-settings-in-katalon-studio#id_1">failure handling</a> schema to determine whether the execution should be allowed to continue or stop.</td></tr></tbody></table> 

## Returns

<p xmlns="http://www.w3.org/1999/xhtml" className="p"><strong className="ph b">true</strong> if the image presents. Otherwise, false.</p> 

## <a id="id_0__id_1" class="anchor_top_offset"/>Example

You want to visually search for a UI element that matches the given image file, and tap on it when found:

<pre xmlns="http://www.w3.org/1999/xhtml" className="pre codeblock"><code>Mobile.tapOnImage("/Users/myaccount/Desktop/image.png"){"\n"}</code></pre> 
