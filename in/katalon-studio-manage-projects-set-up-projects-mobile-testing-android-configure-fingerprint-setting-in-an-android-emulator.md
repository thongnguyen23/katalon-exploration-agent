---
hide_title: true
title: Configure fingerprint setting in an Android emulator
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="task-3592" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/> Configure fingerprint setting in an Android emulator

<section xmlns="http://www.w3.org/1999/xhtml" className="section context"><div className="p"><ul className="ul"><li className="li"><p className="p">Here is the <a className="xref j-external-link" href="https://drive.google.com/file/d/1KTWwUFEeHuC0OUZjm_MQ4V1G5osQVCsy/view?usp=sharing" target="_blank">sample app</a> for this guide.</p></li><li className="li"><p className="p">You can also see this <a className="xref j-external-link" href="https://drive.google.com/file/d/1OgEnrctf5l9daqn2T9UV_YleQal7qhcf/view?usp=sharing" target="_blank">video</a> for demonstration. </p></li></ul></div> </section> 
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol steps"><li className="li step stepexpand"><span className="ph cmd">Create an emulator with Fingerprint settings, for instance Pixel 3 API 30.<img className="image" width={300} src={useBaseUrl("/4472dbb0-faeb-11ed-878a-0242c7a41fd4/Pixel_3_emulator_fingerprint_setting.jpeg")} alt="Pixel 3 emulator fingerprint" /></span></li><li className="li step stepexpand"><span className="ph cmd">We can select any of the options below for the screen lock setting.</span><div className="itemgroup info"><img className="image" width={300} src={useBaseUrl("/44194a00-faeb-11ed-878a-0242c7a41fd4/Pixel_3_screenlock_settings.jpeg")} alt="fingerprint setting" /></div></li><li className="li step stepexpand"><span className="ph cmd">Use the adb command to emulate finger touching action.</span><div className="itemgroup info"><pre className="pre codeblock"><code>//Open terminal{"\n"}adb -e emu finger touch &lt;finger ID&gt;{"\n"}//finger ID from 1 to 10{"\n"}Ex: adb -e emu finger touch 10</code></pre></div></li></ol> 
<section xmlns="http://www.w3.org/1999/xhtml" className="section result">The fingerprint emulation is accomplished. <img className="image" src={useBaseUrl("/43ce1030-faeb-11ed-878a-0242c7a41fd4/Pixel_3_emulator_finger_touch.jpeg")} /></section> 
