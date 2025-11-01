---
hide_title: true
title: Global variables in Katalon Recorder
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="id" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Global variables in <span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon Recorder</span> 

In test automation, sometimes multiple test cases might require the same values. Instead of manually duplicating the same set of values across multiple test cases, you can create global variables to reuse the same values across test cases. This saves time and reduces maintenance efforts as projects increase in complexity. From version 5.6.0 onwards, you can use the **Global Variable Profile** feature in Katalon Recorder (KR) to help you automate tests with ease.

This feature reduces syntax complexity so that you can simply use global variables with just one click.

Global variables are cross-compatible with Katalon Studio when migrating your projects.
:::info notes
Global variables are fixed. You cannot modify them during a test execution.
:::

## <a id="id_1" class="anchor_top_offset"/>Global Variable Profile

Creating a Global Variable Profile allows you to save which global variables apply to which workflow. These Profiles can be migrated to Katalon Studio (KS) along with your projects.

Follow these steps:

1. Open Katalon Recorder.
2. On the left sidebar, go to **Global Variable Profile** and click on the + button next to it to create a new Global Variable Profile.
3. Right click on the newly-created Global Variable Profile and select **Set as default profile**.

Repeat the steps to create multiple Global Variable Profiles.
:::info notes
- You must set one Global Variable Profile as default.
- You cannot delete a default Global Variable Profile. To delete it, you have to set another Global Variable Profile as default.
:::
## <a id="id_2" class="anchor_top_offset"/>Add Global Variables

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Follow these steps:</p> 
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol"><li className="li">Go to <strong className="ph b">Global Variable Profile</strong> and right-click on the profile.</li><li className="li">     <p className="p">Select <strong className="ph b">Use this in a test case</strong>.</p>     <p className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-recorder/docs/5.6.0-release/use-gv-in-test-case.png")} alt="kr ui use gv in test case" /><br /><br />     </p>     <p className="p">The <strong className="ph b">Add global variables to test case</strong> box pops up.</p>   </li><li className="li">     <p className="p">Follow the two steps in the popup box.</p>     <ul className="ul"><li className="li">         <p className="p">Step 1: Select the test case you want to add global variables to.</p>         <p className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-recorder/docs/5.6.0-release/add-gv-step1.png")} alt="kr ui use gv in test case" /><br /><br />         </p>       </li><li className="li">         <p className="p">Step 2: Check your test data and select its value.</p>         <p className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-recorder/docs/5.6.0-release/add-gv-step2.png")} alt="kr ui use gv in test case" /><br /><br />         </p>         <div className="note note note_note"><span className="note__title">Note:</span>            <p className="p">From KR 5.6.0 onwards, you can easily use a selected command without the need to know the syntax for implementing global variables in a test case.</p>         </div>       </li></ul>   </li></ol> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">You can now run the tests without inputting the same sets of values for every test.</p> 
