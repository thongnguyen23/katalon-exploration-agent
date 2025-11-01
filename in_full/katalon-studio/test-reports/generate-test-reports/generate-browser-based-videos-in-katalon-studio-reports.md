---
hide_title: true
title: Generate browser-based videos in Katalon Studio reports
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="id" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Generate browser-based videos in Katalon Studio reports

<div xmlns="http://www.w3.org/1999/xhtml" className="p"><div className="note important note_important"><span className="note__title">Important:</span> <ul className="ul"><li className="li">You need an active <span className="ph">Katalon Studio Enterprise</span> license.</li><li className="li">You need to install the FFmpeg library. See: <a className="xref" href="#id_2">Install FFmpeg library</a>.</li></ul></div></div>
<div xmlns="http://www.w3.org/1999/xhtml" className="p">You can use the browser-based recording feature in <span className="ph">Katalon Studio</span> to capture videos of your test executions. This feature allows you to:<ul className="ul"><li className="li"><p className="p">Record video of browser window only (even if it is hidden behind another window).</p></li><li className="li"><p className="p">Record video of Headless browser. To learn more about Headless Browser Execution, see: <a className="xref" href="/katalon-studio/execute-tests/headless-browsers-execution-in-katalon-studio">Headless Browsers Execution</a>.</p> </li><li className="li"><p className="p"> Record videos of multiple browsers simultaneously (for instance, parallel execution of Test Suite Collection).</p></li></ul></div>
<div xmlns="http://www.w3.org/1999/xhtml" className="p">This document shows you how to enable the browser-based recording feature in Katalon Studio and install FFmpeg as a third-party library for video encoding.<div className="note note note_note"><span className="note__title">Note:</span> <ul className="ul"><li className="li">You can only record and watch videos for Web UI testing.</li><li className="li">This feature supports test suite and test suite collection execution.</li><li className="li">This feature is available for Chrome, Microsoft Edge (Chromium-based), and Headless Chrome. To learn more about Headless Chrome, refer to the Google Developer website here: <a className="xref j-external-link" href="https://developers.google.com/web/updates/2017/04/headless-chrome" target="_blank">Getting Started with Headless Chrome</a>.</li><li className="li">For screen-based recorder, see <a className="xref j-external-link" href="https://docs.katalon.com/katalon-studio/test-reports/generate-test-reports/generate-screen-based-videos-in-katalon-studio-reports" target="_blank">Generate screen-based videos in Katalon Studio reports</a>.</li></ul></div></div>

## Enable browser-based recorder

To enable browser-based recorder in Katalon Studio, follow the steps below:

1. Go to **Project > Settings > Execution**. 

2. In the **During-Execution Options** panel:
 
- Enable Video Recorder by checking **Record video during execution**.
                    
- Select **Record Type** as **Browser-based Recorder**.
- Specify the applicable test cases by choosing either **Failed test cases** or **All Test Cases**.
- Specify video format and quality based on your preferences:
    - **Video format**: WEBM (`.webm`), AVI (`.avi`), MOV (`.mov`), or MP4 (`.mp4`).
    - **Video quality**: Low; Medium or High.                    

<img src="https://tw-cdn.katalon.com/katalon-studio/Test%20report/Generate%20browser-based%20videos.png" alt="browser-based recorder" width="750" />

3. Go to **Desired Capabilities > Web UI**, then select **Chrome**, **Chrome Headless**, or **Edge Chromium**.

4. Click the **Add** button, then type in the following value to set a window size of 1500x1000 for the browser to record and allow all remote origins, as shown in the sample screenshot below.

    | Name | Type | Value |
    |------|------|-------|
    | args | List | --window-size=1500,1000 <br /> --remote-allow-origins=* |

<img src="https://docs.katalon.com/fd3a0860-9336-11ee-ab4f-0242c7a41fd4/KS_set_desired_capabilities_for_browser_based_record.png" alt="Set desired capabilities for Chrome" width="700" />

To learn more about setting desired capabilities for WebUI testing, see: [Set up desired capabilities for WebUI testing](/katalon-studio/manage-projects/project-settings/desired-capabilities/set-up-desired-capabilities-for-webui-testing-in-katalon-studio).

5. Click **Apply & Close**.

## <a id="id_2" class="anchor_top_offset"/>Install FFmpeg library

<div xmlns="http://www.w3.org/1999/xhtml" className="p">To install the FFmpeg library:<ul className="ul"><li className="li"><div className="p">For macOS, use the following command with Homebrew: <pre className="pre codeblock"><code>brew install ffmpeg</code></pre></div></li><li className="li"><div className="p">For Linux, use the following command: <pre className="pre codeblock"><code>sudo apt-get install ffmpeg</code></pre></div></li><li className="li"><div className="p">For Windows users: <ol className="ol"><li className="li"><p className="p">Go to the <a className="xref j-external-link" href="https://ffmpeg.org/download.html" target="_blank">FFmpeg download web page</a>.</p></li><li className="li"><p className="p">Download the package for Windows.</p></li><li className="li"><p className="p">Add the path to the FFmpeg executable file to your PATH environment variable. See <a className="xref" href="/katalon-studio/test-reports/generate-test-reports/generate-browser-based-videos-in-katalon-studio-reports#task-8960">Add FFmpeg to PATH on Windows</a>.</p></li><li className="li"><p className="p">Reactivate <span className="ph">Katalon Studio</span> for this installation to take effect.</p></li></ol></div></li></ul>
For more information on FFmpeg library, see: <a className="xref j-external-link" href="https://ffmpeg.org/" target="_blank">FFmpeg library</a>.</div>

<div className="p">
    <div className="note attention note_attention">
      <h4 className="note__title">Attention:</h4>
      <ul className="ul">
        <li className="li">
          <p className="p">
            FFmpeg v7 has an issue with the VP9 codec. The output file cannot be played on Chrome or Microsoft Edge browsers but works fine on Safari and Firefox. To resolve this issue, you should downgrade FFmpeg to v6.
          </p>
        </li>
      </ul>
      <h5 className="note__subtitle">Commands to install FFmpeg v6 on macOS:</h5>
      <div className="p" style={{ marginLeft: "20px" }}>
        <p className="p">
          Uninstall FFmpeg v7: <code className="ph codeph">brew uninstall ffmpeg</code>
        </p>
        <p className="p">
          Install FFmpeg v6: <code className="ph codeph">brew install ffmpeg@6</code>
        </p>
        <p className="p">
          Link FFmpeg v6: <code className="ph codeph">brew link ffmpeg@6</code>
        </p>
        <p className="p">
          Verify the version: <code className="ph codeph">ffmpeg -version</code>
        </p>
      </div>
    </div>
</div>

### <a id="task-8960" class="anchor_top_offset"/>Add FFmpeg to PATH on Windows

<section xmlns="http://www.w3.org/1999/xhtml" className="section context">
  <p>
    On Windows, to use FFmpeg with Katalon Studio, you need to add it to the system PATH. Follow these steps to configure the PATH variable:
  </p>
</section>

<ol xmlns="http://www.w3.org/1999/xhtml" className="ol steps">
  <li className="li step stepexpand">
    <span className="ph cmd">
      After downloading and extracting the FFmpeg package, rename the extracted folder to <code className="ph codeph">ffmpeg</code>.
    </span>
  </li>
  <li className="li step stepexpand">
    <span className="ph cmd">
      Move the <code className="ph codeph">ffmpeg</code> folder to the root directory of the <code className="ph codeph">C:</code> drive or another location of your choice.
    </span>
  </li>
  <li className="li step stepexpand">
    <span className="ph cmd">
      To add FFmpeg to the PATH, type <kbd className="ph userinput">system variables</kbd> into the search bar, and select <span className="ph uicontrol">Edit the system environment variables</span>.
    </span>
    <div className="itemgroup info">
      <img className="image" width="250" src={useBaseUrl("/1bf5ba7c-3810-43fc-99af-1221b6376319/add_FFmpeg_to_PATH-1.png")} />
    </div>
  </li>
  <li className="li step stepexpand">
    <span className="ph cmd">
      In the <span className="ph uicontrol">System Properties</span> window, go to the <span className="ph uicontrol">Advanced</span> tab and select <span className="ph uicontrol">Environment Variables…</span>.
    </span>
    <div className="itemgroup info">
      <img className="image" width="300" src={useBaseUrl("/6e08cb1a-09bf-40f8-b5da-c299a8eb4c28/add_FFmpeg_to_PATH-2.png")} />
    </div>
  </li>
  <li className="li step stepexpand">
    <span className="ph cmd">
      Under the <span className="ph uicontrol">User variables for [Your Username]</span> section, locate the <code className="ph codeph">Path</code> variable and select <span className="ph uicontrol">Edit…</span>.
    </span>
    <div className="itemgroup info">
      <img className="image" width="450" src={useBaseUrl("/93f0f600-40cb-4909-8dc5-bfcd9cf34f69/add_FFmpeg_to_PATH-3.png")} />
    </div>
  </li>
  <li className="li step stepexpand">
    <span className="ph cmd">
      In the <span className="ph uicontrol">Edit environment variable</span> window, click <span className="ph uicontrol">New</span> and enter the path to the FFmpeg binary folder (for example, <code className="ph codeph">C:\ffmpeg\bin</code>).
    </span>
    <div className="itemgroup info">
      <img className="image" width="350" src={useBaseUrl("/13c774d7-a8fb-429d-bd5f-497b8667312c/add_FFmpeg_to_PATH-4.png")} />
    </div>
  </li>
  <li className="li step stepexpand">
    <span className="ph cmd">
      Click <span className="ph uicontrol">OK</span> to close all dialog boxes and save the changes.
    </span>
  </li>
</ol>

<section xmlns="http://www.w3.org/1999/xhtml" className="section result">
  <p>
    To verify that FFmpeg has been correctly added to the PATH, open the Command Prompt and run the following command:
  </p>
  <pre className="pre codeblock">
    <code>ffmpeg -version</code>
  </pre>
  <p className="p">
    The output should display FFmpeg version details, confirming the installation.
  </p>
  <p className="p">
    <img className="image" width="500" src={useBaseUrl("/77ece238-daf2-4335-88e3-b6af84766db2/add_FFmpeg_to_PATH-5.png")} />
  </p>
  <div className="p">
    <div className="note attention note_attention">
      <h4 className="note__title">Attention:</h4>
      <ul className="ul">
        <li className="li">
          <p className="p">
            If you have already installed FFmpeg, but typing <code className="ph codeph">ffmpeg</code> in the command prompt returns nothing, make sure your user account has full permission <strong className="ph b">OR</strong> run CMD window as Administrator mode.
          </p>
        </li>
      </ul>
    </div>
  </div>
</section>

### <a id="task-5317" class="anchor_top_offset"/>Build and commit a Docker image with FFmpeg installed

<p xmlns="http://www.w3.org/1999/xhtml" className="shortdesc">Katalon Docker image may be used as a container to execute <span className="ph">Katalon Studio</span> tests and write reports to the host's file system. However, the default Katalon Docker image does not include the FFmpeg library required for browser-based video recording.</p> 
<section xmlns="http://www.w3.org/1999/xhtml" className="section context">The following steps guide you through building and committing your own Docker image with FFmpeg installed.<div className="p"><div className="note note note_note"><span className="note__title">Note:</span> <ul className="ul"><li className="li"><p className="p">This procedure assumes you are using the Docker image <code className="ph codeph">katalon:9.7.2</code>. To check for the latest images, visit the <a className="xref j-external-link" href="https://hub.docker.com/r/katalonstudio/katalon/tags" target="_blank">Katalon Docker Hub</a>.</p></li><li className="li"><p className="p">Make sure the image tag matches the version of Katalon Studio installed on your system.</p></li></ul></div></div></section> 
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol steps"><li className="li step stepexpand"><span className="ph cmd">Run a container from the Katalon Docker image.</span><ol type="a" className="ol substeps"><li className="li substep substepexpand"><span className="ph cmd">Open a terminal on your local machine.</span></li><li className="li substep substepexpand"><span className="ph cmd">Run the following command to start a container from the desired Katalon Docker image (for example, version 9.7.2):</span><div className="itemgroup info"><pre className="pre codeblock"><code>docker run -it katalonstudio/katalon:9.7.2 /bin/bash</code></pre></div></li><li className="li substep substepexpand"><span className="ph cmd">Inside the container, update the package manager and install FFmpeg:</span><div className="itemgroup info"><pre className="pre codeblock"><code>apt-get update{"\n"}apt-get -y install ffmpeg</code></pre></div></li></ol></li><li className="li step stepexpand"><span className="ph cmd">Save the updated container as a new image.</span><ol type="a" className="ol substeps"><li className="li substep substepexpand"><span className="ph cmd">Open another terminal and list the active Docker containers to locate the container ID:</span><div className="itemgroup info"><pre className="pre codeblock"><code>docker ps</code></pre><div className="p">Example output:<pre className="pre codeblock"><code>CONTAINER ID{"   "}IMAGE{"                             "}COMMAND{"\n"}6e9278d5d7f4{"   "}katalonstudio/katalon:9.7.2{"      "}"/bin/bash"{"\n"}</code></pre></div></div></li><li className="li substep substepexpand"><span className="ph cmd">Use the container ID from the output to save the updated container as a new Docker image:</span><div className="itemgroup info"><pre className="pre codeblock"><code>docker commit &lt;container id&gt; &lt;new image name&gt;</code></pre><div className="p">For example, if the container ID is <code className="ph codeph">6e9278d5d7f4</code> and you want to name the new image <code className="ph codeph">ksffmpeg</code>, the command would be:<pre className="pre codeblock"><code>docker commit 6e9278d5d7f4 ksffmpeg</code></pre></div></div></li></ol></li><li className="li step stepexpand"><span className="ph cmd">Run your image.</span><div className="itemgroup info">In the below example, we are running the <code className="ph codeph">ksffmpeg</code> image from the Katalon project directory and mapping a docker volume to the drive.<pre className="pre codeblock"><code>docker run -t --rm -v ${"{"}pwd{"}"}:/tmp/project ksffmpeg katalonc.sh -retry=0 -projectPath="/tmp/project/web-keywords-automation.prj" -testSuitePath="Test Suites/WebUI Keywords Test" -browserType="Chrome" -executionProfile="default" -apiKey="&lt;removed&gt;" -orgID=&lt;removed&gt; --config -proxy.auth.option=NO_PROXY -proxy.system.option=NO_PROXY -proxy.system.applyToDesiredCapabilities=true</code></pre></div></li></ol> 
<section xmlns="http://www.w3.org/1999/xhtml" className="section result">You have built your own images for Katalon Docker image. For more information on Katalon Docker image, see: <a className="xref" href="/katalon-studio/execute-tests/katalon-runtime-engine/katalon-docker-image-kdi">Katalon Docker Image (KDI)</a>.</section> 

## <a id="concept-6849" class="anchor_top_offset"/>View recorded videos

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Click the <em className="ph i">Play</em> icon in the <span className="ph uicontrol">Video</span> column to play the video as shown below. Each test step in the video has a description embedded like a subtitle.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">After running the test suite, navigate to the <span className="ph uicontrol">Result</span> tab. You can see a list of test cases. A recorded video is attached to each test case.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" width={700} src={useBaseUrl("/3c12c860-9dec-11ed-998d-0242cfbc79b5/ks-reports-view-video.png")} alt="View result video" /></p> 

### See also

<div xmlns="http://www.w3.org/1999/xhtml" className="p"><ul className="ul"><li className="li"><a className="xref" href="/katalon-studio/troubleshooting/troubleshoot-web-automated-testing/common-issues-with-browser-based-videos-in-katalon-studio-report">Common issues with browser-based videos in Katalon Studio report</a>.</li></ul></div>
