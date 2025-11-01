---
hide_title: true
title: Execute test with Katalon Studio in Internet Explorer (IE) mode in Microsoft Edge
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="id" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Execute test with <span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon Studio</span>  in Internet Explorer (IE) mode in Microsoft Edge

<p xmlns="http://www.w3.org/1999/xhtml" className="p">As the Internet Explorer desktop application is determined to go out of support on June 15, 2022, Microsoft introduces IE mode in Microsoft Edge for organizations that still need Internet Explorer 11 for backward compatibility for legacy websites or apps. To learn more about IE mode, refer to this Microsoft document: <a className="xref j-external-link" href="https://docs.microsoft.com/en-us/deployedge/edge-ie-mode" target="_blank">What is Internet Explorer (IE) mode?</a> </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">This tutorial shows you how to use Katalon Studio to run test cases in IE mode in Microsoft Edge.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">In our example, we use a custom keyword called <code className="ph codeph">openIEModeEdgeBrowser</code> to open Microsoft Edge in IE mode. To learn more about custom keywords in Katalon Studio, refer to this document: <a className="xref" href="/katalon-studio/keywords/custom-keywords/introduction-to-custom-keywords-in-katalon-studio">Introduction to Custom Keywords</a>.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">You can find the sample project with the custom keyword in this GitHub repository: <a className="xref j-external-link" href="https://github.com/katalon-studio-samples/open-ie-mode-sample-project" target="_blank">Open IE Mode in Edge Chromium</a>.</p> 
<div xmlns="http://www.w3.org/1999/xhtml" className="note note note_note"><span className="note__title">Note:</span> <ul className="ul"><li className="li">You can execute tests in Internet Explorer (IE) mode in Microsoft Edge, but you cannot record new tests in IE mode in Microsoft Edge.</li><li className="li"><p className="p">Katalon Studio no longer supports recording or spying in IE as a standalone browser.</p></li></ul></div>

## <a id="id_1" class="anchor_top_offset"/>Configure Internet Options settings


### <a id="task-9625" class="anchor_top_offset"/>Internet Explorer Configurations on Windows 10

<section xmlns="http://www.w3.org/1999/xhtml" className="section context">To run tests on Internet Explorer (IE), you need the following setups:</section> 
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol steps"><li className="li step stepexpand"><span className="ph cmd"><span className="ph uicontrol">Enable Protected Mode</span> must be disabled for all available zones. To do so, choose <span className="ph uicontrol">Internet Options</span> from <span className="ph uicontrol">Control Panel</span>, then switch to the <span className="ph uicontrol">Security</span> tab. Uncheck the <span className="ph uicontrol">Enable Protected Mode</span> option.</span><div className="itemgroup info"><img className="image" width={300} src={useBaseUrl("/ee18bba0-6ef3-11ed-a602-0242cfbc79b5/ks-internet-properties.png")} /></div></li><li className="li step stepexpand"><span className="ph cmd">Zoom the IE browser to 100% so that native mouse events can be set to correct coordinates.</span></li><li className="li step stepexpand"><span className="ph cmd">For IE 11, you also need to set a registry entry on the target computer so that the driver can maintain a connection to the Internet Explorer instances. To do so, follow these steps:</span><ol type="a" className="ol substeps"><li className="li substep substepexpand"><span className="ph cmd">To open the <span className="ph uicontrol">Registry Editor</span>, type <code className="ph codeph">regedit</code> into <span className="ph uicontrol">Command Prompt</span>.</span></li><li className="li substep substepexpand"><span className="ph cmd">Locate the <span className="ph uicontrol">FEATURE_BFCACHE</span> subkey. If you cannot find the <span className="ph uicontrol">FEATURE_BFCACHE</span> subkey, create one.</span><div className="itemgroup info"><ul className="ul"><li className="li">For 32-bit Windows, the key is at <code className="ph codeph">HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Internet Explorer\Main\FeatureControl\FEATURE_BFCACHE </code>.</li><li className="li">For 64-bit Windows, the key is at <code className="ph codeph">HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Internet Explorer\Main\FeatureControl\FEATURE_BFCACHE</code>. </li></ul></div></li><li className="li substep substepexpand"><span className="ph cmd">Inside this subkey, create a <span className="ph uicontrol">DWORD</span> value called <code className="ph codeph">iexplore.exe</code> with the value of 0.</span><div className="itemgroup info"><img className="image" width={600} src={useBaseUrl("/ee371910-6ef3-11ed-a602-0242cfbc79b5/registry-editor.png")} /></div></li></ol></li></ol> 

### <a id="task-6538" class="anchor_top_offset"/>Internet Explorer Configurations on Windows 11

<section xmlns="http://www.w3.org/1999/xhtml" className="section context">To run tests on Internet Explorer (IE),  open <span className="ph uicontrol">Control Panel</span> and go to <span className="ph uicontrol">Network     and Internet</span> &gt; <span className="ph uicontrol">Internet Options</span>, then do as follows:<p className="p"><img className="image" width={500} src={useBaseUrl("/ee1d0160-6ef3-11ed-a602-0242cfbc79b5/win11.png")} /></p></section> 
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol steps"><li className="li step"><span className="ph cmd">In the <span className="ph uicontrol">Internet Properties</span> dialog, select the       <span className="ph uicontrol">Security</span> tab.</span></li><li className="li step"><span className="ph cmd">Choose <span className="ph uicontrol">Local         intranet</span>.</span></li><li className="li step"><span className="ph cmd">Click on the <span className="ph uicontrol">Sites</span> button.</span></li><li className="li step"><span className="ph cmd">Enable <span className="ph uicontrol">Automatically detect intranet network</span>, then click <span className="ph uicontrol">OK</span>.</span></li></ol> 

### <a id="task-6207" class="anchor_top_offset"/>Replace the IE WebDriver

<section xmlns="http://www.w3.org/1999/xhtml" className="section context">To run your test with IE mode, you need to manually replace the IE WebDriver in Katalon Studio configuration folder. Do as follows:</section> 
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol steps"><li className="li step"><span className="ph cmd">Download the 32 bit Windows Internet Explorer Driver Server from Selenium: <a className="xref j-external-link" href="https://www.selenium.dev/downloads/" target="_blank">The Internet Explorer Driver Server</a>.</span></li><li className="li step"><span className="ph cmd">Go to <code className="ph codeph">&lt;Katalon Studio folder&gt;\configuration\resources\drivers\iedriver_win64</code> to replace the <code className="ph codeph">driver.exe</code> file with the one you have downloaded.</span></li></ol> 

## <a id="task-9430" class="anchor_top_offset"/>Create the openIEModeEdgeBrowser custom keyword

<ol xmlns="http://www.w3.org/1999/xhtml" className="ol steps"><li className="li step stepexpand"><span className="ph cmd">Go to <span className="ph uicontrol">Tests Explorer</span> &gt;       <span className="ph uicontrol">Keywords</span>, and create a new keyword package.</span><div className="itemgroup info"><p className="p">Here we name the package <code className="ph codeph">com.example</code>.</p><p className="p"><img className="image" width={500} src={useBaseUrl("/ee49b6b0-6ef3-11ed-a602-0242cfbc79b5/ks-855-new-keyword-package.png")} /></p></div></li><li className="li step stepexpand"><span className="ph cmd">Right-click on the newly created package and create a new       keyword class.</span><div className="itemgroup info"><p className="p">We name the class <code className="ph codeph">openIEModeEdgeBrowser</code>.</p><p className="p"><img className="image" width={500} src={useBaseUrl("/ee49b6b0-6ef3-11ed-a602-0242cfbc79b5/ks-855-new-keyword-package.png")} /></p></div><div className="itemgroup info"><p className="p">In the <code className="ph codeph">openIEModeEdgeBrowser.groovy</code> file, copy and         paste the following script and save it.</p></div><div className="itemgroup info"></div></li></ol> 

  ```jsx
  package com.example
  import static com.kms.katalon.core.checkpoint.CheckpointFactory.findCheckpoint
  import static com.kms.katalon.core.testcase.TestCaseFactory.findTestCase
  import static com.kms.katalon.core.testdata.TestDataFactory.findTestData
  import static com.kms.katalon.core.testobject.ObjectRepository.findTestObject

  import com.kms.katalon.core.annotation.Keyword
  import com.kms.katalon.core.checkpoint.Checkpoint
  import com.kms.katalon.core.checkpoint.CheckpointFactory
  import com.kms.katalon.core.mobile.keyword.MobileBuiltInKeywords
  import com.kms.katalon.core.model.FailureHandling
  import com.kms.katalon.core.testcase.TestCase
  import com.kms.katalon.core.testcase.TestCaseFactory
  import com.kms.katalon.core.testdata.TestData
  import com.kms.katalon.core.testdata.TestDataFactory
  import com.kms.katalon.core.testobject.ObjectRepository
  import com.kms.katalon.core.testobject.TestObject
  import com.kms.katalon.core.webservice.keyword.WSBuiltInKeywords
  import com.kms.katalon.core.webui.keyword.WebUiBuiltInKeywords

  import internal.GlobalVariable

  import org.openqa.selenium.WebElement
  import org.openqa.selenium.ie.InternetExplorerDriver
  import org.openqa.selenium.ie.InternetExplorerOptions
  import org.openqa.selenium.WebDriver
  import org.openqa.selenium.By

  import com.kms.katalon.core.mobile.keyword.internal.MobileDriverFactory
  import com.kms.katalon.core.webui.driver.DriverFactory

  import com.kms.katalon.core.testobject.RequestObject
  import com.kms.katalon.core.testobject.ResponseObject
  import com.kms.katalon.core.testobject.ConditionType
  import com.kms.katalon.core.testobject.TestObjectProperty

  import com.kms.katalon.core.mobile.helper.MobileElementCommonHelper
  import com.kms.katalon.core.util.KeywordUtil

  import com.kms.katalon.core.webui.exception.WebElementNotFoundException


  class openIEModeEdgeBrowser {
      /**
      * Open browser
      */
      @Keyword
      def openBrowser(String url) {
          System.setProperty("webdriver.ie.driver", DriverFactory.getIEDriverPath());
          InternetExplorerOptions edgeIe11Options = new InternetExplorerOptions();
          Map<String, Object> ops = (Map<String, Object>) edgeIe11Options.getCapability("se:ieOptions");
          ops.put("ie.edgechromium", true);
          ops.put("ie.edgepath", "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe");
          edgeIe11Options.setCapability("ignoreProtectedModeSettings", true);
          edgeIe11Options.setCapability("ignoreZoomSetting", true);
          WebDriver driver = new InternetExplorerDriver(edgeIe11Options);
          driver.get(url)
          DriverFactory.changeWebDriver(driver)
      }
  }
  ```

## <a id="task-3136" class="anchor_top_offset"/>Use the custom keyword to execute test cases in IE mode

<ol xmlns="http://www.w3.org/1999/xhtml" className="ol steps"><li className="li step stepexpand"><span className="ph cmd">In Katalon Studio, create a test case.</span></li><li className="li step stepexpand"><span className="ph cmd">Modify the test case. Open the test case and use the custom keyword as the first test step to open Microsoft Edge in IE mode.</span><div className="itemgroup info">For example, we use the custom keyword at the beginning of the test case. <p className="p">In <span className="ph uicontrol">Manual</span> view:</p><p className="p"><img className="image" width={700} src={useBaseUrl("/ee4ceb00-6ef3-11ed-a602-0242cfbc79b5/ks-open-browser.png")} /></p></div><div className="itemgroup info"><p className="p">In <span className="ph uicontrol">Script</span> view:</p></div><div className="itemgroup info"><pre className="pre codeblock"><code>// Use the custom keyword and URL defined as global variable to open the site in Edge, with IE mode{"\n"}CustomKeywords.'com.example.openIEModeEdgeBrowser.openBrowser'(GlobalVariable.G_SiteURL){"\n"}</code></pre><p className="p"><img className="image" width={700} src={useBaseUrl("/ee2565d0-6ef3-11ed-a602-0242cfbc79b5/ks-custom-keyword-script-mode.png")} /></p></div></li><li className="li step stepexpand"><span className="ph cmd">Save your test case, then select the <span className="ph uicontrol">IE</span> option to run the test.</span><div className="itemgroup info"><img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/run-test-in-edge-with-IE-mode/KS-Run-dropdown-IE.png")} alt="Run dropdown" /><br /><br /></div></li></ol> 
<section xmlns="http://www.w3.org/1999/xhtml" className="section result"><p className="p">Katalon Studio opens a Microsoft Edge browser session in IE mode.</p><p className="p"><img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/run-test-in-edge-with-IE-mode/AUT-opened-in-IE-mode.png")} width={600} alt="Microsoft Edge browser session opened" /><br /><br /></p><p className="p">After the execution, open the <span className="ph uicontrol">Log Viewer</span>. You can see a note that says Katalon Studio successfully opened the browser in IE mode and the test case passed.</p><p className="p"><img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/tutorials/run-test-in-edge-with-IE-mode/KS-Log-View-results.png")} width={850} alt="Use keyword in test case" /><br /><br /></p></section> 
