---
hide_title: true
title: Use Katalon plugins for Jenkins integration on Windows/macOS
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="id" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Use Katalon plugins for Jenkins integration on  Windows/macOS

This tutorial shows you how to integrate Katalon with Jenkins on Windows and macOS via the Katalon plugin for Jenkins.

:::tip requirements
- An active Katalon Runtime Engine license. To learn more about activating the Katalon Runtime Engine license, you can refer to this document: [Activate Katalon License](/katalon-studio/get-started/activate-licenses).
:::

## <a id="id_1" class="anchor_top_offset"/>Installation

<div xmlns="http://www.w3.org/1999/xhtml" className="p">Install Jenkins. Follow the instructions in the following
  Jenkins documents:<ul className="ul"><li className="li"><p className="p">For Windows: <a className="xref j-external-link" href="https://www.jenkins.io/doc/book/installing/windows/" target="_blank">Windows</a></p></li><li className="li"><p className="p">For macOS: <a className="xref j-external-link" href="https://www.jenkins.io/doc/book/installing/macos/" target="_blank">macOS</a></p></li></ul></div>
    

## <a id="id_2" class="anchor_top_offset"/>Execute Katalon Studio tests in Jenkins with the Katalon         plugin

    
      

### <a id="task-3099" class="anchor_top_offset"/>Install the Katalon plugin on Jenkins

<section xmlns="http://www.w3.org/1999/xhtml" className="section context">To run Katalon tests on Jenkins, you need to install the Katalon plugin on Jenkins. Do as follows:</section> 
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol steps"><li className="li step stepexpand"><span className="ph cmd">Sign in to Jenkins and go to <span className="ph uicontrol">Manage Jenkins</span> &gt;   <span className="ph uicontrol">Manage Plugins</span>. </span><div className="itemgroup stepresult">The <span className="ph uicontrol">Plugin Manager</span> page appears.</div></li><li className="li step stepexpand"><span className="ph cmd">Click on the <span className="ph uicontrol">Available</span> tab and search for the Katalon plugin.</span><div className="itemgroup info"><img className="image" width={850} src={useBaseUrl("/c1d37300-6af7-11ed-a602-0242cfbc79b5/jenkins-install-plugin.png")} alt="plugin-manager" /></div></li><li className="li step stepexpand"><span className="ph cmd">Select the plugin and choose  <span className="ph uicontrol">Install without restart</span>.</span></li></ol> 

### <a id="concept-2352" class="anchor_top_offset"/>Upload Katalon projects on Jenkins

<p xmlns="http://www.w3.org/1999/xhtml" className="p">After installing the <strong className="ph b">Katalon</strong> plugin, you can now start the Katalon Studio test in Jenkins.</p> 
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol"><li className="li">     <p className="p">In the Jenkins Dashboard, go to <strong className="ph b">New Item</strong> and create a <strong className="ph b">Freestyle project</strong>.</p>     <p className="p"><img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/jenkins-plugin-windows/KS-JENKINS-Create-a-freestyle-project.png")} alt="Create a new Freestyle project" /><br /><br /></p>   </li><li className="li">     <p className="p">To upload your Katalon project on Jenkins, you can upload your Katalon project from a Git repository or your local workspace. Here, we use a Git repository.</p>     <ul className="ul"><li className="li">In the <strong className="ph b">Source Code Management</strong> section, choose <strong className="ph b">Git</strong>.</li><li className="li">         <p className="p">Enter your repository URL, then select branches to build, repository browser, and additional behaviors, if any.</p>         <p className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/jenkins-plugin-windows/Picture4.png")} alt="Upload Katalon project" /><br /><br />         </p>       </li></ul>   </li></ol> 

### <a id="concept-3999" class="anchor_top_offset"/>Build your project

<ol xmlns="http://www.w3.org/1999/xhtml" className="ol anchor_top_offset" id="concept-3999__ol-2106"><li className="li">     <p className="p">In the <strong className="ph b">Build</strong> section, click <strong className="ph b">Add build step</strong> and choose <strong className="ph b">Execute Katalon Studio Tests</strong>. The <strong className="ph b">Execute Katalon Studio Tests</strong> box opens, asking you to input the Katalon Runtime Engine version and command arguments.<img className="image" src={useBaseUrl("/c20865b0-6af7-11ed-a602-0242cfbc79b5/Jenkins_-_Execute_Katalon_Studio_Tests.png")} alt="jenkins - Execute Katalon Studio Tests" /></p>   </li><li className="li">     <p className="p">Specify the Katalon Studio version you wish to execute with:</p>     <ul className="ul"><li className="li">If you haven't downloaded Katalon Runtime Engine (KRE), you can input the KRE version you wish to execute with in the <strong className="ph b">Download Katalon Studio version</strong> box. KRE will be downloaded and deployed automatically. You can retrieve the list of all releases on our Github repository: <a className="xref j-external-link" href="https://github.com/katalon-studio/katalon-studio/releases" target="_blank">Releases</a>. </li><li className="li">If you want to use a pre-installed version, manually input the KRE version you have installed in the <strong className="ph b">Use pre-installed Katalon Studio</strong> box with the following command line: <pre className="pre codeblock"><code>&lt;KRE stored folder&gt;-&lt;KRE pre-installed-version&gt;</code></pre>For example: <code className="ph codeph">/Users/USERNAME/Downloads/Katalon_Studio_Engine_MacOS-8.1.0</code>.</li></ul>   </li><li className="li">     <p className="p">Input your command in the <strong className="ph b">Command arguments</strong> box:</p>     <p className="p">Here is a sample of command arguments to run test with TestCloud configurations. You can generate the Command arguments for tests with TestCloud configurations by using Katalon Studio <a className="xref j-external-link" href="https://docs.katalon.com/docs/execute/cloud-based-test-execution/test-execution-with-testcloud/integrate-testcloud-with-katalon-runtime-engine" target="_blank">Command Builder</a>. To understand about the syntax of the command, see: <a className="xref j-external-link" href="https://docs.katalon.com/docs/execute/katalon-runtime-engine/command-line-syntax-in-katalon-runtime-engine" target="_blank">Command-Line Syntax in Katalon Runtime Engine</a>. </p>     <pre className="pre codeblock"><code>-browserType="Chrome" -retry=0 -statusDelay=15 -testSuitePath="Test Suites/TS_RegressionTest" -apikey=&lt;YOUR_API_KEY&gt;{"\n"}{"\n"}</code></pre><img className="image" src={useBaseUrl("/c1b69c30-6af7-11ed-a602-0242cfbc79b5/jenkins-sample-command.png")} alt="jenkins build command arguments" />     <div className="note warning note_warning"><span className="note__title">Warning:</span>        <ul className="ul"><li className="li">           <p className="p">When you use the <strong className="ph b">Katalon</strong> plugin on Jenkins, or copying commands generated by Command Builder from Katalon Studio, please remove argument <code className="ph codeph">-noSplash</code> and <code className="ph codeph">-runMode=console</code>.</p>         </li></ul>     </div>     <div className="note note note_note"><span className="note__title">Note:</span>        <ul className="ul"><li className="li">If you belong to more than one Organization subscribing to Runtime Engine licenses, you can choose which Organization validates your license usage with the following command line: <code className="ph codeph">-orgID=&lt;Katalon_OrgID&gt;</code>.</li><li className="li">Make sure your current browser version is compatible with the KRE Webdriver version. To learn more about upgrading or downgrading WebDrivers, you can refer to this document: <a className="xref" href="/katalon-studio/manage-projects/set-up-projects/web-testing/handle-webdrivers/upgrade-or-downgrade-webdrivers-in-katalon-studio#id_2">Update or Downgrade WebDrivers</a>.</li></ul>     </div>   </li><li className="li">     <p className="p">After you are done with the configuration, click <strong className="ph b">Save</strong>, then click <strong className="ph b">Build Now</strong> to run the project.</p>   </li><li className="li">     <p className="p">To view the console log, click on your current build on Jenkins and select <strong className="ph b">Console Output</strong>.</p>     <p className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/jenkins-plugin-windows/KS-JENKINS-console-output.png")} alt="View console output" /><br /><br />     </p>   </li></ol> 

### <a id="concept-3080" class="anchor_top_offset"/>Troubleshoot empty videos recorded after running tests on Windows

<p xmlns="http://www.w3.org/1999/xhtml" className="p">If you encounter an issue of having empty videos recorded after running your tests in Jenkins on Window, it is because the WebDriver hasn't launched during test execution. To fix this issue, please uninstall Jenkins of Windows services, and replace it by a DOS batch file containing the following codes:</p> 
<pre xmlns="http://www.w3.org/1999/xhtml" className="pre codeblock"><code>cd D:\Tools\Jenkins //path to Jenkins folder{"\n"}java -jar --webroot=jenkins.war{"\n"}</code></pre> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <em className="ph i">Code sample courtesy of Sébastien Taniere</em> </p> 
    

## <a id="id_7" class="anchor_top_offset"/>See also

    
      
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul">   <li className="li">     <a className="xref" href="#">Execute       Katalon Studio tests with Jenkins Pipeline Script       (Jenkinsfile)</a>.</li> </ul> 
    
  
