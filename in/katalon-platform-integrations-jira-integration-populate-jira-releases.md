---
title: Populate Jira releases (Legacy)
---
import useBaseUrl from '@docusaurus/useBaseUrl';
import Reusable from '@site/src/reusable/Reusable.mdx';

<Reusable />

<p xmlns="http://www.w3.org/1999/xhtml" className="p"><span className="ph">Katalon TestOps</span> allows you to populate Jira releases for test planning and management. Depending on your use case, you can do this in two ways:</p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">Create a new TestOps release linked to a Jira release. This method allows you to import a Jira release of any status whenever you create a new release in <span className="ph">Katalon TestOps</span>.</li></ul> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">OR</p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">Populate unreleased Jira releases. This method allows you to import all of the <em className="ph i">unreleased</em> releases from a Jira project to <span className="ph">Katalon TestOps</span>.</li></ul> 

## Requirements

<div xmlns="http://www.w3.org/1999/xhtml" className="p"><ul className="ul"><li className="li"><p className="p">You have enabled Jira integration in <span className="ph">Katalon TestOps</span>. See <a className="xref" href="/katalon-platform/integrations/jira-integration/enable-testops---jira-integration-for-test-management">Jira integration in <span className="ph">Katalon TestOps</span></a>.</p></li></ul></div>

## <a id="task-3667" class="anchor_top_offset"/>Populate unreleased Jira releases

<section xmlns="http://www.w3.org/1999/xhtml" className="section context">To populate unreleased Jira releases in <span className="ph">Katalon TestOps</span>, do as follows:</section> 
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol steps"><li className="li step stepexpand"><span className="ph cmd">In the <span className="ph uicontrol">Planning</span> &gt; <span className="ph uicontrol">Releases</span>, click on the <span className="ph uicontrol">Populate Jira Releases</span> button.</span><div className="itemgroup stepresult">The <span className="ph uicontrol">Populate Jira Releases</span> box pops up with a dropdown list containing all of your Jira projects.<p className="p"><img className="image" width={850} src={useBaseUrl("/596eb4d0-5c2b-11ed-a602-0242cfbc79b5/to-populate-jira-release.png")} /></p></div></li><li className="li step stepexpand"><span className="ph cmd">Select your Jira project  in the dropdown menu, then click <span className="ph uicontrol">OK</span>.</span></li><li className="li step stepexpand"><span className="ph cmd"><strong className="ph b">Optional:</strong> In case you change your start date and release date in Jira, click <span className="ph uicontrol">Refresh</span> to see the latest  changes in TestOps.</span></li></ol> 
<section xmlns="http://www.w3.org/1999/xhtml" className="section result">Once imported successfully, you can see the name, status, start date and release date of all unreleased releases of the selected Jira projects in <span className="ph">Katalon TestOps</span>.<p className="p"><img className="image" src={useBaseUrl("/5972fa90-5c2b-11ed-a602-0242cfbc79b5/to-releases.png")} /></p></section> 
<nav xmlns="http://www.w3.org/1999/xhtml" role="navigation" className="related-links"><div className="linklist"><strong>Next step</strong><br /><br /><ul className="linklist"><li className="linklist"><a className="link" href="/katalon-platform/plan/link-test-runs-to-a-release-in-testops">Link test runs to a release in TestOps</a></li></ul></div></nav> 

## <a id="task-4547" class="anchor_top_offset"/>Create a new TestOps release linked to a Jira release

<section xmlns="http://www.w3.org/1999/xhtml" className="section context">To create a new embedded Jira release in <span className="ph">Katalon TestOps</span>, do as follows:</section> 
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol steps"><li className="li step stepexpand"><span className="ph cmd">Click on the <span className="ph uicontrol">Create Release</span> button at the top right corner.</span><div className="itemgroup info">Once you have enabled Jira integration in <span className="ph">Katalon TestOps</span>, the <span className="ph uicontrol">Jira Project</span> and <span className="ph uicontrol">Jira Release</span> sections are added in the <span className="ph uicontrol">Create Release</span> page.</div><div className="itemgroup info"><img className="image" width={500} src={useBaseUrl("/59762ee0-5c2b-11ed-a602-0242cfbc79b5/to-create-releases.png")} /></div></li><li className="li step stepexpand"><span className="ph cmd">Select your Jira project and Jira release in the dropdown menu, then click <span className="ph uicontrol">Create</span>.</span></li></ol> 
<section xmlns="http://www.w3.org/1999/xhtml" className="section result">Once created successfully, you can see the linked Jira release status next to the name of the newly created TestOps release. You can now link your test runs to this release. </section> 
<nav xmlns="http://www.w3.org/1999/xhtml" role="navigation" className="related-links"><div className="linklist"><strong>Next step</strong><br /><br /><ul className="linklist"><li className="linklist"><a className="link" href="/katalon-platform/plan/link-test-runs-to-a-release-in-testops">Link test runs to a release in TestOps</a></li></ul></div></nav> 
