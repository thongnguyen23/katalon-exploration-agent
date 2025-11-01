---
hide_title: true
title: Library management in Katalon Studio
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="concept-8611" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Library management in <span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon Studio</span> 

<p xmlns="http://www.w3.org/1999/xhtml" className="p"><span className="ph">Katalon Studio</span> allows using external Java <code className="ph codeph">.jar</code> libraries either through project settings or adding them to a designated folder. You can leverage this to extend the capabilities of <span className="ph">Katalon Studio</span> and handle specific situations when needed. </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">This document shows you ways to add external libraries to <span className="ph">Katalon Studio</span> and replace the built-in libraries with the external ones in a test project.</p> 

## <a id="concept-7517" class="anchor_top_offset"/>Add external libraries to a  project

<p xmlns="http://www.w3.org/1999/xhtml" className="p">You can add external libraries to a <span className="ph">Katalon Studio</span> project in  three different ways:</p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">Use the Gradle plugin.</li><li className="li">Go to Library Management settings of a project.</li><li className="li">Copy and paste a library <code className="ph codeph">.jar</code> file to the Drivers folder of a project.</li></ul> 

### <a id="task-760" class="anchor_top_offset"/>Use Gradle in <span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon Studio</span> 

<div xmlns="http://www.w3.org/1999/xhtml" className="li step p"><span className="ph cmd"><span className="ph">Katalon Studio</span> supports automatically downloading libraries from Maven repositories using the Gradle plugin. You can refer to our GitHub repository here: <a className="xref j-external-link" href="https://github.com/katalon-studio/gradle-plugin" target="_blank">Katalon Studio Gradle plugin</a>.</span></div>

### <a id="task-4018" class="anchor_top_offset"/>Use project settings

<section xmlns="http://www.w3.org/1999/xhtml" className="section context">To add external libraries in project settings, do as follows:</section> 
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol steps"><li className="li step stepexpand"><span className="ph cmd">In <span className="ph">Katalon Studio</span>, go to <span className="ph uicontrol">Project</span> &gt; <span className="ph uicontrol">Settings</span> &gt; <span className="ph uicontrol">Library Management</span>.</span></li><li className="li step stepexpand"><span className="ph cmd">In <span className="ph menucascade"><span className="ph uicontrol">Library Management</span><abbr title="and then"> &gt; </abbr><span className="ph uicontrol">External Libraries</span></span>, click <span className="ph uicontrol">Add</span> to browse your <code className="ph codeph">.jar</code> file(s) (and its dependencies if any).</span><div className="itemgroup info"><img className="image" width={500} src={useBaseUrl("/8f73fde0-22b2-11ed-9930-0242fe3e4a3f/KS-LIBRARY-Add-external-library.png")} alt="Add external libraries" /></div><div className="itemgroup info">To remove an added external library, select a library and click <span className="ph uicontrol">Remove</span>.</div></li><li className="li step stepexpand"><span className="ph cmd">Click <span className="ph uicontrol">Apply and Close</span>.</span><div className="itemgroup stepresult">If you have any unsaved items, Katalon Studio will trigger the <span className="ph uicontrol">Save Resources</span> dialog, prompting you to save your work.<p className="p"><img className="image" width={300} src={useBaseUrl("/3131ca09-b356-4de2-a1b8-dad54beaf79e/KS-LIBRARY-Save-resources.png")} /></p></div></li><li className="li step stepexpand"><span className="ph cmd">Click <span className="ph uicontrol">OK</span> to save the selected items and apply the library changes.</span></li></ol> 
<section xmlns="http://www.w3.org/1999/xhtml" className="section result">Once the changes are saved, <span className="ph">Katalon Studio</span> will reload your project, close all open editors, and add the library file(s) to the project's <span className="ph uicontrol">Drivers</span> folder.<p className="p"><img className="image" width={500} src={useBaseUrl("/8f758480-22b2-11ed-9930-0242fe3e4a3f/KS-LIBRARY-View-add-external-library-in-folder.png")} alt="Libraries added in the Drivers folder" /></p> </section> 

### <a id="task-3738" class="anchor_top_offset"/>Copy and paste a library .jar file to the Drivers folder

<ol xmlns="http://www.w3.org/1999/xhtml" className="ol steps"><li className="li step stepexpand"><span className="ph cmd">Copy the <code className="ph codeph">.jar</code> file (and its dependencies, if any) you want to add to the project.</span></li><li className="li step stepexpand"><span className="ph cmd">Go to your project folder, select the <span className="ph uicontrol">Drivers</span> folder and paste the <code className="ph codeph">.jar</code> file.</span><div className="itemgroup info"><img className="image" width={500} src={useBaseUrl("/ed2532a0-cc63-11ed-a4d3-0242cfbc79b5/ks-paste-file-in-drivers.png")} alt="Manually add the library" /></div></li><li className="li step stepexpand"><span className="ph cmd">Close and re-open the project in <span className="ph">Katalon Studio</span> to reload the class paths.</span></li></ol> 
<section xmlns="http://www.w3.org/1999/xhtml" className="section result"><p className="p">When your <code className="ph codeph">.jar</code> library file is recognized by <span className="ph">Katalon Studio</span>, you should be able to use it.</p></section> 

## <a id="task-4328" class="anchor_top_offset"/>Exclude built-in libraries

<div xmlns="http://www.w3.org/1999/xhtml" className="section prereq p"><ul className="ul"><li className="li">An active <span className="ph">Katalon Studio Enterprise</span> license.</li></ul></div>

The **Exclude built-in libraries** feature allows you to remove built-in libraries stored in the `.classpath` file of a project folder. This feature applies to all libraries in the `.classpath` file, excluding the following:

- `com.kms.katalon.*.jar`
- `selenium-server-standalone-3.141.59.jar`
- `poi-3.17.jar`
- `poi-ooxml-3.17.jar`
- `poi-ooxml-schemas-3.17.jar`
- `java-client-7.0.0.jar`
- `io.cucumber.*.jar`

Removing the above libraries may cause failure of the relevant features.

You can also replace the excluded built-in library with an external one for flexible libraries usage in a test project.

<ol xmlns="http://www.w3.org/1999/xhtml" className="ol steps"><li className="li step stepexpand"><span className="ph cmd">In <span className="ph">Katalon Studio</span>, go to <span className="ph uicontrol">Project</span> &gt; <span className="ph uicontrol">Settings</span> &gt; <span className="ph uicontrol">Library Management</span>.</span></li><li className="li step stepexpand"><span className="ph cmd">In the <span className="ph uicontrol">Exclude the following built-in libraries</span> section, click <span className="ph uicontrol">Add</span> to add a built-in library you want to remove.</span></li><li className="li step stepexpand"><span className="ph cmd">In the <span className="ph uicontrol">External Libraries</span> section, click <span className="ph uicontrol">Add</span> to browse an external library to replace the excluded one.</span><div className="itemgroup info"><img className="image" src={useBaseUrl("/8f727740-22b2-11ed-9930-0242fe3e4a3f/KS-Exclude-the-library.png")} alt="Exclude libraries" /></div></li><li className="li step stepexpand"><span className="ph cmd">Click <span className="ph uicontrol">Apply and Close</span>.</span></li></ol> 
