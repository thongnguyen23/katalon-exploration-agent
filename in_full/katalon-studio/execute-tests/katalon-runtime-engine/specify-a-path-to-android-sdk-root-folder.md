---
hide_title: true
title: Specify a path to Android SDK root folder
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="id" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Specify a path to Android SDK root folder

<p xmlns="http://www.w3.org/1999/xhtml" className="p">You can use a custom Android SDK location instead of the Katalon Studio default location. Katalon Runtime Engine supports the <code className="ph codeph">ANDROID_HOME</code> environment variable to specify a path to Android SDK root folder. To configure environment variable with KRE commands, see: <a className="xref" href="/katalon-studio/execute-tests/katalon-runtime-engine/command-line-syntax-in-katalon-runtime-engine#concept-1437">General arguments</a>.</p> 
    

## <a id="id_1" class="anchor_top_offset"/>Specify a path to Android SDK root folder

    
      
<p xmlns="http://www.w3.org/1999/xhtml" className="p">By default, the Android SDK root folder is located at   <strong className="ph b">~/.katalon/tools/android<em className="ph i">sdk</em>. You can rename or     move your Android SDK root folder to another location and use     the</strong> ANDROIDHOME environment variable to point the path to   that new location. See also: <a className="xref" href="#">[Mobile]     Android Setup</a>.</p> 
    
      

## <a id="id_2" class="anchor_top_offset"/>Command-line option

<p xmlns="http://www.w3.org/1999/xhtml" className="p">Start Katalon Studio with this command-line option instead of double-clicking on the <strong className="ph b">Katalon</strong> app:</p> 
<ul xmlns="http://www.w3.org/1999/xhtml" className="ul"><li className="li"><p className="p">For Linux and macOS:</p><div className="p"><pre className="pre codeblock"><code>$ export ANDROID_HOME=&lt;Your Android SDK{"\n"}{"                  "}location&gt;</code></pre></div><p className="p">For example:</p><pre className="pre codeblock"><code>$ export ANDROID_HOME=/opt/dev/android-sdk-linux{"\n"}$ ./katalon &lt;arguments&gt;{"\n"}</code></pre></li><li className="li"><p className="p">For Windows:</p><p className="p">1. In the Windows explorer search bar, search for <strong className="ph b">Edit the system environment variables</strong>.</p><p className="p"><img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/how-to-guides/android-home-path/KS-android-home-edit-environment-variables.png")} alt="Edit the system environment variable" /><br /><br /></p><p className="p">The <strong className="ph b">System Properties</strong> dialog appears. Click <strong className="ph b">Environment Variables</strong>.</p><p className="p"><img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/how-to-guides/android-home-path/KS-android-home-environment.png")} alt="system properties" /><br /><br /></p><p className="p">2. In the <strong className="ph b">System variables</strong>, click <strong className="ph b">New</strong> to create a new environment variable like so:</p><ul className="ul"><li className="li"> <strong className="ph b">Variable</strong>: <strong className="ph b">ANDROID_HOME</strong> </li><li className="li"> <strong className="ph b">Value</strong>: your custom path to the Android SDK root folder</li></ul><p className="p"><img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/how-to-guides/android-home-path/KS-android-home-new.png")} alt="new" /><br /><br /></p><p className="p"><img className="image" src={useBaseUrl("https://github.com/katalon-studio/docs-images/raw/master/katalon-studio/how-to-guides/android-home-path/KS-android-home-value.png")} alt="Window Environment Variable" /><br /><br /></p></li></ul> 
<div xmlns="http://www.w3.org/1999/xhtml" className="note note note_note"><span className="note__title">Note:</span> <p className="p">For Appium to locate the tools, keep the ADB file and these folders as their original names:</p><ul className="ul"><li className="li">build-tools</li><li className="li">platform-tools</li><li className="li">tools</li></ul></div>
