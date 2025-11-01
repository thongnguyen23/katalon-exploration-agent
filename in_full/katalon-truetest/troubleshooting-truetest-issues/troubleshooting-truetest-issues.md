---
title: Troubleshooting TrueTest issues
hide_table_of_contents: false
toc_min_heading_level: 2
toc_max_heading_level: 2
---

This document lists out all the common issues and solutions you can encounter when setting up and using TrueTest. You can look for the troubleshooting with the corresponding error code.

---

## 02-03-0014

You are unable to generate user journey map.

### Cause 
This error happens when:
- the data collected by TrueTest agent is insufficient
- the created user sessions are too simple to generate a map. For example, if the application under test is just one static page, the user session created on that page will be simple.
- `Error Code 014`: user session data is insufficient as a result of session attribute-based filtering.


### Remedy
Create user sessions on dynamic pages, ensuring that the sessions are complex enough to generate a journey map.

---
## 04-06-0015 & 04-06-0025

TrueTest is unable to push generated test artifacts into the integrated Git repository.

### Cause
This error happens due to the following reasons:
- The Personal Access Token (PAT) of the Git repository is expired
- The Git URL format is not supported

### Remedy
- If the PAT has expired, you need to generate a new one and add it to the Script Repository settings in TestOps. See Configure a Git repository in TestOps.
- If the URL format is not supported, you need to use the format that TrueTest supports. The correct format should look like https://dev.azure.com and does not include your username.
  
---
## 04-06-0035

Failed to clone the script repository due to incorrect credentials.

When configuring script repository in TestOps, you can input email or Git username in the Username field. However, TrueTest Agent cannot commit test cases to a script repository with an email form username.
<img src="https://docs.katalon.com/b809be90-10b7-11ee-bd0e-0242c7a41fd4/ATG_troubleshooting_git_username.png" width="400" alt="Troubleshooting Git username" />

### Remedy
To work with TrueTest, you need to edit the integrated script repository with a Git username instead of email form username.

---
## 04-06-0045
Personal Access Token is not granted with WRITE permission.

TrueTest Agent failed to generate user journey map.

### Cause
The agent failed to generate test cases because it was not able to commit the tests to the repository.

To generate and store test cases, TrueTest Agent requires Write permission to the configured Git repository. When setting up test environment for the agent, you need to link a Git script repository with Write permission.
<img src="https://docs.katalon.com/188f34f0-d8fc-11ed-ae00-0242cfbc79b5/ATG_link_project.png" width="600" alt="Link project" />

If your Git script repository is not configured with Write permission, you need to reconfigure the script repository's personal access token with Write permission. See: [Configure a Git repository in TestOps](/katalon-platform/organize/configure-a-git-repository-in-testops).

The following are some specific examples of Write permission configuration for different Git providers.

### Remedy
- GitHub personal access token: you need to provide the `repo:status` scope. See: [GitHub available scope](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/scopes-for-oauth-apps#available-scopes).
- GitLab personal access token: you need to assign the `write_repository` scope. See: [GitLab personal access token scopes](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html#personal-access-token-scopes).
- Atlassian Bitbucket Repository Access Token: you need to provide the `repository:write` permission. See: [Bitbucket Repository Access Token permissions](https://support.atlassian.com/bitbucket-cloud/docs/repository-access-token-permissions/).
- Azure DevOps access token: you need to provide the `vso.code_write` scope. See: [Azure DevOps access token scopes](https://learn.microsoft.com/en-us/azure/devops/integrate/get-started/authentication/oauth?view=azure-devops#scopes).
- AWS CodeCommit Git credentials: you need to create an IAM policy with write access to repository. See: [AWS managed policies for CodeCommit](https://docs.aws.amazon.com/codecommit/latest/userguide/security-iam-awsmanpol.html).

---
## 04-06-0055

Failed to push test artifacts to a protected git branch.

The TrueTest agent cannot push and commit generated test artifacts to a protected git branch although the Personal Access Token has been granted with WRITE permission.

### Remedy
Set the git branch to non-protected or select a different non-protected git branch.

---
## TrueTest Agent installation errors
If you do not see any network activity in the previous steps, please open the Developer Tools' Console tab and check for errors.

### Content Security Policy error
If you see an error *“Refused to load the script 'https://static.katalon.com/libs/traffic-agent/v1/traffic-agent.min.js' because it violates the following Content Security Policy directive:…”*, it means your application applies a security policy to block third-party content.

### Remedy
You need to update your Content Security Policy (CSP) configurations to allow the content to be downloaded from [katalon.com](https://katalon.com). This can be achieved by adding `*.katalon.com` or `static.katalon.com` into the CSP configuration:
- `script-src 'unsafe-inline' *.katalon.com`;
- `worker-src 'self' blob:`;
- `connect-src 'self' *.katalon.com`;

---
### 403 Forbidden
A 403 Forbidden error in the Console means the current page's URL does not match any patterns in the data tracking domains configured for the TrueTest Agent.

### Remedy
Please follow these guidelines to update the tracking domains accordingly: [Edit application under test](/katalon-platform/create-tests/test-case-generation-with-truetest/edit-application-under-test).
