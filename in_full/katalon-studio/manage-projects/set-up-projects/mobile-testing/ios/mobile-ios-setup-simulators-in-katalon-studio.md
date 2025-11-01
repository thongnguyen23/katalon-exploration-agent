---
hide_title: true
title: '[Mobile] iOS Setup (Simulators) in Katalon Studio'
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="id" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>[Mobile] iOS Setup (Simulators) in <span xmlns="http://www.w3.org/1999/xhtml" className="ph">Katalon Studio</span> 

<p xmlns="http://www.w3.org/1999/xhtml" className="p">This article shows you how to set up Xcode simulators to test iOS applications with Katalon Studio.</p> 
<div xmlns="http://www.w3.org/1999/xhtml" className="p">To begin with, you need to setup a macOS environment. You can not execute iOS mobile testing in Windows and Linux.<div className="note note note_note"><span className="note__title">Note:</span> <ul className="ul"><li className="li">From version 9.1.0 onwards, <span className="ph">Katalon Studio</span> supports Appium 2 for mobile testing.</li></ul></div></div>
<nav xmlns="http://www.w3.org/1999/xhtml" role="navigation" className="related-links"><div className="linklist relinfo"><strong>Related information</strong><br /><br /><ul className="linklist"><li className="linklist"><a className="link" href="/katalon-studio/get-started/sample-projects/mobile/mobile-create-and-run-ios-test-case-in-katalon-studio">[Mobile] Create and Run iOS Test Case in Katalon Studio</a></li><li className="linklist"><a className="link" href="/katalon-studio/troubleshooting/troubleshoot-mobile-automated-testing/troubleshooting-automated-mobile-testing-overview">Troubleshooting automated mobile testing</a></li></ul></div></nav> 

## <a id="id_1" class="anchor_top_offset"/>Part 1: Install Xcode

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Install Xcode version 10.2 or newer. You can download Xcode from the App Store or the Apple Developer website: <a className="xref j-external-link" href="https://developer.apple.com/xcode/" target="_blank">Xcode 13</a>.</p> 
<div xmlns="http://www.w3.org/1999/xhtml" className="p"><div className="note note note_note"><span className="note__title">Note:</span> <ul className="ul"><li className="li">Xcode must support the current version of your macOS and iOS device. Check that your macOS and iOS device are compatible with Xcode in this document <a className="xref" href="/katalon-studio/supported-environments-for-katalon-studio-and-katalon-runtime-engine-kre#id_3">supported iOS environments in Katalon Studio</a> and Apple Developer document <a className="xref j-external-link" href="https://developer.apple.com/support/xcode/" target="_blank">System requirements</a>.</li></ul></div></div>

## <a id="id_2" class="anchor_top_offset"/>Part 2: Install Appium and Xcode command-line tools


### <a id="task-7459" class="anchor_top_offset"/>Install with built-in tools

<section xmlns="http://www.w3.org/1999/xhtml" className="section context">You can install Appium and Xcode command-line tools (Xcode CLT) via Katalon built-in tools. To do so:</section> 
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol steps"><li className="li step stepexpand"><span className="ph cmd">Go to <span className="ph uicontrol">Tools</span> &gt; <span className="ph uicontrol">Set up iOS environment</span> and select <span className="ph uicontrol">Install Dependencies</span>.</span><div className="itemgroup info"><img className="image" width={500} src={useBaseUrl("/8ac344d0-8f2c-11ee-ab4f-0242c7a41fd4/ks-910-set-up-ios-env.png")} alt="Install dependencies via Katalon built-in tools" /></div></li><li className="li step stepexpand"><span className="ph cmd">Katalon will automatically install the latest version of Xcode CLT, Appium, Homebrew, NodeJS, and other iOS dependencies.</span><div className="itemgroup info"><img className="image" width={500} src={useBaseUrl("/8f2b8330-22b2-11ed-9930-0242fe3e4a3f/KS-825-KS-install-dependencies.png")} alt="KS installs dependencies" /></div></li></ol> 

### <a id="task-2441" class="anchor_top_offset"/>Install manually

<ol xmlns="http://www.w3.org/1999/xhtml" className="ol steps"><li className="li step stepexpand"><span className="ph cmd">Install the command-line tool for Xcode. You can download the command-line tool compatible with your Xcode version from the Apple Developer website here: <a className="xref j-external-link" href="https://developer.apple.com/download/all/" target="_blank">Download</a>.</span><div className="itemgroup info"><div className="p">Alternatively, you can copy and paste the following command-line arguments in this order in the <strong className="ph b">Terminal</strong> to install the command-line tool for Xcode:<pre className="pre codeblock"><code>xcode-select --install</code></pre><pre className="pre codeblock"><code>sudo xcode-select -s /Applications/Xcode.app/Contents/Developer</code></pre> </div></div></li><li className="li step stepexpand"><span className="ph cmd">Download and install Node.js from the Node.js website: <a className="xref j-external-link" href="https://nodejs.org/en/download/" target="_blank">Node.js Downloads</a>.</span><div className="itemgroup info">Make sure you install Node.js into a location where you have full Read/Write permissions.</div></li><li className="li step stepexpand"><span className="ph cmd">Install Appium with the following commands in the Terminal:</span><div className="itemgroup info"><ul className="ul"><li className="li">For <span className="ph">Katalon Studio</span> 9.1.0 onwards, install the latest Appium version:<pre className="pre codeblock"><code>npm install -g appium</code></pre></li><li className="li">For <span className="ph">Katalon Studio</span> before 9.1.0, install Appium 1.12.1+:<pre className="pre codeblock"><code>npm install -g appium@version</code></pre></li></ul></div><div className="itemgroup info"><div className="note note note_note"><span className="note__title">Note:</span> <ul className="ul"><li className="li">If you are using emulators other than Xcode simulators, some emulators come with Appium installed. If you want to run an application on an emulator, check your emulator settings before installing Appium.</li></ul></div><p className="p">To learn more about Appium, you can refer to the Appium document here: <a className="xref j-external-link" href="http://appium.io/docs/en/about-appium/getting-started/#installing-appium" target="_blank">Getting started</a>.</p></div></li></ol> 

## <a id="concept-8181" class="anchor_top_offset"/>Part 3: Set up Xcode simulators for mobile testing in Katalon Studio

<p xmlns="http://www.w3.org/1999/xhtml" className="p">After installing Xcode, Katalon automatically recognizes Xcode   simulators as iOS devices. To check whether Katalon successfully   recognizes Xcode simulators, on the main toolbar, select the   <strong className="ph b">iOS</strong> device in the dropdown list next to   <strong className="ph b">Run</strong>.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" src={useBaseUrl("/8f2ae6f0-22b2-11ed-9930-0242fe3e4a3f/KS-TOOLBAR-iOS.png")} alt="Katalon recognizes Xcode simulators" /></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">You should see a list of pre-installed Xcode simulators appearing as iOS devices.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" src={useBaseUrl("/8f2a71c0-22b2-11ed-9930-0242fe3e4a3f/KS-iOS-Katalon-regconizes-simulators.png")} alt="Katalon recognizes Xcode simulators" /></p> 

## <a id="task-1208" class="anchor_top_offset"/>Part 4: Prepare the iOS application file

To execute mobile testing with Xcode simulators, you need to prepare an `.app` file.

1. Open the `.xcodeproj` project file with Xcode. Here, we open our sample `Coffee Timer.xcodeproj` project file.
    
    <img src="https://docs.katalon.com/8f29fc90-22b2-11ed-9930-0242fe3e4a3f/open-xcode-file.png" alt="Coffee Timer folder screen" width="700" />
    
2. After opening the project in Xcode, choose one of the iOS simulators to launch the apps.
    
    <img src="https://docs.katalon.com/8f28eb20-22b2-11ed-9930-0242fe3e4a3f/KS-iOS-Choose-simulator-1.png" alt="choose ipad 9th" />
    
3. To build the `.app` file, click **Product > Build**.
    
    Wait for the build to finish, to find the `app` file, go to `~/Library/Developer/Xcode/DerivedData/{app name}/Build/Products/{scheme}-iphonesimulator/{app name}.app`. In this example, we can find our sample `Coffee Timer.app` file at: `~/Library/Developer/Xcode/DerivedData/Coffee Timer/Build/Products/Debug-iphonesimulator/Coffee Timer.app`.
    
    **Tips**: To quickly search for the `DerivedData` folder, copy and paste the following path `~/Library/Developer/Xcode/DerivedData` into the **Spotlight**.

<nav xmlns="http://www.w3.org/1999/xhtml" role="navigation" className="related-links"><div className="linklist"><strong>Learn more with our Katalon Academy course:</strong><br /><br /><ul className="linklist"><li className="linklist"><a className="link j-external-link" href="https://academy.katalon.com/courses/codeless-solution-mobile-testing/?utm_source=kat_docs&utm_medium=ios_setup" target="_blank">Solve Mobile Testing Challenges with Codeless Solution</a></li></ul></div></nav> 
