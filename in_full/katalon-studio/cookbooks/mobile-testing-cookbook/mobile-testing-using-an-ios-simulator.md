---
hide_title: true
title: Mobile testing using an iOS simulator
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="concept-1903" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Mobile testing using an iOS simulator

<p xmlns="http://www.w3.org/1999/xhtml" className="shortdesc">Learn how to perform mobile testing in Katalon Studio using an iOS simulator.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Mobile testing using an iOS simulator allows you  to test your iOS apps in a virtual environment that mimics real Apple devices. The simulator, available through Xcode, lets you check how apps work on different iPhone and iPad models and operating system versions early in development without needing physical devices. </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">When performing mobile testing using an iOS simulator in Katalon Studio, follow these pre-testing steps:</p> 
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol"><li className="li"><p className="p"><strong className="ph b">Install Xcode</strong>: Download and install Xcode from the Mac App Store to access iOS development and testing tools.</p></li><li className="li"><p className="p"><strong className="ph b">Install Appium and Xcode command-line tools</strong>: You need Appium 2.x for automating mobile tests and the Xcode command-line tools for simulator management.</p></li><li className="li"><p className="p"><strong className="ph b">Set up Xcode simulator for mobile testing</strong>: Configure the Xcode simulator to mimic specific iOS devices for testing your app.</p></li><li className="li"><p className="p"><strong className="ph b">Prepare the iOS application file</strong>: Build or obtain the <code className="ph codeph">.app</code> or <code className="ph codeph">.ipa</code> file of your iOS application to load it into the simulator for testing.</p></li></ol> 

## Before you begin

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Before you proceed with testing your mobile app using an iOS simulator, there are a certain considerations that you need to keep in mind or configure. To begin with, you need to setup a macOS environment. You <strong className="ph b">can     not</strong> execute iOS mobile testing in Windows and Linux.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">We recommend going to the following developer documentation for more information on app build schemes and  requirements: <a className="xref j-external-link" href="https://developer.apple.com/documentation/xcode/running-your-app-in-simulator-or-on-a-device" target="_blank">Running your app in Simulator or a device</a>.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">To get started with mobile testing using an iOS simulator, you need to install Xcode first.</p> 

## <a id="id_1-jpa1qcuj" class="anchor_top_offset"/>Install Xcode

<p xmlns="http://www.w3.org/1999/xhtml" className="shortdesc">Learn how to install Xcode for your mobile testing using an iOS simulator.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Xcode is the integrated development environment used for building apps across all Apple platforms. Xcode includes iOS, iPadOS, and visionOS simulators (on Macs with Apple silicon), and is available for free on the Mac App Store.</p> 
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol"><li className="li"><div className="p">Go to the Mac App Store or click on the link to download Xcode: <a className="xref j-external-link" href="https://developer.apple.com/xcode/" target="_blank">Xcode</a>.<div className="note note note_note"><span className="note__title">Note:</span> <ul className="ul"><li className="li">Install Xcode version 10.2 or newer. </li><li className="li">Xcode must support the current version of your macOS and iOS device. Check that your macOS and iOS device are compatible with Xcode in this document <a className="xref" href="/katalon-studio/supported-environments-for-katalon-studio-and-katalon-runtime-engine-kre">supported iOS environments in Katalon Studio</a> and Apple Developer document <a className="xref j-external-link" href="https://developer.apple.com/support/xcode/" target="_blank">System requirements.</a></li></ul></div></div></li><li className="li"><p className="p">Launch Xcode. A dialog will show which Simulator runtimes are built-in and available for download. Select <span className="ph uicontrol">Continue</span> to finish setting up Xcode.</p></li><li className="li"><p className="p">Once Xcode setup is complete, relaunch Safari to use <span className="ph menucascade"><span className="ph uicontrol">Open Page With</span><abbr title="and then"> &gt; </abbr><span className="ph uicontrol">[Your selected simulator]</span></span> in the Develop menu and <span className="ph uicontrol">Open with Simulator</span> in Responsive Design Mode.</p></li></ol> 

## <a id="id_2-nnf1ioo0" class="anchor_top_offset"/>Install Appium 2.x and Xcode command-line tools

<p xmlns="http://www.w3.org/1999/xhtml" className="shortdesc">Learn how to install Appium 2.x and XCode command-line tools for your mobile testing using an iOS simulator.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">There are two ways to go about installing these pre-testing tools. You have the option to install them using the built-in tools function in Katalon Studio, or you can install each manually.</p> 

### <a id="task-fi233hzd" class="anchor_top_offset"/>Install with built-in tools

<section xmlns="http://www.w3.org/1999/xhtml" className="section context">From Katalon Studio version 8.3.0 onwards, you can install Appium and Xcode command-line tools (Xcode CLT) via Katalon built-in tools. To do so:</section> 
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol steps"><li className="li step stepexpand"><span className="ph cmd">Go to <span className="ph menucascade"><span className="ph uicontrol">Tools</span><abbr title="and then"> &gt; </abbr><span className="ph uicontrol">Set up iOS environment</span></span> and select <span className="ph uicontrol">Install Dependencies</span>.</span><div className="itemgroup info"><img className="image" width={500} src={useBaseUrl("/a0a7024d-8dcc-44d8-930d-7b81c64f8508/KS-825-Install-dependencies-via-built-in-tools.png")} alt="Install dependencies via Katalon built-in tools" /></div></li><li className="li step stepexpand"><span className="ph cmd">Katalon will automatically install the latest version of Xcode CLT, Appium, Homebrew, NodeJS, and other iOS dependencies.</span><div className="itemgroup info"><img className="image" width={500} src={useBaseUrl("/5edbd2e4-fa6b-4746-b3e5-bc631ad16307/KS-825-KS-install-dependencies.png")} alt="KS installs dependencies" /></div></li></ol> 

### <a id="task-625idsd9" class="anchor_top_offset"/>Install manually

<ol xmlns="http://www.w3.org/1999/xhtml" className="ol steps"><li className="li step stepexpand"><span className="ph cmd">Install the command-line tool for Xcode. You can download the command-line tool compatible with your Xcode version from the Apple Developer website here: <a className="xref j-external-link" href="https://developer.apple.com/download/all/" target="_blank">Download</a>.</span><div className="itemgroup info"><div className="p">Alternatively, you can copy and paste the following command-line arguments in this order in the Terminal to install the command-line tool for Xcode:<pre className="pre codeblock"><code>xcode-select --instal</code></pre><pre className="pre codeblock"><code>sudo xcode-select -s /Applications/Xcode.app/Contents/Developer</code></pre> </div></div></li><li className="li step stepexpand"><span className="ph cmd">Download and install Node.js from the Node.js website: <a className="xref j-external-link" href="https://nodejs.org/en/download/" target="_blank">Node.js Downloads</a>.</span><div className="itemgroup info">Make sure you install Node.js into a location where you have full Read/Write permissions.</div></li><li className="li step stepexpand"><span className="ph cmd">Install Appium with the following commands in the Terminal:</span><div className="itemgroup info"><ul className="ul"><li className="li">For <span className="ph">Katalon Studio</span> 9.1.0 onwards, install the latest Appium version:<pre className="pre codeblock"><code>npm install -g appium</code></pre></li><li className="li">For <span className="ph">Katalon Studio</span> before 9.1.0, install Appium 1.12.1+:<pre className="pre codeblock"><code>npm install -g appium@version</code></pre></li></ul></div><div className="itemgroup info"><div className="note note note_note"><span className="note__title">Note:</span> <ul className="ul"><li className="li">If you are using emulators other than Xcode simulators, some emulators come with Appium installed. If you want to run an application on an emulator, check your emulator settings before installing Appium.</li></ul></div></div></li></ol> 

## <a id="concept-dy6j220p" class="anchor_top_offset"/>Set up Xcode simulators for mobile testing in Katalon Studio

<p xmlns="http://www.w3.org/1999/xhtml" className="p">After installing Xcode, Katalon automatically recognizes Xcode simulators as iOS devices. </p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">To check whether Katalon Studio successfully recognizes Xcode simulators, on the main toolbar, select the iOS device in the dropdown list next to <strong className="ph b">Run</strong>.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" src={useBaseUrl("/62485a76-6e66-4cad-92f7-548c3426e2db/KS-TOOLBAR-iOS.png")} alt="Katalon recognizes Xcode simulators" /></p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">You should see a list of pre-installed Xcode simulators appearing as iOS devices.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" src={useBaseUrl("/341828fc-c527-4811-9218-38923b0e27c1/KS-iOS-Katalon-regconizes-simulators.png")} alt="Katalon recognizes Xcode simulators" /></p> 

## <a id="task-to52f4mt" class="anchor_top_offset"/>Prepare the iOS application file

<section xmlns="http://www.w3.org/1999/xhtml" className="section context">To execute mobile testing with Xcode simulators, prepare your <code className="ph codeph">.app</code> or <code className="ph codeph">.ipa</code> file.</section> 

1. Open the `.xcodeproj` project file with Xcode. In the example below, we will open our sample `Coffee Timer.xcodeproj` project file.
    <img src="https://docs.katalon.com/e6ca1f38-61fd-4b46-b917-ed5960d05060/open-xcode-file.png" alt="Open Xcode project" width="600" /> <br/>
2. After opening the project in Xcode, choose one of the iOS simulators to launch the apps.
    <img src="https://docs.katalon.com/f7670761-c060-4fc6-8766-7f9daaf7aaa2/KS-iOS-Choose-simulator-1.png" alt="Choose simulators" width="600" /> <br/>

3. To build the `.app` file, click **Product > Build**.
    Wait for the build to finish, to find the `app` file, go to `~/Library/Developer/Xcode/DerivedData/{app name}/Build/Products/{scheme}-iphonesimulator/{app name}.app`. In this example, we can find our sample `Coffee Timer.app` file at: `~/Library/Developer/Xcode/DerivedData/Coffee Timer/Build/Products/Debug-iphonesimulator/Coffee Timer.app`.

    **Note**: To quickly search for the DerivedData folder, copy and paste the following path ~/Library/Developer/Xcode/DerivedData into the Spotlight.

<section xmlns="http://www.w3.org/1999/xhtml" className="section result">Congratulations! You may now proceed to recording a mobile test using your iOS simulator. See the following cookbook topic for more information: <a className="xref" href="/katalon-studio/cookbooks/mobile-testing-cookbook/mobile-testing-on-a-real-ios-device#task-ffch4oc5">Record a mobile test case</a>.</section> 
