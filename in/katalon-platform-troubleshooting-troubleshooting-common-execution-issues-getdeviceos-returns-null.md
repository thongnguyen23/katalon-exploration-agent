---
hide_title: true
title: getDeviceOS returns null
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="troubleshooting-4097" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>getDeviceOS returns null

<p xmlns="http://www.w3.org/1999/xhtml" className="shortdesc"> </p> 
<section xmlns="http://www.w3.org/1999/xhtml" className="section condition"><p className="p">When users run Mobile.getDeviceOS() function to  get the device OS / platform name in <span className="ph">TestCloud</span> mobile environment, the function returns null.</p></section> 
<div xmlns="http://www.w3.org/1999/xhtml" className="bodydiv troubleSolution"><section className="section cause"><section className="section remedy"><div className="li step p"><span className="ph cmd">Users can use the code below to achieve the platform name and platform version when running tests with <span className="ph">TestCloud</span> devices.</span><div className="itemgroup info"><pre className="pre codeblock"><code>import com.kms.katalon.core.mobile.keyword.internal.MobileDriverFactory{"\n"}{"\n"}import io.appium.java_client.AppiumDriver{"\n"}{"\n"}AppiumDriver&lt;?&gt; driver = MobileDriverFactory.getDriver(){"\n"}println driver.getCapabilities().getCapability("platformName"){"\n"}println driver.getCapabilities().getCapability("platformVersion")</code></pre></div><div className="itemgroup stepresult"><p className="p">On Android:<img className="image" width={500} src={useBaseUrl("/2591fc40-4c6b-11ee-af7c-0242c7a41fd4/TestCloud_Mobile_Native_getDeviceOS_workaround_Android.png")} /></p><p className="p">On iOS:<img className="image" width={500} src={useBaseUrl("/2596b730-4c6b-11ee-af7c-0242c7a41fd4/TestCloud_Mobile_Native_getDeviceOS_workaround_iOS.png")} /></p></div></div></section></section></div>
