---
hide_title: true
title: Custom Keywords Refactoring in Katalon Studio
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="id" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Custom Keywords Refactoring in <span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon Studio</span> 

<p xmlns="http://www.w3.org/1999/xhtml" className="p">When you move a custom keyword from a package to another one, Katalon Studio updates the new package and keyword identifier in test scripts accordingly. You can refactor custom keywords in both test cases and the Custom Keyword section.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Here is an example:</p> 
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol"><li className="li"><p className="p">Open <a className="xref" href="/katalon-studio/get-started/sample-projects/data-driven-test/sample-webui-project-with-data-driven-testing-shopping-cart-sample-in-katalon-studio">the shopping cart sample project</a> and any test case.</p></li><li className="li"><p className="p">Create a new package in the Keywords folder. Then drag and drop the <code className="ph codeph">Login</code> keyword from <code className="ph codeph">Simple</code> to the newly created package.</p></li><li className="li"><p className="p">Re-open the test case and observe. Katalon Studio has updated the package and keyword identifier in the test scripts accordingly.</p></li></ol> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><strong className="ph b">Before drag-and-drop</strong></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/custom-keyword-refactor/package-bf.png")} width={600} /><br /><br /></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/custom-keyword-refactor/identifier-bf.png")} width={600} /><br /><br /></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><strong className="ph b">After drag-and-drop</strong></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/custom-keyword-refactor/package-aft.png")} width={600} /><br /><br /></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/custom-keyword-refactor/identifier-aft.png")} width={600} /><br /><br /></p> 
