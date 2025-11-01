---
title: Use Katalon Report Uploader (Legacy)
---
import useBaseUrl from '@docusaurus/useBaseUrl';
import Reusable from '@site/src/reusable/Reusable.mdx';

<Reusable />

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Katalon Report Uploader is a utility to upload reports to Katalon TestOps. The utility supports JUnit, Katalon Studio, and Katalon Recorder report format. It can be used with CLI, Docker, GitHub Action, and other CIs.</p> 

## <a id="task-2323" class="anchor_top_offset"/>Usage in CLI

<section xmlns="http://www.w3.org/1999/xhtml" className="section context">Follow these steps to use Katalon Report Uploader in CLI.</section> 
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol steps"><li className="li step stepexpand"><span className="ph cmd">Download <a className="xref j-external-link" href="https://github.com/katalon-studio/report-uploader/releases" target="_blank">Reports Uploader</a> and install <a className="xref j-external-link" href="https://www.java.com/en/download/manual.jsp" target="_blank">Java JRE</a> and <a className="xref j-external-link" href="https://www.oracle.com/technetwork/java/javase/downloads/index.html" target="_blank">Java JDK</a>.</span></li><li className="li step stepexpand"><span className="ph cmd">Get the path to your Katalon report folders, e.g. <code className="ph codeph">C:\Users\alex\Katalon Studio\Web Sample\Reports\Test Suite\20190523_143946</code>.</span></li><li className="li step stepexpand"><span className="ph cmd">Open command prompt and paste in the command:</span><div className="itemgroup info">       <pre className="pre codeblock"><code>java -jar katalon-report-uploader-0.0.5.jar --projectId=3 --path="d:\katalon-reports" --email=admin@mail.me --password=admin --type=katalon --push-to-xray=true</code></pre>       <ul className="ul"><li className="li"> <code className="ph codeph">projectId</code>: Your project ID in Katalon TestOps.</li><li className="li"> <code className="ph codeph">path</code>: The local path of Katalon Studio Reports folder identified in step 2.</li><li className="li"> <code className="ph codeph">email</code>: The email registered for your Katalon account. If an API Key is used as <code className="ph codeph">password</code>, this field is not required.</li><li className="li"> <code className="ph codeph">password</code>: The password used for signing in Katalon TestOps or an API Key of that account. Using API Key is recommended as it will not expose your password.</li><li className="li"> <code className="ph codeph">type</code>: One of the values "katalon", "junit", or "katalon_recorder".</li><li className="li"> <code className="ph codeph">server</code>: (<strong className="ph b">Optional</strong>) The Katalon TestOps server endpoint, by default it is <code className="ph codeph">https://analytics.katalon.com</code>.</li><li className="li"><code className="ph codeph">--push-to-xray=true</code> (optional): If your TestOps project is integrated with Xray test management, this option enables pushing the test results to Xray.</li></ul>     </div></li></ol> 
<div xmlns="http://www.w3.org/1999/xhtml" className="li stepsection">Alternatively, you can use the TestOps interface to specify the parameters.</div>
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol steps" start={4}><li className="li step stepexpand"><span className="ph cmd">Open TestOps dashboard and go to <span className="ph uicontrol">Settings</span> &gt; <span className="ph uicontrol">Integrations </span> &gt; <span className="ph uicontrol">Report Uploader</span>.</span><div className="itemgroup info"><img className="image" width={700} src={useBaseUrl("/53e01194-ea1d-4de9-b738-4c50b63abf8f/TestOps_integrations_report_uploader.png")} alt="TestOps report uploader" /></div></li><li className="li step stepexpand"><span className="ph cmd">Follow the on-screen instructions to produce the command.</span></li></ol> 

## <a id="id_2" class="anchor_top_offset"/>Usage for Docker


### Environment variables

<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <code className="ph codeph">SERVER</code> The URL of Katalon TestOps. Default   <code className="ph codeph">https://analytics.katalon.com</code>.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <code className="ph codeph">EMAIL</code> The email registered for your Katalon   account.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <code className="ph codeph">PASSWORD</code> The password used for signing in Katalon   TestOps or an API Key.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <code className="ph codeph">PROJECT_ID</code> Your project ID in Katalon TestOps.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <code className="ph codeph">TYPE</code> One of the values including "katalon",   "junit", or "katalon_recorder".</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <code className="ph codeph">REPORT_PATH</code> The path of the report folder. The   physical report folder should be mounted as a Docker volume   first.</p> 

### Example

<pre xmlns="http://www.w3.org/1999/xhtml" className="pre codeblock"><code>docker run -t --rm -v &lt;path&gt;:/katalon/report -e PASSWORD=&lt;APIKey&gt; -e PROJECT_ID=&lt;ProjectId&gt;-e TYPE=katalon -e REPORT_PATH=/katalon/report katalonstudio/report-uploader:0.0.8</code></pre> 

## <a id="id_5" class="anchor_top_offset"/>Usage for Continuous Integration (CI) systems


### Jenkins Pipeline

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Example on our GitHub repository: <a className="xref j-external-link" href="https://github.com/katalon-studio-samples/report-uploader-sample/blob/master/Jenkinsfile" target="_blank">Jenkinsfile</a>. </p> 

### GitHub action

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Marketplace Listing on  GitHub: <a className="xref j-external-link" href="https://github.com/marketplace/actions/katalon-report-uploader" target="_blank">katalon-report-uploader</a>.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Example:</p> 
<pre xmlns="http://www.w3.org/1999/xhtml" className="pre codeblock"><code> - name: Katalon Report Uploader{"\n"}{"    "}uses: katalon-studio/report-uploader@v0.0.7.11{"\n"}{"    "}env:{"\n"}{"      "}PASSWORD: ${"{"}{"{"} secrets.KATALON_API_KEY {"}"}{"}"}{"\n"}{"      "}PROJECT_ID: 50236{"\n"}{"      "}TYPE: junit{"\n"}{"      "}REPORT_PATH: ${"{"}{"{"} github.workspace {"}"}{"}"}/junit-report-sample</code></pre> 

### CircleCI

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Example on our GitHub repository:   <a className="xref j-external-link" href="https://github.com/katalon-studio-samples/report-uploader-sample/blob/master/.circleci/config.yml" target="_blank">circleci/config.yml</a>.</p> 

### GitLab CI

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Example on our GitHub repository: <a className="xref j-external-link" href="https://github.com/katalon-studio-samples/report-uploader-sample/blob/master/.gitlab-ci.yml" target="_blank">.gitlab-ci.yml</a>.</p> 

### AWS Codebuild

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Example on our GitHub repository: <a className="xref j-external-link" href="https://github.com/katalon-studio-samples/report-uploader-sample/blob/master/buildspec.yml" target="_blank">buildspec.yml</a>.</p> 

### Azure DevOps Pipeline

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Example on our GitHub repository:   <a className="xref j-external-link" href="https://github.com/katalon-studio-samples/report-uploader-sample/blob/master/azure-pipelines.yml" target="_blank">azure-pipelines.yml</a>.</p> 
