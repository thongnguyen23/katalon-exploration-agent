---
hide_title: true
title: Capture Windows Objects using the Windows Spy Utility in Katalon Studio
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# Capture Windows Objects using the Windows Spy Utility in Katalon Studio

:::important
Starting in version 10.3.0, Desktop app testing is available again as a **beta** feature with a new built-in driver (no installation required).

Windows Desktop app testing remains to be temporarily unavailable in Katalon Studio 10.0.0 to 10.2.x due to compatibility issues with WinAppDriver.

- To continue using the legacy WinAppDriver workflow, use Katalon Studio 9.x.
- For full details on feature availability and version support, see the [Katalon Studio Release Notes: Version 10.x](/katalon-studio/release-notes/katalon-studio-release-notes-version-10.x).
:::

<p xmlns="http://www.w3.org/1999/xhtml" className="p">This guide shows you how to capture Windows objects with the Windows spy utility.</p> 
<div xmlns="http://www.w3.org/1999/xhtml" className="note important note_important"><span className="note__title">Important:</span> <ul className="ul"><li className="li">WinAppDriver is running on the test machine. To learn how to set up and run WinAppDriver, see: <a className="xref" href="/katalon-studio/manage-projects/set-up-projects/windows-desktop-apps-testing/set-up-winappdriver-in-katalon-studio">Set up WinAppDriver</a>.</li></ul></div>
<p xmlns="http://www.w3.org/1999/xhtml" className="p">To use the utility, first you need to open the <strong className="ph b">Spy Windows Objects</strong> dialog. From the main toolbar, click on the <strong className="ph b">Spy Windows Objects</strong> icon.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/windows-spy-tutorial/KS-Windows-Spy-Objects-button.png")} alt="Spy Windows Objects dialog" /><br /><br /></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">The <strong className="ph b">Spy Windows Objects</strong> dialog is displayed as below:</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/windows-spy-tutorial/KS-Windows-Object-Spy-dialog.png")} alt="Spy Windows Objects dialog" /><br /><br /></p> 
<nav xmlns="http://www.w3.org/1999/xhtml" role="navigation" className="related-links"><div className="linklist relinfo relconcepts"><strong>Related concepts</strong><br /><br /><ul className="linklist"><li className="linklist"><a className="link" href="/katalon-studio/manage-projects/set-up-projects/windows-desktop-apps-testing/set-up-winappdriver-in-katalon-studio#concept-5429">Set up WinAppDriver</a></li></ul></div></nav> 

## Configure the Windows spy utility

<p xmlns="http://www.w3.org/1999/xhtml" className="p">To configure the utility, in the <strong className="ph b">Configurations</strong> section, specify the following fields:</p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">     <p className="p"> <strong className="ph b">Configuration</strong>: the WinAppDriver URL and desired capabilities.</p>   </li><li className="li">     <p className="p"> <strong className="ph b">Application File</strong>: the absolute path to the Windows executable file (*.exe) of the testing machine. For Windows users, click on the <strong className="ph b">Browse...</strong> button to locate the application file.</p>   </li></ul> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">For example, we provide the IP address to the remote Windows machine and the path to Notepad executable as the AUT.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/windows-spy-tutorial/KS-Configure-Spy-Utility.png")} alt="CONFIGURATIONS section" /><br /><br /> </p> 

:::info notes
For Universal Windows Platform (UWP) applications, the executable file should be:

- *ApplicationID*, if the application is published on the Microsoft store.
- *PackageFamilyName!Application ID*, if the application is still in development.
:::
## <a id="id_2" class="anchor_top_offset"/>Capture Windows objects

To capture Windows objects, follow these steps:

1. Start the connection to the WinAppDriver by clicking on the **Start** button.
    
    <img src="https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/windows-spy-tutorial/KS-Windows-spy-utility-start-button.png" alt="Start button" />
    
    You can see the opened window of the executed AUT in the **Screen View** section:
    
    <img src="https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/windows-spy-tutorial/KS-Windows-spy-utility-executed-AUT.png" alt="Screen view Windows spy utulity" />
    
    All available objects on the window are displayed in the **All Objects** section. You can verify an object by clicking on it; the utility highlights the object with a green border in **Screen View**.
    
    <img src="https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/windows-spy-tutorial/KS-Windows-spy-utility-executed-highlighted-object.png" alt="Screen view Windows spy utulity" />
    
2. Add the captured objects. Select the objects you want to capture by checking on the checkbox on the left.
    
    The selected objects are displayed in the **Captured Objects** section.
    
    <img src="https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/windows-spy-tutorial/KS-Select-Captured-Objects.png" alt="Spy object window screen" />
    
3. To save the captured objects, click on the **Add to Object Repository** button. In the opened dialog, select your desired folder, then click **OK**.
    
    <img src="https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/windows-spy-tutorial/KS-Add-to-Object-Repository.png" alt="Add to object repo screen" />
    
    The captured objects are added to the selected folder in the **Object Repository**.
    
    <img src="https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/windows-spy-tutorial/KS-Object-Repository.png" alt="Object repo result screen" />
    
4. To end the capturing session, click on the **OK** button at the bottom of the dialog.

:::tip tips
While spying, recording, or executing a test on a desktop application:

- Do not lock the screen of the testing machine
- Do not run multiple instances of the AUT simultaneously.
:::