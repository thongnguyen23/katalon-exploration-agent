---
hide_title: true
title: Private Plugins in Katalon Studio
---

# <a id="id_5" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Private Plugins in <span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon Studio</span> 

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Private plugins are Katalon plugins that are developed for   private use. With private plugins supported, you can build,   distribute, install, and use your plugins without publishing them   on Store for public access.</p> 

## Requirements

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><span className="ph">Katalon Studio</span> version 7.0.0 onwards.</li><li className="li">An active Katalon Studio Enterprise license. To learn more     about activating licenses, you can refer to this document: <a className="xref" href="/katalon-studio/get-started/activate-licenses">Activate       Katalon licenses</a>.</li></ul> 

## <a id="id_6" class="anchor_top_offset"/>Build Private Plugins

<p xmlns="http://www.w3.org/1999/xhtml" className="p">If you don't know how to build a plugin that can be used in   <span className="ph">Katalon Studio</span>,  refer to the documents on how to develop <a className="xref" href="/katalon-platform/plugins-and-add-ons/katalon-store/katalon-studio-plugins/create-your-first-katalon-studio-plugin">platform     plugins</a> and <a className="xref" href="/katalon-platform/plugins-and-add-ons/katalon-store/katalon-studio-plugins/how-to-develop-a-custom-keywords-plugin-in-katalon-studio">custom     keywords plugins</a>.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">If you have already written custom keywords, then code reuse   across projects can be achieved easily by distributing the keywords   as plugins. This utility is especially helpful when you need to   test a set of products that frequently encounter recurring   problems. Before, you would have to copy and paste every custom   keyword class from projects to projects. Whenever the   implementation of the custom keyword changes, you would need to   update that change in all projects. Now, you can deploy and install   custom keyword plugins through only a few commands and manual   steps.</p> 

## <a id="id_7" class="anchor_top_offset"/>Store Private Plugins

<p xmlns="http://www.w3.org/1999/xhtml" className="p">You need to store private plugins in the   <code className="ph codeph">&lt;project_name&gt;/Plugins</code> folder for <span className="ph">Katalon Studio</span>   to treat them as local plugins. There are two types of plugins:   <strong className="ph b">Platform</strong> and <strong className="ph b">Custom Keyword</strong>.   Noticeably, <strong className="ph b">Platform</strong> plugins need storing in the   <code className="ph codeph">&lt;project_name&gt;/Plugins/platform</code> folder.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Below is the structure of the <code className="ph codeph">Plugins</code> folder:</p> 
<pre xmlns="http://www.w3.org/1999/xhtml" className="pre codeblock"><code>Plugins{"\n"}{"\n"} |{"\n"}{"\n"} |___ platform{"\n"}{"\n"}{"         "}|___ IDE plugin 1.jar{"\n"}{"\n"}{"         "}|___ IDE plugin 2.jar{"\n"}{"\n"}{"         "}|___ ....{"\n"}{"\n"}{"         "}|___ IDE plugin n.jar{"\n"}{"\n"} |___ Custom keyword plugin 1.jar{"\n"}{"\n"} |___ Custom keyword plugin 2.jar{"\n"}{"\n"} |___ ...{"\n"}{"\n"} |___ Custom keyword plugin n.jar{"\n"}</code></pre> 

## <a id="id_8" class="anchor_top_offset"/>Use Private Plugins in <span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon Studio</span> 

<p xmlns="http://www.w3.org/1999/xhtml" className="p">In <strong className="ph b">Project &gt; Settings &gt; Plugins</strong>, select one of the following options:</p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"> <strong className="ph b">Katalon Store and Local</strong>: <span className="ph">Katalon Studio</span> will install plugins from the Store and the Plugins folder of each project.</li><li className="li"> <strong className="ph b">Local</strong>: <span className="ph">Katalon Studio</span> will install plugins from the Plugins folder only.</li></ul> 
<div xmlns="http://www.w3.org/1999/xhtml" className="note note note_note"><span className="note__title">Note:</span> <ul className="ul"><li className="li">To install plugins offline, see <a className="xref" href="/katalon-platform/plugins-and-add-ons/katalon-store/katalon-studio-plugins/installing-plugin-offline-in-katalon-studio">Offline Plugin Installation</a>.</li></ul></div>
