---
hide_title: true
title: View captured screenshots in Katalon Studio reports
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="id" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>View captured screenshots in Katalon Studio reports

<p xmlns="http://www.w3.org/1999/xhtml" className="p">With Katalon Studio, you can capture screenshots during test   execution. When a test case fails, the screenshots captured help you identify the problem and debug the test script more effectively.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">By default, Katalon Studio captures screenshots automatically   upon test failures. This feature is  applicable to Web UI   and Mobile testing.</p> 

## <a id="id_1" class="anchor_top_offset"/>View screenshots

<p xmlns="http://www.w3.org/1999/xhtml" className="p">When a test suite fails, you can either open a test suite's report or go to a test suite's <strong className="ph b">Result</strong> tab for captured screenshots.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">To view the captured screenshots in a test suite's <strong className="ph b">Results</strong> tab, follow these steps:</p> 
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol"><li className="li">Select the failed Test Suite.</li><li className="li">Open its <strong className="ph b">Result</strong> tab.</li><li className="li">Select a failed test case.</li><li className="li">     <p className="p">Click <strong className="ph b">Show Test Case Details</strong> on the top right corner.</p>     <p className="p">The Test Case's Log then appears.</p>   </li><li className="li">     <p className="p">Click on the <strong className="ph b">Image</strong> tab.</p>     <p className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/screenshots-videos/log-image.png")} alt="log image" /><br /><br />     </p>   </li></ol> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">To view the captured screenshots in a test suite's report, click <strong className="ph b">Export report</strong> and select the file type (HTML, CSV or PDF), then open the exported file for viewing.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/screenshots-videos/export-report-for-screenshots.png")} alt="export report pdf" /><br /><br /> </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">You can also use the captured screenshots (screenshots taken as checkpoints) for visual testing with TestOps Visual Testing. See: <a className="xref" href="/katalon-platform/analyze/analytics/visual-testing/use-testops-visual-testing">Visual Testing</a>.</p> 

## <a id="id_2" class="anchor_top_offset"/>Deactivate screenshots

<p xmlns="http://www.w3.org/1999/xhtml" className="p">To turn off the default settings, go to <span className="ph uicontrol">Project Settings</span> &gt; <span className="ph uicontrol">Execution</span>. In the displayed <span className="ph uicontrol">During-Execution Options</span> panel, uncheck <span className="ph uicontrol">Take Screenshot when execution failed</span>, and click <span className="ph uicontrol">Apply and Close</span>.</p> 

## <a id="id_3" class="anchor_top_offset"/>Configure screenshots manually

<div xmlns="http://www.w3.org/1999/xhtml" className="p">If you wish to manually set the conditions for capturing screenshots during tests, you can use the following built-in keywords for Web UI and Mobile testing: <ul className="ul"><li className="li"><a className="xref" href="/katalon-studio/keywords/keyword-description-in-katalon-studio/web-ui-keywords/webui-take-screenshot">[WebUI] Take Screenshot</a></li><li className="li"><a className="xref" href="/katalon-studio/keywords/keyword-description-in-katalon-studio/visual-based-web-testing-keywords/webui-take-a-screenshot-as-checkpoint">[WebUI] Take Screenshot As Checkpoint</a></li><li className="li"><a className="xref" href="/katalon-studio/keywords/keyword-description-in-katalon-studio/visual-based-web-testing-keywords/webui-take-area-screenshot-as-a-checkpoint">[WebUI] Take Area Screenshot As Checkpoint</a></li><li className="li"><a className="xref" href="/katalon-studio/keywords/keyword-description-in-katalon-studio/web-ui-keywords/webui-take-area-screenshot">[WebUI] Take Area Screenshot</a></li><li className="li"><a className="xref" href="/katalon-studio/keywords/keyword-description-in-katalon-studio/visual-based-web-testing-keywords/webui-take-element-screenshot-as-checkpoint">[WebUI] Take Element Screenshot As Checkpoint</a></li><li className="li"><a className="xref" href="/katalon-studio/keywords/keyword-description-in-katalon-studio/web-ui-keywords/webui-take-element-screenshot">[WebUI] Take Element Screenshot</a></li><li className="li"><a className="xref" href="/katalon-studio/keywords/keyword-description-in-katalon-studio/visual-based-web-testing-keywords/webui-take-full-page-screenshot-as-checkpoint">[WebUI] Take Full Page Screenshot As Checkpoint</a></li><li className="li"><a className="xref" href="/katalon-studio/keywords/keyword-description-in-katalon-studio/web-ui-keywords/webui-take-full-page-screenshot">[WebUI] Take Full Page Screenshot</a></li><li className="li"><a className="xref" href="/katalon-studio/keywords/keyword-description-in-katalon-studio/mobile-keywords/mobile-take-screenshot">[Mobile] Take Screenshot</a></li></ul> </div>

### <a id="id_4" class="anchor_top_offset"/>Configure screenshots in Manual mode in Katalon Studio

If you are not familiar with coding in Script mode, you can also insert built-in keywords in Manual mode.

Follow these steps:

1. Open Katalon Studio and go to your Project.
2. Select a Test Case in Manual mode.
    
    The Test Case shows all Test steps.
    
    Double click on a Test step and choose options (as shown in the picture below).
    
    <img src="https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/screenshots-videos/insert-webui-keyword-in-test-case-studio.png" alt="navigate to web ui keyword" />
    
    You have added a new Test step in Manual mode.
    
3. Double click on the new Test step, and enter the keyword.
    
    A list of built-in keywords for capturing screenshots displays as below.
    
    <img src="https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/screenshots-videos/custom-keyword-for-screenshots.png" alt="list of built-in keyword" />
    
4. Select a built-in keyword (e.g., **Take Full Page Screenshot As Checkpoint**).
    
    You have inserted the built-in keyword.
    
    <img src="https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/screenshots-videos/input-no-value.png" alt="Take Full Page Screenshot As Checkpoint" />
    
5. Double click on the **Input** section of the newly-added keyword to insert a value.
    
    The **Input** box appears as below.
    
    <img src="https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/screenshots-videos/input-with-value.png" alt="Result after select Take Full Page Screenshot As Checkpoint" />
    
6. Insert a value for the keyword (e.g., **Sample Visual Test**), then click **OK**.

See also:

- [Record Screen-based Videos](/katalon-studio/test-reports/generate-test-reports/generate-screen-based-videos-in-katalon-studio-reports)
- [Record Browser-based Videos](/katalon-studio/test-reports/generate-test-reports/generate-browser-based-videos-in-katalon-studio-reports)
