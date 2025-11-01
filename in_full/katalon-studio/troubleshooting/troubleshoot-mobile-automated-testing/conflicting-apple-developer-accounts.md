---
hide_title: true
title: Conflicting Apple Developer accounts
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="troubleshooting-2164" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Conflicting Apple Developer accounts

<section xmlns="http://www.w3.org/1999/xhtml" className="section condition"><p className="p">Cannot record/playback the application because of multiple Apple Developer accounts conflict. </p></section> 
<div xmlns="http://www.w3.org/1999/xhtml" className="bodydiv troubleSolution"><section className="section remedy"><div className="li step p"><span className="ph cmd">Open terminal, run the following commands:</span><div className="itemgroup info"><pre className="pre codeblock"><code>sudo gem install fastlane -NV{"\n"}hash -r # for bash{"\n"}rehash # for zsh{"\n"}fastlane sigh resign ./path/app.ipa --signing_identity "Apple Distribution: Company Name" -p "my.mobileprovision"</code></pre>There are two fields in the commands above:  <ul className="ul"><li className="li"><code className="ph codeph">--signing_identity</code>: Apple Distribution - Company Name</li><li className="li"><code className="ph codeph">-p</code>: Provisioning profile path</li></ul><p className="p">To get the correct value of the field <code className="ph codeph">--signing_identity</code>, run <code className="ph codeph">security find-identity -v -p codesigning</code>. To get the correct value of the field <code className="ph codeph">-p</code>, we need to navigate to the provisioning profile folder: <code className="ph codeph">~/Library/MobileDevice/Provisioning\ Profiles</code>.</p><p className="p"><img className="image" width={300} src={useBaseUrl("/cb1600d0-8de8-11ee-ab4f-0242c7a41fd4/Xcode_-_Preferences.jpeg")} alt="Xcode Preferences" /><img className="image" src={useBaseUrl("/cb007d00-8de8-11ee-ab4f-0242c7a41fd4/Xcode_-_download_Manual_Profiles.png")} alt="Download manual profiles" /></p></div></div></section></div>
