---
hide_title: true
title: Canvas automation
---

# <a id="concept-9276" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Canvas automation

<p xmlns="http://www.w3.org/1999/xhtml" className="shortdesc">This article demonstrates how <span className="ph">Katalon Studio</span> helps users to automate Canvas application test cases.</p> 
<div xmlns="http://www.w3.org/1999/xhtml" className="note note note_note"><span className="note__title">Note:</span> <p className="p">This integration provides assistance for certain user-specific use cases, but it is not officially supported. Compatibility with all user requirements is not guaranteed.</p></div>
<p xmlns="http://www.w3.org/1999/xhtml" className="p">A canvas is a rectangular area on an HTML page, and it is specified with the elements in HTML 5. All objects inside the canvas can not be accessible via DOM (by Xpath, CSS, or Property). Because of the limited access to DOM, users have to find the coordinates for objects before performing the actions.</p> 

## Use case

<p xmlns="http://www.w3.org/1999/xhtml" className="p">We illustrate two different application with our sample project:</p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p"><a className="xref j-external-link" href="https://www.online-calculator.com//html5/simple/index.php?v=10" target="_blank">Online calculator</a>.</p></li><li className="li"><p className="p"><a className="xref j-external-link" href="https://kitchen.applitools.com/ingredients/canvas" target="_blank">Kitchen application</a>.</p></li></ul> 

## Test steps

<div xmlns="http://www.w3.org/1999/xhtml" className="p"><ul className="ul"><li className="li">Perform calculations (1+8=9) on the calculator.</li><li className="li"><p className="p">Open the Web application with Canvas.</p></li><li className="li"><p className="p">Capture the Canvas Object.</p></li><li className="li"><p className="p">Find the Coordinates for the Targeted Object inside the Canvas.</p></li><li className="li"><p className="p">Perform the action.</p></li></ul></div>

## <a id="task-8804" class="anchor_top_offset"/>Automate Canvas application test case with Katalon Studio

<section xmlns="http://www.w3.org/1999/xhtml" className="section context">   <ul className="ul"><li className="li">       <p className="p"><a className="xref j-external-link" href="https://github.com/katalon-studio-samples/katalon-canvas-sample.git" target="_blank">Sample Git repository for this project</a>.</p></li><li className="li"><p className="p">You can refer to this <a className="xref j-external-link" href="https://academy.katalon.com/katalon-demo-and-integration/?video=36510" target="_blank">video demonstration</a> of the steps below.</p>     </li></ul> </section> 
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol steps"><li className="li step"><span className="ph cmd">Canvas application is completely working on coordinates. </span></li><li className="li step"><span className="ph cmd">Find the coordinates for the object.</span></li><li className="li step"><span className="ph cmd">Write a test script by using object coordinates.</span></li><li className="li step"><span className="ph cmd">Run the test script on the browser. </span></li><li className="li step"><span className="ph cmd">Verify the test result.</span></li></ol> 
