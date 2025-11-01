---
title: Unable to find valid certification path to request target
---

### Condition & Cause 

You encounter the error message `“PKIX path building failed: sun.security.provider.certpath.SunCertPathBuilderException: unable to find valid certification path to requested target“` when running with TestCloud.

This issue happens because the generated CA certificate is not set as trusted by the system, therefore restricts Katalon Studio to connect with TestCloud.

### Solution

You need to download the cert chain from the browser (Chrome/Firefox) and import it into the Local System Trusted Store.

#### Export and download the certificate chain from the browser

1. Make sure that the proxy server is enabled.
2. Open the Chrome and access https://testcloud.katalon.com/healthcheck.
3. Export and download the certificate chain as follows:
   1. Click the lock icon from URL address bar.
   2. Select **Connection is secure** > **Certificate is valid**.
   <img src="https://tw-cdn.katalon.com/katalon-testcloud/troubleshooting/testcloud-check-connection.png" alt="Select Connection is secure" width="600" />
   3. In the Certificate Viewer dialog, select the **Details** tab then **Export**.
   <img src="https://tw-cdn.katalon.com/katalon-testcloud/troubleshooting/testcloud-select-details-tab.png" alt="Select the Details tab" width="400" />
   4. Save the certificate in the “Base64-encoded ASCII, certificate chain” format.
   <img src="https://tw-cdn.katalon.com/katalon-testcloud/troubleshooting/testcloud-save-cert.png" alt="Download certificate" width="600" />

#### Install the certificate into Local System Trusted Store

:::info Permission Required
- To complete this action, the system must access the Trusted Root Certification Authorities store. Please run the application with administrator privileges to allow access to the local system certificate store.
:::

Open Windows PowerShell with Administrator and run the following PowerShell command to install it into Local System Trusted Store. 

```jsx
Import-Certificate -FilePath "downloaded-file-location" -CertStoreLocation Cert:\LocalMachine\Root
```

Replace the `downloaded-file-location` with the certificate's location, for example,  `C:\Users\user.name\Downloads\katalon.crt`.