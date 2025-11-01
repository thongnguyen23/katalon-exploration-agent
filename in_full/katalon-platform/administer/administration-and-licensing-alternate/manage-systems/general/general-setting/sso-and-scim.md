---
title: Custom Domain, SSO, and SCIM Configuration Guide
---
This document shows you how to configure Custom Domain, SSO, and SCIM.
## Custom Domain

A custom domain allows you to use your own branded URL (e.g., yourcompany.katalon.com). This improves your organization’s branding, makes login easier for users, and provides a more professional experience when accessing your system.

Please note:

- The **custom domain is managed directly by our Katalon team.**
- If a custom domain is not set, the system will automatically generate a **default domain** when required.
- Users **cannot configure or modify** the custom domain themselves.
- To request or update a custom domain, you must **contact Katalon Customer Support** at `support@katalon.com`.

---

## SSO and SCIM Overview

Katalon TestOps supports **SAML 2.0 Single Sign-On (SSO)** for authentication and **SCIM 2.0** for automated user provisioning, attribute synchronization, and deprovisioning.

Integrating with your Identity Provider (IdP) centralizes identity and access management.

> Strict SCIM Mode (recommended): When enabled, all user management is controlled by the IdP. TestOps becomes read-only for SCIM-managed attributes.
> 

---

## Requirements

- A supported IdP that provides SAML SSO and, for provisioning, **SCIM 2.0**, such as:
    - Okta
    - Microsoft Entra ID (Azure AD)
    - Any SCIM 2.0–compliant IdP
- You must configure SSO before enabling SCIM (required).
- You must have either the Account Admin or System Admin role. See this [document](/katalon-platform/administer/administration-and-licensing-alternate/about-administration#account-level-roles) for more details on roles.

---

## Configure Single Sign-On

To configure SSO in Katalon TestOps, first generate metadata by setting up an Identity Provider (IdP).

Katalon supports any IdP that conforms to the SAML 2.0 protocol. You can use one of the following platforms to configure your IdP:

- [Okta](https://www.okta.com/)
- [Auth0](https://auth0.com/)
- [Ping](https://www.pingidentity.com/en.html)

To set up the IdP, enter the values below in your IdP settings. Refer to your platform’s documentation for detailed steps.

:::info notes
- All values are **case-sensitive**.
- `{custom-domain}` is the Custom Domain you configured.
:::
- **Single Sign-On (SSO) URL:** `https://login.katalon.com/realms/katalon/broker/{custom-domain}/endpoint`
    - *Example:* If your Custom Domain is testops.katalon.io, the SSO URL is `https://login.katalon.com/realms/katalon/broker/testops/endpoint`.
- **SP Entity ID:** `https://login.katalon.com/realms/katalon/broker/{custom-domain}/endpoint`
    - *Example:* With Custom Domain testops.katalon.io, the SP Entity ID is `https://login.katalon.com/realms/katalon/broker/testops/endpoint`.
- **Attribute statement:** Email

IdP metadata is typically provided by the IdP as an XML file. Your metadata is automatically encrypted in the Katalon database.

**In Katalon TestOps**

1. Go to **Admin → System → General → General Setting → Custom Domain and SSO**.
2. Toggle **Enable SSO**.
3. Select one:
    - **Require SSO** – all users must authenticate through SSO.
    - **Optional SSO** – users may sign in using SSO or standard login.
4. Paste the IdP metadata XML into the **Metadata** field.
5. Click **Save Changes**.

<img src="https://tw-cdn.katalon.com/katalon-platform/admin/general-setting/general-setting.png" alt="General Setting UI" width="1080"/>

---

## Configure SCIM Provisioning

:::tip tip 
We recommend using **Okta** for SCIM. Our team has validated Okta and confirmed it works seamlessly with Katalon. While other IdPs may also work, they could introduce unexpected issues that may affect the stability of your integration.
:::
SCIM (System for Cross-domain Identity Management) is an open standard designed to simplify the automated provisioning and management of user identities across applications. It reduces manual effort and ensuring consistent access control.

### In TestOps

> 🚧 Important: SCIM requires SSO to be enabled first.
> 

You need to first set up SCIM within Katalon TestOps to use **SCIM Base URL** and **Bearer Token** inside Okta:

1. Go to **Admin → System → General → General Setting → Custom Domain and SSO**.
2. Ensure **SSO is enabled**.
3. Toggle **Enable SCIM Provisioning**.
4. TestOps generates:
    - **SCIM Base URL** (read-only, copyable)
    - **Bearer Token** (masked, regenerable, copyable)
5. Set **Attribute Management Authority**:
    - **IdP** – attributes are synced from the IdP and locked in TestOps.
    - **Katalon TestOps** – attributes are managed manually within TestOps.
    <details> 
        <summary> List of managed attributes </summary>
        - License Source
        - License Type
        - Full Name
        - Role
        - Username
        - Employee ID
        - Job Title
        - Department
    </details>
6. Click **Save Changes**.

<img src="https://tw-cdn.katalon.com/katalon-platform/admin/general-setting/general-setting.png" alt="General Setting UI" width="1080"/>


---

## Example: Okta SCIM Provisioning
  <iframe
    src="https://demo.arcade.software/FN1jTDGt1KrXYpkbkGsL?embed&embed_mobile=tab&embed_desktop=inline&show_copy_link=true"
    title="Share an Analytics Dashboard View by Email"
    frameborder="0"
    loading="lazy"
    webkitallowfullscreen
    mozallowfullscreen
    allowfullscreen
    allow="clipboard-write"
    style={{ width: "100%", height: "500px", border: "none" }}>
  </iframe>

### Step 1: Configure provisioning integration settings:

1. In your Okta application, go to **General → Provisioning → Select SCIM**.
2. The **Provisioning** tab appears.
3. Then configure the following:
    - **SCIM connector base URL** → copy from **SCIM Base URL field** in TestOps.
    <img src="https://tw-cdn.katalon.com/katalon-platform/admin/general-setting/scim-url.png" alt="SCIM Base URL field in TestOps" width="500" />
    - **Unique identifier field for users** → email.
    - **Supported actions** → check:
        - Import New Users and Profile Updates
        - Push New Users
        - Push Profile Updates
        - Push Group (currently this is not supported)
        - Import Groups (currently this is not supported)
        <img src="https://tw-cdn.katalon.com/katalon-platform/admin/general-setting/support-actions.png" alt="Supported Provisioning Actions in Okta"/>
    - **Authentication Mode** → HTTP Header.
    - **Bearer Token** → copy from **Bearer Token field** in TestOps.
        <img src="https://tw-cdn.katalon.com/katalon-platform/admin/general-setting/bearer-token.png" alt="Bearer Token field in TestOps" width="500"/>
4. Click **Test Connector Configuration**.

### Step 2: Configure provisioning To App settings
  <iframe
    src="https://demo.arcade.software/ilkM4KiA5KAqHtV3fZcX?embed&embed_mobile=tab&embed_desktop=inline&show_copy_link=true"
    title="Share an Analytics Dashboard View by Email"
    frameborder="0"
    loading="lazy"
    webkitallowfullscreen
    mozallowfullscreen
    allowfullscreen
    allow="clipboard-write"
    style={{ width: "100%", height: "500px", border: "none" }}>
  </iframe>

1. Go to **Provisioning → To App → Edit**.
2. Enable:
    - **Create Users**
    - **Update User Attributes**
    - **Deactivate Users**
3. Click **Save** to save changes

### Step 3: Configure Custom Attribute

1. In your Provisioning tab, scroll down to **Katalon Attribute Mappings.**
2. Click **Go to Profile Editors**.
<img src="https://tw-cdn.katalon.com/katalon-platform/admin/general-setting/attribute-mappings.png" alt="Attribute Mappings in Okta" width="600"/> <br/>

3. Then, click **Add Attribute**.
4. Fill out the **Add Attribute** dialog. You need to complete the following four (4) required fields. Please refer to the screenshot below to follow along.

    > **Note:** For **Namespace**, use this value: `urn:katalon:params:scim:schemas:extension:2.0:User`
    1. Account Roles:
    <img src="https://tw-cdn.katalon.com/katalon-platform/admin/general-setting/account_roles.png" alt="Account Roles - Attribute Mappings in Okta" width="500"/> <br/>
    2. Project roles:
    <img src="https://tw-cdn.katalon.com/katalon-platform/admin/general-setting/project_roles.png" alt="Project Roles - Attribute Mappings in Okta" width="500"/> <br/>
    3. Licenses:
    <img src="https://tw-cdn.katalon.com/katalon-platform/admin/general-setting/licenses.png" alt="Licenses - Attribute Mappings in Okta" width="500"/> <br/>
    4. Organization:
    <img src="https://tw-cdn.katalon.com/katalon-platform/admin/general-setting/org.png" alt="Licenses - Attribute Mappings in Okta" width="500"/> <br/>

### Step 4: Assign Users

1. Navigate to the app's **Assignments** tab.
2. Click **Assign > Assign to people**.
    <img src="https://tw-cdn.katalon.com/katalon-platform/admin/general-setting/assign-to-people.png" alt="Assign to People screen in Okta" width="600"/> <br/>
3. Select the user you want, then click **Assign** next to their name.
4. In the dialog, some fields (such as **Name** and **Email**) will be auto-filled..
    - You will also see custom fields (such as the one you created in Step 3). Choose the appropriate value based on your account and organization.
    <img src="https://tw-cdn.katalon.com/katalon-platform/admin/general-setting/example-fields.png" alt="Example Fields after mapping in Okta" width="500"/> <br/>
5. Click **Save and go back** when finished.
6. Repeat the steps to assign additional users. Once done, click **Done**.
    <video width="600" controls>
    <source src="https://tw-cdn.katalon.com/katalon-platform/admin/general-setting/assign-ok.mov" type="video/mp4" />
    </video>

## Custom Attribute Reference

| Data Type     | Variable Name          | External Namespace                                                | Required? | What to Enter                     | Allowed Values / Examples                                                                                                                                                                                                                                                                                                                                                       | Attribute Type |
| ------------- | ------------------ | -------------------------------------------------------- | --------- | --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- |
| String array  | **licenses**       | `urn:katalon:params:scim:schemas:extension:2.0:User`     | **Yes**   | **License Assignments** <br/> License_Source(Account/Org):License_Types  | Format: <br/> - `AC-<accountId>:<license-type>` <br/> - `OG-<orgId>:<license-type>` <br/><br/> License types: <br/> - `KSE` (Katalon Studio Enterprise) <br/> - `TO_FULL` (Katalon TestOps Full) <br/> - `KAM` (Katalon Account Manager) <br/> - `GUEST` (Katalon TestOps Guest) <br/><br/> Example: `["AC-1234:KSE", "OG-5678:KAM"]` <br/>           | personal       |
| String array  | **account\_roles** | `urn:katalon:params:scim:schemas:extension:2.0:User` | No        | Roles at the **account level**    | - `ACCOUNT_ADMIN`  <br/> - `SYSTEM_ADMIN`  <br/> - `USER` <br/><br/> Example: `["ACCOUNT_ADMIN", "USER"]` <br/><br/>*Default Value: `USER`*                                                                                                                                                                                                                                           | personal       |
| String array  | **project\_roles** | `urn:katalon:params:scim:schemas:extension:2.0:User`     | No        | Roles at the **project level**    | Format: <br/> - `ALL:<role>` → applies to all projects <br/> - `PJ-<projectId>:<role-value>` → project with prefix <br/> - `<projectId>:<role-value>` → project without prefix <br/><br/> Role values: <br/> - `PROJECT_ADMIN` <br/> - `TEST_LEAD` <br/> - `TESTER` <br/> - `MEMBER` <br/><br/> Example: `["ALL:TESTER", "PJ-1234:PROJECT_ADMIN"]` <br/> | personal       |
| Integer array | **organizations**  | `urn:katalon:params:scim:schemas:extension:2.0:User`     | No        | IDs of organizations              | Organization IDs are integers. <br/> Example: `[12345, 67890]` <br/>                                                                                                                                                                                                                                                                           | personal       |


**💡Tip:**
- To get Organization or Account ID: Go to Admin > Org > Organization Management:
    <img src="https://tw-cdn.katalon.com/katalon-platform/admin/general-setting/org-account-id.png" alt="Account & Org ID" width="500"/> <br/>
- To get the Project ID: Go to a specific project > Settings > General:
    <img src="https://tw-cdn.katalon.com/katalon-platform/admin/general-setting/project-id.png" alt="Project General Screen" width="500"/> <br/>
