---
title: Set up Kubernetes test environments for TestOps (Legacy)
---
import useBaseUrl from '@docusaurus/useBaseUrl';
import Reusable from '@site/src/reusable/Reusable.mdx';

<Reusable />

This document demonstrates how to set up an AWS EKS Kubernetes test environment inside Katalon TestOps.

Kubernetes is an open-source platform that orchestrates container distribution for running test cases. It's like having an assistant to handle the containers for you.

See [Kubernetes Overview](https://kubernetes.io/docs/concepts/overview/) to learn more about what Kubernetes is and what it can do.

:::tip Requirements
- [AWS EKS Kubernetes cluster created](https://docs.aws.amazon.com/eks/latest/userguide/create-cluster.html)
- [IAM users created](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html)
:::

## Steps to set up a Kubernetes test environment

:::info Notes
The setup works best with Kubernetes version 1.25 or later.
:::

To set up a **Kubernetes test environment**, follow these steps:

1. Sign in to [Katalon TestOps](https://testops.katalon.io/login) and go to **TestOps Settings > Organization Setup**.

<img src="https://docs.katalon.com/5bed8b90-e28b-11ee-b3a4-0242c7a41fd4/TestOps_organization_setup.png" alt="Katalon TestOps Organization Setup page showing Test Environments option" width="300px" />

This shows the **Test Environments** page. It also lists the agents you have.

<img src="https://tw-cdn.katalon.com/katalon-platform/execute/k8s-create-test-env/TO_Decemeber_20_2023_Test_Environments_page.png" alt="TestOps Test Environments page listing available agents" width="500px" />

2. Click **Kubernetes** to switch to the **Kubernetes Test Environments** page.
3. Click the **Create Kubernetes Test Environment** button at the upper right corner.

<img src="https://tw-cdn.katalon.com/katalon-platform/execute/k8s-create-test-env/TO_Decemeber_20_2023_Create_Kubernetes_test_environment_button.png" alt="Button to create a Kubernetes Test Environment in TestOps." width="500px" />

4. Fill in the information for your agent. The images below are taken from a AWS EKS dashboard:
<img src="https://tw-cdn.katalon.com/katalon-platform/execute/k8s-create-test-env/TO-TDAP-2857-test-environment-Kubernetes-set-up-fields.png" alt="Form fields to configure a Kubernetes Test Environment in TestOps" width="500px" />
    - **Agent Name**: The display name for your agent
    - **URL**: The API server endpoint.
    - **Certificate Authority (CA)**: The content of your certificate authority. To get this information, go select your Kubernetes cluster in **Amazon Elastic Kubernetes Service > Clusters**, and it's listed in **Overview > Details**.
<img src="https://tw-cdn.katalon.com/katalon-platform/execute/k8s-create-test-env/TO-TDAP-2857-AWS-EKS-Kubernetes-certificate-authority.png" alt="Field in AWS EKS cluster to copy Kubernetes Certificate Authority content from" width="500px" />
    - **Namespace**: The namespace created for your **Kubernetes** cluster, can be viewed in **Overview > Resource > Resource Types > Cluster > Namespaces**
<img src="https://tw-cdn.katalon.com/katalon-platform/execute/k8s-create-test-env/TO-TDAP-2857-AWS-EKS-Kubernetes-namespace-details.png" alt="Namespace details from AWS EKS cluster" width="500px" />
    - **Authentication Type**: The authentication method to access **Kubernetes** environment (see more right below).
5. Click **Test Connection** to ensure your information is correct.
6. When the connection is correct, click **Create**.

## Authentication Type

The **Authentication Type** section has a dropdown menu with 3 options: **Username/Password**, **Token**, or **AWS EKS**.

### Username/Password
The username/password pair is a classic authentication method. If you've set up your Kubernetes cluster to have users, you can use this as the method of authentication.
<img src="https://tw-cdn.katalon.com/katalon-platform/execute/k8s-create-test-env/TO-TDAP-2857-auth-type-username-password.png" alt="Authentication Type dropdown showing Username and Password option selected" width="300px" />

For example, in **AWS EKS**, they are the **Identity and Access Management (IAM)** user's username and password, often labeled as **AWS Access Key ID** and **AWS Secret Access Key**. See [IAM users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users.html) for more details.

As the root user creates an **IAM** user, they must first set a **username**. This is the string to fill in the **Username** field.
<img src="https://tw-cdn.katalon.com/katalon-platform/execute/k8s-create-test-env/TO-TDAP-2857-AWS-EKS-IAM-user-create.png" alt="IAM user creation screen in AWS EKS" width="500px" />
As for the **Password** field, there are two scenarios:

1. **The root user chooses to set a custom password**: once the **IAM** user is created, use this password to fill in the “**Password**” field.
<img src="https://tw-cdn.katalon.com/katalon-platform/execute/k8s-create-test-env/TO-TDAP-2857-AWS-EKS-IAM-user-password-create.png" alt="IAM user password creation screen in AWS EKS" width="500px" />

2. **The root user chooses to auto-generate a password:** Once the **IAM** user is created, **EKS** asks the user to download credentials as a CSV file. Viewing the file shows both the Username and Password, like so:
<img src="https://tw-cdn.katalon.com/katalon-platform/execute/k8s-create-test-env/TO-TDAP-2857-sample-user-credentials-csv-file.png" alt="Example of AWS EKS IAM user credentials downloaded as a CSV file" width="500px" />

### Token

As an alternative to **Username/Password**, a **token** can be used as the authentication method.
<img src="https://tw-cdn.katalon.com/katalon-platform/execute/k8s-create-test-env/TO-TDAP-2857-auth-type-token.png" alt="Authentication Type dropdown showing Token option selected" width="300px" />
For Kubernetes accounts created via `kubectl`: See [kubectl Create Token](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_create/kubectl_create_token/) to learn more about creating a token using `kubectl`.

For **AWS EKS** users: See [Configure AWS CLI](https://docs.aws.amazon.com/cli/latest/reference/configure/) to configure a profile and see [Get a token for authentication with an Amazon EKS cluster](https://docs.aws.amazon.com/id_id/cli/latest/reference/eks/get-token.html) to see how to create an access token.
### AWS EKS

AWS EKS users can also choose this as the authentication method. The required fields are:
    - **Region**: The region where your Kubernetes cluster was created.
    - **Cluster**: The name of your cluster.
    - **Access Key**: The IAM account's access key.
    - **Private Access Key**: The IAM account's private access key.
<br></br>
<img src="https://tw-cdn.katalon.com/katalon-platform/execute/k8s-create-test-env/TO-TDAP-2857-auth-type-AWS-EKS.png" alt="Authentication Type dropdown showing AWS EKS option with fields for region, cluster, and access keys" width="300px" />

Both the **Access Key** and **Private Access Key** can be found as you configure an AWS EKS profile. See [Configure AWS CLI](https://docs.aws.amazon.com/cli/latest/reference/configure/) to configure a profile.