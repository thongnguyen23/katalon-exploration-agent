---
title: Filter test run list by build name in Katalon TestOps (Legacy)
---
:::tip requirements
You must execute tests from Katalon Runtime Engine.
:::
In Katalon TestOps, you can filter Test Runs by Build name to:

- Find and track the list of Test Runs linked with specific Build names.
- Monitor testing progress linked with those Builds.

## Add Build name in Command Line or Console Mode
1. Open Command prompt.
2. Find the Command Line option `--info -buildLabel` and edit it with your own info.

    You can find it in this list of [katalonc command options](/katalon-studio/execute-tests/katalon-runtime-engine/command-line-syntax-in-katalon-runtime-engine#general-options).

## Filter Test Runs by Build name in Katalon TestOps
1. Sign in to [Katalon TestOps](https://testops.katalon.io/login) and go to your Project.

2. Go to **Reports > Test Runs**.

3. Find the **Build Label** filter as shown below.

    By default, it will display All which means that all of your Test Runs in all Builds are listed.
    <img src="https://github.com/katalon-studio/docs-images/raw/master/katalon-analytics/docs/testops-may-filter-test-runs-list-by-build-name/build-label-button-2.png" alt="build name new UI" /> <br />

4. Click **Build Label**, then manually input the `-buildLabel` value that was previously configured in Katalon Studio.

    <img src="https://github.com/katalon-studio/docs-images/raw/master/katalon-analytics/docs/testops-may-filter-test-runs-list-by-build-name/build-label-box.png" alt="build name box" width="500" /> <br />


5. Click **Update**. You can now see the list of Test Runs associated with that `-buildLabel`.

    **Note**: The Build name will be displayed under the **Configuration** section on each Test Run.You can also go back to the default filter by clicking **Clear**.