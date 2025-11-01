---
hide_title: true
title: Use the keyboard keys while automating Android apps
---

# <a id="task-4914" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Use the keyboard keys while automating Android apps

<ol xmlns="http://www.w3.org/1999/xhtml" className="ol steps"><li className="li step stepexpand"><span className="ph cmd">At the top of your test script, add the following script to import the following libraries: </span><div className="itemgroup info"><pre className="pre codeblock"><code>import com.kms.katalon.core.mobile.keyword.internal.MobileDriverFactory{"\n"}{"\n"}import io.appium.java_client.android.AndroidDriver{"\n"}import io.appium.java_client.android.nativekey.AndroidKey{"\n"}import io.appium.java_client.android.nativekey.KeyEvent</code></pre></div></li><li className="li step stepexpand"><span className="ph cmd">Use this code to access the keys. <code className="ph codeph">AndroidKey</code> is an enum with key entries like <code className="ph codeph">AndroidKey.ENTER</code> and <code className="ph codeph">AndroidKey.A</code>. For example:</span><div className="itemgroup info"><pre className="pre codeblock"><code>AndroidDriver&lt;?&gt; driver = MobileDriverFactory.getDriver(){"\n"}driver.pressKey(new KeyEvent(AndroidKey.ENTER))</code></pre><p className="p">For a complete list of keys, refer to the java-client 6.1.0 API documentation: <a className="xref j-external-link" href="https://appium.github.io/java-client/io/appium/java_client/android/nativekey/AndroidKey.html" target="_blank">Enum AndroidKey</a>.</p></div></li></ol> 
