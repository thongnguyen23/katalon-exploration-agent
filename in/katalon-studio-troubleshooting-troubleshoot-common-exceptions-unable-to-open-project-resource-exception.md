---
hide_title: true
title: 'Unable to open project: Resource Exception'
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="troubleshooting-7676" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Unable to open project: Resource Exception

<section xmlns="http://www.w3.org/1999/xhtml" className="section condition"><div className="p">You encounter the following message in Katalon Studio: <pre className="pre codeblock"><code>Unable to open project: Resource Exception</code></pre>This issue might happen because Katalon Studio fails to read the project description file (<span className="ph filepath">.project</span>).</div></section> 
<div xmlns="http://www.w3.org/1999/xhtml" className="bodydiv troubleSolution"><section className="section remedy"><ol className="ol steps"><li className="li step stepexpand"><span className="ph cmd">Navigate to  your project folder.</span></li><li className="li step stepexpand"><span className="ph cmd">Delete the <span className="ph filepath">.project</span> file.</span><div className="itemgroup info"><img className="image" width={500} src={useBaseUrl("/8411e2f0-9df0-11ed-998d-0242cfbc79b5/project-file.png")} /></div></li><li className="li step stepexpand"><span className="ph cmd">Open your project in Katalon Studio again.</span><div className="itemgroup stepresult">Katalon Studio  opens the project successfully.</div></li></ol></section></div>
