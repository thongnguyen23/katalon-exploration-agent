---
title: Install Katalon Studio
---
import useBaseUrl from '@docusaurus/useBaseUrl';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';



This article shows you  how to install Katalon Studio on macOS, Windows, and Linux. 


## Requirements

- A valid email to register your Katalon account.
- An active Internet connection to download Katalon Studio.
- Do a quick check on system requirements before using Katalon Studio. You can refer to this document here: [Supported Environment](/katalon-studio/supported-environments-for-katalon-studio-and-katalon-runtime-engine-kre#id_1).

## Installation steps

<Tabs>
  <TabItem value="macos" label="macOS" default>
    <ol xmlns="http://www.w3.org/1999/xhtml" className="ol steps"><li className="li step stepexpand anchor_top_offset" id="task-4619__download-ks"><span className="ph cmd">Download the suitable <span className="ph">Katalon Studio</span> version and edition for your macOS system on <a className="xref j-external-link" href="https://katalon.com/download" target="_blank">Katalon download page</a>.</span></li><li className="li step stepexpand"><span className="ph cmd">Double-click the downloaded <code className="ph codeph">.dmg</code> file to proceed with the installation.</span></li><li className="li step stepexpand"><span className="ph cmd">Drag <span className="ph">Katalon Studio</span> to the <span className="ph uicontrol">Application</span> folder when prompted.</span></li><li className="li step stepexpand"><span className="ph cmd">To start <span className="ph">Katalon Studio</span>, double-click the <span className="ph">Katalon Studio</span> application.</span><div className="itemgroup info">Once started, the application should display the splash screen similar to the following screenshot:</div><div className="itemgroup info"><img className="image" width={500} src={useBaseUrl("/cbf418b0-750d-11ed-a602-0242cfbc79b5/ks-855-activating.png")} /></div></li></ol> 
  </TabItem>
  <TabItem value="windows" label="Windows">
    <ol xmlns="http://www.w3.org/1999/xhtml" className="ol steps"><li className="li step stepexpand"><span className="ph cmd">Download the suitable <span className="ph">Katalon Studio</span> version and edition for your Windows system on <a className="xref j-external-link" href="https://katalon.com/download" target="_blank">Katalon download page</a>.</span></li><li className="li step stepexpand"><span className="ph cmd">Extract the downloaded <code className="ph codeph">.zip</code> file to <code className="ph codeph">C:\Users\&lt;username&gt;</code> folder.</span><div className="itemgroup info"><div className="note note note_note"><span className="note__title">Note:</span> <ul className="ul"><li className="li"><p className="p">For Windows users, if you are extracting Katalon Studio outside of the <code className="ph codeph">C:\Users\&lt;username&gt;</code> folder, make sure the current user has the Read/Write permission for Katalon Studio package or runs the software with administrator privileges.</p></li></ul></div></div></li><li className="li step stepexpand"><span className="ph cmd">Double-click the <code className="ph codeph">katalon.exe</code> file to start <span className="ph">Katalon Studio</span>.</span><div className="itemgroup info">Ensure you are using the default font size (set to 100%) in both <span className="ph">Katalon Studio</span> and your current OS to avoid the name field not being displayed on some pop-up windows. To adjust the font size:<ul className="ul"><li className="li">For Windows, you can refer to the Microsoft document here: <a className="xref j-external-link" href="https://support.microsoft.com/en-us/windows/change-the-size-of-text-in-windows-10-1d5830c3-eee3-8eaa-836b-abcc37d99b9a" target="_blank">Edit the font size</a>.</li><li className="li">For <span className="ph">Katalon Studio</span>: Go to <span className="ph uicontrol">Window</span> &gt; <span className="ph uicontrol">Preferences</span> &gt; <span className="ph uicontrol">General</span> &gt; <span className="ph uicontrol">Appearance</span> &gt; <span className="ph uicontrol">Colors and Fonts</span>. Select <span className="ph uicontrol">Dialog Font</span> and edit the font size.</li></ul></div></li></ol> 
  </TabItem>
  <TabItem value="linux" label="Linux">
    <section xmlns="http://www.w3.org/1999/xhtml" className="section context">Before installing, make sure you set up the environment required for <span className="ph">Katalon Studio</span>.</section> 
<div xmlns="http://www.w3.org/1999/xhtml" className="li stepsection"><strong className="ph b">Set up environment for <span className="ph">Katalon Studio</span></strong></div>
<ol xmlns="http://www.w3.org/1999/xhtml" className="ol steps"><li className="li step stepexpand"><span className="ph cmd">Install OpenJDK 17  (NOT Oracle JDK). Open your Terminal and type:</span><div className="itemgroup info"><pre className="pre codeblock"><code>sudo apt-get install openjdk-17-jre</code></pre><div className="note note note_note"><span className="note__title">Note:</span> <ul className="ul"><li className="li">If you update Katalon Studio from 8.x to 9.0.0, make sure to upgrade your OpenJDK to version 17.</li></ul></div></div><div className="itemgroup info">Once you finish the installation, your <code className="ph codeph">OpenJDK</code> information is displayed when you execute <code className="ph codeph">java - version</code> command.<p className="p"><img className="image" src={useBaseUrl("/95888a70-22b2-11ed-9930-0242fe3e4a3f/KS-INSTALLATION-View-OpenJDK-information.png")} /></p></div><div className="itemgroup info">If you have multiple versions of OpenJDK installed on your Ubuntu and the correct version is not being used, use the alternatives command to switch between them:<pre className="pre codeblock"><code>sudo update-alternatives --config java //then choose the openjdk-8-jre option</code></pre>Verify the version of the JDK again using <code className="ph codeph">java -version</code> command.<div className="note note note_note"><span className="note__title">Note:</span> <ul className="ul"><li className="li"><p className="p">After you have finished configuring the system, restart for your changes to take effect.</p></li></ul></div></div><div className="itemgroup info">You can find more information about the installation steps for other Linux distributions at the OpenJDK document: <a className="xref j-external-link" href="http://openjdk.java.net/install/" target="_blank">How to download and install prebuilt OpenJDK packages.</a></div></li><li className="li step stepexpand"><span className="ph cmd">Download the suitable  <span className="ph">Katalon Studio</span> version and edition for your Linux system on <a className="xref j-external-link" href="https://katalon.com/download" target="_blank">Katalon download page</a>.</span></li><li className="li step stepexpand"><span className="ph cmd">Use the <code className="ph codeph">-xf</code> command to extract the <code className="ph codeph">tar.gz</code> file, for example: <code className="ph codeph">$tar -xf Katalon_Studio_PE_Linux_64-8.5.5.tar.gz</code>.</span><div className="itemgroup info">In the extracted folder, you can find the <span className="ph">Katalon Studio</span> app.</div></li><li className="li step stepexpand"><span className="ph cmd">Open <span className="ph">Katalon Studio</span> by double-clicking on <span className="ph">Katalon Studio</span>, or run <code className="ph codeph">cd ./katalon</code> in your Terminal.</span></li></ol>
  </TabItem>
</Tabs>

## Install Katalon Studio in a restricted environment

:::note
This workaround applies to Katalon Studio Enterprise (KSE) v10.1.0 and later.
:::

 In environments where system directories such as `C:\Program Files` are write-protected, it's still possible to run applications by redirecting their configuration and workspace data to user-accessible locations. This guide explains how to configure an application to operate normally under such restrictions.

### Prerequisites
- The application is already extracted or installed in a directory you cannot write to (e.g., `C:\Program Files\AppName`).
- You have read and execute access to the application folder.
- The application uses a configuration file (e.g., app.ini or app.cfg) to define runtime data and configuration paths.

### Steps

1. Copy the `resources` files to a writable directory.
  1. Navigate to the application's `configuration\resources` directory.
  2. Copy the entire `resources` folder.
  3. Paste it into a writable path under your user profile, for example:
    ```
    C:\Users\<your-username>\.yourapp\config\resources
    ```
    :::tip
    Create the `.yourapp\config` directory structure manually if it doesn't exist.
    :::

2. Modify the configuration file.
  Most desktop applications provide an `.ini` or similar file to define startup parameters. You can override the default configuration and workspace paths here.
  1. Open the application's configuration file (e.g., `app.ini`) located in the root folder of the application.
  2. Add or update the following lines to redirect configuration and workspace paths to a user-writable location:
    ```
    -data
    @user.home/.yourapp/config
    -configuration
    @user.home/.yourapp/configuration
    ```
    Replace `.yourapp` with a folder name relevant to your application if needed.

The application runs from a restricted directory without needing elevated permissions.

All runtime, workspace, and configuration files are written to your user profile directory.

Application behavior remains unchanged for the end user.

:::note Notes
- Ensure the user directory has sufficient space and permissions for storing configuration files and logs.
- Back up the user-specific configuration directory if needed for portability or troubleshooting.
- This approach is useful in enterprise environments with strict system directory policies.
:::