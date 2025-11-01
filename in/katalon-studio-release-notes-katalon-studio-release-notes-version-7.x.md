---
hide_title: true
title: 'Katalon Studio Release Notes: Version 7.x'
---

# <a id="id_version-70" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Katalon Studio Release Notes: Version 7.x


## <a id="id_1" class="anchor_top_offset"/>Official Release - Version 7.9.1


:::info notes
- If you upgrade from v7.9.0, you can use **Help** > **Check for updates...** for an in-app upgrade. [Learn more](/katalon-studio/get-started/workspace-settings/update-katalon-studio)
- If you currently use a version prior to v7.9.0, download the latest version from [our website](https://www.katalon.com/download/). To reuse Preferences from previous versions, refer to [this guide](/katalon-studio/get-started/workspace-settings/katalon-studio-preferences/preferences-in-katalon-studio).
:::

### <a id="id_2" class="anchor_top_offset"/>Improvements

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul">   <li className="li">Support Chrome 88.</li>   <li className="li">Support Microsoft Edge (Chromium) 88.</li> </ul> 
      
### <a id="id_3" class="anchor_top_offset"/>Fixes

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul">   <li className="li">Bug: [Web Testing] Cannot run assertion test steps with the     active web driver.</li>   <li className="li">Bug: Cannot export execution reports manually on Windows     machines.</li>   <li className="li">Bug: [Katalon Runtime Engine] Cannot run the command generated     by Command Builder due to the <code className="ph codeph">apiKeyOnPremise</code>     parameter.</li>   <li className="li">Bug: An error displayed when moving the Search tab.</li>   <li className="li">Bug: An error displayed when using Ctrl+Shift+O to remove     libraries while scripting.</li> </ul> 
      
## <a id="id_4" class="anchor_top_offset"/>Version 7.9.0

:::info notes
You will not be able to use **Check for updates...** to upgrade to v7.9+ due to the core engine upgrade (but you can upgrade from v7.9 to later versions via **Check for updates...**).

- Download the latest version from [our website](https://www.katalon.com/download/).
- To reuse Preferences from previous versions, refer to [this guide](/katalon-studio/get-started/workspace-settings/katalon-studio-preferences/preferences-in-katalon-studio).
:::

### <a id="id_5" class="anchor_top_offset"/>New features

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">Support screenshot taking keywords for Mobile and Web testing, including: <ul className="ul"><li className="li">[Mobile] <a className="xref" href="/katalon-studio/keywords/keyword-description-in-katalon-studio/visual-based-mobile-testing-keywords/mobile-take-screenshot-as-checkpoint">Take Screenshot As Checkpoint</a></li><li className="li">[Mobile] <a className="xref" href="/katalon-studio/keywords/keyword-description-in-katalon-studio/mobile-keywords/mobile-take-element-screenshot">Take Element Screenshot</a></li><li className="li">[Mobile] <a className="xref" href="/katalon-studio/keywords/keyword-description-in-katalon-studio/visual-based-mobile-testing-keywords/mobile-take-element-screenshot-as-checkpoint">Take Element Screenshot As Checkpoint</a></li><li className="li">[Mobile] <a className="xref" href="/katalon-studio/keywords/keyword-description-in-katalon-studio/mobile-keywords/mobile-take-area-screenshot">Take Area Screenshot</a></li><li className="li">[Mobile] <a className="xref" href="/katalon-studio/keywords/keyword-description-in-katalon-studio/visual-based-mobile-testing-keywords/mobile-take-area-screenshot-as-checkpoint">Take Area Screenshot As Checkpoint</a></li><li className="li">[WebUI] <a className="xref" href="/katalon-studio/keywords/keyword-description-in-katalon-studio/web-ui-keywords/webui-take-screenshot">Take Screenshot</a></li><li className="li">[Web UI] <a className="xref" href="/katalon-studio/keywords/keyword-description-in-katalon-studio/visual-based-web-testing-keywords/webui-take-a-screenshot-as-checkpoint">Take Screenshot As Checkpoint</a></li><li className="li">[WebUI] <a className="xref" href="/katalon-studio/keywords/keyword-description-in-katalon-studio/web-ui-keywords/webui-take-element-screenshot">Take Element Screenshot</a></li><li className="li">[Web UI] <a className="xref" href="/katalon-studio/keywords/keyword-description-in-katalon-studio/visual-based-web-testing-keywords/webui-take-element-screenshot-as-checkpoint">Take Element Screenshot As Checkpoint</a></li><li className="li">[WebUI] <a className="xref" href="/katalon-studio/keywords/keyword-description-in-katalon-studio/web-ui-keywords/webui-take-area-screenshot">Take Area Screenshot</a></li><li className="li">[Web UI] <a className="xref" href="/katalon-studio/keywords/keyword-description-in-katalon-studio/visual-based-web-testing-keywords/webui-take-area-screenshot-as-a-checkpoint">Take Area Screenshot As Checkpoint</a></li></ul> </li><li className="li">Support Class File Decompiler for debug. <a className="xref" href="/katalon-studio/maintain-tests/configure-class-file-decompilation-in-katalon-studio">Learn more</a> </li><li className="li">Support setting a new default JRE in test projects. <a className="xref" href="/katalon-studio/get-started/workspace-settings/katalon-studio-preferences/set-a-new-default-jre-for-test-projects-in-katalon-studio#task-4780">Learn more</a> </li><li className="li">[Katalon TestOps Vision] Support <a className="xref j-external-link" href="https://github.com/katalon-studio-samples/web-visual-testing-samples" target="_blank">a sample project for Visual Testing with TestOps Vision</a>.</li></ul> 

### <a id="id_6" class="anchor_top_offset"/>Improvements

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">Upgrade Eclipse IDE from version 4.6 to 4.16.</li><li className="li">Upgrade Groovy compiler from version 2.4.7 to version     2.4.20.</li><li className="li">Notarize Katalon Studio and Katalon Runtime Engine applications     for macOS Catalina. <a className="xref j-external-link" href="https://developer.apple.com/documentation/xcode/notarizing_macos_software_before_distribution" target="_blank">Learn       more</a>   </li><li className="li">Enhance qTest Integration, including:      <ul className="ul"><li className="li">Support uploading screenshots in test results to qTest. <a className="xref" href="/katalon-studio/integrations/test-management/configure-qtest-integration-in-katalon-studio#task-1921">Learn           more</a>       </li><li className="li">[CLI] Submit automation test status with build information to         qTest Manager by <code className="ph codeph">-qTestBuildLabel</code> and         <code className="ph codeph">-qTestBuildURL</code>. <a className="xref" href="/katalon-studio/execute-tests/katalon-runtime-engine/command-line-syntax-in-katalon-runtime-engine#concept-5395">Learn           more</a>       </li><li className="li">Execution Status Mapping. <a className="xref" href="/katalon-studio/integrations/test-management/configure-qtest-integration-in-katalon-studio#task-9375">Learn           more</a>       </li><li className="li">Map a Katalon test case to a qTest test case by database ID. <a className="xref" href="/katalon-studio/integrations/test-management/configure-qtest-integration-in-katalon-studio#task-1893">Learn           more</a>       </li></ul>   </li><li className="li">[Jira Integration] Import JIRA issue summary along with issue     ID to form Test Case Name in Katalon Studio.</li><li className="li">Update <a className="xref j-external-link" href="https://docs.katalon.com/javadoc/index.html" target="_blank">Javadoc       7.9.0</a>.</li><li className="li">Support Chrome 87.</li><li className="li">Support Microsoft Edge (Chromium) 87.</li></ul> 
      

### <a id="id_7" class="anchor_top_offset"/>Deprecated

      
        
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul">   <li className="li">Deprecated Katalon Studio version for Windows 32-bit.</li> </ul> 
      
    
      

### <a id="id_8" class="anchor_top_offset"/>Fixes

      
        
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul">   <li className="li">Bug: [Incorrect Test Results] Katalon returned PASSED when test     scripts contained invalid syntax.</li>   <li className="li">Bug: [Web UI Testing] Instead of logging warning messages and     marking PASSED, <code className="ph codeph">WebUI.verifyElementAttributeValue</code>     marks failed if the element is not present.</li>   <li className="li">Bug: Katalon Studio IDE sometimes failed to save Groovy files'     changes, including keywords, test listeners, step definitions while     renaming test objects.</li>   <li className="li">Bug: Performance issues of Applitools sample project. <a className="xref j-external-link" href="https://github.com/katalon-studio-samples/katalon-studio-applitools-plugin-sample" target="_blank">Learn       more</a>   </li> </ul> 
      
    
    

## <a id="id_9" class="anchor_top_offset"/>Version 7.8.2

    
          

### <a id="id_10" class="anchor_top_offset"/>Improvements

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">[Katalon TestOps (Beta) Integration] Support detecting Assertions in execution log. <a className="xref j-external-link" href="https://forum.katalon.com/t/katalon-studio-7-8-2-make-use-of-assertions-for-better-test-case-quality-and-failure-investigation" target="_blank">Learn more</a> </li><li className="li">[Time Capsule] Allow turning on/turning off Time Capsule in Project Settings (Go to Project &gt; Settings &gt; Execution &gt; WebUI). <a className="xref" href="/katalon-studio/maintain-tests/fix-broken-web-test-objects-with-time-capsule-in-katalon-studio">Learn more</a> </li></ul> 
      

### <a id="id_11" class="anchor_top_offset"/>Fixes

      
        
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul">   <li className="li">Bug: An issue of generating a Time Capsule for an error that     doesn't cause test execution to fail.</li>   <li className="li">Bug: An issue of showing "No application is started yet" when     test execution is already started. Address <a className="xref j-external-link" href="https://github.com/katalon-studio/katalon-studio/issues/409" target="_blank">here</a>   </li>   <li className="li">Bug: Cannot generate execution reports when     <code className="ph codeph">WebUI.comment</code> contains invalid XML characters.</li> </ul> 
      
    
    

## <a id="id_12" class="anchor_top_offset"/>Version 7.8.0 - 7.8.1

    
              

### <a id="id_13" class="anchor_top_offset"/>New features

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">Support Time Capsule for optimizing fixing broken Web Test Objects. <a className="xref" href="/katalon-studio/maintain-tests/fix-broken-web-test-objects-with-time-capsule-in-katalon-studio">Learn more</a>. </li><li className="li">[Katalon Studio Enterprise] Support browser-based video recording. <a className="xref" href="/katalon-studio/test-reports/generate-test-reports/generate-browser-based-videos-in-katalon-studio-reports">Learn more</a>. </li><li className="li">[Windows Testing] Support coordinates-based recording with Click Element Offset and Right-click Element Offset keywords on both <a className="xref" href="/katalon-studio/record-and-spy/windows-record-and-spy-utilities/windows-record-tutorials-in-katalon-studio">Windows Recorder</a> and <a className="xref" href="/katalon-studio/record-and-spy/windows-record-and-spy-utilities/native-windows-recorder-in-katalon-studio">Native Windows Recorder</a>.</li><li className="li">Provide Checksum for each Katalon Studio package named <code className="ph codeph">all-packages.sha256</code> and Open source libraries' license scanning report in HTML named <code className="ph codeph">KatalonStudio-openSourceReport.html</code> (Go to <a className="xref j-external-link" href="https://github.com/katalon-studio/katalon-studio/releases" target="_blank">our GitHub Repository</a>, download those files in each build's Assets).</li><li className="li">[Katalon Studio Enterprise] Allow replacing a built-in library with an external one for flexible libraries usage in a test project. <a className="xref" href="/katalon-studio/manage-projects/project-settings/library-management-in-katalon-studio#task-4328">Learn more</a>. </li><li className="li">[Web Service Testing] Import SOAP requests from SoapUI and WSDLs having no service endpoints. <a className="xref" href="/katalon-studio/test-objects/api-test-objects/import-web-service-objects/import-web-service-requests-from-soapui-to-katalon-studio">Learn more</a>.</li><li className="li">[Katalon TestOps (Beta) Integration] Export BDD reports generated in Katalon Studio to display in TestOps. <a className="xref" href="/katalon-platform/analyze/reports/view-test-reports/view-bdd-test-results-in-testops">Learn more.</a></li><li className="li">[Katalon TestOps (Beta) Integration] Support generating commands for TestOps CI in Katalon Studio's Command Builder.</li><li className="li">[Katalon TestOps (Beta) Integration] Allow overriding TestOps Project ID via command line.</li><li className="li">[Katalon TestOps (Beta) Integration] View Releases in Katalon Studio's Test Explorer.</li><li className="li">Provide in-app tutorials for new Katalon users to start testing Web UI, Mobile, Web Service and Windows applications (Go to Help &gt; Tutorials &gt; Select Web UI/Mobile/Web Service/Windows).</li><li className="li">You can create a new project with Desktop type.</li><li className="li">[Katalon Studio Enterprise] Configure idle timeout for license usage management. <a className="xref" href="/katalon-platform/administer/administration-tasks/manage-licenses/manage-katalon-licenses">Learn more.</a></li></ul> 
      

### <a id="id_14" class="anchor_top_offset"/>Improvements

      
        
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul">   <li className="li">Support Microsoft Edge (Chromium) 86</li>   <li className="li">Support Chrome 86</li>   <li className="li">[qTest Integration]: Generate qTest - Katalon Studio parity     report in HTML, sync up qTest test case version and test steps's     content, and send Skipped test results to qTest. Learn     more</li>   <li className="li">[Kobiton Integration] Support SSO for authentication and     corresponding command options. <a className="xref" href="/katalon-studio/execute-tests/katalon-runtime-engine/command-line-syntax-in-katalon-runtime-engine#concept-5395">Learn       more</a>   </li>   <li className="li">[Jira Cloud Integration]: Support importing BDD Feature Files.     <a className="xref" href="/katalon-studio/integrations/test-management/configure-jira-integration-in-katalon-studio">Learn       more</a>   </li>   <li className="li">[BDD Testing Framework] Allow setting default package for step     defenitions. <a className="xref" href="/katalon-studio/bdd-testing/work-with-bdd-feature-files-in-katalon-studio#id_5">Learn       more</a>.</li>   <li className="li">[Mobile Testing] Support "Attributes" Selector Strategy and add     "Verify and Highlight" feature to Mobile Spy/Recorder.</li>   <li className="li">[Katalon TestOps (Beta) Integration]: Support automatically     retrying uploading Test Projects and Test Reports from Katalon     Studio to Katalon TestOps upon failure.</li>   <li className="li">Replace Katalon Help with Start Page for a new fresh look and     more customized information for each user.</li>   <li className="li">Reduce the size of Katalon Docker Image.</li>   <li className="li">Discontinued new purchase of Katalon Runtime Engine DevOps     license. Read more about <a className="xref" href="/katalon-studio/katalon-studio-enterprise-and-katalon-runtime-engine-license/katalon-runtime-engine-devops-sunsetting">Katalon       Runtime Engine DevOps Sunsetting</a>.</li>   <li className="li">Display SKIP test status in execution reports.</li> </ul> 
      
    
      

### <a id="id_15" class="anchor_top_offset"/>Fixes

      
        
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul">   <li className="li">Bug: An issue of not installing Smart Wait extension     automatically on Chrome when running tests.</li>   <li className="li">Bug: Failed to display items in table and tree views on macOS     Big Sur.</li>   <li className="li">Bug: [Katalon Studio Enterprise - Export Test Artifacts] Cannot     export test cases.</li>   <li className="li">Bug: [Katalon Studio Enterprise] Cannot import API from OpenAPI     Specification 3.0.</li>   <li className="li">Bug: [Katalon Runtime Engine] Cannot execute Dynamic Test     Suites.</li>   <li className="li">Bug: An issue of Katalon Runtime Engine activation failure on     Katalon Docker Image.</li>   <li className="li">Bug: GUI issues on Windows machines when scaling to more than     100% size of text.</li>   <li className="li">Bug: [Test Object's Editor] Cannot display all object     properties in a window screen.</li>   <li className="li">Bug: API Requests with fileupload body uses a file path instead     of a file name.</li>   <li className="li">Bug: [Katalon TestOps (Beta) Integration]: Cannot display more     than 20 projects fetched from Katalon TestOps (Beta).</li> </ul> 
      
    
    

## <a id="id_16" class="anchor_top_offset"/>Version 7.7.0 - 7.7.1 - 7.7.2

    
              

### <a id="id_17" class="anchor_top_offset"/>New features

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">[Katalon Record Utility] Support adding verification test steps     during recording with Chrome, Edge (Chromium-based), and Firefox.     <a className="xref" href="/katalon-studio/record-and-spy/webui-record-and-spy-utilities/record-web-utility-in-katalon-studio#id_3">Learn       more</a>.</li><li className="li">[Katalon Studio Enterprise - Web Service Testing] Import     RESTful API with OpenAPI Specification 3.0.    </li><li className="li">[Web Service Testing] Import RESTful requests from WADLs. <a className="xref" href="/katalon-studio/test-objects/api-test-objects/import-web-service-objects/import-restful-requests-from-wadls-to-katalon-studio">Learn       more</a>   </li><li className="li">[Windows Testing] Support passing Capabilities including     <code className="ph codeph">appArguments</code> and <code className="ph codeph">appWorkingDir</code> for Native     Windows Recorder. <a className="xref" href="/katalon-studio/manage-projects/project-settings/desired-capabilities/introduction-to-desired-capabilities-in-katalon-studio">Learn       more</a>   </li><li className="li">Support using Global Variables in Email Settings.    </li><li className="li">[Katalon Runtime Engine] Allow selecting an Organization for     license validation when activating Katalon Runtime Engine. <a className="xref" href="#">Learn       more</a>   </li><li className="li">[Katalon TestOps (Beta) Integration] Support integration with     Katalon TestOps Vision for visual testing. <a className="xref j-external-link" href="https://forum.katalon.com/t/visual-testing-image-comparison-with-katalon-studio-7-8-0-and-katalon-testops/45557" target="_blank">Learn       more</a>   </li></ul> 
      

### <a id="id_18" class="anchor_top_offset"/>Improvements

      
        
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul">   <li className="li">Support Microsoft Edge (Chromium) 85</li>   <li className="li">Support Chrome 85</li>   <li className="li">Install the Basic Reports plugin automatically for all     users</li>   <li className="li">Publish <a className="xref j-external-link" href="https://docs.katalon.com/javadoc/index.html" target="_blank">API docs version       7.7</a>   </li> </ul> 
      
    
      

### <a id="id_19" class="anchor_top_offset"/>Fixes

      
        
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul">   <li className="li">Bug: [Katalon Runtime Engine] An issue of generating reports     after execution</li>   <li className="li">Bug: [Katalon Runtime Engine] An exception thrown when updating     WebDriver automatically in Command Line. Address <a className="xref j-external-link" href="https://forum.katalon.com/t/test-collection-are-not-running-from-azure-getting-classnotfoundexception-com-kms-katalon-core-logging-logback-systemoutfilter-cannot-be-found-by-ch-qos-logback-classic-1-2-3-and-lots-of-unable-to-resolve-class-errors/47743" target="_blank">here</a>   </li>   <li className="li">Bug: [Katalon Record Utility] Unable to locate Objects during     execution if the objects are captured with such options as     <strong className="ph b">Merge objects</strong>, <strong className="ph b">Duplicate objects</strong>,     or <strong className="ph b">Replace existing objects</strong>   </li>   <li className="li">Bug: [TestNG] Return incorrect test results when using the     <code className="ph codeph">runTestNGTestClasses</code> keyword</li> </ul> 
      
    
    

## <a id="id_20" class="anchor_top_offset"/>Version 7.6.6

    
          
      

### <a id="id_21" class="anchor_top_offset"/>Improvements

      
        
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul">   <li className="li">[qTest Integration] Upload test results of the integrated Test     Suites in Test Suite Collection to qTest</li>   <li className="li">[Katalon TestOps (Beta) Integration] Display TestOps Plans in     Tests Explorer. <a className="xref" href="/katalon-platform/execute/test-execution-with-testops/schedule-test-runs-in-testops">Learn       more</a>   </li>   <li className="li">[Katalon Studio Enterprise] Enhance Self-healing Insights. <a className="xref" href="/katalon-studio/maintain-tests/self-healing-tests-in-katalon-studio#id_8">Learn       more</a>   </li>   <li className="li">[Katalon Studio Enterprise] Enhance UX of adding test cases to     test suites</li>   <li className="li">Support <a className="xref" href="/katalon-platform/troubleshooting/troubleshooting-common-administrative-issues/account-activation-problems">troubleshooting       activation problems</a>   </li> </ul> 
      
    
      

### <a id="id_22" class="anchor_top_offset"/>Fixes

      
        
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul">   <li className="li">Bug: An issue related to Test Objects' names in Katalon Record     Utility</li>   <li className="li">Bug: [Command Builder] An issue of setting the waiting time to     update execution status of the Test Suite</li>   <li className="li">Bug: [Windows Testing] Test execution failure caused by the     default timeout of <code className="ph codeph">switchToWindowTitle</code>   </li>   <li className="li">Bug: [Web Service Testing] An issue of saving test request's     body</li> </ul> 
      
    
    

## <a id="id_23" class="anchor_top_offset"/>Version 7.6.5

    
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">You can download Katalon Studio version 7.6.5 <a className="xref j-external-link" href="https://github.com/katalon-studio/katalon-studio/releases/tag/v7.6.5" target="_blank">here</a>.</p> 
    
          
      

### <a id="id_24" class="anchor_top_offset"/>Improvements

      
        
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul">   <li className="li">[qTest Integration] Include qTest Test Case ID in the name of     Katalon Test Cases downloaded from qTest</li> </ul> 
      
    
      

### <a id="id_25" class="anchor_top_offset"/>Fixes

      
        
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul">   <li className="li">Bug: [Web Recorder] Unable to use <strong className="ph b">Run from       here</strong> when recording web with Internet Explorer WebDriver     v3.6.0.0</li>   <li className="li">Bug: [Web Recorder] Unable to capture navigate actions when     recording with Internet Explorer WebDriver</li>   <li className="li">Bug: [Mobile Recorder] Unable to perform any actions on an     Android Tab element</li>   <li className="li">Bug: [Mobile Recorder] Unable to detect elements when     spying/recording an iOS app</li>   <li className="li">Bug: [qTest Integration] Unable to send test reports to qTest     automatically</li>   <li className="li">Bug: [Jira Integration - Katalon BDD] An issue of importing     incorrect content of Feature files from Jira</li>   <li className="li">Bug: [TestRail Integration] TestRail plugin does not support     Manual Proxy Configuration</li>   <li className="li">Bug: [Kobiton Integration] Unable to apply System Proxy     configuration when retrieving Kobiton devices and applications</li>   <li className="li">Bug: [Katalon TestOps (Beta) Integration] Unable to upload test     results to Katalon TestOps (Beta)</li>   <li className="li">Bug: [Report Email] Unable to receive any emails or receive     unexpected test suite report emails</li>   <li className="li">Bug: [Test Listeners] Text field is not visible when renaming a     test listener</li>   <li className="li">Bug: [Katalon Runtime Engine] Unexpected stack trace is     displayed at the end of execution</li> </ul> 
      
    
    

## <a id="id_26" class="anchor_top_offset"/>Version 7.6.2

    
          
      

### <a id="id_27" class="anchor_top_offset"/>New Features

      
        
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul">   <li className="li">Katalon TestOps (Beta) Integration: Support associating a test     execution in Katalon Studio with Release on Katalon TestOps (Beta)     via command-line parameter. <a className="xref" href="/katalon-platform/plan/link-test-execution-with-a-testops-release-using-command-builder">Learn       more</a>   </li>   <li className="li">Katalon TestOps (Beta) Integration: Display the Executions     table in Tests Explorer. <a className="xref" href="/katalon-studio/get-started/workspace-settings/integrate-katalon-platform-with-katalon-studio">Learn       more</a>   </li> </ul> 
      
    
      

### <a id="id_28" class="anchor_top_offset"/>Fixes

      
        
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul">   <li className="li">Bug: [Self-healing mechanism] Null Pointer Exception thrown     when XPath/CSS locator is empty</li> </ul> 
      
    
    

## <a id="id_29" class="anchor_top_offset"/>Version 7.6.0 - 7.6.1

    
              

### <a id="id_30" class="anchor_top_offset"/>New features

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">[Katalon Studio Enterprise] Support Self-Healing Web tests. <a className="xref" href="/katalon-studio/maintain-tests/self-healing-tests-in-katalon-studio">Learn more</a>. </li><li className="li">[Katalon Studio Enterprise] Support setting timeout and maximum response size for API requests. <a className="xref" href="/katalon-studio/manage-projects/project-settings/execution-settings-in-katalon-studio#concept-7417">Learn more</a>. </li><li className="li">[Katalon Studio Enterprise] Support retrying failed test executions immediately in Test Suite's execution. <a className="xref" href="/katalon-studio/execute-tests/execute-dynamic-test-suites-in-katalon-studio#id_2">Learn more</a>. </li><li className="li">[Mobile Testing] Fully support Selector Strategies. <a className="xref" href="/katalon-studio/test-objects/mobile-test-objects/locator-strategies-for-mobile-objects">Learn more</a>. </li><li className="li">[Mobile Testing] Support App Center Test integration. <a className="xref" href="/katalon-platform/integrations/cloud-device-integrations/app-center-integration">Learn more</a>. </li><li className="li">[API Testing] Support importing RESTful requests from SoapUI to Katalon Studio. <a className="xref" href="/katalon-studio/test-objects/api-test-objects/import-web-service-objects/import-web-service-requests-from-soapui-to-katalon-studio">Learn more</a>. </li><li className="li">[Desktop Testing] Support new Windows keywords, including <a className="xref" href="/katalon-studio/keywords/keyword-description-in-katalon-studio/windows-keywords/windows-set-encrypted-text">setEncryptedText</a>, <a className="xref" href="/katalon-studio/keywords/keyword-description-in-katalon-studio/windows-keywords/windows-get-attribute">getAttribute</a>, <a className="xref" href="/katalon-studio/keywords/keyword-description-in-katalon-studio/windows-keywords/windows-verify-element-attribute-value">verifyElementAttributeValue</a>, <a className="xref" href="/katalon-studio/keywords/keyword-description-in-katalon-studio/windows-keywords/windows-wait-for-element-attribute-value">waitForElementAttributeValue</a>, <a className="xref" href="/katalon-studio/keywords/keyword-description-in-katalon-studio/windows-keywords/windows-verify-element-present">verifyElementPresent</a>, <a className="xref" href="/katalon-studio/keywords/keyword-description-in-katalon-studio/windows-keywords/windows-verify-element-not-present">verifyElementNotPresent</a>, <a className="xref" href="/katalon-studio/keywords/keyword-description-in-katalon-studio/windows-keywords/windows-verify-element-not-present">waitForElementPresent</a>, and <a className="xref" href="/katalon-studio/keywords/keyword-description-in-katalon-studio/windows-keywords/windows-verify-element-not-present">waitForElementNotPresent</a>. </li><li className="li">Allow overriding <code className="ph codeph">Browser Type</code> and <code className="ph codeph">Execution       Profile</code> of all Test Suites in a Test Suite Collection via command line. <a className="xref" href="/katalon-studio/execute-tests/katalon-runtime-engine/get-started-with-katalon-runtime-engine#id_10">Learn more</a>. </li><li className="li">Support Content Assist function for Custom Keywords in test cases (same as built-in keywords).</li></ul> 
      

### <a id="id_31" class="anchor_top_offset"/>Improvements

      
        
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul">   <li className="li">[Katalon Studio Enteprise] Applitools Integration becomes a     built-in feature with its libraries updated to the latest     versions</li>   <li className="li">Support updating Microsoft Edge (Chromium) driver in Katalon     Studio Tools</li>   <li className="li">Set Chrome as the default browser</li> </ul> 
      
    
      

### <a id="id_32" class="anchor_top_offset"/>Fix

      
        
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul">   <li className="li">Bug: Log Viewer displays incorrect test results if a test case     has Call Test Case steps</li>   <li className="li">Bug: [Desktop Testing] <code className="ph codeph">setText()</code> keyword does not     clear the current text before setting the given text</li>   <li className="li">Bug: [qTest Integration] Unable to upload reports to qTest in     qTest v10.1.0.0 or later</li> </ul> 
      
    
    

## <a id="id_33" class="anchor_top_offset"/>Version 7.5.10

    
              
      

### <a id="id_34" class="anchor_top_offset"/>New feature

      
        
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul">   <li className="li">Support importing test scripts of Selenium IDE version 3.x. <a className="xref" href="/katalon-studio/get-started/migrate-from-other-tools/import-selenium-ide-version-3-projects-to-katalon-studio">Learn       more</a>   </li> </ul> 
      
    
      

### <a id="id_35" class="anchor_top_offset"/>Improvement

      
        
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul">   <li className="li">[WebUI Testing] Support Recorder and Spy with Microsoft Edge     (Chromium)</li> </ul> 
      
    
      

### <a id="id_36" class="anchor_top_offset"/>Fix

      
        
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul">   <li className="li">Bug: [Mobile] An issue of missing mobile devices when using     Custom Capabilities. Address <a className="xref j-external-link" href="https://github.com/katalon-studio/katalon-studio/issues/275" target="_blank">#275</a>   </li> </ul> 
      
    
    

## <a id="id_37" class="anchor_top_offset"/>Version 7.5.5

    
              
      

### <a id="id_38" class="anchor_top_offset"/>New features

      
        
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul">   <li className="li">[Katalon Studio Enterprise] Support "Debug from here". <a className="xref" href="/katalon-studio/debug-a-test-case/debug-a-test-case-in-katalon-studio#id_9">Learn       more</a>   </li>   <li className="li">[Web Service Testing] Support parameterizing a SOAP request's     service endpoint. <a className="xref" href="/katalon-studio/test-objects/api-test-objects/rest-request/parameterize-a-web-service-object#id_4">Learn       more</a>   </li>   <li className="li">[Web Service Testing] Support defining body content of RESTful     API requests with methods other than POST/PUT/PATCH/DELETE</li> </ul> 
      
    

### <a id="id_39" class="anchor_top_offset"/>Improvements

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">[Custom Keywords] Organize Custom Keywords in an alphabetical order in Keyword Browser and support categorizing them with <code className="ph codeph">keywordObject</code>. <a className="xref" href="/katalon-studio/keywords/custom-keywords/introduction-to-custom-keywords-in-katalon-studio#task-5120">Learn more</a>. </li><li className="li">Improve Katalon Studio's performance of checking/unchecking test folders containing more than 50 Test Cases</li><li className="li">Log Viewer has a new design: Root cause shown on the top of the stack trace and Test Object ID added to Selenium’s common exceptions for better debugging.</li><li className="li">[Desktop Testing] Increase the default timeout and allow changing this default value when using <code className="ph codeph">switchToWindowTitle</code> during recording and executing tests. Learn more. </li></ul> 
      

### <a id="id_40" class="anchor_top_offset"/>Fixes

      
        
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul">   <li className="li">Bug: [Mobile] NullPointerException exception thrown by the     <code className="ph codeph">startExistingApplication</code> keyword when running on a     Sauce Labs device</li>   <li className="li">Bug: [Mobile] Unable to capture objects using Spy Mobile</li> </ul> 
      
    
    

## <a id="id_41" class="anchor_top_offset"/>Version 7.5.0 - 7.5.2

    
              

### <a id="id_42" class="anchor_top_offset"/>New features

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">[Katalon Studio Enterprise] Implement Native Windows Recorder     (for Windows only). <a className="xref" href="/katalon-studio/record-and-spy/windows-record-and-spy-utilities/native-windows-recorder-in-katalon-studio">Learn       more</a>   </li><li className="li">[Katalon Studio Enterprise] Send Test Suite Collection's report     emails. <a className="xref" href="/katalon-studio/test-reports/share-test-reports-via-email-in-katalon-studio">Learn       more</a>   </li><li className="li">[Katalon Studio Enterprise] Support retrying Failed test data     only in Test Suite's execution. <a className="xref" href="/katalon-studio/execute-tests/execute-dynamic-test-suites-in-katalon-studio#id_2">Learn       more</a>   </li><li className="li">[Web Testing] Support a new WebUI keyword to upload files by     drag-and-drop. <a className="xref" href="/katalon-studio/keywords/keyword-description-in-katalon-studio/web-ui-keywords/webui-upload-file-by-drag-and-drop">Learn       more</a>   </li><li className="li">Allow setting a default execution profile at project level. <a className="xref" href="/katalon-studio/data-driven-testing/global-variables-and-execution-profile#id_4">Learn       more</a>   </li></ul> 

### <a id="id_43" class="anchor_top_offset"/>Improvements

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">Support Microsoft Edge (Chromium) 83</li><li className="li">Support Chrome 83</li><li className="li">[Katalon Runtime Engine] Improve execution log in CLI mode by printing out applied proxy configurations</li><li className="li">Improve Proxy Settings with two separate types, including <strong className="ph b">Authentication</strong> and <strong className="ph b">System</strong> proxies. <a className="xref" href="/katalon-studio/get-started/workspace-settings/katalon-studio-preferences/preferences-in-katalon-studio">Learn more</a> </li><li className="li">[Web Service] Enhance WSDL importing feature. <a className="xref" href="/katalon-studio/test-objects/api-test-objects/import-web-service-objects/import-soap-requests-from-wsdls-to-katalon-studio">Learn more</a>.</li><li className="li">[Web Service] Support defining a content type for form-data HTTP Body of RESTful requests.<a className="xref" href="#">Learn more</a> </li><li className="li">Downgrade the MySQL Connector/J, the official JDBC driver for MySQL, from 8.0.17 to 8.0.15</li><li className="li">Upgrade the Microsoft JDBC Driver 6.2 for SQL Server</li><li className="li">Enhance GUI of the following components: Image-based Testing in Tests Explorer, Katalon TestOps (Beta) Integration dialog, Activation dialog, and CAPTCHA error in the Activation dialog</li></ul> 
      

### <a id="id_44" class="anchor_top_offset"/>Fixes

      
        
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul">   <li className="li">Bug: An issue of OAUth1.0 Authorization</li>   <li className="li">Bug: [Mobile Testing] Unable to scroll down to see all test     object attributes</li>   <li className="li">Bug: [Tests Explorer] Unable to open a feature file if it is     not under the <strong className="ph b">Include</strong> folder. Address <a className="xref j-external-link" href="https://github.com/katalon-studio/katalon-studio/issues/293" target="_blank">#293</a>   </li>   <li className="li">Bug: Window Objects' references in Test Case not being updated     automatically when Windows Objects are renamed. Address <a className="xref j-external-link" href="https://github.com/katalon-studio/katalon-studio/issues/289" target="_blank">#289</a>   </li>   <li className="li">Bug: Exposing proxy password</li> </ul> 
      
    
    

## <a id="id_45" class="anchor_top_offset"/>Version 7.4.0

    
      
      

### <a id="id_46" class="anchor_top_offset"/>New features

      
        
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul">   <li className="li">Support migrating Selenium/TestNG/JUnit test scripts to Katalon     Studio. <a className="xref" href="/katalon-studio/get-started/migrate-from-other-tools/seleniumtestngjunit-migration-to-katalon-studio">Learn       more</a>   </li>   <li className="li">Publish <a className="xref j-external-link" href="https://store.katalon.com/product/180/TestNG-JUnit-Keywords" target="_blank">TestNG/JUnit       Keywords</a> plugin</li>   <li className="li">Support Chrome 81</li> </ul> 
      
    
    

## <a id="id_47" class="anchor_top_offset"/>Version 7.3.2 - 7.3.3

    
      
      

### <a id="id_48" class="anchor_top_offset"/>Fix

      
        
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul">   <li className="li">Bug: Unable to activate Katalon Runtime Engine on Oracle Linux     Server 7.6</li> </ul> 
      
    
    

## <a id="id_49" class="anchor_top_offset"/>Version 7.3.1

    
          
      

### <a id="id_50" class="anchor_top_offset"/>Improvement

      
        
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul">   <li className="li">[Katalon Runtime Engine] Improve execution log in CLI mode</li> </ul> 
      
    
      

### <a id="id_51" class="anchor_top_offset"/>Fixes

      
        
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul">   <li className="li">Bug: Unable to activate Katalon Studio</li>   <li className="li">Bug: Unable to open a containing folder of a package in Tests     Explorer</li>   <li className="li">Bug: [Web Service] An issue of saving HTTP Body content created     with <code className="ph codeph">x-www-form-urlencoded</code> or <code className="ph codeph">form-data</code>     option</li>   <li className="li">Bug: [Web Service] An issue of handling API response in XML     format</li>   <li className="li">Bug: [Web Service] Unable to send a SOAP request behind     proxy</li>   <li className="li">Bug: [DDT] An issue of Database Connection settings being saved     across projects</li> </ul> 
      
    
    

## <a id="id_52" class="anchor_top_offset"/>Version 7.3.0

    
              
      

### <a id="id_53" class="anchor_top_offset"/>New Features

      
        
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul">   <li className="li">Support Microsoft Edge (Chromium) on both Windows and     macOS</li>   <li className="li">[Windows] Support parameterizing Windows test objects. <a className="xref" href="/katalon-studio/test-objects/windows-test-objects/windows-test-objects-in-katalon-studio#id_6">Learn       more</a>   </li>   <li className="li">Add a Notification icon</li> </ul> 
      
    
      

### <a id="id_54" class="anchor_top_offset"/>Improvements

      
        
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul">   <li className="li">Support configuring <code className="ph codeph">Delay Between Actions</code> in     milliseconds in Execution settings</li>   <li className="li">Enhance UI</li>   <li className="li">Include the <code className="ph codeph">TestObject</code> class in <a className="xref j-external-link" href="https://docs.katalon.com/javadoc/index.html" target="_blank">Katalon API       Documents</a>   </li> </ul> 
      
    
      

### <a id="id_55" class="anchor_top_offset"/>Fixes

      
        
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul">   <li className="li">Bug: [Runtime Engine] An issue of counting the number of     execution processes</li>   <li className="li">Bug: [Windows] An issue of debugging Windows test scripts</li>   <li className="li">Bug: [Kobiton Integration] An issue of not displaying error     message for invalid account</li>   <li className="li">Bug: [BDD] <code className="ph codeph">runFeatureFolder</code> throws exception when     tests fail</li>   <li className="li">Bug: An issue of configuring the port of Mail Server in Email     settings</li>   <li className="li">Bug: [API] Unable to send a request in macOS or Linux if its     HTTP body uses <code className="ph codeph">form-data</code> or <code className="ph codeph">file</code> with     relative path on Windows machine</li> </ul> 
      
    
    

## <a id="id_56" class="anchor_top_offset"/>Version 7.2.7

    
      
      

### <a id="id_57" class="anchor_top_offset"/>Fixes

      
        
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul">   <li className="li">Bug: [BDD] <code className="ph codeph">java.lang.NoClassDefFoundError</code> thrown     when running a feature file</li>   <li className="li">Bug: An issue of Smart Wait preventing request state in     XMLHttpRequest from being read</li> </ul> 
      
    
    

## <a id="id_58" class="anchor_top_offset"/>Version 7.2.6

    
          
      

### <a id="id_59" class="anchor_top_offset"/>Fixes

      
        
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul">   <li className="li">Bug: Fail to activate Katalon Studio Enterprise with Katalon     accounts registered with unconventional domains such as     <code className="ph codeph">.technology</code>.</li>   <li className="li">Bug: [Desktop Apps Testing] An issue of losing Windows test     objects when users drag and drop their folders.</li>   <li className="li">Bug: [Desktop Apps Testing] An issue with automatically     updating Windows test objects' references in Test Scripts after a     drag and drop.</li>   <li className="li">Bug: [Desktop Apps Testing] Cannot identify Windows test     objects by relative path.</li>   <li className="li">Bug: [Desktop Apps Testing] Cannot create a new item with a     right-click on a Windows object.</li>   <li className="li">Bug: [Desktop Apps Testing] Cannot edit a Windows object's     property.</li>   <li className="li">Bug: [Mobile Testing] A performance issue of the     <code className="ph codeph">setSliderValue</code> keyword when testing with a Sauce Labs     device.</li>   <li className="li">Bug: [Mobile Testing] Fail to recognize iPad device and create     a new remote session with iPad simulator.</li> </ul> 
      
    
      

### <a id="id_60" class="anchor_top_offset"/>Discontinued Support

      
        
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul">   <li className="li">Business Support Service</li> </ul> 
      
    
    

## <a id="id_61" class="anchor_top_offset"/>Version 7.2.5

    
              
      

### <a id="id_62" class="anchor_top_offset"/>New Features

      
        
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul">   <li className="li">[Web Service] Support configuring Content Type in HTTP Header     separately from HTTP Body. <a className="xref" href="/katalon-studio/test-objects/api-test-objects/rest-request/restful-request">Learn       more</a>.</li> </ul> 
      
    
      

### <a id="id_63" class="anchor_top_offset"/>Improvements

      
        
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul">   <li className="li">[Kobiton Integration] Allow customizing Kobiton Server URL in     Katalon Studio Preferences.</li>   <li className="li">Enhance Smart Wait's performance during test executions.</li> </ul> 
      
    
      

### <a id="id_64" class="anchor_top_offset"/>Fixes

      
        
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul">   <li className="li">Bug: An issue related to a failure of Swagger's importing     multiple requests without operation ID.</li>   <li className="li">Bug: An issue where Click step passes but no actual action is     performed.</li> </ul> 
      
    
    

## <a id="id_65" class="anchor_top_offset"/>Version 7.2.4

    
      
      

### <a id="id_66" class="anchor_top_offset"/>New Features

      
        
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul">   <li className="li">Support editing JVM parameters in Execution Settings. <a className="xref" href="/katalon-studio/manage-projects/project-settings/execution-settings-in-katalon-studio">Learn       more</a>.</li> </ul> 
      
    
    

## <a id="id_67" class="anchor_top_offset"/>Version 7.2.3

    
      
      

### <a id="id_68" class="anchor_top_offset"/>Fixes

      
        
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul">   <li className="li">Bug: Cannot send SOAP Request due to failure in parsing WSDL     definition</li> </ul> 
      
    
    

## <a id="id_69" class="anchor_top_offset"/>Version 7.2.2

    
      
      

### <a id="id_70" class="anchor_top_offset"/>New Features

      
        
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul">   <li className="li">[Web Testing] Support image-based object recognition. <a className="xref" href="#">Learn       more</a>   </li> </ul> 
      
    
    

## <a id="id_71" class="anchor_top_offset"/>Version 7.2.0 - 7.2.1

    
              
      

### <a id="id_72" class="anchor_top_offset"/>New Features

      
        
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul">   <li className="li">New Windows keywords:      <ul className="ul">       <li className="li">         <a className="xref j-external-link" href="https://docs.katalon.com/katalon-studio/docs/windows-kw-get-element-position.html" target="_blank">           <code className="ph codeph">getElementPosition</code>         </a>       </li>       <li className="li">         <a className="xref j-external-link" href="https://docs.katalon.com/katalon-studio/docs/windows-kw-get-element-rect.html" target="_blank">           <code className="ph codeph">getElementRect</code>         </a>       </li>       <li className="li">         <a className="xref j-external-link" href="https://docs.katalon.com/katalon-studio/docs/windows-kw-start-app-title.html" target="_blank">           <code className="ph codeph">startApplicationWithTitle</code>         </a>       </li>       <li className="li">         <a className="xref j-external-link" href="https://docs.katalon.com/katalon-studio/docs/windows-kw-switch-window.html" target="_blank">           <code className="ph codeph">switchToWindow</code>         </a>       </li>       <li className="li">         <a className="xref j-external-link" href="https://docs.katalon.com/katalon-studio/docs/windows-kw-switch-window-title.html" target="_blank">           <code className="ph codeph">switchToWindowTitle</code>         </a>       </li>     </ul>   </li>   <li className="li">New Mobile keywords:      <ul className="ul">       <li className="li">         <a className="xref j-external-link" href="https://docs.katalon.com/katalon-studio/docs/mobile-execute-command.html" target="_blank">           <code className="ph codeph">executeMobileCommand</code>         </a>       </li>       <li className="li">         <a className="xref j-external-link" href="https://docs.katalon.com/katalon-studio/docs/mobile-double-tap.html" target="_blank">           <code className="ph codeph">doubleTap</code>         </a>       </li>       <li className="li">         <a className="xref j-external-link" href="https://docs.katalon.com/katalon-studio/docs/mobile-long-press.html" target="_blank">           <code className="ph codeph">longPress</code>         </a>       </li>       <li className="li">         <a className="xref j-external-link" href="https://docs.katalon.com/katalon-studio/docs/mobile-set-encrypted-text.html" target="_blank">           <code className="ph codeph">setEncryptedText</code>         </a>       </li>     </ul>   </li>   <li className="li">Support adding <a className="xref" href="/katalon-studio/get-started/workspace-settings/katalon-studio-preferences/configure-proxy-preferences-in-katalon-studio">Proxy       Exceptions</a> in Proxy Preferences and     <code className="ph codeph">-proxy.excludes</code> option in console mode.</li>   <li className="li">[Mobile Recorder] Implement the following actions: Get Text,     Swipe, and Scroll To Text.</li> </ul> 
      
    
      

### <a id="id_73" class="anchor_top_offset"/>Changes and Improvements

      
        
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul">   <li className="li">Support ChromeDriver version 79.</li>   <li className="li">Add <strong className="ph b">Profiles</strong> to Test Suite Collection     Report.</li>   <li className="li">[Mobile- iOS] Support <strong className="ph b">Install Dependencies</strong> and     <strong className="ph b">Install WebDriverAgent</strong> tools on the main menu.     Please be noted that you have to install <a className="xref j-external-link" href="https://brew.sh/" target="_blank">homebrew</a> manually.</li>   <li className="li">[Command Syntax] Support both <code className="ph codeph">-serverUrl</code> and     <code className="ph codeph">-serverURL</code> arguments.</li>   <li className="li">Make the <code className="ph codeph">DriverFactory.changeWebDriver()</code> method a     public method.</li>   <li className="li">Support <strong className="ph b">Open containing folder</strong> for Folders in     Tests Explorer.</li> </ul> 
      
    
      

### <a id="id_74" class="anchor_top_offset"/>Fixes

      
        
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul">   <li className="li">Bug: [Windows] An issue related to creating a project.</li>   <li className="li">Bug: An issue related to saving Web Service Message.</li>   <li className="li">Bug: Empty result tab after a Test Suite execution.</li>   <li className="li">Bug: Test Script lost parens in method call after editing some     steps.</li>   <li className="li">Bug: [KRE] an issue related to the <code className="ph codeph">retry</code>     option.</li>   <li className="li">Bug: [Web] Cannot set a timeout in <strong className="ph b">Wait for       options</strong>.</li>   <li className="li">Bug: [Web Service Request] an issue related to saving HTTP     Header.</li> </ul> 
      
    
    

## <a id="id_75" class="anchor_top_offset"/>Version 7.1.0-7.1.1

    
              
      

### <a id="id_76" class="anchor_top_offset"/>New Features

      
        
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul">   <li className="li">[Katalon TestOps (Beta)] Support Billing Manager role for being     in charge of subscription. <a className="xref" href="/katalon-platform/administer/administration-tasks/manage-users/manage-users">Learn       more</a>.</li>   <li className="li">Support naming test artifacts, including Test Case, Test     Object, Test Data File, Test Suite, Test Suite Collection, and     Checkpoint with UTF-8 characters.</li>   <li className="li">Automatically update keywords' references in other custom     keyword classes when renaming or drag-and-dropping a custom     keyword.</li> </ul> 
      
    
      

### <a id="id_77" class="anchor_top_offset"/>Changes and Improvements

      
        
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul">   <li className="li">[Web Service] Support all file types of the form-data option in     HTTP Body when creating a POST request.</li>   <li className="li">[Web Service] Support API responses in other languages.</li>   <li className="li">Auto-healing Smart Xpath becomes a built-in feature of Katalon     Studio Enterprise. For standard Katalon Studio users who have     already subscribed to this plugin, please contact Katalon team via     business@katalon.com.</li>   <li className="li">Display a progress dialog when adding a bulk number of Test     Cases to a Test Suite.</li>   <li className="li">Handle SVG elements and add a context menu during Spying to     capture objects.</li>   <li className="li">[KRE] Improve running multiple projects with multiple sessions     concurrently.</li>   <li className="li">Support turning off Smart Wait with both global and local     settings. <a className="xref" href="/katalon-studio/record-and-spy/webui-record-and-spy-utilities/smart-wait-function">Learn       more</a>.</li>   <li className="li">[Web Service] Support redirection in POST request and 308     status code.</li>   <li className="li">Tips: You're recommended to open large HAR files with other     tools than Katalon Studio or keep those files not too large for     Katalon Studio to read it.</li> </ul> 
      
    
      

### <a id="id_78" class="anchor_top_offset"/>Fixes

      
        
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul">   <li className="li">Bug: Test Suite result is incorrect if a called test case gets     failed when <em className="ph i">log test steps</em> is disabled.</li>   <li className="li">Bug: Web Recorder does not generate XPath locators for SVG     elements.</li>   <li className="li">Bug: [Mobile] Cannot run a browser test on Android device using     Appium 1.15.0+.</li>   <li className="li">Bug: Cannot create a new project when failing to read Sample     Projects.</li>   <li className="li">Bug: Cannot execute test scripts having import paths containing     wildcard character (<code className="ph codeph">*</code>).</li>   <li className="li">Bug: Cannot start a browser when running with an iOS     simulator.</li>   <li className="li">Bug: NullPointerException when using Katalon Studio for the     first time.</li>   <li className="li">Bug: Cannot read variables in a custom profile if executing a     test suite collection remotely.</li>   <li className="li">Bug: Cannot execute test scripts that have Global Variables'     names containing the <code className="ph codeph">$</code> symbol.</li>   <li className="li">     Bug: An issue related to saving changes in Test Case Variable View.</li>   <li className="li">Bug: Katalon Studio does not read proxy configuration during     Recording.</li>   <li className="li">Bug: Web Recorder simultaneously generates     <code className="ph codeph">NavigateToUrl</code> keyword and action of an element.</li> </ul> 
      
    
    

## <a id="id_79" class="anchor_top_offset"/>Version 7.0.0- 7.0.10

    
              

### <a id="id_80" class="anchor_top_offset"/>New Features

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">Support <strong className="ph b">Close and Clean up</strong> item in Project menu for closing the project and removing the following items: <code className="ph codeph">.classpath</code>, and <code className="ph codeph">.project</code> files; <code className="ph codeph">bin</code>, <code className="ph codeph">Libs</code>, and <code className="ph codeph">.settings</code> folders.</li><li className="li">Support manually uploading Test Suite Collections' results to Katalon TestOps (Beta).</li><li className="li">Support connecting to Git with SSH. <a className="xref" href="/katalon-studio/manage-projects/project-settings/git-integration/git-integration-in-katalon-studio">Learn more</a> </li><li className="li">Allow configuring the usage tracked by Katalon Studio. <a className="xref" href="/katalon-studio/get-started/workspace-settings/katalon-studio-preferences/preferences-in-katalon-studio">Learn more</a>.</li><li className="li">Support data-driven testing with additional database sources. <a className="xref" href="/katalon-studio/data-driven-testing/configure-database-connection-for-data-driven-testing-in-katalon-studio">Learn more</a>.</li><li className="li">Support attaching Katalon Studio's source code for debugging. <a className="xref" href="/katalon-studio/execute-tests/execute-a-test-case">Learn more</a>.</li><li className="li">Support customizing Tests Explorer. <a className="xref" href="/katalon-studio/get-started/workspace-settings/toolbars-and-views-in-katalon-studio#concept-2869">Learn more</a>.</li><li className="li">Support Test Objects refactoring. <a className="xref" href="/katalon-studio/maintain-tests/refactor-test-objects-in-katalon-studio">Learn more</a>.</li><li className="li">Support Custom Keywords refactoring. <a className="xref" href="/katalon-studio/keywords/custom-keywords/custom-keywords-refactoring-in-katalon-studio">Learn more</a>.</li><li className="li">Support private plugins. <a className="xref" href="/katalon-platform/plugins-and-add-ons/katalon-store/katalon-studio-plugins/using-katalon-store-plugins">Learn more</a>.</li><li className="li">Support Windows 10 desktop application testing. See <a className="xref" href="/katalon-studio/get-started/supported-applications-under-test-aut/introduction-to-desktop-app-testing-in-katalon-studio">Windows Desktop Apps Test Design</a>.</li><li className="li">Support sharing test artifacts across projects. <a className="xref" href="/katalon-studio/manage-test-artifacts/test-artifacts-sharing-in-katalon-studio">Learn more</a>.</li><li className="li">Support Smart Wait function in a script and a project. See <a className="xref" href="/katalon-studio/record-and-spy/webui-record-and-spy-utilities/smart-wait-function">[WebUI] Smart Wait Function</a>.</li><li className="li">Support <a className="xref" href="/katalon-studio/manage-projects/set-up-projects/windows-desktop-apps-testing/set-up-winappdriver-in-katalon-studio">the WinAppDriver installation</a> and <a className="xref" href="/katalon-studio/manage-projects/set-up-projects/web-testing/handle-webdrivers/upgrade-or-downgrade-webdrivers-in-katalon-studio">Terminate running WebDrivers</a> options in Katalon Studio Tools.</li><li className="li">Support WebDriver event listeners. <a className="xref" href="/katalon-studio/manage-projects/set-up-projects/web-testing/handle-webdrivers/handle-webdrivers-with-eventfiringwebdriver-in-katalon-studio">Learn more</a>.</li><li className="li">Support customizing the Console log. <a className="xref" href="/katalon-studio/test-reports/view-test-reports/view-and-customize-execution-log-in-katalon-studio">Learn more</a>.</li><li className="li">Support Cucumber keywords executing one or multiple feature files with tags. Learn more about <a className="xref" href="/katalon-studio/keywords/keyword-description-in-katalon-studio/cucumber-keywords/cucumber-run-feature-file-with-tags">runFeatureFileWithTags</a> and <a className="xref" href="/katalon-studio/keywords/keyword-description-in-katalon-studio/cucumber-keywords/cucumber-run-feature-folder-with-tags">runFeatureFolderWithTags</a>.</li></ul> 

### <a id="id_81" class="anchor_top_offset"/>Changes and Improvements

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">[Web Service] Encode special characters in query parameters.</li><li className="li">Revert <strong className="ph b">IEDriverServer</strong> from 3.141.59 to 3.6.0.</li><li className="li">[Console mode] The <code className="ph codeph">katalon</code> launcher is replaced by <code className="ph codeph">katalonc</code> and there is a separate app named <strong className="ph b">Katalon Studio Runtime Engine</strong> for executing Katalon Studio in console mode. Click <a className="xref j-external-link" href="https://www.katalon.com/download/" target="_blank">here</a> to download.</li><li className="li">Convert <strong className="ph b">qTest</strong> and <strong className="ph b">Kobiton</strong> built-in integrations into plugins.</li><li className="li">Display errors of test scripts in the <strong className="ph b">Problems</strong> view.</li><li className="li">Support ChromeDriver version 77 and IEDriverServer version 3.141.59.</li><li className="li">Show a full stack trace of an exception thrown by custom classes in Test Hooks.</li><li className="li">Support manually uploading test suite collections' results to Katalon TestOps (Beta).</li><li className="li">[Web Service] Support passing proxy details through the script. <a className="xref" href="/katalon-studio/get-started/workspace-settings/katalon-studio-preferences/configure-proxy-preferences-in-katalon-studio">Learn more</a>.</li><li className="li">Update documents of <a className="xref j-external-link" href="https://docs.katalon.com/javadoc/index.html" target="_blank">Katalon Studio API Specification</a> to version 7.0.0.</li><li className="li">Upgrade Apache POI to version 3.17.</li><li className="li">Dynamic Querying Test Suite is renamed Dynamic Test Suite.</li><li className="li">Add plugins reloading options to the Project Settings.</li><li className="li">Support parsing the Request Message's template from the associated <code className="ph codeph">XSD</code> file when importing test objects from WSDL.</li><li className="li">Support adding the Organisation ID parameter to the Command Generator.</li><li className="li">Support selecting a Katalon TestOps (Beta)'s organization on the activation.</li><li className="li">Enhancement: Add some JVM options to reduce Katalon Studio's memory consumption.</li><li className="li">Support a hotkey of Spy Utility in Web Recorder to capture objects. <a className="xref" href="/katalon-studio/record-and-spy/webui-record-and-spy-utilities/record-web-utility-in-katalon-studio">Learn more</a>.</li><li className="li">Update <strong className="ph b">Quick Start</strong> in Katalon Studio after activation.</li><li className="li">Support adding <code className="ph codeph">.gitignore</code> and <code className="ph codeph">build.gradle</code> files when creating a project.</li><li className="li">Support uploading reports with pdf, HTML, CSV formats (generated by Basic Report plugin) to Katalon TestOps (Beta). <a className="xref" href="#">Learn more</a>.</li><li className="li">Support submitting test run results with captured videos to Katalon TestOps (Beta). <a className="xref" href="#">Learn more</a>.</li><li className="li">Support uploading the <code className="ph codeph">*.rp</code> file to Katalon TestOps (Beta) to parse more information on test results.</li><li className="li">Support creating a test plan right from the test suite collection screen in Katalon Studio to enhance the integration of Katalon Studio with Katalon TestOps (Beta). <a className="xref" href="#">Learn more</a>.</li><li className="li">Support uploading Project Code from Katalon Studio to Katalon TestOps (Beta). <a className="xref" href="#">Learn more</a>.</li><li className="li">Update the integration mechanism with Katalon TestOps (Beta). <a className="xref" href="#">Learn more</a>.</li><li className="li">Update the integration configurations with Katalon TestOps (Beta) when a new project is created.</li><li className="li">Support auto-filling the input of <a className="xref" href="#">Katalon API Key</a> in the command-line generator.</li><li className="li">Support generating test results in JUnit format.</li><li className="li">Support uploading reports of test suite collections to Katalon TestOps (Beta).</li><li className="li">Remove unnecessary information in the console log when users execute in the console mode for the first time.</li><li className="li">Support passing more information to the console mode execution with <code className="ph codeph">--info -buildLabel="text" -buildURL="text"</code>. See <a className="xref" href="/katalon-studio/execute-tests/katalon-runtime-engine/command-line-syntax-in-katalon-runtime-engine#concept-1437">General Options</a> in Console Mode Execution.</li><li className="li">Upgrade the activation mechanism in Katalon Studio to seamlessly integrate with Katalon TestOps (Beta). See <a className="xref" href="/katalon-studio/get-started/activate-licenses">Activate Katalon Studio</a>.</li><li className="li">Merge the Plugins menu into the Tools menu.</li><li className="li">Support MySQL Database version <strong className="ph b">8.0.17</strong>.</li><li className="li">Support automatically reloading plugins when opening a project.</li></ul> 

### <a id="id_82" class="anchor_top_offset"/>Fixes

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">Bug: [DDT] Cannot get values from data files with database type     in a test case.</li><li className="li">Bug: Cannot log in to Katalon Studio with passwords containing     special characters.</li><li className="li">Bug: [Web Service] SOAP response has an empty header.</li><li className="li">Bug: Cannot reload plugins with credentials containing special     characters.</li><li className="li">Bug: The <strong className="ph b">Results</strong> tab of Test Suites/Test Suite     Collection fails to automatically refresh after the first     execution.</li><li className="li">Bug: <strong className="ph b">Show references</strong> of test objects fails to     display the objects' references in global variables and test case     variables.</li><li className="li">Bug: Cannot send SOAP requests when <strong className="ph b">WSDL</strong> files     contain the relative <code className="ph codeph">xsi:schemaLocation</code>.</li><li className="li">     Bug: [WebUI Keyword] The <code className="ph codeph">WebUI.clickImage</code> keyword fails to perform.</li><li className="li">Bug: [Web Service] <code className="ph codeph">getCurrentRequest()</code> always gets     default values instead of a variable's values passed from test     case.</li><li className="li">Bug: Incorrectly return code when <strong className="ph b">Follow       redirects</strong> is disabled in Web Service Request. <a className="xref j-external-link" href="https://forum.katalon.com/t/followreridects-does-not-work/33800" target="_blank">More       details</a>.</li><li className="li">Bug: Cannot save modifications in the configuration tab of the     Web Service Request.</li><li className="li">Bug: Cannot detect mobile test objects having parameterized     global variables in their properties.</li><li className="li">Bug: [Console Mode] To retry executing failed test cases in     Test Suite Collection fails to return the correct exit code.</li><li className="li">Bug: [Data Binding] An issue causes binding Variables to Test     Data to fail.</li><li className="li">Bug: [WebService] Verification Editor doesn't keep Unicode     characters.</li><li className="li">Bug: [Mobile Testing] Cannot retry executing failed test     cases.</li><li className="li">Bug: Web service response displays garbled text as non-Latin     characters.</li><li className="li">Bug: [Basic Report Plugin] CSV Report status is always     Incomplete.</li><li className="li">Bug: The Log Viewer’s cursor incorrectly renders when     selecting a log message.</li><li className="li">Bug: Newly added variables disappear after a switch from the     Variable tab to another tab.</li><li className="li">Bug: An issue related to Variable binding when the data     contains special characters.</li><li className="li">Bug: The Delay keyword doesn't work when the passing data is     BigDecimal.</li><li className="li">Bug: Har files disappear after having been opened for the first     time with the current Web Service object.</li><li className="li">Bug: [Custom Keyword] an issue related to the default package     name when users create a keyword without entering a package     name.</li><li className="li">Bug: [Katalon TestOps (Beta)] Cannot navigate to the URL     configured by users in View Execution History.</li><li className="li">Bug: [Katalon TestOps (Beta)] an issue related to the error     message when users create a new project for the invited team     without permission.</li><li className="li">Bug: [GlobalVariable] Cannot execute a script with a profile     that has a Global Variable with invalid syntax.</li><li className="li">Bug: [WebUI Keywords] The <code className="ph codeph">verifyElementPresent()</code>     and <code className="ph codeph">verifyElementNotPresent()</code> keywords should return     <code className="ph codeph">false</code> instead of throwing an exception when the     verified elements do not exist.</li><li className="li">Bug: The <code className="ph codeph">Delay between actions</code> fails to perform as     configured.</li><li className="li">Bug: An issue causes <code className="ph codeph">callTestCase</code> to fail.</li><li className="li">Bug: <code className="ph codeph">findWebElements</code> fails when the <code className="ph codeph">Default       wait for element timeout</code> is set to 0 in the Execution     Settings.</li><li className="li">Bug: [Web Recorder] An issue related to the <code className="ph codeph">Cannot save       entity: file path length limit exceeded.</code> error when saving     test objects.</li><li className="li">Bug: Custom Keywords are not displayed in the Recent keywords     after being used.</li><li className="li">Bug: An issue related to renaming a folder with uppercase or     lowercase characters. <a className="xref j-external-link" href="https://github.com/katalon-studio/katalon-studio/issues/189" target="_blank">More       details</a>.</li></ul> 
