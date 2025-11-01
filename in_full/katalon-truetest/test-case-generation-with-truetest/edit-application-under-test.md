---
title: Edit application under test
---

This guide shows you how to edit an Application Under Test for TrueTest.

After setting up an Application Under Test (AUT), you can review and edit the configuration on every AUT. You can also flexibly select to generate test cases for specific AUT by pausing and resuming the tracking activity on the AUT.

Go to **Settings** > **TrueTest** to arrive at the **TrueTest Configuration** menu.

<img src="https://tw-cdn.katalon.com/truetest/truetest-configuration-page.png" width="1080" alt="TrueTest Configuration page" /> <br/>

1. To pause the tracking activity, click **Pause Tracking** > **Pause** to confirm. Refresh the page for the feature to take effect. TrueTest Agent will stop tracking user interaction data performed on the AUT.

   To resume data tracking on the AUT, click **Resume Tracking**.
    
2. To edit the AUT information, click *options* > **Edit**. You can edit the name and description for the AUT.
    
<img src="https://tw-cdn.katalon.com/truetest/truetest-edit-aut.png" width="500" alt="TrueTest Edit AUT dialog" />
    
- To edit an existing data tracking environment or test environment, click the corresponding settings icon (⚙️) > **Edit**. 
    <img src="https://tw-cdn.katalon.com/truetest/truetest-edit-tracking-and-test-environment.png" width="800" alt="Edit data tracking and test environment" /> <br/>

- For data tracking environment: you can edit the domain.
- For test environment: you can edit the environment name, login credentials, private tunnel use. You can also select the environment as the default environment used for generating test cases. There must be one default environment at a time, so you cannot toggle off the current default environment.
    
To remove the TrueTest integration on the AUT, select *options* > **Remove**. In the opened dialog, click **Remove** to confirm. Removing the integration means that all tracked data, user journey maps, and user flows will be permanently removed. However, the generated test cases for this AUT will remain.
    
You cannot remove an AUT if TrueTest is generating map or test cases from it.

<img src="https://tw-cdn.katalon.com/truetest/truetest-remove-aut.png" width="700" alt="Remove an AUT" />