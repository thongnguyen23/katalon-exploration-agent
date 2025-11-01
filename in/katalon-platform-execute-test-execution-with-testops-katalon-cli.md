---
title: Katalon CLI (Legacy)
---
import useBaseUrl from '@docusaurus/useBaseUrl';
import Reusable from '@site/src/reusable/Reusable.mdx';

<Reusable />

<p xmlns="http://www.w3.org/1999/xhtml" className="p">The Katalon Command-line Interface (CLI) Docker Image allows you to trigger test execution from existing test schedules on TestOps. You can use this image to integrate with your desired CI/CD pipeline and trigger execution upon code changes.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Katalon CLI is available on Docker Hub: <a className="xref j-external-link" href="https://hub.docker.com/r/katalonstudio/katalon-cli" target="_blank">Katalon CLI</a>.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">This guide lists out the available configurations and sample use cases with the image.</p> 

## Prerequisites

<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">A valid TestOps account with the necessary permissions to trigger executions.</p></li><li className="li"><p className="p">Access to a compatible CI/CD environment with Docker installed.</p></li></ul> 

## Usage

<div xmlns="http://www.w3.org/1999/xhtml" className="p">With Docker installed and running, you can start triggering a schedule.<pre className="pre codeblock"><code>docker run katalonstudio/katalon-cli schedule &lt;parameters&gt;</code></pre></div>
<div xmlns="http://www.w3.org/1999/xhtml" className="p"><strong className="ph b">Parameters</strong><ul className="ul"><li className="li"><p className="p"><code className="ph codeph">--api-key</code>: your Katalon API key, see: <a className="xref" href="/katalon-platform/administer/settings/katalon-api-key-in-katalon-testops">Katalon API key</a>.</p></li><li className="li"><p className="p"><code className="ph codeph">--username</code> and <code className="ph codeph">--password</code>: the username and password of your TestOps account. </p></li><li className="li"><p className="p"><code className="ph codeph">--project-id</code>: the ID of the project that contains your test schedule. This parameter is not required when using<code className="ph codeph">IDS_EXACT_MATCHES</code> for <code className="ph codeph">operator</code>.</p></li><li className="li"><p className="p"><code className="ph codeph">--operator=&lt;IDS_EXACT_MATCHES | NAME_CONTAINS | NAME_STARTS_WITH | NAME_ENDS_WITH&gt;</code>: the operator to filter the schedule, by id or by naming pattern.</p></li><li className="li"><p className="p"><code className="ph codeph">--values</code>: the value that corresponds with the operator in use.</p></li></ul></div>
<div xmlns="http://www.w3.org/1999/xhtml" className="p"><strong className="ph b">Environment variables</strong>: You can use environment variables instead of parameters.<ul className="ul"><li className="li">API_KEY</li><li className="li">USERNAME</li><li className="li">PASSWORD</li><li className="li">PROJECT_ID</li><li className="li">OPERATOR</li><li className="li">VALUES</li></ul></div>

## Trigger command for TestOps schedules

<p xmlns="http://www.w3.org/1999/xhtml" className="p">To trigger an existing schedule on TestOps, you need to retrieve the schedule information, specifically the ID of your TestOps project and the ID of the test schedule.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">In your TestOps project, go to <span className="ph uicontrol">Executions</span> &gt; <span className="ph uicontrol">Schedules</span>, and select the desired test schedule. <img className="image" width={700} src={useBaseUrl("/98c05fd0-bfee-11ee-ac6d-0242c7a41fd4/TestOps_schedules.png")} /></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">You can find the project ID and schedule ID in the browser's address bar. For example, in the URL <code className="ph codeph">https://testops.katalon.io/team/&lt;team-id&gt;/project/1366723/grid/plan/618831/job</code>, <code className="ph codeph">1366723</code> is the project ID and <code className="ph codeph">618831</code> is the schedule ID.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">The following are some sample commands to trigger an execution from the schedule:</p> 
<div xmlns="http://www.w3.org/1999/xhtml" className="p">Trigger an execution with Katalon API key and schedule ID:<pre className="pre codeblock"><code>docker run katalonstudio/katalon-cli schedule trigger --api-key=xxx --operator=IDS_EXACT_MATCHES --values=618831</code></pre></div>
<div xmlns="http://www.w3.org/1999/xhtml" className="p">Trigger an execution with username / password and name pattern matching (<code className="ph codeph">--project-id</code> is required). This command triggers all schedules whose names contain the word "multiple".<pre className="pre codeblock"><code>docker run katalonstudio/katalon-cli schedule trigger --username=john.doe@testing.com --password=password --project-id=1366723 --operator=NAME_CONTAINS --values="multiple"</code></pre></div>
