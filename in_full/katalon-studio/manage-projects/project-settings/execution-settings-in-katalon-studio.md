---
hide_title: true
title: Execution settings in Katalon Studio
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# Execution settings in Katalon Studio

Execution settings help define the desired behaviors that apply to the project during and after test execution.

To access default Execution Settings, from the main menu, select **Project > Settings > Execution**.

<img className="image" src={useBaseUrl("/cb68a610-9d7d-11ee-b8c3-0242c7a41fd4/ks-900-execution-settings.png")} />


- **Default execution**: The default environment that Katalon Studio uses for executing test scripts.
- **Log executed test steps**: When enabled, the logs will include executed test steps. See [View and customize execution log in Katalon Studio](/katalon-studio/test-reports/view-test-reports/view-and-customize-execution-log-in-katalon-studio).
- **Default wait for element timeout (in seconds)**: The default timeout period that Katalon Studio waits for the application under test to be loaded when executing the automation test.
- **Hide hostname in test reports and log viewer**: Hide the username and host address of the machine in test reports and log viewer.
- **Take screenshot when execution failed**: When enabled, Katalon Studio will capture screenshot of the failed test suite. To learn how to access these screenshots, see [View captured screenshots in Katalon Studio reports](/katalon-studio/test-reports/view-test-reports/view-captured-screenshots-in-katalon-studio-reports).
- **Record Video during execution**: When enabled, you can choose to record your test execution with [Browser-based Recorder](/katalon-studio/test-reports/generate-test-reports/generate-browser-based-videos-in-katalon-studio-reports) or [Screen-based Recorder](/katalon-studio/test-reports/generate-test-reports/generate-screen-based-videos-in-katalon-studio-reports).
- **Post-Execution Options**
  - **Open report**: Specify whether the report generated after your test suite's execution finishes is to be opened immediately.
  - **Terminate drivers**: Specify when any driver remains after execution is terminated.


<p xmlns="http://www.w3.org/1999/xhtml" className="p">Execution settings help define the desired behaviors that apply to the project during and after test execution.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">To access default <span className="ph uicontrol">Execution Settings</span>, from the main menu, select <span className="ph menucascade"><span className="ph uicontrol">Project</span><abbr title="and then"> &gt; </abbr><span className="ph uicontrol">Settings</span><abbr title="and then"> &gt; </abbr><span className="ph uicontrol">Execution</span></span>.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" width={600} src={useBaseUrl("/cb68a610-9d7d-11ee-b8c3-0242c7a41fd4/ks-900-execution-settings.png")} /></p> 
<dl xmlns="http://www.w3.org/1999/xhtml" className="dl"><dt className="dt dlterm"><span className="ph uicontrol">Default execution</span></dt><dd className="dd">The default environment that Katalon Studio uses for executing test scripts.</dd><dt className="dt dlterm"><span className="ph uicontrol">Log executed test steps</span></dt><dd className="dd">When enabled, the logs will include executed test steps. <a className="xref" href="/katalon-studio/test-reports/view-test-reports/view-and-customize-execution-log-in-katalon-studio#id_8">Learn more</a>.</dd><dt className="dt dlterm"><span className="ph uicontrol">Default wait for element timeout (in seconds)</span></dt><dd className="dd">The default timeout period that Katalon Studio waits for the application under test to be loaded when executing the automation test.</dd><dt className="dt dlterm"><span className="ph uicontrol">Hide hostname in test reports and log viewer</span></dt><dd className="dd">Hide the username and host address of the machine in test reports and log viewer.</dd><dt className="dt dlterm"><span className="ph uicontrol">Take screenshot when execution failed</span></dt><dd className="dd">When enabled, Katalon Studio will capture screenshot of the failed test suite. To learn how to access these screenshots, see <a className="xref" href="/katalon-studio/test-reports/view-test-reports/view-captured-screenshots-in-katalon-studio-reports">View captured screenshots in Katalon Studio reports</a>.</dd><dt className="dt dlterm"><span className="ph uicontrol">Record Video during execution</span></dt><dd className="dd">When enabled, you can choose to record your test execution with <a className="xref" href="/katalon-studio/test-reports/generate-test-reports/generate-browser-based-videos-in-katalon-studio-reports">Browser-based Recorder</a> or <a className="xref" href="/katalon-studio/test-reports/generate-test-reports/generate-screen-based-videos-in-katalon-studio-reports">Screen-based Recorder</a>.</dd><dt className="dt dlterm"><span className="ph uicontrol">Post-Execution Options</span></dt><dd className="dd"><ul className="ul"><li className="li"><span className="ph uicontrol">Open report</span>: Specify whether the report generated after your test suite's execution finishes is to be opened immediately.</li><li className="li"><span className="ph uicontrol">Terminate drivers</span>: Specify when any driver remains after execution is terminated.</li></ul></dd></dl> 

## <a id="concept-5782" class="anchor_top_offset"/>Edit JVM parameters

<div xmlns="http://www.w3.org/1999/xhtml" className="p"><div className="note important note_important"><span className="note__title">Important:</span> <ul className="ul"><li className="li">An active <span className="ph">Katalon Studio Enterprise</span> license.</li></ul></div></div>
<p xmlns="http://www.w3.org/1999/xhtml" className="p">You can edit VM arguments in the execution settings by going to <span className="ph uicontrol">Project</span> &gt; <span className="ph uicontrol">Settings</span> &gt; <span className="ph uicontrol">Execution</span> &gt; <span className="ph uicontrol">Launch Arguments</span>.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">In the <span className="ph uicontrol">VM Arguments</span> tab, enter your arguments. VM Arguments entered in the executions settings of a project change the behavior of a Java process of each execution. For example:</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" width={600} src={useBaseUrl("/caebade0-9d7d-11ee-b8c3-0242c7a41fd4/ks-910-launch-arguments.png")} /></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">To make sure if the configuration works, add this simple test case:</p> 
<div xmlns="http://www.w3.org/1999/xhtml" className="p"><pre className="pre codeblock"><code>import com.kms.katalon.core.util.KeywordUtil{"\n"}KeywordUtil.logInfo(System.getProperty("testme")) </code></pre><img className="image" width={700} src={useBaseUrl("/9eeea870-7f77-11ed-998d-0242cfbc79b5/ks-855-vm-example-tc.png")} /></div>
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Currently, <span className="ph">Katalon Studio</span> does not support VM arguments values containing space. Below is a list of the most used JVM Parameters:</p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><div className="p">Specify minimal and maximal heap sizes:<ul className="ul"><li className="li"><code className="ph codeph">-Xms&lt;heap size&gt;[unit]</code></li><li className="li"><code className="ph codeph">-Xmx&lt;heap size&gt;[unit]</code></li><li className="li"><code className="ph codeph">-XX:MaxMetaspaceSize=&lt;metaspace size&gt;[unit]</code></li></ul></div></li><li className="li"><div className="p">Configure the JVM stack size, for example <code className="ph codeph">-Xss16M</code> sets the stack size equal to 16 MB. Similarly letter k or K to indicate KB, m or M to indicate MB, and g or G to indicate GB:<ul className="ul"><li className="li"><p className="p">Configure the stack size to be 16MB: <code className="ph codeph">-Xss16M</code></p></li><li className="li"><p className="p">Configure the stack size to be 1024KB: <code className="ph codeph">-Xss1024K</code></p></li></ul></div></li><li className="li"><div className="p">Garbage collection implementation types: <ul className="ul"><li className="li">Serial Garbage Collector:&nbsp;<code className="ph codeph">-XX:+UseSerialGC</code></li><li className="li">Parallel Garbage Collector:&nbsp;<code className="ph codeph">-XX:+UseParallelGC</code></li><li className="li">CMS Garbage Collector:&nbsp;<code className="ph codeph">-XX:+USeParNewGC</code></li><li className="li">G1 Garbage Collector:&nbsp;<code className="ph codeph">-XX:+UseG1GC</code></li></ul></div></li><li className="li"><div className="p">Garbage collection logging: <ul className="ul"><li className="li">Specify the log file rolling policy:&nbsp;<code className="ph codeph">-XX:+UseGCLogFileRotation</code></li><li className="li">Denote the max number of log files that can be written for a single application life cycle:&nbsp;<code className="ph codeph">-XX:NumberOfGCLogFiles=&lt; number of log files &gt;</code></li><li className="li">Specify the max size of the file:&nbsp;<code className="ph codeph">-XX:GCLogFileSize=&lt; file size &gt;[ unit ]</code></li><li className="li">Denote the file's location:&nbsp;<code className="ph codeph">-Xloggc:/path/to/gc.log</code></li></ul></div></li><li className="li"><div className="p">Handling out of memory:<ul className="ul"><li className="li">Dump heap into physical file in case of OutOfMemoryError:&nbsp;<code className="ph codeph">-XX:+HeapDumpOnOutOfMemoryError</code></li><li className="li">Denote the path where the file is to be written:&nbsp;<code className="ph codeph">-XX:HeapDumpPath=./java_pid&lt;pid&gt;.hprof</code></li><li className="li">Issue emergency commands to be executed in case of out of memory error:&nbsp;<code className="ph codeph">-XX:OnOutOfMemoryError="&lt; cmd args &gt;;&lt; cmd args &gt;"</code></li><li className="li">Limits the proportion of the VM's time that is spent in GC before an OutOfMemory error is thrown:&nbsp;<code className="ph codeph">-XX:+UseGCOverheadLimit</code></li></ul></div></li></ul> 

## WebUI settings

You can configure default behaviors and timeouts for Web UI test execution, such as page load timeouts and action delays, by navigating to **Project > Settings > Execution > Web UI**. 

These settings decide Katalon Studio behaviors when executing WebUI test in your test project:

![WebUI Project settings](https://tw-cdn.katalon.com/katalon-studio/manage-projects/project-settings/KS_WebUI_Project_settings.png)

- **Default Smart Wait**: Tells the web driver to wait for the web page to become static before any operations are performed. See [Smart Wait function](/katalon-studio/record-and-spy/webui-record-and-spy-utilities/smart-wait-function).
- **Default Smart Locator**: Available from Katalon Studio version 9.4.0, this installs Smart Locator extension when executing, and uses Smart Locator in Self-healing. Disabling this option might cause error to test cases that contains smart locators.
- **Default wait when IE hangs**: Specifies Katalon Studio default waiting time when IE hangs.
- **Default page load timeout**
  - **Wait until the page is loaded**: This enables Katalon Studio to wait for the web page to load completely, which can help with timeout error.
  - **Wait for (in seconds)**: This enables Katalon Studio to wait for the web page to load completely within the specified default timeout period (in seconds).
- **Delay between actions**: This enables Katalon Studio to wait between test steps when executing test cases in seconds and in milliseconds.
- **Enable smart web inspectors**: Starting Katalon Studio 10.2.0 and later, this allows you to test web apps built on advanced web technologies like Flutter apps, Canvas elements, and closed Shadow DOM. Enable this only if your web AUT uses any of these technologies. 

  :::tip
  If your web AUT does not use any of these AUTs, do not turn this on. For recording test cases on these types of WebUI AUT, use [Web Recorder Plus](/katalon-studio/record-and-spy/webui-record-and-spy-utilities/katalon-web-recorder-plus).
  :::

## Web Service settings

:::tips requirements
An active Katalon Studio Enterprise license.
:::

<p xmlns="http://www.w3.org/1999/xhtml" className="p">You can set default settings for Web Service test execution by going to <span className="ph uicontrol">Project</span> &gt; <span className="ph uicontrol">Settings</span> &gt; <span className="ph uicontrol">Execution</span> &gt; <span className="ph uicontrol">Web Service</span>. The following global configurations are applied to both RESTful and SOAP requests in a project.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" width={600} src={useBaseUrl("/cbd96940-9d7d-11ee-b8c3-0242c7a41fd4/ks-910-WS-execution-settings.png")} /></p> 
<div xmlns="http://www.w3.org/1999/xhtml" className="p">
  <ul className="ul"><li className="li">
      <p className="p"><span className="ph uicontrol">Connection Timeout in milliseconds (0=unlimited)</span>: The time to establish the connection with the remote server. When it is set to 0 or left empty, Katalon waits for a response forever.</p>
    </li><li className="li">
      <p className="p"><span className="ph uicontrol">Socket Timeout in milliseconds (0=unlimited)</span>: The time waiting for data – after establishing the connection.</p>
    </li><li className="li">
      <p className="p"><span className="ph uicontrol">Max Response size in bytes</span>: The maximum number of bytes <span className="ph">Katalon Studio</span> renders from a response. When it is set to 0 or left empty, <span className="ph">Katalon Studio</span> downloads a response regardless of its size. Please note that downloading a large response may affect the application's performance.</p>
    </li></ul>
</div>
<p xmlns="http://www.w3.org/1999/xhtml" className="p">For your convenience, we provide a shortcut to these global settings in a test request view.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" width={600} src={useBaseUrl("/8f9bd130-22b2-11ed-9930-0242fe3e4a3f/timeout-maxsize.png")} alt="A test request view" /></p> 

### Web Service settings in script view

<p xmlns="http://www.w3.org/1999/xhtml" className="p">You can set request timeout and maximum response size via a script using the built-in functions of <span className="ph">Katalon Studio</span>.</p> 
<div xmlns="http://www.w3.org/1999/xhtml" className="sectiondiv"><strong className="ph b">Request timeout</strong><div className="p"><ul className="ul"><li className="li">Override timeout settings of a project in a test case<div className="p"><pre className="pre codeblock"><code>Map&lt;String, Object&gt; generalSettings = RunConfiguration.getExecutionGeneralProperties(){"\n"}generalSettings.put(RunConfiguration.REQUEST_CONNECTION_TIMEOUT, 3500){"\n"}generalSettings.put(RunConfiguration.REQUEST_SOCKET_TIMEOUT, 3500)</code></pre></div></li><li className="li">Change timeout settings of a specific test request <div className="p"><pre className="pre codeblock"><code>RequestObject request = findTestObject("Object Repository/Localhost") request.setConnectionTimeout(3500) request.setSocketTimeout(3500){"\n"} {"\n"}// Or to unset the timeout request.setConnectionTimeout(RequestObject.TIMEOUT_UNSET) request.setSocketTimeout(RequestObject.TIMEOUT_UNSET) {"\n"}{"\n"}// Or to set the timeout to unlimited request.setConnectionTimeout(RequestObject.TIMEOUT_UNLIMITED) request.setSocketTimeout(RequestObject.TIMEOUT_UNLIMITED) {"\n"}// Or if you just want to set to its default value (The default value is set to unlimited) request.setConnectionTimeout(RequestObject.DEFAULT_TIMEOUT) request.setSocketTimeout(RequestObject.DEFAULT_TIMEOUT)</code></pre></div></li></ul></div></div>
<div xmlns="http://www.w3.org/1999/xhtml" className="sectiondiv"><strong className="ph b">Maximum response time</strong><div className="note note note_note"><span className="note__title">Note:</span> <ul className="ul"><li className="li"><p className="p"><span className="ph">Katalon Studio</span> also supports setting the maximum response size of execution using <code className="ph codeph">-maxResponseSize</code> in the command line. <a className="xref" href="/katalon-studio/execute-tests/katalon-runtime-engine/command-line-syntax-in-katalon-runtime-engine#concept-1437">Learn more</a>.</p></li></ul></div><div className="p"><ul className="ul"><li className="li"><p className="p">Override response size limit of a project in a test case</p>
        <div className="p"><pre className="pre codeblock"><code>Map&lt;String, Object&gt; generalSettings = RunConfiguration.getExecutionGeneralProperties(){"\n"}generalSettings.put(RunConfiguration.REQUEST_MAX_RESPONSE_SIZE, 400)</code></pre></div></li><li className="li"><p className="p">Change maximum response size setting of a specific test request</p>
        <div className="p"><pre className="pre codeblock"><code>RequestObject request = findTestObject("Object Repository/Basic Auth"){"\n"}request.setMaxResponseSize(400) {"\n"}{"\n"}// Or to unset response size limit. And so, the project's max response size setting will be used.{"\n"}request.setMaxResponseSize(RequestObject.MAX_RESPONSE_SIZE_UNSET) {"\n"}{"\n"}// Or to set response size limit to unlimited{"\n"}request.setMaxResponseSize(RequestObject.MAX_RESPONSE_SIZE_UNLIMITED) {"\n"}{"\n"}// Or if you just want to set to its default value (The default value is set to unlimited){"\n"}request.setMaxResponseSize(RequestObject.DEFAULT_MAX_RESPONSE_SIZE)</code></pre></div></li></ul></div></div>
