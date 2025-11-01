---
hide_title: true
title: Platform coverage reports
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="id_dashboard-platform-coverage" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Platform coverage reports


## Requirements

<div xmlns="http://www.w3.org/1999/xhtml" className="p"><ul className="ul"><li className="li"><p className="p">You have subscribed to <span className="ph">Ultimate</span>   plan. To request for a trial, refer to: <a className="xref" href="/katalon-platform/administer/katalon-platform-packages/katalon-trial-plan">Katalon Trial Plan</a>.</p></li></ul></div>

## Overview

<p xmlns="http://www.w3.org/1999/xhtml" className="p">The <span className="ph uicontrol">Platform Coverage</span> report shows the coverage of test runs or test results in each corresponding operating system and browser. You can filter the profile and specify a period to check the test coverage in your project.</p> 
<div xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" src={useBaseUrl("/8dfdffb0-22b2-11ed-9930-0242fe3e4a3f/KT-JULY22-dashboard-platform-coverage.png")} alt="View platform coverage" /><div className="note note note_note"><span className="note__title">Note:</span> <ul className="ul"><li className="li"><p className="p">The default period is the last 6 months (compared to the current date).</p></li></ul></div></div>

## Insights

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Testing your software/application on different platforms is vital to see if it works accordingly. Hence this report offers you a comprehensive report of all platform performance.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">The report offers you the following insights:</p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">You can understand how many test runs have been executed on each platform based on the size of each dot. Consequently, you know which platform has more or less test executions than the other platforms.</li><li className="li">You can figure out the percentage of failed/passed test runs on each platform based on the color of each dot. Consequently, you know which platform has more or less failed/passed tests than the other platforms.</li></ul> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">You then know if your project is going in the right direction through such analytics. Your team could also learn to focus on the prioritized platforms in accordance with the initial plan.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">For example, within the default 6-month period and if you select the <span className="ph uicontrol">By Test Run</span> option, and the report is represented as follows:</p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li">One green dot in the "Mac OS &amp; Chrome" platform.</li><li className="li">One orange dot in the "Linux &amp; Firefox" platform.</li><li className="li">The size of the green dot is more significant than the orange one.</li></ul> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Then the analytics provides you with the following information:</p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">Tests are run better (e.g., more <em className="ph i">passed</em> tests and with a consistent result) on Mac OS &amp; Chrome than on Linux &amp; Firefox.</p></li><li className="li"><p className="p">The quality of test runs on Mac OS &amp; Chrome is better than Linux &amp; Firefox.</p></li><li className="li"><p className="p">There are more tests on Mac OS &amp; Chrome and they are of a good quality (because the dot is green and bigger in size) while the quality is not so good on Linux &amp; Firefox (because it's orange) and the team should focus on creating more tests and fixing bugs for tests on Linux &amp; Firefox platform.</p></li></ul> 
