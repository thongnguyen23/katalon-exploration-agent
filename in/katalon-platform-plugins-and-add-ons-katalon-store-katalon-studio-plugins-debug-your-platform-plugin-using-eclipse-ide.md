---
hide_title: true
title: Debug your platform plugin using Eclipse IDE
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="id" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Debug your platform plugin using Eclipse IDE

<p xmlns="http://www.w3.org/1999/xhtml" className="p">This tutorial will illustrate how to debug a platform plugin   using Eclipse IDE via <a className="xref j-external-link" href="https://help.eclipse.org/2019-03/topic/org.eclipse.jdt.doc.user/tasks/task-running_and_debugging.htm" target="_blank">Java     Remote Debugging</a> feature.</p> 

## Requirements

<div xmlns="http://www.w3.org/1999/xhtml" className="p"><ol className="ol"><li className="li">Java SDK 1.8</li><li className="li">Maven 3.3+</li><li className="li"><span className="ph">Katalon Studio</span> version 6.1.0 or later</li><li className="li">Eclipse IDE (We used Eclipse 4.11 in this article)</li></ol></div>

## <a id="id_2" class="anchor_top_offset"/>        Step 1: Start <span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon Studio</span>  with remote debugger            mode      

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Start <span className="ph">Katalon Studio</span> via CLI using this command:</p> 
<pre xmlns="http://www.w3.org/1999/xhtml" className="pre codeblock"><code>&lt;katalon_installed_folder&gt;/katalon -vmargs -Xdebug -Xrunjdwp:transport=dt_socket,server=y,suspend=n,address=8000{"\n"}</code></pre> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">The <code className="ph codeph">&lt;katalon_installed_folder&gt;</code> is the   absolute path to Katalon installed folder.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">If you are using macOS, the   <code className="ph codeph">&lt;katalon_installed_folder&gt;</code> should be <code className="ph codeph">/Applications/Katalon Studio.app/Contents/MacOS</code>.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">The <code className="ph codeph">address=8000</code> is a local port number, JVM will   allow a debugger to attach to <span className="ph">Katalon Studio</span> via this port. You can   change to another port if needed.</p> 

## <a id="id_3" class="anchor_top_offset"/>        Step 2: Import your platform plugin to Eclipse IDE as a            Maven project      

<p xmlns="http://www.w3.org/1999/xhtml" className="p">In this example, we will use the last tutorial project: <a className="xref j-external-link" href="https://github.com/katalon-studio/katalon-studio-sample-plugin" target="_blank">katalon-studio-sample-plugin     1</a> to debug.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-store/docs/publisher/import-plugin-project-to-eclipse-ide.png")} width={500} /><br /><br /> </p> 

## <a id="id_4" class="anchor_top_offset"/>        Step 3: Set a breakpoint      

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Open a Java file and set a breakpoint in the code. In this   example, we set the breakpoint in the line of class <a className="xref j-external-link" href="https://github.com/katalon-studio/katalon-studio-sample-plugin/blob/master/src/main/java/com/mycompany/plugin/MyPluginActivationListener.java" target="_blank">MyPluginActivationListener</a>:</p> 
<pre xmlns="http://www.w3.org/1999/xhtml" className="pre codeblock"><code>System.out.println("Hello, my plugin is: " + plugin.getPluginId());{"\n"}</code></pre> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-store/docs/publisher/set-breakpoint.png")} width={700} /><br /><br /> </p> 

## <a id="id_5" class="anchor_top_offset"/>        Step 4: Create a Java Remote Application            Debugger      

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Click on the arrow dropdown of Eclipse debug icon <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-store/docs/publisher/debug-icon.png")} />, choose <code className="ph codeph">Debug Configuration</code> item.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-store/docs/publisher/debug-configurations.png")} width={500} /><br /><br /> </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Right-click on the <code className="ph codeph">Java Remote Application</code> and   choose <code className="ph codeph">New Configuration</code> to add new Remote   Debugger</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-store/docs/publisher/new-configuration.png")} width={600} /><br /><br /> </p> 

## <a id="id_6" class="anchor_top_offset"/> Step 5: Configure the Java Remote Application Debugger 

<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <code className="ph codeph">Browse</code> to your platform plugin project at the text field under <code className="ph codeph">Project</code> section.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Enter the port number you declared at step 1 to the <code className="ph codeph">Port:</code> text field under <code className="ph codeph">Connection Properties</code>section.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Click <code className="ph codeph">Debug</code> to finish setup.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-store/docs/publisher/new-remote-debugger.png")} width={600} /><br /><br /> </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">If your setup is correct, there is the connect icon which will be displayed on Eclipse toolbar. <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-store/docs/publisher/stop-debug-icon.png")} /><br /><br /></p> 

## <a id="id_7" class="anchor_top_offset"/>        Step 6: Import plugin to <span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon Studio</span>  and start            debugging      

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Import your plugin and do your expected actions to make the   breakpoint you placed at step 2 will be hit.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">In this sample, the breakpoint will hit immediately after the   plugin successfully installed.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-store/docs/publisher/breakpoint-hit.png")} /><br /><br /> </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">You now can debug your platform plugin project as a   normal Java project.</p> 

## <a id="id_8" class="anchor_top_offset"/>        Step 7: Disconnect and stop debugging      

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Press the <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-store/docs/publisher/stop-debug-icon.png")} /> icon to disconnect and stop your debugging session.</p> 
