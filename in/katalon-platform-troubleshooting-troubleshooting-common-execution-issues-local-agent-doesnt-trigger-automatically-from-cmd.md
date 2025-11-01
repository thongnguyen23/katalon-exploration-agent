---
hide_title: true
title: Local Agent doesn't trigger automatically from CMD
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="troubleshooting-3204" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Local Agent doesn't trigger automatically from CMD

<section xmlns="http://www.w3.org/1999/xhtml" className="section condition"><p className="p">When you schedules a test run and starts a local agent, the agent  freezes after response with status 200 without running the execution. You have to trigger the execution manually by clicking or pressing enter on the CMD.<img className="image" src={useBaseUrl("/4491d560-faeb-11ed-878a-0242c7a41fd4/Execution_-_Local_agent_status_200.jpeg")} alt="Local agent status 200" /></p></section> 
<div xmlns="http://www.w3.org/1999/xhtml" className="bodydiv troubleSolution"><section className="section cause"><p className="p">The issue stems from a new feature of the windows 10 console. Under the default configuration, whenever you click on a command window in windows 10, it immediately pauses the application process when it attempts to write to the console. The command window has gone into "selection" mode because QuickEditMode has been disabled. We need to enable the QuickEdit Mode.</p></section><section className="section remedy"><ol className="ol steps"><li className="li step"><span className="ph cmd">Right-click on the top left bar, then select <span className="ph uicontrol">Default</span>.<img className="image" src={useBaseUrl("/44601700-faeb-11ed-878a-0242c7a41fd4/select_Defaults.jpeg")} alt="select Defaults" /></span></li><li className="li step"><span className="ph cmd">Select and check on QuickEdit Mode, then select <span className="ph uicontrol">OK</span>.<img className="image" src={useBaseUrl("/44685460-faeb-11ed-878a-0242c7a41fd4/enable_QuickEdit_Mode.jpeg")} alt="enable QuickEdit Mode" /></span></li><li className="li step"><span className="ph cmd">Restart the CMD again and start running the execution.</span></li></ol></section></div>
