---
hide_title: true
title: SikuliX integration
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="concept-9849" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>SikuliX integration

<p xmlns="http://www.w3.org/1999/xhtml" className="p">SikuliX automates anything you see on the screen of your desktop computer running Windows, Mac or some Linux/Unix. Integrating Katalon Studio with SikuliX can be useful in image-based testing, particularly in cases where direct access to a GUI's internal elements or the application/web page source code is challenging or inaccessible. </p> 

## <a id="task-2573" class="anchor_top_offset"/>Import and run SikuliX tests

<ol xmlns="http://www.w3.org/1999/xhtml" className="ol steps"><li className="li step stepexpand"><span className="ph cmd"><a className="xref j-external-link" href="https://launchpad.net/sikuli/+download" target="_blank">Download</a> the latest version of SikuliX. </span></li><li className="li step stepexpand"><span className="ph cmd"> Import SikuliX to <span className="ph">Katalon Studio</span> from <span className="ph menucascade"><span className="ph uicontrol">Project</span><abbr title="and then"> &gt; </abbr><span className="ph uicontrol">Settings</span><abbr title="and then"> &gt; </abbr><span className="ph uicontrol">Library Management</span></span>.<img className="image" src={useBaseUrl("/56fb8e10-7d56-11ee-8403-0242c7a41fd4/KS-SikuliX_library_import.png")} alt="import SikuliX in Katalon Studio" /></span></li><li className="li step stepexpand"><span className="ph cmd">Import SikuliX classes to your script.</span><div className="itemgroup info"><pre className="pre codeblock"><code>import org.sikuli.script.Key{"\n"}import org.sikuli.script.Screen{"\n"}import org.sikuli.script.FindFailed{"\n"}import org.sikuli.script.ImagePath</code></pre>Using the <code className="ph codeph">ImagePath</code> method, you can tell SikuliX the location of your sample images, for example:       <code className="ph codeph">ImagePath.add(System.getProperty("user.dir") + "\\Screenshots\\Sikuli");</code></div></li><li className="li step stepexpand"><span className="ph cmd">Here are exemplary steps to find and click a specific UI element using  sample .png images. </span><div className="itemgroup info"><pre className="pre codeblock"><code>Screen s = new Screen(){"\n"}s.find("Windows.png"){"\n"}s.click("Windows.png")</code></pre></div></li></ol> 
