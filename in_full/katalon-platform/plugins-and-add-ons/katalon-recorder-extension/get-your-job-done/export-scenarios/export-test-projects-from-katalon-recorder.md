---
hide_title: true
title: Export test projects from Katalon Recorder
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="id" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Export test projects from <span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon Recorder</span> 

<p xmlns="http://www.w3.org/1999/xhtml" className="p">From version 5.6.0 onwards, Katalon Recorder (KR) you can export multiple tests into a single file. This file is compatible with many other frameworks, such as Katalon Studio, Java Maven or Python. From version 5.9.0 onwards, you can export your project to Selenium 4.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">The export feature is especially useful to outgrow the capabilities of KR. As your work requirements and projects complexity increase, you can move your test artifacts and projects to other frameworks. This allows you to benefit from further advanced testing without losing your work.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">The table below shows the full list of exporting features that KR offers, compared with Selenium IDE:</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-recorder/docs/5.6.0-release/KR%20vs.%20Selenium%20exporting%20features.png")} alt="KR vs Selenium in exporting" /><br /><br /></p> 

## <a id="id_2" class="anchor_top_offset"/>Export to Katalon Studio and other frameworks

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Requirements (for Java/Python frameworks):</p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">ChromeDriver installed.</li><li className="li">Java/Python IDE installed (preferably IntelliJ).</li></ul> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Follow these steps:</p> 
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol"><li className="li">Open Katalon Recorder.</li><li className="li"><p className="p">On the left sidebar, go to <strong className="ph b">Export</strong> &gt; <strong className="ph b">Export to other frameworks</strong>.</p></li><li className="li"><p className="p">Select a framework (e.g., Katalon Studio or Selenium 3, Java (WebDriver + TestNG)).</p></li><li className="li"><p className="p">Select the tests you want to export. </p><p className="p"><img className="image" src={useBaseUrl("/8ab1bae0-22b2-11ed-9930-0242fe3e4a3f/KR-590-selenium-4.jpeg")} /></p><p className="p">Katalon Recorder also notifies you here if there are incompatible commands.</p></li><li className="li"><p className="p">Click <strong className="ph b">Export</strong>.</p></li></ol> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">You can now import the file/project with your framework of choice.</p> 
<div xmlns="http://www.w3.org/1999/xhtml" className="note note note_note"><span className="note__title">Note:</span> <ul className="ul"><li className="li"><p className="p">For Java JUnit, Java TestNG and Python, the data is exported as a full project. You can open the project in the Java/Python IDE.</p></li><li className="li"><p className="p">For other frameworks, the data is exported as a .zip file.</p></li></ul></div>
