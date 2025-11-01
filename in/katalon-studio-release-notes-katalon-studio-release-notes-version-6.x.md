---
hide_title: true
title: 'Katalon Studio Release Notes: Version 6.x'
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="id_version-60" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Katalon Studio Release Notes: Version 6.x

    

## <a id="id_1" class="anchor_top_offset"/>Version 6.3.3

    
          
      

### <a id="id_2" class="anchor_top_offset"/>Improvements

      
        
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul">   <li className="li">Remove the SLF4J warning message in the execution log when     running in Console mode.</li>   <li className="li">Add a menu item on Katalon Studio's main toolbar for manually     updating WebDrivers.</li> </ul> 
      
    
      

### <a id="id_3" class="anchor_top_offset"/>Fixes

      
        
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul">   <li className="li">Bug: Cannot create or open a dynamic test suite.</li>   <li className="li">Bug: <code className="ph codeph">Run from here</code> doesn't work if the script     contains <a className="xref j-external-link" href="http://docs.groovy-lang.org/latest/html/documentation/core-operators.html#_unary_operators" target="_blank">Postfix</a>     expressions.</li> </ul> 
      
    
    

## <a id="id_4" class="anchor_top_offset"/>Version 6.3.0 - 6.3.2

    
              

### <a id="id_5" class="anchor_top_offset"/>New Features

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">Support Dark theme in addition to the default Light theme. See     <a className="xref" href="/katalon-studio/get-started/workspace-settings/change-katalon-studio-theme">Using       Katalon Studio in Dark theme</a>.</li><li className="li">Support spying, recording and executing the Mobile script on     custom cloud-based testing tools; and an option to choose between     AndroidDriver or iOSDriver when Appium is set as <code className="ph codeph">Remote       server type</code>. See <a className="xref" href="/katalon-studio/manage-projects/set-up-projects/mobile-testing/mobile-app-testing-with-remote-devices">Testing       Mobile Apps Using Custom Cloud Devices</a> and <a className="xref" href="/katalon-studio/manage-projects/project-settings/desired-capabilities/set-up-remote-server-in-desired-capabilities-in-katalon-studio">Remote       Desired Capabilities</a>.</li><li className="li">Support testing existing applications on Android and iOS     devices. See <a className="xref" href="/katalon-studio/keywords/keyword-description-in-katalon-studio/mobile-keywords/mobile-start-existing-application">[Mobile]       Start Existing Application</a>.</li></ul> 

### <a id="id_6" class="anchor_top_offset"/>Improvements

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">Allow Test Reports to be viewed directly in Test Suite and Test Suite Collection Views in Result Tab. See <a className="xref" href="/katalon-studio/test-reports/view-test-reports/view-test-suite-and-test-suite-collection-reports-in-katalon-studio">Test Suite Report</a> or <a className="xref" href="/katalon-studio/test-reports/view-test-reports/view-test-suite-and-test-suite-collection-reports-in-katalon-studio">Test Suite Collection Report</a>.</li><li className="li">Support sending custom headers in SOAP requests.</li><li className="li">Directly parameterize Global variables in Test Objects. See <a className="xref" href="/katalon-studio/data-driven-testing/global-variables-and-execution-profile">Global Variables</a>.</li><li className="li">Allow implementing variable binding without converting test data to strings. See <a className="xref" href="#">Enhanced Variable Binding</a>.</li><li className="li">Support implementing an annotation called BeforeTestDataBindToTestCase in test listener. See <a className="xref" href="#">[Quick tip] Enhanced Variable Binding</a>.</li><li className="li">Support Move up and Move down items in the default profile. See <a className="xref" href="/katalon-studio/data-driven-testing/global-variables-and-execution-profile">Global Variables</a><a className="xref" href="/katalon-studio/data-driven-testing/global-variables-and-execution-profile">Execution profile</a>.</li><li className="li">Support quickly setting up your devices by displaying sub-menus of Android, iOS and Kobiton devices in Mobile Spy and Recorder tool items.</li><li className="li">Enhancement: Remove the <strong className="ph b">-- disable-extensions</strong> argument from Chrome Desired Capabilities.</li><li className="li">Support Chrome version 76.</li></ul> 
      

### <a id="id_7" class="anchor_top_offset"/>Fixes

      
        
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul">   <li className="li">Bug: Test object references are displayed incorrectly when new     test objects are created from the existing ones.</li>   <li className="li">Bug: The scroll bar disappears in the Variables section.</li>   <li className="li">Bug: Incorrectly detect and highlight Mobile Test Objects when     using Mobile Recorder or Mobile Object Spy.</li>   <li className="li">Bug: Incorrectly detect Test Objects’ locations when     using Mobile Recorder or Mobile Object Spy.</li>   <li className="li">Bug: Cannot record additional items when using Web Recorder on     existing test cases.</li>   <li className="li">Bug: Cannot activate Katalon Studio after resetting the     password.</li>   <li className="li">Bug: Cannot load test steps in Manual View of a test case when     <em className="ph i">Initially open Test Case in Script view</em> is set by     default.</li>   <li className="li">Bug: Cannot run test cases with Microsoft Edge 18.0 on     BrowserStack.</li>   <li className="li">Bug: Katalon Studio always uses Xpath as a default element     locator instead of Web Locators defined by users.</li>   <li className="li">Bug: <em className="ph i">Continue Recording</em> silently deletes WebService     parameters.</li>   <li className="li">Bug: The new checkpoint dialog box is not resizable and does     not display all UI elements on Windows 10.</li>   <li className="li">Bug: The Sender field is empty when users send an email.</li>   <li className="li">Bug: An issue related to running a test suite with too large     test data.</li>   <li className="li">Bug: NullPointerException occurs when using Web Recorder on an     empty test case.</li>   <li className="li">Bug: Global Variables initialization fails when an existing     WebDrivers’ instance is used in a custom profile.</li>   <li className="li">Bug: "Bind to test case as string" checkbox in Test Data is     always checked while a test suite is executed.</li>   <li className="li">Bug: Slow performance of adding Variables to test cases.</li>   <li className="li">Bug: HAR files fail to be logged when the     <strong className="ph b">SendRequestAndVerify</strong> keyword is used.</li>   <li className="li">Bug: The <strong className="ph b">TapAtPosition</strong> keyword fails to     run.</li> </ul> 
      
    
    

## <a id="id_8" class="anchor_top_offset"/>Version 6.2.2

    
          
      

### <a id="id_9" class="anchor_top_offset"/>Improvements

      
        
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul">   <li className="li">Support sending emails from another email address in addition     to the default username.</li> </ul> 
      
    
      

### <a id="id_10" class="anchor_top_offset"/>Fixes

      
        
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul">   <li className="li">Bug: Cannot save test cases when the Test Case default view is     in Script Mode</li>   <li className="li">Bug: Cannot execute test cases with Microsoft Edge     18.17763.</li>   <li className="li">Bug: Cannot send emails with TLS Protocol.</li>   <li className="li">Bug: An open profile is required being saved when it is just     reopened, and no modification has been made.</li> </ul> 
      
    
    

## <a id="id_11" class="anchor_top_offset"/>Version 6.2.0 - 6.2.1

    
          
      

### <a id="id_12" class="anchor_top_offset"/>Improvements

      
        
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul">   <li className="li">Show plugins which failed to reload</li>   <li className="li">Support SSL client certificate</li>   <li className="li">Support Appium v1.12.1, iOS 12.2, Xcode 10.2</li>   <li className="li">Support overriding default WebDrivers per project</li>   <li className="li">Update selenium-standalone-server from 3.7.1 to 3.141.59</li>   <li className="li">Update appium-java-client from 5.0.0 to 7.0.0</li>   <li className="li">Remove embedded carthage, libimobiledevice, and ios-deploy</li> </ul> 
      
    
      

### <a id="id_13" class="anchor_top_offset"/>Fixes

      
        
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul">   <li className="li">Bug: Cannot send emails if the attachment is empty</li>   <li className="li">Bug: Cannot import Postman requests with protocol HTTP</li>   <li className="li">Bug: TimeoutException when evaluating variables for Web Service     requests</li>   <li className="li">Bug: Cannot save a draft request to Object Repository</li>   <li className="li">Bug: Cannot edit build.gradle files</li>   <li className="li">Bug: [Linux] Icons on the toolbar aren't displayed</li>   <li className="li">Bug: [Linux] Katalon Studio UI hangs when selecting Keywords in     Manual view</li>   <li className="li">Bug: Cannot filter files in Project Explorer using keywords     containing uppercase characters</li>   <li className="li">Bug: Cannot import Postman collections containing requests with     the same names</li>   <li className="li">Bug: Cannot import Postman collections with long folder     names</li>   <li className="li">Bug: Cannot execute web testing projects on cloud mobile     devices (e.g. Sauce Labs)</li>   <li className="li">Bug: Cannot import Postman collections containing requests with     body information missing</li>   <li className="li">Bug: Cannot import Postman requests whose names are URLs</li>   <li className="li">Bug: Custom headers are not sent along with SOAP requests</li>   <li className="li">Bug: Postman collection's sub-folder structure was not     preserved</li>   <li className="li">Bug: Katalon Studio is hanged when editing an argument type in     Desired Capabilities dialog</li> </ul> 
      
    
    

## <a id="id_14" class="anchor_top_offset"/>Version 6.1.3 - 6.1.5

    
          
      

### <a id="id_15" class="anchor_top_offset"/>Plug-ins

      
        
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul">   <li className="li">     <a className="xref j-external-link" href="https://store.katalon.com/product/74/Test-Suite-Collection-Scheduler" target="_blank">       <strong className="ph b">Test         Suite Collection Scheduler Plugin</strong>     </a>: A plugin that lets     Katalon Studio run a test suite collection at a specific time in     the future.</li>   <li className="li">     <a className="xref j-external-link" href="https://store.katalon.com/product/59/Basic-Report" target="_blank">       <strong className="ph b">Katalon         Studio Report Plugin</strong>     </a>: A plugin that replaces the     current report feature of Katalon Studio. Starting from v6.1.5, the     report feature is no longer available natively in Katalon Studio,     users need to download this plugin to continue using this     feature.</li> </ul> 
      
    

### <a id="id_16" class="anchor_top_offset"/>Fixes and Improvements

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">Fixed a bug where Kobiton devices are duplicated.</li><li className="li">Fixed a bug where Katalon Studio cannot be opened if a custom keyword plugin contains errors.</li><li className="li">Fixed a bug where HAR files are not generated with the correct name.</li><li className="li">Fixed a bug where Safari webdriver install requirements pop-up shows up before every test.</li><li className="li">Fixed a bug where test execution crashes when failing to get recent projects.</li><li className="li">Fixed a bug where <code className="ph codeph">executeJavaScript</code> keyword fails when there are 3 arguments.</li><li className="li">Fixed a bug in Jira Plugin where Default JIRA Issue Type field in integration setting contains duplicated values.</li><li className="li">Added some small UI improvements when selecting devices and app files.</li><li className="li">[BETA] Added the capability to import Test Objects from Postman collection JSON file. Importable fields include Postman fields in Params, Headers, Body.</li><li className="li">Added a scroll bar in dropdown when selecting execution profiles.</li><li className="li">Added the capability to display all user folders/files in Tests Explorer.</li><li className="li">Added the capability to allow configuration of plugin installation location in <span className="ph menucascade"><span className="ph uicontrol">Preferences</span><abbr title="and then"> &gt; </abbr><span className="ph uicontrol">Katalon</span><abbr title="and then"> &gt; </abbr><span className="ph uicontrol">Plugins</span></span>.</li><li className="li">Added the capability to use variables in XPaths when finding test objects.</li></ul> 
    

## <a id="id_17" class="anchor_top_offset"/>Version 6.1.2

    
          

### <a id="id_18" class="anchor_top_offset"/>Fixes and Improvements

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">Allowed users to disable auto-redirection for API test     objects.</li><li className="li">Highlighted test steps that call <code className="ph codeph">markFailed</code>.</li><li className="li">Fixed a bug that caused test cases to fail with status     <code className="ph codeph">Reason: BUG! exception in phase 'semantic analysis' in source       unit</code>.</li><li className="li">Showed test case tags in HTML, CSV, and PDF reports.</li><li className="li">Added a tab to Search Dialog for searching test objects.</li><li className="li">Showed raw data of request and response when executing an API     test object.</li><li className="li">Fixed a bug that caused the last step to by marked as     <code className="ph codeph">failed</code> if any previous steps had failed.</li><li className="li">Fixed an issue of API testing where POST request JSON Body     content is disappeared.</li></ul> 
      

### <a id="id_19" class="anchor_top_offset"/>Build custom keywords with Settings

      
        
<p xmlns="http://www.w3.org/1999/xhtml" className="p">With this new feature, a <strong className="ph b">Settings</strong> page under   <strong className="ph b">Project Settings/Plugins</strong> can be created for a   custom-keyword plugin. This can be utilized to store project-scoped   variables for users to customize.</p> 
      
                      
<h4 xmlns="http://www.w3.org/1999/xhtml" className="title topictitle4 anchor_top_offset" id="id_20">Add Settings page</h4> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Custom Keyword Plugin declares the setting page UI in   <strong className="ph b">katalon-plugin.json</strong> with this sample:</p> 
<pre xmlns="http://www.w3.org/1999/xhtml" className="pre codeblock"><code>{"{"}{"\n"}{"   "}"keywords": [],{"\n"}{"   "}"configuration": {"{"}{"\n"}{"      "}"settingId": "some id",{"\n"}{"      "}"settingPage": {"{"}{"\n"}{"         "}"name": "name",{"\n"}{"         "}"components": [{"\n"}{"            "}{"{"}{"\n"}{"               "}"key": "key1",{"\n"}{"               "}"type": "text",{"\n"}{"               "}"label": "My Label 1",{"\n"}{"               "}"defaultValue":"My default value 1"{"\n"}{"            "}{"}"},{"\n"}{"            "}{"{"}{"\n"}{"               "}"key": "key2",{"\n"}{"               "}"type": "secret",{"\n"}{"               "}"label": "My Label 2"{"\n"}{"            "}{"}"}, ...{"\n"}{"         "}]{"\n"}{"      "}{"}"}{"\n"}{"   "}{"}"}{"\n"}{"}"}{"\n"}</code></pre> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">     <p className="p">       <strong className="ph b">settingId</strong>: id the setting file that stores user       setting properties in the setting page. There is a file will       generated to store user settings at location:</p>     <div className="p">       <pre className="pre codeblock"><code>&lt;Project dir&gt;/settings/external/&lt;settingId&gt;.properties</code></pre>     </div>   </li><li className="li">     <p className="p">       <strong className="ph b">settingPage</strong> : contains the following       sub-properties</p>     <ul className="ul"><li className="li">         <strong className="ph b">name</strong>: Name of the setting page</li><li className="li">         <strong className="ph b">components</strong>: list of UI components          <ul className="ul"><li className="li">             <strong className="ph b">key</strong>: key of the component</li><li className="li">             <strong className="ph b">label</strong>: label of the component</li><li className="li">             <strong className="ph b">type</strong>: type of the component ('text' or             'secret')</li><li className="li">             <strong className="ph b">defaultValue</strong>: default value of the             component</li></ul>       </li></ul>   </li></ul> 
<h4 xmlns="http://www.w3.org/1999/xhtml" className="title topictitle4 anchor_top_offset" id="id_21">Prepare to test</h4> 
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol"><li className="li">Clone <code className="ph codeph">https://github.com/katalon-studio/katalon-studio-excel-custom-keywords-plugin</code></li><li className="li">Open the project in Katalon Studio at least once </li><li className="li">     <p className="p">Modify katalon-plugin.json with this template</p>     <pre className="pre codeblock"><code>{"{"}{"\n"}{"   "}"keywords": ["com.katalon.plugin.keyword.excel.ExcelReadKeywords", "com.katalon.plugin.keyword.excel.ExcelWriteKeywords"],{"\n"}{"   "}"configuration": {"{"}{"\n"}{"      "}"settingId": "com.katalon.plugin.keyword.excel-keywords",{"\n"}{"      "}"settingPage": {"{"}{"\n"}{"         "}"name": "Excel Keywords",{"\n"}{"         "}"components": [{"\n"}{"            "}{"{"}{"\n"}{"               "}"key": "username",{"\n"}{"               "}"type": "text",{"\n"}{"               "}"label": "Username"{"\n"}{"            "}{"}"},{"\n"}{"            "}{"{"}{"\n"}{"               "}"key": "password",{"\n"}{"               "}"type": "secret",{"\n"}{"               "}"label": "Password"{"\n"}{"            "}{"}"}{"\n"}{"         "}]{"\n"}{"      "}{"}"}{"\n"}{"   "}{"}"}{"\n"}{"}"}{"\n"}</code></pre></li><li className="li">Build excel keyword project     <code className="ph codeph">gradle katalonPluginPackage</code>     <p className="p">A jar file will be generated in <strong className="ph b">/build/libs</strong> folder</p></li><li className="li"><p className="p">Copy and paste the generated jar file to <strong className="ph b">Plugins</strong> folder of a Katalon Studio project (Project A)</p>   </li><li className="li"><p className="p">Open <strong className="ph b">Project A</strong> and navigate to <strong className="ph b">Project Settings/Plugins/Excel Keywords</strong></p>   </li><li className="li"><p className="p">Customize the settings as wish</p></li></ol> 
<h4 xmlns="http://www.w3.org/1999/xhtml" className="title topictitle4 anchor_top_offset" id="id_22">Retrieve the setting values</h4> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">The values can be retrieved in keyword script as the following sample:</p> 
<pre xmlns="http://www.w3.org/1999/xhtml" className="pre codeblock"><code>import com.kms.katalon.core.configuration.RunConfiguration as RunConfiguration{"\n"}import com.kms.katalon.core.setting.BundleSettingStore as BundleSettingStore{"\n"}{"\n"}BundleSettingStore bundleSetting = new BundleSettingStore(RunConfiguration.getProjectDir(), '&lt;setting_id&gt;', true){"\n"}println(bundleSetting.getString('username', '')){"\n"}println(bundleSetting.getString('password', ''){"\n"}</code></pre> 
    

## <a id="id_23" class="anchor_top_offset"/>Version 6.1.1

    
              
      

### <a id="id_24" class="anchor_top_offset"/>Fixes and Improvements

      
        
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul">   <li className="li">Added a warning when executing CLI mode under the target     project folder.</li>   <li className="li">Fixed an issue where Katalon Studio cannot reload plugins.</li>   <li className="li">Added the current version and commit ID to the Katalon Studio's     window title bar.</li>   <li className="li">Updated chromedriver to version 73.0.3683.68</li>   <li className="li">Updated EdgeDriver to version 6.17134</li> </ul> 
      
    
      

### <a id="id_25" class="anchor_top_offset"/>Auto-healing Smart XPath Plugin

      
        
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul">   <li className="li">Fixed an issue where XPaths with incorrect syntax stop the     healing process.</li>   <li className="li">Added screenshots of alternative XPaths' results to assist the     review process.</li> </ul> 
      
    
      

### <a id="id_26" class="anchor_top_offset"/>Package Test Listeners as plugins

      
        
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul">   <li className="li">From Katalon Studio 6.1.1 Test Listeners can be packaged as     plugins.</li>   <li className="li">For a sample plugin see     https://github.com/katalon-studio/katalon-studio-result-summary-test-listeners-plugin.</li>   <li className="li">The only differences between Test Listeners and Custom Keywords     plugins are in <code className="ph codeph">build.gradle</code> and     <code className="ph codeph">katalon-plugin.json</code>:</li> </ul> 
        
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <code className="ph codeph">build.gradle</code>:</p> 
                  
<pre xmlns="http://www.w3.org/1999/xhtml" className="pre codeblock"><code>sourceSets {"{"}{"\n"}{"  "}main {"{"}{"\n"}{"    "}groovy {"{"}{"\n"}{"      "}srcDirs = ['Keywords', 'Libs', 'Test Listeners', 'Include/scripts/groovy']{"\n"}{"    "}{"}"}{"\n"}{"  "}{"}"}{"\n"}{"}"}{"\n"}</code></pre> 
                
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <code className="ph codeph">katalon-plugin.json</code>:</p> 
                  
<pre xmlns="http://www.w3.org/1999/xhtml" className="pre codeblock"><code>{"{"}{"\n"}{"    "}"keywords": [],{"\n"}{"    "}"listeners": ["KatalonPluginResultSummary"]{"\n"}{"}"}{"\n"}</code></pre> 
              
    
    

## <a id="id_27" class="anchor_top_offset"/>Version 6.1.0

    
          
      

### <a id="id_28" class="anchor_top_offset"/>Custom Keyword Plugin

      
        
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Introducing Custom Keyword Plugin for Katalon Studio v6.1.0 for   collaboration. Custom Keywords now can be shared among the project   team or to the world via Katalon Store. Simply Create. Upload. and   Share!</p> 
        
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/new/version-61/Window.png")} /><br /><br /> </p> 
      
    

### <a id="id_29" class="anchor_top_offset"/>Fixes and Improvements

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">Fixed an issue where project having many <code className="ph codeph">GlobalVariables</code> cannot be opened. <a className="xref j-external-link" href="https://github.com/katalon-studio/katalon-studio/issues/74" target="_blank">Click here for more details.</a></li><li className="li">Fixed merging Objects to Object Repository issue. <a className="xref j-external-link" href="https://github.com/katalon-studio/katalon-studio/issues/103" target="_blank">Click here for more details.</a></li><li className="li">Removed the dialogs when Katalon Studio is closed. <a className="xref j-external-link" href="https://forum.katalon.com/t/rate-us-pop-up-message/18830" target="_blank">Click here for more details.</a></li><li className="li">Fixed an issue where <code className="ph codeph">RunConfiguration</code> cannot be functioned. <a className="xref j-external-link" href="https://forum.katalon.com/t/unable-to-apply-global-directory-file-storage-path-in-6-0-5/20747/12" target="_blank">Click here for more details.</a></li><li className="li">Fixed an issue where the report is overlapped when running Test Suite Collection in Command Line Mode. <a className="xref j-external-link" href="https://github.com/katalon-studio/katalon-studio/issues/19" target="_blank">Click here for more details.</a></li><li className="li">Fixed an issue where copied console log contains special characters. <a className="xref j-external-link" href="https://forum.katalon.com/t/copy-paste-from-console-log/18458" target="_blank">Click here for more details.</a> </li><li className="li">Implemented a few adjustments on Katalon Studio UI.</li><li className="li">Fixed an issue with loading Custom Keyword plugin. <a className="xref j-external-link" href="https://forum.katalon.com/t/how-to-package-custom-keyword-as-plugin/20321/18?u=devalex88" target="_blank">Click here for more details.</a></li></ul> 
    

## <a id="id_30" class="anchor_top_offset"/>Version 6.0.6

    
      
      

### <a id="id_31" class="anchor_top_offset"/>Fixes and Improvements

      
        
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul">   <li className="li">Fixed an issue where REST WS Object - URL field automatically     added question mark right after saving</li>   <li className="li">Fixed an issue where recorder function is not working with     Internet Explorer in Katalon Studio version 5.10.1</li>   <li className="li">Fixed an issue where script view for Profile variables is     empty</li>   <li className="li">Provide more details in log error messages</li>   <li className="li">Fixed an issue where users can not set proxy settings to     selenium grid for accessing applications behind the firewall</li>   <li className="li">Fixed overriding Global Variable for Test Suite Collection     issue</li>   <li className="li">Fixed an issue where Test Suite Collection cannot be executed     in CMD mode</li> </ul> 
      
    
    

## <a id="id_32" class="anchor_top_offset"/>Version 6.0.5

    
          
      

### <a id="id_33" class="anchor_top_offset"/>OAuth 2.0 Support

      
        
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Since version 6.0.5, Katalon Studio supports OAuth 2.0 expanding   Web Service testing capabilities. Most of the common grant types   are supported including “Authorization code,”   “Password Credentials,” “Client   Credentials,” and “Refresh Token.” <a className="xref" href="/katalon-studio/test-objects/api-test-objects/authorization/authorization-oauth-2.0-in-katalon-studio">Learn     more</a> </p> 
        
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/authorization-oauth2/5.png")} /><br /><br /> </p> 
      
    
      

### <a id="id_34" class="anchor_top_offset"/>Fixes and Improvements

      
        
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul">   <li className="li">Fixed an issue where more than one keyword setText is displayed     on Web Record dialog</li>   <li className="li">Fixed an issue where commented lines at the bottom of test     script are accidentally deleted - <a className="xref j-external-link" href="https://forum.katalon.com/t/most-of-my-automation-script-got-deleted/16005/4" target="_blank">More       details</a>   </li>   <li className="li">Fixed some minor bugs and made some enhancements for BDD</li>   <li className="li">Fixed Global variables issues - <a className="xref j-external-link" href="https://forum.katalon.com/t/groovy-error-unable-to-resolve-class-internal-globalvariable/9557/168" target="_blank">More       details</a>   </li>   <li className="li">Allows users to create Web Service Object in code</li>   <li className="li">Fixed an issue where profiles are evaluated even though it is     not in use</li>   <li className="li">Moved ScreenUtil from WebUIAbstractKeyword to ImageKeyword</li>   <li className="li">Display information log when using GlobalVariable, not in     selected ExecutionProfile</li>   <li className="li">Fixed an issue where ScrollToText function does not work</li>   <li className="li">Fixed an issue where adding the value with multiple lines in     the variable section can not be function(Global or Normal) - <a className="xref j-external-link" href="https://github.com/katalon-studio/katalon-studio/issues/46" target="_blank">More       details</a>   </li>   <li className="li">Fixed an issue where commented lines at the bottom of test     script are deleted accidentally</li> </ul> 
      
    
    

## <a id="id_35" class="anchor_top_offset"/>Version 6.0

    
                  
      

### <a id="id_36" class="anchor_top_offset"/>Introduce Katalon Store Integration

      
        
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Katalon Store is a platform that leads users to the world of   amazing plugins for Katalon Studio. This is also a collaborative   marketplace for both end-users and developers to build add-on   products, in order to maximize Katalon Studio's test automation   capabilities. Katalon Store website is available at   www.store.katalon.com.</p> 
        
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/new/version-60/3.png")} /><br /><br /> Each plugin in Katalon Store comes with a detailed   description so that you can preview the functions and features   before installing.</p> 
        
<p xmlns="http://www.w3.org/1999/xhtml" className="p">If you cannot find the suitable add-on to your wish, you are   welcomed to be the publisher with the Publish A New Plugin and   Manage Published Plugins functions.</p> 
      
    

### <a id="id_37" class="anchor_top_offset"/>Download, Manage, and Search for Plugins from Your Katalon         Studio

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Directly linked to your Katalon Studio app., all of the   installed plugins can be easily reloaded and managed from your   local device. Learn more <a className="xref" href="/katalon-platform/get-started/get-started-with-katalon-testops">here</a>.   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/new/version-60/2.png")} /><br /><br /> </p> 
      

### <a id="id_38" class="anchor_top_offset"/>Install Executable JAR File Plugins

      
        
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/new/version-60/1.png")} /><br /><br /> Katalon allows you to install executable JAR plugins   right on the Quick Access Toolbar. In case these JAR files are   already available on your computer, you can easily install them by   navigating to <strong className="ph b">Plugin</strong> &gt; <strong className="ph b">Install     Plugin</strong>.</p> 
      
    
      

### <a id="id_39" class="anchor_top_offset"/>Fixes and Improvements

      
        
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul">   <li className="li">Fixed remembering chosen test cases issue in Test Case Browser     model</li>   <li className="li">Fixed duplicating added test case to a test suite issue</li>   <li className="li">Allow to run a test suite with duplicated test cases using data     binding</li>   <li className="li">Fixed an issue where Automatically check for new version does     not work with unchecked</li>   <li className="li">Fixed an issue where SWTException thrown when clicking 'Capture     Object'</li>   <li className="li">Fixed an issue on swipe command, losing objects references</li>   <li className="li">Fixed SwipeKeyword and TapAtPositionKeyword that didn't work     properly</li>   <li className="li">Improve new project pop-up UI</li> </ul> 
      
    
