---
hide_title: true
title: 'Unable to capture objects. Reason: ScreenshotException'
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="troubleshooting-5242" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Unable to capture objects. Reason: ScreenshotException

<section xmlns="http://www.w3.org/1999/xhtml" className="section condition"><p className="p">When recording automation on Android apps you might encounter the error message: <code className="ph codeph">Unable to capture objects. Reason: ScreenshotException</code>. </p><p className="p"><img className="image" src={useBaseUrl("/fdd47600-8e88-11ee-ab4f-0242c7a41fd4/KS_-_error_Unable_to_capture_objects.jpeg")} alt="Katalon Studio - error Unable to capture objects" /></p></section> 
<div xmlns="http://www.w3.org/1999/xhtml" className="bodydiv troubleSolution"><section className="section cause"><p className="p">This is a known issue that some Android app may have settings that prevent screenshots from being taken. See Android <a className="xref j-external-link" href="https://developer.android.com/reference/android/view/WindowManager.LayoutParams#FLAG_SECURE" target="_blank">FLAG_SECURE</a>. </p></section><section className="section remedy"><div className="li step p"><span className="ph cmd">The Android app developer needs to disable <a className="xref j-external-link" href="https://developer.android.com/reference/android/view/WindowManager.LayoutParams#FLAG_SECURE" target="_blank">FLAG_SECURE</a> from the Android app so that <span className="ph">Katalon Studio</span> can capture and automate the screen.</span></div></section></div>
