---
hide_title: true
title: TestLink Integration
---
import useBaseUrl from '@docusaurus/useBaseUrl';

    

# <a id="id_testlink-integration" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>TestLink Integration

    
    
  

## <a id="id_1" class="anchor_top_offset"/>TestLink Installation

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">Download XAMPP from Apache Friends: <a className="xref j-external-link" href="https://www.apachefriends.org/download.html" target="_blank">XAMPP</a>. </p></li><li className="li"><p className="p">Upon successful installation, Tomcat will be started by default.</p></li><li className="li"><p className="p">Start the Apache and MySQL services from XAMPP Control Panel.<img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/Testlink/1-XAMPP-control-panel.png")} width={700} alt="TestLink Installation" /><br /><br /></p></li></ul> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">Download the TestLink from SourceForge: <a className="xref j-external-link" href="https://sourceforge.net/projects/testlink/files/TestLink%201.9/" target="_blank">TestLink</a>. You can use the latest version for the integration.</p></li><li className="li"><p className="p">Extract TestLink and place it on <code className="ph codeph">XAMPP/htdocs</code> directory. </p></li><li className="li"><p className="p">Enter this URL in any browser: <code className="ph codeph">http://localhost/phpmyadmin/</code> </p></li><li className="li"><p className="p">Create a new database called <code className="ph codeph">testlink</code> from the database menu.</p></li><li className="li"><p className="p">Add a user account from the <span className="ph uicontrol">Privileges</span> tab under <span className="ph uicontrol">More</span> options for <span className="ph uicontrol">testlink</span> database.<img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/Testlink/2-Add-user-1.png")} width={700} alt="Add user account in TestLink" /><br /><br /></p><p className="p"><img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/Testlink/3-Add-user-2.png")} width={700} alt="Add user account in TestLink" /><br /><br /></p></li></ul> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">Enter this URL in any browser to open the TestLink installation setup: <code className="ph codeph">http://localhost/testlink-1.9.16/install/index.php</code> </p></li><li className="li"><p className="p">Check the <span className="ph uicontrol">I agree to the terms set out in this license</span> checkbox and click <span className="ph uicontrol">Continue</span>.<img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/Testlink/4-Agree-term.png")} width={600} alt="Agree terms in TestLink" /><br /><br /></p></li></ul> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">The below permissions will be failed.<img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/Testlink/5-Testlink-package.png")} width={600} alt="Failed terms in the TestLink package" /><br /><br /></li></ul> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">Navigate to the TestLink package and open the <code className="ph codeph">config.inc.php</code> file.</p></li><li className="li"><div className="p">Update the parameters as below:<pre className="pre codeblock"><code>$tlCfg-&gt;log_path = 'D:/xampp/htdocs/testlink-1.9.16/logs/'; (Path of testlink package){"\n"}$grepositoryPath = 'D:/xampp/htdocs/testlink-1.9.16/uploadarea/'; (Path of testlink package){"\n"}</code></pre></div></li></ul> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">Refresh the page and the above “failed” status will be resolved.</li></ul> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/Testlink/6-Failed-permission.png")} width={700} alt="Resolve failed terms in the TestLink package" /><br /><br /></p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">Click <span className="ph uicontrol">Continue</span>.</p></li><li className="li"><p className="p">Enter the Database name as <code className="ph codeph">testlink</code>.</p></li><li className="li"><p className="p">Enter the Database admin login and password as <code className="ph codeph">admin</code>.</p></li><li className="li"><p className="p">Enter your database username and password for “TestLink DB login and password”.<img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/Testlink/7-Process-testlink-setup.png")} width={500} alt="Set up Testlink" /><br /><br /></p></li></ul> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">Click <span className="ph uicontrol">Process TestLink Setup!</span>.</p></li><li className="li"><p className="p">Once the installation is completed, a window displays to notify that the installation is successful.<img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/Testlink/8-Successful.png")} width={600} alt="Successfully install Testlink" /><br /><br /></p></li></ul> 

## <a id="id_2" class="anchor_top_offset"/>TestLink Login

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">Enter this URL to login to TestLink: <code className="ph codeph">http://localhost/testlink-1.9.16/</code> </p></li><li className="li"><p className="p">Enter the Login Name and Password as <code className="ph codeph">admin</code> to login as admin.<img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/Testlink/9-Testlink-login.png")} width={500} alt="Login Testlink" /><br /><br /></p></li></ul> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">Once you login to TestLink, it prompts to create a Test Project.</p></li><li className="li"><p className="p">Create a Test Plan, Build, Test suite with Test cases by selecting the corresponding links from the Dashboard.</p></li></ul> 

## <a id="id_3" class="anchor_top_offset"/>Test Project Creation

<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/Testlink/10-Test-project-creation.png")} alt="Create test project in Testlink" /><br /><br /> </p> 

## <a id="id_4" class="anchor_top_offset"/>Test Plan Creation

<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/Testlink/11-Test-plan-creation.png")} alt="Create test plan in Testlink" /><br /><br /> </p> 

## <a id="id_5" class="anchor_top_offset"/>Build Creation

<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/Testlink/12-Build-creation.png")} alt="Build creation in Testlink" /><br /><br /> </p> 

## <a id="id_6" class="anchor_top_offset"/>Test Suite Creation

<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/Testlink/13-Test-suite-creation.png")} alt="Test suite creation in Testlink" /><br /><br /> </p> 

## <a id="id_7" class="anchor_top_offset"/>Test Case Creation

<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/Testlink/14-Test-case-creation.png")} alt="Test case creation in Testlink" /><br /><br /> </p> 

## <a id="id_8" class="anchor_top_offset"/>API Key Generation and Execution Type Changes on TestLink

<ol xmlns="http://www.w3.org/1999/xhtml" className="ol"><li className="li">Generate the API Key on TestLink as below. <ul className="ul"><li className="li">Click on <span className="ph uicontrol">My Settings</span>.</li><li className="li">Personal API access Key will be <span className="ph uicontrol">none</span> under the <span className="ph uicontrol">API Interface</span> section.</li><li className="li">Click <span className="ph uicontrol">Generate a new key</span>.</li><li className="li">Key will be generated from <span className="ph uicontrol">Personal API access key</span>.<p className="p"><img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/Testlink/15-API-key.png")} alt="Create API key in Testlink" /><br /><br /></p></li></ul></li><li className="li">After generating a key, update the test execution status as <span className="ph uicontrol">Automated</span> as below.<img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/Testlink/16-Automated-status.png")} width={700} alt="Create API key in Testlink" /><br /><br /></li></ol> 

## <a id="id_9" class="anchor_top_offset"/>Integration of Katalon test scripts with TestLink

<p xmlns="http://www.w3.org/1999/xhtml" className="p">First, go to Katalon Store and install the plugin: <a className="xref j-external-link" href="https://store.katalon.com/product/71/TestLink-Integration" target="_blank">TestLink Integration</a>. Then, open Katalon Studio and reload plugin. See <a className="xref" href="/katalon-platform/plugins-and-add-ons/katalon-store/katalon-studio-plugins/installing-plugin-offline-in-katalon-studio#id_2">Reload your plugins in <span className="ph">Katalon Studio</span></a>.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Make a note of the TestLink Key, TestLink Url, Project Name, Test Plan Name, and Build Name created on TestLink. These details need to be used in our configuration in below:</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Go to <strong className="ph b">Project &gt; Settings &gt; Plugins &gt; TestLink Integration</strong> and setup these following configurations:</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/Testlink/KS-TESTLINK-Enable-Testlink.png")} alt="Enable TestLink Integration" /><br /><br /></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">This plugin provides the only custom keyword <code className="ph codeph">updateResults</code> to update the test results on TestLink.</p> 

## <a id="id_10" class="anchor_top_offset"/>Test Execution Results update on TestLink

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Before execution, the test status will be <span className="ph uicontrol">Not Run</span> on TestLink. If the test case is passed, the status will be updated as <span className="ph uicontrol">Passed</span>.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/Testlink/18-Passed.png")} width={500} alt="View test results in Testlink" /><br /><br /></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">If the test case is failed, the status will be updated as <span className="ph uicontrol">Failed</span>.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/Testlink/19-Failed.png")} width={500} alt="View test results in Testlink" /><br /><br /></p> 
