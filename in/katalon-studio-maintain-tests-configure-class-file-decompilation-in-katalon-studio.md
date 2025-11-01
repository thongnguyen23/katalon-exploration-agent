---
hide_title: true
title: Configure class file decompilation in Katalon Studio
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="id" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Configure class file decompilation in Katalon Studio

<p xmlns="http://www.w3.org/1999/xhtml" className="p">As a precondition before debugging test scripts, you need to prepare and attach source code to a class file in Katalon Studio.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">You can read and interact with source code in previous versions by using the default feature of Eclipse Platform, Source Attachment. Katalon Studio decompiles class files automatically and directly. Particularly, Katalon finds, downloads, and attaches source code behind the scene; hence, you do not have to manually perform these steps.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">In case Katalon Studio fails to find the source attachment owing to the Internet connection or the <code className="ph codeph">jar</code> file not being found, it decompiles a class file and displays the decompiled source.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Katalon Class Decompiler is enabled by default for all Katalon Studio instances. This document gives you many additional configurations.</p> 

## <a id="id_1" class="anchor_top_offset"/>Use Class Decompiler for debug

<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Requirements</strong>:</p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">An active Katalon Studio Enterprise license</li><li className="li">Enabled Decompiler in Katalon <strong className="ph b">Preferences</strong> </li></ul> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">With <strong className="ph b">Katalon Class File Decompiler</strong>, you can always access a class file's source code to set a breakpoint for debugging test scripts. Learn about <a className="xref" href="/katalon-studio/debug-a-test-case/debug-a-test-case-in-katalon-studio#id_8">Debug Mode</a> in Katalon Studio.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/execute-a-test-case-or-a-test-suite/decompiler-introduction.png")} alt="decompiler-introduction" /><br /><br /></p> 

## <a id="id_2" class="anchor_top_offset"/>Configure Class Decompiler

<p xmlns="http://www.w3.org/1999/xhtml" className="p">For further configurations, open the Decompiler in Katalon Preferences:</p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">Windows: Go to <strong className="ph b">Windows</strong> &gt; <strong className="ph b">Preferences</strong> &gt; <strong className="ph b">Java</strong> &gt; <strong className="ph b">Decompiler</strong>.</li><li className="li">macOS: Go to <strong className="ph b">Katalon Studio</strong> &gt; <strong className="ph b">Preferences</strong> &gt; <strong className="ph b">Java</strong> &gt; <strong className="ph b">Decompiler</strong>.</li></ul> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/class-decompiler/decompiler.png")} alt="decompiler-introduction" /><br /><br /> </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Katalon Studio supports the following Decompilers, including CFR, FernFlower (selected by default), Jad-Core, JD, and Procyon.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/class-decompiler/decompilers.png")} alt="decompiler-introduction" /><br /><br /> </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <strong className="ph b">Disable Class Decompiler</strong> </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">To turn off <strong className="ph b">Katalon Class Decompiler</strong>, you need to set <strong className="ph b">Class File Viewer</strong> to the default viewer in <strong className="ph b">Preferences</strong> &gt; <strong className="ph b">General</strong> &gt; <strong className="ph b">Editors</strong> &gt; <strong className="ph b">File Associations</strong>.</p> 
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol"><li className="li">For "*<em className="ph i">.class</em>" and "*<em className="ph i">.class without source</em>" in <strong className="ph b">File Types</strong>, select "<em className="ph i">Class File Viewer</em>" in <strong className="ph b">Associated Editors</strong>.</li><li className="li">Click <strong className="ph b">Default</strong> to set it as the default viewer.</li><li className="li">     <p className="p">Click <strong className="ph b">Apply and Close</strong>.</p>     <p className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/class-decompiler/switch.png")} alt="decompiler-introduction" /><br /><br />     </p>   </li></ol> 
