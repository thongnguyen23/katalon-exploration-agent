---
hide_title: true
title: Headless mode produces a blank white window in Chrome version 129
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="troubleshooting-tstl4rd8" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Headless mode produces a blank white window in Chrome version 129

<section xmlns="http://www.w3.org/1999/xhtml" className="section condition"><p className="p">When running tests in headless mode with Chrome version 129, a blank white window matching the browser's size may occasionally appear.</p></section> 
<div xmlns="http://www.w3.org/1999/xhtml" className="bodydiv troubleSolution"><section className="section cause"><p className="p">This issue is caused by a known bug in Chrome version 129. As of now, Google has not provided a timeline or plan to resolve this bug in future updates.</p><p className="p">To work around this issue, follow these steps:</p></section><section className="section remedy"><ol className="ol steps"><li className="li step stepexpand"><span className="ph cmd">Go to <span className="ph menucascade"><span className="ph uicontrol">Project</span><abbr title="and then"> &gt; </abbr><span className="ph uicontrol">Settings</span><abbr title="and then"> &gt; </abbr><span className="ph uicontrol">Desired Capabilities</span><abbr title="and then"> &gt; </abbr><span className="ph uicontrol">Web UI</span><abbr title="and then"> &gt; </abbr><span className="ph uicontrol">Chrome (headless)</span></span>.</span></li><li className="li step stepexpand"><span className="ph cmd">Add the following parameter: <code className="ph codeph">--window-position=-10000,-10000</code></span><div className="itemgroup info"><img className="image" width={700} src={useBaseUrl("/484e29fc-861a-4c87-943c-258264a85672/hide-blank-window.png")} /></div><div className="itemgroup stepresult">This setting will hide the blank white window when running tests in headless mode.</div></li></ol></section></div>
