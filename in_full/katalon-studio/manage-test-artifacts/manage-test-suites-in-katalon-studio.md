---
hide_title: true
title: Manage test suites in Katalon Studio
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="id" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Manage test suites in Katalon Studio

<p xmlns="http://www.w3.org/1999/xhtml" className="p">A test suite (TS) is a collection of test cases.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">A test case can be part of a different test suite. You can group test cases to a test suite in some logical way, such as grouping all tests related to regression testing or security, or all tests for a specific component or high-level feature/business case. A test suite can also be used as a dynamic way to cover requirements.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">This guide shows you how to create and manage test cases in a test suite.</p> 

## <a id="task-8314" class="anchor_top_offset"/>Create a new test suite

<section xmlns="http://www.w3.org/1999/xhtml" className="section context">To create a new test suite, do as follows:</section> 
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol steps"><li className="li step stepexpand"><span className="ph cmd">From the menu bar, select <span className="ph uicontrol">File</span> &gt; <span className="ph uicontrol">New</span> &gt; <span className="ph uicontrol">Test         Suite</span>.</span><div className="itemgroup info"><img className="image" width={600} src={useBaseUrl("/996c5450-22b2-11ed-9930-0242fe3e4a3f/KS-TDAP-837-create-new-test-suite.png")} alt="create a new test suite" /></div></li><li className="li step stepexpand"><span className="ph cmd">Fill in the <span className="ph uicontrol">Name</span> of the test suite and the       <span className="ph uicontrol">Description</span> (optional).</span><div className="itemgroup info"><img className="image" width={600} src={useBaseUrl("/9969bc40-22b2-11ed-9930-0242fe3e4a3f/KS-TDAP-837-new-test-suite-dialog.png")} alt="New test suite dialog" /></div></li><li className="li step stepexpand"><span className="ph cmd">Click <span className="ph uicontrol">OK</span> when you are done.</span><div className="itemgroup info"><p className="p">Alternatively, you can create a new test suite after creating a         test case. In a test case, click the <span className="ph uicontrol">Add to test           suite</span>.</p></div><div className="itemgroup stepxmp"><img className="image" src={useBaseUrl("/99685cb0-22b2-11ed-9930-0242fe3e4a3f/KS-TDAP-837-add-TC-to-test-suite.png")} alt="Add test case to a test suite" /></div><div className="itemgroup info"><p className="p">You can choose to add that test case to an         existing or a new test suite.</p></div></li></ol> 

## <a id="task-39" class="anchor_top_offset"/>Add test cases to a test suite

<p xmlns="http://www.w3.org/1999/xhtml" className="shortdesc">There are several ways to add test cases into test suites in <span className="ph">Katalon Studio</span>. You can drag and drop test case into test suites or use the test suite editor to manually add the test case. You can add a test case in the same test suite many times.</p> 
<section xmlns="http://www.w3.org/1999/xhtml" className="section context"><p className="p">To add test cases to a test suite, do as follows:</p></section> 
<div xmlns="http://www.w3.org/1999/xhtml" className="li step p"><span className="ph cmd">Open a test suite, then select <span className="ph uicontrol">Add
      Test Case</span> from the command toolbar.</span><div className="itemgroup stepxmp"><img className="image" width={500} src={useBaseUrl("/9965ebb0-22b2-11ed-9930-0242fe3e4a3f/KS-TDAP-837-add-test-case-to-TS.png")} alt="Add test cases to a test suite" /></div></div>
<section xmlns="http://www.w3.org/1999/xhtml" className="section result"><p className="p">All test cases in <span className="ph">Katalon Studio</span> are displayed in the     <span className="ph uicontrol">Test Case Browser</span> dialog for you to select your     preferred options. The selected test cases are added to the test     case list accordingly.</p><p className="p">By default, the checkbox at the end of the test case row is checked. It means that the test case is executed when you run a test suite. If you want to disable a test case execution, uncheck the box.</p></section> 

## <a id="task-7577" class="anchor_top_offset"/>Remove test cases from a test suite

<section xmlns="http://www.w3.org/1999/xhtml" className="section context">A test suite should have at least one test case. You can remove one or many test cases in a test suite. Follow these steps:</section> 
<div xmlns="http://www.w3.org/1999/xhtml" className="li step p"><span className="ph cmd">Click on one or more  test cases you want to remove, then click <span className="ph uicontrol">Delete</span> from the main toolbar.</span><div className="itemgroup stepxmp"><img className="image" width={500} src={useBaseUrl("/9963a1c0-22b2-11ed-9930-0242fe3e4a3f/KS-TDAP-837-Delete-TC-in-TS-main-toolbar.png")} alt="Delete test cases in a test suite from the main toolbar" /></div><div className="itemgroup info">Alternatively, you can also right-click &gt; <span className="ph uicontrol">Delete</span>.</div><div className="itemgroup stepxmp"><img className="image" width={500} src={useBaseUrl("/9962de70-22b2-11ed-9930-0242fe3e4a3f/KS-TDAP-837-Delete-TC-in-TS-righ-click.png")} alt="Delete test cases from a test suite by right-clicking" /></div></div>
