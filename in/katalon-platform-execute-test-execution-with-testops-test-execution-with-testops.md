---
title: Test execution with TestOps (Legacy)
---
import Reusable from '@site/src/reusable/Reusable.mdx';

<Reusable />

<p xmlns="http://www.w3.org/1999/xhtml" className="p">In Katalon TestOps, you can set up a remote execution to run tests in several environments.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">The setup for execution with <span className="ph">TestOps</span> includes:</p> 
<div xmlns="http://www.w3.org/1999/xhtml" className="p"><ol className="ol"><li className="li">Create a test environment.</li><li className="li">Create a script repository.</li><li className="li">Schedule test runs.</li></ol></div>

## <a id="id_1" class="anchor_top_offset"/>Create a test environment

<p xmlns="http://www.w3.org/1999/xhtml" className="p">A test environment connects your machine with Katalon TestOps to   activate a remote execution.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">You can define which machine or machines execute the remote test   runs by configuring a test environment in Katalon TestOps.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Katalon TestOps offers the following options:</p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">     <a className="xref" href="/katalon-platform/execute/test-execution-with-testops/local-test-environments/create-a-local-test-environment-with-an-agent">Create       a Local Test Environment with an Agent</a>.</li><li className="li">     <a className="xref" href="/katalon-platform/execute/test-execution-with-testops/set-up-docker-test-environments-for-testops">Set       up an Agent to execute tests in a Docker Environment</a>.</li><li className="li">     <a className="xref" href="/katalon-platform/execute/test-execution-with-testops/set-up-kubernetes-test-environments-for-testops">Create       a Kubernetes Test Environment</a>.</li><li className="li">     <a className="xref" href="/katalon-platform/execute/test-execution-with-testops/set-up-circleci-test-environments-for-testops">Create       a CircleCI Test Environment</a>.</li></ul> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Once you have created a test environment, you can upload tests   to a script repository in TestOps for test planning.</p> 

## <a id="id_2" class="anchor_top_offset"/>Set up a script repository

<p xmlns="http://www.w3.org/1999/xhtml" className="p">A script repository stores test scripts for test executions. You can manage your test scripts in Katalon TestOps and decide the execution schedule (test planning) and execution environment (the test environment you have created). See: ​ <a className="xref" href="/katalon-platform/organize/configure-a-git-repository-in-testops">Upload Test Scripts from a Git Repository</a> ​ .</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">With a set-up test environment and Git repository, your tests are ready for execution in Katalon TestOps.</p> 

## <a id="id_3" class="anchor_top_offset"/>Schedule test runs

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Planning test executions allows you to keep track of testing progress and monitor test results.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">You can configure a schedule for automatic test runs or execute tests manually in Katalon TestOps.</p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">For automatic test executions, see: <a className="xref" href="/katalon-platform/execute/test-execution-with-testops/schedule-test-runs-in-testops">Schedule Test Runs</a>.</li><li className="li">For manual test executions, see: <a className="xref" href="/katalon-platform/execute/test-execution-with-testops/schedule-test-runs-in-testops#id">Execute Test Runs manually</a>.</li></ul> 
