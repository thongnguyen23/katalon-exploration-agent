---
title: Use TestCloud in CI/CD pipelines
---

To execute tests in TestCloud environments with Katalon Runtime Engine, you only need a TestCloud subscription or trial; Katalon Runtime Engine license is not required. This also enables you to use TestCloud in any CI/CD pipelines configured with KRE.

### Test suite execution

To trigger test suite execution with TestCloud environments from KRE, you need to specify the following arguments:

<table style={{ width: '100%' }} className="table">
  <colgroup>
    <col style={{width: '20%' }} />
    <col style={{width: '40%' }} />
    <col style={{width: '10%' }} />
    <col style={{width: '30%' }} />
  </colgroup>
  <thead>
    <tr>
      <th>Command-line argument</th>
      <th>Description</th>
      <th>Data type</th>
      <th>Mandatory</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>-browserType="TestCloud"</code></td>
      <td>The browser type used for test suite execution. The "TestCloud" value means you are using TestCloud environments.</td>
      <td>String</td>
      <td>Required (for single test suite execution)</td>
    </tr>
    <tr>
      <td><code>-testcloudEnvironmentId</code></td>
      <td>The ID of the environment which corresponds to a combination of OS, browser type and browser version to execute. This ID can be generated with <a href="/katalon-studio/execute-tests/katalon-runtime-engine/get-started-with-katalon-runtime-engine#id_10">Command Builder</a>.</td>
      <td>String</td>
      <td>Required (for single test suite execution)</td>
    </tr>
    <tr>
      <td><code>-testcloudTunnel</code></td>
      <td>Allow the execution to be performed via TestCloud Tunnel.</td>
      <td>Boolean</td>
      <td>Optional</td>
    </tr>
    <tr>
      <td><code>-testcloudMobileDeviceId</code></td>
      <td>The unique ID of the TestCloud mobile device.</td>
      <td>String</td>
      <td>Required (for single test suite execution)</td>
    </tr>
    <tr>
      <td><code>-testcloudMobileId</code></td>
      <td>The ID of the TestCloud mobile OS version.</td>
      <td>String</td>
      <td>Required (for single test suite execution)</td>
    </tr>
        <tr>
      <td><code>-testcloudAppId</code></td>
      <td>The ID of the TestCloud application. KRE generates this command when the <strong>Override with application from TestCloud Application Repository</strong> option is selected.</td>
      <td>String</td>
      <td>Optional</td>
    </tr>
  </tbody>
</table>

:::caution Note
To execute API testing with TestCloud, make sure to specify `-browserType="TestCloud"` in your command. Additionally, set the `-testcloudEnvironmentId` to match a supported environment—for example, Desktop > Linux > Chrome (any version).
:::

#### Example

With GitHub Actions, to execute a test suite from KRE command to TestCloud environment, you can use the following workflow template:

```jsx 
name: CI
on:
  push:
    branches: [ master ]
  pull_request:
    branches: [ master ]

jobs:
  build:
    runs-on: windows-latest
    steps:
    - name: Checkout
      uses: actions/checkout@v3.0
    - name: Katalon Studio Github Action
      uses: katalon-studio/katalon-studio-github-action@v3.0
      with:
          version: '8.6.5'
          projectPath: '${{ github.workspace }}'
          args: '-noSplash -retry=0 -testSuiteCollectionPath="Test Suites/Sample Test Suite" -browserType="TestCloud" -testcloudEnvironmentId="256" -apiKey= ${{ secrets.API_KEY }} --config -webui.autoUpdateDrivers=true'
```

### Test suite collection execution

The TestCloud environments for individual test suites are already included in the test suite collection file. Therefore, the `browserType` and `testcloudEnvironmentId` arguments are not required. The test suites configured with TestCloud are automatically uploaded to TestCloud environments. See: [Manage test suite collections in Katalon Studio](/katalon-studio/manage-test-artifacts/manage-test-suite-collections-in-katalon-studio).

<img width="700" src="/ef89ff70-3041-11ee-99f7-0242c7a41fd4/KS_test_suite_collection_config.png" alt="Test suite collection execution"/>


