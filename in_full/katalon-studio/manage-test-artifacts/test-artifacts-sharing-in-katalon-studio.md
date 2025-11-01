---
hide_title: true
title: Test Artifacts Sharing in Katalon Studio
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="id" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Test Artifacts Sharing in <span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon Studio</span> 

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Test artifacts sharing allows you to import and export test   artifacts across Katalon Studio projects. These test artifacts   include test cases, test objects, profiles, and custom   keywords.</p> 

## Requirements

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">An active Katalon Studio Enterprise license. To       learn more about activating your licenses, you can refer to this       document: <a className="xref" href="/katalon-studio/get-started/activate-licenses">Activate         Katalon License</a>.</p></li></ul> 

## <a id="id_1" class="anchor_top_offset"/>Export test artifacts

<ol xmlns="http://www.w3.org/1999/xhtml" className="ol"><li className="li"><p className="p">From the main menu, <strong className="ph b">Tools &gt; Utility &gt; Export Test Artifact</strong>.</p><p className="p"><img className="image" width={400} src={useBaseUrl("/40f74f30-7f89-11ed-998d-0242cfbc79b5/ks-855-export-ta.png")} /></p></li><li className="li"><p className="p">In the <strong className="ph b">Export Test Artifacts</strong> window:</p><ul className="ul"><li className="li">Add the test cases, test objects, profiles, and/or custom keywords that you wish to export.</li><li className="li">Under <strong className="ph b">Export Location</strong>, select the destination folder for the exported file(s).</li></ul><p className="p"><img className="image" height={797} src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/import-export-test-artifact/export-test-artifacts.png")} width={497} /><br /><br /></p></li><li className="li"><p className="p">Click <strong className="ph b">OK</strong> to export the selected test artifacts.</p></li></ol> 

## <a id="id_2" class="anchor_top_offset"/>Import test artifacts

<div xmlns="http://www.w3.org/1999/xhtml" className="note note note_note"><span className="note__title">Note:</span> <ul className="ul"><li className="li"><p className="p">You can only import test artifacts exported from Katalon Studio. The format of the exported file name is <code className="ph codeph">shared-[timestamp].zip</code>.</p></li></ul></div>
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol"><li className="li"><p className="p">From the main menu, <strong className="ph b">Tools &gt; Utility &gt; Import Test Artifact</strong>.</p><p className="p"><img className="image" width={400} src={useBaseUrl("/40fc5840-7f89-11ed-998d-0242cfbc79b5/ks-855-import-ta.png")} /></p></li><li className="li"><p className="p">In the <strong className="ph b">Import Test Artifacts</strong> window, choose your desired file to import, test case import location, and test object import location.</p><p className="p"><img className="image" height={171} src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/import-export-test-artifact/import-test-artifact.png")} width={496} /><br /><br /></p></li><li className="li"><p className="p">Click <strong className="ph b">OK</strong>. Refresh the <span className="ph uicontrol">Tests Explorer</span> by right-clicking &gt; <strong className="ph b">Refresh</strong> to view them in the specified locations.</p></li></ol> 
