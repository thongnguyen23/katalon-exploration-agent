---
title: Open a test project in Katalon Studio
---

To open an existing project in Katalon Studio, do as follows:

1. From the main menu, select **File** > **Open Project**.

<img alt="open project" width="600" src="https://tw-cdn.katalon.com/katalon-studio/manage-projects/file_open_project.png" />

2. Browse to the folder where your project is located and select it.

You can also quickly open recent test project by selecting from a list displayed under the **File** menu.

<img alt="browsing folder" src="https://tw-cdn.katalon.com/katalon-studio/manage-projects/browsing-folder.png" width="600" />

### Trust dialog on first open

When you open a project for the first time, Katalon Studio will show a **"Trust and open this project"** dialog. This security prompt ensures you’re aware of the source before opening and potentially executing harmful scripts.

New projects you create in Katalon Studio are trusted by default. If you move or rename the project folder, Katalon Studio prompts you to trust it again. This applies even to projects you've previously trusted.

<img alt="trust dialog popup" src="https://tw-cdn.katalon.com/katalon-studio/manage-projects/trust_dialog.png" width="600" />

In this dialog, you can:

- Review the project path.
- Decide whether to trust this project or all projects inside the parent folder.

:::note
- Trusting a parent folder also trusts all projects directly inside it, including the one you're opening.
- However, if this project contains subfolders with separate project files, those sub-projects won’t be trusted automatically. You'll still see the trust dialog when opening them.
:::

- Click **Trust Project** to continue, or **Don't Open** if you’re unsure.