---
hide_title: true
title: Create your first automation script in Katalon Recorder
---

# <a id="id" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Create your first automation script in <span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon Recorder</span> 

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Broadly speaking, there are usually two steps to create an   automate scenario in Katalon Recorder: 1. Add commands to interact   with websites 2. Add verify or assert commands to make sure your   test case follows the correct flow.</p> 

## <a id="id_1" class="anchor_top_offset"/>Add commands to interact with websites

<div xmlns="http://www.w3.org/1999/xhtml" className="p">To get started, use the Recorder to automatically create a test
  case: <ul className="ul"><li className="li"><p className="p">Click on the <strong className="ph b">Record</strong> button.</p></li><li className="li"><p className="p">Switch to
        the currently active tab.</p></li><li className="li"><p className="p">Start interacting with your website.</p></li><li className="li"><p className="p">Switch to Katalon Recorder.</p></li><li className="li"><p className="p">Click the <strong className="ph b">Stop</strong>
        button.</p></li></ul></div>
<p xmlns="http://www.w3.org/1999/xhtml" className="p">You should see your interactions are recorded as a test   case.</p> 
    

## <a id="id_2" class="anchor_top_offset"/>Add verify or assert commands

    
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">There are two ways to add verify or assert commands.</p> 
    
          

### <a id="id_3" class="anchor_top_offset"/>After the recording of a test case

<div xmlns="http://www.w3.org/1999/xhtml" className="p">If you just have just recorded a test case:<ul className="ul"><li className="li"><p className="p"> Add a new test
        step through the toolbar item.</p></li><li className="li"><p className="p">Type <code className="ph codeph">verify</code> or
        <code className="ph codeph">assert</code> in the Command field of the new test step.</p></li><li className="li"><p className="p">Choose from the list of available suggested commands (for example
        <code className="ph codeph">verifyElementPresent</code>).</p></li><li className="li"><p className="p">Click on the button
        <strong className="ph b">Select a target element for the current command</strong>
        located next to the Target field of the new test step.</p></li><li className="li"><p className="p">Switch to
        the currently active tab.</p></li><li className="li"><p className="p">Select an element on the page.</p></li><li className="li"><p className="p">Switch
        back to Katalon Recorder.</p></li></ul></div>
<p xmlns="http://www.w3.org/1999/xhtml" className="p">You should see the newly created assert or verify command for   the target element.</p> 

### <a id="id_4" class="anchor_top_offset"/>During the recording of a test case

<div xmlns="http://www.w3.org/1999/xhtml" className="p">If you are recording a test case:<ul className="ul"><li className="li"><p className="p">Right-click on the target
        element.</p></li><li className="li"><p className="p">Choose a command from the context menu item <em className="ph i">Katalon
          Recorder (Selenium tests generator)</em>.</p></li></ul> </div>
