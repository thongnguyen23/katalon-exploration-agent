---
hide_title: true
title: Test different browser locales in Chrome with Desired Capabilities in Katalon Studio
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="id" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Test different browser locales in Chrome with Desired Capabilities in <span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon Studio</span> 

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Chrome sets a default UI language with the first Chrome window   that opens. In other words, if you alter browser locales, for   example, with command line argument <code className="ph codeph">chrome.exe--lang=de</code>  to start Chrome in German, the Chrome driver still   defines the default language from the Chrome browser.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">To test different browser locales, you can instead configure   Desired Capabilities. You can learn about this here: <a className="xref" href="/katalon-studio/manage-projects/project-settings/desired-capabilities/introduction-to-desired-capabilities-in-katalon-studio">Desired     Capabilities</a> </p> 

## <a id="id_1" class="anchor_top_offset"/>Use Configured Desired Capability with Test Case Variables

In this section, we show you two possible approaches to alter browser locales while testing:

- To test one specific language with a test case.
- To test different languages with a test suite.
:::info notes
- Here is a sample project you can download as a .zip file:
    - [Sample test cases run with multiple locales](https://github.com/katalon-studio-samples/multi-locales-sample/blob/main/Test%20Cases/Run%20with%20local%20Chrome.tc).
    - [Sample test suite with data binding support](https://github.com/katalon-studio-samples/multi-locales-sample/tree/main/Test%20Suites).
:::

### <a id="concept-7430" class="anchor_top_offset"/>Create a test case to test one language

<p xmlns="http://www.w3.org/1999/xhtml" className="p">In the following example, we configure a test case with a specific browser locale, like French.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Do as follows:</p> 
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol"><li className="li">     <p className="p">Create a New Test Case. Go to <strong className="ph b">File &gt; New &gt; Test Case.</strong></p>   </li><li className="li">     <p className="p">Create Test Case Variables. See also: <a className="xref" href="/katalon-studio/data-driven-testing/test-case-variables#id_1">Test Case Variables</a>.</p>     <ul className="ul"><li className="li">Switch to the Variables tab of your Test Case.</li><li className="li">Click <strong className="ph b">Add</strong>. A new row appears in the variable list.</li><li className="li">Input the "locale" variable like so:</li></ul>     <table className="table anchor_top_offset" id="concept-7430__4fe0145a-d5f6-48f1-9998-195100745696"><caption /><tbody className="tbody"><tr className><td className="entry"><strong className="ph b">Name</strong></td><td className="entry"><strong className="ph b">Type</strong></td><td className="entry"><strong className="ph b">Default Value</strong></td></tr><tr className><td className="entry">locale</td><td className="entry">String</td><td className="entry">"fr"</td></tr></tbody></table>     <ul className="ul"><li className="li">         <p className="p">In our example, the <strong className="ph b">Default Value</strong> is <code className="ph codeph">fr</code>, the language code for French. You can find other language codes for Chrome here: <a className="xref j-external-link" href="https://developers.google.com/admin-sdk/directory/v1/languages" target="_blank">language code</a>.</p>         <p className="p"><img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/how-to-guides/tests-different-browser-locales-with-DC/Test-case-variables-2.png")} alt="test case with variables" /><br /><br /></p>       </li></ul>   </li><li className="li">     <p className="p">After defining Test Case Variables, we override default language settings in Chrome by using Configured Desired Capabilities. You can learn more about this here: <a className="xref" href="/katalon-studio/manage-projects/project-settings/desired-capabilities/introduction-to-desired-capabilities-in-katalon-studio#id_2">Configured Desired Capabilities</a></p>     <ul className="ul"><li className="li">Switch to the Script tab of your Test Case.</li><li className="li">         <p className="p">Copy and paste the below code into your test script. With this code, you can manipulate the locales of the testing browsers.</p>         <pre className="pre codeblock"><code>import com.kms.katalon.core.configuration.RunConfiguration{"\n"}{"\n"}Map prefs = [('intl.accept_languages') : locale]{"\n"}// Map preferences key to manipulate page's language.{"\n"}{"\n"}RunConfiguration.setWebDriverPreferencesProperty("prefs", prefs){"\n"}</code></pre>       </li><li className="li">         <p className="p">Continue writing the script or use Web Spy/Record Utility to complete your test case.</p>         <div className="note note note_note"><span className="note__title">Note:</span>            <div className="p">             <ul className="ul"><li className="li">                 <p className="p">In case you wish to alter browser locales with an existing test script, copy and paste the above sample code before the test script.</p>               </li></ul>           </div>         </div>         <p className="p"><img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/how-to-guides/tests-different-browser-locales-with-DC/configured-desired-capabilities.png")} alt="Final results after configuring Desired Capabilities" /><br /><br /></p>       </li><li className="li">         <p className="p">Your Test Case is now ready to run with Chrome in French.</p>       </li></ul>   </li></ol> 

### <a id="id_3" class="anchor_top_offset"/>

<div xmlns="http://www.w3.org/1999/xhtml" className="note important note_important"><span className="note__title">Important:</span> <ul className="ul"><li className="li">Make sure to configure all your test cases with Desired Capabilities as per Part 1.</li></ul></div>
<div xmlns="http://www.w3.org/1999/xhtml" className="note note note_note"><span className="note__title">Note:</span> <ul className="ul"><li className="li"><p className="p">Desired Capabilities can be reused across projects. You can refer to this document: <a className="xref" href="/katalon-studio/manage-projects/project-settings/desired-capabilities/manage-desired-capabilities-in-katalon-studio">Reuse Desired Capabilities</a> for further details.</p></li></ul></div>
<p xmlns="http://www.w3.org/1999/xhtml" className="p">In the following example, we demonstrate how to create a Test Suite with Test case variables to test different browser locales. Here, we use French, English, and Spanish.</p> 
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol"><li className="li">Create a test suite. Go to <strong className="ph b">File &gt; New &gt; Test Suite.</strong> </li><li className="li"><p className="p">Click <strong className="ph b">Add</strong> in the command toolbar, then choose pre-configured test cases.</p><p className="p"><img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/d22b289b2b07c6ae15b9a52e11a3cc245e725974/katalon-studio/how-to-guides/tests-different-browser-locales-with-DC/new-test-suite.png")} alt="New Test Suite" /><br /><br /></p></li><li className="li"><p className="p">Create a data file. Go to <strong className="ph b">File &gt; New &gt; Test Data.</strong> Choose <strong className="ph b">Data Type</strong> as <strong className="ph b">Internal Data.</strong> </p><p className="p">You use this data file to input different language codes you want to test on browsers. For our example, we input <code className="ph codeph">fr</code>,<code className="ph codeph">en</code>,<code className="ph codeph">es</code>.</p><p className="p"><img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/how-to-guides/tests-different-browser-locales-with-DC/create-new-data-file-2.png")} alt="New Data file 2" /><br /><br /></p><p className="p"><img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/how-to-guides/tests-different-browser-locales-with-DC/New%20Data%20File.png")} alt="New Data file" /><br /><br /></p></li><li className="li"><p className="p">Manage Data Binding</p><ul className="ul"><li className="li"><p className="p">Return to your test suite, click <strong className="ph b">Show Data Binding</strong> to expand the <strong className="ph b">Data Binding</strong> section. Make sure you click on the correct pre-configured test case beforehand.</p><p className="p">This step binds the New Data File from Step 3 with the Test Suite you want to run. See also <a className="xref" href="/katalon-studio/data-driven-testing/manage-data-binding">Manage Data Binding</a>.</p><p className="p"><img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/how-to-guides/tests-different-browser-locales-with-DC/show-data-variables.png")} alt="Show Data Binding section" /><br /><br /></p></li><li className="li"><p className="p">The final results should show as below:</p><p className="p"><img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/how-to-guides/tests-different-browser-locales-with-DC/Test%20Suite%20Data%20Binding.png")} alt="Test Suite data" /><br /><br /></p></li></ul></li></ol> 

## <a id="concept-8841" class="anchor_top_offset"/>Use Custom Profiles in Desired Capabilities

You can also test different browser locales with a Remote Server. In this case, you can set Custom Desired Capabilities to alter the default language in Chrome.

Here is a sample project you can download as a .zip file: [Sample test cases with custom execution](https://github.com/katalon-studio-samples/multi-locales-sample/blob/main/Test%20Cases/Run%20with%20custom%20execution.tc).

:::tip requirements
- Make sure that you are running Selenium Grid Hub & Node while executing the test.
- Make sure to update the browser by clicking **Tools > Update WebDrivers > Choose browser**.
:::
<p xmlns="http://www.w3.org/1999/xhtml" className="p">The following example shows you how to create a custom profile with Spanish as the testing language. Do as follows:</p> 

1. Create a new custom profile in **Desired Capabilities**. Go to **Project > Settings > Desired Capabilities > Custom.**
    
    <img src="https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/project-settings-new-ui/KS-LOCALE-Custom-settings.png" alt="Custom settings KS screen" />
    
2. In the command toolbar, click **Add** to add a custom profile. In the newly added property line, change the name to `spanish` for better recognition, then click on *More* (...) under the **Value** column. A **Custom Execution Configuration Builder** dialog opens.
    
    <img src="https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/project-settings-new-ui/KS-LOCALES-Name-the-property.png" alt="Enter value in Custom settings screen" />
    
3. In the **Custom Execution Configuration Builder** dialog, specify the **Driver Name** as **Remote**, then click on *More* (...) under the **Preferences** column. A **Driver Builder** dialog opens.Fill in the **Driver Builder** dialog as shown below:
    
    <img src="https://github.com/katalon-studio/docs-images/raw/5ce4d691c2e1223380169717503cd3189ae5b1ed/katalon-studio/how-to-guides/tests-different-browser-locales-with-DC/Custom-Execution%20-Configuration%20-Builder-2.jpg" alt="Custom Execution Configuration Builder screen" />
    
    - **Remote Server URL**: `http://localhost:port/wd/hub` - the URL to the Remote server.
    - **Remote Server Type**: Choose **Selenium**.
    - Click **Add** on the command toolbar, then input the following values:
        
        
        | **Table 1** |  |  |
        | --- | --- | --- |
        | Name | Type | Value |
        | browserName | string | chrome |
        | goog:chromeOptions(*) | Dictionary(**) | Click *More* (...). In the pop-up **Dictionary Property Builder** dialog, click **Add**, then input values from Table 2. |
        
        (*) `*goog:chromeOptions`: Support passing the ChromeOptions object into the ChromeDriver constructor.*
        
        (**) `*Dictionary`: the data type permits you to input a collection of keys and values. You can learn more about this here: [Data types](/katalon-studio/create-test-cases/value-types-in-katalon-studio).*
        
        | **Table 2** |  |  |
        | --- | --- | --- |
        | Name | Type | Value |
        | prefs | Dictionary | Click *More* (...). In the pop-up **Dictionary Property Builder** dialog, click **Add**, then input values from Table 3. |
        
        | **Table 3** |  |  |
        | --- | --- | --- |
        | Name | Type | Value |
        | intl.accept_languages(*) | String | es(**) |
        
        (*) `*intl.accept_languages`: Support passing preference key to manipulate a page's language.*
        
        (**) `*es`: the language code for Spanish.*
        
        <img src="https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/how-to-guides/tests-different-browser-locales-with-DC/KS-LOCALES-Custom-settings.png" alt="dictionary property builder screen" width="700" />
        :::info notes
        - The capabilities properties are case-sensitive.
        :::
4. Click **OK** to save the settings in each table. The above commands should result in the following:
    
    <img src="https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/project-settings-new-ui/KS-LOCALE-Final-results.png" alt="result screen" width="800" /> <br/>
    
    <img src="https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/how-to-guides/tests-different-browser-locales-with-DC/final-results-3.png" alt="result screen" width="800" />