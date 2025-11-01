---
hide_title: true
title: Refactor test objects in Katalon Studio
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="id" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Refactor test objects in Katalon Studio

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Test object refactoring is an ability to view and manage the unused test objects. For a significant and long-term project, refactoring is critical to keeping your object repository up-to-date and organized.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">A test object is only counted as "used" when it's referenced by the method  <code className="ph codeph">findTestObject("test object ID")</code>. An unused test object is any Web, Web Service, Mobile, Windows test object that you haven't referred to in any test case, test listener, or keyword.</p> 
<div xmlns="http://www.w3.org/1999/xhtml" className="note important note_important"><span className="note__title">Important:</span> <p className="p">An active <span className="ph">Katalon Studio Enterprise</span> license.</p></div>
<p xmlns="http://www.w3.org/1999/xhtml" className="p">To retrieve all unused test objects, go to <span className="ph uicontrol">Tools</span> &gt; <span className="ph uicontrol">Test Object</span> &gt; <span className="ph uicontrol">Show unused Test Objects</span>.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <img className="image" height={141} src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/test-object-refactor/option.png")} width={486} /><br /><br /> </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">The <span className="ph uicontrol">Unused Test Objects Report</span> displays a list of test objects that you haven't used yet.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <img className="image" height={254} src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/test-object-refactor/a.png")} width={745} /><br /><br /> </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">You can double-click to view the object's details. You can decide whether or not to remove the outdated and obsolete objects.</p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">To remove all unused objects: Click <span className="ph uicontrol">Delete all</span>. In case you want to maintain the objects for other collaborators, you can export the objects  with <a className="xref" href="/katalon-studio/manage-test-artifacts/test-artifacts-sharing-in-katalon-studio">Test Artifact Sharing</a>.</li><li className="li"><p className="p">To removed individual objects, locate the objects in test explorer, right-click and select <span className="ph uicontrol">Delete</span>.</p></li></ul> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <img className="image" height={552} src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/test-object-refactor/remove-one.png")} width={636} /><br /><br /> </p> 

## <a id="id_1" class="anchor_top_offset"/>Object references

<p xmlns="http://www.w3.org/1999/xhtml" className="p">You can see where a test object has been used by viewing its references. Right-click the object and select <span className="ph uicontrol">Show References</span>. Katalon Studio searches for that object and returns its references. Double-click highlighted reference to go to the corresponding place in that project.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/test-object-refactor/830-object-reference.png")} /><br /><br /></p> 
