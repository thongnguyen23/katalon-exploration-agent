---
hide_title: true
title: Set desired capabilities in Windows desktop app testing
---
import useBaseUrl from '@docusaurus/useBaseUrl';


# Set desired capabilities in Windows desktop app testing

:::note
- Starting from Katalon Studio 10.3.0, Windows Desktop app testing is available again as a beta feature. It supports spy, record, and execution of basic test cases using a new built-in driver based on the FlaUI library, replacing WinAppDriver. No separate installation is required.
- If you are using earlier 10.x versions of Katalon Studio, Windows Desktop app testing remains unavailable due to incompatibility with the W3C WebDriver protocol. To access the legacy WinAppDriver-based functionality, use Katalon Studio 9.x. For details, refer to the [Katalon Studio Release Notes: Version 10.x](/katalon-studio/release-notes/katalon-studio-release-notes-version-10.x).
:::

<p xmlns="http://www.w3.org/1999/xhtml" className="shortdesc">This article shows you how to configure desired capabilities for Windows Desktop Application testing.</p>

<ol xmlns="http://www.w3.org/1999/xhtml" className="ol steps"><li className="li step stepexpand"><span className="ph cmd">Go to <span className="ph uicontrol">Project</span> &gt; <span className="ph uicontrol">Settings</span> &gt; <span className="ph uicontrol">Desired Capabilities</span> &gt; <span className="ph uicontrol">Windows</span> to open the Windows desired capabilities settings.</span><div className="itemgroup info"><p className="p"><img className="image" width={650} src={useBaseUrl("/8e461829-4e42-44a0-9987-32eecb594b31/ks-project-settings-desired-caps.png")} /></p><p className="p">Alternatively, start your <span className="ph uicontrol">Windows Recorder/Spy</span> or <span className="ph uicontrol">Native Windows Recorder</span> session. In the <span className="ph uicontrol">Configuration</span> field, click <span className="ph uicontrol">Edit</span>.</p><p className="p"><img className="image" width={650} src={useBaseUrl("/a5ab6f8d-a3d3-413d-9c6b-1d6767dc10b5/ks-windows-recorder-click-edit.png")} /></p></div></li><li className="li step stepexpand"><span className="ph cmd">In <span className="ph uicontrol">WinAppDriver URL</span>, enter the URL to the WinAppDriver server following this format: <code className="ph codeph">http://&lt;ip-address&gt;:&lt;port&gt;</code>. By default, Katalon Studio is set to <code className="ph codeph">http://127.0.0.1:4723</code>.</span></li><li className="li step stepexpand"><span className="ph cmd">In the table below, click <span className="ph uicontrol">(+) Add</span> to add desired capabilities.</span><div className="itemgroup info">Katalon Studio supports the same capabilities as WinAppDriver does. To learn more about the supported capabilities, refer to this WinAppDriver document: <a className="xref j-external-link" href="https://github.com/microsoft/WinAppDriver/blob/master/Docs/AuthoringTestScripts#supported-capabilities" target="_blank">WinAppDriver supported capabilities</a>.<div className="note note note_note"><span className="note__title">Note:</span> <p className="p">Katalon only supports <code className="ph codeph">appArguments</code> and <code className="ph codeph">appWorkingDir</code> capabilities in <span className="ph uicontrol">Native Windows Recorder</span>:</p><ul className="ul"><li className="li"><code className="ph codeph">appArguments</code>: Support passing arguments to the AUT. You can also use this desired capabilities to record action without opening a Windows.</li><li className="li"><code className="ph codeph">appWorkingDir</code>: Specify the Application Under Test working directory.</li></ul></div></div></li></ol> 

## Set up Desired Capabilities in Katalon Studio 10.3.0

Katalon Studio 10.3.0 introduces a new built-in Windows driver that follows the W3C WebDriver specification. As a result, all **non-standard desired capabilities** must now include the `appium:` namespace prefix.

If you previously defined custom capabilities in **Project Settings > Desired Capabilities > Windows**, update them as follows:

| Legacy Capability | Updated Format         |
| ----------------- | ---------------------- |
| `appWorkingDir`   | `appium:appWorkingDir` |
| `appArguments`    | `appium:appArguments`  |

To update:

1. Go to **Project > Settings > Desired Capabilities > Windows**.
2. Update any non-standard capabilities by adding the `appium:` prefix.
3. Click **Apply and Close** to save your changes.

:::important Notes
- You only need to update the desired capabilities once per project.
- The capability `ms:waitForAppLaunch` is no longer supported.
- Use the built-in keyword `Windows.delay(<numberOfSeconds>)` to pause test execution and wait for the application to launch.
:::

## Use cases

### Example 1: Set delaying time for an app launch

<p xmlns="http://www.w3.org/1999/xhtml" className="p">The following example shows you how to set desired capabilities   to wait for a defined amount of time before launching an application.</p> 
<div xmlns="http://www.w3.org/1999/xhtml" className="note important note_important"><span className="note__title">Important:</span> <ul className="ul"><li className="li">Download and install WinAppDriver version 1.2
      onwards. You can refer to this document to install WinAppDriver: <a className="xref" href="/katalon-studio/manage-projects/set-up-projects/windows-desktop-apps-testing/set-up-winappdriver-in-katalon-studio">Set
        up WinAppDriver</a>.</li><li className="li">Appium version 1.16.0 onwards to support WinAppDriver.</li></ul></div>
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Go to the desired capabilities settings, click   <span className="ph uicontrol">Add</span>, then input the following value:</p> 

| **Name** | **Type** | **Value** |
| --- | --- | --- |
| ms:waitForAppLaunch | string | 25(*) |

(*) *This means delaying the app launch for 25 seconds. The maximum is 50 seconds.*

<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" width={650} src={useBaseUrl("/62eeec2f-9885-49de-9888-fa37f5fabbf6/ks-windows-recorder-desired-caps.png")} alt="Delay app launch" /></p> 

### Example 2: Use desired capabilities with Native Windows Recorder

<p xmlns="http://www.w3.org/1999/xhtml" className="p">The following example shows you how to set desired capabilities in Native Windows Recorder.</p> 
<p xmlns="http://www.w3.org/1999/xhtml" className="p">Open the <span className="ph uicontrol">Native Windows Recorder</span> session dialog, in the <span className="ph uicontrol">Configuration</span> field, click <span className="ph uicontrol">Edit</span>.</p> 

Click (+) Add and input the following values:

| **Name** | **Type** | **Value** |
| --- | --- | --- |
| appWorkingDir | String | C:\User\**user_name**\Desktop\workspace\katalon |
| appArguments | String | --arg1 --arg2 |

<p xmlns="http://www.w3.org/1999/xhtml" className="p"><img className="image" width={650} src={useBaseUrl("/87a75d7c-5e50-4a3d-a668-e7092fb2a93d/ks-windows-desired-caps-example-2.png")} /></p> 
