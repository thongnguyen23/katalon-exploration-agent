---
hide_title: true
title: Manage Desired Capabilities in Katalon Studio
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="id" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Manage Desired Capabilities in <span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon Studio</span> 

<p xmlns="http://www.w3.org/1999/xhtml" className="p">You can reuse desired capabilities   across Katalon Studio projects by importing and exporting desired   capabilities in a JSON file. See also <a className="xref" href="/katalon-studio/manage-projects/project-settings/desired-capabilities/introduction-to-desired-capabilities-in-katalon-studio">Desired     capabilities</a>.</p> 
<div xmlns="http://www.w3.org/1999/xhtml" className="p">This is useful if you want to: <ul className="ul"><li className="li"><p className="p">Reuse or copy the configured
        desired capabilities to another projects with some minor changes.</p></li><li className="li"><p className="p">Share the configured desired capabilities for team members to
        reduce effort.</p></li></ul></div>

## Requirements

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">An active       Katalon Studio Enterprise license. You can learn more about       activating licenses in this document: <a className="xref" href="/katalon-studio/get-started/activate-licenses">Activate         Katalon License</a>.</p></li></ul> 

## <a id="id_1" class="anchor_top_offset"/>Export desired capabilities

<ol xmlns="http://www.w3.org/1999/xhtml" className="ol"><li className="li">     <p className="p">Go to <strong className="ph b">Project/Settings/Desired Capabilities</strong> &gt; Choose the driver with the desired capabilities you wish to export. Click <strong className="ph b">Export</strong>.</p>     <p className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/project-settings-new-ui/KS-DC-Export-DC.png")} /><br /><br />     </p>   </li><li className="li">     <p className="p">A dialog box appears. Select the destination folder, then click <strong className="ph b">Save</strong>.</p>     <p className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/azure-devops/desired-capabilities-management/export-chrome-save.png")} width={400} alt="Save JSON file" /><br /><br />     </p>   </li></ol> 

## <a id="id_2" class="anchor_top_offset"/>Import desired capabilities

<p xmlns="http://www.w3.org/1999/xhtml" className="p">After exporting the JSON files, you can modify them if needed, then import them into another projects.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Follow these steps:</p> 
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol"><li className="li">     <p className="p">Go to <strong className="ph b">Project/Settings/Desired Capabilities</strong> &gt; choose the driver you want to import the desired capabilities of. Click <strong className="ph b">Import</strong>.</p>     <p className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/project-settings-new-ui/KS-DC-Import-DC.png")} /><br /><br />     </p>   </li><li className="li">     <p className="p">A dialog box appears. Click <strong className="ph b">Browse</strong>. Navigate to the JSON file you want to import and select it. Click <strong className="ph b">OK</strong>.</p>     <div className="note note note_note"><span className="note__title">Note:</span>        <ul className="ul"><li className="li">You can decide whether to override all existing desired capabilities by checking/unchecking the <strong className="ph b">Override existing properties</strong> box.</li></ul>     </div>     <p className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/azure-devops/desired-capabilities-management/chrome_dc.png")} width={400} /><br /><br />     </p>   </li></ol> 

## <a id="id_3" class="anchor_top_offset"/>See also

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">     <a className="xref" href="/katalon-studio/manage-test-artifacts/test-artifacts-sharing-in-katalon-studio">Test       Artifacts Sharing</a>   </li><li className="li">     <a className="xref" href="/katalon-platform/plugins-and-add-ons/katalon-store/katalon-studio-plugins/private-plugins-in-katalon-studio">Private       Plugins</a>   </li></ul> 
