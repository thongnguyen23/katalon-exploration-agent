---
title: "Jenkins Integration"
---
import useBaseUrl from '@docusaurus/useBaseUrl';

:::tip Requirements 
- You have downloaded and installed [Jenkins](https://www.jenkins.io/download/).
- You have downloaded and installed [Katalon Runtime Engine](/katalon-studio/execute-tests/katalon-runtime-engine/get-started-with-katalon-runtime-engine).
:::

## Install the Katalon plugin on Jenkins
To run Katalon tests on Jenkins, you need to install the Katalon plugin on Jenkins. Do as follows:
1. Sign in to Jenkins and go to **Manage Jenkins > Manage Plugins**.
The **Plugin Manager** page appears.
    
<img src="https://docs.katalon.com/c1d37300-6af7-11ed-a602-0242cfbc79b5/jenkins-install-plugin.png" width="700" alt="Katalon Plugin Manager"/>

2. Click on the **Available** tab and search for the Katalon plugin.
plugin-manager.

3. Select the plugin and choose **Install without restart**.


## Configure Test Runs in Katalon TestOps
You must schedule test runs in Katalon TestOps before assigning this schedule to Jenkins for test executions. See: [Schedule Test Runs](/katalon-platform/execute/test-execution-with-testops/schedule-test-runs-in-testops).

:::info Note
Choose the **Save Configurations** option in the **Schedule Test Run** dialog to schedule Test Runs for Jenkins.
:::

## Execute Katalon TestOps plan on Jenkins
To execute the test run scheduled from Katalon TestOps on Jenkins, do as follows:
1. On Jenkins, create a new **Freestyle** project.

2. In **Build Steps**, add **Execute Katalon TestOps Plan**.

    <img src="https://docs.katalon.com/c1acb120-6af7-11ed-a602-0242cfbc79b5/jenkins-execute-kt-plan.png" width="700" alt="Add Execute Katalon TestOps Plan"/>

    The Execute Katalon TestOps Plan is added as a build step.

    <img src="https://docs.katalon.com/c19bc130-6af7-11ed-a602-0242cfbc79b5/jenkins-build-step.png" width="700" alt="The Execute Katalon TestOps Plan is added as a build step"/>

3. In **Server URL**, enter your TestOps server URL: `https://testops.katalon.io`.
4. In **Credentials**, add a secret text with the secret value is your Katalon API key. Add your credentials.
<img src="https://docs.katalon.com/c172dc70-6af7-11ed-a602-0242cfbc79b5/jenkins-add-credentials.png" width="700" alt="Add your Katalon API key and credentials"/>

5. After you added your Katalon API key, select it and click on **Test Connection**. If you are successfully connected, you can retrieve your projects and test plan.
<img src="https://docs.katalon.com/c1cc4710-6af7-11ed-a602-0242cfbc79b5/jenkins-test-connection.png" width="700" alt="Test Connection"/>

6. Choose your project, then choose the test plan that you want to execute.
7. Save your project, then click **Build Now**.

#### Result
Your test run is executed. You can view the execution log in Console Output.
After the test is completed, you can go back to Katalon TestOps to view and analyze your report.