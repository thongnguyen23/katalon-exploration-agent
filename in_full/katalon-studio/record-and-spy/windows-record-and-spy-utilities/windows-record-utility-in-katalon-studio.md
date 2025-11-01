---
hide_title: true
title: Windows Record Utility in Katalon Studio
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# Windows Record Utility in Katalon Studio

:::important
Starting in version 10.3.0, Desktop app testing is available again as a **beta** feature with a new built-in driver (no installation required).

Windows Desktop app testing remains to be temporarily unavailable in Katalon Studio 10.0.0 to 10.2.x due to compatibility issues with WinAppDriver.

- To continue using the legacy WinAppDriver workflow, use Katalon Studio 9.x.
- For full details on feature availability and version support, see the [Katalon Studio Release Notes: Version 10.x](/katalon-studio/release-notes/katalon-studio-release-notes-version-10.x).
:::

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Katalon Studio provides the Windows record utility that allows you to record and playback actions performed in a Windows desktop application. With this utility, you can quickly create a test case, and later manually enhance the test.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">This article introduces you to the components of the Windows record utility in Katalon Studio.</p> 

## Requirements

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">WinAppDriver is running on the test machine. To learn how to set up and run WinAppDriver, see: <a className="xref" href="/katalon-studio/manage-projects/set-up-projects/windows-desktop-apps-testing/set-up-winappdriver-in-katalon-studio">Set up WinAppDriver</a>.</li></ul> 
<nav xmlns="http://www.w3.org/1999/xhtml" role="navigation" className="related-links"><div className="linklist relinfo relconcepts"><strong>Related concepts</strong><br /><br /><ul className="linklist"><li className="linklist"><a className="link" href="/katalon-studio/manage-projects/set-up-projects/windows-desktop-apps-testing/set-up-winappdriver-in-katalon-studio#concept-5429">Set up WinAppDriver</a></li></ul></div></nav> 

## The Windows record utility

<p xmlns="http://www.w3.org/1999/xhtml" className="p">To open the utility, from the main toolbar, click on <strong className="ph b">Record Windows Action</strong>.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/windows-record-utility/KS-Record-Windows-Action-button.png")} alt="Spy Windows Objects icon" /><br /><br /> </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">The <strong className="ph b">Windows Action Recorder</strong> dialog is displayed as below:</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/windows-record-utility/KS-Windows-Action-Recorder-dialog.png")} alt="Windows Action Recorder dialog" /><br /><br /> </p> 
      

### Configurations

      
        
<p xmlns="http://www.w3.org/1999/xhtml" className="p">In the <strong className="ph b">CONFIGURATIONS</strong> section, you can   specify:</p> 
        
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul">   <li className="li">     <p className="p">       <strong className="ph b">Configuration</strong>: the WinAppDriver URL and desired       capabilities.</p>   </li>   <li className="li">     <p className="p">       <strong className="ph b">Application File</strong>: the absolute path to the       Windows executable file (*.exe) of the testing machine. For Windows       users, click on the <strong className="ph b">Browse...</strong> button to locate the       application file.</p>   </li> </ul> 
      
    

### Recorded actions

<p xmlns="http://www.w3.org/1999/xhtml" className="p">After you interact with the application under test (AUT) using the built-in actions, the recorded actions are displayed in the <strong className="ph b">Recorded Actions</strong> tab.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/windows-record-utility/KS-Recorded-Actions-tab.png")} alt="Recorded Actions tab" /><br /><br /> </p> 

### Captured objects

<p xmlns="http://www.w3.org/1999/xhtml" className="p">During a recording session, the captured Windows objects are displayed in the <strong className="ph b">Captured Objects</strong> tab. You can view and edit the object name, locator and properties.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/windows-record-utility/KS-Captured-Objects-tab.png")} alt="Captured Objects tab" /><br /><br /> </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">You can modify the locator of an object in <strong className="ph b">Object Properties</strong> and click <strong className="ph b">Highlight</strong> to verify if the new locator correctly identifies the associated object.</p> 

### Screen View

<p xmlns="http://www.w3.org/1999/xhtml" className="p">The <strong className="ph b">Screen View</strong> shows the application screenshots taken when you press the <strong className="ph b">Start</strong> button to record or the <strong className="ph b">Refresh Screen</strong> button to recapture the application images. The size of a captured screenshot is the same as the displayed application window on the testing machine.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/windows-record-utility/KS-Screen-View-section.png")} alt="Screen view" /><br /><br /> </p> 

### Screen Objects

<p xmlns="http://www.w3.org/1999/xhtml" className="p">The <strong className="ph b">Screen Objects</strong> section shows a tree of all Windows objects you can interact with. To update this tree view, you can press the <strong className="ph b">Refresh Screen</strong> button.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">The selected object is highlighted with a green border on the <strong className="ph b">Screen View</strong>.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/windows-record-utility/KS-Screen-view.png")} alt="Object highlighted in the Screen View" /><br /><br /> </p> 

### Possible Actions

<p xmlns="http://www.w3.org/1999/xhtml" className="p">The <strong className="ph b">Possible Actions</strong> provides the built-in Windows actions that you can use to interact with the AUT.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/windows-record-utility/KS-Possible-Actions-section.png")} alt="Possible actions" /><br /><br /> </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">There are two types of Windows actions:</p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">     <p className="p">Object action: an action that you can perform on a specific Windows object. This type of action requires you to first select the target object on the <strong className="ph b">Screen Objects</strong>, e.g., performing the <em className="ph i">Click</em> action on a menu item.</p>   </li><li className="li">     <p className="p">Application action: an action for interacting with the application, e.g., the <em className="ph i">Close Application</em> action.</p>   </li></ul> 

## Export Option

<p xmlns="http://www.w3.org/1999/xhtml" className="p">When you finish the recording session, there are three options to export the recorded actions to a test case:</p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">Export to new test case (selected by default).</li><li className="li">Append to test case.</li><li className="li">Overwrite test case.</li></ul> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/windows-record-utility/KS-Export-Windows-script.png")} alt="Export actions dialog" /><br /><br /> </p> 
