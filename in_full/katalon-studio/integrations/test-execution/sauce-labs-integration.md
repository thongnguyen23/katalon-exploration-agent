---
hide_title: true
title: Sauce Labs integration
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="id" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Sauce Labs integration

<div xmlns="http://www.w3.org/1999/xhtml" className="note important note_important"><span className="note__title">Important:</span> <ul className="ul"><li className="li"><p className="p">An active Katalon Studio Enterprise license. To learn more about activating your license, you can refer to this document: <a className="xref" href="/katalon-studio/get-started/activate-licenses">Activate Katalon license</a>.</p></li></ul></div>
    

## <a id="id_1" class="anchor_top_offset"/>Install the Sauce Labs Integration plugin

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Download and install the <strong className="ph b">Sauce Labs Integration</strong>   plugin. You can download the plugin from the Katalon Store here: <a className="xref j-external-link" href="https://store.katalon.com/product/75/Sauce-Labs-Integration#pricing-content" target="_blank">Sauce     Labs Integration</a>.</p> 
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">To activate the plugin, navigate to Account Settings in Katalon   Studio and click <strong className="ph b">Reload Plugin</strong>.</p> 
    
## <a id="id_2" class="anchor_top_offset"/>Sauce Labs for WebUI testing

### <a id="id_3" class="anchor_top_offset"/>Create a default Sauce Labs custom profile from the plugin

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Go to <strong className="ph b">Project &gt; Settings &gt; Plugins &gt; Sauce Labs Integration</strong>. Enter your credentials and your desired Sauce Labs operating environments and systems, including:</p> 
<table xmlns="http://www.w3.org/1999/xhtml" className="table anchor_top_offset" id="id_3__8a404094-5829-4910-b649-28740c46f0d6"><caption /><thead className="thead"><tr className><th className="entry anchor_top_offset" id="id_3__8a404094-5829-4910-b649-28740c46f0d6__entry__1">Information</th><th className="entry anchor_top_offset" id="id_3__8a404094-5829-4910-b649-28740c46f0d6__entry__2">Description</th></tr></thead><tbody className="tbody"><tr className><td className="entry" headers="id_3__8a404094-5829-4910-b649-28740c46f0d6__entry__1 id_3__8a404094-5829-4910-b649-28740c46f0d6__entry__2 ">API Key</td><td className="entry" headers="id_3__8a404094-5829-4910-b649-28740c46f0d6__entry__1 id_3__8a404094-5829-4910-b649-28740c46f0d6__entry__2 ">An API Key is the Access Key generated from the User Settings in Sauce Labs. You can refer to this Sauce Labs document for further details about retrieving the API key: <a className="xref j-external-link" href="https://docs.saucelabs.com/basics/acct-team-mgmt/managing-user-info/#user-settings" target="_blank">User Settings</a>.</td></tr><tr className><td className="entry" headers="id_3__8a404094-5829-4910-b649-28740c46f0d6__entry__1 id_3__8a404094-5829-4910-b649-28740c46f0d6__entry__2 ">Username</td><td className="entry" headers="id_3__8a404094-5829-4910-b649-28740c46f0d6__entry__1 id_3__8a404094-5829-4910-b649-28740c46f0d6__entry__2 ">Your username displayed in Sauce Labs. You can retrieve the Sauce Labs username in the User Settings.</td></tr><tr className><td className="entry" headers="id_3__8a404094-5829-4910-b649-28740c46f0d6__entry__1 id_3__8a404094-5829-4910-b649-28740c46f0d6__entry__2 ">Browser's name</td><td className="entry" headers="id_3__8a404094-5829-4910-b649-28740c46f0d6__entry__1 id_3__8a404094-5829-4910-b649-28740c46f0d6__entry__2 ">The execution browser you want to execute with. For example, Safari.</td></tr><tr className><td className="entry" headers="id_3__8a404094-5829-4910-b649-28740c46f0d6__entry__1 id_3__8a404094-5829-4910-b649-28740c46f0d6__entry__2 ">Platform</td><td className="entry" headers="id_3__8a404094-5829-4910-b649-28740c46f0d6__entry__1 id_3__8a404094-5829-4910-b649-28740c46f0d6__entry__2 ">The operating system you want to execute with. For example, macOS 10.13</td></tr><tr className><td className="entry" headers="id_3__8a404094-5829-4910-b649-28740c46f0d6__entry__1 id_3__8a404094-5829-4910-b649-28740c46f0d6__entry__2 ">Version</td><td className="entry" headers="id_3__8a404094-5829-4910-b649-28740c46f0d6__entry__1 id_3__8a404094-5829-4910-b649-28740c46f0d6__entry__2 ">The browser version you want to execute with. For example, you want to run with Safari 11.1, input <code className="ph codeph">11.1</code>.</td></tr><tr className><td className="entry" headers="id_3__8a404094-5829-4910-b649-28740c46f0d6__entry__1 id_3__8a404094-5829-4910-b649-28740c46f0d6__entry__2 ">Job's Name</td><td className="entry" headers="id_3__8a404094-5829-4910-b649-28740c46f0d6__entry__1 id_3__8a404094-5829-4910-b649-28740c46f0d6__entry__2 ">The test case name you want to present in Sauce Labs. By default, this is set to <strong className="ph b">Default Job</strong>.</td></tr></tbody></table> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Click <strong className="ph b">Generate Sauce Labs Custom Profile</strong> to finalize your profile.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/saucelabs-plugin/KS-SAUCELABS-Enable-saucelabs-integration.png")} alt="Enable Sauce Labs integration" /><br /><br /> </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">To view the newly created custom profile, go to <strong className="ph b">Projects &gt; Settings &gt; Desired Capabilities &gt; Custom</strong>.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/saucelabs-plugin/KS-SAUCELABS-View-custom-saucelabs-profiles.png")} alt="View Sauce Labs custom profile" /><br /><br /> </p> 

:::info notes
The default custom profile is named `saucelabs_default`.
:::

:::warning known issues
You can only edit the default custom profile properties from the **Sauce Labs Integration** generator in **Project > Settings > Plugins > Sauce Labs Integration**.
:::

### <a id="id_4" class="anchor_top_offset"/>Create a Sauce Labs custom profile using custom desired capabilities

<p xmlns="http://www.w3.org/1999/xhtml" className="p">You can also create a new Sauce Labs custom profile using custom desired capabilities. To do so:</p> 
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol"><li className="li">     <p className="p">Go to <strong className="ph b">Projects &gt; Settings &gt; Desired Capabilities &gt; Custom</strong>.</p>   </li><li className="li">     <p className="p">Click <strong className="ph b">Add</strong>, then name the new custom profile with the following syntax: <code className="ph codeph">saucelabs_&lt;your-custom-profile-name&gt;</code>. Here, we name our profile <code className="ph codeph">saucelabs_custom</code>.</p>   </li><li className="li">     <p className="p">Click on <em className="ph i">More</em> (...) under the <strong className="ph b">Value</strong> column. In the <strong className="ph b">Custom Execution Configuration Builder</strong> dialog, click <strong className="ph b">Add</strong>, then choose <strong className="ph b">Remote</strong>.</p>   </li><li className="li">     <p className="p">Click on <em className="ph i">More</em> (...) under the <strong className="ph b">Preferences</strong> column. In the pop-up <strong className="ph b">Driver Builder</strong> dialog, specify as follows:</p>     <ul className="ul"><li className="li"> <strong className="ph b">Remote server URL</strong>: specify the Driver Creation URL in Sauce Labs. To find the Driver Creation URL, open your Sauce Labs account, go to <strong className="ph b">Account</strong> &gt; <strong className="ph b">User settings</strong>, then scroll to the <strong className="ph b">Driver Creation</strong> section.</li></ul>     <p className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/saucelabs-plugin/KS-SAUCELABS-Driver-URL.png")} alt="Add Sauce Labs custom profile via desired capabilities" /><br /><br />     </p>     <ul className="ul"><li className="li">         <p className="p"> <strong className="ph b">Remote server type</strong>: choose <strong className="ph b">Selenium</strong>.</p>       </li><li className="li">         <p className="p">Specify your Sauce Labs <code className="ph codeph">username</code>, <code className="ph codeph">accessKey</code>.</p>       </li><li className="li">Add other properties for your execution environment. You can refer to the Sauce Labs platform configuration here: <a className="xref j-external-link" href="https://saucelabs.com/platform/platform-configurator" target="_blank">Platform configuration</a>.</li></ul>     <p className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/saucelabs-plugin/KS-SAUCELABS-Desired-capabilities.png")} alt="Add Sauce Labs custom profile via desired capabilities" /><br /><br />`</p>     <p className="p">You can now use the newly created profile to execute tests.</p>   </li></ol> 

### <a id="concept-7793" class="anchor_top_offset"/>Execute a test case with Sauce Labs profiles

To execute a test case with Sauce Labs profiles, do as follows:

1. Open a test case.
2. Click the dropdown list next to **Run**.
3. Select **Custom capabilities**.
4. Select your Sauce Labs profile.

    <img src="https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/saucelabs-plugin/830-KS-SAUCELABS-Execute-test-case-saucelabs-profile.png" alt="KS saucelabs execute test case profile screen" />

### <a id="id_6" class="anchor_top_offset"/>Execute a test suite with Sauce Labs profiles

<p xmlns="http://www.w3.org/1999/xhtml" className="p">To execute a test suite with Sauce Labs profiles, do as follows:</p> 
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol"><li className="li">     <p className="p">Open a test suite.</p>   </li><li className="li">     <p className="p">Add the test cases you want to execute into the test suite.</p>   </li><li className="li">     <p className="p">Click the dropdown list next to <strong className="ph b">Run</strong>.</p>   </li><li className="li">     <p className="p">Select <strong className="ph b">Custom capabilities</strong>.</p>   </li><li className="li">     <p className="p">Select your Sauce Labs profile.</p>   </li></ol> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/saucelabs-plugin/KS-SAUCELABS-Execute-test-suite-saucelabs-profile.png")} alt="Execute Sauce Labs custom profile in a test suite" /><br /><br /> </p> 

### <a id="id_7" class="anchor_top_offset"/>Execute a test suite collection with Sauce Labs profiles

<p xmlns="http://www.w3.org/1999/xhtml" className="p">To execute a test suite collection with Sauce Labs profiles, do as follows:</p> 
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol"><li className="li"><p className="p">Open a test suite collection.</p></li><li className="li"><p className="p">Add the test suites you want to execute into the test suite collection.</p></li><li className="li"><p className="p">Double-click on the cell under the <strong className="ph b">Run with</strong> column. A <strong className="ph b">Select an environment</strong> dialog opens.</p><p className="p"><img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/saucelabs-plugin/KS-SAUCELABS-Select-environment-test-suite-collection.png")} alt="Choose Sauce Labs custom profile in a test suite collection" /><br /><br /></p></li><li className="li"><p className="p">Select your Sauce Labs profile.</p><p className="p"><img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/saucelabs-plugin/KS-SAUCELABS-Select-environment-TSC.gif")} alt="Choose Sauce Labs custom profile in a test suite collection" /><br /><br /></p></li><li className="li"><p className="p">Click <strong className="ph b">OK.</strong> Then click <strong className="ph b">Execute</strong>.</p><p className="p"><img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/saucelabs-plugin/KS-SAUCELABS-Execute-test-suite-collection-saucelabs-profile.png")} alt="Execute Sauce Labs custom profile in a test suite collection" /><br /><br /></p></li></ol> 

### <a id="id_8" class="anchor_top_offset"/>View test execution results on Sauce Labs

<p xmlns="http://www.w3.org/1999/xhtml" className="p">To view Katalon test execution results on Sauce Labs, on the Sauce Labs Dashboard, switch to the <strong className="ph b">Automated &gt; Test Results</strong> tab.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">You can see the test results displayed as follows:</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/saucelabs-plugin/KS-SAUCELABS-Uploaded-test-results.png")} alt="View test execution results in Sauce Labs" /><br /><br /> </p> 

:::info notes
- If you are running with the `saucelabs_default` profile, your test result is uploaded to the **US West 1** data center.
- Make sure to select the correct data center that you specify in the **Remote server URL** of your Sauce Labs custom profile.
    
    <img src="https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/saucelabs-plugin/KS-SAUCELABS-data-center.png" alt="Saucelabs plugin Data center screen" />
:::

## <a id="id_9" class="anchor_top_offset"/>Sauce Labs for mobile testing and hybrid application testing

<p xmlns="http://www.w3.org/1999/xhtml" className="p">To enable mobile and hybrid application testing with Sauce Labs profiles, you need to manually add capabilities in <strong className="ph b">Projects &gt; Settings &gt; Desired Capabilities &gt; Custom</strong>.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/saucelabs-plugin/KS-SAUCELABS-Add-saucelabs-profile-mobile-testing.png")} alt="Add custom profile for mobile testing" /><br /><br /> </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Then add mobile and hybrid application testing capabilities in the Sauce Labs document here: <a className="xref j-external-link" href="https://docs.saucelabs.com/mobile-apps/automated-testing/appium/real-devices/" target="_blank">Appium Testing with Real Devices</a>.</p> 
