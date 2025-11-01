---
hide_title: true
title: Common WebDriverAgent installation issues
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="troubleshooting-838" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Common WebDriverAgent installation issues

<p xmlns="http://www.w3.org/1999/xhtml" className="shortdesc"> </p> 
<section xmlns="http://www.w3.org/1999/xhtml" className="section condition"><p className="p">The following are some common issues you may encounter when install WebDriverAgent.</p></section> 
<div xmlns="http://www.w3.org/1999/xhtml" className="bodydiv troubleSolution"><section className="section cause"><p className="p">Unrecognized device.</p><p className="p"><img className="image" width={400} src={useBaseUrl("/eddf4760-8f51-11ee-ab4f-0242c7a41fd4/unrecognized_device.png")} /></p></section><section className="section remedy"><div className="li step p"><span className="ph cmd">Try reconnecting the device and click <kbd className="ph userinput">Trust</kbd> for the connected machine.</span></div></section></div>

#### Cause
Failed to install the WebDriverAgent.

<img src="https://docs.katalon.com/edcd9420-8f51-11ee-ab4f-0242c7a41fd4/failed_to_install_webdriveragent.png" alt="failed to install webdrive agent warning" width="700"/> <br/>

You can try the following workarounds:
#### Remedy

- Add the Read, Write, and Execute permissions to `.appium` folder.
    
    ```
    sudo chmod -R 777 ~/.appium
    ```
    
- Reinstall Appium and xcuitest driver.
    
    ```
    npm install -g appium
    appium driver install xcuitest
    ```
#### Cause
No provisioning profile.

<img src="https://docs.katalon.com/edd0a160-8f51-11ee-ab4f-0242c7a41fd4/no_provisioning_profile.png" alt="provisioning profile and dev indentity tab" width="600" /> <br/>

#### Remedy 

Make sure you have installed provisioning profile and certificates on your machine.

To view your installed certificates, see: [View a signing certificate](https://help.apple.com/xcode/mac/current/#/dev97211aeac?sub=devf945466d0).

View your provisioning profiles in `~/Library/MobileDevice/Provisioning Profiles`.

<div xmlns="http://www.w3.org/1999/xhtml" className="bodydiv troubleSolution"><section className="section cause"><p className="p">Don't see your identities.</p><p className="p">Invalid trust settings.</p></section><section className="section remedy"><div className="li step p"><span className="ph cmd">Make sure that the Apple Worldwide Developer Relations Certificate Authority is added to the login keychain.</span><div className="itemgroup info"><img className="image" width={700} src={useBaseUrl("/edbc2f00-8f51-11ee-ab4f-0242c7a41fd4/missing-intermediate-cert.png")} /></div></div></section></div>
<div xmlns="http://www.w3.org/1999/xhtml" className="bodydiv troubleSolution"><section className="section cause"><p className="p">Issue when using Xcode 14.x with Appium 1.x </p></section><section className="section remedy"><div className="li step p"><span className="ph cmd">See this troubleshooting: <a className="xref" href="/katalon-studio/troubleshooting/troubleshoot-mobile-automated-testing/unable-to-execute-tests-with-ios-on-macos-ventura-and-xcode-14.x">Unable to execute tests with iOS on macOS Ventura and XCode 14.x</a>.</span></div></section></div>
<div xmlns="http://www.w3.org/1999/xhtml" className="bodydiv troubleSolution"><section className="section cause"><p className="p">codesign wants to sign using key &lt;keyname&gt; in your keychain.</p></section><section className="section remedy"><div className="li step p"><span className="ph cmd">Configure the access control of the certificate to allow all applications to access the key.</span><div className="itemgroup info"><img className="image" width={500} src={useBaseUrl("/edbfff90-8f51-11ee-ab4f-0242c7a41fd4/keychain_allow_all_applications_to_access.png")} alt="Keychain Access" /></div></div></section></div>
