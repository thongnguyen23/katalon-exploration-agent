---
hide_title: true
title: Unable to start a new sessison with TestCloud
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="troubleshooting-6781" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Unable to start a new sessison with TestCloud

<section xmlns="http://www.w3.org/1999/xhtml" className="section condition"><p className="p">You might encounter this error when running test in Katalon Studio 10.x: <img src="https://tw-cdn.katalon.com/katalon-testcloud/testcloud-unable-to-start-new-session.png" alt="Unable to start a new TestCloud session" width="800" /></p></section> 

<div xmlns="http://www.w3.org/1999/xhtml" className="bodydiv troubleSolution"><section className="section cause"><p className="p">This error occurs due to an incompatibility between the Appium version and the selected mobile device. By default, if the <code className="ph codeph">appiumVersion</code> desired capability is not declared, Katalon Studio will use <code className="ph codeph">appiumVersion=2.11.2</code> for execution. Devices running iOS earlier than 15 are not compatible with Appium 2.11.2.</p></section><section className="section remedy"><div className="li step p"><span className="ph cmd">To resolve this issue, you should specify a compatible Appium version in the desired capabilities. Refer to the Appium version configuration guide to use suitable version for the mobile device: <a className="xref" href="/katalon-testcloud/advanced-use-cases/configure-appium-version">Configure Appium version</a>.</span></div></section></div>
