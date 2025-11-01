---
title: Auto-distributed executions (Legacy)
---
import useBaseUrl from '@docusaurus/useBaseUrl';
import Reusable from '@site/src/reusable/Reusable.mdx';

<Reusable />

## <a id="id_1" class="anchor_top_offset"/>How it works

<div xmlns="http://www.w3.org/1999/xhtml" className="note important note_important"><span className="note__title">Important:</span> <ul className="ul"><li className="li">Katalon Runtime Engine</li><li className="li">Agent version 1.7.0 onwards</li><li className="li">At least 2 active Agents</li></ul></div>
<p xmlns="http://www.w3.org/1999/xhtml" className="p">In Katalon TestOps, you can execute tests in parallel. During parallel execution, test runs are automatically load-balanced. This means that each time a test run starts, the test run is distributed to an available and active local test environment, minimizing execution time.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">When a test run is executed, the test sessions will be assigned to the previously configured Agents in this order of priority:</p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">Idle Agents</li><li className="li">Agents that have not exceeded their Threshold</li><li className="li">Agents with the least number of queued Test Runs</li></ul> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">When an Agent completes a test run session, queued jobs that were first assigned to other Agents can be automatically reassigned to this Agent for immediate execution.</p> 

## <a id="id_2" class="anchor_top_offset"/>Configure Auto-distributed executions

<ol xmlns="http://www.w3.org/1999/xhtml" className="ol"><li className="li"><p className="p">To enable Auto-distributed executions, make sure that you have at least 2 active Agents. You can learn how to set-up Agents here: <a className="xref" href="/katalon-platform/execute/test-execution-with-testops/local-test-environments/create-a-local-test-environment-with-an-agent">Create a Local Test Environment</a>.</p></li><li className="li"><p className="p">Make sure that your test suite collection is configured for parallel execution. If not, you can follow these steps: <a className="xref" href="/katalon-platform/execute/test-execution-with-testops/local-test-environments/run-multiple-test-suites-in-parallel-with-agents">Run multiple Test Suites in Parallel</a>.</p></li><li className="li"><p className="p">Create a test schedule and assign your test run types to those Agents. Learn more: <a className="xref" href="/katalon-platform/execute/test-execution-with-testops/schedule-test-runs-in-testops#task-7544">Schedule Test Runs</a>.</p><div className="note tip note_tip"><span className="note__title">Tip:</span> <p className="p">When configuring multiple rest run types, test run types must share a minimum of 1 mutual Agent for distributed execution. In other words, assign test run types to multiple, overlapping Agents.</p></div></li><li className="li"><p className="p">Activate your Agents before the scheduled test run time.</p></li><li className="li"><p className="p">Once the test run types execute, the test sessions of these test run types are assigned to the previously configured agents automatically.</p></li></ol> 
