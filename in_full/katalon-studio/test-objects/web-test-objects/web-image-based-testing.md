---
hide_title: true
title: Web Image-based Testing
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# Image-based Testing for WebUI

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Katalon Studio provides an image locator method to associate   test objects with images. With this method, you can perform   image-based testing when elements of the web application under   tests (AUT) retain their appearance even though the underlying   structures have changed.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">This guide shows you how to configure image-based object   recognition, capture screenshots, and reduce the chance of failures   in image-based testing.</p> 

## Requirements

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">An active Katalon Studio Enterprise license.</li></ul> 

## Enable Image-based object recognition

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Image-based object recognition is enabled by default for web test execution in <span className="ph uicontrol">Project Settings</span> &gt; <span className="ph uicontrol">Self-Healing</span> &gt; <span className="ph uicontrol">WebUI</span>.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" width={600} src={useBaseUrl("/561d14e0-d5fe-11ee-9719-0242c7a41fd4/ks-931-enable-image-based.png")} /></p> 

## Capture screenshots for object recognition

<section xmlns="http://www.w3.org/1999/xhtml" className="section context">To produce images associated with captured Test objects, Katalon   Studio includes the <span className="ph uicontrol">Add Screenshot</span>  button in both   Web Recorder and Spy utilities.<p className="p">Here we use the <span className="ph">Spy Web Utility</span> to capture     screenshots. Follow these steps:</p></section> 
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol steps"><li className="li step stepexpand"><span className="ph cmd">From the main toolbar, select <span className="ph uicontrol">Spy Web</span>.</span><div className="itemgroup info"><img className="image" width={500} src={useBaseUrl("/560bd6d0-d5fe-11ee-9719-0242c7a41fd4/ks-931-select-spy-web.png")} /></div></li><li className="li step stepexpand"><span className="ph cmd">In the displayed  <span className="ph uicontrol">Object Spy</span> dialog, specify your       URL. In this example, we use the following demo site: <kbd className="ph userinput">https://cms.demo.katalon.com/</kbd>.</span><div className="itemgroup info"><img className="image" width={500} src={useBaseUrl("/55fd30d0-d5fe-11ee-9719-0242c7a41fd4/ks-931-object-spy-dialog.png")} /></div></li><li className="li step stepexpand"><span className="ph cmd">Click  the <span className="ph uicontrol">Start</span>       button to start capturing.</span><div className="itemgroup stepresult">Katalon Studio will launch the web page automatically.</div></li><li className="li step stepexpand"><span className="ph cmd">Navigate to the web element you want to capture, right-click and select <span className="ph uicontrol">Capture Object</span>.</span><div className="itemgroup info"><img className="image" src={useBaseUrl("/56032440-d5fe-11ee-9719-0242c7a41fd4/ks-web-image-capture-object.png")} /></div></li><li className="li step stepexpand"><span className="ph cmd">In the <span className="ph uicontrol">Captured Objects</span> section, select the object, then click <span className="ph uicontrol">Add Screenshot</span> button on the bottom right corner.</span><div className="itemgroup stepresult">The Spy utility verifies the image with the message       <em className="ph i">"Screenshot taken!"</em>.<p className="p"><img className="image" width={500} src={useBaseUrl("/5616d350-d5fe-11ee-9719-0242c7a41fd4/ks-931-screenshot-taken.png")} /></p></div></li><li className="li step stepexpand"><span className="ph cmd">Click <span className="ph uicontrol">Save</span> to save the captured object and its screenshot.</span><div className="itemgroup info"><div className="note note note_note"><span className="note__title">Note:</span> <ul className="ul"><li className="li">The image comparison algorithm in Katalon Studio compares a             screenshot of an object with the displayed image of the             corresponding web element on the active browser, pixel by pixel.             Therefore, if you capture object images using other tools, you have             to resize the images to the displayed sizes of the web elements on             the active browser.</li></ul></div></div></li></ol> 

## Add image locator to objects

By default, Image Locator is not captured when recording or spying objects to avoid performance issues.

To manually capture and add an Image Locator to a test object:

1. Select the object in **Object Repository**.

2. In the **Object** view, check **Image** as the selection method.

    <img src= "https://docs.katalon.com/5621cfd0-d5fe-11ee-9719-0242c7a41fd4/KS_object_image_selector.png" alt="Check Image as the selection method" width="700" />

    :::note
    To add screenshots stored outside the project folder, provide the absolute path to the screenshot in the **Path** property when enabling the image locator.

    <img src= "https://docs.katalon.com/5618a810-d5fe-11ee-9719-0242c7a41fd4/KS_object_screenshot_absolute_path.png" alt="Provide the absolute path to the screenshot in the Path property" width="700" />
    :::

3. Select the screen region that contains the UI element you want to associate with this object.

4. The selected image will be saved as a reference to the object for image-based testing.

5. (Optional) You can rename or replace the image as needed.

<section xmlns="http://www.w3.org/1999/xhtml" className="section context">After you capture a screenshot using the Web Recorder/Spy utility, Katalon Studio automatically adds an image locator to the   associated object. To use the image as the main locator for the object:</section> 
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol steps"><li className="li step stepexpand"><span className="ph cmd">Select the object in <span className="ph uicontrol">Object Repository</span>.</span></li><li className="li step stepexpand"><span className="ph cmd">In the <span className="ph uicontrol">Object</span> view, check <span className="ph uicontrol">Image</span> as the selection method.</span><div className="itemgroup info"><img className="image" width={500} src={useBaseUrl("/5621cfd0-d5fe-11ee-9719-0242c7a41fd4/KS_object_image_selector.png")} alt="Object view - image locator" /><div className="note note note_note"><span className="note__title">Note:</span> <p className="p">To add screenshots stored outside the project folder, provide the           absolute path to the screenshot in the <span className="ph uicontrol">Path</span>           property when enabling the image locator.</p>         <p className="p"><img className="image" width={500} src={useBaseUrl("/5618a810-d5fe-11ee-9719-0242c7a41fd4/KS_object_screenshot_absolute_path.png")} alt="object screenshot absolute path" /></p></div></div></li></ol> 
<section xmlns="http://www.w3.org/1999/xhtml" className="section result">Katalon Studio will use the specified image to identify the object.</section> 
    

## Reduce image-based testing failures

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Since reliable image-based testing depends on image comparison,   you can reduce the chance of failures in two ways:</p> 
      
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul">   <li className="li">     <p className="p">       <strong className="ph b">Screen Resolution</strong>: The screen resolutions of       screenshot capturing devices and test executing devices can affect       the accuracy of image comparison. We recommend capturing       screenshots and executing tests on the same device for the best       results.</p>   </li>   <li className="li">     <p className="p">       <strong className="ph b">Capture tool</strong>: We recommend using built-in       capture tools in Web Recorder and Spy utility since they       automatically resize the captured images.</p>   </li> </ul> 
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <strong className="ph b">See also</strong>:</p> 
      
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul">   <li className="li">     <a className="xref j-external-link" href="https://github.com/katalon-studio-samples/image-recognition-web" target="_blank">Sample       Project</a>   </li>   <li className="li">     <a className="xref" href="/katalon-studio/maintain-tests/self-healing-tests-in-katalon-studio">Self-Healing       Tests</a>   </li> </ul> 
    
  
