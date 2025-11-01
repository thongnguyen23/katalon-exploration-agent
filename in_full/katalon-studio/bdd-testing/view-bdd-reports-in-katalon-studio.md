---
hide_title: true
title: View BDD reports in Katalon Studio
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="id_9" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>View BDD reports in Katalon Studio

<p xmlns="http://www.w3.org/1999/xhtml" className="p">After execution, there are two places for you to view BDD reports: in Katalon Studio and in Katalon TestOps.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">There is no custom report for executing feature file. Katalon Studio uses only generated Cucumber reports for test suite and test suite collection execution, in which the test cases contain the Cucumber features file.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">The generated Cucumber reports are located in the same folder of Katalon Studio report folder. In <span className="ph uicontrol">Tests Explorer</span>, right-click at the desired <span className="ph uicontrol">Report</span> folder and choose <span className="ph uicontrol">Open Containing Folder</span>. Katalon Studio redirects you to the local folder where Cucumber reports are stored. </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Katalon Studio generates Cucumber reports for each feature file and in three formats: JSON, XML, HTML.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" width={750} src={useBaseUrl("/96345ad0-22b2-11ed-9930-0242fe3e4a3f/ks-840-cucumber-report-folder.png")} alt="report folder" /></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">You can also view BDD test reports in Katalon TestOps. By default, the BDD test report feature on Katalon TestOps is disabled to avoid mixing the BDD and Katalon Studio formatted data. To enable the feature, you can refer to this guide: <a className="xref" href="/katalon-platform/analyze/reports/view-test-reports/view-bdd-test-results-in-testops">View BDD Test Results in Katalon TestOps</a>.</p> 
