---
hide_title: true
title: Combine Katalon Studio with SAP Scripting Tracker for Windows
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# Combine Katalon Studio  with SAP Scripting Tracker for Windows

:::important
Starting in version 10.3.0, Desktop app testing is available again as a **beta** feature with a new built-in driver (no installation required).

Windows Desktop app testing remains to be temporarily unavailable in Katalon Studio 10.0.0 to 10.2.x due to compatibility issues with WinAppDriver.

- To continue using the legacy WinAppDriver workflow, use Katalon Studio 9.x.
- For full details on feature availability and version support, see the [Katalon Studio Release Notes: Version 10.x](/katalon-studio/release-notes/katalon-studio-release-notes-version-10.x).
:::

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Scripting Tracker is a utility and a replacement to the SAP GUI Scripting Development Tools. It is an SAP GUI analyzer and recorder on the SAP GUI Scripting base. You can learn more about SAP Scripting Tracker in the SAP blog post here: <a className="xref j-external-link" href="https://blogs.sap.com/2014/11/20/scripting-tracker-development-tool-for-sap-gui-scripting/" target="_blank">Scripting Tracker – Development Tool for SAP GUI Scripting</a>.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">This tutorial demonstrates how to combine <span className="ph">Katalon Studio</span> with SAP Scripting Tracker for Windows.</p> 

## Requirements

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">WinAppDriver version 1.1.0 onwards. To learn more about setting up WinAppDriver, you can refer to this document: <a className="xref" href="/katalon-studio/manage-projects/set-up-projects/windows-desktop-apps-testing/set-up-winappdriver-in-katalon-studio">Set up WinAppDriver</a>.</li><li className="li">SAP Scripting Tracker version 3.15 onwards. You can download the SAP Scripting Tracker from the Scripting Tracker website: <a className="xref j-external-link" href="https://tracker.stschnell.de/#" target="_blank">Scripting Tracker</a>.</li></ul> 
    

## Enable SAP GUI Scripting in SAP

    
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">To enable SAP scripting mode, you can refer to the SAP document   here: <a className="xref j-external-link" href="https://help.sap.com/viewer/8ecea00c1f854fd0a433c4aef5da1ea2/Cloud/en-US/001675913cc54719930aa8197478dcde.html" target="_blank">Enabling     Scripting on the Server Side</a>.</p> 
    
  

## Implement the Java code recording for SAP Scripting         Tracker

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Katalon can only read Java language generated from SAP Scripting   Tracker. To use SAP GUI Scripting in the context of Java you need   the Java COM Bridge (JACOB). You can download and install Java COM   Bridge (JACOB) from the GitHub repository: <a className="xref j-external-link" href="https://sourceforge.net/projects/jacob-project/" target="_blank">Java COM     Bridge (JACOB)</a>.</p> 

## Build your test case in Katalon Studio


### Download our sample Katalon SAP GUI project

<p xmlns="http://www.w3.org/1999/xhtml" className="p">This sample project provides you with code samples, custom   keywords, and sample test cases that give you the necessary   preparations to automate your test script with SAP Scripting   Tracker.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">You can clone or download the sample project here at our GitHub   repository: <a className="xref j-external-link" href="https://github.com/katalon-studio-samples/kat-sap-gui-sample-test" target="_blank">Katalon     SAP GUI sample project</a>.</p> 

### Add your login account to a test case in Katalon Studio

<ol xmlns="http://www.w3.org/1999/xhtml" className="ol"><li className="li">After downloading our sample project, from the <strong className="ph b">Test Explorer</strong> panel, open <strong className="ph b">Profiles &gt; default</strong>. </li><li className="li">     <p className="p">Double-click the <strong className="ph b">Value</strong> cell of the <strong className="ph b">username</strong> and <strong className="ph b">password</strong> variables.</p>     <p className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/katalon-sap-scripting-tracker/KS-SAP-Open-the-default-file.png")} alt="Open the default file" /><br /><br />     </p>   </li><li className="li">     <p className="p">In the opened <strong className="ph b">Edit variables</strong> dialog, change the sample value to your SAP account.</p>     <p className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/katalon-sap-scripting-tracker/KS-SAP-Fill-in-your-username.png")} alt="Fill in your username" /><br /><br />     </p>     <p className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/katalon-sap-scripting-tracker/KS-SAP-Fill-in-ur-password.png")} alt="Fill in your password" /><br /><br />     </p>   </li></ol> 

### Create a new test case in Katalon Studio based on the sample project

<ol xmlns="http://www.w3.org/1999/xhtml" className="ol"><li className="li">     <p className="p">Create a new test case. Go to <strong className="ph b">File &gt; New &gt; Test Case</strong>.</p>   </li><li className="li">     <p className="p">From the <strong className="ph b">Test Explorer</strong> panel of our sample project, go to <strong className="ph b">Test Cases &gt; Common</strong> folder. There are 3 sample test cases as follows:</p>     <table className="table anchor_top_offset" id="concept-6577__7dcc198f-0ff4-4e53-a1db-1ec20d3ac424"><caption /><tbody className="tbody"><tr className><td className="entry"><strong className="ph b">StartSAPLogon</strong></td><td className="entry">This sample test case starts SAP Logon, then goes to the sign-in section.</td></tr><tr className><td className="entry"><strong className="ph b">Login</strong></td><td className="entry">This sample test case starts an SAP session then uses the <strong className="ph b">username</strong> and <strong className="ph b">password</strong> variables to login</td></tr><tr className><td className="entry"><strong className="ph b">TestCaseTemplate</strong></td><td className="entry">This sample test case calls the <strong className="ph b">StartSAPLogon</strong> and <strong className="ph b">Login</strong> test cases, then enables Katalon to read the SAP Scripting Tracker script.</td></tr></tbody></table>     <p className="p"><img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/katalon-sap-scripting-tracker/KS-SAP-3-sample-test-cases.png")} alt="3 sample test cases" /><br /><br /></p>   </li><li className="li">     <p className="p">Open the <strong className="ph b">Script</strong> tab of the <strong className="ph b">TestCaseTemplate</strong> test case, copy the content and paste it into the <strong className="ph b">Script</strong> tab of the new test case created from step 1.</p>     <p className="p"><img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/katalon-sap-scripting-tracker/830-KS-SAP-Copy-the-test-script-in-the-TestCaseTemplate-sample.png")} alt="Copy the test script in the TestCaseTemplate sample test" /><br /><br /></p>     <p className="p"><img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/katalon-sap-scripting-tracker/830-KS-SAP-Paste-the-test-script-into-the-new-test-case.png")} alt="Paste the test script into the new test case" /><br /><br /></p>   </li></ol> 

### Record test script using SAP Scripting Tracker

<div xmlns="http://www.w3.org/1999/xhtml" className="p"><ol className="ol"><li className="li"><p className="p">Start SAP Logon and sign in SAP GUI with your SAP account.</p><p className="p"><img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/katalon-sap-scripting-tracker/KS-SAP-Start-SAPLogon.png")} alt="Start SAPLogon" /><br /><br /></p></li><li className="li"><p className="p">After signing in, open SAP Scripting Tracker. Click <strong className="ph b">Refresh</strong>, then select the current SAP session.</p><p className="p"><img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/katalon-sap-scripting-tracker/KS-SAP-select-SAP-session.png")} alt="Select the SAP session" /><br /><br /></p></li><li className="li"><p className="p">Choose Java language, then click <strong className="ph b">Record</strong> to start recording your SAP GUI script.</p><p className="p"><img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/katalon-sap-scripting-tracker/KS-SAP-Choose-Java-language.png")} alt="Choose Java" /><br /><br /></p><p className="p">Here, we record the following scenario:</p><ul className="ul"><li className="li">In the opened SAP GUI session, go to <strong className="ph b">SAP Menu &gt; Human Resources</strong>. Double-click on <strong className="ph b">PPMDT - Manager's Desktop</strong>. The <strong className="ph b">Manager's Desktop</strong> interface opens.</li><li className="li">Double-click on <strong className="ph b">Personal Data</strong> to open the folder.</li><li className="li">Navigate to <strong className="ph b">Reports &gt; Employee data</strong>, then click <strong className="ph b">Maternity</strong>.</li></ul><p className="p">We stop recording here.</p><p className="p"><img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/katalon-sap-scripting-tracker/ezgif.com-gif-maker.gif")} alt="Recording from Scripting Tracker" /><br /><br /></p></li><li className="li"><p className="p">After finishing your recording, copy and paste the content from Scripting Tracker into your Katalon test script.</p><p className="p"><img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/katalon-sap-scripting-tracker/KS-SAP-Copy-the-script-from-Scripting-Tracker.png")} alt="Copy the script from Scripting Tracker" /><br /><br /></p><p className="p"><img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/katalon-sap-scripting-tracker/KS-SAP-Paste-after-pasting-the-script-into-Katalon.png")} alt="Paste the script into the Katalon test script" /><br /><br /></p><p className="p"><img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/katalon-sap-scripting-tracker/KS-SAP-Final-results.png")} alt="Results after pasting the script into the Katalon test script" /><br /><br /></p></li></ol></div>

### Run the test script in Katalon Studio

:::info notes
Make sure you have `WinAppDriver.exe` running from the installation directory. By default, you can find it at `C:\Program Files (x86)\Windows Application Driver\WinAppDriver.exe`.
:::

<p xmlns="http://www.w3.org/1999/xhtml" className="p">To run the recorded test script, on the main toolbar, select <strong className="ph b">Windows</strong> in the dropdown list next to <strong className="ph b">Run</strong>.</p> 
<img xmlns="http://www.w3.org/1999/xhtml" className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/katalon-sap-scripting-tracker/KS-SAP-Run-the-test.png")} alt="Run the test" /> 
<br xmlns="http://www.w3.org/1999/xhtml" /> 
<br xmlns="http://www.w3.org/1999/xhtml" /> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><span className="ph">Katalon Studio</span>  automatically signs in SAP GUI with your SAP account and playback the recorded steps from Scripting Tracker.</p> 
