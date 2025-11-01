---
hide_title: true
title: Windows Spy Utility in Katalon Studio
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# Windows Spy Utility in Katalon Studio

:::important
Starting in version 10.3.0, Desktop app testing is available again as a **beta** feature with a new built-in driver (no installation required).

Windows Desktop app testing remains to be temporarily unavailable in Katalon Studio 10.0.0 to 10.2.x due to compatibility issues with WinAppDriver.

- To continue using the legacy WinAppDriver workflow, use Katalon Studio 9.x.
- For full details on feature availability and version support, see the [Katalon Studio Release Notes: Version 10.x](/katalon-studio/release-notes/katalon-studio-release-notes-version-10.x).
:::

<p xmlns="http://www.w3.org/1999/xhtml" className="p">The Windows spy utility helps capture test objects quickly and allows you to specify several object properties and locator strategies.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">This article introduces you to the components of the Windows spy utility in Katalon Studio.</p> 

## Requirements

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">WinAppDriver is running on the test machine. To learn how to set up and run WinAppDriver, see: <a className="xref" href="/katalon-studio/manage-projects/set-up-projects/windows-desktop-apps-testing/set-up-winappdriver-in-katalon-studio">Set up WinAppDriver</a>.</li></ul> 

## The Windows spy utility

<p xmlns="http://www.w3.org/1999/xhtml" className="p">To open the utility, from the main toolbar, click on the <strong className="ph b">Spy Windows Object</strong> button.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/windows-spy-utility/KS-Windows-Spy-Objects-button.png")} alt="Spy Windows Objects icon" /><br /><br /> </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">The <strong className="ph b">Spy Windows Objects</strong> dialog is displayed as below:</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/windows-spy-utility/KS-Windows-Object-Spy-dialog.png")} alt="Spy Windows Objects dialog" /><br /><br /> </p> 
      

### Configurations

      
        
<p xmlns="http://www.w3.org/1999/xhtml" className="p">In the <strong className="ph b">Configurations</strong> section, you can   specify:</p> 
        
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul">   <li className="li">     <p className="p">       <strong className="ph b">Configuration</strong>: the WinAppDriver URL and desired       capabilities.</p>   </li>   <li className="li">     <p className="p">       <strong className="ph b">Application File</strong>: the absolute path to the       Windows executable file (*.exe) of the testing machine. For Windows       users, click on the <strong className="ph b">Browse...</strong> button to locate the       application file.</p>   </li> </ul> 
        
<p xmlns="http://www.w3.org/1999/xhtml" className="p">When the application under test (AUT) is started, the utility   captures all available Windows objects on the current window of the   AUT and displays them in the <strong className="ph b">All Objects</strong>   section.</p> 
      
    

### All objects

<p xmlns="http://www.w3.org/1999/xhtml" className="p">The <strong className="ph b">All Objects</strong> section shows a tree of all the objects of the AUT, including the associated Windows element names (highlighted in blue) and tag names.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/windows-spy-utility/KS-All-Objects-section.png")} alt="All objects section" /><br /><br /> </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">To add a Windows object, check the checkbox on the left of the desired Windows object. The added object is then displayed in the <strong className="ph b">Captured Objects</strong> section.</p> 

## Screen view

<p xmlns="http://www.w3.org/1999/xhtml" className="p">When an object is selected in the <strong className="ph b">All Objects</strong> section, the position of the associated element is highlighted in the <strong className="ph b">Screen View</strong>. This helps verify the selected Windows element.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/windows-spy-utility/KS-Screen-View-section.png")} alt="Captured objects section" /><br /><br /> </p> 

### Captured objects

<p xmlns="http://www.w3.org/1999/xhtml" className="p">The <strong className="ph b">Captured Objects</strong> section shows all the captured Windows elements you want to add to the <strong className="ph b">Object Repository</strong>.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">To view details about a captured object, click on it. The detailed information is displayed in the <strong className="ph b">Object Properties</strong> section.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/windows-spy-utility/KS-Captured-Objects-section.png")} alt="Captured objects section" /><br /><br /> </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">You can view and edit the object name, locator and properties before adding it to the <strong className="ph b">Object Repository</strong>.</p> 
      

### Object properties

      
        
<p xmlns="http://www.w3.org/1999/xhtml" className="p">The <strong className="ph b">Object Properties</strong> section allows you to   configure the following information:</p> 
        
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul">   <li className="li">     <strong className="ph b">Object Name</strong>: the Windows object name.</li>   <li className="li">     <strong className="ph b">Locator Strategy</strong>: the type of object locator     to identify the Windows element. To generate the object locator of     the desired locator type, click on the <strong className="ph b">Generate</strong>     button.</li>   <li className="li">     <strong className="ph b">Locator</strong>: the generated object locator that can     be customized.</li>   <li className="li">     <strong className="ph b">Properties</strong> table: all properties of the     captured objects.</li> </ul> 
        
<p xmlns="http://www.w3.org/1999/xhtml" className="p">To add the captured objects to the <strong className="ph b">Object     Repository</strong>, click <strong className="ph b">OK</strong> and select the   target folder where you want to save the objects.</p> 
      
    

## View and edit the captured objects

<p xmlns="http://www.w3.org/1999/xhtml" className="p">You can view and edit the locator and properties of a captured object in the <strong className="ph b">Object</strong> view.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Go to <strong className="ph b">Tests Explorer</strong>&gt; <strong className="ph b">Object Repository</strong>, and select the desired Windows object. Details about a captured object are displayed in the <strong className="ph b">Object</strong> view as follows:</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/windows-spy-utility/KS-Object-view.png")} alt="Object view" /><br /><br /> </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">In the <strong className="ph b">Object</strong> view, you can view and edit:</p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"> <strong className="ph b">Locator</strong>: the locator type and locator of the object.</li><li className="li"> <strong className="ph b">Object Properties</strong>: the properties of the object.</li></ul> 
