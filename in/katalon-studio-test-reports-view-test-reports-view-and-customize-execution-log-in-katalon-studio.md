---
hide_title: true
title: View and customize execution log in Katalon Studio
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# View and customize execution log in Katalon Studio 

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Viewing the execution log is the very first approach when   troubleshooting automation test execution. The critical information   in the log can quickly help project teams pinpoint the root causes   of any issues. Katalon Studio execution logs are optimized to   provide such information so that you can have a comprehensive view   of the tests run.</p> 

## View Execution Log

After executing a test case or test suite, you can review the results in the Log Viewer tab.

The **Log Viewer** provides detailed, real-time logs of each test step, including status, duration, browser and platform info, and any errors encountered during execution.

<img src= "https://tw-cdn.katalon.com/katalon-studio/Test+report/View+test+reports/KS_10.3.0_view_execution_log.png" alt="View KS 10.3.0 execution log" width="600" />

Features include:

- Pass/Fail icons: Each test step is marked with a green check (✅) for passed steps and a red cross (❌) for failed steps, making it easy to identify issues at a glance.
- Step Details: Click on any test step to view its detailed execution logs, including error messages (if applicable).
- Execution Metadata: The Log Viewer displays useful context such as:
    - Browser type and version
    - Platform (e.g., Windows, macOS)
    - Selenium version
    - Session ID
- Expand/Collapse Steps: Use the arrow icons on the left to expand or collapse individual test steps for a more focused view.

### Tabular view vs. Tree View

The Log Viewer can be viewed in different modes: **Tabular view** and **Tree view**. You can switch to **Tree View** by selecting the toggle as illustrated below:

<img src= "https://tw-cdn.katalon.com/katalon-studio/Test+report/View+test+reports/KS_10.3.0_Log_viewer_switch_view.png" alt="Switch Log Viewer to Tabular or Tree view" width="600" />

The **Tree View** display logs in a structural way that relates to how the test case/test suite is organized. Additionally, you can navigate to the respective step by selecting from the context menu, as shown below:

<img src= "https://tw-cdn.katalon.com/katalon-studio/Test+report/View+test+reports/KS_10.3.0_Log_viewer_in_tree_view.png" alt="View Log Viewer in Tree view" width="600" />

<p xmlns="http://www.w3.org/1999/xhtml" className="p">The <strong className="ph b">Log Viewer</strong> can be viewed in different modes: <strong className="ph b">tabular</strong> view and <strong className="ph b">tree</strong> view. You can switch to tree view by selecting the <strong className="ph b">Tree View</strong> toggle as illustrated below:</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" src={useBaseUrl("/5a3af540-5627-11ed-a602-0242cfbc79b5/ks-tree-view.png")} /></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">The <strong className="ph b">Tree View</strong> display logs in a structural way that relates to how the test case/test suite is organized. Additionally, you can navigate to the respective step by selecting from the context menu, as shown below:</p> 
<img src="https://tw-cdn.katalon.com/katalon-studio/test-objects/api-test-objects/log-viewer.png" alt="Log Viewer in KS" width="1080"/>

### Scroll Lock

<p xmlns="http://www.w3.org/1999/xhtml" className="p">While the test is being executed, the <strong className="ph b">Log Viewer</strong> is being updated with real-time log messages, where the most recent log messages is shown at the bottom. Therefore, the <strong className="ph b">Log Viewer</strong> keeps scrolling down during the test execution. However, users may want to keep the <strong className="ph b">Log Viewer</strong> standing still so that they can verify particular log messages. To stop this scrolling behavior, you can select <strong className="ph b">Scroll Lock</strong>.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" src={useBaseUrl("/5a313140-5627-11ed-a602-0242cfbc79b5/ks-852-scroll-lock.png")} /></p> 
    

## Customize Console Log

### Execution Progress Debugger

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Katalon Studio execution log displays complete details of actions performed during the test run to help you debug better. The test log contains all relevant information about the test run. Full test step statements and desired capabilities information are also included. Log levels are ANSI color-coded for different kinds of levels: INFO, DEBUG, WARING, and ERROR for an easier view of the execution log, as shown in the screenshot below.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" width={700} src={useBaseUrl("/5a296910-5627-11ed-a602-0242cfbc79b5/ks-console-log.png")} /></p> 

### Extensive logs for Web Service testing

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Sending and receiving Web Service can be a troublesome task due to many factors involved on both the client and server sides. The <code className="ph codeph">HAR</code> file contains low-level data to help you identify critical performance problems with Web services quickly.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Katalon Studio includes the <code className="ph codeph">HAR</code> file in the Web Service execution log. Upon sending requests, you can access the <code className="ph codeph">.har</code> files from the <span className="ph uicontrol">Console</span> tab. The file is stored directly on the current executed machine.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" width={700} src={useBaseUrl("/5a2d60b0-5627-11ed-a602-0242cfbc79b5/ks-har-file.png")} /></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">If you execute Web Service test suites, you can right-click at the desired Report folder and choose <span className="ph uicontrol">Open Containing Folder</span>. The <code className="ph codeph">.har</code> files are stored in the main folder of the generated reports folder. For example, the file path can be <code className="ph codeph">20230608_112253/requests/main/0.har</code>.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" width={500} src={useBaseUrl("/9cd23000-0de0-11ee-bd0e-0242c7a41fd4/ks-har-files-path.png")} /></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Using the <code className="ph codeph">.har</code> file in services analyzer such as <a className="xref j-external-link" href="https://toolbox.googleapps.com/apps/har_analyzer/" target="_blank">HAR Analyzer</a> of Google Admin Toolbox can provide quality insights about the Web Service request and response. This helps the project team quickly identify key issues and efficiently allocate resources to address the issue. Some issues that can be identified include:</p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">Performance issues: slow page load, a timeout when performing a specific task</li><li className="li">Page rendering issues: incorrect page format or missing information</li></ul> 

### Logs Configuration

<p xmlns="http://www.w3.org/1999/xhtml" className="p">The deepest level of logs is called TRACE. Use the TRACE level when you need more log details than DEBUG level, which is used by default. You can also lessen the logs' details by using the INFO level.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">In case you want to change the log’s level of one or multiple packages, this setting is located and stored in <span className="ph uicontrol">Include</span> &gt; <span className="ph uicontrol">Config</span> &gt; <code className="ph codeph">log.properties</code> file.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" width={700} src={useBaseUrl("/5a162f30-5627-11ed-a602-0242cfbc79b5/ks-log-properties.png")} /></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">By uncommenting the <code className="ph codeph">logging.level.com.kms=TRACE</code> line, the differences are noticeable:</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><strong className="ph b">Before</strong></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" width={700} src={useBaseUrl("/5a259880-5627-11ed-a602-0242cfbc79b5/ks-debug.png")} /></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><strong className="ph b">After</strong></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" width={700} src={useBaseUrl("/5a221610-5627-11ed-a602-0242cfbc79b5/ks-trace.png")} /></p> 

### Log executed test steps

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Go to <span className="ph uicontrol">Project Settings</span> &gt; <span className="ph uicontrol">Executions</span> and find the option for <span className="ph uicontrol">Log executed test steps</span>. By enabling or   disabling this option, you can decide whether the logs include   executed test steps.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" width={700} src={useBaseUrl("/5a1a26d0-5627-11ed-a602-0242cfbc79b5/ks-log-executed-test-steps.png")} /></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><strong className="ph b">Enabled</strong> </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" width={700} src={useBaseUrl("/5a341770-5627-11ed-a602-0242cfbc79b5/ks-step-enabled.png")} /></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><strong className="ph b">Disabled</strong> </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" width={700} src={useBaseUrl("/5a3e0280-5627-11ed-a602-0242cfbc79b5/ks-disabled.png")} /></p> 

### Summary

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">Katalon Studio execution logs are enhanced for a better debugging process and observation of execution progress.</li><li className="li">The logs level can be configured directly from the <code className="ph codeph">log.properties</code> file.</li><li className="li">A <code className="ph codeph">.har</code> file is generated and stored in Web Service request logs. It can be used to analyze and troubleshoot performance or connection issues (if any).</li><li className="li">Logs can be set to include or exclude the executed test steps.</li></ul> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Learn more about working with the execution log and more in our Katalon Academy course: <a className="xref j-external-link" href="https://academy.katalon.com/courses/software-test-reporting/?utm_source=kat_docs&utm_medium=execution%20_log" target="_blank">Katalon Studio: How To Work With Execution Logs and Test Reports</a>.</p> 
