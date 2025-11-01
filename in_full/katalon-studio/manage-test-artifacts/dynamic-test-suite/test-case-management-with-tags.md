---
title: Test Case Management With Tags
---
import useBaseUrl from '@docusaurus/useBaseUrl';


<div xmlns="http://www.w3.org/1999/xhtml" className="note note note_note"><span className="note__title">Note:</span> <ul className="ul"><li className="li"><p className="p"><strong className="ph b">Test Case Management With Tags</strong> and <strong className="ph b">Basic Search For Dynamic Test Suite</strong> becomes the official built-in feature of Katalon Studio. See <a className="xref" href="/katalon-studio/manage-test-artifacts/dynamic-test-suite/manage-dynamic-test-suites-in-katalon-studio">Manage dynamic test suites in Katalon Studio</a>.</p></li></ul></div>
<p xmlns="http://www.w3.org/1999/xhtml" className="p">To manage test cases better in Katalon Studio, you can   manipulate tag properties by utilizing the existing tag values.   With the <strong className="ph b">Test Case Management with Tags</strong> plugin,   you can view all tags in the project and save time by appending   existing tags to test cases.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">This document shows you how to append and manage tags, search   for test cases with multiple tags, and execute test cases with   specific tags in console mode.</p> 
    

## Test Case Management with Tags Plugin
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">To append and manage tags, first install our plugin from the   Katalon Store: <a className="xref j-external-link" href="https://store.katalon.com/product/6/Test-Case-Management-with-Tags" target="_blank">Test     Case Management with Tags</a>.</p> 
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Then, open Katalon Studio and select <strong className="ph b">Your Account &gt;     Reload Plugins</strong>. For detailed instructions, see <a className="xref" href="/katalon-platform/plugins-and-add-ons/katalon-store/katalon-studio-plugins/installing-plugin-offline-in-katalon-studio#id_2">Reload     Plugins</a>.</p>   

## Append and Manage Tags   

### Add Tags to a test case

<p xmlns="http://www.w3.org/1999/xhtml" className="p">You can add tags to a test case when you first create a test case. To learn more about how to create a test case, see <a className="xref" href="/katalon-studio/create-test-cases/create-test-case-overview">Create Test Case</a>.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">You can also add tags to a test case using the <strong className="ph b">Properties</strong> tab. Do as follows:</p> 
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol"><li className="li">Open your desired test case.</li><li className="li"><p className="p">Switch to the <strong className="ph b">Properties</strong> tab. In this tab, you can find more details on a test case, including associated tags.</p></li><li className="li"><p className="p">Input your tag values, separate them by commas or semi-colons.</p><p className="p">To remove a tag, delete it from the tag field.</p><p className="p"><img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/test-case-management-with-tags/tag.png")} alt="properties tab" /><br /><br /></p></li></ol> 

### Append Tags

<p xmlns="http://www.w3.org/1999/xhtml" className="p">You can view all tags in your project and append tags to a test case. After installing the <strong className="ph b">Test Case Management with Tags</strong> plugin, follow these instructions:</p> 
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol"><li className="li">     <p className="p">Open a test case and switch to the <strong className="ph b">Properties</strong> tab.</p>     <p className="p">Under the <strong className="ph b">Tag</strong> field, you can find the <strong className="ph b">Append tags</strong> button.</p>   </li><li className="li">     <p className="p">Click on the <strong className="ph b">Append</strong> button. The <strong className="ph b">Append Tags</strong> dialog appears with a list of all tags in your project.</p>   </li><li className="li">     <p className="p">Search for and select tags you wish to add to the current test case.</p>     <div className="note note note_note"><span className="note__title">Note:</span>        <p className="p">Tags previously added to this test case already display as selected, and cannot be deselected.</p>     </div>   </li><li className="li">     <p className="p">Click <strong className="ph b">Append</strong> when you are done. New tags are now added to your test case.</p>     <p className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/test-case-management-with-tags/append-tags.png")} alt="append tags dialog" /><br /><br />     </p>   </li></ol> 

## Search For Test Cases With Multiple Tags

<p xmlns="http://www.w3.org/1999/xhtml" className="p">After you successfully install the Test Case Management With Tags plugin, in a Dynamic Querying Test Suite, you can search for test cases with multiple tags using the <strong className="ph b">Query Provider</strong>.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">To search for test artifacts labeled with multiple tags, do as follows:</p> 
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol"><li className="li">Open a dynamic test suite. See also: <a className="xref" href="/katalon-studio/manage-test-artifacts/manage-test-suites-in-katalon-studio">Dynamic Test Suite (Dynamic Test Cases List)</a>.</li><li className="li">     <p className="p">Directly type in the <strong className="ph b">Query</strong> box following this syntax: <code className="ph codeph">tag=(NameOfTag1,NameOfTag2)</code>. For example: <code className="ph codeph">tag=(may,december)</code>.</p>     <p className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/test-case-management-with-tags/query.png")} alt="query box" /><br /><br />     </p>   </li></ol> 

## Execute Test Cases With Specific Tags in Console Mode

:::tip requirements
- An active Katalon Runtime Engine license
- The Test Case Management with Tags plugin installed
:::

In console mode, you can filter and execute test cases attached with certain tags. In your command, add this argument:

`-testCaseTags="<tag1>,<tag2>"`

Learn more about how to run tests in console mode with Katalon Runtime Engine at [Command Syntax (Command-line/Console Mode Execution)](/katalon-studio/execute-tests/katalon-runtime-engine/command-line-syntax-in-katalon-runtime-engine).

<p xmlns="http://www.w3.org/1999/xhtml" className="p">When you execute a test in the terminal, you can see the process   where test cases are filtered before executing. For example:</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">TC1 <em className="ph i">Verify Successful Login is associated with these tags:     jan,apr TC2</em> Verify Successful Appointment is associated with   these tags: jan,feb,mar TC3_Visual Testing Example is associated   with these tags: jan,feb</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">In the command, you add this argument:   <code className="ph codeph">testCaseTags="jan,feb"</code>.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">The execution log should look like this:</p> 
<pre xmlns="http://www.w3.org/1999/xhtml" className="pre codeblock"><code>----------------- TEST CASE TAGS PLUGIN START FILTERING -----------------{"\n"}Test Cases/Main Test Cases/TC1_Verify Successful Login is filtered out {"\n"}Test Cases/Main Test Cases/TC2_Verify Successful Appointment is a test case to be run{"\n"}Test Cases/Main Test Cases/TC3_Visual Testing Example is a test case to be run{"\n"}----------------- TEST CASE TAGS PLUGIN FINISH FILTERING -----------------{"\n"}</code></pre> 
