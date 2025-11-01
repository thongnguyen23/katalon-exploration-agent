---
hide_title: true
title: '[Cucumber] Run Feature Folder'
---

# <a id="id" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>[Cucumber] Run Feature Folder


## Description

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Execute multiple feature files stored in the same features folder.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Keyword name: <code className="ph codeph">runFeatureFolder</code></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Keyword syntax: <code className="ph codeph">runFeatureFolder(folderRelativePath, flowControl)</code></p> 

## Parameter

<div xmlns="http://www.w3.org/1999/xhtml" className="p"><table className="table anchor_top_offset" id="id__b9a2ac67-782c-4eb0-9158-891f7e4dd112"><caption /><colgroup><col style={{width: '25%'}} /><col style={{width: '25%'}} /><col style={{width: '25%'}} /><col style={{width: '25%'}} /></colgroup><thead className="thead"><tr className><th className="entry anchor_top_offset" id="id__b9a2ac67-782c-4eb0-9158-891f7e4dd112__entry__1">Parameter</th><th className="entry anchor_top_offset" id="id__b9a2ac67-782c-4eb0-9158-891f7e4dd112__entry__2">Parameter Type</th><th className="entry anchor_top_offset" id="id__b9a2ac67-782c-4eb0-9158-891f7e4dd112__entry__3">Required</th><th className="entry anchor_top_offset" id="id__b9a2ac67-782c-4eb0-9158-891f7e4dd112__entry__4">Description</th></tr></thead><tbody className="tbody"><tr className><td className="entry" headers="id__b9a2ac67-782c-4eb0-9158-891f7e4dd112__entry__1 id__b9a2ac67-782c-4eb0-9158-891f7e4dd112__entry__2 id__b9a2ac67-782c-4eb0-9158-891f7e4dd112__entry__3 id__b9a2ac67-782c-4eb0-9158-891f7e4dd112__entry__4 ">folderRelativePath</td><td className="entry" headers="id__b9a2ac67-782c-4eb0-9158-891f7e4dd112__entry__1 id__b9a2ac67-782c-4eb0-9158-891f7e4dd112__entry__2 id__b9a2ac67-782c-4eb0-9158-891f7e4dd112__entry__3 id__b9a2ac67-782c-4eb0-9158-891f7e4dd112__entry__4 ">String</td><td className="entry" headers="id__b9a2ac67-782c-4eb0-9158-891f7e4dd112__entry__1 id__b9a2ac67-782c-4eb0-9158-891f7e4dd112__entry__2 id__b9a2ac67-782c-4eb0-9158-891f7e4dd112__entry__3 id__b9a2ac67-782c-4eb0-9158-891f7e4dd112__entry__4 ">Yes</td><td className="entry" headers="id__b9a2ac67-782c-4eb0-9158-891f7e4dd112__entry__1 id__b9a2ac67-782c-4eb0-9158-891f7e4dd112__entry__2 id__b9a2ac67-782c-4eb0-9158-891f7e4dd112__entry__3 id__b9a2ac67-782c-4eb0-9158-891f7e4dd112__entry__4 ">The folder relative path starts from the current project location.</td></tr><tr className><td className="entry" headers="id__b9a2ac67-782c-4eb0-9158-891f7e4dd112__entry__1 id__b9a2ac67-782c-4eb0-9158-891f7e4dd112__entry__2 id__b9a2ac67-782c-4eb0-9158-891f7e4dd112__entry__3 id__b9a2ac67-782c-4eb0-9158-891f7e4dd112__entry__4 ">flowControl</td><td className="entry" headers="id__b9a2ac67-782c-4eb0-9158-891f7e4dd112__entry__1 id__b9a2ac67-782c-4eb0-9158-891f7e4dd112__entry__2 id__b9a2ac67-782c-4eb0-9158-891f7e4dd112__entry__3 id__b9a2ac67-782c-4eb0-9158-891f7e4dd112__entry__4 ">FailureHandling</td><td className="entry" headers="id__b9a2ac67-782c-4eb0-9158-891f7e4dd112__entry__1 id__b9a2ac67-782c-4eb0-9158-891f7e4dd112__entry__2 id__b9a2ac67-782c-4eb0-9158-891f7e4dd112__entry__3 id__b9a2ac67-782c-4eb0-9158-891f7e4dd112__entry__4 ">Optional</td><td className="entry" headers="id__b9a2ac67-782c-4eb0-9158-891f7e4dd112__entry__1 id__b9a2ac67-782c-4eb0-9158-891f7e4dd112__entry__2 id__b9a2ac67-782c-4eb0-9158-891f7e4dd112__entry__3 id__b9a2ac67-782c-4eb0-9158-891f7e4dd112__entry__4 ">Controls the execution flow if the step fails. Specify <a className="xref" href="/katalon-studio/maintain-tests/configure-failure-handling-settings-in-katalon-studio">failure handling</a> schema to determine whether the execution should be allowed to continue or stop.</td></tr></tbody></table></div>

## Returns

<p xmlns="http://www.w3.org/1999/xhtml" className="p">An instance of <code className="ph codeph">CucumberRunnerResult</code> that includes the status of keyword and report folder location.</p> 

## Example

<div xmlns="http://www.w3.org/1999/xhtml" className="p"><pre className="pre codeblock"><code>CucumberKW.runFeatureFolder('Include/features/New Feature Folder'){"\n"}</code></pre></div>
