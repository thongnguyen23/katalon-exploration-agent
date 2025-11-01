---
title: Katalon API Key in Katalon TestOps
---
import { TestOpsG2_TabNameValue, TestOpsG2_TabNameLabel, TestOpsG3_TabNameValue, TestOpsG3_TabNameLabel, MarjNote_Value } from "../../../../reusable-component";
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

<Tabs>
  <TabItem value={TestOpsG2_TabNameValue} label={TestOpsG2_TabNameLabel}>
    
You need to generate API Keys in Katalon TestOps in the following circumstances:

* When you want to integrate Katalon Studio with Katalon TestOps in console mode. See [Katalon Studio Integration](/katalon-studio/test-reports/upload-test-results-from-katalon-studio-to-katalon-testops-manually).

* When you want to integrate Katalon TestOps with other platforms such as [Jira](/katalon-platform/integrations/jira-integration/enable-testops---jira-integration-for-test-management) and [Jenkins](/katalon-platform/integrations/cicd-integrations/jenkins-integration/use-katalon-plugins-for-jenkins-integration/integrate-jenkins-with-testops).

* When you want to create a test environment such as [CircleCI](/katalon-platform/execute/test-execution-with-testops/set-up-circleci-test-environments-for-testops), [AWS EKS](/katalon-platform/execute/test-execution-with-testops/set-up-kubernetes-test-environments-for-testops), or [create a local test environment with an agent](/katalon-platform/execute/test-execution-with-testops/local-test-environments/create-a-local-test-environment-with-an-agent).

:::note 
  - In the command-line generator in Katalon Studio, the command-line options for API Keys, including `-apiKey=<Your_API_Key>` and `-apikey=<Your_API_Key>` are both accepted.
:::

---

## Generate a Katalon API Key

To create a new API Key, follow these steps:

1. Sign in to [Katalon TestOps](https://testops.katalon.io/login).

2. Click on the *Avatar* icon at the top right corner.

3. Go to **User Settings** > **Katalon API Key** or click on [this link](https://testops.katalon.io/user/apikey) to access to the **Katalon API Key** page directly.

   The **Katalon API Key** page appears.

   <br/>

   <img src="https://tw-cdn.katalon.com/katalon-testops/my-profile/API Key Step 3.png" alt="Katalon API Key page" width="1080"/>

4. Click **Create API Key** in the top right corner.

   The **Create API Key** box pops up.

5. Enter a name for your key, select the expiration period, then click **Create**.

   <br/>

   <img src="https://tw-cdn.katalon.com/katalon-testops/my-profile/API Key Step 5.png" alt="Create API Key dialog" width="500
   "/>

### Result

You have successfully added a new API key.

## Use a Katalon API Key

Follow these steps if you want to use your Katalon API Key:

1. Go to your **Katalon API Key** page.

   You can see a list of all API Keys here.

2. Click on the *Copy* icon of the API Key you want to use.

   <br/>

   <img src="https://tw-cdn.katalon.com/katalon-testops/my-profile/Use API Key Step 2.png" alt="Copy an API Key" width="1080"/>

3. Paste the copied API Key to the required platform.

## Remove a Katalon API Key

Follow these steps to remove a Katalon API Key:

1. Go to your **Katalon API Key** page.

   You can see a list of all API Keys here.

2. Click on the *Trash bin* icon of the API Key you want to remove.

   <br/>

   <img src="https://tw-cdn.katalon.com/katalon-testops/my-profile/Remove API Key Step 2.png" alt="Remove an API Key" width="1080"/>

3. Click **Delete** to confirm your action.

### Result

You have successfully removed a Katalon API Key.
  </TabItem>  

  <TabItem value={TestOpsG3_TabNameValue} label={TestOpsG3_TabNameLabel} default>

This section describes how to create and remove a Katalon API Key in Katalon TestOps.


## Create a Katalon API Key

1. Log in to Katalon TestOps.

2. Click on your **Profile** at the top right corner > **User Settings**. 

   The Personal Integration tab appears by default. 

3. Click on the **Katalon API Key** tab.

<img src="https://tw-cdn.katalon.com/katalon-testops/my-profile/API Key Page.png" alt="API Key Page" width="1080"/>

4. Click on **Create API Key** at the top right. 

   Input the following information:
   - **Key name**: The label of the API Key.
   - **Expiration**: Select the expiration period for the dropdown menu.
   - **Description**: (Optional) Add a description for the API Key.

5. Click **Create**.

### Result

You have successfully created a Katalon API Key.

---

## Remove a Katalon API Key

1. Go to your **Katalon API Key** page.

   You can see a list of all API Keys here.

2. Click on the **Delete** icon of the API Key you want to remove. It is represented by a trash bin icon.

<img src="https://tw-cdn.katalon.com/katalon-testops/my-profile/API Key Page Delete.png" alt="API Key Page Delete" width="1080"/>

3. Click on **Delete** to confirm your action in the pop-up dialog.

### Result

You have successfully removed a Katalon API Key.
  
  </TabItem>
</Tabs>