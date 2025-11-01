---
hide_title: true
title: Quality reports
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="id_dashboard-quality" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Quality reports


## Overview

<p xmlns="http://www.w3.org/1999/xhtml" className="p">The <span className="ph uicontrol">Quality</span> dashboard allows you to monitor the quality of test cases based on their execution history.</p> 
    
<p xmlns="http://www.w3.org/1999/xhtml" className="p">The quality is measured by grouping the number of executed test cases in each flakiness category (flakiness level: 0% - 5%, 5% - 10%, …, 95% - 100%).</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" src={useBaseUrl("/8e01f750-22b2-11ed-9930-0242fe3e4a3f/KT-JULY22-dashboard-quality.png")} alt="View quality reports" /></p> 

## Insights

<p xmlns="http://www.w3.org/1999/xhtml" className="p">The flakiness of a test case is calculated based on the number of failed/passed statuses the test case has.</p> 
    
<p xmlns="http://www.w3.org/1999/xhtml" className="p">A flakiness probability of over 50% means that the quality of this test case is bad since it performs inconsistently over time, which prompts further investigation to find the root cause to resolve it immediately.</p> 
    
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Meanwhile, if there is an incredible number of executed test cases with less than 50% of flakiness, it could mean that the quality of test cases is good enough.</p> 
    
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Since the quality of test cases tells you how good/bad your product is, predicting the efforts to spend on debugging or addressing the problem of the bad test quality, you could plan your production cycle accordingly to make sure that the product deployment would still meet the timeline you and your team expect.</p> 
