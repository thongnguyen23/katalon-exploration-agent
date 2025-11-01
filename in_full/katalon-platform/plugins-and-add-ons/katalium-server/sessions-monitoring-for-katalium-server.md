---
hide_title: true
title: Sessions Monitoring for Katalium Server
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="id" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Sessions Monitoring for Katalium Server

:::info notes
This feature is only available in Grid mode.
:::
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Katalium Grid Hub will automatically capture screenshots of   browsers started by its Grid Node. This will help you monitor   on-going sessions and debug test execution errors. All sessions are   stored in the directory   <code className="ph codeph">&lt;user_home&gt;/katalon-selenium</code>.</p> 
## <a id="id_1" class="anchor_top_offset"/>View all sessions
    
<p xmlns="http://www.w3.org/1999/xhtml" className="p">To see the list of all sessions, go to   <code className="ph codeph">http://hub_grid:4444/grid/admin/KatalonConsole/index.html</code>.</p> 
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">For example:</p> 
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalium-server/docs/view-session-details/1-view-session.png")} /><br /><br /> </p>  

## <a id="id_2" class="anchor_top_offset"/>View screenshots of each session
<p xmlns="http://www.w3.org/1999/xhtml" className="p">In the list of sessions, select the session you want to view   screenshots.</p> 
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">   <img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalium-server/docs/view-session-details/2-session-details.png")} /><br /><br /> </p> 

## <a id="id_3" class="anchor_top_offset"/>Clean up old sessions   
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Katalium Grid Hub schedules a daily job to clean up sessions   older than two months.</p> 
    
  
