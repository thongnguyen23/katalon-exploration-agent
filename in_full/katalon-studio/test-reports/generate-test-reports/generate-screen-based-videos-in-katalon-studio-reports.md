---
hide_title: true
title: Generate screen-based videos in Katalon Studio reports
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="id" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Generate screen-based videos in <span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon Studio</span>  reports

<p xmlns="http://www.w3.org/1999/xhtml" className="p"><span className="ph">Katalon Studio</span> supports screen-based recording when running WebUI tests.</p> 

:::info notes
- Screen-based recorder is only applicable for local WebUI testing.
- Screen-based recorder is available for single test suite execution only. To record parallel executions, you can refer to [Record Browser-based Videos](/katalon-studio/test-reports/generate-test-reports/generate-browser-based-videos-in-katalon-studio-reports).
:::

<p xmlns="http://www.w3.org/1999/xhtml" className="p">We recommend the <a className="xref j-external-link" href="https://www.codecguide.com/download_kl.htm" target="_blank">K-Lite Codec</a> to play the recorded video.</p> 

## <a id="task-4891" class="anchor_top_offset"/>Enable screen-based recorder

<section xmlns="http://www.w3.org/1999/xhtml" className="section context"><div className="note note note_note"><span className="note__title">Note:</span> <p className="p">If you use macOS, make sure you first enable Katalon Studio for screen recording. On your Mac, go to <span className="ph uicontrol">Privacy &amp; Security</span> settings &gt; <span className="ph uicontrol">Privacy</span> &gt; <span className="ph uicontrol">Screen Recording</span> &gt; Allow <span className="ph">Katalon Studio</span> to do Screen Recording.</p></div><p className="p">To enable screen recorder, follow these steps:</p></section> 

1. In Katalon Studio, go to **Project > Settings > Execution**.

2. In the **During-Execution Options** panel, enable Video Recorder by checking **Record video during execution**.

3. Select **Record Type** as **Screen Recorder** and specify the applicable test cases by choosing either **Failed test cases** or **All Test Cases**.

<img src="https://tw-cdn.katalon.com/katalon-studio/Test%20report/Generate%20screen-based%20videos.png" alt="Enable Screen-based Recorder" width="750" />

4. Specify video settings based on your preferences.

We recommend AVI (`.avi`) format and low quality to save disk space. Higher video quality means bigger file size.

- **Video format**: AVI (`.avi`) or MOV (`.mov`).
- **Video quality**: Low; Medium or High.

5. Click **Apply and Close**.

## <a id="id_3" class="anchor_top_offset"/>View recorded videos

<p xmlns="http://www.w3.org/1999/xhtml" className="p">After running the test suite, navigate to the <span className="ph uicontrol">Result</span> tab. You can see a list of test cases. A recorded video is attached to each test case accordingly.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Click on the <em className="ph i">Play</em> icon in the <span className="ph uicontrol">Video</span> column to play the video or navigate to the video folder and use any available video player.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" width={700} src={useBaseUrl("/2b3bb4b0-c877-11ed-a4d3-0242cfbc79b5/KS_test_suite_result_video.png")} alt="KS test suite result video column" /></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" width={700} src={useBaseUrl("/2b380b30-c877-11ed-a4d3-0242cfbc79b5/Screen-based_recording_result.png")} alt="Recorded video" /></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Each test step in a video has a description embedded like a subtitle.</p> 
