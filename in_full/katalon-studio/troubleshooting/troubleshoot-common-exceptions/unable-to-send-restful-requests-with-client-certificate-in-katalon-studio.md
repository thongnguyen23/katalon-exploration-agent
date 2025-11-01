---
hide_title: true
title: Unable to send RESTful requests with client certificate in Katalon Studio
---

# <a id="troubleshooting-ibtbdxnk" class="anchor_top_offset"/><a id="ariaid-title1" class="anchor_top_offset"/>Unable to send RESTful requests with client certificate in Katalon Studio

<section xmlns="http://www.w3.org/1999/xhtml" className="section condition"><p className="p">When trying to send RESTful requests using a client certificate, you may encounter the following error:</p><div className="p"><pre className="pre codeblock"><code>Could not initialize class org.apache.commons.ssl.KeyMaterial</code></pre></div></section> 

#### Cause

The root cause of the issue is related to the outdated `yet-commons-ssl-0.3.11` library, which is used to parse the certificate file in Katalon Studio. This library does not support Java versions 9 and later.

Since Katalon Studio version 9.x, the embedded JRE has been upgraded to JRE 17, which is incompatible with this library. As a result, the system searches for the JKS keystore format, even when the certificate is in PKCS12 format.

You need to update the keystore format from PKCS12 to JKS. Follow these steps:
#### Remedy
1. Locate the security folder inside the JRE used by Katalon Studio: `<path to your Katalon Studio product>\jre\conf\`.
2. Open the file named `java.security` in a text editor.
3. Change the keystore type.
- Find the line: `keystore.type=pkcs12`
- Change it to: `keystore.type=jks`

4. Save the changes, close the file, and restart Katalon Studio to apply the updated configuration.
Was this page helpful?