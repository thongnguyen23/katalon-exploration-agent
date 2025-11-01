---
hide_title: true
title: Use Katalon plugins for Jenkins integration on Ubuntu
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="id" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Use Katalon plugins for Jenkins integration on Ubuntu

<p xmlns="http://www.w3.org/1999/xhtml" className="p">This tutorial  walks you through basic steps to run Katalon   Studio tests using Katalon plugin for Jenkins  on a headless Ubuntu machine i.e. a machine without any   display. You can find the plugin on Jenkins here: <a className="xref j-external-link" href="https://plugins.jenkins.io/katalon" target="_blank">Katalon</a>.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">If you are interested in using Docker images instead, you can refer to our sample project on GitHub:  <a className="xref j-external-link" href="https://github.com/katalon-studio-samples/ci-samples" target="_blank">ci-samples</a>.</p> 

## <a id="id_1" class="anchor_top_offset"/>Install Jenkins on Ubuntu

<p xmlns="http://www.w3.org/1999/xhtml" className="p">To install Jenkins, follow the instructions in this Jenkins document: <a className="xref j-external-link" href="https://jenkins.io/doc/book/installing/#debianubuntu" target="_blank">Debian/Ubuntu</a>.</p> 
    

## <a id="id_2" class="anchor_top_offset"/>Install Google Chrome

    
              
<pre xmlns="http://www.w3.org/1999/xhtml" className="pre codeblock"><code>wget -O google-chrome-stable_current_amd64.deb https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb{"\n"}sudo dpkg -i google-chrome-stable_current_amd64.deb{"\n"}sudo apt -y -f install{"\n"}</code></pre> 
          
  
    

## <a id="id_3" class="anchor_top_offset"/>Install Xvfb

    
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">From <a className="xref j-external-link" href="https://en.wikipedia.org/wiki/Xvfb" target="_blank">Wikipedia</a>:</p> 
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">"Xvfb or X virtual framebuffer is a display server implementing   the X11 display server protocol. In contrast to other display   servers, Xvfb performs all graphical operations in virtual memory   without showing any screen output. From the point of view of the   client, it acts exactly like any other X display server, serving   requests and sending events and errors as appropriate. However, no   output is shown. This virtual server does not require the computer   it is running on to have any kind of graphics adapter, a screen or   any input device. Only a network layer is necessary."</p> 
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <code className="ph codeph">sudo apt install -y xvfb</code> </p> 
    
  

## <a id="task-3099" class="anchor_top_offset"/>Install the Katalon plugin on Jenkins

<section xmlns="http://www.w3.org/1999/xhtml" className="section context">To run Katalon tests on Jenkins, you need to install the Katalon plugin on Jenkins. Do as follows:</section> 
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol steps"><li className="li step stepexpand"><span className="ph cmd">Sign in to Jenkins and go to <span className="ph uicontrol">Manage Jenkins</span> &gt;   <span className="ph uicontrol">Manage Plugins</span>. </span><div className="itemgroup stepresult">The <span className="ph uicontrol">Plugin Manager</span> page appears.</div></li><li className="li step stepexpand"><span className="ph cmd">Click on the <span className="ph uicontrol">Available</span> tab and search for the Katalon plugin.</span><div className="itemgroup info"><img className="image" width={850} src={useBaseUrl("/c1d37300-6af7-11ed-a602-0242cfbc79b5/jenkins-install-plugin.png")} alt="plugin-manager" /></div></li><li className="li step stepexpand"><span className="ph cmd">Select the plugin and choose  <span className="ph uicontrol">Install without restart</span>.</span></li></ol> 

## <a id="id_5" class="anchor_top_offset"/>Create and configure a new Jenkins project

<p xmlns="http://www.w3.org/1999/xhtml" className="p">To keep it simple, I will use <em className="ph i">Freestyle project</em>.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <img className="image" src={useBaseUrl("https://raw.githubusercontent.com/katalon-studio/docs-images/master/katalon-studio/docs/jenkins-docker/new-item.png")} alt="jenkins docker" /><br /><br /> </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">The sample Katalon Studio project can be cloned from <a className="xref j-external-link" href="https://github.com/katalon-studio-samples/ci-samples" target="_blank">Github</a>.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/jenkins-plugin-ubuntu/Picture3.png")} alt="source code management" /><br /><br /> </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Next, add and configure the build step <em className="ph i">Execute Katalon Studio tests</em> provided by Katalon plugin for Jenkins.</p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">Katalon Studio will be downloaded and installed automatically based on the version you specify.</li><li className="li">Leave out <code className="ph codeph">-runMode</code> in the arguments list.</li><li className="li">If you want to learn more about <code className="ph codeph">xvfb-run</code> configuration please see <a className="xref j-external-link" href="http://manpages.ubuntu.com/manpages/xenial/man1/xvfb-run.1.html" target="_blank">its manual</a>. If you are not sure, only change the resolution <code className="ph codeph">1024x768x24</code> and leave other options as-is.</li></ul> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/jenkins-plugin-ubuntu/Picture4.png")} alt="execute katalon studio tests" /><br /><br /> </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/jenkins-plugin-ubuntu/Picture5.png")} alt="publish test result report" /><br /><br /> </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">If for some network conditions the Katalon Studio package cannot be downloaded, you can install it manually and specify its location.</p> 
<pre xmlns="http://www.w3.org/1999/xhtml" className="pre codeblock"><code>me@ubuntu:~$ sudo su{"\n"}root@ubuntu:~$ su jenkins{"\n"}jenkins@ubuntu:~$ wget https://github.com/katalon-studio/katalon-studio/releases/download/v5.10.1/Katalon_Studio_Linux_64-5.10.1.tar.gz{"\n"}jenkins@ubuntu:~$ tar -xzf Katalon_Studio_Linux_64-5.10.1.tar.gz{"\n"}jenkins@ubuntu:~$ cd Katalon_Studio_Linux_64-5.10.1 &amp;&amp; pwd{"\n"}</code></pre> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">The last command will print the location you need (<code className="ph codeph">/var/lib/jenkins/Katalon_Studio_Linux_64-5.10.1</code>).</p> 

## <a id="id_6" class="anchor_top_offset"/>Run the Jenkins job

Go to the Jenkins project page (e.g. at `http://localhost:8060/jenkins/job/test/` if its name is “test”), click **Build Now**.

After it is complete, you can find the report in the *Last Successful Artifacts* section.


### <a id="troubleshooting-1428" class="anchor_top_offset"/>Troubleshoot: Unable to init server: Could not connect: Connection refused

<section xmlns="http://www.w3.org/1999/xhtml" className="section condition"><p className="p">When you run your test with Jenkins on Ubuntu using the Katalon plugin, you might encounter the error: <em className="ph i">"Unable to init server: Could not connect: Connection refused"</em></p></section> 
<div xmlns="http://www.w3.org/1999/xhtml" className="bodydiv troubleSolution"><section className="section remedy"><div className="li step p"><span className="ph cmd">To resolve this error, make sure  your Ubuntu machine uses OpenJDK 8. You can verify the version of the JDK  using the command: <code className="ph codeph">java -version</code></span></div></section></div>

### <a id="troubleshooting-9307" class="anchor_top_offset"/>Troubleshooting: java.io.IOException: Permission denied

<section xmlns="http://www.w3.org/1999/xhtml" className="section condition"><p className="p">When you run your test with Jenkins on Ubuntu using the Katalon plugin for Jenkins, you might encounter the error: <em className="ph i">"java.io.IOException: Permission denied"</em></p></section> 
<div xmlns="http://www.w3.org/1999/xhtml" className="bodydiv troubleSolution"><section className="section cause"><p className="p">This error occurs because Jenkins requires  permission to read, write, and execute the Katalon project folders. </p></section><section className="section remedy"><div className="li step p"><span className="ph cmd">To resolve this error, run the following command to grant   permission for Jenkins to read, write, and execute files:</span><div className="itemgroup info"><pre className="pre codeblock"><code>$sudo chmod -R 777 &lt;path to your Katalon project folder&gt;</code></pre><div className="p">For example: <pre className="pre codeblock"><code>$sudo chmod -R 777 /home/ubuntu/Katalon\ Studio/testingisfun/</code></pre></div></div></div></section></div>
