---
title: Command-line syntax in Katalon Runtime Engine
---
import useBaseUrl from '@docusaurus/useBaseUrl';


This guide lists out the supported command-line syntax and arguments of Katalon Runtime Engine.

:::note note 
To upgrade the default JRE 8 to higher versions, refer to this document for further details: [Run tests with another JRE in the command line](/katalon-studio/get-started/workspace-settings/katalon-studio-preferences/set-a-new-default-jre-for-test-projects-in-katalon-studio#task-2496).
:::

## Requirements

- Katalon Runtime Engine is installed. See: [Get started with Katalon Runtime Engine](/katalon-studio/execute-tests/katalon-runtime-engine/get-started-with-katalon-runtime-engine).
- A Katalon Runtime Engine License. To learn more about activating your license, you can refer to this document: [Katalon license](/katalon-studio/get-started/activate-licenses).
 
## Use plugins in console mode

You can also continue using your plugins of choice with console commands. See this guide: [Use Plugins in Console Mode](/katalon-platform/plugins-and-add-ons/katalon-store/katalon-studio-plugins/using-katalon-store-plugins#id_9).

## General arguments

Here's the list of options supported for the `katalonc` commands for Katalon Studio.

### Required arguments

**`-runMode=console`** <br/> 
Enable console mode.

**`-projectPath=<path>`** <br/> 
Specify the project location (include .prj file). The absolute path must be used in this case.

**`-testSuitePath=<path>`** <br/> 
Specify the test suite file (without extension .ts). The relative path (root being project folder) must be used in this case.

**`-testSuiteCollectionPath=<path>`** <br/> 
Specify the test suite file (without extension .tsc). The relative path (root being project folder) must be used in this case.

**`-browserType=<browser>`** <br/> 
Specify the browser type used for Test Suite execution or Test Suite Collection execution (the specified browser is used for all test suites in that collection).
  
  The following browsers are supported in KRE:
  - Firefox
  - Chrome
  - IE
  - Edge
  - Edge Chromium
  - Safari
  - Remote
  - Android
  - iOS
  - Web Service

:::info info
- If `-testSuitePath` is specified, `-testSuiteCollectionPath` is not required.
- Only Chrome, Firefox, and Remote are available for use in the Linux version.  
- **Web Service** is used for Web Service test execution.
- To execute Web Service testing with TestCloud, make sure to specify `-browserType="TestCloud"` in your command. The `-testcloudEnvironmentId` should correspond to selecting TestCloud Desktop browser > Linux > Chrome (any version).
:::

**`-apiKey=<Your_API_Key>`** or **`-apikey=<Your_API_Key>`** <br/> 
API Keys are used to represent a user's credentials. See: [API Keys](/katalon-platform/administer/settings/katalon-api-key-in-katalon-testops).


### Optional arguments

**`statusDelay=<seconds>`** <br/> 
System updates execution status of the test suite after the specified delay (in seconds).

**`retry=<number of retry times>`** <br/> 
Number of times the test cases in the test suite are run.

**`retryStrategy=<allExecutions | failedExecutions | immediately>`** <br/> 
Supported from version 7.6 onwards. Specifies which executions to retry (overrides the test suite setting):  
  - **allExecutions**: Retry all executions when the test suite fails.  
  - **failedExecutions**: Retry only the failed executions.  
  - **immediately**: Retry failed executions immediately (Enterprise only).

**`maxFailedTests=<T>`** 
  - From version 8.1.0, terminates execution when the number of failed tests reaches `T`.  
  - Counts failures in test cases, retried test cases, iterations, and retried iterations.

**`reportFolder=<path>`** <br/> 
Destination folder for saving report files. Supports absolute or relative paths.

**`reportFileName=<name>`** <br/> 
Specifies the report file name (.html, .csv, .log). Default is `report` if not set.  
  >**Note:** Only interpreted if `reportFolder` is specified.

**`sendMail=<e-mail address>`** <br/> 
Email address to receive the report files. If not specified, reports are not sent.

**`remoteWebDriverUrl=<remote web server url>`** <br/> 
URL for the remote WebDriver server.

**`serverUrl=<server url>`** <br/> 
URL for activating a KRE license. Required for Private Instance activation in console mode from v8.3.5 onwards.

**`appiumDirectory=<path>`** <br/> 
Path to the Appium installation (e.g., `/opt/homebrew/lib/node_modules/appium`).

**`remoteWebDriverType=<Selenium | Appium>`** <br/> 
Type of the remote WebDriver.  
  >**Note:** Only interpreted if `remoteWebDriverUrl` is set.

**`deviceId=<Android device ID / iOS UUID>`** <br/> 
Device ID for executing tests.  
  >**Note:** Only interpreted if `browserType` is set.

**`executionProfile`** <br/> 
Specifies the execution profile. From v7.6.0 onwards, applies to all test suites in a collection.

**`delayBetweenInstances=<value>`**
  - Sets a delay between test suite executions in a collection.  
  - Value: Integer between 0 and 999 (seconds).  
  - Console log message shown when a suite is ready to start.

**`g_<variable_name>`** <br/> 
Override Execution Profile variables (e.g., `g_userName="admin"`).

**`testSuiteQuery=<search-query>`** <br/> 
Override dynamic test suite search queries from CLI.  
  Example: `testSuiteQuery="ids=(Test Cases/TC1,Test Cases/TC2)"`

**`testSuiteCollectionQuery`** <br/> 
Enable/Disable test suites in a collection via index.  
  - `testSuiteCollectionQuery="indexes=(0,3)"` enables the 1st and 4th test suites.  
  - No index = all disabled.

**`maxResponseSize`** <br/> 
Override project setting for max response size (from v7.6).  
  >**Example**: `maxResponseSize=400`

**`-licenseRelease -orgID=<organization ID>`** <br/> 
Release previous execution session before checking license.  
  >**Example**: `licenseRelease=true`, `orgID=89151`

**`--config webui.autoUpdateDrivers=true`** <br/> 
Allows WebDriver binaries to auto-update in console mode.

### License retry mechanism (optional arguments)

These parameters allow you to control how KRE handles license retries when no license is available during test execution. Use them together to specify how often and for how long KRE should retry license activation.

**`-enableLicenseRetry`** <br/>
Enable or disable the license retry mechanism when no license is available.

- **Default in version 9.x:** `false`  
- **Default in version 10.x:** `true`  
- The input must be a Boolean

---

**`-licenseRetryMaxDuration`**
Specify the maximum duration (in minutes) that KRE will retry license activation. After this time, KRE stops retrying if activation is not successful.

- **Default value:** `20`
- **Type:** Integer

---

**`-licenseRetryInterval`**
Specify how often (in minutes) KRE should retry the license activation attempt.

- **Default value:** `5`
- **Type:** Integer
- **Constraint:** Must be ≥ `3`
- **Note:** Should not exceed `licenseRetryMaxDuration`.

---

**`-licenseRetryMaxJitter`**
Specify the jitter factor (in minutes) to add randomness to the retry interval.

- **Default value:** `2`
- **Type:** Integer
- **Formula:** `licenseRetryMaxJitter / licenseRetryInterval`
- **Constraint:** Should not exceed `licenseRetryInterval`.

---

:::important How these parameters work together
When `-enableLicenseRetry` is set to `true`, KRE will attempt to reactivate the license whenever it encounters an issue where no license is available.

You can control how long the retry process will last using `-licenseRetryMaxDuration`.

The `-licenseRetryInterval` specifies how frequently KRE should retry, while `-licenseRetryMaxJitter` adds some randomness to avoid predictable retry intervals.
:::

---

#### Example usage

Configure KRE to retry license activation for up to 10 minutes, with retry attempts every 3 minutes and a jitter factor of 1 minute:

``` jsx 
katalon.exe -noSplash -runMode=console -retry=2 -retryStrategy=failedExecutions -statusDelay=60 -projectPath="%projectPath%" -testSuitePath=%testSuite% -browserType="Firefox" -executionProfile="default" -apiKey="<your_api_key>" -orgID=<your_org_id> -testOpsProjectId=<your_project_id> --config -webui.autoUpdateDrivers=true -licenseRelease=true -reportFolder=./Reports/Your_Report_Folder -enableLicenseRetry=true -licenseRetryMaxDuration=10 -licenseRetryInterval=3 -licenseRetryMaxJitter=1 
```

### Windows-specific arguments

**`-consoleLog`** <br/>
Display log in the console. Only use this option when running Katalon Studio in Windows Command Prompt. Do not use this option in other OSes or CI tools, for example Jenkins.

**`-noExit`** <br/>
Keep the console open after the execution is completed. Only use this option when running Katalon Studio in Windows Command Prompt. Do not use this option in other OSes or CI tools, for example Jenkins.


## Proxy arguments

:::tip notes
- You can exclude a list of hosts from proxy in the **Manual proxy configuration**. For more details, refer to: [Proxy settings](/katalon-studio/get-started/workspace-settings/katalon-studio-preferences/preferences-in-katalon-studio).
- You can pass proxy details via a request object in Web Service testing. For more details, refer to: [Override proxy details in the test script](/katalon-studio/get-started/workspace-settings/katalon-studio-preferences/preferences-in-katalon-studio).
:::

These proxy options must be used with `--config` parameter, for example: `--config -proxy.auth.option=MANUAL_CONFIG` 

```jsx 
katalonc -noSplash -runMode=console -projectPath="C:\Users\Katalon Studio\Project\YourProject.prj" -retry=0 -testSuitePath="Test Suites/download" -executionProfile="default" -browserType="Chrome" --config -proxy.auth.option=MANUAL_CONFIG -proxy.auth.server.type=HTTP -proxy.auth.server.address=192.168.1.16 -proxy.auth.server.port=16000 -proxy.system.option=MANUAL_CONFIG -proxy.system.server.type=HTTP -proxy.system.server.address=127.0.0.1 -proxy.system.server.port=12701 -proxy.system.username=katalon -proxy.system.password=T3stP@zZW0rol -proxy.system.applyToDesiredCapabilities=true
```

### Authentication proxy arguments

> Use these arguments to configure proxy settings for Katalon Runtime Engine (KRE), especially in environments that require authentication.

---

**`proxy.auth.option`** 
Specifies how KRE should handle proxy settings.

- **Options:** `NO_PROXY`, `USE_SYSTEM`, `MANUAL_CONFIG`

---

**`-proxy.auth.server.type`**  
Defines the type of proxy server.

- **Options:** `HTTP`, `HTTPS`, `SOCKS`

---

**`-proxy.auth.server.address`**
Sets the address of the proxy server.
  >**Example:** `localhost`, `katalon.com`

---

**`-proxy.auth.server.port`**  
Defines the port number used by the proxy server.
  >**Example:** `80`, `8080`, `9999`

---

**`-proxy.auth.excludes`**  
Specifies addresses that should bypass the proxy.
  >**Example:** `127.0.0.1`, `localhost`, `myserver.com`

---

**`-proxy.auth.username`**  
This option is required if the specified proxy server requires authentication.
  >**Example:** `MyProxyUsername`  


---

**`-proxy.auth.password`**  
This option is required if the specified proxy server requires authentication.
  >**Example:** `MyProxyPassword`  



### System proxy arguments

**`-proxy.system.option`**  
The available values for this option are: `NO_PROXY`, `USE_SYSTEM`, or `MANUAL_CONFIG`.

---

**`-proxy.system.server.type`**  
Available types: `HTTP`, `HTTPS`, or `SOCKS`.

---

**`-proxy.system.server.address`**  
Example: `localhost`, `katalon.com`.

---

**`-proxy.system.server.port`**  
Example: `80`, `8080`, `9999`.

---

**`-proxy.system.excludes`**  
Example: `127.0.0.1`, `localhost`, `myserver.com`.

---

**`-proxy.system.username`**  
Example: `MyProxyUsername`. This option must be specified if your proxy requires authentication.

---

**`-proxy.system.password`**  
Example: `MyProxyPassword`. This option must be specified if your proxy requires authentication.

---

**`-proxy.system.applyToDesiredCapabilities`**  
Example: `true` or `false`.

---

#### **For versions below 7.5.0**

**`-proxy.option`**  
Available values: `NO_PROXY`, `USE_SYSTEM`, or `MANUAL_CONFIG`.

---

**`-proxy.server.type`**  
Available types: `HTTP`, `HTTPS`, or `SOCKS`.

---

**`-proxy.server.address`**  
Example: `localhost`, `katalon.com`.

---

**`-proxy.server.port`**  
Example: `80`, `8080`, `9999`.

---

**`-proxy.excludes`**  
Example: `127.0.0.1`, `localhost`, `myserver.com`.

---

**`-proxy.username`**  
Example: `MyProxyUsername`. This option must be specified if your proxy requires authentication.

---

**`-proxy.password`**  
Example: `MyProxyPassword`. This option must be specified if your proxy requires authentication.


## Integration arguments

### TestOps integration arguments

**`-testOpsProjectId`**  
The ID of the TestOps Project that is associated with the test run.  
Example: `-testOpsProjectId=123456`.

**`-testOpsReleaseId`**  
The ID of the TestOps release that is associated with the test run.

**`--info -buildLabel=<text> -buildURL=<text>`**  
Pass the build's label and URL, which are displayed in Katalon TestOps.  
  >**Example**:
``` jsx
--info -buildLabel="Build 1" -buildURL="http://192.168.35.52:8080/job/katalon-demo/job/master/179/"
```


**`-testOpsBuildId`**  
From version 8.0.0, you can specify the build ID to update the Test Suite/Test Suite Collection report.  
  >**Example**: `-testOpsBuildId=24`

**`-testOps.baselineCollectionId=<CollectionId>`**  
From version 8.4.0 onwards, you can specify a baseline collection ID to which Katalon visual testing functionality compares newly captured images in your test runs.  
See: [Use TestOps Visual Testing](/katalon-platform/analyze/analytics/visual-testing/use-testops-visual-testing)  
  >**Example**: `-testOps.baselineCollectionId=1234`


**`-testOps.serverUrl=<URL>`**  
From version 8.4.0 onwards, you can specify the URL for TestOps server for authentication and integration.  
You can use this argument to work with different offerings of TestOps, including:
- Public Cloud and On-premise
- Private Instance
- Staging and Production

> **Note:** If `-testOps.serverUrl` is not specified, the default URL is `https://testops.katalon.io`.

**`-testOps.customField=<key1:value1, key2:value2>`**  
Assign pre-existent custom fields to the test run. Multiple custom fields can be assigned, separated by a comma. The command also creates a custom field and assigns it to the test run if the custom field was never created before.

**`-testOps.tag=<tag1, tag2>`**  
Assign pre-existent tags to the test run. Multiple tags can be assigned, separated by a comma. The command also creates a tag and assigns it to the test run if the tag was never created before. 

**`-testOps.enabled=true/false`**  
From version 10.1.0 onwards, you can enable or disable TestOps integration from the command line.  
This option overrides the settings in **Project Settings**.

**`-testOps.testRunName=<name>`**
From version 10.3.1 onwards, you can adjust the name of the test run uploaded to TestOps.

If not specified or the`testRunName` value has an invalid format, the original name of the executed TS and TSC will be used.

### TestCloud integration arguments

**`-testcloudEnvironmentId=<ID>`**  
The ID of the environment which corresponds to a combination of OS, browser type and browser version to execute (Available from 8.2.5 onwards).

:::important  
- To get the TestCloud environment ID, open Katalon Studio and use the command builder. For detailed information, follow this guide: [Generate Command with Command Builder](/katalon-studio/execute-tests/katalon-runtime-engine/get-started-with-katalon-runtime-engine#id_10).  
- This parameter already contains the information about browser type. Therefore, the `-browserType` parameter is not generated in this integration.
:::

**`-testcloudTunnel`**  
Allow the execution to be performed via a tunnel (Available from 8.2.5 onwards).

**`--testcloudMobileDeviceId=<device name>`** and **`-testcloudMobileId=<device name>`**  
When combined with `-browserType="TestCloud"`, these parameters set the execution environment to mobile browser on TestCloud. To generate the correct device name values, you should use Command Builder in Katalon Studio. See: [Run tests on mobile browsers in Katalon Runtime Engine](/katalon-testcloud/web-testing/mobile-browser-testing-with-testcloud#concept-6882).


### Kobiton integration arguments

**`--config -kobiton.authentication.username=<yourKobitonUsername> -kobiton.authentication.password=<yourPassword>`** <br/>
Passing Kobiton username and password.

---

**`--config -kobiton.authentication.serverUrl=<defaultKobitonServer> -kobiton.authentication.username=<yourKobitonUsername> -kobiton.authentication.apiKey=<yourKobitonAPIKey>`**  <br/>
Passing Kobiton Server URL, username, and API Key (Available in 7.8 and later).

---

**`-kobitonDeviceId=<yourKobitonDeviceId>`** <br/>
ID of the destination where the result is uploaded on it.


### Azure DevOps integration arguments

**`-adoPlanId=<testplanID>`**  
ID of the test plan used for submitting test run(s) (available from version 8.0.0).

---

 **`-adoTestRunName=<testRunName>`**  
From version 8.0.0, you can create test run(s) on ADO with the specified name.

---

**`--info -adoDefinitionID=<definitionID>`**  
From version 8.0.0, you can get the latest completed Build ID of the specified Definition ID and pass it to Test Run properties on ADO.

