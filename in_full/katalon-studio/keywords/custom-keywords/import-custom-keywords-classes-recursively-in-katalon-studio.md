---
hide_title: true
title: Import Custom Keywords classes recursively in Katalon Studio
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="id" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Import Custom Keywords classes recursively in <span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon Studio</span> 

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Hypothetically, you want to call a Custom Keyword within a Custom Keyword that is defined in another class. Check out the code below for a sample implementation.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/import-custom-keywords-classes-recursively/f5uxhyxe7z65.png")} /><br /><br /></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Keywords/my.a/Greeting.groovy</p> 
<pre xmlns="http://www.w3.org/1999/xhtml" className="pre codeblock"><code>package my.aimport com.kms.katalon.core.annotation.Keywordclass Greeting {"{"} @Keyword def greet(String someone) {"{"} return my.b.AI.sayHelloTo(someone) {"}"}{"}"}{"\n"}</code></pre> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Keywords/my.b/AI.groovy</p> 
<pre xmlns="http://www.w3.org/1999/xhtml" className="pre codeblock"><code>package my.bclass AI {"{"} static def sayHelloTo(String someone) {"{"} return "Hello, ${"{"}someone{"}"}." {"}"}{"}"}{"\n"}</code></pre> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">TC1:</p> 
<pre xmlns="http://www.w3.org/1999/xhtml" className="pre codeblock"><code>import com.kms.katalon.core.webui.keyword.WebUiBuiltInKeywords as WebUIdef str = CustomKeywords.'my.a.Greeting.greet'("Drunda")WebUI.comment("&gt;&gt;&gt; ${"{"}str{"}"}"){"\n"}</code></pre> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">The TC1 ran fine:</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/import-custom-keywords-classes-recursively/30qrty5tymg5.png")} /><br /><br /></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><em className="ph i">Credit to <a className="xref j-external-link" href="https://forum.katalon.com/discussion/6971/importing-custom-keywords-classes-recursively-within-a-custom-keyword#Comment_16124" target="_blank">kazurayam</a> </em></p> 
