---
hide_title: true
title: How to resolve elapsed time mismatched between the Object Repositories and
  the Test Cases?
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="troubleshooting-2548" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>How to resolve elapsed time mismatched between the Object Repositories and the Test Cases?

<section xmlns="http://www.w3.org/1999/xhtml" className="section condition"><p className="p">There is a difference between elapsed time between the two methods of simulating a HTTP request in <span className="ph">Katalon Studio</span>. <img className="image" src={useBaseUrl("/46abee00-7d5c-11ee-8403-0242c7a41fd4/KS_-_difference_in_elapsed_time_.jpeg")} alt="difference in elapsed time" /></p></section> 
<div xmlns="http://www.w3.org/1999/xhtml" className="bodydiv troubleSolution"><section className="section cause"><p className="p"><span className="ph">Katalon Studio</span> use Java HTTPClient as the library to simulate HTTP request. When running a test case or test suite, <span className="ph">Katalon Studio</span> will create a different Java process. When combining with HTTPClient, the first request always takes longer to establish and keep the connection alive, but the subsequent request connection's elapsed time will be back to normal.</p></section><section className="section remedy"><div className="li step p"><span className="ph cmd">If you don't want to eliminate the elapsed time difference, send a temporary request at the beginning of test cases or test suite in a <a className="xref" href="/katalon-studio/create-test-cases/test-fixtures-and-test-listeners-test-hooks-in-katalon-studio#task-2997">test listener</a> and track the response's elapsed time in the main test script.</span></div></section></div>
