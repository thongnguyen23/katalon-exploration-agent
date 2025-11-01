---
hide_title: true
title: '[Cucumber] Run Feature File'
---

# <a id="id" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>[Cucumber] Run Feature File


## Description

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Execute a single Feature File.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Keyword name: <code className="ph codeph">runFeatureFile</code></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Keyword syntax: <code className="ph codeph">runFeatureFile(relativeFilePath, flowControl)</code></p> 

## Parameters

<div xmlns="http://www.w3.org/1999/xhtml" className="p"><table className="table anchor_top_offset" id="id__4b4ad339-824e-4733-9ed0-6d95eee844e3"><caption /><colgroup><col style={{width: '25%'}} /><col style={{width: '25%'}} /><col style={{width: '25%'}} /><col style={{width: '25%'}} /></colgroup><thead className="thead"><tr className><th className="entry anchor_top_offset" id="id__4b4ad339-824e-4733-9ed0-6d95eee844e3__entry__1">Parameter</th><th className="entry anchor_top_offset" id="id__4b4ad339-824e-4733-9ed0-6d95eee844e3__entry__2">Parameter Type</th><th className="entry anchor_top_offset" id="id__4b4ad339-824e-4733-9ed0-6d95eee844e3__entry__3">Required</th><th className="entry anchor_top_offset" id="id__4b4ad339-824e-4733-9ed0-6d95eee844e3__entry__4">Description</th></tr></thead><tbody className="tbody"><tr className><td className="entry" headers="id__4b4ad339-824e-4733-9ed0-6d95eee844e3__entry__1 id__4b4ad339-824e-4733-9ed0-6d95eee844e3__entry__2 id__4b4ad339-824e-4733-9ed0-6d95eee844e3__entry__3 id__4b4ad339-824e-4733-9ed0-6d95eee844e3__entry__4 ">relativeFilePath</td><td className="entry" headers="id__4b4ad339-824e-4733-9ed0-6d95eee844e3__entry__1 id__4b4ad339-824e-4733-9ed0-6d95eee844e3__entry__2 id__4b4ad339-824e-4733-9ed0-6d95eee844e3__entry__3 id__4b4ad339-824e-4733-9ed0-6d95eee844e3__entry__4 ">String</td><td className="entry" headers="id__4b4ad339-824e-4733-9ed0-6d95eee844e3__entry__1 id__4b4ad339-824e-4733-9ed0-6d95eee844e3__entry__2 id__4b4ad339-824e-4733-9ed0-6d95eee844e3__entry__3 id__4b4ad339-824e-4733-9ed0-6d95eee844e3__entry__4 ">Yes</td><td className="entry" headers="id__4b4ad339-824e-4733-9ed0-6d95eee844e3__entry__1 id__4b4ad339-824e-4733-9ed0-6d95eee844e3__entry__2 id__4b4ad339-824e-4733-9ed0-6d95eee844e3__entry__3 id__4b4ad339-824e-4733-9ed0-6d95eee844e3__entry__4 ">A relative file path of the feature file.</td></tr><tr className><td className="entry" headers="id__4b4ad339-824e-4733-9ed0-6d95eee844e3__entry__1 id__4b4ad339-824e-4733-9ed0-6d95eee844e3__entry__2 id__4b4ad339-824e-4733-9ed0-6d95eee844e3__entry__3 id__4b4ad339-824e-4733-9ed0-6d95eee844e3__entry__4 ">flowControl</td><td className="entry" headers="id__4b4ad339-824e-4733-9ed0-6d95eee844e3__entry__1 id__4b4ad339-824e-4733-9ed0-6d95eee844e3__entry__2 id__4b4ad339-824e-4733-9ed0-6d95eee844e3__entry__3 id__4b4ad339-824e-4733-9ed0-6d95eee844e3__entry__4 ">FailureHandling</td><td className="entry" headers="id__4b4ad339-824e-4733-9ed0-6d95eee844e3__entry__1 id__4b4ad339-824e-4733-9ed0-6d95eee844e3__entry__2 id__4b4ad339-824e-4733-9ed0-6d95eee844e3__entry__3 id__4b4ad339-824e-4733-9ed0-6d95eee844e3__entry__4 ">Optional</td><td className="entry" headers="id__4b4ad339-824e-4733-9ed0-6d95eee844e3__entry__1 id__4b4ad339-824e-4733-9ed0-6d95eee844e3__entry__2 id__4b4ad339-824e-4733-9ed0-6d95eee844e3__entry__3 id__4b4ad339-824e-4733-9ed0-6d95eee844e3__entry__4 ">Controls the execution flow if the step fails. Specify <a className="xref" href="/katalon-studio/maintain-tests/configure-failure-handling-settings-in-katalon-studio">failure handling</a> schema to determine whether the execution should be allowed to continue or stop.</td></tr></tbody></table></div>

## Returns

<p xmlns="http://www.w3.org/1999/xhtml" className="p">An instance of <code className="ph codeph">CucumberRunnerResult</code> that includes the status of the keyword and report folder location.</p> 

## Example

<div xmlns="http://www.w3.org/1999/xhtml" className="p"><pre className="pre codeblock"><code>CucumberKW.runFeatureFile('Include/features/New Feature File.feature'){"\n"}</code></pre></div>
