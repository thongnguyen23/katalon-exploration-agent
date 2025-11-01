---
hide_title: true
title: '[Native render only] [Webview render] Capture elements in hybrid Android apps in Katalon Studio'
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="id" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>[Native render only] [Webview render] Capture elements in hybrid Android apps in <span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon Studio</span> 

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Katalon Mobile Recorder/Spy utility can detect elements in hybrid app rendered as native app, but cannot as Webview. </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">This tutorial provides a solution to capture Android hybrid mobile elements in WebView with Appium and Chrome Devtools. </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">You can learn more about Android WebView functionalities from the Android developer documentation here: <a className="xref j-external-link" href="https://developer.android.com/reference/android/webkit/WebView" target="_blank">WebView</a>.</p> 
    

## <a id="id_1" class="anchor_top_offset"/>Enable WebView debugging for hybrid Android apps

    
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Enable WebView debugging in your Android app. To enable this,   set the <code className="ph codeph">setWebContentsDebuggingEnabled</code> property on the   <code className="ph codeph">android.webkit.WebView</code> element to <code className="ph codeph">true</code>.   You can learn more about configuring WebView for debugging from the   Chrome developer documentation here: <a className="xref j-external-link" href="https://developer.chrome.com/docs/devtools/remote-debugging/webviews/" target="_blank">Remote     debugging WebViews</a>.</p> 
    
  

## <a id="id_2" class="anchor_top_offset"/>Install ChromeDriver for Appium
1. By default, Appium installation includes the latest version of ChromeDriver. However, if your testing device are running different Chrome browser version, you should download the compatible version with Chrome on your testing devices. You can download ChromeDriver from the Chromium website: [ChromeDriver](https://sites.google.com/chromium.org/driver/downloads).
2. Specify the ChromeDriver version in the session. Go to **Project** > **Settings** > **Desired capabilities** > **Mobile** > **Android** and add this property:
    
    
    | **Name** | **Type** | **Value** |
    | --- | --- | --- |
    | chromedriverExecutable(*) | String | `<path-to-your-chromedriver>` (**) |
    
    (*) `chromedriverExecutable`: Support specifying ChromeDriver version in session capabilities.
    
    (**)`<path-to-your-chromedriver>`: full path to the ChromeDriver executable downloaded from Step 1. For example: `/Users/katalon.team/Downloads/chromedriver`.
    
    <img src="https://docs.katalon.com/963bfbf0-22b2-11ed-9930-0242fe3e4a3f/KS-HYBRID-Specify-path-to-ChromeDriver.png" alt="Project settings desired capabilities" />

### Result

<p xmlns="http://www.w3.org/1999/xhtml" className="p">After enabling WebView and installing ChromeDriver for Appium, you may now capture elements. See <a className="xref" href="/katalon-studio/record-and-spy/mobile-record-and-spy-utilities/hybrid-mobile-apps-testing/native-render-only-capture-elements-in-hybrid-android-apps">[Native render only] Capture elements in hybrid Android apps</a>. Do check the note in Step 3 for additional instructions.</p> 
