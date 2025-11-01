---
hide_title: true
title: Mobile app testing with remote devices
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="id_mobile-testing-apps-cloud-devices" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Mobile app testing with remote devices

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Katalon Studio supports executing a Mobile script on both remote and custom cloud devices. You can test your mobile applications on custom cloud devices such as Sauce Labs or BrowserStack.</p> 
<div xmlns="http://www.w3.org/1999/xhtml" className="note note note_note"><span className="note__title">Note:</span> <ul className="ul"><li className="li">The Mobile Record and Spy utilities are only available on remote devices.</li><li className="li">Generate Command dialog does not require the <span className="ph uicontrol">Remote Server URL</span> and <span className="ph uicontrol">Remote Server Type</span>. Katalon Studio uses the current settings of Remote execution.</li></ul></div>

## <a id="task-6367" class="anchor_top_offset"/>Configure a remote device

<section xmlns="http://www.w3.org/1999/xhtml" className="section context">To set up a remote device for mobile app testing, do as follows:</section> 
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol steps"><li className="li step stepexpand"><span className="ph cmd">Go to <span className="ph uicontrol">Spy Mobile</span> or <span className="ph uicontrol">Record Mobile</span> &gt; <span className="ph uicontrol">Remote Devices</span>.</span></li><li className="li step stepexpand"><span className="ph cmd">In the opened dialog, click <span className="ph uicontrol">Edit</span>.</span><div className="itemgroup stepresult">A <span className="ph uicontrol">Project Settings</span> dialog appears.<p className="p"><img className="image" width={700} src={useBaseUrl("/08e9fac0-94b4-11ee-ab4f-0242c7a41fd4/ks-910-config-remote-device.png")} /></p><p className="p">Alternatively, you can go to <span className="ph uicontrol">Project</span> &gt; <span className="ph uicontrol">Settings</span> &gt; <span className="ph uicontrol">Desired Capabilities</span> and select <span className="ph uicontrol">Remote</span>.</p></div></li><li className="li step stepexpand"><span className="ph cmd">Enter the <span className="ph uicontrol">Remote server URL</span>,  select the <span className="ph uicontrol">Remote server type</span> and input the <span className="ph uicontrol">Desired Capabilities</span> for your remote device.</span></li><li className="li step stepexpand"><span className="ph cmd">Click <span className="ph uicontrol">Apply and Close</span>.</span></li></ol> 

## <a id="id_5" class="anchor_top_offset"/>Enter Application Path/ID

<p xmlns="http://www.w3.org/1999/xhtml" className="p"> <span className="ph uicontrol">Application Path/ID</span> is the path to the downloadable link of the app or the ID of the application file (<code className="ph codeph">.apk</code>; <code className="ph codeph">.ipa</code>) after being uploaded to the cloud. For example, the application ID of Kobiton is <kbd className="ph userinput">kobiton-store:23616</kbd>.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" height={210} src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/docs/mobile-testing-cloud-devices/2-AppID.png")} width={393} /><br /><br /></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">If the <span className="ph uicontrol">Application Path/ID</span> is not specified, Katalon Studio will start the application on the device defined in the <span className="ph uicontrol">Desired Capabilities</span> settings.</p> 
