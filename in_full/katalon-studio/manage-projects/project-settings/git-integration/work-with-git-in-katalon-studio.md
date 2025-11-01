---
title: Work with Git in Katalon Studio
---

Katalon Studio supports a seamless built-in Git integration. Once enabled, you can access all Git features at Katalon Studio's main toolbar.

This document shows you how to integrate and use Git in Katalon Studio.

## Enable Git integration

To enable Git integration, do as follows:

1. Go to **Katalon Studio** > **Preferences** > **Katalon** > **Git**.

Check the **Enable Git Integration** box.

<img src="https://docs.katalon.com/91f04880-22b2-11ed-9930-0242fe3e4a3f/ks-840-enable-git-integration.png" alt="Enable Git integration" width="600"/>

    
2. Click **Apply and Close**.

You can start using Git at Katalon Studio main toolbar.
    
<img src="https://docs.katalon.com/cbe831d0-750d-11ed-a602-0242cfbc79b5/ks-pe-git-enabled-1.png" alt="Git in main toolbar" width="300"/>
    
3. For advanced configurations, go to **Katalon Studio** > **Preferences** > **Team** > **Git**.

    <img src="https://docs.katalon.com/19435220-51ef-11ee-bc71-0242c7a41fd4/ks-900-git-preferences.png" alt="Git Team" width="400"/>    

## Clone a Git repository

After enabling Git Integration, you can clone an existing **Git repository** into a new directory on the local machine.

Do as follows:

1. In the main toolbar, click on the *Git* icon and select **Clone Project**.

You can also click on **Clone Git Project** in the **Tests Explorer** section.
    
<img src="https://docs.katalon.com/ca2d8980-750d-11ed-a602-0242cfbc79b5/ks-pe-clone-git-1.png" alt="" width="400"/>
    
2. The **Clone Git Repository** dialog appears.

### Connect to Git with HTTPS

To allow Katalon Studio to retrieve details of your repository, enter all required information and click **Next**.

<img src="https://docs.katalon.com/91f8d400-22b2-11ed-9930-0242fe3e4a3f/ks-840-clone-git-repo.png" alt="clone Git repository" width="600"/>

- **Repository URL**: the remote URL to your Git repository in HTTPS protocol. See Git documentation: [About remote repositories](https://help.github.com/en/articles/which-remote-url-should-i-use). To get HTTPS Protocol, go to your account on GitHub, GitLab, Bitbucket, or AzureDevOps, then go to the repository you want to clone to Katalon Studio. Click **Clone** and select **HTTPS**, then copy the **HTTPS Protocol**.
- **Authentication**:
    - **Username**: the username to access the Git repository.
    - **Password**: the personal access token to access the Git repository. To learn how to create a Git personal access token, you can refer to these documents:
        - GitHub: [Creating a personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token).
        - Azure Repos: To clone your repository from Azure DevOps, you need to click **Generate Git Credential**. Copy the **Username** and the generated **Password**, then paste them accordingly in the **Authentication** section in Katalon Studio. See: [Use personal access tokens](https://docs.microsoft.com/en-us/azure/devops/organizations/accounts/use-personal-access-tokens-to-authenticate?view=azure-devops&tabs=Windows).
            
            <img src="https://docs.katalon.com/e25f63a0-7acd-11ed-998d-0242cfbc79b5/generate-git-credential-azure.png" alt="" width="500"/>

        - Bitbucket: [HTTP access tokens](https://confluence.atlassian.com/bitbucketserver/personal-access-tokens-939515499.html).
        - GitLab: [Create a personal access token](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html#create-a-personal-access-token).

:::note
- When your Git credentials on GitHub change, you need to return to this step: [Clone a Git repository](https://docs.katalon.com/katalon-studio/manage-projects/project-settings/git-integration/work-with-git-in-katalon-studio#task-7549). 
- AWS CodeCommit is currently not supported in Katalon Studio.
:::

If you cannot access the repository after clicking **Next**, the connection might have issues with SSL verification. You can use the command below to bypass SSL verification (Not recommended):

```jsx
git config --global http.sslVerify
```

### Trust dialog on first open

When you successfully clone a project from a Git repository and open it for the first time, Katalon Studio will show a **"Trust and open this project"** dialog. This security prompt ensures you’re aware of the source before opening and potentially executing harmful scripts.

In this dialog, you can:

<img alt="Trust Dialog" src="https://tw-cdn.katalon.com/katalon-studio/manage-projects/trust-dialog-clone-project.png" width="500"/>


- Review the project path.
- Decide whether to trust this project or all projects inside the parent folder.

:::note
- Trusting a parent folder also trusts all projects directly inside it, including the one you're opening.
- However, if this project contains subfolders with separate project files, those sub-projects won’t be trusted automatically. You'll still see the trust dialog when opening them.
:::
- Click **Trust Project** to continue, or **Don't Open** if you’re unsure.

### Connect to Git with SSH Keys

To connect to Git with SSH keys, see [Git Integration Authentication with SSH Keys](https://docs.katalon.com/katalon-studio/manage-projects/project-settings/git-integration/git-integration-authentication-with-ssh-keys-in-katalon-studio).

:::info Known issues
- Currently, the Git integration in Katalon Studio supports SSH SHA-1, RSA-1024 and RSA-2048 private keys. Since GitHub has dropped the support for DSA and RSA SHA-1, you cannot integrate Katalon Studio with GitHub via SSH. You can still integrate Katalon Studio with other cloud-hosted services of Git, such as GitLab, BitBucket, and Microsoft Azure DevOps.
- The workaround for this issue is to use:
    - HTTPS protocol with GitHub personal access token. See [Connect to Git with HTTPS](https://docs.katalon.com/katalon-studio/manage-projects/project-settings/git-integration/work-with-git-in-katalon-studio#id_4).
    - Git with a terminal.
    - 3rd party tools.
:::

## Publish a local non-Git project as a Git repository

**Share Project** is a step to enable Git configuration for your new Katalon Studio project.

1. In the main toolbar, click the **Git icon > Share Project**.
    
<img src="https://docs.katalon.com/9208d990-22b2-11ed-9930-0242fe3e4a3f/ks-840-share-project.png" alt="share project" width="200"/>
    
2. Folder **.git** and file **.gitignore** are created within the Katalon project.
    
    **.gitignore** tells Git which files (or patterns) it should ignore. By default, **.gitignore** contains these files and patterns: `/bin /Libs .settings .classpath /.svn`
    
## Commit

The **Commit** option allows users to view all current changes and decide which changes are stored in the local branch. For more information on the commit command, refer to this Git document: [Git commit](https://git-scm.com/docs/git-commit).

Do as follows:

1. In the main toolbar, click on **Git** dropdown arrow > **Commit**.
    
    <img src="https://docs.katalon.com/2fd25360-3404-11ed-9930-0242fe3e4a3f/ks-850-pe-commit.png" alt="commit project" width="200"/>
    
2. The **Git Staging** tab is displayed for configuration.
    
    <img src="https://docs.katalon.com/9217cdb0-22b2-11ed-9930-0242fe3e4a3f/ks-840-commit.png" alt="Git staging" width="700"/>
    <br/>
       | **Field** | **Description** |
       | --- | --- |
       | Unstaged Changes | Changes which have been made. |
       | Staged Changes | Selected changes from Unstaged Changes. These changes are committed. |
3. From the **Unstaged Changes** list, select the changes to be committed, then right-click on them and select **Add To Index**. You can also drag and drop items from the Unstaged Changes to the Staged Changes. Selected changes are added to the **Staged Changes** list.
    
4. Enter your comments into the **Commit Message**.
5. Click on **Commit** to store your staged changes into the local branch.

## Manage Branches

### New Branch

To create a new branch, do as follows:

1. In the main toolbar, click on **Git** dropdown arrow > **Manage Branches** > **New Branch**.
    
    <img src="https://docs.katalon.com/d7ef6f60-3404-11ed-9930-0242fe3e4a3f/ks-pe-new-branch.png" alt="new branch" width="300"/>
    
2. The **Create Branch** dialog displays.
    
    <img src="https://docs.katalon.com/9212ebb0-22b2-11ed-9930-0242fe3e4a3f/ks-840-create-new-branch.png" alt="Create branch dialog" width="500"/>

    <br/>

    | **Field** | **Description** |
    | --- | --- |
    | Source | Select either remote or local branch, which is your source branch. <img alt=" " src="https://tw-cdn.katalon.com/katalon-studio/manage-projects/select source.png" width="500" />|
    | Branch name | The name to be used for the new branch|
    | Checkout new branch | Option to let Katalon Studio checkout that branch after created. |
    
3. Click **Finish** to create a new branch.

### Checkout Branch
    <br/>
The **Checkout Branch** option allows you to switch from one branch to another.

Do as follows:

1. **Manage Branches** > **Checkout Branch**.
    
<img src="https://docs.katalon.com/920ef410-22b2-11ed-9930-0242fe3e4a3f/ks-840-check-out-branch.png" alt="Checkout branch" width="300" />

1. The **Select Source** dialog displays.Select the local branch you want to check out to be the current branch. The branch with a **√** icon is your current local branch.
    
    <img src="https://docs.katalon.com/920dbb90-22b2-11ed-9930-0242fe3e4a3f/ks-840-select-source-branch.png" alt="select source brand" width="400"/>
    
2. Click **OK** when you finish.

### Delete Branch

To delete a branch, do as follows:

1. In the main toolbar, click on **Git** dropdown arrow > **Manage Branches** > **Delete Branch**.
    
    <img src="https://docs.katalon.com/920b71a0-22b2-11ed-9930-0242fe3e4a3f/ks-840-delete-branch.png" alt="delete branch" width="300"/>

    
2. In the **Delete Branch** dialog, both local and remote branches are displayed. Select a branch to delete.
    
    <img src="https://docs.katalon.com/91e2db00-22b2-11ed-9930-0242fe3e4a3f/ks-840-delete-branch-dialog.png" alt="delete branch dialog" width="400"/>
    
3. Click **OK** when you finish.

## Push

:::note
- Before doing any push, you need to commit your changes.
:::

You can use push command to upload the local branch to the remote branch. For more information on the push command, refer to this Git document: [Git push](https://git-scm.com/docs/git-push).

Do as follows:

1. In the main toolbar, click on **Git** dropdown arrow > **Push**.
    
    <img src="https://docs.katalon.com/f4f6f6e0-3405-11ed-9930-0242fe3e4a3f/ks-pe-850-push.png" alt="push changes" width="200"/>

    The **Push Branch master** dialog appears.
    
2. Choose from the **Remote branch** list which branch to be updated (All remote branches in your Git repository are listed here).Click **Next** after finishing selecting your remote branch.
    
    <img src="https://docs.katalon.com/91fa3390-22b2-11ed-9930-0242fe3e4a3f/ks-840-push-branch.png" alt="push branch" width="400"/>

:::note
- If you enter a name besides the listed branches, a new remote branch with that name is created accordingly.
:::
    
3. The **Push Confirmation** dialog appears with details of your commit.
4. Click **Finish** to push your commits to the remote repository.

## Pull

You can use the pull command to incorporate changes from a remote repository into the current branch. For more information on the pull command, refer to this Git document: [Git pull](https://git-scm.com/docs/git-pull).

Do as follows:

1. In the main toolbar, click on **Git** dropdown arrow > **Pull**.The **Pull** dialog appears.
    
    <img src="https://docs.katalon.com/d9edbaf0-3405-11ed-9930-0242fe3e4a3f/ks-pe-850-pull.png" alt="pull changes" width="200"/> 

2. Select the remote branch to be pulled into your local branch.
    
    <img src="https://docs.katalon.com/91ffd8e0-22b2-11ed-9930-0242fe3e4a3f/ks-840-remote-branch.png" alt="remote branch" width="400"/>

3. Click **Finish**.
4. The **Pull Result** dialog displays information about pulling requests on the selected branch.
    
    <img src="https://docs.katalon.com/91fe5240-22b2-11ed-9930-0242fe3e4a3f/ks-840-pull-result.png" alt="Pull result dialog" width="400"/>
    
5. Click **OK** when you finish.

## Fetch

You can retrieve all information about changes that have occurred in remote branches. For more information on the fetch command, refer to this Git document: [Git fetch](https://git-scm.com/docs/git-fetch).

Do as follows:

1. In the main toolbar, click on **Git** dropdown arrow > **Fetch**.
    
    <img src="https://docs.katalon.com/942348c0-3403-11ed-9930-0242fe3e4a3f/ks-pe-850-fetch.png" alt="Git Fetch" width="200"/>

2. The **Fetch Results** dialog appears.Remote branches, tags, and remote changes are fetched automatically.
    
    <img src="https://docs.katalon.com/91dd83d0-22b2-11ed-9930-0242fe3e4a3f/ks-840-fetch-result.png" alt="Fetch results dialog" width="400"/>

3. In the main toolbar, click **Show History**.
    
    <img src="https://docs.katalon.com/cfc42d40-3403-11ed-9930-0242fe3e4a3f/ks-pe-850-show-history.png" alt="Show history" width="200"/>
    
4. The **History** tab appears.Details regarding all the branches and tags you've just fetched are displayed.
    
    <img src="https://docs.katalon.com/921e0f40-22b2-11ed-9930-0242fe3e4a3f/ks-840-history.png" alt="History tab" width="900"/>


## Resolve Git conflicts using Katalon Studio

### Why do we have Git conflicts?

- In a source control system like Git, conflicts occur when two or more people make changes to the same file concurrently. The conflicts may appear at a member's local repository or Git remote repository.
- To avoid conflicts, the team must collaborate following several Git practices. For example, before **pushing** new source code to the Git remote repository, one must remember to **fetch** the latest version from Git remote repository, **resolve** any conflicts, and **merge** the code with the local version.

Below is an example of how to resolve Git conflicts using Katalon Studio:

- The chart below demonstrates how conflicts may occur when Tom and Emma are working on the same project. The conflicts occur when Tom and Emma try to push new code to the Git remote repository without updating the changes from each other.
    
<img src="https://docs.katalon.com/e238a1c0-7acd-11ed-998d-0242cfbc79b5/Git-conflict.png" alt="Git conflict" width="500" />
    

**Given situation:**

- Tom and Emma are working on the same test case in a test project. Emma added a new comment ("EMMA ADDED THIS COMMENT"), then committed and pushed the change to the Git remote repository.
    
  <img src="https://docs.katalon.com/e24d8950-7acd-11ed-998d-0242cfbc79b5/Git-conflict-2.png" alt="git conflict 2" width="600" />

    
- At almost the same time, Tom added a new comment ("TOM ADDED THIS COMMENT"), then committed and tried to push to the Git remote repository.
    
<img src="https://docs.katalon.com/e27c8890-7acd-11ed-998d-0242cfbc79b5/Resolve-Git-conflict-2.png" alt="resolve git conflict" width="600" />
    
- Unfortunately, since Emma had pushed the code before Tom, so the version of code in Git was different from the version of code in Tom's local repository. Therefore, Git rejected Tom's push action.

**Question: What should Tom do to push its change to the Git remote control?**

- First, Tom has to pull the code from the Git remote repository to his local machine.
    
<img src="https://docs.katalon.com/e2443a80-7acd-11ed-998d-0242cfbc79b5/Resolve-Git-conflict-3.png" alt="pull the code" width="600" />
    
- Obviously, Tom will see a message about the conflict:
    
<img src="https://docs.katalon.com/e2563be0-7acd-11ed-998d-0242cfbc79b5/Resolve-Git-conflict-4.png" alt="message about the conflict" width="400" />

- In the **Script** mode of the test case **TC2_Verify Successful Appointment** in Tom's Katalon Studio project, there are errors with indicators such as `<<<<<<<` (convention from Git). Let's look at the script more carefully:
    
<img src="https://docs.katalon.com/e2694eb0-7acd-11ed-998d-0242cfbc79b5/Resolve-Git-conflict-5.png" alt="script" width="600" />
    
- Recall that the comments were added by Tom and Emma, and the conflict is now on Tom's Katalon Studio project. Everything within `"<<<<<<< HEAD"` and `"======="` is the change from Tom. And, everything within `"======="` and `">>>>>>> branch 'master'…"` comes from Emma, which is currently in the Git remote repository.
- Now Tom has to decide which change is correct, or both are correct or wrong. Tom has to replace these lines of code with the correct ones. For example, "THIS IS THE CORRECT COMMENT":
    
<img src="https://docs.katalon.com/e2729d80-7acd-11ed-998d-0242cfbc79b5/Resolve-Git-conflict-6.png" alt="decide which change is correct" width="600" />
    
- After resolving the conflict, Tom is now able to commit and push the change to the Git remote repository.

### Best practices

Here are some suggested best practices for Katalon-related projects.

- Don’t commit logs or reports. Exclude generated files like `Reports/`, as they clutter history and cause conflicts.
- Version-control profiles and test data when needed. Include files from `Profiles/` and `Data Files/` if tests rely on them. These are usually easy to merge—just document changes in commit messages.
- Use Katalon Export/Import for enterprise sharing. Enterprise users can move test cases between projects using **Tools > Utility > Test Artifacts Sharing**, but rely on Git for daily work.
- Commit core test artifacts. Always include folders like `Test Cases/`, `Test Suites/`, `Object Repository/`, `Profiles/`, and `Keywords/` to ensure full project functionality.
- Keep your `.gitignore` clean. Ignore generated and IDE-specific files (`Reports/`, `bin/`, `.cache/`, etc.) to avoid clutter and merge issues.
- Review project setting changes. Changes to `Project/Settings/` (e.g., environment variables) should be limited and reviewed by the team.
- Use Git submodules only if truly needed. For shared libraries or keyword packages across projects, Git submodules can help. They centralize shared code but add complexity, so use them only when necessary.