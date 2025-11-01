---
hide_title: true
title: Activate licenses
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# Activate licenses

<p xmlns="http://www.w3.org/1999/xhtml" className="p">In this article, we will guide you through the activation of your Katalon Studio Enterprise (KSE) and Katalon Runtime Engine (KRE) licenses.</p> 
<div xmlns="http://www.w3.org/1999/xhtml" className="note note note_note"><span className="note__title">Note:</span> <ul className="ul"><li className="li">To learn more about the details of Katalon licenses, see <a className="xref" href="#">Types of Licenses</a>.</li><li className="li">If you are behind a proxy server, before activating Katalon licenses, you need to configure the Authentication proxy settings. To learn more about how to configure a proxy, see <a className="xref" href="/katalon-studio/katalon-studio-enterprise-and-katalon-runtime-engine-license/configure-proxy-authentication">Configure proxy authentication</a>.</li></ul></div>

## Activate your Katalon Studio Enterprise (KSE) license

:::note Requirements
- The Owner or Admin of your Organization have assigned a KSE license to your user account before doing this step; or you are a Trial user who can evaluate KSE for 30 days.
- You have downloaded and installed Katalon Studio Enterprise. For detailed instruction, see [Install Katalon Studio](/katalon-studio/get-started/install-katalon-studio).
- If you have previously logged in to a Katalon account in Katalon Studio, click on the **Profile** button and select **Log out** to prompt the dialog.

    <img className="image" width={400} src={useBaseUrl("/4b532ea0-f396-11ed-878a-0242c7a41fd4/ks-profile-log-out-task-3426.png")} alt="The profile button and the log out option in Katalon Studio." />
:::

1. Open the application. The **Welcome to Katalon Studio Enterprise** dialog automatically pops up.

    <img className="image" width={300} src={useBaseUrl("/ee571f79-1131-4f86-b0c0-1f4cf5870d48/ks-970-welcome-dialog.png")} alt="The Katalon Studio activation dialog box." />

2. Click **Log in from Browser**. Log in by using your preferred credentials.

    <img className="image" width={300} src={useBaseUrl("/6144575d-6b03-4ee6-8b02-43f88e8e9959/ks-950-login-options.png")} />

    If you log in with SSO, see [Log in to Katalon Studio with SSO](/katalon-platform/administer/administration-tasks/security-settings/single-sign-on-configurations#task-7202).

Upon successful login, you are redirected to Katalon Studio Enterprise.

### Advanced Settings

You can configure your advanced login settings if:
- You are logging in via a License Server.
- You need to [configure a proxy connection](/katalon-studio/katalon-studio-enterprise-and-katalon-runtime-engine-license/configure-proxy-authentication).

1. Open the application. The **Welcome to Katalon Studio Enterprise** dialog automatically pops up. 

2. Click Advanced settings link located below the login options.

3. The **Advanced Settings** dialog pops up. Set up your configuration options.
    1. **License server address**: Enter the Private Instance URL used for license authentication.
    2. **Launch browser login site in**: If you select **Log in from browser**, choose where the login page should open:

        - **In-app browser**: Opens a built-in browser within Katalon Studio. Use this if you want to keep the login flow contained or if your system restricts launching external browsers.
        
        - **System default browser**: Opens the login page in your default web browser (e.g., Chrome, Safari). Recommended if you're already signed in to your Katalon or SSO account in your main browser or prefer using browser-based tools like password managers.
    3. Click **Save** to apply your login settings.

Your advanced login configuration is now saved and ready for use.

:::note
For **On-Premises users on versions before 3.0.0**: If you select login via **License server**, the **Log in with License server** dialog pops up. The Private Instance URL you have saved in Advanced settings in Step 3 is prepopulated. Enter your email address and password to continue.

    <img src="https://tw-cdn.katalon.com/katalon-studio/get-started/activate-licenses/Log_in_from_browser_with_license_server_address.png" alt="Katalon Studio Login with License server" width="400" />
:::

### Enable Remember Me in Login 

When you enable the **Remember Me** option, you do not need to re-enter your username and password each time you start Katalon Studio or when you’re signed out due to session expiration or inactivity.

<img src= "https://tw-cdn.katalon.com/katalon-studio/get-started/activate-licenses/Enable_Remember_Me_login.png" alt="Login and enable Remember Me" width="400" />

:::note Notes
- This feature applies when you login via **License Server** and **Log in from Browser**.
- If you are logged out due to `Session Expired`, `License Expired`, or `Idle Timeout Exceeded`, Katalon Studio displays a notification dialog informing you of the reason and provide options to quickly sign back in through the Relogin feature.
    - Login with another account: When clicked, Katalon Studio navigates you to the login screen, where you can sign in manually using your preferred method.
    - Relogin: Available only if you previously selected **Remember Me** in the login dialog. Katalon Studio automatically signs you back in using the same method as your initial login (either Login with Browser or License Server).

        Example: If you are logged out due to inactivity, the Relogin dialog is displayed:

        <img src= "https://tw-cdn.katalon.com/katalon-studio/get-started/activate-licenses/Logout_inactivity.png" alt="Logout due to inactivity" width="300" />
:::

## Activate your Katalon Runtime Engine (KRE) license

Your Katalon Runtime Engine (KRE) license is activated automatically after the owner or administrator of your organization has granted you a KRE license.

To use KRE, you need to authenticate your account with your Katalon API key.

To view your API key, refer to this guide: [API Keys](/katalon-platform/administer/profile/katalon-api-key-in-katalon-testops).

:::info notes
To view details about your current license, see: [View License Details](/katalon-studio/katalon-studio-enterprise-and-katalon-runtime-engine-license/view-license-details).
:::

## Activate a license while offline

An offline license needs to be activated before it can be used.
:::tip requirements
- A machine ID. To view your machine ID, see [How Katalon generates a machine ID](/katalon-studio/katalon-studio-enterprise-and-katalon-runtime-engine-license/how-katalon-generates-a-machine-id).
- A `KSE_<machine_ID>.lic` or `KRE_<machine_ID>.lic` file.
    - To get this license file, provide your machine ID to your organization's owner or administrator and ask them to grant you an offline license.
    - They can learn how to grant an offline license through this guide: [Grant an offline license to users](/katalon-platform/administer/administration-tasks/manage-licenses/grant-a-katalon-license#grant-an-offline-license-to-users).
:::

Receive your license file from your organization owner or administrator and execute the following steps:

Put your .lic file in its appropriate license folder.

Note that `.katalon` is a hidden folder. To find the license folder in your computer, search for:

- Windows: `C:\\Users\\<user_name>\\.katalon\\license`
- Linux: `/home/<user_name>/.katalon/license`
- macOS: `/Users/<user_name>/.katalon/license`

### Activate KSE offline license

<p xmlns="http://www.w3.org/1999/xhtml" className="shortdesc">Perform this step only after you have copied your corresponding <code className="ph codeph">.lic</code> file to its directory. If you have not yet, read: <a className="xref" href="/katalon-studio/get-started/activate-licenses#task-6026">Activate a license while offline</a>. </p> 
<section xmlns="http://www.w3.org/1999/xhtml" className="section context">Upon opening Katalon Studio for the first time, or while you are logged out, you will automatically be prompted to activate your license by a pop-up window. </section> 
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol steps"><li className="li step stepexpand"><span className="ph cmd">In the login  dialog, click <span className="ph uicontrol">Offline license</span>.</span><div className="itemgroup info"><img className="image" width={500} src={useBaseUrl("/84588ab0-76fe-11ee-8403-0242c7a41fd4/ks-900-offline-activation.png")} alt="The Katalon Studio activation dialog." /></div></li><li className="li step stepexpand"><span className="ph cmd">In the <span className="ph uicontrol">License file</span> section, click <span className="ph uicontrol">Choose file</span>       to select your <code className="ph codeph">.lic</code> file.</span></li><li className="li step stepexpand"><span className="ph cmd">Click <span className="ph uicontrol">Activate</span>. </span></li></ol> 
<section xmlns="http://www.w3.org/1999/xhtml" className="section result">Katalon Studio Enterprise offline is ready for use. </section> 

### Activate KRE offline license

<p xmlns="http://www.w3.org/1999/xhtml" className="shortdesc">Determine the correct directory for your license file before executing this step. If you have not yet, read: <a className="xref" href="/katalon-studio/get-started/activate-licenses#task-6026">Activate a license while offline</a>.</p> 
<section xmlns="http://www.w3.org/1999/xhtml" className="section context">Activate KRE offline by:</section> 
<div xmlns="http://www.w3.org/1999/xhtml" className="li step p"><span className="ph cmd">Putting your <code className="ph codeph">KRE_&lt;machine_ID&gt;.lic</code> file in the license folder. </span><div className="itemgroup info"><div className="note note note_note"><span className="note__title">Note:</span> <ul className="ul"><li className="li"><p className="p">To execute multiple sessions in parallel, put multiple license files in the license folder.</p></li></ul></div></div></div>
<section xmlns="http://www.w3.org/1999/xhtml" className="section result">Your KRE license is now activated. Every time you start running a test with KRE, KRE automatically verifies that your license file is available and valid.<p className="p">It should look as the image below.<img className="image" width={500} src={useBaseUrl("/07331b10-df9e-11ed-b480-0242cfbc79b5/task_9082_kre_offline.png")} alt="Activating Katalon Runtime Engine offline." /></p></section> 

## Activate a license with Private Instance

:::note Requirements
- You have downloaded and installed Katalon Studio Enterprise.
- A private instance URL. To learn more about Private Instance, contact our sales team via <kbd className="ph userinput">business@katalon.com</kbd>.
:::

### Activate a KSE license with Private Instance

To log in and activate your Katalon Studio Enterprise license with Private Instance:

1. Open the application. The **Welcome to Katalon Studio Enterprise** dialog automatically pops up.

    <img className="image" width={400} src={useBaseUrl("/669e2490-e282-11ee-b3a4-0242c7a41fd4/ks-970-login-dialog.png")} alt="The Katalon Studio activation dialog box." />

    Click **Log in from License server**.

2. Select your login option.
    1. If you select **Log in from License server**, a dialog pops up where you can enter your Private Instance URL and credentials.
        - In the **License server address** field: Enter the Private Instance URL used for authentication.
        - Enter your email address and password.

        <img src="https://tw-cdn.katalon.com/katalon-studio/get-started/activate-licenses/Log_in_from_browser_with_license_server_address.png" alt="Katalon Studio Login with License server" width="400" />

        Click **Log in** to continue.

    2. For On-Premises users on version 3.0.0 onwards, you can select **Log in from a browser** after setting your On-Premises server URL in **Advanced Settings**. See [Advanced Settings](#advanced-settings).

You have successfully logged in using your Private Instance and activated your KSE license.

### Activate a KRE license with Private Instance

To activate a KRE license with Private Instance, pass the Private Instance URL used for authentication to the `-serverUrl` parameter.

For example: 

```jsx
./katalonc -noSplash -runMode=console -projectPath="/Users/katalon/Downloads/web-visual-testing-samples-master/Web UI Tests with TestOps Vision.prj" -retry=0 -testSuitePath="Test Suites/TS_RegressionTest_With TestOps Vision" -browserType="Chrome" -executionProfile="default" -apiKey=<your-API-key> --config -proxy.auth.option=NO_PROXY -proxy.system.option=NO_PROXY -proxy.system.applyToDesiredCapabilities=true -serverURL="https://admin-tenant1.katalon-cloudops.com/"

```
:::info notes
- For a better experience with Katalon Studio, you can also install our plugins. See [Using Plugins with Katalon Studio Enterprise License](/katalon-platform/plugins-and-add-ons/katalon-store/katalon-studio-plugins/using-katalon-store-plugins).
- If you have any activation problems, see [Troubleshoot Activation Problems](/katalon-platform/troubleshooting/troubleshooting-common-administrative-issues/account-activation-problems).
- For further instructions on working with KRE, refer to [Command Syntax](/katalon-studio/execute-tests/katalon-runtime-engine/get-started-with-katalon-runtime-engine#task-7433).
:::
