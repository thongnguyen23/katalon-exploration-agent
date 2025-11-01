---
hide_title: true
title: Common iOS dependencies installation issues
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="troubleshooting-5183" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Common iOS dependencies installation issues

<p xmlns="http://www.w3.org/1999/xhtml" className="shortdesc"> </p> 
The following are some common issues you may encounter when install iOS dependencies.

<div xmlns="http://www.w3.org/1999/xhtml" className="bodydiv troubleSolution"><section className="section cause"><p className="p">Command not found: brew.</p><p className="p">Can't find brew in PATH</p><p className="p"><img className="image" width={400} src={useBaseUrl("/edb81050-8f51-11ee-ab4f-0242c7a41fd4/cant_find_brew_in_path.png")} /></p></section><section className="section remedy"><div className="li step p"><span className="ph cmd">We recommend reinstalling brew and add the brew to your PATH environment variable. See: <a className="xref j-external-link" href="https://brew.sh/" target="_blank">Homebrew</a>.</span></div></section></div>
<div xmlns="http://www.w3.org/1999/xhtml" className="bodydiv troubleSolution"><section className="section cause"><p className="p">Incompatible Node.js or <code className="ph codeph">npm</code> version.</p><p className="p"><img className="image" width={400} src={useBaseUrl("/eddbec00-8f51-11ee-ab4f-0242c7a41fd4/incompatible_nodejs.png")} /></p></section><section className="section remedy"><div className="li step p"><span className="ph cmd"> Reinstall Node.js version 18.0.0 or later, along with <code className="ph codeph">npm</code> version 8 or later.</span></div></section></div>
<div xmlns="http://www.w3.org/1999/xhtml" className="bodydiv troubleSolution"><section className="section cause"><p className="p">Failed to install Appium.</p></section><section className="section remedy"><div className="li step p"><span className="ph cmd">There may exist a version of Appium on your machine. We recommend uninstalling Appium and reinstall with the Katalon Studio dialog.</span><div className="itemgroup info"><div className="p">Try the following command to uninstall Appium:<pre className="pre codeblock"><code>sudo npm uninstall -g appium</code></pre></div></div></div></section></div>

#### Cause
Unable to find xcode version.

#### Remedy

Try the following command:
```
sudo xcode-select -s /Applications/Xcode.app
```