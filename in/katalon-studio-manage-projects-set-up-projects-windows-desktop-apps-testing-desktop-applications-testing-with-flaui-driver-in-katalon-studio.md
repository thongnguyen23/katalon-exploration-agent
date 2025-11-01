---
title: Desktop applications testing with FlaUI driver in Katalon Studio
---

Starting from Katalon Studio 10.3.0, Windows Desktop app testing is available again as a beta feature. This version introduces a new built-in driver based on the FlaUI library, replacing WinAppDriver. The new driver supports spy, record, and execution of basic test cases—no separate installation required.

If your projects rely on Windows Desktop app testing, we recommend the following:
- Upgrade to Katalon Studio 10.3.0 or later to use the built-in FlaUI-based driver (beta).
- Stay on Katalon Studio 9.x to continue using the legacy WinAppDriver-based workflow.

## Auto-start driver on localhost

By default, if the Desktop Driver URL is left blank in **Project Settings > Desired Capabilities > Windows**, Katalon Studio will:

- Automatically start the built-in desktop driver on `localhost:4723` when you spy, record, or execute a Windows test.

- Automatically stop the driver once the task is complete.

<img src= "https://tw-cdn.katalon.com/katalon-studio/manage-projects/set-up-projects/windows-desktop-apps-testing/Winapp_testing_blank_driver_url.png" alt="Blank Desktop Driver URL" width="600" /> <br/>

:::note
The first time you use Desktop testing, driver initialization may take a few seconds due to Windows OS verification. Performance will improve in subsequent runs.

<img src= "https://tw-cdn.katalon.com/katalon-studio/manage-projects/set-up-projects/windows-desktop-apps-testing/KS_10.3.0_FlaUI_driver_delay_start.png" alt="FlaUI driver delayed start" width="600" />
:::

## Set Up Desktop Driver on a Remote Machine

If you need to test a Windows desktop application running on a remote machine, you must manually start the desktop driver by following these steps:

1. Locate the driver package
On the machine with Katalon Studio installed, go to the following path and copy the file FlaUI.WebDriver.zip to your remote machine: 

    ```jsx
    <Katalon Studio folder>\configuration\resources\extensions\FlaUIWebDriver\FlaUI.WebDriver.zip
    ```

2. Extract and start the driver. 
    1. On the remote machine, extract the contents of `FlaUI.WebDriver.zip`.
    2. Open a terminal or Command Prompt and run the following command (replace `<remote-machine-ip>` with the IP address of the remote machine, which you can get using `ipconfig`):

    ```jsx
    FlaUI.WebDriver.exe --urls=http://<remote-machine-ip>:4724 --environment Development --SessionCleanup:SchedulingIntervalSeconds=300

    ```

3. In your local Katalon Studio, go to **Project Settings > Desired Capabilities > Windows** and set the Desktop Driver URL to:

    ```jsx
    http://<remote-machine-ip>:4724
    ```

4. To verify if the driver is running, open a browser and navigate to:

    ```jsx
    http://<remote-machine-ip>:4724/status
    ```

    A successful response confirms that the driver is running and ready to accept commands.

    <img src= "https://tw-cdn.katalon.com/katalon-studio/manage-projects/set-up-projects/windows-desktop-apps-testing/Verify_status_FlaUI_driver.png" alt="FlaUI driver ready" width="600" />

## Known issues and limitations

The following are known limitations and issues in Katalon Studio 10.3.0 (Beta) for Windows Desktop app testing; we are actively working to improve support and will address these in future versions.

- Application closing may be delayed. It can take several seconds to close the application under test.
- Applications with multiple windows may cause focus issues. Examples include splash screens, loading bars, or multiple main windows. To maintain focus and ensure test stability:
    - Provide the Application Title in the Spy/Recorder screen.
    - Use the `Windows.startApplicationWithTitle()` keyword instead of `startApplication()`.
    - If your app includes windows with different titles, use a regex pattern, e.g., SplashScreen|MainWindow|LoadingBar.
- Some applications require administrator privileges Apps like 1Password need the driver to run with elevated permissions. In such cases:
    - Manually start the desktop driver as Administrator.
    - Copy the driver URL (e.g., `http://localhost:4723`) to **Project Settings > Desired Capabilities > Windows > Desktop Driver URL**.
- Dropdown lists and context menus cannot be inspected locally. These UI components are not capturable when the app runs on the same machine. To inspect them:
    - Run the application on a remote machine.
    - Use **Remote Inspect** to capture dropdown or context menu elements.