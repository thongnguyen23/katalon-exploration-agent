---
hide_title: true
title: Configure Proxy Preferences in Katalon Studio
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# <a id="id" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Configure Proxy Preferences in Katalon Studio

<p xmlns="http://www.w3.org/1999/xhtml" className="p">In <span className="ph">Katalon Studio</span>, there are two proxy categories: Authentication and System proxies. You can apply different proxy configurations for connecting to the Katalon server and your servers during testing.</p> 
<div xmlns="http://www.w3.org/1999/xhtml" className="p">To access Proxy preferences, go to <span className="ph menucascade"><span className="ph uicontrol">Katalon Studio</span><abbr title="and then"> &gt; </abbr><span className="ph uicontrol">Preferences</span><abbr title="and then"> &gt; </abbr><span className="ph uicontrol">Katalon</span><abbr title="and then"> &gt; </abbr><span className="ph uicontrol">Proxy</span></span>. Select the <span className="ph uicontrol">Authentication</span> or <span className="ph uicontrol">System</span> section for the corresponding proxy configuration.<ul className="ul"><li className="li"><p className="p">Authentication proxy configurations: used for  authenticating with  Katalon Authentication servers. This affects account authentication, <span className="ph">Katalon TestOps</span>, <span className="ph">TestCloud</span>, Store integration, the Katalon auto-updater, WebDriver auto-updater, sample projects providers, and more.</p></li><li className="li"><p className="p">System proxy configurations:  applies to other network
        connections generated when using <span className="ph">Katalon Studio</span>, including but not
        limited to recording, spying, executing tests, integrating with
        other tools, and downloading Web Drivers or Android SDK.</p></li></ul></div>

## Proxy configuration options


In both the **Authentication** and **System** Proxy options, select one of the three options below.

<img src="https://docs.katalon.com/9bd1c3a0-28e9-11ed-9930-0242fe3e4a3f/ks-850-proxy-option.png" alt="KS - Preferences System" width="700" /> <br/>

- **No proxy**: Connect directly without proxy.
- **Use system proxy configuration**: Katalon Studio guesses which proxy server your system is behind by checking Java, browser and operating system settings, and environment variables.
- **Manual proxy configuration**: Manually set up your proxy with the following settings:
      - Address: A Proxy server host.
      - Port: A Proxy server port.
      - Excludes: A list of addresses separated by commas. Enter the beginning or the ending of the address in the list (e.g,`.192.168.*`, `.katalon.com`)
            
            **Note**: Katalon Studio only supports proxy exceptions in web recorder and spy utilities with Chrome and Firefox.

## <a id="task-8122" class="anchor_top_offset"/>Use desired capabilities to set different proxy settings

<section xmlns="http://www.w3.org/1999/xhtml" className="section context"><span className="ph">Katalon Studio</span> applies the system proxy to the desired capabilities   of a test execution on the instance automatically. <p className="p">If you want to     configure different proxy settings depending on your projects, you     can use <span className="ph uicontrol">Desired Capabilities</span> as follows:</p>  </section> 
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol steps"><li className="li step stepexpand"><span className="ph cmd">Open your project and go to <span className="ph menucascade"><span className="ph uicontrol">Katalon Studio</span><abbr title="and then"> &gt; </abbr><span className="ph uicontrol">Preferences</span><abbr title="and then"> &gt; </abbr><span className="ph uicontrol">Katalon</span><abbr title="and then"> &gt; </abbr><span className="ph uicontrol">Proxy</span><abbr title="and then"> &gt; </abbr><span className="ph uicontrol">System</span></span>.</span></li><li className="li step stepexpand"><span className="ph cmd">At the bottom of the displayed view, uncheck the       <span className="ph uicontrol">Auto-apply to test execution desired capabilities</span>       option.</span><div className="itemgroup stepxmp"><img className="image" width={700} src={useBaseUrl("/6eee4fd0-a2dc-11ed-998d-0242cfbc79b5/ks-proxy-setting-uncheck.png")} alt="Uncheck the Auto-apply to test execution desired capabilities at the end of the Proxy System setting" /></div></li><li className="li step stepexpand"><span className="ph cmd">Click <span className="ph uicontrol">Apply</span> to save.</span></li><li className="li step stepexpand"><span className="ph cmd">Go to <span className="ph menucascade"><span className="ph uicontrol">Project</span><abbr title="and then"> &gt; </abbr><span className="ph uicontrol">Settings</span><abbr title="and then"> &gt; </abbr><span className="ph uicontrol">Desired Capabilities</span></span>  and       select a testing environment.</span></li><li className="li step stepexpand"><span className="ph cmd">Specify the proxy details. For example:</span><div className="itemgroup stepxmp"><img className="image" width={700} src={useBaseUrl("/6ed1ee30-a2dc-11ed-998d-0242cfbc79b5/proxy-project-settings.png")} alt="Specify proxy details in Project settings" /></div></li><li className="li step stepexpand"><span className="ph cmd"> Click <span className="ph uicontrol">Apply &amp; Close</span>.</span></li></ol> 

## <a id="id_5" class="anchor_top_offset"/>Override proxy details in the test script

<p xmlns="http://www.w3.org/1999/xhtml" className="p"><span className="ph">Katalon Studio</span> supports an option to pass proxy details via a request object in Web Service testing.</p> 
<div xmlns="http://www.w3.org/1999/xhtml" className="note note note_note"><span className="note__title">Note:</span> <ul className="ul"><li className="li">The proxy information passed in the request object overrides the proxy information in <span className="ph uicontrol">Proxy Preferences</span>.</li></ul></div>
<div xmlns="http://www.w3.org/1999/xhtml" className="p">See the example below: <pre className="pre codeblock"><code>RequestObject requestObject = findTestObject("google"){"\n"}ProxyInformation proxyInfo = new ProxyInformation();{"\n"}proxyInfo.setProxyServerAddress("localhost"){"\n"}proxyInfo.setProxyServerPort(8001){"\n"}proxyInfo.setProxyOption(ProxyOption.MANUAL_CONFIG.toString()){"\n"}proxyInfo.setProxyServerType(ProxyServerType.HTTP.toString()){"\n"}requestObject.setProxy(proxyInfo)</code></pre> </div>
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Another workaround to override proxy details in script mode is to get your current proxy format, then pass your new proxy information in.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">See the example below:</p> 
<pre xmlns="http://www.w3.org/1999/xhtml" className="pre codeblock"><code>import com.google.gson.Gson {"\n"}import com.kms.katalon.core.configuration.RunConfiguration {"\n"}import com.kms.katalon.core.network.ProxyInformation {"\n"}import com.kms.katalon.core.network.ProxyOption{"\n"}{"\n"}// Get current proxy information {"\n"}ProxyInformation proxy = RunConfiguration.getProxyInformation() {"\n"}println(proxy){"\n"}{"\n"}// Switch proxy {"\n"}proxy.setProxyOption(ProxyOption.MANUAL_CONFIG.name()) {"\n"}proxy.setProxyServerAddress("127.0.0.1") {"\n"}proxy.setProxyServerPort(8082) {"\n"}Map&lt;String, Object&gt; generalProperties = RunConfiguration.getExecutionGeneralProperties(); {"\n"}generalProperties.put(RunConfiguration.PROXY_PROPERTY, new Gson().toJson(proxy)); {"\n"}println proxy{"\n"}{"\n"}// Switch back to no_proxy {"\n"}proxy.setProxyOption(ProxyOption.NO_PROXY.name()) {"\n"}proxy.setProxyServerAddress("") {"\n"}proxy.setProxyServerPort(0) {"\n"}Map&lt;String, Object&gt; generalProperties = RunConfiguration.getExecutionGeneralProperties(); generalProperties.put(RunConfiguration.PROXY_PROPERTY, new Gson().toJson(proxy)); {"\n"}{"\n"}println proxy{"\n"}</code></pre> 
