---
hide_title: true
title: Dynamic Test Suite in Katalon Recorder
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="id" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Dynamic Test Suite in <span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon Recorder</span> 


:::tip requirements
Katalon Recorder version 5.6.0 onwards.
:::
<p xmlns="http://www.w3.org/1999/xhtml" className="p">With Dynamic Test Suites, you can add multiple test cases at run   time via a search query. It allows users to execute test cases with   certain tags dynamically.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">In this article, we show you how to categorize test cases with   tags and execute them in a dynamic test suite.</p> 

## <a id="id_1" class="anchor_top_offset"/>Categorize Test Cases with Tags

:::info notes
A tag can be reused across test cases, but you can not have a duplicated tag in a test case.
:::
### <a id="id_2" class="anchor_top_offset"/>Categorize test cases with Tags Management

<p xmlns="http://www.w3.org/1999/xhtml" className="p">The <strong className="ph b">Tags Management</strong> function allows you to manage all tags in one place. You can add/remove or edit tags in one or many selected test cases.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Follow these steps:</p> 
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol"><li className="li">     <p className="p">In the <strong className="ph b">Actions</strong> panel, click <strong className="ph b">Tags Management</strong>. The <strong className="ph b">Tags Management</strong> dialog opens.</p>   </li><li className="li">     <p className="p">In the opened dialog, the first interface shows you a list of existing tags and the number of test cases where the tags are present. If you have no tags, this page should be blank.</p>     <p className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-recorder/docs/dynamic-test-suite/KR-DYNAMIC-List-of-existing-tags.png")} alt="List of existing tags" /><br /><br />     </p>     <ul className="ul"><li className="li">         <p className="p">To add new tags, click <strong className="ph b">Add new tag</strong>. The opened interface allows you to add new tags to one or many selected test cases. You can also add tags to all test cases in a test suite.</p>         <p className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-recorder/docs/dynamic-test-suite/KR-DYNAMIC-Add-new-tag.png")} alt="Add new tags from tags management" /><br /><br />         </p>         <ul className="ul"><li className="li">             <p className="p">Input the new tag name, then click <strong className="ph b">Save</strong> to add tags to selected test cases.</p>             <p className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-recorder/docs/dynamic-test-suite/KR-DYNAMIC-Add-tags-from-tags-management.png")} alt="Add new tags from tags management" /><br /><br />             </p>           </li><li className="li">             <p className="p">After adding tags, the tag icon is highlighted in the sidebar for this test case.</p>             <p className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-recorder/docs/dynamic-test-suite/KR-DYNAMIC-Highlighted-tag-icon-after-adding-tags.png")} alt="Tags icon highlighted after adding tags" /><br /><br />             </p>           </li></ul>       </li><li className="li">         <p className="p">To remove tags, click <em className="ph i">Remove</em> (Trash icon) of the tag you wish to remove. Katalon Recorder deletes it from all test cases.</p>         <p className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-recorder/docs/dynamic-test-suite/KR-DYNAMIC-Remove-the-tag.png")} alt="Remove tags in all test cases" /><br /><br />         </p>       </li><li className="li">         <p className="p">To edit tags, click <em className="ph i">Edit</em> (Pencil icon) of the tag you wish to edit. By default, Katalon Recorder will check the box of the test case where the edited tag exists. After editing the tags, click <strong className="ph b">Save</strong>. The new tag will replace the previous one in all checked test cases.</p>         <p className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-recorder/docs/dynamic-test-suite/KR-DYNAMIC-Edit-tags.png")} alt="Edit tags in all test cases" /><br /><br />         </p>         <p className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-recorder/docs/dynamic-test-suite/KS-DYNAMIC-Click-save-to-edit.png")} alt="Save edited tags" /><br /><br />         </p>         <div className="note note note_note"><span className="note__title">Note:</span>            <ul className="ul"><li className="li">               <p className="p">If you wish to remove the edited tag from a test case, leave the box of the test case unchecked. In the above example, when changing the tag name from <code className="ph codeph">Dashboard</code> to <code className="ph codeph">Calculator</code>, if you uncheck the <strong className="ph b">Test case 01</strong> test case, there will be no tags named <code className="ph codeph">Dashboard</code> or <code className="ph codeph">Calculator</code> in this test case.</p>             </li><li className="li">               <p className="p">If you wish to add the edited tag to a test case, check the box of the test case you wish to add the tag. In the above example, when changing the tag name from <code className="ph codeph">Dashboard</code> to <code className="ph codeph">Calculator</code>, if you check the box of the <strong className="ph b">UI Test</strong> test case, a new tag named <code className="ph codeph">Calculator</code> will be added to this test case.</p>             </li></ul>         </div>       </li></ul>   </li></ol> 

### <a id="id_3" class="anchor_top_offset"/>Categorize test cases from test case view

<p xmlns="http://www.w3.org/1999/xhtml" className="p">You can also add tags directly to a test case. To do so, open the desired test case. Click <strong className="ph b">Add new tag</strong> in the test case header, then manually input the tag name or select an existing tag in the dropdown list.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/b8e6cfa9512728f2d1c7b99e7336bafe19089a20/katalon-recorder/docs/dynamic-test-suite/KR-DYNAMIC-Add-new-tags-from-test-case%202.png")} alt="Add tags from test case view" /><br /><br /> </p> 

### <a id="id_4" class="anchor_top_offset"/>Categorize test cases from the Workspace sidebar

<p xmlns="http://www.w3.org/1999/xhtml" className="p">To quickly add new tags from the <strong className="ph b">Workspace</strong> sidebar, click <strong className="ph b">Tags</strong> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-recorder/docs/dynamic-test-suite/KR-DYNAMIC-Tag-icon.png")} alt="Tag icon" /><br /><br />. A pop-up <strong className="ph b">Tag this test case</strong> dialog allows you to manually input the tag name or select an existing tag in the dropdown list.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-recorder/docs/dynamic-test-suite/KR-DYNAMIC-Add-tags-from-the-workspace-sidebar.png")} alt="Add tags from the Workspace sidebar" /><br /><br /> </p> 
    

## <a id="id_5" class="anchor_top_offset"/>Execute Dynamic Test Suite containing Categorized Test         Cases

    
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">After categorizing your test cases with tags, you can now   execute them in a dynamic test suite.</p> 
    
              

### <a id="id_6" class="anchor_top_offset"/>Create a new Dynamic Test Suite

<p xmlns="http://www.w3.org/1999/xhtml" className="p">To quickly create a new Dynamic Test Suite, click on a tag from the <strong className="ph b">Workspace</strong> sidebar or the test case view.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-recorder/docs/dynamic-test-suite/KR-DYNAMIC-Click-a-tag-from-the-workspace-sidebar.png")} alt="Click a tag from the workspace sidebar" /><br /><br /> </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">An <strong className="ph b">Execute test case</strong> dialog opens, showing all test cases of the selected tag.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-recorder/docs/dynamic-test-suite/KR-DYNAMIC-an-execute-test-case-dialog.png")} alt="An execute test case dialog opens" /><br /><br /> </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Alternatively, you can also click <em className="ph i">Add</em> (+) in the <strong className="ph b">Dynamic Test Suite</strong> section from the <strong className="ph b">Workspace</strong> sidebar to create a new Dynamic Test Suite.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-recorder/docs/dynamic-test-suite/KR-dynamic-Create-Dynamic-Test-Suite-manually.png")} alt="Create a new dynamic test suite manually" /><br /><br /> </p> 

### <a id="id_7" class="anchor_top_offset"/>Add categorized test cases into a Dynamic Test Suite

<p xmlns="http://www.w3.org/1999/xhtml" className="p">To add categorized test cases into a Dynamic Test Suite, select or type the tags of the desired test cases in the <strong className="ph b">Input tags</strong> box. Each tag is separated by a comma. Then click <strong className="ph b">Apply</strong> to query out the matching test cases.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">For example: To add the test cases with the <code className="ph codeph">aTag_1</code> and <code className="ph codeph">atag_2</code> tags into the dynamic test suite, you can click on the <code className="ph codeph">aTag_1</code> and <code className="ph codeph">atag_2</code> tags or input <code className="ph codeph">aTag_1,atag_2</code> into the <strong className="ph b">Input tags</strong> box, then click <strong className="ph b">Apply</strong>. Katalon Recorder will query out the matching test cases.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <img className="image" src={useBaseUrl("https://user-images.githubusercontent.com/16775806/138648208-d277f8e4-145f-47af-8a84-7076abb92ac1.gif")} alt="Results after searching query" /><br /><br /> </p> 

### <a id="id_8" class="anchor_top_offset"/>Run the Dynamic Test Suite

<p xmlns="http://www.w3.org/1999/xhtml" className="p">After selecting test cases, click <strong className="ph b">Execute</strong> in the <strong className="ph b">Execute test case</strong> dialog to create and execute the dynamic test suite with the specified query.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-recorder/docs/dynamic-test-suite/KR-DYNAMIC-execute-a-dynamic-test-suite.png")} alt="Execute the dynamic test suite" /><br /><br /></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">If you are running the test suite from the dynamic test suite view, click <strong className="ph b">Play</strong> instead.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-recorder/docs/dynamic-test-suite/KR-DYNAMIC-click-play.png")} alt="Click play in the test suite view" /><br /><br /></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">After executing the test suite, you can check the status of your test in the <strong className="ph b">Log</strong> tab.</p> 
<div xmlns="http://www.w3.org/1999/xhtml" className="note note note_note"><span className="note__title">Note:</span> <p className="p">For real-time monitoring and better reporting capabilities, consider integrating your project with Katalon TestOps. To learn more about TestOps integration, you can refer to this document: <a className="xref" href="/katalon-platform/plugins-and-add-ons/katalon-recorder-extension/get-your-job-done/execution-report/view-execution-reports-in-testops">View execution reports in TestOps</a>.</p></div>
