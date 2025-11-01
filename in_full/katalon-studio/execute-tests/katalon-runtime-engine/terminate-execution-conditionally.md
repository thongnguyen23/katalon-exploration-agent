---
hide_title: true
title: Terminate execution conditionally
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="id" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Terminate execution conditionally

<p xmlns="http://www.w3.org/1999/xhtml" className="p">In this article, you will learn how to terminate a test execution automatically by configuring a maximum number of test failures in manual view or via the command-line option, with examples using common use cases.</p> 
<div xmlns="http://www.w3.org/1999/xhtml" className="note important note_important"><span className="note__title">Important:</span> <ul className="ul"><li className="li">A Katalon Runtime Engine License. See <a className="xref" href="#">Katalon licensing</a>.</li></ul></div>
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Consider using the condition to terminate execution when a set of tests is mature and takes hours to finish. Once a significant number of tests fail, they may fail for the same cause. This feature helps you save time, provide early feedback, and avoid the execution of unnecessary test cases.</p> 
    

## <a id="id_1" class="anchor_top_offset"/>Set a maximum number of test failures

:::info What is a test failure?
A test failure is a failed test case or test iteration in an execution.

- 1 test case fails = 1 test failure
- 1 retried test case fails = 1 test failure
- 1 test iteration (test case + data row) fails = 1 test failure
- 1 retried test iteration fails = 1 test failure
:::          

### <a id="id_2" class="anchor_top_offset"/>With Command Builder

:::info note
For detailed instruction on how to run a test execution in Console mode, see [Command Builder](/katalon-studio/execute-tests/katalon-runtime-engine/get-started-with-katalon-runtime-engine).
:::
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Go to Katalon Studio and set a maximum number of test failures.</p> 
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol"><li className="li">     <p className="p">In the toolbar, select <strong className="ph b">Build CMD</strong> (Build Command).</p>   </li><li className="li">     <p className="p">In the <strong className="ph b">Generate Command for Console Mode &gt; Execution Configurations</strong>, check the box <strong className="ph b">Terminate the execution once the total number of test failures reaches this threshold</strong>. In the text field, input your desired maximum number of test failures.</p>     <p className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/condition-to-stop/condition%20to%20stop%20-%202.png")} alt="command builder" /><br /><br />     </p>     <div className="note note note_note"><span className="note__title">Note:</span>        <p className="p">The maximum test cases failure must be greater than 0 and a natural number (1, 2, 3...). Otherwise, Katalon Studio will not start the execution.</p>     </div>   </li><li className="li">     <p className="p">After you are done with the configuration, click <strong className="ph b">Generate command</strong>. A command containing the <code className="ph codeph">-maxFailedTests</code> option is generated.</p>     <p className="p">Copy the generated command to use in Console mode.</p>     <p className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/condition-to-stop/generate%20command%201.png")} /><br /><br />     </p>     <p className="p">You can also execute the test with the property file. To save the property file in the <strong className="ph b">Execution Configurations</strong> dialog, click <strong className="ph b">Generate property file &gt; Save</strong>.</p>   </li></ol> 

### <a id="id_3" class="anchor_top_offset"/>With Command-line option

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Use the command-line option: <code className="ph codeph">-maxFailedTests=T</code>, where T is the maximum number of test failures.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/condition-to-stop/Command-line-2.png")} /><br /><br /> </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">See <a className="xref" href="/katalon-studio/execute-tests/katalon-runtime-engine/command-line-syntax-in-katalon-runtime-engine">Katalonc command-line option</a> for the list of common command-line options supported.</p> 
    

## <a id="id_4" class="anchor_top_offset"/>Report Incomplete Test Suite

    
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">When a test suite has at least 1 test case <strong className="ph b">Not     Run</strong>, the final status of that test suite is marked   <strong className="ph b">Incomplete</strong>.</p> 
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">For test suites marked <strong className="ph b">Incomplete</strong> or   <strong className="ph b">Not started yet</strong>, Katalon Studio automatically   sends attachments to TestOps after execution ends. The reports   include the execution logs and JUnit Reports.</p> 
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Test suites marked <strong className="ph b">Incomplete</strong> or <strong className="ph b">Not     started yet</strong> and the attachments of the test suite   execution cannot be uploaded to 3rd-party tools (qTest, JIRA,   Slack, Azure DevOps Test Plans, TestRail).</p> 
    
  

## <a id="id_5" class="anchor_top_offset"/>Troubleshoot

<p xmlns="http://www.w3.org/1999/xhtml" className="p">When a test suite or test suite collection is terminated, you can find the test suite or test suite collection reference ID and the maximum number of test failures in the execution log.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/condition-to-stop/Execution%20log.png")} alt="execution log" /><br /><br /> </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">This applies to either sequential or parallel mode execution. You can check which test execution was terminated and why. You can also see the report in the manual view of Katalon Studio. See also <a className="xref" href="/katalon-studio/test-reports/view-test-reports/view-and-customize-execution-log-in-katalon-studio">View and Customize Execution Log</a>.</p> 
    

## <a id="id_6" class="anchor_top_offset"/>Common Use Cases

    
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Below are three example use cases to illustrate how the   parameter works:</p> 
      
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul">   <li className="li">In the case of a test suite execution.</li>   <li className="li">In the case of a test suite collection executed in sequential     mode.</li>   <li className="li">In the case of a test suite collection executed in parallel     mode.</li> </ul> 
    
              

### <a id="id_7" class="anchor_top_offset"/>Terminate Test Suite Execution

<p xmlns="http://www.w3.org/1999/xhtml" className="p">In this section, we outline an example execution of a test suite with this parameter.</p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">     <p className="p">Given that you have a test suite that has 10 test cases.</p>     <p className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/condition-to-stop/Test%20suite%20UC%201.png")} alt="Test Suites" /><br /><br />     </p>   </li><li className="li">     <p className="p">You want to stop the test suite after 4 test failures. Set T = 4.</p>     <p className="p"> <strong className="ph b">Configure in Command Builder</strong>     </p>     <p className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/condition-to-stop/terminate.png")} alt="command builder" /><br /><br />     </p>     <p className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/condition-to-stop/command%20UC%201.png")} alt="execution log" /><br /><br />     </p>     <p className="p"> <strong className="ph b">Execute in Console Mode</strong>     </p>   </li><li className="li">     <p className="p">The test suite is terminated once the number of failures becomes 4. The execution ends, and the rest test cases do not run.</p>     <p className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/condition-to-stop/Test%20log%20result%20-%20UC%201.png")} alt="info" /><br /><br />     </p>   </li><li className="li">     <p className="p">Katalon Studio generates a report in JUnit, HTML, PDF, and CSV format. The report does not show information for test cases that were not run.</p>     <p className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/condition-to-stop/Test%20Result%20in%20KS%20-%20UC%201.png")} alt="report in Katalon Studio" /><br /><br />     </p>     <div className="note note note_note"><span className="note__title">Note:</span>        <p className="p">See also <a className="xref" href="/katalon-studio/test-reports/view-test-reports/view-test-suite-and-test-suite-collection-reports-in-katalon-studio#id_1">Test Suite and Test Suite Collection Reports</a>.</p>     </div>   </li></ul> 

### <a id="id_8" class="anchor_top_offset"/>Terminate Test Suite Collection Executed In Sequential Mode

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">     <p className="p">Given that you have 5 test suites, each test suite has 10 test cases. You want to stop the test suite collection after 20 test failures. Set T = 20.</p>   </li><li className="li">     <p className="p">The test suite collection executes in sequential mode and is terminated once the number of failures becomes 20. The rest test cases in the terminated test suite and the rest test suite do not run.</p>     <p className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/condition-to-stop/Report%20TSC%20UC2.png")} alt="report test suite collection" /><br /><br />     </p>   </li><li className="li">     <p className="p">Katalon Studio generates a report in JUnit, HTML, PDF, and CSV format. The report does not show information for test cases and test suites that were not run.</p>     <div className="note note note_note"><span className="note__title">Note:</span>        <p className="p">Learn more about how to create and execute a <a className="xref" href="/katalon-studio/manage-test-artifacts/manage-test-suite-collections-in-katalon-studio">Manage test suite collections in Katalon Studio</a>.</p>     </div>   </li></ul> 

### <a id="id_9" class="anchor_top_offset"/>Terminate Test Suite Collection Executed In Parallel Mode

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">     <p className="p">Given that you have a test suite collection that has 5 test suites with 3 parallel instances. You want to stop the test suite collection after 20 test failures. Set T = 20.</p>     <div className="note note note_note"><span className="note__title">Note:</span>        <ul className="ul"><li className="li">           <p className="p">Instances is the number of test suites you set to run at the same time.</p>         </li><li className="li">           <p className="p">T is the maximum number of test case failures (threshold).</p>         </li></ul>     </div>   </li><li className="li">     <p className="p">When the test suite begins execution, the first 3 test suites run at the same time with T = 20 in each test suite.</p>   </li><li className="li">     <p className="p">The test suite collection is terminated once the total number of failures becomes 20. The rest test cases in the terminated test suite and the rest test suite do not run. However, the currently running test suites will not be terminated.</p>     <p className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/condition-to-stop/Report%20UC%203.png")} alt="report test suite collection in parallel mode" /><br /><br />     </p>   </li><li className="li">     <p className="p">Katalon Studio generates a report in JUnit, HTML, PDF, and CSV format. The report does not show information for test cases and test suites that were not run.</p>   </li></ul> 
