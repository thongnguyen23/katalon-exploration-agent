---
hide_title: true
title: TestCloud execution time in Katalon Studio
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="concept-8700" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>TestCloud execution time in Katalon Studio

<p xmlns="http://www.w3.org/1999/xhtml" className="p">When using <span className="ph">TestCloud</span> in <span className="ph">Katalon Studio</span>, you may encounter slow test execution time. For example, opening a browser window can take a few seconds. Execution time with <span className="ph">TestCloud</span> in <span className="ph">Katalon Studio</span> is usually longer than in <span className="ph">TestOps</span> due to the following factors:</p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p"><span className="ph">TestCloud</span> devices are hosted in several regions with multiple Internet hops that  increase latency.</p></li><li className="li"><p className="p"><span className="ph">Katalon Studio</span> and <span className="ph">Katalon Runtime Engine</span> sequentially send Selenium commands to <span className="ph">TestCloud</span> using the Remote WebDriver protocol. This can increase execution time if the script or custom keywords contain many individual steps.</p></li></ul> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">The following diagram compares the execution models of <span className="ph">TestCloud</span>: local execution, <span className="ph">TestCloud</span>-<span className="ph">Katalon Studio</span>, and <span className="ph">TestCloud</span>-<span className="ph">TestOps</span>.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" src={useBaseUrl("/ebc9b1d0-9407-11ee-ab4f-0242c7a41fd4/test-execution-models-comparison.png")} alt="TestCloud execution models" /></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">The execution model of <span className="ph">TestCloud</span> with <span className="ph">TestOps</span> achieves the same network performance as in local machine, as most components are hosted in Katalon network. This model also removes the need to maintain an online machine to host <span className="ph">Katalon Studio</span> or <span className="ph">Katalon Runtime Engine</span>.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">To remove latency, we recommend uploading your tests to <span className="ph">TestOps</span> and schedule them with <span className="ph">TestCloud</span>.</p> 
