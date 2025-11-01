---
hide_title: true
title: Katalon Docker Image (KDI)
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="id" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Katalon Docker Image (KDI)

<div xmlns="http://www.w3.org/1999/xhtml" className="note important note_important"><span className="note__title">Important:</span> <ul className="ul"><li className="li">Docker installed. You can refer to the instructions in the Docker document here: <a className="xref j-external-link" href="https://docs.docker.com/get-docker/" target="_blank">Get Docker</a>. </li><li className="li">An active Katalon Runtime Engine floating license. See: <a className="xref" href="#">Types of licenses</a>.</li></ul></div>
<p xmlns="http://www.w3.org/1999/xhtml" className="p">This tutorial shows you how to run tests with Katalon Docker Image (KDI). </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">KDI contains up-to-date browsers, including Google Chrome, Mozilla Firefox, Microsoft Edge, and Katalon Studio. With KDI, you do not need to use the Katalon Studio and Runtime Engine apps installed on your local machine.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">KDI for Katalon Studio is available at Docker Hub: <a className="xref j-external-link" href="https://hub.docker.com/r/katalonstudio/katalon/" target="_blank">katalonstudio/katalon</a>.</p> 
<div xmlns="http://www.w3.org/1999/xhtml" className="note note note_note"><span className="note__title">Note:</span> <ul className="ul"><li className="li">You can find the source code of the Docker image in our GitHub repository: <a className="xref j-external-link" href="https://github.com/katalon-studio/docker-images" target="_blank">KDI</a>.</li><li className="li">You can download our GitHub sample project for CI configurations using Docker image: <a className="xref j-external-link" href="https://github.com/katalon-studio/docker-images-samples" target="_blank">CI samples</a>.</li><li className="li"><p className="p">Docker <code className="ph codeph">latest</code> and <code className="ph codeph">latest-slim</code> tags now point to the latest version 10.x.</p></li></ul></div>

## <a id="task-867" class="anchor_top_offset"/>Pull Katalon Docker Image (KDI)

<p xmlns="http://www.w3.org/1999/xhtml" className="shortdesc">Follow these steps to pull the Katalon Docker Image (KDI).</p> 
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol steps"><li className="li step stepexpand"><span className="ph cmd">Open a Terminal from your local machine.</span></li><li className="li step stepexpand"><span className="ph cmd">Copy and paste the following command: </span><div className="itemgroup info"><pre className="pre codeblock"><code>docker pull katalonstudio/katalon:10-latest-slim{"\n"}</code></pre>This opens Docker and pulls the latest Katalon Runtime Engine 10.x version. <div className="note tip note_tip"><span className="note__title">Tip:</span> <ul className="ul"><li className="li">The <code className="ph codeph">10-latest-slim</code> tag applies to the latest Katalon Runtime Engine, which we recommend for production use.</li><li className="li">You may also use the <code className="ph codeph">10-latest</code> tag to pull in WebDriverManager and Gradle.</li><li className="li">The major version number in the tag (<code className="ph codeph">10-latest-slim</code>, <code className="ph codeph">10-latest</code>, <code className="ph codeph">9-latest-slim</code>, <code className="ph codeph">9-latest</code>, <code className="ph codeph">8-latest</code>) should match your major version of Katalon Studio (<strong className="ph b">10</strong>.0,<strong className="ph b">9</strong>.7, <strong className="ph b">8</strong>.6). </li></ul></div></div></li></ol> 
<section xmlns="http://www.w3.org/1999/xhtml" className="section result"><p className="p">You should see the <code className="ph codeph">katalonstudio/katalon</code> image in your Docker application.</p><p className="p"><img className="image" width={700} src={useBaseUrl("/4d1d00f6-e386-4452-85db-4fc3da5e7982/Pull_Katalon_Docker_Image.png")} /></p><div className="p">To check which Chrome and Firefox versions are supported by the Katalon Docker Image, run the following command: <pre className="pre codeblock"><code>docker run -t --rm katalonstudio/katalon:10-latest-slim cat /katalon/version{"\n"}</code></pre></div></section> 

## <a id="id_2" class="anchor_top_offset"/>Execute Katalon Studio tests with Katalon Docker Image

:::tip requirements
- Katalon Docker Image version 7.2.1 onwards.
- Make sure you have Docker open while running the test.
:::

1. Open **Terminal**, then go to the test project directory you wish to run. For example, we want to run the **CI sample** test project, we will direct to our **CI sample** project folder in our local machine.
2. Inside your test project folder, input the following command:
    
    For macOS:
    ```jsx
    docker run -t --rm -v "$(pwd)":/tmp/project katalonstudio/katalon katalonc.sh -projectPath=/tmp/project [Option1] [Option2] ... [OptionN]
    
    ```
    For Window PowerShell:
    ```jsx
    docker run -t --rm -v ${pwd}:/tmp/project katalonstudio/katalon katalonc.sh -projectPath=/tmp/project [Option1] [Option2] ... [OptionN]
    
    ```
    For Window CMD:
    ```jsx
    docker run -t --rm -v "%cd%":/tmp/project katalonstudio/katalon katalonc.sh -projectPath=/tmp/project [Option1] [Option2] ... [OptionN]
    
    ```
:::info notes
- The `katalonc.sh` command starts Katalon Studio and other necessary components.
- All Katalon Studio console mode arguments are accepted except `runMode`. You can find more command-line options at [Command Syntax](/katalon-studio/execute-tests/katalon-runtime-engine/command-line-syntax-in-katalon-runtime-engine#concept-1437).
:::
For example, we want to run the **TS_RegressionTest** test suite from the **CI sample** project with the Chrome browser in Katalon Docker Image. We enter the command as follows:

```jsx
docker run -t --rm -v "$(pwd)":/tmp/project katalonstudio/katalon katalonc.sh -projectPath=/tmp/project -browserType="Chrome" -testSuiteCollectionPath="Test Suites/TS_RegressionTestCollection" -apiKey="<your_API_key>"

```

<img src="https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/katalon-docker-image/KS-DOCKER-Run-test-with-Docker.png" alt="CI cmd" /> 

:::info notes
- To avoid syntax errors, you can use the Command Builder to generate commands. To learn more about the command builder, you can refer to this document: [Command Builder](/katalon-studio/execute-tests/katalon-runtime-engine/get-started-with-katalon-runtime-engine#id_10).
- `<your_API_Key>`: the API key verifies your credentials. The command-line options of API Key, including `apiKey=` and `apikey=` are both accepted. To learn more about API keys, you can refer to this document: [API key](/katalon-platform/administer/settings/katalon-api-key-in-katalon-testops).
:::
1. You can view the console log in Docker during the test.
    
  <img src="https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/jenkins-docker/docker-log.png" alt="docker screen" width="600" /> <br/>
    
2. To view your report files, you can go to this directory: `<your-project-folder>/Reports` or your third-party integration like Katalon TestOps, Azure DevOps, or qTest. Katalon Studio supports exporting test reports in **HTML**, **CSV**, **PDF**, and **JUnit**.
    

## <a id="id_3" class="anchor_top_offset"/>Proxy Configuration

    
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">If you need to configure proxies for Katalon Studio, you can   refer to this document: <a className="xref" href="/katalon-studio/execute-tests/katalon-runtime-engine/command-line-syntax-in-katalon-runtime-engine#id_5">Proxy     Options</a>.</p> 
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">These proxy options must be used with the <code className="ph codeph">--config</code>   parameter, for example:</p> 
              
<pre xmlns="http://www.w3.org/1999/xhtml" className="pre codeblock"><code>docker run -t --rm -v "$(pwd)":/tmp/project katalonstudio/katalon katalonc.sh -projectPath=/tmp/project -browserType="Chrome" -retry=0 -statusDelay=15 -testSuitePath="Test Suites/TS_RegressionTest" -apikey="&lt;your_API_key&gt;" --config -proxy.option=MANUAL_CONFIG -proxy.server.type=HTTP -proxy.server.address=192.168.1.221 -proxy.server.port=8888{"\n"}</code></pre> 
          
  

## <a id="id_4" class="anchor_top_offset"/>Prevent user permissions issue on your machine

<p xmlns="http://www.w3.org/1999/xhtml" className="p">You can run the test under the current user ID using the <code className="ph codeph">KATALON_USER_ID</code> environment variable. This helps avoid permission issues when accessing artifacts generated after the test execution. Follow these steps:</p> 
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol"><li className="li"><div className="p">Open <strong className="ph b">Terminal</strong>, then run <pre className="pre codeblock"><code>id -u $USER</code></pre>The result will tell you the current user ID. Here, the user ID is: 502</div><p className="p"><img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/katalon-docker-image/KS-DOCKER-userID.png")} width={700} alt="Current userID" /><br /><br /></p></li><li className="li"><p className="p">To execute the test with the current user ID, enter the following command line:</p><pre className="pre codeblock"><code>docker run -t --rm -e KATALON_USER_ID=&lt;the-current-userID&gt; -v "$(pwd)":/tmp/project katalonstudio/katalon katalonc.sh -projectPath=/tmp/project [Option1] [Option2] ... [OptionN]{"\n"}</code></pre><p className="p">For example, we want to run the test with the userID from step 1, we enter the command as follows:</p><pre className="pre codeblock"><code>docker run -t --rm -e KATALON_USER_ID=502 -v "$(pwd)":/tmp/project katalonstudio/katalon katalonc.sh -projectPath=/tmp/project [Option1] [Option2] ... [OptionN]{"\n"}</code></pre></li></ol> 

### <a id="concept-2613" class="anchor_top_offset"/>Execute Katalon Studio tests with Katalon Docker Image version below 7.2.1

<div xmlns="http://www.w3.org/1999/xhtml" className="note important note_important"><span className="note__title">Important:</span> <ul className="ul"><li className="li"><p className="p">Make sure you have Docker open while running the test.</p></li></ul></div>
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Inside your test project directory, input the following command:</p> 
<pre xmlns="http://www.w3.org/1999/xhtml" className="pre codeblock"><code>docker run -t --rm -v "$(pwd)":/katalon/katalon/source katalonstudio/katalon katalon-execute.sh [Option1] [Option2] ... [OptionN]{"\n"}</code></pre> 
<div xmlns="http://www.w3.org/1999/xhtml" className="note note note_note"><span className="note__title">Note:</span> <div className="p"><ul className="ul"><li className="li"><p className="p">All Katalon Studio console mode arguments are accepted except <code className="ph codeph">-runMode</code>, <code className="ph codeph">-reportFolder</code>, and <code className="ph codeph">-projectPath</code>. You can find more command line options at <a className="xref" href="/katalon-studio/execute-tests/katalon-runtime-engine/command-line-syntax-in-katalon-runtime-engine#concept-1437">Command Syntax</a></p></li></ul></div></div>
<div xmlns="http://www.w3.org/1999/xhtml" className="p"><table className="table anchor_top_offset" id="concept-2613__36670bf6-05dd-4382-8e0b-5531048bfa26"><caption /><colgroup><col style={{width: '33.33333333333333%'}} /><col style={{width: '66.66666666666666%'}} /></colgroup><thead className="thead"><tr className><th className="entry anchor_top_offset" id="concept-2613__36670bf6-05dd-4382-8e0b-5531048bfa26__entry__1">Command-line Option</th><th className="entry anchor_top_offset" id="concept-2613__36670bf6-05dd-4382-8e0b-5531048bfa26__entry__2">Description</th></tr></thead><tbody className="tbody"><tr className><td className="entry" headers="concept-2613__36670bf6-05dd-4382-8e0b-5531048bfa26__entry__1 concept-2613__36670bf6-05dd-4382-8e0b-5531048bfa26__entry__2 "><code className="ph codeph">katalon-execute.sh</code></td><td className="entry" headers="concept-2613__36670bf6-05dd-4382-8e0b-5531048bfa26__entry__1 concept-2613__36670bf6-05dd-4382-8e0b-5531048bfa26__entry__2 ">This command starts Katalon Studio and other necessary components.</td></tr><tr className><td className="entry" headers="concept-2613__36670bf6-05dd-4382-8e0b-5531048bfa26__entry__1 concept-2613__36670bf6-05dd-4382-8e0b-5531048bfa26__entry__2 "><code className="ph codeph">/katalon/katalon/source</code></td><td className="entry" headers="concept-2613__36670bf6-05dd-4382-8e0b-5531048bfa26__entry__1 concept-2613__36670bf6-05dd-4382-8e0b-5531048bfa26__entry__2 "><p className="p">The <code className="ph codeph">katalon-execute.sh</code> command looks for the test project inside this directory.</p><p className="p">If you don't want to use this command line, define the test project directory with the <code className="ph codeph">docker run -w</code> argument as follows:</p><p className="p"><code className="ph codeph">docker run -t --rm -v "$(pwd)":/tmp/source -w /tmp/source katalonstudio/katalon katalon-execute.sh [Option1] [Option2] ... [OptionN]</code></p></td></tr></tbody></table></div>

## <a id="concept-2870" class="anchor_top_offset"/>Known limitations for ARM64-based platforms

<p xmlns="http://www.w3.org/1999/xhtml" className="shortdesc">Starting from Katalon Studio version 10.0.0, Katalon Docker Image supports ARM64 platforms, including macOS (M1, M2) and Linux (Ubuntu ARM64). However, a few limitations exist when working with these platforms:</p> 
<div xmlns="http://www.w3.org/1999/xhtml" className="p"><ul className="ul"><li className="li"><p className="p">Docker slim tags (for example, <code className="ph codeph">9.6.0-slim</code> and <code className="ph codeph">9-latest-slim</code>) aren't supported yet for ARM64.</p></li><li className="li"><p className="p">Chrome and Edge Chromium browsers aren't supported on ARM64 platforms. Executing tests with Chrome and Edge Chromium on these Docker images isn't supported yet.</p></li></ul></div>
    

## <a id="id_6" class="anchor_top_offset"/>See also

    
      
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul">   <li className="li">     <a className="xref" href="#">Integrate       Jenkins on Docker hosted in Ubuntu</a>   </li>   <li className="li">     <a className="xref" href="#">Integrate       Jenkins Pipeline (Jenkinsfile) with Katalon Studio Docker       Image</a>   </li> </ul> 
    
  
