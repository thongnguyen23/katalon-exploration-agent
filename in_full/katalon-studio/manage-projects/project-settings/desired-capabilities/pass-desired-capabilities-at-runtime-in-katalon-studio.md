---
hide_title: true
title: Pass desired capabilities at runtime in Katalon Studio
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="id" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Pass desired capabilities at runtime in <span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon Studio</span> 

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Desired capabilities configured in project settings are applied   at the project level. You can also use desired capabilities at the   test case level by passing desired capabilities to the test   script.</p> 
    

## <a id="id_1" class="anchor_top_offset"/>Pass desired capabilities at runtime for WebUI Testing

    
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">To apply desired capabilities at runtime, place the following   sample code before the test script. This also overrides the desired   capabilities predefined in project settings.</p> 
              
<pre xmlns="http://www.w3.org/1999/xhtml" className="pre codeblock"><code>import com.kms.katalon.core.configuration.RunConfiguration{"\n"}RunConfiguration.setWebDriverPreferencesProperty(&lt;key&gt;, &lt;value&gt;){"\n"}</code></pre> 
          
          

### <a id="id_2" class="anchor_top_offset"/>Open Firefox browser in private mode

<p xmlns="http://www.w3.org/1999/xhtml" className="p">The following example demonstrates how to configure the desired capabilities at runtime to open a test case in private mode in Firefox.</p> 
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol"><li className="li">     <p className="p">Open the test case in script mode.</p>   </li><li className="li">     <p className="p">Pass the <code className="ph codeph">-private</code> argument to the sample code as follows. Then place the code before the test script.</p>     <pre className="pre codeblock"><code>import com.kms.katalon.core.configuration.RunConfiguration{"\n"}Map firefoxOptions =[args:"-private"]{"\n"}RunConfiguration.setWebDriverPreferencesProperty('moz:firefoxOptions', firefoxOptions){"\n"}</code></pre>   </li><li className="li">     <p className="p">Continue writing the script or use Web Spy/Record Utility to complete your test case.</p>     <p className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/desired-capabilities-override-in-run-time/KS-DC-firefox-private-mode-runtime.png")} alt="DC at test script" /><br /><br />     </p>   </li><li className="li">     <p className="p">Run the test with Firefox.</p>     <p className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/desired-capabilities-override-in-run-time/KS-DC-run-with-firefox.png")} alt="Run Firefox" /><br /><br />     </p>     <div className="note note note_note"><span className="note__title">Note:</span>        <ul className="ul"><li className="li">           <p className="p">Make sure to update the browser by clicking <strong className="ph b">Tools</strong> &gt; <strong className="ph b">Update WebDrivers &gt; Choose browser</strong>.</p>         </li></ul>     </div>     <p className="p">The test successfully opens a Firefox browser in private mode.</p>     <p className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/desired-capabilities-override-in-run-time/KS-DC-Open-firefox-private.png")} alt="Open Firefox in private mode" /><br /><br />     </p>   </li></ol> 

### <a id="id_3" class="anchor_top_offset"/>Override desired capabilities in project settings

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Suppose you want to override desired capabilities pre-configured in project settings; you can use the above sample code in the test script.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">In the following example, we defined the desired capabilities for Chrome window-sized 1200x600 in project settings. We want to override this setting to run a test with a Chrome window in private mode sized 100x100. Do as follows:</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/project-settings-new-ui/KS-DC-runtime-windows-sized-1200x600.png")} alt="Set DC in project settings" /><br /><br /> </p> 
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol"><li className="li">     <p className="p">To override the desired capabilities at runtime, open the test case in script mode. Pass the desired capabilities to the same key with the capabilities defined in project settings. Then place the code before the test script.</p>     <p className="p">Here, we want to override the <code className="ph codeph">--window-size=1200,600</code> capabilities. We pass the <code className="ph codeph">--window-size=100,100</code> and <code className="ph codeph">--incognito</code> capabilities to the <code className="ph codeph">args</code> key in the sample code as follows. Then place the code before the test script.</p>     <div className="p">       <pre className="pre codeblock"><code>import com.kms.katalon.core.configuration.RunConfiguration{"\n"}RunConfiguration.setWebDriverPreferencesProperty("args", ["--window-size=100,100","--incognito"])</code></pre>     </div>   </li><li className="li">     <p className="p">Continue writing the script or use Web Spy/Record Utility to complete your test case.</p>     <p className="p"> <img className="image" src={useBaseUrl("https://github.com/Yen8298/docs-images/raw/master/katalon-studio/docs/desired-capabilities-override-in-run-time/KS-DC-window-sized-100x100-incognito-runtime.png")} alt="DC at test script" /><br /><br />     </p>   </li><li className="li">     <p className="p">Run the test with Chrome.</p>     <p className="p"> <img className="image" src={useBaseUrl("https://github.com/Yen8298/docs-images/raw/master/katalon-studio/docs/desired-capabilities-override-in-run-time/KS-DC-Chrome-windows-100x100-incognito-run.png")} alt="Set DC in project settings" /><br /><br />     </p>     <p className="p">The test successfully opens a Chrome window-size 100x100 in private mode (overriding Chrome window-size 1200x600).</p>   </li></ol> 

### <a id="concept-4049" class="anchor_top_offset"/>Pass desired capabilities at runtime for remote execution

<p xmlns="http://www.w3.org/1999/xhtml" className="p">To apply desired capabilities at runtime, place the following   sample code before the test script. This also overrides the desired   capabilities predefined in project settings.</p> 
<pre xmlns="http://www.w3.org/1999/xhtml" className="pre codeblock"><code>import com.kms.katalon.core.configuration.RunConfiguration{"\n"}RunConfiguration.setDriverPreferencesProperty('Remote',{"  "}capsName , capsValue)</code></pre> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">For example, we want to set remote execution environment as   Windows 10, enter the following sample code before the test   script:</p> 
<pre xmlns="http://www.w3.org/1999/xhtml" className="pre codeblock"><code>import com.kms.katalon.core.webui.keyword.WebUiBuiltInKeywords as WebUI{"\n"}import com.kms.katalon.core.configuration.RunConfiguration{"\n"}{"\n"}RunConfiguration.setDriverPreferencesProperty('Remote', 'os', 'Windows'){"  "}{"\n"}RunConfiguration.setDriverPreferencesProperty('Remote', 'os_version', '10'){"  "}{"\n"}{"\n"}WebUI.openBrowser('google.com')</code></pre> 
<nav xmlns="http://www.w3.org/1999/xhtml" role="navigation" className="related-links"><div className="linklist relinfo"><strong>Related information</strong><br /><br /><ul className="linklist"><li className="linklist"><a className="link j-external-link" href="https://docs.katalon.com/javadoc/com/kms/katalon/core/configuration/RunConfiguration.html" target="_blank">RunConfiguration</a></li></ul></div></nav> 
