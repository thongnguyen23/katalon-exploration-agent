---
title: Real-time TestCloud executions monitor
---

The Live TestCloud Execution Monitoring view allows you to track your test execution in real-time as they are running on remote devices or virtual machines. Whether you're working with automation or live testing, this feature provides the control and information you need to ensure software quality and speed up your development cycle. 

To access the **Execution** page and view your test metadata, follow these steps:

1. Log in to [TestCloud Web App](https://cloud.katalon.com/) site with your Katalon account.
2. In the left sidebar, select **Execution**. 
<img src="https://tw-cdn.katalon.com/katalon-testcloud/testcloud-live-testing/testcloud-execution-monitor/testcloud-web-app-select-execution.png" alt="Select Execution icon" width="200" />

3. In the **Execution List**, select the test execution you want to view in details.
<img src="https://tw-cdn.katalon.com/katalon-testcloud/testcloud-live-testing/testcloud-web-app-execution-list.png" width="800" alt="Select the test execution you want to view in details"/>

4. On the **Execution** page, you can view the following information:
<img src="https://tw-cdn.katalon.com/katalon-testcloud/testcloud-live-testing/testcloud-execution-monitor/testcloud-web-app-execution-monitor-view.png" alt="TestCloud Web App Execution view" width="1080" />

   - **List of tests**: 1 TestCloud Execution may have more than 1 Tests and will display at the left column
   - **Commands**: View Selenium or Appium commands with corresponding screenshot and  video timestamp for `takeScreenshot` keywords
      <img src="https://tw-cdn.katalon.com/katalon-testcloud/tcm-test-step-with-screenshot.png" width="600" alt="'Take Element Screenshot UI" />
   - **Logs**: Selenium (browser), Appium (mobile), and device logs
   - **Videos**: Real-time recordings from the `Open browser`, `Start app` steps to the `Close browser`, `Close app` steps, allows you to watch what happens with the web/app while the test is running.
   - **Test channels**: Executions from Katalon Studio and TestOps
   - **Test types**: Automated and live testing
   - **Configuration details**: Desired capabilities and response capabilities

:::caution Known limitations
- For Live testing, logs, videos, and environment fields will be empty.
- Executions from Linux machine: command details, logs and videos are currently unavailable.
- Real-time video is not available for test running on macOS machine. You can still view the video recording after the test is finished.
:::

