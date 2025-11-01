---
title: Configure proxy authentication
hide_table_of_contents: false
toc_min_heading_level: 2
toc_max_heading_level: 2
---

If you are behind a proxy server, before activating Katalon licenses, you need to configure the Authentication proxy settings.

This guide will allow you to authenticate and activate your Katalon licenses while working behind a proxy server.

## General proxy authentication

1. Open Katalon Studio. In the toolbar, click on the *Profile* button and select **Log out**. 
   You will be logged out of your current account, and the **Welcome to Katalon Studio** dialog appears.
   
   <img src= "/108add10-bf7c-11ee-ac6d-0242c7a41fd4/ks-930-login-dialog.png" width="400" alt="Katalon login"/>
   
2. Click **Advanced settings** at the bottom of the dialog.

   <img src="https://tw-cdn.katalon.com/katalon-studio/get-started/activate-licenses/Login_Advanced_settings.png" alt="Katalon Studio Login Advanced Settings" width="400" /> 
   
   In the **Advanced Settings** dialog, select one of the three options below:
   - **No proxy**: There's no proxy.
   - **Use system proxy configuration**: Katalon Studio automatically syncs with the proxy server behind your system.
   - **Manual proxy configuration**: You can manually set up your proxy.

3. When you're done, click **Save**.
4. In the case you want to activate Katalon Runtime Engine with proxy settings, refer to the [Proxy arguments](/katalon-studio/execute-tests/katalon-runtime-engine/command-line-syntax-in-katalon-runtime-engine#id_5) for command-line syntax. 
   1. Whitelist the wild-card Katalon domain (*.katalon.com)
   2. Include the necessary proxy arguments in the command line interface. Choose `MANUAL_CONFIG` for the proxy option and make sure the credentials are correct.
   3. Avoid copying from another text editor because it may contain invisible/invalid characters that are not supported by Katalon TestOps. 
   
### Result
You've configured proxy authentication. You can continue signing in to Katalon Studio.

## Kerberos proxy authentication (Beta)

Starting from version 10.2.0, Katalon Studio supports setting proxy authentication with Kerberos on Windows machine. Before using, you need to add the `-Dkatalon.kerberosEnabled` parameter in the `katalon.ini` file.

1. On Windows, locate the `katalon.ini` file in the folder that contains Katalon Studio application. For example: `C:\Users\<username>\Downloads\Katalon_Studio_Windows_64-8.6.9\katalon.ini`.
2. Open the file in a text editor and add the following parameter: `-Dkatalon.kerberosEnabled=true`. 
3. Restart Katalon Studio.

### Result
You can now use Kerberos for proxy authentication in **Advanced settings**.