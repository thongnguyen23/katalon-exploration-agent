---
title: Link test execution with a TestOps release using command builder (Legacy)
---
import useBaseUrl from '@docusaurus/useBaseUrl';
import Reusable from '@site/src/reusable/Reusable.mdx';

<Reusable />


## Requirements

<p xmlns="http://www.w3.org/1999/xhtml" className="p">You have already configured TestOps integration. <a className="xref" href="#">Learn more</a>. </p> 

## <a id="id_2" class="anchor_top_offset"/>Create a new Release in Katalon TestOps

<p xmlns="http://www.w3.org/1999/xhtml" className="p">You can create a new Release or use an existing Release. See: <a className="xref" href="/katalon-platform/plan/create-and-edit-releases-in-testops">Create and edit releases in TestOps</a>.</p> 

## <a id="id_3" class="anchor_top_offset"/>Select a TestOps Release to generate command

<p xmlns="http://www.w3.org/1999/xhtml" className="p">In <strong className="ph b">Katalon Studio</strong>, open the <strong className="ph b">Command Generator</strong> and select a Test Suite that you want to execute in CLI.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">In the <strong className="ph b">Katalon TestOps</strong> section, select the release you want to link your execution with after running the test suite.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" src={useBaseUrl("/8b03f990-22b2-11ed-9930-0242fe3e4a3f/ks-generate-command-release-section.png")} alt="kse-generate-command-release-section" /></p> 
<div xmlns="http://www.w3.org/1999/xhtml" className="note note note_note"><span className="note__title">Note:</span> <ul className="ul"><li className="li"><p className="p">If you have not created any Releases in TestOps, it will be set as <strong className="ph b">Default Release</strong>.</p></li></ul></div>
<p xmlns="http://www.w3.org/1999/xhtml" className="p">After finishing the above steps, click on <strong className="ph b">Generate Command</strong> and copy it to the command line.</p> 

## <a id="id_4" class="anchor_top_offset"/>View linked execution and release in Katalon TestOps

<p xmlns="http://www.w3.org/1999/xhtml" className="p">After executing your test suite with CLI, sign in to <a className="xref j-external-link" href="https://testops.katalon.io/login" target="_blank">Katalon TestOps</a> and go to your project, then go to <span className="ph uicontrol">Planning</span> &gt; <span className="ph uicontrol">Releases</span>. You can view the list of all releases here. </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" src={useBaseUrl("/8b0495d0-22b2-11ed-9930-0242fe3e4a3f/kt-release-page.png")} alt="kte-june2022-releases-page" /></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Click on a release (e.g., the <strong className="ph b">7.6</strong> release) and select <span className="ph uicontrol">Test Runs</span> to view all test executions linked to the chosen Release.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" src={useBaseUrl("/8b035d50-22b2-11ed-9930-0242fe3e4a3f/kt-release-test-runs-page.png")} alt="kte-june2022-releases-test-runs-page" /></p> 
